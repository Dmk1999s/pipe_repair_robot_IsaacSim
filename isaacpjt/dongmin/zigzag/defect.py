"""[Isaac 3.11] 결함 · 비드 · 마개 — 수리 연출의 3종 프림.

`repair_demo.py` 가 확립한 **프림 가시성 전환** 방식을 지그재그 코스로 옮긴 것이다.
프림 셋이 하는 일이 서로 다르다는 점이 핵심이다:

    결함 `/World/Defect/hole`   시각. 관벽 조각에 ø28 관통 구멍. 처음에 **보임**
    비드 `/World/Defect/bead`   시각. 그 구멍을 메운 용접 비드. 처음에 **숨김**
    마개 `/World/LeakPlug`      물리+시각. 배관에서 **지운 삼각형 그대로**.
                                처음에 숨김 + 충돌 끔

배관 충돌 메시에서 개구 자리의 삼각형을 실제로 지우므로 **진짜 관통 구멍**이
생긴다. 시뮬 시작 뒤에는 삼각 메시를 다시 cook 할 수 없어 구멍을 되메울 수
없으므로, 지운 조각을 그대로 복제해 두었다가 용접 성공 시 **보이기·충돌만 켠다.**

## repair_demo.py 와 다른 점

`repair_demo` 는 개구를 `(x, y)` 평면 거리로 골랐다. 그 식은 **개구 축이 ±Z
(천장/바닥)이고 관 축이 X 인 직관**에서만 맞아서, 반쪽을 안 자르면 천장에도
구멍이 뚫리는 부작용이 있었다(주석에 실측이 남아 있다: 제거 98개 = 바닥 49 +
천장 49).

여기서는 `course.wall_uv_many()` 로 삼각형마다 **(진행거리 s, 시계각, 반경)**
을 구해서 고른다. 시계각이 위/아래를 이미 구분하므로 반쪽을 자를 필요가 없고,
곡선 구간에서도 그대로 성립한다.

🚨 다만 결함 **STL 조각**은 직관 전용이다 — 축 X 인 곧은 관벽 조각이라 굽힘에
   놓으면 벽에서 뜬다. `install()` 이 직선 구간인지 검사한다.
"""

import math
import struct
from pathlib import Path

import numpy as np
from pxr import Gf, PhysxSchema, Sdf, UsdGeom, UsdPhysics

import course

MM = 0.001
MESHES = Path(__file__).resolve().parent / "meshes"

DEFECT_ROOT = "/World/Defect"
PLUG_PATH = "/World/LeakPlug"

COLOR_HOLE = (0.05, 0.05, 0.06)      # 구멍 — 거의 검정
COLOR_BEAD = (0.85, 0.55, 0.20)      # 용접 비드 — 주황


def load_stl(path):
    """이진 STL → (정점 m, 삼각형 색인). son `repair_demo.load_stl` 과 같다."""
    data = Path(path).read_bytes()
    n = struct.unpack("<I", data[80:84])[0]
    a = np.frombuffer(data[84:84 + n * 50], dtype=np.uint8).reshape(n, 50)
    tri = a[:, 12:48].copy().view("<f4").reshape(n * 3, 3).astype(np.float64)
    pts, inv = np.unique(np.round(tri, 5), axis=0, return_inverse=True)
    return pts * MM, inv.reshape(n, 3)


def patch_transform(s, clock_deg):
    """STL 조각 프레임 → 월드. 조각은 '축 X, 패치가 +Z, 원점은 관 축 위' 다.

    코스 프레임 (원점 o, 접선 t, 왼쪽 l, 위 u) 에 대해
        X_local → t
        Y_local → l·cosθ − u·sinθ
        Z_local → u·cosθ + l·sinθ        ← 패치가 향하는 쪽 = 시계각 θ
    시계각 규약(+Z 에서 왼쪽으로)은 `course.wall_uv` 와 같다.
    """
    o, t, l, u = course.frame_at(s)
    th = math.radians(clock_deg)
    r0 = t
    r1 = l * math.cos(th) - u * math.sin(th)
    r2 = u * math.cos(th) + l * math.sin(th)
    m = Gf.Matrix4d(
        float(r0[0]), float(r0[1]), float(r0[2]), 0.0,
        float(r1[0]), float(r1[1]), float(r1[2]), 0.0,
        float(r2[0]), float(r2[1]), float(r2[2]), 0.0,
        float(o[0]), float(o[1]), float(o[2]), 1.0)
    return m


