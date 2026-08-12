"""[Isaac 3.11] 조립 프로브 — 새 로봇·새 배관을 붙여 보고 **사실만 찍는다.**

`zigzag_demo.py` 를 쓰기 전에 코드로는 알 수 없는 세 가지를 실측한다.

  ① **DOF 이름** — 이게 이 프로브의 존재 이유다.
     robot_from_bot_welder_art_v2.usda 는 서스펜션과 휠 조인트가 **같은 이름**을
     쓴다(`SpringJoints/RearBody_A0` 와 `DriveJoints/RearBody_A0`). USD 경로는
     다르지만 Isaac 의 `dof_names` 는 조인트 **프림 이름**에서 나오므로, 12개가
     충돌하면 인덱스를 이름으로 고를 수 없다. son 로봇은 `_piston_`/`_wheel_`
     처럼 접미사가 달라서 이 문제가 없었다 — 그대로 베끼면 안 된다.
  ② **합성 방식** — 로봇 usda 는 defaultPrim 이 `World` 라 PhysicsScene 과
     Looks 를 통째로 안고 있다. AddReference 로 붙이면 PhysicsScene 이 2개가
     된다. 그래서 `Sdf.CopySpec` 으로 /World/Robot 과 /World/Looks 만 같은
     경로에 복사한다 — 머티리얼 바인딩이 `</World/Looks/...>` 절대경로라
     경로를 유지해야 안 깨진다.
  ③ **안착 거동** — 다리 12개가 각각 예압 18N(3000 N/m × 초과 6mm, maxForce
     60N 로 상한)으로 벽을 민다. son 로봇은 6개 × 9N 이었다. 안착 중 로봇이
     뒤로 얼마나 밀리는지가 START_S 를 정한다.

실행:
    ISAAC_STREAM=0 PYTHONUNBUFFERED=1 isaac_python probe_robot.py
"""

import sys
from pathlib import Path

from isaacsim import SimulationApp                        # noqa: E402

simulation_app = SimulationApp({"headless": True})

import numpy as np                                        # noqa: E402
from isaacsim.core.api import World                       # noqa: E402
from isaacsim.core.prims import SingleArticulation        # noqa: E402
from isaacsim.core.utils.types import ArticulationAction  # noqa: E402
from pxr import Gf, PhysxSchema, Sdf, UsdGeom, UsdLux, UsdPhysics  # noqa: E402

WS = Path("/home/ubuntu/cobot3_ws")
ROBOT_USDA = str(WS / "robot_from_bot_welder_art_v2.usda")
# 배관은 코스가 고른다 (`ZIGZAG_COURSE=long|hook`) — scene.py 와 같은 출처.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import course                                             # noqa: E402
PIPE_USDA = str(WS / course.PIPE_USDA_NAME)

PHYSICS_HZ = 240.0
START_X = 0.20          # 로봇 원점을 관 입구에서 200mm 안쪽에 둔다
SETTLE_STEPS = 480      # 2초

world = World(stage_units_in_meters=1.0,
              physics_dt=1.0 / PHYSICS_HZ, rendering_dt=1.0 / 60.0)
stage = world.stage
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
UsdGeom.Xform.Define(stage, "/World")

light = UsdLux.SphereLight.Define(stage, "/World/Light")
light.CreateIntensityAttr(3e6)
light.CreateRadiusAttr(0.05)
UsdGeom.Xformable(light).AddTranslateOp().Set(Gf.Vec3d(0.2, 0.2, 0.4))

# ── 배관 ────────────────────────────────────────────────────────────
# defaultPrim 이 단일 Xform(TestPipeZigzagHook) 이라 참조로 깨끗하게 붙는다.
stage.DefinePrim("/World/Pipe", "Xform").GetReferences().AddReference(PIPE_USDA)

# ── 로봇 ────────────────────────────────────────────────────────────
# 🚨 참조가 아니라 **복사**다. 위 머리말 ② 참조.
_robot_layer = Sdf.Layer.FindOrOpen(ROBOT_USDA)
if _robot_layer is None:
    raise SystemExit(f"[중단] 로봇 레이어를 못 열었다: {ROBOT_USDA}")
_root = stage.GetRootLayer()
for _p in ("/World/Looks", "/World/Robot"):
    if not Sdf.CopySpec(_robot_layer, Sdf.Path(_p), _root, Sdf.Path(_p)):
        raise SystemExit(f"[중단] CopySpec 실패: {_p}")
print(f"[준비] 로봇 복사 완료 — /World/Robot, /World/Looks")

robot_prim = stage.GetPrimAtPath("/World/Robot")
_xf = UsdGeom.Xformable(robot_prim)
_xf.ClearXformOpOrder()
_xf.AddTranslateOp().Set(Gf.Vec3d(START_X, 0.0, 0.0))
print(f"[준비] 로봇 배치 x={START_X * 1000:.0f}mm (관 축 +X, 회전 없음)")

