"""[Isaac 3.11] 지그재그 훅 R100 씬 조립 — 배관 + 로봇 + DOF 색인.

`zigzag_demo.py` 와 프로브가 같이 쓴다. 조립 규칙을 두 곳에 두면 반드시 어긋나므로
**여기 한 곳**에만 둔다.

## 배관과 로봇을 붙이는 방식이 서로 다르다 — 이유가 있다

    배관  AddReference    defaultPrim 이 단일 Xform(TestPipeZigzagHook) 이라
                          참조로 깨끗하게 얹힌다. `repair_demo.py` 와 같다.
    로봇  Sdf.CopySpec    🚨 defaultPrim 이 `World` 라 **PhysicsScene 을 안고
                          있다.** 참조로 붙이면 스테이지에 PhysicsScene 이 2개가
                          된다. 그렇다고 /World/Robot 만 참조하면 머티리얼
                          바인딩(`</World/Looks/RedBodyMat>` 절대경로 20개)이
                          참조 범위 밖을 가리켜 전부 끊긴다.
                          → /World/Robot 과 /World/Looks 를 **같은 경로로 복사**
                            한다. 절대경로가 그대로 유효하고 PhysicsScene 은 안
                            따라온다. son 로봇(defaultPrim=PipeRobotBellows,
                            PhysicsScene 없음)과 사정이 달라서 생긴 차이다.

## 🚨 DOF 이름 — 이 로봇의 가장 고약한 함정

서스펜션과 휠 조인트가 **같은 프림 이름**을 쓴다:

    /World/Robot/SpringJoints/RearBody_A0   (prismatic, 서스펜션)
    /World/Robot/DriveJoints/RearBody_A0    (revolute,  휠)

Isaac 은 충돌하는 두 번째 이름 뒤에 `_0` 을 붙여 구분한다. 스테이지 순서상
SpringJoints 가 먼저라서 실측(probe_robot.py) 결과는 이렇다:

    RearBody_A0      → **서스펜션** (prismatic, 리밋 −4~+6mm)
    RearBody_A0_0    → **휠**       (revolute, 무한회전)

즉 `_0` 이 붙은 쪽이 휠이다. son 로봇은 `_piston_`/`_wheel_` 로 이름이 달라
이 문제가 없었다 — `repair_demo.py` 의 색인 코드를 그대로 베끼면 안 된다.
이름 규칙에만 기대면 조용히 뒤바뀔 수 있으므로 `resolve_dofs()` 가 안착 후
**물리로 교차검증**한다(서스펜션은 리밋 안, 휠은 자유회전).
"""

import math
import re

import numpy as np
from pxr import Gf, PhysxSchema, Sdf, UsdGeom, UsdLux, UsdPhysics, UsdShade

import course

WS = "/home/ubuntu/cobot3_ws"
ROBOT_USDA = f"{WS}/robot_from_bot_welder_art_v2.usda"
# 🔑 배관은 코스가 고른다 (`ZIGZAG_COURSE=long|hook`). long 쪽은 `build_pipe.py`
#    가 `course._SEGS` 에서 생성한 것이라 둘이 어긋날 수가 없다.
PIPE_USDA = f"{WS}/{course.PIPE_USDA_NAME}"

ROBOT = "/World/Robot"
PIPE = "/World/Pipe"

# ── 로봇 실측 (robot_from_bot_welder_art_v2.usda) ────────────────────
WHEEL_R = 0.008              # 휠 반경
WHEEL_MOUNT_R = 0.040        # 휠 중심의 로봇 축 기준 반경
WHEEL_TIP_R = WHEEL_MOUNT_R + WHEEL_R       # 0.048 — 무부하 시 휠 바깥면 반경
# 🚨 밀착 판정 기준은 **휠 중심**이 앉는 반경이다. 휠 바깥면이 관 내벽(50mm)에
#    닿으면 중심은 50 − 8 = 42mm 에 온다. `WHEEL_TIP_R − WHEEL_R` (= 40mm) 로
#    쓰면 밀착인데도 전부 "뜸" 으로 나온다 — 실제로 한 번 그렇게 찍혔다.
WHEEL_SEAT_R = 0.050 - WHEEL_R              # 0.042
WHEEL_TRACK_DEG = (90.0, 210.0, 330.0)      # 휠 궤도 시계각 3줄
WHEEL_W = 0.012              # 휠 폭 → 궤도가 차지하는 각폭 ±8.6° @r40
BODY_R = 0.025               # 본체 코어 콜라이더 반경
BODY_LEN = 0.064             # 본체 코어 길이
ROBOT_HALF_LEN = 0.094       # 원점에서 본체 끝까지 (Rear −94 / Front +94)
# 서스펜션 예압: stiffness 3000 N/m × (target 12mm − limit 6mm) = 18N, maxForce 60N
PRELOAD_N = 3000.0 * (0.012 - 0.006)
N_LEG = 12

