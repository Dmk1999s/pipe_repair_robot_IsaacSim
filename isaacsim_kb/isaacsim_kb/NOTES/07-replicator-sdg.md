# Isaac Sim 5.1 — Replicator / 합성 데이터 생성(SDG)

출처: `replicator_tutorials/*`, `synthetic_data_generation/*`, `action_and_event_data_generation/*`

## 1. 도구 개요 (Tools > Replicator)
- **Semantics Schema Editor**: prim에 시맨틱 라벨 부여/편집. segmentation·bbox 어노테이터에 필수.
  코드: `isaacsim.core.utils.semantics.add_labels(prim, labels=[...], instance_name="class")`
- **Synthetic Data Visualizer**: 뷰포트에서 센서 출력 직접 확인
- **Synthetic Data Recorder**: GUI 녹화 도구 (기본 `BasicWriter`)
- **Replicator YAML**: 설정 파일 기반 SDG 파이프라인
- **Getting Started Scripts**: `standalone_examples/api/isaacsim.replicator.examples/sdg_getting_started_0{1..4}.py`

## 2. 핵심 개념 — Isaac Sim식 Replicator 사용법
Replicator 단독 워크플로우와 달리, Isaac Sim에서는
**`step()`은 캡처만 트리거하고 랜덤화는 커스텀 이벤트로 분리**하는 패턴을 쓴다.

```python
import omni.replicator.core as rep

rep.orchestrator.set_capture_on_play(False)     # 매 프레임 자동 캡처 끄기
# 또는 carb.settings.get_settings().set("/omni/replicator/captureOnPlay", False)

rep.orchestrator.step(rt_subframes=-1, pause_timeline=True, delta_time=None)
```
- `rt_subframes`: 같은 프레임을 여러 번 렌더 → 머티리얼 로딩 지연/고스팅 아티팩트 완화.
  전역 설정은 `/omni/replicator/RTSubframes`. **머티리얼 랜덤화 시 최소 2 필요.**
- `pause_timeline`: 스텝 후 타임라인 일시정지
- `delta_time`: 타임라인 진행 시간. `0.0`이면 같은 시뮬 상태를 여러 번 캡처 가능.
- SDG는 **DLSS Quality 모드 권장**: `carb.settings.get_settings().set("/rtx/post/dlss/execMode", 2)`

### 커스텀 이벤트 랜덤화
```python
with rep.trigger.on_custom_event(event_name="randomize_dome_light_color"):
    rep.create.light(light_type="Dome", color=rep.distribution.uniform((0,0,0),(1,1,1)))
rep.utils.send_og_event(event_name="randomize_dome_light_color")   # 수동 트리거
```

### 쓰기 완료 대기 (데이터 유실 방지)
```python
while not BackendDispatch.is_done_writing():
    await omni.kit.app.get_app().next_update_async()
```

## 3. Writer / Annotator
```python
writer = rep.writers.get("BasicWriter")
writer.initialize(output_dir=..., rgb=True, bounding_box_2d_tight=True, semantic_segmentation=True)
writer.attach([render_product])
```
- 커스텀 writer:
```python
from omni.replicator.core import AnnotatorRegistry, BackendDispatch, Writer, WriterRegistry
class MyCustomWriter(Writer):
    def __init__(self, output_dir, rgb=True, normals=False):
        self.backend = BackendDispatch({"paths": {"out_dir": output_dir}})
        self.annotators = []                       # ★ 초기화 때 반드시 리셋 (5.1 버그픽스 사항)
        if rgb: self.annotators.append(AnnotatorRegistry.get_annotator("rgb"))
    def write(self, data: dict): ...
    def on_final_frame(self): ...
WriterRegistry.register(MyCustomWriter)
```
  - 렌더 프로덕트가 여러 개면 어노테이터 키가 `"rgb-<render_product_name>"` 형태 → `split("-")`로 분기.
- `isaacsim.replicator.writers.DataVisualizationWriter`: bbox를 rgb/normals 위에 그려서 검증
- `CosmosWriter`: NVIDIA Cosmos용 RGB/seg/depth/edge 동기 캡처 (이미지+비디오)
  ※ standalone에서 비디오가 안 만들어지면 writer detach 전에 app update를 몇 번 돌릴 것.
- `PoseWriter`: 포즈 추정 데이터셋용

## 4. Synthetic Data Recorder (GUI)
- Writer 프레임: Render Products 목록(카메라 경로 + 해상도, 같은 카메라 중복 가능),
  Parameters(BasicWriter 체크박스 / 커스텀 writer는 JSON 파라미터 파일),
  Output(작업 디렉터리 + S3 지원), Config(JSON으로 상태 저장/로드)
- Control 프레임: Start/Stop/Pause/Resume, Number of Frames(0=무한), **RTSubframes**,
  Control Timeline(타임라인 동기), Verbose
