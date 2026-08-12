# Isaac Sim 5.1 — 버전/설치/성능/알려진 문제

출처: `overview/release_notes.md`, `overview/known_issues.md`, `overview/extensions_renaming.md`,
`introduction/workflows.md`, `installation/*`, `reference_material/sim_performance_optimization_handbook.md`,
`robot_setup/asset_structure.md`

## 1. 5.1.0 주요 변경점
- Kit **107.3.3**, DGX Spark 지원. Compatibility Checker가 본체에 통합됨.
- **deprecated 확장은 6.0에서 완전 제거 예정.**
- PhysX: 그리퍼용 **joint parameter tuning 튜토리얼** 신설,
  **articulation 접촉 제약을 마지막에 푸는 옵션** 추가 → 그리퍼 관통(penetration) 개선
  (`isaacsim.core.api`에서 PhysX scene attribute로 노출)
- 로봇: Schunk EGK25/EGU50/EZU35/SVH hand, Booster T1 추가. G1 업데이트.
  **UR10e follow target 예제 추가**
- 센서: RTX 센서 semantic segmentation(Object ID) 지원, 비시각 재질을 USD 속성으로 지정,
  IMU 디바이스측 처리(성능↑), MotionBVH 기본 비활성화, 모든 RTX 센서 어노테이터 성능 개선.
  `Camera.set_opencv_*_properties`가 `imageSize`를 올바르게 설정하도록 수정.
- ROS: Simulation Interfaces **v1.1.0(World 서비스)** 지원 —
  GetAvailableWorlds/GetCurrentWorld/LoadWorld/UnloadWorld.
  `--isaac/startup/ros_sim_control_extension=True`로 시작 시 활성화.
  내부 ROS 2 Humble/Jazzy 라이브러리에 common_interfaces, tf2_ros, sensor_msgs_py 포함.
  기본 bridge 라이브러리 설정 = `system_default` (22.04→Humble, 24.04→Jazzy 자동 로드).
  **CameraInfo에서 fy를 항상 fx와 같게 하던 버그 수정**, 타임스탬프 중복/누락 수정.
- Motion generation: **RMPflow collision sphere 시각화가 로봇 위치 변경을 따라가지 않던 버그 수정**
- Robot Assembler: 그리퍼 base prim이 원점이 아닐 때의 배치 문제, scenegraph instancing 문제 수정
- Surface Gripper: 상태를 Enum으로, 배치 업데이트용 C++ 인터페이스, 스레드화로 성능 개선
- Grasp Editor: rigid body가 재스케일되던 문제 수정
- SimulationApp: 종료/시작 시 hang 다수 수정, **Linux에서 DISPLAY 없으면 headless 강제**,
  `close(skip_cleanup=...)` 추가
- 라이브스트리밍은 aarch64 미지원. Docker는 멀티아치 + 기본 rootless 사용자.

## 2. 확장 리네이밍 (4.5) — 마이그레이션 표 (자주 쓰는 것만)
| 구 (≤4.2) | 신 (4.5+) |
|---|---|
| omni.isaac.core | isaacsim.core.api / .prims / .utils |
| omni.isaac.core_nodes | isaacsim.core.nodes |
| omni.isaac.motion_generation | isaacsim.robot_motion.motion_generation |
| omni.isaac.manipulators | isaacsim.robot.manipulators |
| omni.isaac.franka / .universal_robots | isaacsim.robot.manipulators.examples |
| omni.isaac.surface_gripper | isaacsim.robot.surface_gripper |
| omni.isaac.sensor | isaacsim.sensors.camera / .physics / .physx / .rtx |
| omni.isaac.range_sensor, .proximity_sensor | isaacsim.sensors.physx |
| omni.isaac.ros2_bridge | isaacsim.ros2.bridge |
| omni.isaac.ros2_bridge.robot_description | isaacsim.ros2.urdf |
| omni.isaac.tf_viewer | isaacsim.ros2.tf_viewer |
| omni.importer.urdf / omni.exporter.urdf | isaacsim.asset.importer.urdf / isaacsim.asset.exporter.urdf |
| omni.isaac.robot_assembler | isaacsim.robot_setup.assembler |
| omni.isaac.robot_description_editor | isaacsim.robot_setup.lula_editor / .xrdf_editor |
| omni.isaac.gain_tuner | isaacsim.robot_setup.gain_tuner |
| omni.isaac.grasp_editor | isaacsim.robot_setup.grasp_editor |
| omni.isaac.lula / lula_test_widget | isaacsim.robot_motion.lula / .lula_test_widget |
| omni.isaac.nucleus | isaacsim.storage.native |
| omni.isaac.cloner | isaacsim.core.cloner |
| omni.isaac.debug_draw | isaacsim.util.debug_draw |
| omni.isaac.examples | isaacsim.examples.interactive |
| omni.isaac.kit | isaacsim.simulation_app |
| omni.isaac.wheeled_robots | isaacsim.robot.wheeled_robots |
| omni.isaac.cortex | isaacsim.cortex.framework / .behaviors |
| omni.isaac.occupancy_map | isaacsim.asset.gen.omap |
| omni.isaac.utils | isaacsim.core.utils |
| omni.replicator.isaac | isaacsim.replicator.domain_randomization / .examples / .writers |