_WHEEL_RE = re.compile(r"^(Rear|Front)Body_[AB][012]_0$")
_SUSP_RE = re.compile(r"^(Rear|Front)Body_[AB][012]$")
_BELLOWS_RE = re.compile(r"^(J0|J1|J2|J3|J_front)(:[12])?$")


def build_stage(world, *, contact_offset, flooded, glass=False):
    """배관·로봇·조명을 올린다. 반환: stage."""
    stage = world.stage
    UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
    UsdGeom.Xform.Define(stage, "/World")

    # 조명 — 한 점으로는 안 된다. 코스를 따라 약 0.45m 마다 하나씩 둔다.
    # 🚨 고정 4개로 박아 두면 안 된다 — 코스를 늘렸을 때(long, 5.05m) 뒷구간이
    #    통째로 어두워 카메라 검출이 죽는다. 훑기는 "밝은 벽에 둘러싸인 어두운
    #    덩어리" 로 구멍을 찾으므로 조명이 곧 검출 성능이다.
    _n_light = max(4, int(round(course.S_TOTAL / 0.45)))
    for k in range(_n_light):
        s = course.S_TOTAL * (k + 0.5) / _n_light
        x, y, _, _ = course.point_at(s)
        lt = UsdLux.SphereLight.Define(stage, f"/World/Light{k}")
        lt.CreateIntensityAttr(2.0e6)
        lt.CreateRadiusAttr(0.04)
        UsdGeom.Xformable(lt).AddTranslateOp().Set(Gf.Vec3d(x, y, 0.30))

    stage.DefinePrim(PIPE, "Xform").GetReferences().AddReference(PIPE_USDA)

    _layer = Sdf.Layer.FindOrOpen(ROBOT_USDA)
    if _layer is None:
        raise SystemExit(f"[중단] 로봇 레이어를 못 열었다: {ROBOT_USDA}")
    root = stage.GetRootLayer()
    for p in ("/World/Looks", "/World/Robot"):
        if not Sdf.CopySpec(_layer, Sdf.Path(p), root, Sdf.Path(p)):
            raise SystemExit(f"[중단] CopySpec 실패: {p}")

    apply_pipe_material(stage, flooded=flooded, glass=glass)
    apply_contact_offset(stage, contact_offset)
    return stage


def apply_pipe_material(stage, *, flooded, glass=False):
    """관 상태로 마찰을 정한다 (설계 v3 §12.3).

    🚨 배관 usda 에 박힌 값은 0.9/0.8 로 **설계값과 다르다.** 그대로 두면 만관
       조건인데 건식보다도 잘 붙는 꼴이 된다. 물리 재질을 따로 바인딩해 덮는다.
       `materialPurpose="physics"` 라 표시 재질과 충돌하지 않는다.
    """
    fs, fd = (0.30, 0.25) if flooded else (0.40, 0.35)
    mat = UsdShade.Material.Define(stage, "/World/PipePhysMat")
    api = UsdPhysics.MaterialAPI.Apply(mat.GetPrim())
    api.CreateStaticFrictionAttr(fs)
    api.CreateDynamicFrictionAttr(fd)
    api.CreateRestitutionAttr(0.0)

    gl = None
    if glass:
        gl = UsdShade.Material.Define(stage, "/World/Glass")
        sh = UsdShade.Shader.Define(stage, "/World/Glass/Shader")
        sh.CreateIdAttr("UsdPreviewSurface")
        sh.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set(
            Gf.Vec3f(0.55, 0.58, 0.60))
        sh.CreateInput("opacity", Sdf.ValueTypeNames.Float).Set(0.25)
        sh.CreateInput("roughness", Sdf.ValueTypeNames.Float).Set(0.4)
        gl.CreateSurfaceOutput().ConnectToSource(sh.ConnectableAPI(), "surface")

    n = 0
    for p in stage.Traverse():
        if str(p.GetPath()).startswith(PIPE + "/") and p.IsA(UsdGeom.Mesh):
            UsdShade.MaterialBindingAPI.Apply(p).Bind(
                mat, bindingStrength=UsdShade.Tokens.weakerThanDescendants,
                materialPurpose="physics")
            if gl is not None:
                UsdShade.MaterialBindingAPI.Apply(p).Bind(
                    gl, bindingStrength=UsdShade.Tokens.strongerThanDescendants)
            n += 1
    return fs, fd, n


