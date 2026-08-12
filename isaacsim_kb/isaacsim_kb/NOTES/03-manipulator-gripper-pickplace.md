# Isaac Sim 5.1 — 매니퓰레이터 / 그리퍼 / Pick & Place

출처: `robot_setup_tutorials/*`, `robot_setup/*`, `robot_simulation/*`, `importer_exporter/*`,
`core_api_tutorials/tutorial_core_adding_manipulator.md`

## 1. 매니퓰레이터 셋업 파이프라인 (튜토리얼 6→7→8→9)
1. **Import**: URDF/MJCF/CAD → USD (URDF Importer)
2. **Assemble**: 팔 + 그리퍼를 하나의 articulation으로 결합 (수동 fixed joint 또는 Robot Assembler)
3. **Configure**: articulation solver 설정, physics material, effort limit, 게인 튜닝
4. **Generate config**: URDF 재출력 + Lula robot_description.yaml + collision spheres
5. **Control**: Lula IK / RMPflow / PickPlaceController

## 2. URDF Importer (`isaacsim.asset.importer.urdf`) — File > Import
- Links: **Moveable base**(모바일) vs **Static base**(6축 팔 → `root_joint`로 고정)
- Default Density: URDF에 mass 없는 링크용. 0이면 물리엔진 기본값 자동 계산.
- **Joint Configuration**:
  - *Stiffness*: kp/damping 직접 입력
  - *Natural Frequency*: `Kp = m·ωn²`, `Kd = 2·m·ζ·ωn` (ζ=1 임계감쇠). 저장은 항상 stiffness로.
  - 다중 선택 편집: ctrl+click / shift+click
- Drive Type: **Acceleration**(관성 정규화, 질량 변화에 불변 — 이상적 액추에이터) vs **Force**(스프링-댐퍼)
- Target: None / Position / Velocity. **position 제어 → stiffness, velocity 제어 → damping** 설정.
- Ignore Mimic 체크 해제 시 mimic joint에 PhysX Mimic API 부여.
- Colliders: Collision From Visuals, Convex Hull / Convex Decomposition,
  **Allow self-collision은 기본 off 권장**, Replace Cylinders with Capsules.
- 특수문자는 `_`로 치환됨 → URDF에서 미리 정리 권장.
- **ROS 2 노드에서 직접 import**: 확장 `isaacsim.ros2.urdf` 활성화 → File > Import from the ROS 2 URDF Node
  (Node에 `robot_state_publisher` 입력). ROS 2 bridge 필요.
- 커스텀 태그: `<sensor ... isaac_sim_config="...">`(RTX Lidar), `<loop_joint>`(폐루프),
  `<fixed_frame name= ...>`(센서/EE 오프셋용 참조 프레임 — link 추가 없이 프레임 정의)
- 임포트 결과는 Isaac Sim Asset Structure를 따르고 메시는 이미 instanceable.

## 3. USD → URDF Exporter
- 확장: Isaac Sim USD to URDF Exporter (`omni.exporter.urdf`), File > Export URDF
- **그리퍼 조립 후 반드시 재출력** → Lula/RMPflow가 올바른 EE 오프셋·구조를 인식.

## 4. 팔 + 그리퍼 결합 두 가지 방법
### Option 1 — 수동 (GUI)
- 그리퍼 USD를 드래그, prim명을 `ee_link` 등으로 변경
- `wrist_3_link`의 위치/자세로 xform 설정
- `ee_link/root_joint`에서 **Articulation Root 제거** (로봇당 articulation root는 하나)
- root_joint의 `Body0`를 `/ur/wrist_3_link`로 설정
- 베이스 로봇 prim의 `IsaacRobotAPI` → `isaac:physics:robotJoints` / `robotLinks`에 `/ur/ee_link` 추가

### Option 2 — Robot Assembler (권장)
- Tools > Robotics > Asset Editors > Robot Assembler
- Base Robot + Attach Point(`wrist_3_link`), Attach Robot + Attach Point(`robotiq_arg2f_base_link`),
  Assembly Namespace(예: `ee_link`)
- Begin Assembling → 90° 단위 회전 버튼/기즈모로 자세 조정 → Assemble and Simulate → End Simulation And Finish
- 결과: `configuration/<robot>_<namespace>_<attach>.usd` + **Variant set** 생성
  → Property > Variants에서 `None`/`robotiq_2f_140` 전환으로 EE 교체 가능
