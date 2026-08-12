# Isaac Sim 5.1.0 지식베이스 — 라우팅 인덱스

원본: `/home/rokey/docs.isaacsim.omniverse.nvidia.com/5.1.0/` (HTML 1,433개 / 542MB) · 정리일 2026-07-31

---

## ⚠ 읽는 규칙 (Claude용)

1. **이 파일(INDEX.md)만 먼저 읽는다.** 아래 라우팅 표에서 주제를 찾는다.
2. 표가 가리키는 **노트 파일 1개만** Read 한다. `§N`은 그 파일의 `## N.` 섹션 번호.
   → 대부분의 질문은 여기서 끝난다.
3. 노트로 부족할 때만 다음 단계로 내려간다:
   - Python 시그니처가 필요하면 → `API_INDEX.md`를 **grep** (통째로 Read 금지, 470K)
   - 원문 세부가 필요하면 → `FILEMAP.md`에서 경로를 찾아 `text/…` **그 파일 1개만** Read
   - 그래도 못 찾으면 → `text/` 를 grep, 최후에 `OUTLINE.md`(84K)
4. **`text/` 전체나 대용량 파일을 통째로 읽지 않는다.**

### 못 찾았을 때 (중요)

단계별로 내려가되, **2회 이상 헛돌면 멈추고 사용자에게 말한다.**

```
라우팅 표에 없음
  → FILEMAP.md 에서 제목으로 유사 문서 탐색
  → grep -rl "<핵심어>" text/   (파일명만 얻고 1개만 Read)
  → 그래도 없음  ➜  "이 KB에 없다"고 명시하고 멈춘다
```

**절대 하지 말 것**
- KB에서 못 찾았는데 일반 지식으로 메꿔서 답하기.
  Isaac Sim은 버전마다 API가 크게 바뀌었다(4.5 대량 리네이밍, 5.0 Core Experimental 도입).
  기억에 의존한 답은 **다른 버전 API일 확률이 높다.**
- 출처를 안 밝히고 단언하기. 답에는 근거 파일 경로를 남긴다.

**이 KB에 애초에 없는 것들** (찾지 말고 바로 그렇게 말할 것)
| 범주 | 실제 출처 |
|---|---|
| 두산 M0609 사양 (joint limit, 링크 치수, 토크) | 두산 URDF / 데이터시트 — `doosan-robot2/` |
| OnRobot RG2 사양 | 제조사 문서 — `onrobot_rg2/` |
| Isaac Lab 본체 사용법 (학습 스크립트, 태스크 정의) | Isaac Lab 별도 문서. 여기엔 "배포" 부분만 있음 |
| ROS 2 자체 문법·패키지 사용법 | ROS 2 공식 문서. 여기엔 Isaac Sim 브리지 부분만 |
| USD/PhysX 심층 레퍼런스 | Omniverse USD·PhysX 문서. 여기엔 Isaac Sim 관점 요약만 |
| Isaac Sim 5.1 **이외** 버전의 동작 | 없음. 버전 차이가 관건이면 그렇다고 말할 것 |
| Python API의 상세 설명·예제 | `API_INDEX.md`는 **시그니처만**. 설명은 `text/py/` 원문에 있고 그마저 얇을 수 있음 |

**노트와 원문이 어긋나면 `text/` 원문이 정답.** 노트는 요약이라 손실이 있다.
그런 경우 노트를 고쳐 두는 것까지가 마무리다.

---

## 주제 → 위치

### 이 프로젝트 (M0609 + RG2)
| 찾는 것 | 위치 |
|---|---|
| M0609 전용 요약 전부 | `NOTES/00-M0609-project-cheatsheet.md` |
| M0609이 RMPflow 미지원인 이유 / config 3종 유지 | `NOTES/00` §1 |
| config 점검 체크리스트 | `NOTES/00` §2 |
| pick&place 실패 원인별 대응표 | `NOTES/00` §4 |
| 카메라 좌표계·OpenCV 내부파라미터 적용 | `NOTES/00` §5, `NOTES/04` §1–2 |

