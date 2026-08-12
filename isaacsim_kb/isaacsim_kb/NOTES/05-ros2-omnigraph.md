# Isaac Sim 5.1 — ROS 2 Bridge & OmniGraph

출처: `ros2_tutorials/*`, `omnigraph/*`, `installation/install_ros.md`

## 1. OmniGraph 기본
- Action Graph: Window > Graph Editors > Action Graph
- 핵심 노드
  - `omni.graph.action.OnPlaybackTick` — 시뮬 재생 중 매 프레임 tick
  - `omni.graph.action.OnTick`, `omni.graph.action.OnImpulseEvent` (수동 트리거)
  - `isaacsim.core.nodes.IsaacReadSimulationTime` (`resetOnStop`으로 리셋 시 0부터)
  - `isaacsim.core.nodes.IsaacReadSystemTime`
  - `isaacsim.core.nodes.IsaacArticulationController`
  - `isaacsim.core.nodes.IsaacSimulationGate` (step N → N프레임마다 다운스트림 tick)
  - `IsaacCreateRenderProduct`, `IsaacRunOneSimulationFrame`
  - `omni.graph.action.OnPhysicsStep` (그래프를 PipelineStageOnDemand로 두고 사용)

### Python으로 그래프 만들기
```python
import omni.graph.core as og
keys = og.Controller.Keys
(graph, nodes, _, _) = og.Controller.edit(
    {"graph_path": "/ActionGraph", "evaluator_name": "execution",
     # "pipeline_stage": og.GraphPipelineStage.GRAPH_PIPELINE_STAGE_ONDEMAND  # 수동 평가
    },
    {
      keys.CREATE_NODES: [("tick", "omni.graph.action.OnPlaybackTick"), ...],
      keys.CONNECT:      [("tick.outputs:tick", "Node.inputs:execIn"), ...],
      keys.SET_VALUES:   [("Node.inputs:topicName", "/clock"), ...],
    })

og.Controller.attribute("/ActionGraph/print.inputs:text").get() / .set(v)
og.Controller.create_node(path, type); og.Controller.connect(src, dst)
graph.evaluate()                      # OnDemand 그래프 수동 실행
graph.change_pipeline_stage(og.GraphPipelineStage.GRAPH_PIPELINE_STAGE_ONDEMAND)
og.Controller.set(og.Controller.attribute("/ActionGraph/OnImpulseEvent.state:enableImpulse"), True)
```
- 참고 예제: `standalone_examples/api/isaacsim.core.api/omnigraph_triggers.py`

### GUI 단축 메뉴 (그래프 자동 생성)
- **Tools > Robotics > Omnigraph Controllers**: Joint Position / Joint Velocity /
  Differential / **Open Loop Gripper** 컨트롤러
  - Gripper Controller: 손가락당 1자유도 EE 전부 지원. Parent Robot, Gripper Root,
    Gripper Joint Names(콤마), Gripper Speed, Open/Close Position Limit(비우면 USD joint limit),
    키보드 O/C/N 제어 옵션.
  - ⚠ 팔+그리퍼를 각각 다른 그래프로 제어하려면 **팔 컨트롤러 그래프에서 그리퍼 관절을 제거**할 것.
- **Tools > Robotics > ROS 2 OmniGraphs**: JointStates / Camera / Clock / TF Publisher /
  Odometry Publisher 등 (ROS 2 bridge 활성화 필요)
- 중복 그래프 검증은 하지 않음 → 씬에서 유일성은 사용자 책임.

## 2. ROS 2 설치/환경 (요약)
- 확장 `isaacsim.ros2.bridge`. Isaac Sim 5.1은 **Python 3.11** 사용 →
  ROS 2 패키지(rclpy·커스텀 메시지)는 `build_ros.sh`로 3.11에 맞춰 빌드하거나 시스템 ROS로 colcon build.
- Linux + Fast DDS 기본. 다중 머신이면 **`FASTRTPS_DEFAULT_PROFILES_FILE`** 를 Isaac Sim 실행 전 설정.
  CycloneDDS 사용도 가능.
- ROS를 source한 터미널에서 Isaac Sim을 실행해야 관련 확장이 보임.

## 3. 관절 제어 (JointStates)
그래프: `OnPlaybackTick` → `ROS2PublishJointState`(`/joint_states`) /
`ROS2SubscribeJointState`(`/joint_command`) → `IsaacArticulationController`
+ `IsaacReadSimulationTime` → publisher의 `timeStamp`

