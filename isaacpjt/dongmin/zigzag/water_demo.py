"""[Isaac 3.11] 지그재그 5m 배관 물 채우기 — **로봇 없이 물만 본다.**

`zigzag_demo.py` 에서 로봇·카메라·용접을 다 덜어내고 물만 남긴 것이다. 목적은
하나 — **5m 코스에 물이 제대로 앉는지 눈으로 확인**하는 것. 로봇이 없으니
주파·정렬·검출 변수가 전부 빠져서, 물이 이상하면 물 탓인 게 확실해진다.

## 🚨 양 끝이 뚫려 있다 — 마개가 필수다

코스는 훅 두 개짜리 열린 관이라(s=0 입구, s=5049.56mm 훅 끝) 그냥 채우면
**양쪽으로 다 쏟아진다.** 여기서는 정적 박스 콜라이더로 두 끝을 막는다.
로봇이 없으므로 "로봇은 통과시키고 물만 막는" 복잡한 처리가 필요 없다 —
`zigzag_demo` 에 물을 얹을 때는 그때 다시 풀 문제다.

## 값은 새로 정하지 않는다

입자 설정은 사용자 동결값을 그대로 쓴다(PCO 8 / fluid_rest 4.8 / 간격 9 /
입자-강체 contact 4 · rest 2.5). 조립은 `pipe/water_sim.py` 공용부,
수위 수식은 `pipe/water_model.py` 가 담당한다. 여기서 정하는 것은
**"어디에 물이 있는가"** 뿐이다 — 그게 코스마다 다른 유일한 부분이라
water_sim 머리말이 데모 몫으로 남겨 둔 것이다.

## 연산량

충수율 1/2 (기본) 기준 코스 전체를 채우면 **약 22,000 입자**다. repair_demo
(0.92m, 4,987개)의 4.4배다. 로봇이 없어 관절·접촉 계산이 빠지지만 입자 자체가
무겁다. 먼저 `--s1 1.0` 으로 앞 1m 만 채워 보고 늘릴 것.

    ISO_PASSES=0   isosurface 를 끈다 → 물이 구슬로 보이지만 제일 빠르다
    WATER_FILL=0.3 얕게 채운다 → 입자 수가 비례해서 준다

실행:
    PYTHONUNBUFFERED=1 isaac_python water_demo.py --hold            # 스트리밍으로 본다
    isaac_python water_demo.py --s1 1.0 --hold                      # 앞 1m 만 (빠른 확인)
    ISAAC_STREAM=0 isaac_python water_demo.py --headless --steps 2000   # 로그만

🚨 스트리밍으로 볼 때 `--headless` 를 주지 말 것 — `world.step(render=False)`
   가 되어 서버는 멀쩡한데 화면만 검게 멈춘다.
"""

import argparse
import math
import os
import sys
from pathlib import Path

ap = argparse.ArgumentParser(description="지그재그 배관 물 채우기 (로봇 없음)")
ap.add_argument("--headless", action="store_true")
ap.add_argument("--hold", action="store_true", help="끝나고 창을 열어 둔다")
ap.add_argument("--steps", type=int, default=3000)
ap.add_argument("--s0", type=float, default=0.0, help="채우기 시작 s (m)")
ap.add_argument("--s1", type=float, default=None, help="채우기 끝 s (m). 기본 = 코스 끝")
ap.add_argument("--opaque", action="store_true", help="관을 불투명하게 (기본은 유리)")
A = ap.parse_args()

from isaacsim import SimulationApp                        # noqa: E402

simulation_app = SimulationApp({"headless": A.headless})

import numpy as np                                        # noqa: E402
from isaacsim.core.api import World                       # noqa: E402
from pxr import Gf, PhysxSchema, UsdGeom, UsdLux, UsdPhysics   # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))

import course                                             # noqa: E402
import scene                                              # noqa: E402
import water_model                                        # noqa: E402
import water_sim                                          # noqa: E402

