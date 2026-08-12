# Isaac Sim 5.1 — Core API & Python 워크플로우

출처: `python_scripting/*`, `core_api_tutorials/*`, `index.md`

## 0. 버전 주의사항 (5.x)
- **Core Experimental API**: 5.0.0에서 도입. 기존 `isaacsim.core.api`는 향후 deprecate 예정.
  새 코드는 가능하면 Core Experimental 쪽을 고려. (단 5.1 튜토리얼 대부분은 아직 `isaacsim.core.api` 기준)
- 4.5에서 확장(extension) 대량 리네이밍: `omni.isaac.*` → `isaacsim.*`.
  - `omni.isaac.core` → `isaacsim.core.api`
  - `omni.isaac.franka` → `isaacsim.robot.manipulators.examples.franka`
  - `omni.isaac.motion_generation` → `isaacsim.robot_motion.motion_generation`
  - `omni.isaac.sensor` → `isaacsim.sensors.{camera,physics,physx,rtx}`
  - `omni.isaac.ros2_bridge` → `isaacsim.ros2.bridge`
  - `omni.isaac.nucleus.get_assets_root_path` → `isaacsim.storage.native.get_assets_root_path`
    (`isaacsim.core.utils.nucleus.get_assets_root_path`도 여전히 문서에 등장 — 둘 다 통용)

## 1. 개념 계층: Application / Simulation / World / Scene / Stage
- **Stage**: USD 개념. 모든 것은 prim + attribute.
- **Simulation**: prim의 attribute를 시간에 따라 변화시키는 것.
- **Application**: 렌더링/UI 등 시뮬레이션 전반 관리 (Kit).
- **World**: 시뮬레이션 컨텍스트. 물리 스텝, 콜백, 리셋, task 관리. **싱글턴** (`World.instance()`).
- **Scene**: World가 보유. 시뮬레이션에 관심 있는 USD 에셋의 add/get/reset 담당.

## 2. 두 가지 워크플로우
### Standalone (권장 — 물리/렌더 스텝을 직접 제어)
```python
from isaacsim import SimulationApp
simulation_app = SimulationApp({"headless": False})   # 반드시 최상단, 다른 import보다 먼저

from isaacsim.core.api import World
from isaacsim.core.api.objects import DynamicCuboid
import numpy as np

world = World(stage_units_in_meters=1.0)   # physics_dt=1/200, rendering_dt=20/200 등 지정 가능
world.scene.add_default_ground_plane()
cube = world.scene.add(DynamicCuboid(prim_path="/World/random_cube", name="fancy_cube",
                                     position=np.array([0,0,1.0]),
                                     scale=np.array([.5,.5,.5]),
                                     color=np.array([0,0,1.0])))
world.reset()          # articulation 관련 조회 전에 **필수** (physics handle 전파)
while simulation_app.is_running():
    world.step(render=True)
simulation_app.close()
```
- 실행: `./python.sh my_app.py` (Windows: `python.bat`)
- headless: `{"headless": True}` + matplotlib 창 호출 제거

### Extension / Interactive (BaseSample, hot-reload)
```python
from isaacsim.examples.interactive.base_sample import BaseSample
class HelloWorld(BaseSample):
    def setup_scene(self):        # 빈 스테이지에서 최초 1회만. 클래스 변수 할당 금지
        world = self.get_world()
    async def setup_post_load(self):   # LOAD 후, 물리 1스텝 이후 → 여기서 객체/컨트롤러 초기화
        ...
        await self._world.play_async()
    async def setup_post_reset(self):  # RESET 버튼 후
        ...
    def world_cleanup(self):           # hot reload/clear 시 변수 정리
```
- Ctrl+S로 hot reload. `setup_scene` 변경 시 File > New From Stage Template > Empty 후 LOAD.
- **STOP→PLAY는 제대로 리셋 안 됨. RESET 버튼 사용.**
- 이 워크플로우에서는 async 버전 API 사용 (`world.reset_async()`, `play_async()`).

### Script Editor (Window > Script Editor)
- 앱이 비동기 구동 중 → `asyncio.ensure_future(...)` + `await world.reset_async()` 패턴 필수.

## 3. 콜백
```python
world.add_physics_callback("sim_step", callback_fn=self.physics_step)  # 이름 유일해야 함
def physics_step(self, step_size): ...
```
- physics callback은 반드시 `step_size` 인자를 받는다.

## 4. Task 클래스 (`isaacsim.core.api.tasks.BaseTask`)
씬 생성 / 관측 반환 / 메트릭 계산을 모듈화. 여러 로봇·여러 태스크 확장의 기본.
오버라이드 지점:
- `set_up_scene(scene)` — 에셋 추가. 끝에 `self._move_task_objects_to_their_frame()` 로 offset 적용
- `get_observations()` → dict. `world.get_observations()`로 전체 취합
- `get_params()` → `{"name": {"value":…, "modifiable":bool}}` — 런타임 파라미터 교환용
- `pre_step(control_index, simulation_time)` — 매 물리 스텝 전
- `post_reset()` — 리셋 후 (그리퍼 열기 등)
- `__init__(name, offset)` — **offset으로 태스크 다중 배치** (병렬 태스크 확장의 핵심)

내장 태스크: `isaacsim.core.api.tasks.PickPlace`, `.FollowTarget`, `.Stacking` 및
로봇별 `isaacsim.robot.manipulators.examples.franka.tasks.PickPlace` 등.