- 내부 루프: `await rep.orchestrator.step_async(rt_subframes=..., delta_time=None, pause_timeline=False)`
- 랜덤 카메라를 Script Editor로 먼저 만들어 두고 render product로 붙이는 조합 가능:
```python
camera = rep.create.camera()
with rep.trigger.on_frame():
    with camera:
        rep.modify.pose(position=rep.distribution.uniform((-5,5,1),(-1,15,5)),
                        look_at="/Root/Warehouse/SM_CardBoxA_3")
```

## 5. 주요 튜토리얼 / 예제 매핑
| 주제 | 문서 | standalone 예제 |
|---|---|---|
| 기본 캡처 | Getting Started Scripts | `sdg_getting_started_01~04.py` |
| 다중 카메라 어노테이터 | Useful Snippets | `multi_camera.py` |
| 특정 시점 데이터 접근 | 〃 | `simulation_get_data.py` |
| 커스텀 이벤트 랜덤화+쓰기 | 〃 | `custom_event_and_write.py` |
| 모션 블러 | 〃 | `motion_blur.py` |
| 이벤트/구독 커스텀 FPS | 〃 | `subscribers_and_events.py`, `custom_fps_writer_annotator.py` |
| Cosmos | Cosmos SDG | `cosmos_writer_simple.py` |
| 객체 기반 SDG (대형) | Object Based SDG | 콜라이더/리지드바디 유틸, 바운스 영역, 카메라 충돌구, 모션블러 캡처 전 과정 |
| 씬 기반 SDG | Scene Based SDG | 지게차/팔레트/박스 낙하 + 도메인 랜덤화 |
| 포즈 추정 | Pose Estimation SDG | CenterPose/DOPE 학습 데이터 |
| 랜덤화 스니펫 모음 | Randomization Snippets | 조명/텍스처/순차 랜덤화/물리 기반 볼륨 채우기/SimReady |
| 파지 SDG | Grasping SDG | 그리퍼-객체 파지 데이터 |
| 모빌리티 | MobilityGen | 이동로봇 데이터 |
| 사람/행동 SDG | Replicator Agent(IRA) | `isaacsim.replicator.agent` |
| 객체 SDG | Replicator Object(IRO) | YAML description 파일 기반 |
| 사건 SDG | Replicator Incident(IRI) | 물리 공간 이벤트 생성 |
| VLM 캡셔닝 | Replicator Caption(IRC) | |
| 씬 생성 | SceneBlox, Infinigen | |

## 6. 도메인 랜덤화 API (`isaacsim.replicator.domain_randomization`)
- `scripts/trigger`, `scripts/gate`, `scripts/physics_view`, `scripts/utils`
- 물리 속성(질량/마찰/반발) 텐서 기반 랜덤화는 physics_view 계열 사용.

## 7. Replicator 트러블슈팅 (★)
- **비동기 렌더링으로 프레임 스킵** → `--/exts/isaacsim.core.throttling/enable_async=false`
- 깊이 이미지 노이즈 → Render Settings > Ray Tracing > Anti-Aliasing = None
- 머티리얼 지연 로딩 → `rt_subframes >= 2`
- 고스팅(이동 물체/조명 급변) → `rt_subframes` 증가
- 캡처 이미지가 검게 나옴 → `./isaac-sim.sh --reset-user`
- **`Scatter3D` OmniGraph 노드는 World 사용 스테이지의 물리를 깨뜨림**
- `rep.new_layer()`는 시뮬레이션 시나리오에서 문제 유발 → 생략 가능
- Replicator 그래프 생성 **이후에는 타임라인(스테이지) FPS 변경 불가**(그래프 리셋됨)
  → 타임라인 파라미터를 먼저 설정할 것
- S3 쓰기(Windows)는 AWS config 파일 대신 환경변수로 자격증명 지정
- 확장 리네임: `omni.replicator.character`/`omni.replicator.agent` → `isaacsim.replicator.agent`

## 8. 관련: 매핑 / 점유 격자
- **Occupancy Map** (Tools > Robotics > Occupancy Map, `isaacsim.asset.gen.omap`):
  지정 높이의 2D 점유맵 생성. **모든 지오메트리에 Collision이 켜져 있어야** 감지됨.
  **Origin은 비어 있는 위치**여야 함. Cell Size = 픽셀당 미터.
  Use PhysX Collision Geometry=False면 원본 삼각 메시로 RTX Lidar 사용.
  Visualization 창에서 색상 지정, 회전(180°는 Block World 방향과 일치),
  Coordinate Type을 **"ROS Occupancy Map Parameters File"**로 두면 ROS 맵 파라미터를 바로 얻음.
- **Block World Generator**: 2D 점유맵 이미지 → 3D 블록 월드(충돌 메시 포함). 검은 픽셀=점유.

관련: [[isaacsim-sensors-camera]], [[isaacsim-versions-perf]]
