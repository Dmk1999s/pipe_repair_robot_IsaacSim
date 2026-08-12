# Isaac Sim 5.1 — 개발 도구 / 검증 / 확장 / Isaac Lab / Cortex

출처: `development_tools/*`, `utilities/*`, `robot_setup/*`, `isaac_lab_tutorials/*`,
`cortex_tutorials/*`, `importer_exporter/*`, `gui/*`

## 1. 개발 환경
### VS Code
- **Isaac Sim VS Code Edition** 확장(마켓플레이스) + Isaac Sim 쪽 `isaacsim.code_editor.vscode`
  → 실행 중인 Isaac Sim의 Python 환경에서 코드 실행, 스니펫 삽입, 확장 템플릿 생성
- 설치 폴더에 `.vscode/{launch.json, settings.json, tasks.json}` 제공
  - `Python: Current File` — standalone 스크립트 디버그 (Linux만 지원)
  - `Python: Attach` — 실행 중인 Isaac Sim에 붙기 (`omni.kit.debug.vscode` 확장 활성화 필요)
  - `(Linux) isaac-sim` — 디버거 붙인 채 본체 실행
  - `python.pythonPath = ${workspaceFolder}/kit/python/bin/python3`
  - `tasks.json`의 `setup_python_env`가 `.standalone_examples.env` 생성
- 커맨드라인 인자는 launch.json의 `args`에 추가
  (예: `--/persistent/isaac/asset_root/default="omniverse://my_server"`)
- 디버거 host/port: `--/exts/omni.kit.debug.python/host`, `/port`

### Docker 안 스크립트 디버깅
```bash
./python.sh -m pip install debugpy
./python.sh -m debugpy --wait-for-client --listen 0.0.0.0:5678 <script.py>
```
VS Code는 `debugpy` Remote Attach (localhost:5678) + **pathMappings**
(`localRoot: ${workspaceFolder}/_build/linux-x86_64/release` ↔ `remoteRoot: /isaac-sim`)

### Jupyter
- `isaacsim.code_editor.jupyter` — 인터랙티브 스크립팅 및 standalone Isaac Sim을 노트북에서 구동

### Carb 설정 변경 4가지 방법
1. **Script Editor**(임시): `carb.settings.get_settings().set("/exts/<ext>/data/foo", True)`
   후 `set_extension_enabled_immediate(ext, False/True)`로 확장 재시작
2. **커맨드라인 인자**(임시): `./isaac-sim.sh --/exts/<ext>/data/foo=true`
3. **확장 `.toml`**(영구): `<root>/exts/<ext>/config/extension.toml`의 `[settings]`
4. **`.kit` 파일**(영구, 앱 단위): `<root>/apps/isaacsim.exp.full.kit`의 `[settings]`

### 프로파일링
- **Tracy** 프로파일러 (`utilities/debugging/profiling_performance.md`), 프로파일 존 수동 삽입 가능
- Linux는 `nvidia-smi`, Windows는 작업 관리자 성능 탭

## 2. 검증 — Asset Validator (`isaacsim.asset.validation`)
Window > Asset Validator. 3개 카테고리:
### IsaacSim.PhysicsRules
- `PhysicsJointHasDriveOrMimicAPI` — 비고정 조인트는 drive 또는 mimic API 필수.
  **둘 다 있으면 drive stiffness/damping은 0.0이어야 함**
- `PhysicsJointMaxVelocity` — PhysxJointAPI에 max joint velocity가 양수로 정의
- `PhysicsDriveAndJointState` — drive max force가 유한 양수, drive 타깃과 joint state 값 일치(1e-2)
- `DriveJointValueReasonable` — stiffness 0~1e6, **mimic 조인트는 stiffness/damping = 0**,
  natural frequency 경고 임계 500 Hz
- `JointHasCorrectTransformAndState` — 조인트 변환/상태가 연결 바디와 일관
- `JointHasJointStateAPI` — prismatic="linear", revolute="angular" JointStateAPI
- `MimicAPICheck` — reference joint 타깃 1개, gear ratio/natural freq/damping ratio 정의·비영,
  기어비 부호에 따른 limit 호환성
- `RigidBodyHasMassAPI` — mass·대각 관성 비영, principal axes 정규화
- `RigidBodyHasCollider`, `NonAdjacentCollisionMeshesDoNotClash`(시뮬로 검사),
  `InvisibleCollisionMeshHasPurposeGuide`, `HasArticulationRoot`