```python
og.Controller.edit({"graph_path": "/ActionGraph", "evaluator_name": "execution"}, {
  keys.CREATE_NODES: [
    ("OnPlaybackTick", "omni.graph.action.OnPlaybackTick"),
    ("PublishJointState", "isaacsim.ros2.bridge.ROS2PublishJointState"),
    ("SubscribeJointState", "isaacsim.ros2.bridge.ROS2SubscribeJointState"),
    ("ArticulationController", "isaacsim.core.nodes.IsaacArticulationController"),
    ("ReadSimTime", "isaacsim.core.nodes.IsaacReadSimulationTime")],
  keys.CONNECT: [
    ("OnPlaybackTick.outputs:tick", "PublishJointState.inputs:execIn"), ...,
    ("ReadSimTime.outputs:simulationTime", "PublishJointState.inputs:timeStamp"),
    ("SubscribeJointState.outputs:jointNames", "ArticulationController.inputs:jointNames"),
    ("SubscribeJointState.outputs:positionCommand", "ArticulationController.inputs:positionCommand"),
    ("SubscribeJointState.outputs:velocityCommand", "ArticulationController.inputs:velocityCommand"),
    ("SubscribeJointState.outputs:effortCommand",  "ArticulationController.inputs:effortCommand")],
  keys.SET_VALUES: [("ArticulationController.inputs:robotPath", "/panda"),
                    ("PublishJointState.inputs:targetPrim", "/panda")]})
```
- **Articulation Root** 위치: 고정 베이스 로봇은 world로의 root joint에, 이동 로봇은 트리가 가장 깊은
  rigid body(torso/chassis_link)에.
- 위치/속도 제어는 관절마다 하나씩만. 같은 articulation 안에서 관절별로 다른 모드는 가능.
  (position: stiffness ≫ damping, velocity: **stiffness = 0**)
- 한 메시지에 섞으려면 해당 모드가 아닌 관절은 `float('nan')`.
- `isaac:nameOverride` prim 속성으로 발행되는 이름 변경 가능.

## 4. Clock
- `ROS2PublishClock` ← `IsaacReadSimulationTime`(또는 `IsaacReadSystemTime`) → `/clock`
- 외부 노드는 `use_sim_time:=true` 필요: `ros2 param set /node_name use_sim_time true`
- `IsaacReadSimulationTime`은 기본적으로 **단조 증가**(정지·재생해도 이어짐).
  0부터 다시 하려면 `resetOnStop=True`.
- Camera Helper / RTX Lidar Helper가 시스템 시간을 쓰게 하려면 `useSystemTime=True`.

## 5. 카메라 퍼블리시
### OmniGraph 방식
`IsaacCreateRenderProduct`(cameraPrim, enabled) → `ROS2CameraHelper`(type, topicName, frameId)
- type: rgb / depth / pointcloud / bounding_box_2d_tight / _loose / bounding_box_3d /
  semantic_segmentation / instance_segmentation
- **Camera Helper 노드 하나당 데이터 타입 하나.** 한 번 활성화(재생)된 뒤에는 타입 변경 불가 →
  새 노드를 쓰거나 스테이지 리로드.
- Helper가 실행 시 `/Render/PostProcessing/SDGPipeline` 그래프를 자동 생성 (세션 한정, 저장 안 됨).
- `ROS2CameraInfoHelper`: K/P/R 계산
  `fx = width*focalLength/horizontalAperture`, `fy = height*focalLength/verticalAperture`,
  `cx = width*0.5`, `cy = height*0.5`. 스테레오면 render product 2개 붙이면 Tx/Ty 자동.
- BoundingBox 퍼블리셔는 `vision_msgs` 필요.

### Python 방식 (`omni.replicator` writer 직접 사용)
```python
import omni.replicator.core as rep
import omni.syntheticdata._syntheticdata as sd
render_product = camera._render_product_path
rv = omni.syntheticdata.SyntheticData.convert_sensor_type_to_rendervar(sd.SensorType.Rgb.name)
writer = rep.writers.get(rv + "ROS2PublishImage")
writer.initialize(frameId=..., nodeNamespace="", queueSize=1, topicName="rgb")
writer.attach([render_product])
gate = omni.syntheticdata.SyntheticData._get_node_path(rv + "IsaacSimulationGate", render_product)
og.Controller.attribute(gate + ".inputs:step").set(int(60/freq))
```
- depth: `sd.SensorType.DistanceToImagePlane.name` + `ROS2PublishImage`
- pointcloud: 같은 rendervar + `ROS2PublishPointCloud` (depth+intrinsic으로 복원, 시맨틱 라벨 미지원)
- camera_info: `rep.writers.get("ROS2PublishCameraInfo")` + `isaacsim.ros2.bridge.read_camera_info(render_product_path=...)`
- **카메라 TF**: `ROS2PublishTransformTree`(카메라 prim) + `ROS2PublishRawTransformTree`
  (parent=`{frame}`, child=`{frame}_world`, rotation=`[0.5,-0.5,0.5,0.5]`) →
  포인트클라우드는 ROS 축 프레임 `{frame}`에 발행.

## 6. TF / Odometry
- `ROS2PublishTransformTree`: `targetPrims`에 **articulation root**를 넣으면 하위 링크가 전부 발행됨.
  `parentPrim`으로 기준 프레임 변경(기본 world). topicName은 반드시 `/tf`.
