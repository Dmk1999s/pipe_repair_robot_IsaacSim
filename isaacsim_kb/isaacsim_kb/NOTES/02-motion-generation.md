# Isaac Sim 5.1 — Motion Generation (Lula / RMPflow / IK / RRT / Trajectory)

출처: `manipulators/*`, `manipulators/concepts/*`

패키지: `isaacsim.robot_motion.motion_generation` (구 `omni.isaac.motion_generation`)
설정 파일 위치: `<ext_path>/motion_policy_configs/<robot>/...`

## 1. 구성 파일 3종
| 파일 | 용도 | 필요 알고리즘 |
|---|---|---|
| URDF | 기구학, joint/link 이름, **joint position limit**(필수). mass·inertia·mesh는 무시 | 전부 |
| `robot_description.yaml` (Lula) | c-space 정의(active/fixed joint), 기본 자세, **collision spheres**, accel/jerk limit | 전부 |
| `<robot>_rmpflow_common.yaml` | RMP 파라미터 | RMPflow만 |

- **XRDF**: cuMotion용 설정. Lula robot description의 상위집합. 향후 Lula도 XRDF로 통합 예정.
- 생성 도구: **Tools > Robotics > Lula Robot Description Editor** (Robot Description Editor).
  - Instanceable 에셋 미지원 → `visuals`/`collisions` prim의 Instanceable 체크 해제 후 사용
    (단, 생성된 yaml은 나중에 instanceable 에셋에도 동작함)
  - PLAY 상태에서 사용. Export 전까지 시뮬레이션 정지 금지.

## 2. Active / Fixed Joint (c-space 정의)
- **Active Joint**: Lula가 직접 제어 (팔 관절)
- **Fixed Joint**: 고정으로 간주 (그리퍼 관절) — 런타임 오버라이드 **불가**
  → 그리퍼는 **열린 위치**로 고정값을 주는 게 관례 (닫힌 상태는 열린 상태의 convex hull 안에 들어감)
- Fixed joint 위치 = 로봇의 **기본 자세(default config)**.
  RMPflow는 타깃이 없으면 이 자세로 가고, 있으면 null-space 해소에 이 자세를 선호.
  → 로봇 **앞쪽(+X 관례)**, joint limit에서 먼 자세로 선정할 것.
- `cspace_to_urdf_rules`의 기본값은 매니퓰레이터 USD의 초기 포즈와 **일치**해야 함.
  아니면 태스크 초기화 때 관절을 그 값으로 리셋해야 함.

## 3. Collision Spheres
- Lula는 로봇 표면을 덮는 구(sphere) 집합으로 충돌 회피. 등록된 구는 어떤 장애물과도 교차 불가.
- 추가 방법 3가지: **Add Sphere** / **Connect Spheres**(두 구 사이 보간) / **Generate Spheres**(메시 볼륨 자동 채움, water-tight triangle mesh만).
- 팁: 링크를 감쌀 만큼 크되 과하지 않게. 많을수록 정확하지만 느려짐.
  긴 링크는 양 끝에 생성 후 Connect. Radius Offset 0.03, 링크당 8개 정도가 튜토리얼 기본값.
- 구는 링크 하위 prim으로 스테이지에 생성 → 드래그/반경 수정 가능.

## 4. 인터페이스 계층 (공통 패턴)
```
MotionPolicy / KinematicsSolver / PathPlanner   ← 내부 표현(URDF+yaml)
        ↕  (joint name 매핑)
ArticulationMotionPolicy / ArticulationKinematicsSolver / PathPlannerVisualizer
        ↕
robot Articulation (USD)  → ArticulationAction
```
- `get_active_joints()` / `get_watched_joints()` 로 이름·순서 매핑.
  예: Franka 9DOF 중 RMPflow는 팔 7개만 active, 그리퍼 2개는 제어 안 함
  → 반환 ArticulationAction은 9벡터이며 미제어 관절은 `None`으로 패딩.
- `set_robot_base_pose(pos, quat)`: **베이스가 원점이 아니면 반드시 호출.**
  장애물 위치는 월드 좌표로 조회되기 때문.
