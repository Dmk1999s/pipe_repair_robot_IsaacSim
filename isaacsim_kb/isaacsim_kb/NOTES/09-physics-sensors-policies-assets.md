# Isaac Sim 5.1 — 물리 센서 상세 / RL 정책 배포 / 이동로봇 컨트롤러 / 에셋

출처: `sensors/isaacsim_sensors_physics_*`, `isaac_lab_tutorials/tutorial_policy_deployment.md`,
`robot_simulation/mobile_robot_controllers.md`, `assets/*`, `introduction/examples.md`

## 1. Contact Sensor (`isaacsim.sensors.physics.ContactSensor`)
PhysX Contact Report API 기반. 실제 접촉 셀/압력 패드와 유사한 측정치를 제공.
**파지 성공 판정, 발바닥 접촉 등에 사용.**

속성:
- `radius` — 이 구 영역 안의 접촉만 집계 (영역 밖 접촉은 버림). `-1`이면 제한 없음.
  ※ 구는 **집계 경계**일 뿐, 접촉 자체는 여전히 물체 표면에서만 발생.
- `min_threshold` / `max_threshold` — 접촉 인정 최소 힘 / 출력 최대 힘
- `sensor_period` — 측정 간격. **물리 주기보다 빠를 수 없음** (더 짧게 주면 최신 물리 데이터를 그대로 출력)
- `enabled`

생성:
```python
# 명령 방식
omni.kit.commands.execute("IsaacSensorCreateContactSensor",
    path="Contact_Sensor", parent="/World/Cube",
    sensor_period=1, min_threshold=0.0001, max_threshold=100000,
    translation=Gf.Vec3d(0,0,0))

# 래퍼 클래스 (권장 — 헬퍼 함수 포함)
from isaacsim.sensors.physics import ContactSensor
sensor = ContactSensor(prim_path="/World/Cube/Contact_Sensor", name="Contact_Sensor",
                       frequency=60, translation=np.array([0,0,0]),
                       min_threshold=0, max_threshold=1e7, radius=-1)
```
- **collider API가 있는 prim에만** 생성 가능. Contact Report API는 자동 부여
  (수동: `PhysxSchema.PhysxContactReportAPI.Apply(prim).CreateThresholdAttr(0.0)`)
- `translation`과 `position`, `frequency`와 `dt`는 **동시 지정 불가**

읽기 (3가지):
```python
from isaacsim.sensors.physics import _sensor
iface = _sensor.acquire_contact_sensor_interface()
iface.get_sensor_reading("/World/Cube/Contact_Sensor", use_latest_data=True)  # 권장
#   → CsSensorReading: is_valid, time, value, in_contact
sensor.get_current_frame()   # dict: in_contact, force, number_of_contacts, time,
                             #       body0, body1, position, normal, impulse, contacts, physics_step
iface.get_contact_sensor_raw_data(path)   # CsRawData 리스트(임계값 무시). deprecated 예정
```
- OmniGraph: `Isaac Read Contact Sensor` 노드 (Contact Sensor Prim 지정)
- 시각화: `Isaac xPrim Radius Visualizer Node`
- ⚠ **센서는 Play 시 동적으로 생성됨. 시뮬레이션 중 센서 prim을 옮기면 센서가 무효화됨.**
  계층 변경(부모 리지드바디 변경 등)은 STOP 후에.

## 2. Effort Sensor (`isaacsim.sensors.physics.EffortSensor`)
관절에 가해진 토크(revolute) / 힘 크기(prismatic) 측정.
```python
from isaacsim.sensors.physics.scripts.effort_sensor import EffortSensor
sensor = EffortSensor(prim_path="/World/robot/Arm/RevoluteJoint",
                      sensor_period=0.1, use_latest_data=False, enabled=True)
reading = sensor.get_sensor_reading(use_latest_data=True)   # EsSensorReading: is_valid, time, value
# 커스텀 보간 함수도 전달 가능: get_sensor_reading(interpolation_function)
```
- 파라미터는 멤버 변수 직접 수정(`sensor_period`, `use_latest_data`, `enabled`),
  `update_dof_name()`, `change_buffer_size()`
- OmniGraph: `Isaac Read Effort Node`

## 3. Articulation Joint 힘/토크 (센서 없이 Articulation API로)
```python
art.get_applied_joint_efforts()    # 사용자가 set_joint_efforts로 준 값
art.get_measured_joint_forces()    # 관절별 6D 공간 힘 (총 힘) — 고정 조인트에서 읽으면 F/T 센서 역할
art.get_measured_joint_efforts()   # 운동 방향으로 투영한 능동 성분
```
- 반환값은 **자식 링크 → 부모 링크 방향의 incoming joint force**.
- 조인트 이름 ↔ 링크 인덱스 매핑:
```python
joint = UsdPhysics.Joint.Get(stage, f"/World/Ant/joints/{joint_name}")
body1 = stage.GetPrimAtPath(joint.GetBody1Rel().GetTargets()[0]).GetName()
idx = art._articulation_view.get_link_index(body1)
```

## 4. IMU Sensor
`isaacsim.sensors.physics.IMUSensor`. GUI: Create > Sensors > Imu Sensor.
OmniGraph `Isaac Read IMU Node` → `ROS2 Publish Imu`(frameId를 TF 트리와 일치시킬 것).
5.1에서 디바이스측 처리로 성능 개선, 방향(orientation) 버그 수정됨.