PHYSICS_HZ = float(os.environ.get("PHYSICS_HZ", 240))

# ── 물 (동결값 — 새로 정하지 않는다) ────────────────────────────────
W_SPACING, W_PCO, W_FLUID_REST = 0.009, 0.008, 0.0048
W_R_MAX = 0.045              # 채움 반경 상한 (관 내반경 50 안쪽)
WATER_FILL = float(os.environ.get("WATER_FILL", 0.5))
W_LEVEL_Z = water_model.level_z(WATER_FILL, course.PIPE_IR)
ISO_PASSES = int(os.environ.get("ISO_PASSES", 2))
ANISO = float(os.environ.get("ANISO", 1.0))
# 🚨 입자는 GPU 물리 전용이고, GPU 접촉 생성 허용치보다 작은 contactOffset 을
#    주면 접촉이 아예 안 생겨 물이 관을 뚫고 샌다(repair_demo 실측 기록).
CONTACT_OFFSET = 0.02

S0 = max(0.0, A.s0)
S1 = min(course.S_TOTAL, A.s1 if A.s1 is not None else course.S_TOTAL)
if S1 <= S0:
    raise SystemExit(f"[중단] 채움 구간이 비었다 (s0={S0} s1={S1})")

world = World(stage_units_in_meters=1.0,
              physics_dt=1.0 / PHYSICS_HZ, rendering_dt=1.0 / 60.0)
_pc = world.get_physics_context()
_pc.enable_gpu_dynamics(True)          # 입자는 GPU 전용
_pc.set_broadphase_type("GPU")
stage = world.stage
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
UsdGeom.Xform.Define(stage, "/World")

print("=" * 78)
print(course.describe())
print("=" * 78)

# ── 조명 ────────────────────────────────────────────────────────────
# 유리관을 밖에서 들여다보는 구도라 위에서 넓게 깐다.
_n_light = max(4, int(round(course.S_TOTAL / 0.45)))
for k in range(_n_light):
    s = course.S_TOTAL * (k + 0.5) / _n_light
    x, y, _, _ = course.point_at(s)
    lt = UsdLux.SphereLight.Define(stage, f"/World/Light{k}")
    lt.CreateIntensityAttr(2.0e6)
    lt.CreateRadiusAttr(0.05)
    UsdGeom.Xformable(lt).AddTranslateOp().Set(Gf.Vec3d(x, y, 0.45))
_dome = UsdLux.DomeLight.Define(stage, "/World/Dome")
_dome.CreateIntensityAttr(400.0)

# ── 배관 ────────────────────────────────────────────────────────────
stage.DefinePrim(scene.PIPE, "Xform").GetReferences().AddReference(scene.PIPE_USDA)
_fs, _fd, _n_mesh = scene.apply_pipe_material(
    stage, flooded=True, glass=not A.opaque)
print(f"[준비] 배관 {course.PIPE_USDA_NAME} — 메시 {_n_mesh}개, "
      f"마찰 {_fs}/{_fd}, 표시 {'불투명' if A.opaque else '반투명(유리)'}")


# ── 끝 마개 ─────────────────────────────────────────────────────────
def end_cap(path, s, outward):
    """관 끝을 막는 정적 박스 콜라이더.

    코스 프레임(접선·왼쪽·위)에 맞춰 세운다 — 끝이 축에 나란하지 않은 코스로
    바꿔도 그대로 맞는다. 두께 8mm, 단면 ±60mm 로 외반경 56mm 를 덮는다.
    """
    x, y, tx, ty = course.point_at(s)
    half_t = 0.004
    cx, cy = x + tx * outward * half_t, y + ty * outward * half_t
    m = Gf.Matrix4d(1.0)
    m.SetRow(0, Gf.Vec4d(tx * 2 * half_t, ty * 2 * half_t, 0.0, 0.0))
    m.SetRow(1, Gf.Vec4d(-ty * 0.12, tx * 0.12, 0.0, 0.0))
    m.SetRow(2, Gf.Vec4d(0.0, 0.0, 0.12, 0.0))
    m.SetRow(3, Gf.Vec4d(cx, cy, 0.0, 1.0))
    cube = UsdGeom.Cube.Define(stage, path)
    cube.CreateSizeAttr(1.0)
    UsdGeom.Xformable(cube).AddTransformOp().Set(m)
    p = cube.GetPrim()
    UsdPhysics.CollisionAPI.Apply(p)
    UsdGeom.Imageable(p).MakeInvisible()      # 물만 막고 시야는 안 가린다
    return p