- 월드 상태: `add_sphere/add_cuboid/add_capsule(obj)` 로 `isaacsim.core.api.objects` 객체 등록 후
  매 프레임 `update_world()` 호출 → 등록된 객체의 현재 위치를 재조회.
  RMPflow/RRT는 sphere, capsule, cuboid만 지원 (cone 등은 무시 + 경고).

## 5. RMPflow (Riemannian Motion Policy)
반응형·충돌 회피 가속도 정책. Isaac Sim 매니퓰레이터 제어의 기본.

```python
from isaacsim.robot_motion.motion_generation import RmpFlow, ArticulationMotionPolicy
from isaacsim.robot_motion.motion_generation.interface_config_loader import (
    get_supported_robot_policy_pairs, load_supported_motion_policy_config)

rmp_config = load_supported_motion_policy_config("Franka", "RMPflow")   # 지원 로봇은 이 한 줄
rmpflow = RmpFlow(**rmp_config)
# 또는 직접:
rmpflow = RmpFlow(robot_description_path=".../robot_descriptor.yaml",
                  urdf_path=".../lula_franka_gen.urdf",
                  rmpflow_config_path=".../franka_rmpflow_common.yaml",
                  end_effector_frame_name="right_gripper",
                  maximum_substep_size=0.00334)
rmpflow.add_obstacle(FixedCuboid("/World/obstacle", size=.05, position=...))
art_rmp = ArticulationMotionPolicy(articulation, rmpflow)   # (…, physics_dt) 도 가능

# 매 프레임
rmpflow.set_end_effector_target(target_pos, target_quat)
rmpflow.update_world()
rmpflow.set_robot_base_pose(*articulation.get_world_pose())
articulation.apply_action(art_rmp.get_next_articulation_action(step))
```
지원 로봇 (5.1 기준 `get_supported_robot_policy_pairs()`):
Franka, UR3/UR3e/UR5/UR5e/UR10/UR10e/UR16e, Rizon4, Cobotta_Pro_900/1300,
RS007L/RS007N/RS013N/RS025N/RS080N, FestoCobot, Techman_TM12, Kuka_KR210, Fanuc_CRX10IAL
→ **두산 M0609는 미지원. 직접 config 3종을 만들어야 함.**

### 디버깅 기능 (RMPflow 전용)
- `visualize_collision_spheres()` / `stop_visualizing_collision_spheres()`
- `visualize_end_effector_position()` / `stop_visualizing_end_effector()`
- `set_ignore_state_updates(True)`: 시뮬레이터 상태를 무시하고 내부적으로 상태 롤아웃
  → **RMPflow 문제인지 PD 게인(로봇 추종 실패) 문제인지 구분**하는 표준 기법.
- 정지 상태에서는 stateless. `reset()` 존재.

### RMP 종류와 파라미터 (rmpflow_config.yaml)
- `cspace_target_rmp` — 기본 자세로 끌어당김(리던던시 해소). metric_scalar 1~100 권장(전역 스케일 기준).
- `target_rmp` — EE를 위치 타깃으로. accel_p_gain/accel_d_gain/accel_norm_eps,
  metric_alpha_length_scale, min/max_metric_scalar, proximity_metric_boost_*
- `axis_target_rmp` — EE 축 방향 정렬(자세 타깃). 위치 타깃에 근접할수록 부스트.
- `joint_limit_rmp` — URDF joint limit 회피. `joint_limit_buffers`(배열, c-space 크기와 **일치**)로 여유폭.
- `joint_velocity_cap_rmp` — **로봇마다 반드시 조정**. URDF의 joint velocity limit에 맞춤.
  예: limit 1 rad/s → `max_velocity: 1., velocity_damping_region: .3, damping_gain: 1000., metric_weight: 100.`
- `collision_rmp` — 외부 장애물 회피 (repulsion_gain, metric_modulation_radius 등)
- `damping_rmp` — 저크 감소용 추가 감쇠
- `canonical_resolve` — max_acceleration_norm 등
- `body_cylinders` / `body_collision_controllers` — **자기충돌(베이스 vs EE)** 회피.
  body_cylinders = 절대좌표 두 점 + 반경의 캡슐(베이스 근사),
  body_collision_controllers = URDF 프레임에 붙는 구. 이 둘은 서로 충돌 불가.
  ※ 그 외 링크 간 자기충돌은 RMPflow가 처리하지 않음 → joint limit으로 대응하는 게 산업용 관례.