def _make_mesh(stage, path, stl, color, xform):
    pts, idx = load_stl(stl)
    mesh = UsdGeom.Mesh.Define(stage, path)
    mesh.CreatePointsAttr([Gf.Vec3f(*p) for p in pts])
    mesh.CreateFaceVertexCountsAttr([3] * len(idx))
    mesh.CreateFaceVertexIndicesAttr(idx.reshape(-1).tolist())
    mesh.CreateExtentAttr([Gf.Vec3f(*pts.min(0)), Gf.Vec3f(*pts.max(0))])
    mesh.CreateSubdivisionSchemeAttr("none")
    mesh.CreateDisplayColorAttr([Gf.Vec3f(*color)])
    UsdGeom.Xformable(mesh).AddTransformOp().Set(xform)
    return mesh


class Defect:
    """결함 한 곳의 프림 묶음과 상태."""

    def __init__(self, stage, s, clock_deg, dia_m,
                 defect_mesh, bead_mesh, bead_op, plug_prim, plug_coll,
                 n_removed, n_tris):
        self.stage = stage
        self.s = s
        self.clock_deg = clock_deg
        self.dia = dia_m
        self.defect_mesh = defect_mesh
        self.bead_mesh = bead_mesh
        self._bead_op = bead_op
        self.plug_prim = plug_prim
        self._plug_coll = plug_coll
        self.n_removed = n_removed
        self.n_tris = n_tris
        self.repaired = False
        # 결함 중심의 월드 좌표 — **관벽 위 점**이다.
        # 🚨 프림 원점을 쓰면 안 된다. STL 조각의 원점은 **관 축 위**라
        #    `wpos(defect_mesh)` 는 벽이 아니라 축 위 점을 준다
        #    (repair_demo 가 이걸로 거짓 판정을 낸 기록이 있다).
        self.world = course.wall_point(s, clock_deg)

    def uv(self):
        """결함 중심의 (진행거리, 시계각). 정렬 오차는 이 좌표에서 잰다."""
        return self.s, self.clock_deg

    def align_error_mm(self, tip_world):
        """토치 끝과 결함의 **관벽을 펼친 평면에서의** 어긋남(mm).

        🚨 3차원 직선거리를 쓰면 안 된다 — 용접 간극이 그대로 오차로 잡혀
           허용치를 항상 넘는다. 재려는 것은 "토치가 결함을 겨누고 있는가" 다.
        """
        s_t, c_t, _ = course.wall_uv(tip_world)
        d_ax = (s_t - self.s) * 1000.0
        d_ci = course.PIPE_IR * math.radians(
            (c_t - self.clock_deg + 180.0) % 360.0 - 180.0) * 1000.0
        return math.hypot(d_ax, d_ci), d_ax, d_ci

    def swap(self, tip_world, aligned):
        """용접 결과를 반영한다. 반환: 실제로 수리됐는가.

        🔑 **비드는 정렬 성공 여부와 무관하게 켠다.** 다만 자리는 결함이 아니라
           **토치가 실제로 있던 곳**이다. 정렬이 빗나가면 비드가 엉뚱한 데
           남고 결함은 그대로 뚫려 있어야 검증이 산다(설계 7.2).
        """
        s_t, c_t, _ = course.wall_uv(tip_world)
        self._bead_op.Set(patch_transform(s_t, c_t))
        UsdGeom.Imageable(self.bead_mesh).MakeVisible()
        if not aligned:
            return False
        UsdGeom.Imageable(self.defect_mesh).MakeInvisible()
        self._plug_coll.CreateCollisionEnabledAttr(True)
        UsdGeom.Imageable(self.plug_prim).MakeVisible()
        self.repaired = True
        return True