end_cap("/World/CapIn", 0.0, -1.0)
end_cap("/World/CapOut", course.S_TOTAL, +1.0)
print(f"[준비] 끝 마개 2개 — s=0 과 s={course.S_TOTAL * 1000:.0f}mm. "
      f"양 끝이 열린 관이라 없으면 물이 다 쏟아진다")

_n_off, _ = scene.apply_contact_offset(stage, CONTACT_OFFSET)
print(f"[준비] contactOffset {CONTACT_OFFSET * 1000:.0f}mm, 프림 {_n_off}개 "
      f"(GPU 물리 하한 — 이보다 작으면 물이 관을 뚫는다)")

# ── 물 ──────────────────────────────────────────────────────────────
_psys = water_sim.make_water_system(
    stage, "/World/ParticleSystem", pco=W_PCO, fluid_rest=W_FLUID_REST,
    contact=0.004, rest=0.0025, iso_passes=ISO_PASSES, aniso=ANISO)
water_sim.bind_water_materials(stage, _psys)

def radial_axial(px, py, pz):
    """월드 점 → (중심선 수직거리, 축방향 잔차). 둘 다 벡터.

    🚨 `course.project` 의 `d` 를 그대로 반경으로 쓰면 안 된다. project 는 코스
       **밖** 점을 끝점으로 물려서(clamp) 돌려주므로, 관 입구 뒤 30mm 에 있는
       점도 "중심선에서 30mm" 로 나온다 — 관 안으로 오인된다.
       실측으로 걸렸다: 격자 씨딩에서 입구 뒤 x −9~−45mm 의 **126개가 관 밖에
       뿌려졌고**, 누수처럼 보이는데 개수가 늘지 않아 정체가 드러났다.
    → 물린 지점에서 접선 방향으로 얼마나 벗어났는지(축방향 잔차)를 따로 낸다.
      코스 안이면 0 이고, 밖이면 그만큼 튀어나온다. 수직거리는 그 성분을 뺀 뒤 잰다.
    """
    _, _, tx, ty, cx, cy = course.project(px, py)
    vx, vy = px - cx, py - cy
    ax = vx * tx + vy * ty                       # 축방향 잔차 (안이면 0)
    ex, ey = vx - ax * tx, vy - ax * ty           # 수직 성분만 남긴다
    return np.hypot(np.hypot(ex, ey), pz), ax


# 🔑 **"어디에 물이 있는가" 는 코스마다 다르다** — 여기가 그 부분이다.
#    코스 bbox 를 덮는 격자를 깔고 ① 중심선에서 W_R_MAX 안 ② 수면 아래
#    ③ 채움 구간 [S0, S1] 안 ④ **코스 밖으로 안 삐져나감** 인 점만 남긴다.
#    굽힘도 course 가 알아서 푼다.
_pad = W_R_MAX + W_SPACING
_xs = np.arange(-_pad, 1.20 + _pad, W_SPACING)
_ys = np.arange(-1.10 - _pad, 0.60 + _pad, W_SPACING)
_zs = np.arange(-W_R_MAX, W_LEVEL_Z + 1e-9, W_SPACING)
_X, _Y, _Z = np.meshgrid(_xs, _ys, _zs, indexing="ij")
_s, _, _, _, _, _ = course.project(_X.ravel(), _Y.ravel())
_r, _ax = radial_axial(_X.ravel(), _Y.ravel(), _Z.ravel())
_in = ((_r <= W_R_MAX) & (np.abs(_ax) < 1e-6)      # ← 물린 점 제외
       & (_s >= S0) & (_s <= S1))