### 새 로봇 튜닝 절차 (요약)
1. Franka(7DOF) 또는 UR10(6DOF) 템플릿에서 시작. 크기 다르면 길이 단위 파라미터 스케일 조정.
   관절 수 다르면 `cspace_target_rmp/robust_position_term_thresh` 조정.
2. `joint_limit_buffers` 길이를 실제 DOF에 맞춤.
3. `joint_velocity_cap_rmp/max_velocity`를 URDF velocity limit에 맞춤.
4. `body_cylinders`/`body_collision_controllers` 설정.
5. 처음부터 튜닝해야 하면: 모든 RMP의 metric_scalar/metric_weight = 0으로 끄고
   cspace_target → target → collision → target(재조정) → axis_target → joint_limit → damping 순으로 켜기.
6. **Lula Test Widget** (Tools > Robotics > Lula Test Widget)으로 config 조합 검증.

### EE 프레임이 URDF에 없을 때
RMPflow의 end_effector_frame_name은 **URDF에 존재하는 프레임**이어야 함. 두 옵션:
1. 런타임에 오프셋 변환을 직접 계산
2. **URDF에 fixed joint로 프레임 추가** (권장)
```xml
<link name="gripper_center"/>
<joint name="gripper_center_joint" type="fixed">
  <origin rpy="0 0 0" xyz="0.0 0.0 0.24"/>
  <parent link="onrobot_rg6_base_link"/><child link="gripper_center"/>
</joint>
```
※ 그리퍼 부착 로봇은 **조립 후 URDF를 다시 내보내야** RMPflow가 올바른 구조를 인식.
   (File > Export URDF — USD to URDF Exporter 확장)

## 6. Lula Kinematics Solver (FK/IK)
```python
from isaacsim.robot_motion.motion_generation import (ArticulationKinematicsSolver,
                                                     LulaKinematicsSolver, interface_config_loader)
ks = LulaKinematicsSolver(robot_description_path=..., urdf_path=...)
# 지원 로봇: interface_config_loader.load_supported_lula_kinematics_solver_config("Franka")
print(ks.get_all_frame_names())      # IK/FK 가능한 프레임 목록 (URDF 유래)
aks = ArticulationKinematicsSolver(articulation, ks, "right_gripper")

ks.set_robot_base_pose(*articulation.get_world_poses())
action, success = aks.compute_inverse_kinematics(target_pos, target_quat)
if success: articulation.apply_action(action)
ee_pos, ee_rot_mat = aks.compute_end_effector_pose()
```
- 충돌 인지 **없음** (collision sphere 불필요).
- 현재 관절값을 warm start로 사용. `set_max_iterations()` 등 설정 존재.
- IK 해만으로 로봇을 보내는 건 데모용 — 경로 품질 보장 안 됨.

## 7. Lula RRT (Path Planner)
- `compute_path(active_joint_positions, watched_joint_positions)` → c-space 웨이포인트 열.
- 선형 보간 시 c-space에서 꺾임 → 단독 사용보다 궤적 생성기와 조합.
- `PathPlannerVisualizer.compute_plan_as_articulation_actions(max_cspace_dist)` 로
  ArticulationAction 리스트 생성.

## 8. Trajectory Generation
- `Trajectory` 인터페이스: start_time / end_time / active_joints / joint_targets(time)
- `ArticulationTrajectory(articulation, trajectory)`:
  `get_action_at_time(t)`, `get_action_sequence(timestep)`
  ※ 추종 시작 전 로봇을 궤적의 **초기 상태로 이동**시켜 놓아야 함.
- `LulaCSpaceTrajectoryGenerator`: c-space 웨이포인트 → 스플라인, 시간 최적(속도/가속/저크 한계 포화).
- `LulaTaskSpaceTrajectoryGenerator`: task-space 타깃 열 + EE 프레임명 → 내부적으로 IK → c-space 생성.
  `lula.TaskSpacePathSpec`로 원호/순수 회전/순수 병진 프리미티브 조합 가능.

## 9. cuRobo / cuMotion
- GPU 가속 모션 플래닝. 별도 설치 필요. XRDF 설정 사용. (`manipulators/manipulators_curobo.md`)

관련: [[isaacsim-core-api]], [[isaacsim-manipulator-pickplace]]