### 모션 생성 · 매니퓰레이터
| 찾는 것 | 위치 |
|---|---|
| RMPflow 파라미터 전체 (`target_rmp`, `collision_rmp` 등) | `NOTES/02` §5 |
| RMPflow 새 로봇 튜닝 절차 | `NOTES/02` §5 끝 · 원문 `text/manipulators/concepts/rmpflow_tuning_guide.md` |
| Lula config 3종(URDF/robot_description/rmpflow_common) | `NOTES/02` §1 |
| active/fixed joint, c-space 정의 | `NOTES/02` §2 |
| collision sphere 생성·튜닝 | `NOTES/02` §3 |
| RMPflow 디버깅(collision sphere 시각화, ignore_state_updates) | `NOTES/02` §5 |
| Lula IK/FK (`LulaKinematicsSolver`) | `NOTES/02` §6 |
| RRT 경로 계획 / 궤적 생성 | `NOTES/02` §7–8 |
| cuRobo / cuMotion / XRDF | `NOTES/02` §1, §9 |
| body_cylinders·자기충돌 회피 | `NOTES/02` §5 · 원문 `text/manipulators/manipulators_configure_rmpflow_denso.md` |
| EE 프레임을 URDF에 추가하는 법 | `NOTES/02` §5 끝 |

### 로봇 셋업 · 그리퍼
| 찾는 것 | 위치 |
|---|---|
| URDF 임포트 옵션 (natural frequency, drive type 등) | `NOTES/03` §2 |
| USD→URDF 내보내기 | `NOTES/03` §3 |
| 팔+그리퍼 결합 / Robot Assembler | `NOTES/03` §4 |
| articulation solver 설정, effort limit | `NOTES/03` §5 |
| 게인 튜닝 절차 (position/velocity drive) | `NOTES/03` §6 |
| mimic joint, 폐루프 끊기(Exclude From Articulation) | `NOTES/03` §7 |
| `ParallelGripper` / `SingleManipulator` 사용법 | `NOTES/03` §8 |
| Surface Gripper(흡착) | `NOTES/03` §9 |
| Grasp Editor / isaac_grasp YAML | `NOTES/03` §10 |
| `PickPlaceController` events_dt, end_effector_offset | `NOTES/03` §11 |
| Robot Wizard | `NOTES/08` §3 |
| Asset Validator 규칙 전체 | `NOTES/08` §2 |
| Robot Schema (`IsaacRobotAPI`) | `NOTES/04` §6 |

### Core API · Python
| 찾는 것 | 위치 |
|---|---|
| World/Scene/Stage 개념, standalone vs extension | `NOTES/01` §1–2 |
| standalone 메인 루프 관용구 | `NOTES/01` §2, `NOTES/03` §12, `NOTES/00` §6 |
| Task 클래스(BaseTask) 오버라이드 지점 | `NOTES/01` §4 |
| Controller / `ArticulationAction` | `NOTES/01` §5–6 |
| prim view (`Articulation`, `RigidPrim`, 접촉력) | `NOTES/01` §7 |
| 물리/USD 스니펫(강체, 콜라이더, 머티리얼, 레이캐스트) | `NOTES/01` §10 |
| 확장 리네이밍 (`omni.isaac.*` → `isaacsim.*`) | `NOTES/06` §2 |
| 클래스·함수 시그니처 | `API_INDEX.md` (grep) |

### 센서 · 물리
| 찾는 것 | 위치 |
|---|---|
| 단위·쿼터니언 순서·좌표축 규약 | `NOTES/04` §1 ★ |
| Camera 클래스, OpenCV 왜곡 모델, extrinsic | `NOTES/04` §2 |
| Depth 센서 / RealSense D455 | `NOTES/04` §3 |
| RTX Lidar/Radar 개요 | `NOTES/04` §4 |
| 물리 기초 (rigid body, collider, CCD, joint, articulation) | `NOTES/04` §5 |
| contact/rest offset, combine mode | `NOTES/04` §5 |
| Contact Sensor (파지 판정) | `NOTES/09` §1 |
| Effort Sensor / 관절 힘·토크 읽기 | `NOTES/09` §2–3 |
| IMU | `NOTES/09` §4 |

### ROS 2 · OmniGraph
| 찾는 것 | 위치 |
|---|---|
| OmniGraph Python API (`og.Controller.edit`) | `NOTES/05` §1 |
| GUI 그래프 단축 메뉴 (컨트롤러/ROS2) | `NOTES/05` §1 |
| JointState 발행·구독 + Articulation Controller | `NOTES/05` §3 |
| Clock / `use_sim_time` | `NOTES/05` §4 |
| 카메라 RGB/depth/pointcloud/camera_info 발행 | `NOTES/05` §5 |
| TF / Odometry | `NOTES/05` §6 |
| 퍼블리시 주기 제어 (SimulationGate, frameSkipCount) | `NOTES/05` §7 |
| ROS 2 설치·Python 3.11·DDS | `NOTES/05` §2, `NOTES/06` §4 |
| ROS 2 트러블슈팅 (QoS, depth 흑백, 주기 이상) | `NOTES/05` §9 |