- **deprecated(리네임 아님)**: `omni.isaac.dynamic_control`, `omni.isaac.examples_nodes`, `omni.isaac.repl`
- **제거됨**: omni.isaac.dofbot, .partition, .physics_inspector, .ocs2, .robot_benchmark 등
- `isaacsim.core.deprecation_manager`가 설정값 자동 복사 + 씬 열 때 OmniGraph 노드 타입 자동 갱신
  (**저장해야 반영**, 참조/페이로드 안의 노드는 재귀 갱신 안 되므로 해당 USD를 직접 열어 저장할 것)
- 확장이 없다고 나오면 `isaacsim.core.utils.extensions.enable_extension(...)`로 수동 활성화

## 3. 세 가지 워크플로우
| | 특징 | 권장 용도 |
|---|---|---|
| GUI | 시각적 도구 | 월드 구축, 로봇 조립, 센서 부착, OmniGraph 시각 프로그래밍, ROS bridge 초기화 |
| Extension | 비동기, hot reload, 적응형 물리 스텝 | 스니펫 테스트, 인터랙티브 GUI, 실시간 민감 앱 |
| Standalone Python | 물리/렌더 스텝 직접 제어, headless | 대규모 RL 학습, 체계적 월드 생성/변형, ROS 발행률 제어 |
- GUI에서 만든 것은 USD로 저장 → standalone에서 열어 Python으로 수정하는 조합이 일반적.

## 4. 설치 / ROS 2 환경
- Isaac Sim 5.1 = **Python 3.11 전용**.
- ROS 2 지원: Ubuntu 24.04 → **Jazzy 권장**, 22.04 → **Humble 권장**(Jazzy도 가능), Windows → Humble
- `ROS_DISTRO` 환경변수로 소싱 여부/배포판 판단. 미설정 시 내부 ROS 2 배포판 사용.
- **Python 3.11로 빌드된 ROS만 소싱한 채로 Isaac Sim 실행할 것.** 아니면 내부 라이브러리 사용.
- rclpy·커스텀 패키지를 쓰려면 워크스페이스를 Python 3.11로 빌드
  (IsaacSim-ros_workspaces 저장소의 Dockerfile / `build_ros.sh` 사용)
- Fast DDS(기본) / Cyclone DDS(`RMW_IMPLEMENTATION=rmw_cyclonedds_cpp`)
- 다중 머신: `FASTRTPS_DEFAULT_PROFILES_FILE` 설정
- bridge 끄기: `apps/isaacsim.exp.full.kit`의 `isaac.startup.ros_bridge_extension = ""`
- 제공 패키지: isaac_tutorials, isaac_moveit, carter_navigation, isaac_ros2_messages,
  isaac_ros_navigation_goal, cmdvel_to_ackermann, h1_fullbody_controller, isaacsim(런치)
- PIP 설치도 가능 (`installation/install_python.md`), Jupyter/VS Code 연동 지원.

## 5. 에셋 구조 (권장 레이아웃)
```
asset.usd                     ← 최종 합성본
  ├─ sublayer  : asset_sim_optimized.usd  (구조/시각)
  ├─ reference : configuration/asset_physics.usd   (물리 — 예외적으로 reference)
  ├─ payload   : configuration/asset_sensors.usd, asset_control.usd, asset_ros.usd
  ├─ sublayer  : configuration/asset_robot_schema.usda
  └─ variants  : 기능 세트 전환 (그리퍼 교체 등)
source/  asset_base.usd (원본 그대로, 수정 금지), parts.usd(메시 1개당 1파일), materials.usd
```
- **feature 작성 워크플로우**: 새 스테이지 → 최적화 에셋을 sublayer로 추가 → 루트 레이어에서 feature 편집
  → **저장 전에 sublayer 제거/비활성화** → 최종 에셋에 payload로 추가 (= "Add-on" 패턴)
- URDF 임포터는 기본적으로 이 구조를 따름. 게인은 physics 레이어에 저장 권장.

## 6. 성능 최적화 체크리스트
### 물리
- `world.set_physics_step_size(dt)` — 작을수록 정확·느림
- `world.set_min_simulation_frame_rate(fps)`
- `world.set_gpu_dynamics_enabled(True)` — GPU 여유 있을 때만 이득
### 에셋
- **Merge Mesh Tool** (Tools > Robotics > Asset Editors > Mesh Merge Tool)
- **Scenegraph instancing** (반복 메시 메모리 절감; 자식은 부모 참조의 속성을 변경 못 함)
- **콜라이더 단순화**: 바퀴는 mesh 대신 cylinder/sphere, 몸통은 cube 근사.
  콜라이더 개수 자체를 줄이고, 필요 없는 건 비활성화.