- **중요**: 고정 조인트는 *물리 시뮬레이션 중에만* 유효. 정적으로 놓인 물체(테이블 위 로봇)에는 불필요.
- Python API:
```python
from isaacsim.robot_setup.assembler import RobotAssembler
assembler = RobotAssembler()
assembler.begin_assembly(stage, robot_base, base_mount, robot_attach, attach_mount,
                         assembly_namespace, variant_name)
# 여기서 USD로 추가 변환 조정
assembler.assemble()        # fixed joint 생성 + attach 로봇의 articulation root 제거
assembler.finish_assemble() # 또는 assembler.cancel_assemble()
```

## 5. Articulation 설정 (튜토리얼 7)
`<robot>/root_joint` prim → Property > Physics/Articulation:
- Articulation Enabled
- **Solver Position Iterations Count = 64**, **Velocity Iterations = 4** (mimic joint 많은 복잡 로봇)
- Sleep Threshold = 0.00005, Stabilization Threshold = 0.00001
- 물리 레이어(`configuration/*_physics.usd`)에서 편집 → 상위 에셋에 자동 반영

그리퍼 물리:
- Rigid Body Material 생성 → static/dynamic friction 1.0 (고무 fingertip은 0.8 + Combine Mode `Max`)
- fingertip collider (`colliders/left_inner_finger/mesh_1/box`)에 바인딩
- `finger_joint`의 Drive/Angular/**Max Force = 200** (실제 토크 한계에 맞춤)
  ※ Max Force가 매우 크면 관통/불안정 → Time Step per Second 증가 필요

검증 도구:
- **Physics Inspector** (Tools > Physics > Physics Inspector): DOF 슬라이더로 타깃 위치 도달 확인.
  ⚠ omni.physx를 부분 초기화하므로 열려 있으면 일반 시뮬레이션이 정상 동작하지 않을 수 있음.
- **Gain Tuner** (Tools > Robotics > Asset Editors > Gain Tuner)

## 6. 게인 튜닝 (튜토리얼 11 / Gain Tuner)
### Position drive
1. damping=0으로 두고 stiffness만 증가 → 타깃 근처 수렴할 때까지
2. stiffness를 **한 자릿수(10배) 낮춤**
3. damping = stiffness보다 한 자릿수 낮게 → 기본선(오버슈트 없음). 빠른 응답 원하면 damping 더 낮춤
4. 미세조정. 목표: 오버슈트 1% 이내
- 중력 보상 있는 로봇은 rigid body들의 Disable Gravity 체크 후 튜닝
- **산업용 로봇**(내장 PD, 항상 속도 제한으로 주행): 위에서 구한 stiffness를 ×2 하고
  Joint > Advanced > **Maximum Joint Velocity**를 사양값으로 설정. stiffness를 무한정 올리지 말 것.
### Velocity drive
- stiffness=0, damping만 증가. 추가 부하 예상 시 damping +10%.
- 출력 제한은 max joint velocity 또는 max joint force로.
### 팁
- 함께 움직이는 관절끼리 그룹으로 나눠 튜닝 (예: 휴머노이드 팔/다리 분리)
- USD 기본 max velocity는 대개 비현실적으로 높음 → 실제로 낼 속도로 낮추고 튜닝
- Gain Tuner에서 `Nat. Freq.`=0.5, `Damping Ratio`=1.0 → 임계감쇠 시작점
  (언더슈트→Nat.Freq. ↑, 오버슈트→Nat.Freq. ↓ & Damping Ratio ↑)
- `Save Gains to Physics Layer` 버튼으로 physics 레이어에 저장

## 7. 그리퍼 리깅 — 폐루프 / Mimic Joint (튜토리얼 10, Robotiq 2F-85 예시)
- **Articulation은 kinematic tree여야 함** → 폐루프면 조인트 하나를 articulation에서 제외
  (Joint 섹션 > **Exclude From Articulation**). 이 조인트는 maximal-coordinate로 처리되어
  오차가 가장 많이 쌓이므로, **limit·저항·drive가 없는 순수 공간 제약 조인트**를 고를 것.
  (2F-85에서는 `left/right_inner_knuckle_joint`)
- 힘 기반 파지 모델링: 구동 조인트(`finger_joint`, `right_outer_knuckle_joint`)
  - Stiffness 0.0 / Damping 5000.0 / Max Force 180→(불안정하면) 5.0 / Max Joint Velocity 130 deg/s
  - 평행 유지용 스프링 흉내: `left/right_outer_finger_joint`의 stiffness = 0.05
- **Mimic Joint**: 종속 조인트 선택 → Add > Physics > Mimic Joint,
  Reference Joint = `finger_joint`, gearing = -1.0.
  ※ mimic 적용 조인트의 자체 drive 값은 0으로 비우기 (참조 조인트의 drive가 복사됨)
- 접촉 안정성: 무거운 물체가 미끄러지면 **Physics Scene의 Time Steps per Second를 올린다** (예: 60→80+)
- Self-Collision: Articulation Root Options의 Self-Collision Enabled 체크
- **Layer 활용**: 원본 에셋(`*_base.usd`)은 건드리지 말고 `*_edit.usd`/`*_config.usd` 레이어에서 작업.
  완료 후 Layer 탭에서 prim 드래그로 병합.

## 8. 그리퍼 클래스 (Python)
```python
from isaacsim.robot.manipulators import SingleManipulator
from isaacsim.robot.manipulators.grippers import ParallelGripper

gripper = ParallelGripper(
    end_effector_prim_path="/ur/ee_link/robotiq_arg2f_base_link",
    joint_prim_names=["finger_joint"],
    joint_opened_positions=np.array([0]),
    joint_closed_positions=np.array([40]),
    action_deltas=np.array([-40]),
    use_mimic_joints=True,          # mimic joint 사용 시
)
robot = world.scene.add(SingleManipulator(
    prim_path="/ur", name="ur10_robot",
    end_effector_prim_path="/ur/ee_link/robotiq_arg2f_base_link",
    gripper=gripper))

robot.gripper.get_joint_positions()
robot.gripper.apply_action(ArticulationAction(joint_positions=[pos + 0.1]))
robot.gripper.set_joint_positions(robot.gripper.joint_opened_positions)
```
- 다른 그리퍼 클래스: `SurfaceGripper`(흡착), Franka 전용 `Franka.gripper`
- 로봇 전용 래퍼: `isaacsim.robot.manipulators.examples.franka.Franka` /
  `.universal_robots.UR10` 등 (gripper·end_effector 속성 제공)

## 9. Surface Gripper (흡착식) — `isaacsim.robot.surface_gripper`
- Create > Robots > Surface Gripper
- 접촉점마다 **D6 Joint** 필요: enabled, 모든 joint의 **Body0가 동일**, Exclude from Articulation = True,
  break force/torque 미설정
- 속성: Attachment Points, Max Grip Distance, Retry Interval, **Shear Force Limit**, **Coaxial Force Limit**
- AttachmentPointAPI: `ClearanceOffset`(레이캐스트 시작 오프셋), `Forward Axis`(기본 X)
- Python:
```python
import isaacsim.robot.surface_gripper._surface_gripper as sg
iface = sg.acquire_surface_gripper_interface()
iface.close_gripper(path); iface.open_gripper(path)
iface.set_gripper_action(path, 0.5)   # >0.3 닫기, <-0.3 열기
iface.get_gripper_status(path)        # Open / Closed / Closing
```

## 10. Grasp Editor (`isaacsim.robot_setup.grasp_editor`)
- Tools > Robotics > Grasp Editor. gripper/object 쌍의 파지 자세를 **isaac_grasp YAML**로 저장.
```yaml
format: isaac_grasp
format_version: 1.0
object_frame_link: /World/mug
gripper_frame_link: /World/panda_hand
grasps:
  grasp_0:
    confidence: 1.0
    position: [-0.04346, 0.06759, 0.19895]      # object frame 기준 gripper 위치
    orientation: {w: 0.00332, xyz: [...]}
    cspace_position: {panda_finger_joint1: 0.00943}      # 파지 중 관절값
    pregrasp_cspace_position: {panda_finger_joint1: 0.04} # 열린 상태
```
- 사용: pregrasp 자세로 상대 pose까지 이동 → cspace_position까지 닫기
  `T_g = R_o·ᵒT_g + T_o`, `R_g = R_o·ᵒR_g`
- **프레임 선택이 핵심**: 모션 생성기가 URDF를 쓰므로 URDF에 존재하는 프레임을 골라야 의미가 있음.
  객체 프레임은 비전 파이프라인의 암묵적 기준 프레임과 일치시켜야 함.
- Joint Settings: Position When Open/Closed, Grasp Speed, Max Effort Magnitude
- Utils: Mask Collision, Show Physics Colliders. 시뮬 없이 내보내려면 **Skip Sim**.
- 외력/토크 테스트로 force closure 품질 검증 가능.
- Python:
```python
from isaacsim.robot_setup.grasp_editor import import_grasps_from_file, GraspSpec
from isaacsim.core.utils.xforms import get_world_pose
spec = import_grasps_from_file("franka_mug_grasp.yaml")
obj_t, obj_q = get_world_pose("/World/mug")
g_t, g_q = spec.compute_gripper_pose_from_rigid_body_pose("grasp_1", obj_t, obj_q)
```

## 11. Pick & Place 컨트롤러
```python
from isaacsim.robot.manipulators.controllers import PickPlaceController   # 일반형
# 로봇별: isaacsim.robot.manipulators.examples.franka.controllers.PickPlaceController

ctrl = PickPlaceController(name="controller",
                           cspace_controller=RMPFlowController(...),   # 커스텀 로봇은 직접 지정
                           gripper=robot.gripper,
                           events_dt=[...],                # 10개 이벤트의 dt
                           end_effector_initial_height=0.6)

actions = ctrl.forward(picking_position=..., placing_position=...,
                       current_joint_positions=...,
                       end_effector_offset=np.array([0,0,0.20]))  # ★ 반드시 튜닝
articulation_controller.apply_action(actions)
if ctrl.is_done(): ...
ctrl.reset()
```
- **이벤트 기반 상태 머신**(성공 판정 아님, dt 기반). `events_dt` 10개 값으로 각 단계 속도 조정.
  예시값: `[0.005, 0.002, 1, 0.05, 0.0008, 0.005, 0.0008, 0.1, 0.0008, 0.008]` (UR10e)
  느리게 하려면 해당 dt를 줄인다.
- `end_effector_offset`: EE 링크와 실제 파지점 사이 오프셋. **튜닝 필수.**
- 커스텀 로봇용 RMPFlowController 래핑:
```python
import isaacsim.robot_motion.motion_generation as mg
class RMPFlowController(mg.MotionPolicyController):
    def __init__(self, name, robot_articulation, physics_dt=1/60.):
        self.rmpflow = mg.lula.motion_policies.RmpFlow(
            robot_description_path=".../robot_descriptor.yaml",
            rmpflow_config_path=".../<robot>_rmpflow_common.yaml",
            urdf_path=".../<robot>.urdf",
            end_effector_frame_name="ee_link_...",
            maximum_substep_size=0.00334)
        self.articulation_rmp = mg.ArticulationMotionPolicy(robot_articulation, self.rmpflow, physics_dt)
        mg.MotionPolicyController.__init__(self, name=name,
                                          articulation_motion_policy=self.articulation_rmp)
        self._motion_policy.set_robot_base_pose(*robot_articulation.get_world_pose())
```
- 표준 예제 위치: `standalone_examples/api/isaacsim.robot.manipulators/ur10e/` (gripper_control.py,
  follow_target_example.py, follow_target_example_rmpflow.py, pick_up_example.py)
  및 `.../franka/`, `.../universal_robots/multiple_tasks.py`

## 12. Standalone 메인 루프 관용구
```python
my_world = World(stage_units_in_meters=1.0, physics_dt=1/200, rendering_dt=20/200)
...
my_world.reset()
reset_needed = False
while simulation_app.is_running():
    my_world.step(render=True)
    if my_world.is_stopped():   reset_needed = True
    if my_world.is_playing():
        if reset_needed:
            my_world.reset(); my_controller.reset(); reset_needed = False
        if my_world.current_time_step_index == 0:
            my_controller.reset()
        obs = my_world.get_observations()
        ...
simulation_app.close()
```

관련: [[isaacsim-motion-generation]], [[isaacsim-core-api]]