## 5. RL 정책 배포 (Isaac Lab → Isaac Sim)
데모: Robotics Examples > POLICY > Humanoid(H1) / Quadruped(Spot)
### 절차
1. Isaac Lab에서 학습 (`Isaac-Velocity-Flat-H1-v0` 등),
   `play.py`로 **export** → `exported/` 폴더에 정책 파일
2. `logs/rsl_rl/<task>/<time>/params/`의 `agent.yaml`(신경망), **`env.yaml`(환경·로봇 설정)** 확보
3. Policy Controller 클래스 구현:
   - 생성자: 로봇 USD spawn + SingleArticulation
   - `load_policy()`: 정책 + env 파일 로드
   - `initialize()`: **시뮬 시작 후 1회.** effort/control mode, joint gains, max effort/velocity,
     articulation root를 정책 학습 설정과 일치시킴
   - `_compute_observation()`: env.yaml의 **observation scale을 반드시 곱해서** 텐서 구성
     (예 H1: 69차원 = lin_vel3 + ang_vel3 + gravity3 + command3 + jointpos19 + jointvel19 + prev_action19)
   - `forward()`: `decimation`마다 정책 호출,
     `ArticulationAction(joint_positions=default_pos + action*action_scale)` → `apply_action`
   - ⚠ **위치 제어에 `set_joint_position()` 쓰지 말 것** (관절이 순간이동함)
### 위치→토크 변환
`isaacsim.robot.policy.examples/utils/actuator_network.py`의 `LstmSeaNetwork`
```python
self._actuator_network.setup(file, self.default_pos)
joint_torques, _ = self._actuator_network.compute_torques(pos, vel, action_scale*action)
self.set_joint_efforts(joint_torques)
```
### 디버깅 체크리스트 (★ 순서대로)
1. Isaac Lab에서 정책 자체가 동작하는지 확인
2. **관절 순서**: `art.dof_names` 를 Isaac Sim 에셋과 학습 에셋 양쪽에서 출력해 **정확히 일치**하는지
   (순서가 틀리면 로봇이 넘어짐)
3. **기본 관절 위치**가 올바른지 (틀리면 발끝으로 걷는 등 이상 자세)
4. **관절 물성**: `art.dof_properties` vs env.yaml의 stiffness/damping/effort_limit
   (너무 높으면 저구동, 너무 낮으면 과운동)
5. **Physics Scene의 Time Steps Per Second = 1/dt** (예: dt=0.005 → 200Hz. 60Hz로 두면 실패)
6. 관측/행동 텐서 구조와 스케일 팩터

## 6. 이동로봇 컨트롤러 (`isaacsim.robot.wheeled_robots.controllers`)
- **DifferentialController(name, wheel_radius, wheel_base)**
  `ω_R = (2V + ω·l)/2r`, `ω_L = (2V - ω·l)/2r`
  `robot.apply_wheel_actions(controller.forward([linear, angular]))`
  OmniGraph 입력: wheelRadius, wheelDistance, dt, maxAcceleration/Deceleration,
  maxAngularAcceleration, maxLinear/Angular/WheelSpeed
- **HolonomicController**: 메카넘 휠. 2차 계획법으로 잔여 "net force" 최소화.
  휠 조인트에 `isaacmecanumwheel:radius`, `isaacmecanumwheel:angle` 속성 필요
  → `HolonomicRobotUsdSetup` 클래스가 자동 처리
- **AckermannController**: 조향 차량. ROS 2 튜토리얼에 Twist→AckermannDriveStamped 변환 예제
- 상위 컨트롤러: `WheelBasePoseController(open_loop_wheel_controller=..., is_holonomic=False)`
  → `forward(start_position, start_orientation, goal_position)`

## 7. 예제 / 에셋
- **인터랙티브 예제**: Window > Examples > Robotics Examples
  (카테고리별. Information/Controls/Links 패널에서 소스코드·폴더·문서 바로가기)
- **Standalone 예제**: `<isaac_sim_root>/standalone_examples/` → `./python.sh <path>`
- 에셋 루트 설정: `persistent.isaac.asset_root.default`. Content Browser에서 탐색.
  로딩 진행 상황: `omni.activity.ui` 확장 + Window > Utilities > Activity Progress
  (로봇은 수 분, 대형 환경은 10분 이상 걸릴 수 있음)
- 주요 에셋 카테고리: Robots, Props, Environments(Simple Grid/Room, Warehouse, Hospital, Office,
  JetRacer Track), Sensors(카메라·깊이·RTX Lidar·촉각), Featured, 3rd-party SimReady, NuRec(뉴럴 볼륨)
- 자주 쓰는 경로:
  - `/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd`
  - `/Isaac/Robots/UniversalRobots/ur10e/ur10e.usd`
  - `/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd`
  - `/Isaac/Environments/Simple_Warehouse/warehouse_with_forklifts.usd`
  - `/Isaac/Environments/Grid/default_environment.usd`
  - `/Isaac/Sensors/Intel/RealSense/rsd455.usd`
  - `/Isaac/Props/UIElements/frame_prim.usd` (타깃 표시용 좌표축)
  - `/Isaac/Samples/Rigging/Manipulator/configure_manipulator/ur10e/ur/ur_gripper.usd`

관련: [[isaacsim-sensors-camera]], [[isaacsim-manipulator-pickplace]]
