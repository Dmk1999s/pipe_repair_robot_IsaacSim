# Isaac Sim 5.1 — 센서 / 카메라 / 물리 기초 / USD 규약

출처: `sensors/*`, `reference_material/reference_conventions.md`, `physics/simulation_fundamentals.md`,
`omniverse_usd/robot_schema.md`

## 1. Isaac Sim 규약 (★ 반드시 외울 것)
### 단위
길이 m / 질량 kg / 시간 s / 힘 N / 물리 타임스텝 기본 1/60 s
Linear drive stiffness `kg/s²`, angular `kg·m²/(s²·angle)`, linear damping `kg/s`, 관성 `kg·m²`

### 쿼터니언 순서 — **API마다 다름!**
| API | 표현 |
|---|---|
| Isaac Sim Core | (QW, QX, QY, QZ) |
| USD | (QW, QX, QY, QZ) |
| PhysX | (QX, QY, QZ, QW) |
| Dynamic Control | (QX, QY, QZ, QW) |

### 각도
Isaac Sim Core = **radian**, USD = **degree**, PhysX/Dynamic Control = radian.
행렬은 Core/USD 모두 row-major.

### 축
- 월드: **+Z up, +X forward** (오른손 좌표계)
- 카메라(기본/Isaac): **+Y up, -Z forward**
- USD 축(카메라 prim의 Property 패널 표시): +Y up, -Z forward
- **ROS 카메라 축**: -Y up, +Z forward
  → Isaac 카메라 → ROS 카메라 변환 = **X축 기준 180° 회전**
  → 정적 변환 쿼터니언 `[0.5, -0.5, 0.5, 0.5]` (w,x,y,z)로 `{frame}` ↔ `{frame}_world` 연결
- 이미지 좌표 (0,0) = 좌상단

## 2. 카메라 (`isaacsim.sensors.camera.Camera`)
```python
from isaacsim.sensors.camera import Camera
import isaacsim.core.utils.numpy.rotations as rot_utils

camera = Camera(prim_path="/World/camera",
                position=np.array([0.,0.,25.]),
                frequency=20, resolution=(256,256),
                orientation=rot_utils.euler_angles_to_quats(np.array([0,90,0]), degrees=True))
camera.initialize()           # world.reset() 이후에 호출
camera.add_motion_vectors_to_frame()

frame = camera.get_current_frame()   # dict (rgba, motion_vectors, ...)
rgb = camera.get_rgba()[:, :, :3]
pts2d = camera.get_image_coords_from_world_points(np.array([p1, p2]))
pts3d = camera.get_world_points_from_image_coords(pts2d, depths)
```
- 카메라 데이터는 **render product**를 통해 취득. 뷰포트 자체도 render product.
- Camera 클래스는 **월드 축 규약**으로 position/orientation을 받음.
- prim에 부착: Xform prim을 만들고 그 하위에 `Camera(prim_path=f"{name}/camera")` → 부모 pose 상속.

### 렌즈/캘리브레이션
- Omniverse는 **OpenCV pinhole / fisheye 왜곡 모델을 네이티브 지원**.
  (기존 `fisheyePolynomial` 근사 API는 deprecated. 5.0부터 RTX Camera Projection 속성 →
   `OmniLensDistortion` 스키마로 대체)
```python
((fx,_,cx),(_,fy,cy),(_,_,_)) = camera_matrix
horizontal_aperture = pixel_size * width  * 1e-6     # pixel_size 단위 µm → m
vertical_aperture   = pixel_size * height * 1e-6
focal_length = (pixel_size*fx*1e-6 + pixel_size*fy*1e-6)/2
camera.set_focal_length(focal_length); camera.set_focus_distance(focus_distance)
camera.set_lens_aperture(f_stop)      # f_stop=0.0 → 피사계심도 끄기(디버깅용)
camera.set_horizontal_aperture(horizontal_aperture); camera.set_vertical_aperture(vertical_aperture)
camera.set_clipping_range(0.05, 1.0e5)
camera.set_opencv_pinhole_properties(cx=cx, cy=cy, fx=fx, fy=fy, pinhole=dist_coeffs)
# 또는 camera.set_opencv_fisheye_properties(...)
```
- Extrinsic: 툴킷 변환행렬 → `position=np.array([-dZ, dX, dY])`,
  `orientation=np.array([rW, -rZ, rX, rY])` (툴킷 규약에 따라 다름)
- 예제: `standalone_examples/api/isaacsim.sensors.camera/{camera,camera_opencv_pinhole,camera_opencv_fisheye}.py`
- **뷰포트 해상도는 정사각 픽셀만 지원** → 해상도 종횡비 = aperture 비율이어야 함.
- **Camera Inspector** (Tools > Sensors > Camera Inspector): 다중 뷰포트, 커버리지 확인,
  원하는 프레임 규약으로 pose 조회/설정, Camera State 텍스트박스 복사.

## 3. Depth 센서
- `isaacsim.sensors.camera.SingleViewDepthSensor` — 단일 카메라 뷰 + 후처리로 스테레오 depth 모델링
  (Render Settings > Post Processing > Depth Sensor). RGB Depth Output Mode에 Disparity 등.
- `SingleViewDepthSensorAsset(prim_path=..., asset_path=...)` → `.initialize()`,
  `.get_all_depth_sensor_paths()`, `.get_child_depth_sensor(cam_path)`, `.attach_annotator("DepthSensorDistance")`
- 실물 자산: `/Isaac/Sensors/Intel/RealSense/rsd455.usd` (RGB/좌우 IR/IMU + `Camera_Pseudo_Depth`)
  ※ Pseudo Depth는 실제 스테레오 알고리즘이 아니라 씬 깊이를 그대로 주는 편의 카메라.