유니크 이름/경로 헬퍼:
```python
from isaacsim.core.utils.string import find_unique_string_name
from isaacsim.core.utils.prims import is_prim_path_valid
```

## 5. Controller (`isaacsim.core.api.controllers.BaseController`)
- `forward(...)` 구현 → 반드시 `ArticulationAction` 반환.
- 적용: `robot.apply_action(action)` 또는 `robot.get_articulation_controller().apply_action(action)`

## 6. ArticulationAction / Articulation Controller
```python
from isaacsim.core.utils.types import ArticulationAction
ArticulationAction(joint_positions=np.array([0.0,0.0]), joint_indices=np.array([7,8]))
```
- 각도 단위: **API는 radian**, USD는 degree (컨트롤러가 자동 변환).
- joint_indices 생략 시 전체 관절에 적용 → 개수/순서 반드시 일치.
- **한 관절은 한 가지 제어 방식만** (position/velocity/effort 동시 불가).
- OmniGraph 노드 버전 입력: execIn, targetPrim/robotPath, jointIndices/jointNames,
  positionCommand/velocityCommand/effortCommand.

## 7. Prim 뷰 클래스 (배치 조작)
- `isaacsim.core.prims`: `Articulation`(구 ArticulationView), `RigidPrim`, `XFormPrim`,
  `SingleArticulation`, `SingleXFormPrim` (단일 프림 버전)
- 정규식 경로: `Articulation(prim_paths_expr="/World/Franka_[1-2]", name="frankas_view")`
- **View는 `world.scene.add(view)` + `world.reset()` 후에야 초기화됨.**
- 접촉력: `RigidPrim(..., contact_filter_prim_paths_expr=[...], max_contact_count=N, track_contact_forces=True)`
  → `get_net_contact_forces()`, `get_contact_force_matrix()`, `get_friction_data(dt)`, `get_contact_force_data(dt)`

## 8. 저수준 관절 제어 (dynamic_control — 구 API, 스니펫에 남아있음)
`from omni.isaac.dynamic_control import _dynamic_control` → `dc.get_articulation(path)`,
`dc.wake_up_articulation(art)`, `set_articulation_dof_position_targets/velocity_targets/efforts`,
`find_articulation_dof`, `get_articulation_dof_states`.
※ 속도 제어 전에는 해당 DriveAPI의 **stiffness를 0으로** 설정한 뒤 articulation 핸들을 다시 얻어야 함.

## 9. 자주 쓰는 유틸 스니펫
- 에셋 루트: `get_assets_root_path()` (None이면 예외 처리 필수)
- 스테이지에 참조 추가: `isaacsim.core.utils.stage.add_reference_to_stage(usd_path, prim_path)`
- variant 선택: `prim.GetVariantSet("Gripper").SetVariantSelection("AlternateFinger")`
- 시맨틱 라벨: `isaacsim.core.utils.semantics.add_labels(prim, labels=[...], instance_name="class")`
- 회전 변환: `isaacsim.core.utils.numpy.rotations.euler_angles_to_quats`
- 확장 활성화: `isaacsim.core.utils.extensions.enable_extension("omni.kit.widget.stage")`
- 확장 경로: `get_extension_path_from_name("isaacsim.robot_motion.motion_generation")`
- 디버그 드로잉: `from isaacsim.util.debug_draw import _debug_draw` → `draw_points/clear_points`
  (렌더러/물리와 상호작용 X, 가장 빠름). 대량 지오메트리는 `UsdGeom.Points`(렌더 필요 시) /
  `UsdGeom.PointInstancer`(물리 필요 시).
- 렌더 지연 제거(최신 상태 즉시 렌더): experience `apps/omni.isaac.sim.zero_delay.python.kit`
  또는 `extra_args=["--/app/hydraEngine/waitIdle=1", "--/app/updateOrder/checkForHydraRenderComplete=1000",
  "--/exts/isaacsim.ros2.bridge/publish_multithreading_disabled=1"]`

## 10. 물리/USD 스니펫 요약
- PhysicsScene: `UsdPhysics.Scene.Define` + `PhysxSchema.PhysxSceneAPI` (CCD, GPU dynamics, MBP, TGS)
- 강체/충돌: `omni.physx.scripts.utils.setRigidBody(prim, "convexHull"|"convexDecomposition", False)`,
  `utils.setCollider(prim, approximationShape=...)`
- 질량: `UsdPhysics.MassAPI.Apply(prim).CreateMassAttr(10)` / `CreateDensityAttr(1000)`
  (mass=0이면 볼륨 기반 자동 계산, density 미지정 시 1000 kg/m³)
- 오버랩/레이캐스트: `omni.physx.get_physx_scene_query_interface().overlap_box/overlap_sphere/raycast_closest`
- 머티리얼: `omni.kit.commands.execute("CreateAndBindMdlMaterialFromLibrary", mdl_name="OmniPBR.mdl", ...)`
  + `UsdShade.MaterialBindingAPI(prim).Bind(...)`
- 월드 변환: `omni.usd.utils.get_world_transform_matrix(prim, timecode)`
- 저장: `omni.usd.get_context().save_as_stage(path, None)`

관련: [[isaacsim-motion-generation]], [[isaacsim-manipulator-pickplace]]