_pos = [Gf.Vec3f(float(a), float(b), float(c))
        for a, b, c in zip(_X.ravel()[_in], _Y.ravel()[_in], _Z.ravel()[_in])]
_vel = [Gf.Vec3f(0.0, 0.0, 0.0)] * len(_pos)
n_particles = len(_pos)
if n_particles == 0:
    raise SystemExit("[중단] 입자가 0개다 — 채움 구간·수위를 확인할 것")

inst = water_sim.spawn_water(stage, "/World/WaterParticles", _pos, _vel,
                             _psys, W_FLUID_REST)
_vol = n_particles * W_SPACING ** 3 * 1000.0
print(f"[준비] 물 입자 {n_particles:,}개 — 수위 z{W_LEVEL_Z * 1000:+.0f}mm "
      f"(충수 {WATER_FILL:.0%}), 채움 구간 s {S0 * 1000:.0f}~{S1 * 1000:.0f}mm "
      f"({(S1 - S0) * 1000:.0f}mm)")
print(f"       대표 부피 약 {_vol:.1f} L  (입자 1개 = {W_SPACING ** 3 * 1e6:.2f} mL)")
print(f"       손잡이  ISO_PASSES={ISO_PASSES}"
      f"{' (isosurface 꺼짐 — 구슬로 보인다)' if ISO_PASSES == 0 else ''}"
      f"  ANISO={ANISO}  WATER_FILL={WATER_FILL}")

world.reset()

# ── 실행 ────────────────────────────────────────────────────────────
import time                                               # noqa: E402

print("-" * 78)
_t0, _mark = time.time(), 0
_z0 = np.array(inst.GetPositionsAttr().Get())[:, 2]
for step in range(A.steps):
    world.step(render=not A.headless)
    if step - _mark >= 2 * PHYSICS_HZ:
        _dt = time.time() - _t0
        _rate = (step - _mark) / max(_dt, 1e-9)
        z = np.array(inst.GetPositionsAttr().Get())[:, 2]
        # 관 밖으로 샌 입자 — 마개가 듣는지 이걸로 본다
        pts = np.array(inst.GetPositionsAttr().Get())
        _rr, _aa = radial_axial(pts[:, 0], pts[:, 1], pts[:, 2])
        out = int(((_rr > course.PIPE_IR + 0.010)
                   | (np.abs(_aa) > 0.010)).sum())
        print(f"  t={step / PHYSICS_HZ:5.1f}초  물리 {_rate:6.1f} step/s "
              f"({_rate / PHYSICS_HZ:4.2f}x)  수면 z {z.max() * 1000:+6.1f}mm  "
              f"관 밖 입자 {out:,}개"
              + ("" if out == 0 else "  🚨 새고 있다"))
        _t0, _mark = time.time(), step

pts = np.array(inst.GetPositionsAttr().Get())
_rr, _aa = radial_axial(pts[:, 0], pts[:, 1], pts[:, 2])
out = int(((_rr > course.PIPE_IR + 0.010) | (np.abs(_aa) > 0.010)).sum())
print("=" * 78)
print(f"[결과] 입자 {n_particles:,}개  수면 z {pts[:, 2].max() * 1000:+.1f}mm  "
      f"관 밖 {out:,}개 ({out / n_particles * 100:.2f}%)")
print("       " + ("✅ 물이 관 안에 있다" if out == 0 else
                   "🚨 새고 있다 — 마개·contactOffset 을 의심할 것"))

if A.hold and not A.headless:
    print("[유지] 창을 닫을 때까지 유지한다 (Ctrl+C 로 종료)")
    try:
        while simulation_app.is_running():
            world.step(render=True)
    except KeyboardInterrupt:
        pass

simulation_app.close()