# 배관 물리 재질 — 만관 기준(0.30/0.25). 프로브라 일단 건식 0.40/0.35 로 본다.
_pipe_geom = stage.GetPrimAtPath("/World/Pipe/geom")
if _pipe_geom.IsValid():
    _m = UsdPhysics.MaterialAPI(_pipe_geom)
    print(f"[준비] 배관 마찰 static={_pipe_geom.GetAttribute('physics:staticFriction').Get()} "
          f"dynamic={_pipe_geom.GetAttribute('physics:dynamicFriction').Get()}")

# 감지 밴드 — 0.05 m/s @240Hz 기준 0.5mm 하한
CONTACT_OFFSET = 0.0005
_n = 0
for _p in stage.Traverse():
    if _p.HasAPI(UsdPhysics.CollisionAPI) or _p.IsA(UsdGeom.Mesh):
        _px = PhysxSchema.PhysxCollisionAPI.Apply(_p)
        _px.CreateContactOffsetAttr(CONTACT_OFFSET)
        _px.CreateRestOffsetAttr(0.0)
        _n += 1
print(f"[준비] contactOffset {CONTACT_OFFSET * 1000:.2f}mm → 프림 {_n}개")

art = SingleArticulation(prim_path="/World/Robot", name="zigzag_welder")
world.scene.add(art)
world.reset()

# ── ① DOF 이름 ──────────────────────────────────────────────────────
dof = list(art.dof_names or [])
print("=" * 78)
print(f"DOF {len(dof)} 개")
for k, n in enumerate(dof):
    print(f"  [{k:2}] {n}")

from collections import Counter                            # noqa: E402
dup = {n: c for n, c in Counter(dof).items() if c > 1}
print("=" * 78)
if dup:
    print(f"🚨 **이름 중복 {len(dup)} 종** — 이름으로 인덱스를 고를 수 없다:")
    for n, c in sorted(dup.items()):
        print(f"     {n} × {c}  → 인덱스 {[k for k, m in enumerate(dof) if m == n]}")
else:
    print("✅ DOF 이름이 모두 유일하다 — 이름으로 골라도 된다")

# 조인트 프림 경로 순서도 같이 찍는다(인덱스 추정의 근거)
print("-" * 78)
print("스테이지의 조인트 프림 (경로 순):")
for p in stage.Traverse():
    t = p.GetTypeName()
    if "Joint" in str(t):
        print(f"  {str(t):24} {p.GetPath()}")

# ── ③ 안착 ──────────────────────────────────────────────────────────
print("=" * 78)
_p0 = art.get_world_pose()[0]
print(f"안착 전 로봇 루트 (mm) {np.round(np.asarray(_p0) * 1000, 2)}")
for i in range(SETTLE_STEPS):
    world.step(render=False)
_p1 = art.get_world_pose()[0]
_dp = (np.asarray(_p1) - np.asarray(_p0)) * 1000
print(f"안착 후 로봇 루트 (mm) {np.round(np.asarray(_p1) * 1000, 2)}")
print(f"안착 중 이동 (mm)      {np.round(_dp, 2)}   "
      f"→ 축방향 {_dp[0]:+.1f}mm")

pos = np.asarray(art.get_joint_positions())
print("-" * 78)
print("조인트 위치 (안착 후):")
for k, n in enumerate(dof):
    v = pos[k]
    unit = "mm" if abs(v) < 0.05 else "rad"
    print(f"  [{k:2}] {n:26} {v * 1000:8.3f} mm   ({np.degrees(v):7.2f}°)")

# 링크 월드 위치 — 관 중심선(z=0, y=0) 대비 반경으로 밀착을 본다
print("-" * 78)
_XC = UsdGeom.XformCache()


def wpos(path):
    _XC.Clear()
    t = _XC.GetLocalToWorldTransform(stage.GetPrimAtPath(path)).ExtractTranslation()
    return np.array([float(t[0]), float(t[1]), float(t[2])])


print("휠 12개 — 중심선 기준 반경(관 내반경 50mm, 휠 반경 8mm → 밀착 시 42mm):")
_ok = 0
for side in ("Rear", "Front"):
    for grp in ("A", "B"):
        for i in range(3):
            nm = f"{side}Body_{grp}{i}_Wheel"
            w = wpos(f"/World/Robot/{nm}")
            r = np.hypot(w[1], w[2]) * 1000
            tight = abs(r - 42.0) < 1.5
            _ok += tight
            print(f"  {nm:22} x={w[0]*1000:7.1f}  r={r:6.2f}mm  "
                  f"{'밀착' if tight else '⚠ 뜸'}")
print(f"→ 밀착 {_ok}/12")

print("=" * 78)
print("프로브 종료")
simulation_app.close()