def apply_contact_offset(stage, offset):
    """감지 밴드를 스테이지 전체에 건다.

    🚨 **로봇이 올라온 뒤에 부를 것.** 배관만 있을 때 부르면 정작 넓혀야 할
       휠 콜라이더 12개가 빠진다(`repair_demo.py` 가 같은 실수를 기록해 뒀다).
    """
    n = n_wheel = 0
    for p in stage.Traverse():
        if p.HasAPI(UsdPhysics.CollisionAPI) or p.IsA(UsdGeom.Mesh):
            px = PhysxSchema.PhysxCollisionAPI.Apply(p)
            px.CreateContactOffsetAttr(offset)
            px.CreateRestOffsetAttr(0.0)
            n += 1
            if p.GetPath().pathString.endswith("_Wheel/WheelCollider"):
                n_wheel += 1
    return n, n_wheel


BELLOWS_D6 = ("J0", "J1", "J3", "J_front")


def relax_bellows(stage, deg):
    """벨로우즈 D6 4개의 스윙 리밋(rotY·rotZ)을 ±deg 로 바꾼다.

    🚨 **로봇 usda 를 고치지 않는다.** 스테이지에 올린 뒤 속성만 덮어쓰므로
       원본 파일은 그대로다. R100 통과 가능성을 가르는 값이라 실험적으로
       움직일 수 있어야 해서 따로 뺐다.

    기본값 ±20° 로는 이 코스를 못 지난다(실측): 관절 4개가 전부 리밋에 붙은
    상태에서 본체 사이 꺾임이 25° 밖에 안 나오는데, R100 굽힘은 본체 중심간
    124mm 에 대해 약 71° 를 요구한다.
    """
    n = 0
    for nm in BELLOWS_D6:
        p = stage.GetPrimAtPath(f"{ROBOT}/BellowsJoints/{nm}")
        if not p.IsValid():
            continue
        for ax in ("rotY", "rotZ"):
            for side, val in (("low", -float(deg)), ("high", float(deg))):
                a = p.GetAttribute(f"limit:{ax}:physics:{side}")
                if a:
                    a.Set(val)
                else:
                    p.CreateAttribute(f"limit:{ax}:physics:{side}",
                                      Sdf.ValueTypeNames.Float).Set(val)
        n += 1
    return n


def place_robot(stage, s0):
    """로봇을 코스 진행거리 s0 자리에 **접선 방향으로** 놓는다.

    로봇 장축은 로컬 +X 이고(Rear −62 / Front +62), 관 입구 접선도 +X 라
    s0 가 첫 직선 안이면 회전이 항등이다. 굽힘 구간에서 시작할 수도 있으므로
    일반적으로 접선에 맞춰 Rz 를 준다.
    """
    org, tan, left, up = course.frame_at(s0)
    yaw = math.degrees(math.atan2(tan[1], tan[0]))
    xf = UsdGeom.Xformable(stage.GetPrimAtPath(ROBOT))
    xf.ClearXformOpOrder()
    m = Gf.Matrix4d(1.0)
    m.SetRotate(Gf.Rotation(Gf.Vec3d(0, 0, 1), yaw))
    m.SetTranslateOnly(Gf.Vec3d(float(org[0]), float(org[1]), float(org[2])))
    xf.AddTransformOp().Set(m)
    return yaw