- articulation root가 잘못 잡히면: 기존 root prim의 Articulation Root 섹션 삭제 →
  원하는 링크에 Physics > Articulation Root 추가 → 저장·리로드.
- `IsaacComputeOdometry`(Chassis Prim) → `ROS2PublishOdometry`(chassisFrameId/odomFrameId)
  + `ROS2PublishRawTransformTree`(parent=odom, child=base_link)
- 그라운드트루스 로컬라이제이션: 추가 RawTransformTree (parent=world, child=odom)
- 확인: `ros2 run tf2_tools view_frames`, Isaac 내부 뷰어는 확장 `isaacsim.ros2.tf_viewer` → Window > TF Viewer

## 7. 퍼블리시 주기 제어
- Action Graph는 시뮬레이션 프레임마다 tick → 발행 주기는 시뮬 FPS의 **약수**로만 가능.
- 일반 노드: `IsaacSimulationGate`의 `step` (2 → 2프레임마다)
- 카메라/RTX Lidar Helper: `frameSkipCount` (11 → 12프레임마다 발행; 내부 게이트 step 자동 설정)
- 시뮬 프레임레이트 설정 두 가지
```python
# (1) carb 설정 — 타임라인 실행률. OnPlaybackTick에 영향. 정지/재생 시 유지 안 됨
carb.settings.get_settings().set_bool("/app/runLoops/main/rateLimitEnabled", True)
carb.settings.get_settings().set_int("/app/runLoops/main/rateLimitFrequency", 60)
carb.settings.get_settings().set_int("/persistent/simulation/minFrameRate", 60)

# (2) 물리 실행률 — IsaacReadSimulationTime에 영향. timeline 정지 상태에서만 설정. 지속됨
timeline.stop(); stage.SetTimeCodesPerSecond(60); timeline.set_target_framerate(60); timeline.play()
```
  ⚠ TimeCodesPerSecond는 씬 재생 전 1회만 설정 가능 (바꾸려면 씬 리로드)
- 확인: `ros2 topic hz /topic`

## 8. Standalone 워크플로우에서의 ROS 2
- `OnImpulseEvent` 노드를 ROS 노드 앞에 두고, 원하는 프레임에만 impulse를 켜서 정밀 제어.
- `ROS2Context` 노드로 Domain ID 지정 (`useDomainIDEnvVar=False`면 노드에 설정한 값 사용).
- 예제: `standalone_examples/api/isaacsim.ros2.bridge/` — clock.py, camera_periodic.py,
  camera_manual.py, carter_stereo.py, moveit.py, subscriber.py
- Standalone은 물리·렌더 스텝을 직접 돌리므로 실시간과 어긋남 → **시뮬레이션 클럭을 기준**으로 판단.

## 9. 자주 겪는 문제
- Depth 이미지가 흑백 극단 → 시야에 "무한" 깊이가 있어 대비가 왜곡됨. FOV/깊이 범위 제한.
- RViz에서 센서 토픽이 안 보임 → Isaac Sim은 **Sensor Data QoS**로 발행.
  RViz Topic > Reliability Policy를 **Best Effort**로 변경.
- QoS Profile 노드: `createProfile`을 먼저 "Custom"으로 바꿔야 다른 필드 저장됨.
- 이미지 토픽 주기가 낮음 → 메시지 크기/DDS 큐 병목. render product 해상도 축소.
- 퍼블리시 주기 이상 → `./isaac-sim.sh --reset-user`, CPU 병목이면 `./isaac-sim.fabric.sh --reset-user`(실험적)
- Nav2 성능: `./isaac-sim.sh --/app/asyncRendering=true --/app/renderFrameTimeout=60 --/app/asyncPhysics=true`
- **노드 설정 후 play 전에 씬을 저장**해야 값이 제대로 반영됨.
- Auto Namespace 기능은 복잡한 계층에서 완전하지 않음 → `ros2 node list`로 확인.
- `OgnROS2CameraHelper: sensor_type == camera_info is deprecated` 경고는 무시 가능
  (→ `ROS2CameraInfoHelper` 사용 권장).

## 10. 기타 ROS 2 기능
- Ackermann 컨트롤러, Nav2 연동, MoveIt 2, 멀티로봇 내비게이션
- Generic Publisher/Subscriber, Generic Server/Client (임의 메시지 타입)
- 커스텀 Python/C++ OmniGraph 노드, 커스텀 메시지
- `ROS2 Simulation Control` (서비스/액션으로 시뮬 재생·정지·스텝 제어)
- Prim 속성 조작 서비스, RTF(Real Time Factor) 발행, 카메라 노이즈 추가(Replicator augmentation)
- 자동 네임스페이스 생성: 그래프를 로봇 prim 하위에 만들면 계층에서 namespace 유추

관련: [[isaacsim-sensors-camera]], [[isaacsim-core-api]]