### IsaacSim.RobotRules
- `RobotNaming` — `<Manufacturer>/<robot>/<robot.usd>` (또는 version 폴더 포함), 최소 3단계 중첩
- `RobotSchema` — default prim에 RobotAPI, robotLinks/robotJoints 관계 존재
- `CheckRobotRelationships` — 관계가 **prepend** 되어야 함
- `VerifyRobotPhysicsAttributesSourceLayer` / `...SchemaSourceLayer`
  — `physics:` 속성과 Physx/Physics 스키마는 **`_physics.usd` 레이어**에 작성
- `NoOverrides`, `JointsExist`, `LinksExist`, `ThumbnailExists`(`.thumbs/256x256/<name>.png`), `CleanFolder`
### IsaacSim.SimReadyAssetRules
- `NoNestedMaterials`, `MaterialsOnTopLevelOnly` (모든 머티리얼은 최상위 `Looks` 아래)

## 3. Robot Wizard [Beta] (`Window > Robot Wizard`)
CAD 임포트한 단순 로봇 셋업 자동화. 단계:
Add Robot → Prepare Files → **Robot Hierarchy**(같은 링크로 움직이는 메시들을 한 부모로 묶기;
`Mark as Reference Child`로 링크 원점 기준 지정) → Add Colliders(근사 방식 선택) →
Add Joints & Drives → **Save Robot**(Articulation Root 지정: 고정형=고정 조인트, 이동형=chassis)
결과물:
```
<root>/configurations/<name>_base.usd      # 메시/계층
<root>/configurations/<name>_physics.usd   # 리지드바디/콜라이더/조인트/드라이브
<root>/configurations/<name>_robot.usd     # 로봇 스키마
<root>/<name>.usd                          # variant 통합
```
- 각 페이지에서는 실제 prim이 만들어지지 않고, 다음 단계 버튼을 눌러야 반영됨.
- 최소 환경(ground/light/PhysicsScene)을 Default Prim 밖에 추가 옵션 — 디버깅용.

## 4. 에셋 최적화 실전 (튜토리얼 12, Jetbot 예: 40 → 64 FPS)
- Edit > Preferences > Stage > Authoring > **Inherit Parent Transform** 체크
- 새 스테이지에 원본을 **sublayer**로 넣고 작업 (원본 훼손 방지)
- **Mesh Merge Tool**(Tools > Robotics > Asset Editors > Mesh Merge Tool):
  링크별로 메시 병합, `Combine Materials` 체크 + Looks 경로 지정
- 병합 결과를 `Visuals` scope에 두고, 각 링크에서 **내부 참조**(Add > Reference, Asset Path 비우고
  prim path만 지정)로 가리키게 함
- 동일 형상(좌/우 바퀴)은 하나의 `Visuals/wheel`을 공유하도록 참조 경로 변경
- 마지막에 Visuals prim들을 **Instanceable** 체크 (참조 위에만 적용 가능, 자식 속성 수정 불가)
- 기타: **라이트 10개 초과 시 샘플 기반 조명으로 전환되어 급격히 느려짐**,
  반투명 머티리얼 최소화, 바퀴는 cylinder/sphere 콜라이더

## 5. Instanceable Assets (메모리 절감)
- 요구 계층: **모든 mesh prim은 부모 Xform을 가져야** instanceable 지정 가능
```
Robot/Collisions/Sphere          ✗
Robot/Collisions/Sphere_Xform/Sphere   ✓   (참조도 Xform 쪽으로 이동)
```
- URDF/MJCF 임포터의 **Create Instanceable Asset** 옵션 + `Instanceable USD Path`
  (기본 `./instanceable_meshes.usd`) → 메시가 별도 USD로 분리되고 마스터가 참조
- 기존 에셋 변환 유틸: `create_parent_xforms(asset_usd_path, source_prim_path, save_as_path)`,
  `convert_asset_instanceable(..., create_xforms=True)` (문서에 전체 코드 있음)
- ⚠ 참조된 메시의 USD Relationship(비주얼/피직스 머티리얼, 충돌 필터쌍)은 제거됨
  → 이런 관계는 **부모 Xform에 설정**할 것
- ⚠ **Lula Robot Description Editor는 instanceable 에셋 미지원** (Instanceable 체크 해제 후 작업)