def resolve_dofs(dof_names):
    """DOF 이름 → 용도별 인덱스. 위 머리말의 `_0` 함정을 여기서 흡수한다."""
    names = list(dof_names)
    idx = {
        "wheel": [k for k, n in enumerate(names) if _WHEEL_RE.match(n)],
        "susp": [k for k, n in enumerate(names) if _SUSP_RE.match(n)],
        "bellows": [k for k, n in enumerate(names) if _BELLOWS_RE.match(n)],
    }
    # 🚨 벨로우즈 9개 중 **J2 만 prismatic** 이다(단위 m). 나머지 8개는 rad 다.
    #    섞어서 max(abs()) 를 하면 단위가 다른 값을 비교하게 된다. 각도만 따로 둔다.
    idx["bellows_rot"] = [k for k, n in enumerate(names)
                          if _BELLOWS_RE.match(n) and n != "J2"]
    idx["bellows_rot_names"] = [n for n in names
                                if _BELLOWS_RE.match(n) and n != "J2"]
    idx["ring"] = names.index("RingRotate") if "RingRotate" in names else None
    idx["torch"] = names.index("TorchExtend") if "TorchExtend" in names else None

    problems = []
    if len(idx["wheel"]) != N_LEG:
        problems.append(f"휠 {len(idx['wheel'])}/{N_LEG}")
    if len(idx["susp"]) != N_LEG:
        problems.append(f"서스펜션 {len(idx['susp'])}/{N_LEG}")
    if len(idx["bellows"]) != 9:
        problems.append(f"벨로우즈 {len(idx['bellows'])}/9")
    if idx["ring"] is None or idx["torch"] is None:
        problems.append("토치 조인트 없음")
    if problems:
        raise SystemExit(
            "[중단] DOF 색인 실패: " + ", ".join(problems)
            + f"\n         받은 이름 {len(names)}개: {names}")
    return idx


def verify_dof_roles(art, idx, dof_names):
    """🚨 이름 규칙만 믿지 않는다 — **물리로 교차검증**한다.

    `_0` 이 휠이라는 것은 스테이지 프림 순서에서 나온 결과라, usda 안의 조인트
    순서가 바뀌면 소리 없이 뒤집힌다. 그러면 서스펜션에 속도 명령이 가고 휠은
    리밋에 걸려 로봇이 그냥 안 움직인다 — 원인을 찾기 매우 어려운 고장이다.
    안착 직후 상태로 두 가지를 본다:
        서스펜션 후보 → 값이 전부 리밋 [−4, +6]mm 안이어야 한다
        휠 후보       → prismatic 리밋이 없으므로 그 범위를 벗어나도 정상
    반환: (문제 목록). 비어 있으면 통과.
    """
    pos = np.asarray(art.get_joint_positions())
    bad = []
    susp = pos[idx["susp"]]
    if not np.all((susp >= -0.0045) & (susp <= 0.0065)):
        bad.append(f"서스펜션 후보가 리밋(−4~+6mm)을 벗어났다: "
                   f"{np.round(susp * 1000, 2).tolist()}mm "
                   f"— 휠과 뒤바뀐 것으로 의심된다")
    if np.allclose(pos[idx["wheel"]], 0.0, atol=1e-9):
        bad.append("휠 후보가 전부 정확히 0 이다 — 고정된 관절일 수 있다")
    return bad


class Progress:
    """로봇의 코스 진행도. **본체 두 개의 중점**을 쓴다.

    🚨 `art.get_world_pose()` 를 쓰면 안 된다. 그건 PhysX 가 고른 **루트 링크**
       자세인데, 이 로봇은 벨로우즈 Link1 이 루트로 잡힌다(실측: 원점 x=200mm 에
       놓았는데 194mm 가 나왔다 = Link1 의 로컬 −6mm). 굽힘에서 벨로우즈가
       접히면 그 오차가 커진다.
    """

    def __init__(self, stage):
        self._xc = UsdGeom.XformCache()
        self._rear = stage.GetPrimAtPath(f"{ROBOT}/RearBody")
        self._front = stage.GetPrimAtPath(f"{ROBOT}/FrontBody")

    def _w(self, prim):
        t = self._xc.GetLocalToWorldTransform(prim).ExtractTranslation()
        return np.array([float(t[0]), float(t[1]), float(t[2])])

    def read(self):
        """반환: (s, 중점, 후방중심, 전방중심)."""
        self._xc.Clear()
        r, f = self._w(self._rear), self._w(self._front)
        mid = 0.5 * (r + f)
        s, _, _, _, _, _ = course.project(mid[0], mid[1])
        return float(s), mid, r, f