- **Self-collision 비활성화** (필요 없는 경우 큰 이득)
### 렌더링
- Scene Optimizer 확장, LOD, 컬링
- 머티리얼 끄기 `carb.settings...set_int("/rtx/debugMaterialType", 0)` (되돌리기 -1)
- DLSS: `--/rtx/post/dlss/execMode=` 0 Performance / 1 Balanced / 2 Quality / 3 Auto
  → **SDG는 2(Quality) 권장** (저해상도에서 엣지 아티팩트 방지)
- headless에서 뷰포트 갱신 끄기: `SimulationApp({"headless": True, "disable_viewport_updates": True})`
- 텍스처 스트리밍 예산: Render Settings > Common > Debug > Streaming (기본 GPU 메모리 60%),
  Python은 `/rtx-transient/resourcemanager/texturestreaming/memoryBudget`
### CPU 스레드 (기본은 전부 사용, standalone은 32 제한)
```
./isaac-sim.sh --/plugins/carb.tasking.plugin/threadCount=16 \
               --/plugins/omni.tbb.globalcontrol/maxThreadCount=16
# --/persistent/physics/numThreads
SimulationApp({"headless": False, "limit_cpu_threads": 16})
```
→ 대체로 **32 스레드가 최적**. 과다 스레드는 병목.
### Linux
- CPU governor를 `performance`로: `sudo cpupower frequency-set -g performance`
- 멀티 GPU는 **IOMMU 비활성화** (`amd_iommu=off`)
### 비동기 렌더링 (5.1 신규)
- 정지/일시정지 상태에서 기본 활성 (UI 반응성↑). `isaacsim.core.throttling` 확장이 관리.
- **Replicator SDG에서는 프레임 스킵 유발** → `--/exts/isaacsim.core.throttling/enable_async=false`
### 멀티 GPU 경험칙
- 렌더링하는 카메라 수만큼 GPU 추가 (그 이상은 효율 저하). 카메라가 많을수록 스케일링 좋음.
- SDG는 GPU 2개가 가성비 최적. 4K 이상 단일 카메라는 멀티 GPU 이득.
- **GPU 물리는 GPU 1개만 사용.** 씬 로드 시간은 GPU 수와 무관.

## 7. 알려진 문제 / 자주 겪는 함정 (★ 중요한 것)
- **World/SimulationContext보다 OmniGraph를 먼저 생성**해야 함.
- STOP→START 반복 시 `AttributeError: 'NoneType' ...` → `world.reset()` 계열로 리셋할 것.
- Replicator `Scatter3D` OmniGraph 노드는 World 사용 스테이지에서 **물리를 깨뜨림**.
- `rep.new_layer()`는 시뮬레이션 시나리오에서 문제 유발 가능 → 생략 가능.
- URDF: 링크/조인트/메시 이름에 특수문자·선행 언더스코어·숫자 시작 불가.
  같은 이름의 머티리얼이 여러 개면 하나만 생성됨(색이 뒤섞임).
- USD→URDF Exporter: 콜라이더 메시가 visual에 섞여 들어감, body/joint가 알파벳순으로 기록됨,
  일부 body 이름이 병합으로 덮어써짐, **무한 한계값을 `inf`로 기록** → 파서에 따라 재임포트 실패.
- **Surface Gripper로 articulation root를 가진 물체를 잡으면 실패**
  (`PxD6JointCreate: actors must be different`) → 대상 물체의 Articulation API 비활성화.
- 병렬 메커니즘 그리퍼(Robotiq 2F-85, 2F-C2) 일부 링크가 같이 안 움직이는 문제 존재.
- Gain Tuner가 만든 게인이 지령을 완벽히 추종하지 못할 수 있음(Cobotta Pro 등).
- Physics Inspector의 mimic joint 관련 "failed to find internal joint" 에러는 무시 가능.
- 부모 prim이 body0가 아니면 PhysX 반환값이 USD 값의 **부호 반전**.
- Depth 이미지 노이즈 → Render Settings > Ray Tracing > Anti-Aliasing = None.
- OmniGraph **compound node는 크래시 유발** → 사용 금지 권장.
- `timeCodesPerSecond` 변경 후 writer attach 실패 → 저장·재오픈·재생.
- Franka Open Drawer 예제는 Blackwell GPU에서 `_physics_rate`를 600으로 올려야 동작.
- 로그 줄이기: `--/log/level=error --/log/fileLogLevel=error --/log/outputStreamLevel=error`
- Windows 검은 화면 → `--vulkan`. Ctrl-C로 standalone 종료 시 두 번 눌러야 할 수 있음.
- Isaac Sim 내장 Python에서 **tkinter 미지원**.
- 장기 실행 메모리 누수 완화(실험적):
  `export GLIBC_TUNABLES=glibc.malloc.arena_max=1:glibc.malloc.mmap_max=0:glibc.malloc.mmap_threshold=2147483647`

관련: [[isaacsim-core-api]], [[isaacsim-replicator-sdg]]
