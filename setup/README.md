# 환경 세팅

새 머신에서 이 레포를 돌릴 수 있게 만드는 스크립트다.
전제: **Ubuntu 22.04 + NVIDIA GPU**. 검증은 EC2 `g5.2xlarge`(A10G, headless)에서 했다.

```bash
git clone <이 레포> ~/cobot3_ws
cd ~/cobot3_ws
./setup/install.sh            # system → isaac → pyros → env → build → check
```

단계는 전부 멱등이다. 중간에 끊기면 다시 돌리면 되고, 골라서도 돌아간다:

| 단계 | 하는 일 | 시간 |
|---|---|---|
| `system` | ROS 2 Humble desktop, python 3.11(deadsnakes), Vulkan/GL, colcon | 10분 |
| `isaac` | `~/isaacsim_venv` 에 Isaac Sim 5.1.0.0 (pip, **약 15GB**) | 20~40분 |
| `pyros` | ROS 쪽 python 3.10 패키지 (+ ultralytics/torch 2~3GB) | 5~10분 |
| `env` | `~/.bashrc` 에 `setup/env.sh` 연결, Fast DDS 화이트리스트 생성 | 즉시 |
| `build` | `colcon build` | 1분 |
| `check` | 점검만 한다. 아무것도 안 고침 | 즉시 |
| `driver` | **NVIDIA GRID 드라이버 교체.** 기본에 안 들어간다 — 아래 참조 | 10분 + 재부팅 |

`SKIP_YOLO=1 ./setup/install.sh pyros` 로 torch 다운로드를 건너뛸 수 있다
(대신 결함 검출 노드는 못 돈다).

설치가 끝나면 새 터미널에서:

```bash
ros_set        # ROS 2 노드 터미널 (python 3.10)
isaac_ros      # Isaac Sim 터미널  (python 3.11) — 여기서 ros_set 을 쓰면 안 된다
pyver          # 지금 터미널이 어느 쪽인지
```

---

## 클론만으로는 안 되는 것

### 1. GPU 드라이버 (EC2 DLAMI 라면 거의 확실히 필요)

AWS DLAMI 기본 드라이버(595 계열)는 연산용이라 `nvidia-drm.ko` 가 없다.
`/dev/dri` 에 NVIDIA 렌더 노드가 안 생기고 **Isaac Sim 이 첫 프레임에서
반드시 세그폴트**한다(`librtx.scenedb.plugin.so`). 설정으로는 우회가 안 된다.

```bash
./setup/install.sh driver     # GRID 580.65.06 으로 교체 → sudo reboot
```

`check` 가 `/dev/dri/renderD128 없음` 이라고 하면 이게 원인이다.

### 2. YOLO 가중치

`src/dongyeon/pipe_inspect_demo/resource/yolov8n_seg_best.pt` 는 `*.pt` 가
`.gitignore` 대상이라 레포에 안 들어간다. 이 파일이 없으면 결함 검출 노드
(`pipe_vision`)가 안 뜬다. **따로 백업해 두고 클론 후 넣을 것.**
다시 학습하려면 `src/dongyeon/integration_test/training/generate_dataset.py` 부터.

### 3. 보안그룹 (WebRTC 로 화면을 볼 때만)

| 포트 | 프로토콜 | 용도 |
|---|---|---|
| 49100 | TCP | WebRTC 시그널링 |
| 47998–48020 | UDP | 미디어 스트림 |

클라이언트는 브라우저가 아니라 NVIDIA 전용 앱이다
(`isaacsim-webrtc-streaming-client`, Windows `.exe` / Linux `.AppImage`).
접속 주소는 서버에서 `isaac_pubip` 로 확인한다 — EIP 가 없으면 인스턴스를
정지·시작할 때마다 바뀌고, 옛 주소를 넣으면 **오류 없이 검은 화면에서 멈춘다.**

---

## 함정 세 가지

**① 파이썬이 두 개다.** Isaac Sim 5.1 은 3.11 전용, ROS 2 Humble 은 시스템 3.10.
Isaac 터미널에서 `/opt/ros/humble/setup.bash` 를 소싱하면(=`ros_set`) 3.10
라이브러리가 앞에 잡혀 심볼이 충돌한다. 통신은 DDS 가 나르므로 버전이 달라도 된다.

**② numpy 2.x 를 올리면 안 된다.** `cv_bridge` 와 `scipy` 가 numpy 1.x 헤더로
빌드돼 있어, numpy 2 에서는 `import trimesh` 가 `ValueError: numpy.dtype size
changed` 로, `cv_bridge` 가 `_ARRAY_API not found` 로 조용히 깨진다.
`pyros` 단계가 `numpy<2` 제약으로 못박는다.

**③ 워크스페이스 루트에서 그냥 `colcon build` 하면 실패한다.**
`color_detector` / `color_interfaces` 가 `src/son` 과
`src/dongyeon/integration_test` 에 같은 이름으로 두 벌 있어
`Duplicate package names not supported` 로 멈춘다(내용은 동일). `build` 단계는
`--base-paths` 로 경로를 못박아 이걸 피한다. 직접 부를 때도 똑같이 해야 한다:

```bash
colcon build --symlink-install \
    --base-paths src/dongmin src/dongyeon/pipe_inspect_demo src/son
```

`--symlink-install` 이어도 ament_python 패키지의 `.py` 는 복사된다 —
`pipe_comm` 을 고치면 매번 다시 빌드해야 반영된다.