## 6. Cloner (`isaacsim.core.cloner`) — 대규모 병렬 환경
```python
from isaacsim.core.cloner import Cloner, GridCloner
cloner = GridCloner(spacing=3)
paths = cloner.generate_paths("/World/Cube", 4)     # /World/Cube_0..3
cloner.clone(source_prim_path="/World/Cube_0", prim_paths=paths,
             positions=..., orientations=...,
             replicate_physics=True,                 # PhysX 레벨 복제(빠름)
             base_env_path="/World/Ants", root_path="/World/Ants/Ant_",
             copy_from_source=False)                 # False=USD Inherits(빠름), True=독립 복사본
```
- `replicate_physics=True`면 **런타임 shape 속성 변경 불가** (마찰/반발 랜덤화하려면 끄기)
- 접근: `XFormPrimView("/World/Cube_*")` → `get_world_poses()/set_world_poses()`
- 예제: `standalone_examples/api/isaacsim.core.cloner/cloner_ants.py`

## 7. Isaac Cortex (`isaacsim.cortex.framework` / `.behaviors`)
- **standalone Python 워크플로우 전용.**
- 6단계 파이프라인(60Hz): Perception → World modeling(USD) → **Logical state monitoring**
  → **Decision making(Decider Network)** → Command API(policies) → Control
- **belief world vs reality world** 분리: 시뮬레이션을 로봇의 "믿음(mind)"으로 사용.
  2~5단계는 물리 현실 없이도 동작 → 시뮬레이션 우선 개발 후 ROS로 인지/제어 연결.
- **Commander** 추상화: articulation의 부분 관절을 담당하는 상위 명령 인터페이스.
  예) `CortexFranka` → `robot.arm`(MotionCommander, RMPflow 래핑), `robot.gripper`(FrankaGripper)
  `robot.arm.send(MotionCommand(target_pose))` / `robot.arm.send_end_effector(pose)` / `robot.gripper.close()`
- 회전행렬 헬퍼:
```python
import isaacsim.cortex.framework.math_util as math_util
R = robot.arm.get_fk_R(); ax, ay, az = math_util.unpack_R(R)
target_az = np.array([0,0,-1.0])
target_ay = math_util.normalized(math_util.proj_orth(ay, target_az))
target_ax = np.cross(target_ay, target_az)
target_R  = math_util.pack_R(target_ax, target_ay, target_az)
```
- 예제 시퀀스: Decider Networks → Peck Games → Franka Block Stacking → UR10 Bin Stacking
- ⚠ ROS 동기화 Cortex 샘플은 **25 FPS 아래로 떨어지면 태스크 수행 실패**.

## 8. MJCF Importer (`isaacsim.asset.importer.mjcf`)
- File > Import. 옵션은 URDF와 유사: Model(Create in Stage / reference), Links(Moveable/Static base),
  Default Density(0이면 자동), Colliders(Visualize Collision Geometry, Allow self-collision)
- 특수문자는 `_`로 치환, 언더스코어로 시작하면 `a` 접두. **MJCF에서 미리 이름 정리 권장.**
- Python API 예: `./python.sh standalone_examples/api/isaacsim.asset.importer.urdf/urdf_import.py` (URDF 버전)

## 9. 확장 템플릿 / 커스텀 확장
- **Extension Template Generator** (`isaacsim.examples.extension`):
  Loaded Scenario / Scripting / Configuration Tooling / UI Component Library 템플릿
- VS Code에서 고급 템플릿 생성 가능 (`utilities/vscode_extension_template_generator.md`)
- 커스텀 인터랙티브 예제: `BaseSample` + `BaseSampleUITemplate` 상속 후 examples browser에 등록
- 커스텀 OmniGraph 노드: Python(`omnigraph/omnigraph_custom_python_nodes.md`) / C++
- Omniverse Commands Tool 확장: UI에서 값을 바꾸면 대응되는 omni command를 알려줌 (스크립팅에 유용)

## 10. GUI 참고
- 주요 단축키: `gui/reference_keyboard_shortcuts.md` (뷰포트 조작/선택/파일/애니메이션, 커스텀 핫키)
- Layout Templates(`gui/layouts.md`) — Synthetic Data Generation 레이아웃 등
- Preferences(`gui/preferences.md`) — Stage/Authoring, Rendering, Material, Template Startup 등
- Selection Modes, Create/Replicator 메뉴

관련: [[isaacsim-versions-perf]], [[isaacsim-manipulator-pickplace]]
