# M0609 프로젝트 적용 치트시트

대상: `/home/rokey/cobot3_ws/isaacpjt/M0609` (두산 M0609 + OnRobot RG2, Isaac Sim 5.1 standalone)
현재 구조: `rmpflow/{m0609_description.yaml, m0609_rmpflow_common.yaml,
m0609_rmpflow_controller.py, m0609_pick_place_controller.py}` + `Collected_m0609_camera/`

## 1. M0609은 RMPflow 기본 지원 로봇이 아니다
`load_supported_motion_policy_config()` 지원 목록:
Franka, UR3~UR16e, Rizon4, Cobotta_Pro_900/1300, RS007L/N·RS013N·RS025N·RS080N,
FestoCobot, Techman_TM12, Kuka_KR210, Fanuc_CRX10IAL — **M0609 없음.**
→ 이미 하고 있듯 config 3종(URDF + robot_description.yaml + rmpflow_common.yaml)을 직접 유지해야 함.
표준 참고 경로: `<mg_ext>/motion_policy_configs/<robot>/...`
참고 튜토리얼: `text/manipulators/manipulators_configure_rmpflow_denso.md` (Cobotta Pro 900, 6DOF 사례)

## 2. config 점검 체크리스트 (문제 생기면 여기부터)
- [ ] `joint_limit_buffers` 배열 길이 = **c-space DOF 수(6)**
- [ ] `joint_velocity_cap_rmp.max_velocity` = **M0609 URDF의 joint velocity limit**과 일치
      (`velocity_damping_region`은 limit의 30% 정도가 문서 권장 예시)
- [ ] `robot_description.yaml`의 **Active Joint = 팔 6개, Fixed Joint = RG2 그리퍼 관절**
- [ ] Fixed joint(그리퍼) 기본값 = **열린 상태** (닫힌 자세는 열린 자세의 convex hull 안)
- [ ] `cspace_to_urdf_rules`의 기본 자세 = **M0609 USD의 초기 포즈와 동일**
      (다르면 태스크 초기화 시 그 값으로 관절 리셋)
- [ ] 기본 자세는 로봇 **앞쪽(+X)**, joint limit에서 먼 곳
- [ ] `body_cylinders`(베이스 캡슐) + `body_collision_controllers`(EE 근처 구) 로 자기충돌 방지
- [ ] EE 프레임(`end_effector_frame_name`)이 **URDF에 실제 존재**하는지.
      RG2 파지 중심을 쓰려면 URDF에 fixed joint로 `gripper_center` 링크 추가:
```xml
<link name="gripper_center"/>
<joint name="gripper_center_joint" type="fixed">
  <origin rpy="0 0 0" xyz="0 0 0.XX"/>
  <parent link="onrobot_rg2_base_link"/><child link="gripper_center"/>
</joint>
```
- [ ] 그리퍼 조립 후 **USD→URDF 재출력**했는가 (File > Export URDF)

## 3. 검증 도구 3종
1. **Lula Test Widget** (Tools > Robotics > Lula Test Widget) — config 조합만 따로 검증
2. **RMPflow 디버깅**:
```python
rmpflow.visualize_collision_spheres()
rmpflow.set_ignore_state_updates(True)     # 시뮬 상태 무시 → RMPflow 문제 vs PD게인 문제 구분
```
3. **Gain Tuner** (Tools > Robotics > Asset Editors > Gain Tuner) — Nat.Freq 0.5 / Damping Ratio 1.0 시작

## 4. Pick & Place 실패할 때 보는 곳
| 증상 | 확인 |
|---|---|
| EE가 엉뚱한 위치로 감 | `end_effector_offset` 튜닝 (EE 링크 ↔ 실제 파지점) |
| 단계가 너무 빠르/느림 | `events_dt` 10개 값. **성공 판정이 아니라 dt 기반 상태머신**임 |
| 물체가 미끄러짐 | fingertip **physics material 마찰(1.0)**, `finger_joint` Max Force, |
| | **Physics Scene의 Time Steps Per Second 증가**(60→80+) |
| 그리퍼가 물체를 파고듦 | 5.1의 "articulation 접촉을 마지막에 푸는" PhysX 옵션 검토, contact/rest offset |
| 로봇이 지령을 못 따라감 | PD 게인 (Gain Tuner). RMPflow 출력은 정상인지 위 2번으로 분리 확인 |
| 모션이 진동/오버슈트 | `joint_velocity_cap_rmp`, `damping_rmp`, articulation solver iteration(64/4) |

## 5. 카메라 (Collected_m0609_camera)
- `isaacsim.sensors.camera.Camera`는 **월드 축(+Z up, +X forward)** 규약으로 pose를 받음
- 카메라 prim 자체는 **+Y up / -Z forward**, ROS는 **-Y up / +Z forward**
  → Isaac↔ROS 변환 = X축 180° 회전, 정적 TF 쿼터니언 `[0.5, -0.5, 0.5, 0.5]` (w,x,y,z)
- OpenCV 내부파라미터 적용:
```python
horizontal_aperture = pixel_size * width * 1e-6
focal_length = (pixel_size*fx*1e-6 + pixel_size*fy*1e-6)/2
camera.set_focal_length(focal_length); camera.set_horizontal_aperture(horizontal_aperture)
camera.set_opencv_pinhole_properties(cx=cx, cy=cy, fx=fx, fy=fy, pinhole=dist)
camera.set_lens_aperture(0.0)     # 피사계심도 끄기(디버깅)
```
- 색 판정(현재 `6_pick_place_color.py`)에 쓰는 RGB는 `camera.get_rgba()[:, :, :3]`
- 해상도 종횡비 = aperture 비율이어야 함(정사각 픽셀만 지원)

## 6. Standalone 루프 관용구 (문서 표준형)
```python
my_world = World(stage_units_in_meters=1.0, physics_dt=1/200, rendering_dt=20/200)
my_world.reset()
reset_needed = False
while simulation_app.is_running():
    my_world.step(render=True)
    if my_world.is_stopped(): reset_needed = True
    if my_world.is_playing():
        if reset_needed:
            my_world.reset(); my_controller.reset(); reset_needed = False
        obs = my_world.get_observations()
        ...
simulation_app.close()
```
- `world.reset()`은 **articulation 관련 조회 전에 반드시** (physics handle 전파)
- **World/SimulationContext보다 OmniGraph를 먼저 생성**할 것 (알려진 이슈)
- STOP→PLAY 반복 시 `AttributeError: 'NoneType'` → reset으로 해결

## 7. ROS 2 붙일 때 (필요해지면)
- 그래프 단축: Tools > Robotics > ROS 2 OmniGraphs > JointStates / Camera / Clock / TF Publisher
- 관절 제어: `/joint_command` 구독 → `IsaacArticulationController`,
  position 제어 관절은 stiffness ≫ damping, velocity 제어 관절은 stiffness = 0,
  한 메시지에 섞으려면 해당 없는 값은 `float('nan')`
- Isaac Sim 5.1은 **Python 3.11** — rclpy/커스텀 메시지는 3.11로 빌드된 워크스페이스 필요
- RViz에서 센서 토픽이 안 보이면 Reliability Policy를 **Best Effort**로

## 8. 성능
- headless: `SimulationApp({"headless": True, "disable_viewport_updates": True})`
- 스레드 제한: `SimulationApp({..., "limit_cpu_threads": 16})`
- 콜라이더 단순화 / self-collision 비활성 / instanceable 메시가 가장 효과 큼

관련: [[isaacsim-motion-generation]], [[isaacsim-manipulator-pickplace]], [[isaacsim-core-api]]