def install(stage, s, clock_deg, dia_mm=28.0, pipe_path="/World/Pipe",
            contact_offset=0.0005):
    """결함·비드·마개를 설치하고 배관에 실제 관통 개구를 뚫는다."""
    if course.in_bend(s):
        raise SystemExit(
            f"[중단] 결함을 굽힘 구간(s={s * 1000:.0f}mm)에 두려 한다. "
            f"결함 STL 은 **직관 전용**(축 X 인 곧은 관벽 조각)이라 굽힘에 놓으면 "
            f"조각이 벽에서 뜬다. 직선 구간에 둘 것 — "
            f"{[(round(a * 1000), round(b * 1000)) for a, b in zip(course.SEG_START_S, list(course.SEG_START_S[1:]) + [course.S_TOTAL]) if not course.in_bend((a + b) / 2)]}")

    dia = dia_mm * MM
    xf = patch_transform(s, clock_deg)

    tag = f"{dia_mm:g}".replace(".", "p")
    UsdGeom.Xform.Define(stage, DEFECT_ROOT)
    defect_mesh = _make_mesh(stage, f"{DEFECT_ROOT}/hole",
                             MESHES / f"defect_hole{tag}_w56.stl",
                             COLOR_HOLE, xf)
    bead_mesh = _make_mesh(stage, f"{DEFECT_ROOT}/bead",
                           MESHES / f"bead_hole{tag}_w56.stl",
                           COLOR_BEAD, xf)
    bead_op = UsdGeom.Xformable(bead_mesh).GetOrderedXformOps()[0]
    UsdGeom.Imageable(bead_mesh).MakeInvisible()

    # ── 배관 충돌 메시에 진짜 구멍 ──────────────────────────────────
    pipe_mesh = UsdGeom.Mesh(stage.GetPrimAtPath(f"{pipe_path}/geom"))
    if not pipe_mesh:
        raise SystemExit(f"[중단] 배관 메시를 못 찾았다: {pipe_path}/geom")
    pts = np.array(pipe_mesh.GetPointsAttr().Get())
    idx = np.array(pipe_mesh.GetFaceVertexIndicesAttr().Get()).reshape(-1, 3)
    cent = pts[idx].mean(axis=1)

    s_c, clock_c, r_c = course.wall_uv_many(cent)
    d_ax = s_c - s
    # 원주 거리는 **삼각형 자신의 반경**으로 잰다. 안쪽(50)과 바깥(56)이
    # 같은 각폭이면 호 길이가 다르므로, 내반경으로 일괄 계산하면 바깥면
    # 구멍이 좁아져 관통이 매끈하지 않다.
    d_ci = r_c * np.radians((clock_c - clock_deg + 180.0) % 360.0 - 180.0)
    hole = np.hypot(d_ax, d_ci) < dia / 2.0

    n_removed = int(hole.sum())
    if n_removed == 0:
        raise SystemExit(f"[중단] 개구에 걸리는 삼각형이 없다 "
                         f"(s={s * 1000:.0f}mm, 시계각 {clock_deg}°)")
    kept = idx[~hole]
    pipe_mesh.GetFaceVertexIndicesAttr().Set(kept.reshape(-1).tolist())
    pipe_mesh.GetFaceVertexCountsAttr().Set([3] * len(kept))

    # ── 마개 — 지운 삼각형 그대로 ───────────────────────────────────
    # 🔑 원통이나 평면 뚜껑으로 막으면 **곡률이 달라 Depth 가 안 맞는다**
    #    (repair_demo 실측: 구멍 테두리에서 +3.5mm 파임으로 읽혔다).
    #    잘라낸 조각을 그대로 되살리면 원본과 같은 곡률·반경이라 정확히 맞는다.
    tris = idx[hole]
    used, remap = np.unique(tris, return_inverse=True)
    plug = UsdGeom.Mesh.Define(stage, PLUG_PATH)
    pp = np.asarray(pts[used], dtype=float)
    plug.CreatePointsAttr([Gf.Vec3f(float(a), float(b), float(c)) for a, b, c in pp])
    plug.CreateFaceVertexCountsAttr([3] * len(tris))
    plug.CreateFaceVertexIndicesAttr(remap.reshape(-1).tolist())
    plug.CreateExtentAttr([Gf.Vec3f(*[float(v) for v in pp.min(0)]),
                           Gf.Vec3f(*[float(v) for v in pp.max(0)])])
    plug.CreateSubdivisionSchemeAttr("none")
    plug.CreateDisplayColorAttr([Gf.Vec3f(*COLOR_BEAD)])
    plug_prim = plug.GetPrim()
    # 🚨 **강체로 만들지 않는다.** 강체의 자세는 PhysX 가 쥐고 있어서 시뮬 시작
    #    뒤 USD 변환이 안 먹고, 키네마틱이면 Isaac 이 reset 때
    #    `setLinearVelocity: Body must be non-kinematic!` 로 실패한다.
    #    → **옮기지 않는다.** 잘라낸 자리에 그대로 두고 보이기·충돌만 켠다.
    plug_coll = UsdPhysics.CollisionAPI.Apply(plug_prim)
    plug_coll.CreateCollisionEnabledAttr(False)
    UsdPhysics.MeshCollisionAPI.Apply(plug_prim).CreateApproximationAttr("none")
    px = PhysxSchema.PhysxCollisionAPI.Apply(plug_prim)
    px.CreateContactOffsetAttr(contact_offset)
    px.CreateRestOffsetAttr(0.0)
    UsdGeom.Imageable(plug_prim).MakeInvisible()

    return Defect(stage, s, clock_deg, dia, defect_mesh, bead_mesh, bead_op,
                  plug_prim, plug_coll, n_removed, len(idx))