- 어노테이터: `DepthSensorDistance`, `DistanceToImagePlane`
- 예제: `camera_stereoscopic_depth.py`, `camera_add_depth_sensor.py`

## 4. 다른 센서들 (요약)
- 물리 기반(`isaacsim.sensors.physics`): Contact Sensor, IMU, Effort Sensor, Articulation Joint(force) Sensor, Proximity
- PhysX SDK(`isaacsim.sensors.physx`): Lidar(레거시), Generic, Lightbeam
- RTX(`isaacsim.sensors.rtx`): RTX Lidar(OmniLidar prim), RTX Radar(OmniRadar), RTX 센서 어노테이터,
  비시각 재질(Non-Visual Materials), 배치/캘리브레이션 도구(`isaacsim.sensors.rtx.placement`)
- RTX Lidar 데이터 취득: render product 생성 → annotator 초기화 → **annotator 초기화 후** render product attach →
  timeline play 후 프레임마다 `get_data()`

## 5. 물리 시뮬레이션 기초
### 타임라인
- 시뮬레이션 시간 ≠ 실시간. 기본적으로 실시간 매칭 리미터가 걸려 있음.
- 물리 스텝 수 > 렌더 프레임 수인 경우가 일반적 (예: 물리 120/s, 렌더 60fps → 프레임당 2 물리 스텝)
- 렌더 프레임레이트: Layer 탭 > Root Layer > **Timecodes per second**
- 물리 스텝: **Physics Scene의 Simulation Steps per Second** (없으면 기본 60)
- 이벤트 스트림: Simulation Events / Frame update (pre·post render).
  OmniGraph는 보통 pre-render에 업데이트되지만 물리 스텝마다 돌게 할 수 있음
  (그래프 pipeline stage를 `PipelineStageOnDemand`로 두고 **On Physics Step** 노드 사용).

### 구성요소
- **Rigid Body**: Add > Physics > Rigid Body. 중력/외력의 영향.
- **Collider**: Add > Physics > Collider. 없으면 통과함. 정적 물체엔 collider만.
- **CCD**: 빠른 물체의 터널링 방지. **Physics Scene과 rigid body 양쪽에서 활성화**해야 함.
- Collider 근사: Convex Hull(기본) / Convex Decomposition / Bounding Cube / Sphere /
  Sphere Approximation / **SDF Mesh**(삼각 메시 직접 사용). Triangle mesh·mesh simplification은
  rigid body에서 미지원 → convex hull로 폴백.
- **Contact Offset / Rest Offset** (Collider Advanced):
  - Rest Offset: 충돌 지오메트리 팽창/수축 (시각 메시와 불일치 보정)
  - Contact Offset: 접촉 제약 생성 시작 거리. 크면 정확·느림, 작으면 지터/누락/터널링.
- **Physics Material** (Create > Physics > Physics Material > Rigid Body Material):
  static/dynamic friction, restitution, compliant contact(스프링-댐퍼).
  - **Combine Mode 우선순위**: `average < min < multiply < max` (양쪽 모드가 다르면 우선순위 높은 쪽)
- **Joint**: Body0가 articulation 트리의 **부모**여야 함 (PhysX↔USD 1:1 대응 보장).
  UI로 생성 시 두 번째 선택한 body 위치에 joint 프레임이 생김.
  revolute 기본 축 X, 한계는 기본 없음, **USD는 degree**.
- **Articulation**: jointed body용 최적화 구조. **kinematic tree만 가능**(루프 불가).
- **Residual**: Add > Physics > Residual Reporting → Simulation Data Visualizer에서 수렴도 확인.
  (Simulation Scene / Articulation Root / Joint가 지원)

### USD 물리 스키마 접근 패턴
```python
from pxr import UsdPhysics, PhysxSchema
api = UsdPhysics.SomeAPI(prim) or UsdPhysics.SomeAPI.Apply(prim)
attr = api.GetSomeAttr() or api.CreateSomeAttr(1.0)
attr.Set(10.0)
```
- 속성 이름 규칙 `schema:attribute` (예: `physics:velocity` → `UsdPhysics.RigidBodyAPI(prim).GetVelocityAttr()`).
  UI에서 속성에 마우스를 올리면 툴팁에 실제 이름이 나옴.
- C++ 문서의 `TfToken` 인자는 Python에서 그냥 문자열로 넣으면 됨 (예: joint state의 "Prismatic"/"Angular").

## 6. Robot Schema (실험적, `usd.schema.isaac.robot_schema`)
- `IsaacRobotAPI`(루트): Description, **Namespace**, Robot Links(base부터 순서), Robot Joints
- `IsaacLinkAPI`(모든 링크), `IsaacJointAPI`(모든 조인트) — Name Override, DOF Offset
- `IsaacReferencePointAPI`: 툴/센서 부착점 (Description, Forward Axis)
- URDF/MJCF 임포터로 들어온 에셋은 자동 적용. 구버전 에셋은 수동(Property > + Add > Edit API Schema).
- **서브로봇 합성**: 서브로봇 루트를 부모 로봇의 links/joints 리스트에 추가 (그리퍼 부착이 이 방식)
- 유틸: `GenerateRobotLinkTree(stage, prim)`, `PrintRobotTree`, `GetAllRobotJoints/Links`,
  `GetJointPose`, `GetLinksFromJoint`
- 권장: 스키마는 **별도 레이어**(`configuration/<asset>_robot_schema.usda`)에 저장 후 sublayer로 로드.

관련: [[isaacsim-ros2-omnigraph]], [[isaacsim-core-api]]