### 성능 · 버전 · 문제 해결
| 찾는 것 | 위치 |
|---|---|
| 5.1.0 변경점 | `NOTES/06` §1 |
| 성능 최적화 체크리스트 (물리/렌더/CPU/멀티GPU) | `NOTES/06` §6 ★ |
| 알려진 문제·함정 | `NOTES/06` §7 ★ |
| 에셋 구조(레이어/payload/variant) | `NOTES/06` §5 |
| 에셋 최적화 실전(메시 병합, instancing) | `NOTES/08` §4–5 |
| VS Code 디버깅 / Docker debugpy / carb 설정 | `NOTES/08` §1 |

### Replicator · SDG
| 찾는 것 | 위치 |
|---|---|
| `orchestrator.step` 패턴, capture on play, rt_subframes | `NOTES/07` §2 |
| Writer/Annotator, 커스텀 writer | `NOTES/07` §3 |
| Synthetic Data Recorder | `NOTES/07` §4 |
| 튜토리얼↔standalone 예제 매핑표 | `NOTES/07` §5 |
| Replicator 트러블슈팅 | `NOTES/07` §7 |
| 점유맵(Occupancy Map) / Block World | `NOTES/07` §8 |
| 대형 SDG 튜토리얼 원문(object/scene based, Infinigen 등) | `FILEMAP.md` → `text/replicator_tutorials/` |

### 기타
| 찾는 것 | 위치 |
|---|---|
| Cloner / 병렬 환경 | `NOTES/08` §6 |
| Instanceable 에셋 | `NOTES/08` §5 |
| Isaac Cortex | `NOTES/08` §7 |
| MJCF 임포터 | `NOTES/08` §8 |
| 확장 템플릿·커스텀 노드 | `NOTES/08` §9 |
| RL 정책 배포 + 디버깅 체크리스트 | `NOTES/09` §5 ★ |
| 이동로봇 컨트롤러(differential/holonomic/ackermann) | `NOTES/09` §6 |
| 에셋 경로 모음 (franka.usd, warehouse 등) | `NOTES/09` §7 |

---

## 파일별 비용

| 파일 | 크기 | 언제 |
|---|---|---|
| `INDEX.md` (이 파일) | 9K | **항상 먼저** |
| `NOTES/00~09*.md` | 8–16K each | 라우팅 표가 가리킬 때 1개만 |
| `FILEMAP.md` | 20K | 원문 파일 경로를 찾을 때 |
| `API_INDEX.md` | 470K | **grep 전용** (5,317개 시그니처 / 92개 모듈) |
| `OUTLINE.md` | 84K | 최후 수단 (문서별 소제목까지) |
| `text/**.md` | 1,384개 / 14M | 필요한 1개만 Read |

---

## grep 레시피

```bash
KB=/home/rokey/isaacsim_kb

# 1) 노트에서 먼저
grep -rn "collision sphere" $KB/NOTES/

# 2) API 시그니처
grep -n "PickPlaceController" $KB/API_INDEX.md
grep -A15 "^### ParallelGripper" $KB/API_INDEX.md

# 3) 원문 파일 찾기 (제목 기준)
grep -i "rmpflow" $KB/FILEMAP.md

# 4) 원문 본문 검색 (파일명만 얻고 그 파일만 열기)
grep -rl "joint_velocity_cap_rmp" $KB/text/ | head
```

---

## 커버리지 메모

노트는 **매니퓰레이터·모션생성·센서·ROS2·Core API**를 우선 정독해 작성했다.
Replicator 대형 SDG 튜토리얼, Replicator Agent/Object/Incident/Caption, 클라우드 배포,
cuOpt/창고물류, GUI 레퍼런스 세부는 **요점만** 정리했으므로 그 주제는 `FILEMAP.md`로 원문을 찾을 것.
`py/` API 1,121개는 정독 대신 시그니처 색인(`API_INDEX.md`) + 원문(`text/py/`) 보존 방식.
