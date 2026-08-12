# EC2 개발 환경 세팅 기록 (2026-08-04)

대상: `i-0a4e9b337cb322d22` (**g5.2xlarge**, ap-northeast-2)

> ⚠ **퍼블릭 IP 를 여기 적지 말 것.** 이 인스턴스에는 EIP 가 없어 정지·시작할
> 때마다 주소가 바뀐다(예전에 적혀 있던 `3.39.245.181` 은 이미 죽은 주소다).
> 지금 주소는 서버 안에서 `isaac_pubip` 로 확인한다.

**결론: Isaac Sim 포함 전부 동작한다.** 정찰기·수리기 조립, 카메라 깊이 진단,
최종 자산 생성, 3.11↔3.10 DDS 통신까지 실제로 돌려서 확인했다.

---

## 서버 제원

| | |
|---|---|
| OS | Ubuntu 22.04.5 LTS (jammy), 커널 6.8.0-1061-aws |
| CPU | AMD EPYC 7R32 — 4코어 / 8스레드 |
| RAM | 31 GB |
| GPU | **NVIDIA A10G 23 GB** |
| 드라이버 | **580.65.06** (AWS GRID) ← 595.71.05 에서 교체함. 아래 참조 |
| 디스크 | 97 GB (세팅 후 여유 약 25 GB) |
| 디스플레이 | **없음 (headless)** |

---

## ⚠ 드라이버를 교체했다 — 재부팅 시 확인할 것

원래 깔려 있던 **595.71.05 는 연산용(datacenter) 드라이버**라
`nvidia-drm.ko` 가 없었다. 그래서 `/dev/dri` 에 NVIDIA 렌더 노드가 없었고,
**Isaac Sim 이 첫 프레임에서 반드시 죽었다**:

```
[8.532s] app ready
segfault in librtx.scenedb.plugin.so   (carb.tasking 스레드)
```

headless·RayTracedLighting·텍스처스트리밍off·멀티GPUoff·base experience —
다섯 조합 전부 동일하게 segfault(139). 설정으로는 우회되지 않았다.

**해결: AWS GRID 드라이버 580.65.06 으로 교체.**

```bash
aws s3 cp --no-sign-request \
  s3://ec2-linux-nvidia-drivers/grid-19.0/NVIDIA-Linux-x86_64-580.65.06-grid-aws.run .
sudo ./NVIDIA-Linux-x86_64-580.65.06-grid-aws.run --silent --dkms --no-questions --accept-license
```

> 버킷은 익명 접근이 된다(`--no-sign-request`). IAM 자격증명 불필요.
> 580.65.06 을 고른 이유는 GRID 변형(nvidia-drm 포함)이면서 Isaac Sim 5.1 이
> 공식 지원하는 버전대라 "드라이버가 너무 최신" 가능성까지 같이 없애기 때문이다.

교체 후:

```
/dev/dri/card1, /dev/dri/renderD128   ← 생겼다
nvidia_drm 모듈 로드됨
```

영구 설정도 넣어 뒀다:

```
/etc/modprobe.d/nvidia-drm-modeset.conf   options nvidia-drm modeset=1
/etc/modules-load.d/nvidia.conf           nvidia, nvidia-modeset, nvidia-drm, nvidia-uvm
```

**`ubuntu` 를 `render` 그룹에 넣었다.** 아직 로그인 세션에는 반영이 안 됐을 수
있으니, `renderD128` 권한 오류가 나면 **재로그인**하거나 `sg render -c "..."`
로 감싸서 실행할 것.

교체 전 상태는 `~/driver_rollback_info.txt` 에 있다.

> 부작용: `nvidia-fabricmanager` `libnvidia-nscq` `efa-nv-peermem` `nvidia_fs`
> `gdrdrv` 는 595 에 맞춰져 있어 더 이상 안 맞는다. 이 프로젝트는 쓰지 않는다
> (fabricmanager 는 NVSwitch 용이고 g5 는 단일 GPU라 원래 inactive/disabled 였다).
> GPUDirect Storage 나 EFA 를 쓸 일이 생기면 그때 다시 맞춰야 한다.

---

## 설치된 것

| 구성요소 | 버전 | 위치 |
|---|---|---|
| ROS 2 Humble desktop | 0.10.0 (283패키지) | `/opt/ros/humble` |
| Python (ROS 쪽) | 3.10.12 | `/usr/bin/python3` |
| Python (Isaac 쪽) | **3.11.15** (deadsnakes) | `/usr/bin/python3.11` |
| Isaac Sim | **5.1.0.0** (pip) | `~/isaacsim_venv` |
| Vulkan | 1.4.329 / NVIDIA ICD | `/etc/vulkan/icd.d/nvidia_icd.json` |

### python 3.10 패키지 (ROS 노드 · 오프라인 검증용)

```
numpy 1.26.4   scipy 1.11.4   trimesh 5.0.0   cv2 4.5.4
yaml 6.0.3     matplotlib 3.5.1
networkx, shapely, rtree, pycollada   ← trimesh 가 fix_normals 에 쓴다
```

> apt 의 numpy 1.21 은 최신 trimesh 와 안 맞아(`'numpy._DTypeMeta' object is not
> subscriptable`) pip 로 1.26.4 를 덮어씌웠다. scipy 1.8 이 이 numpy 에 경고를
> 내므로 scipy 도 1.11.4 로 올렸다. **numpy 2.x 는 ROS Humble 과 깨지므로 쓰지 말 것.**

---

## 터미널을 두 가지로 나눠 쓴다

**파이썬이 두 개다.** 자동 소싱하지 않고 터미널마다 별칭으로 고른다.

```bash
ros_set      # ROS 2 노드용   python 3.10
isaac_ros    # Isaac Sim 용   python 3.11
```

**Isaac Sim 터미널에서 `ros_set` 을 쓰면 안 된다.** 3.10 라이브러리가 앞에
잡혀 심볼이 충돌한다. 지금 터미널이 어느 쪽인지는 `pyver` 로 확인한다.

| 별칭 | 하는 일 |
|---|---|
| `ros_set` | ROS 2 humble + 워크스페이스 오버레이 소싱 |
| `isaac_ros` | Isaac 내장 ROS2 브리지 `LD_LIBRARY_PATH` + rclpy `PYTHONPATH` |
| `isaac` | Isaac Sim (headless, 창 없음) |
| `isaac_stream` | Isaac Sim + WebRTC 스트리밍 |
| `isaac_python` | Isaac 쪽 python 3.11 — **WebRTC 스트리밍이 자동으로 켜진다** |
| `pyver` | 현재 터미널이 어느 쪽인지 출력 |

### 🎉 IsaacSim-ros_workspaces 도커 빌드는 필요 없다

HANDOFF.md 는 `camera/rig.py` 와 `robot/state_bridge.py` 가 rclpy 로 직접
발행하니 ROS 2 를 3.11 로 다시 빌드해야 한다고 적고 있다. **Isaac Sim 5.1 은
python 3.11 용 humble rclpy 를 이미 번들로 갖고 있다:**

```
~/isaacsim_venv/.../isaacsim/exts/isaacsim.ros2.bridge/humble/rclpy/
~/isaacsim_venv/.../isaacsim/exts/isaacsim.ros2.bridge/humble/lib/
```

이 두 경로만 `PYTHONPATH` / `LD_LIBRARY_PATH` 에 넣으면
`rclpy` `sensor_msgs` `std_msgs` `geometry_msgs` 가 전부 import 된다.
`isaac_ros` 별칭이 그 일을 한다. 도커도, git clone 도 필요 없다.

(`cv_bridge` 는 번들에 없지만 Isaac 쪽 스크립트가 쓰지 않는다.)

---

## 환경변수 (`~/.bashrc`)

```
ROS_DISTRO=humble
ROS_DOMAIN_ID=143
RMW_IMPLEMENTATION=rmw_fastrtps_cpp
FASTRTPS_DEFAULT_PROFILES_FILE=$HOME/.ros/fastdds_whitelist.xml
OMNI_KIT_ACCEPT_EULA=YES          # NVIDIA Omniverse EULA (2026-08-04 사용자 승인)
COBOT3_WS=$HOME/cobot3_ws
ISAACSIM_VENV=$HOME/isaacsim_venv
ISAACSIM_ROOT=$ISAACSIM_VENV/lib/python3.11/site-packages/isaacsim
```

원본은 `~/.bashrc.bak.20260804_082212` 에 있다.

---

## Fast DDS 화이트리스트

`~/.ros/fastdds_whitelist.xml` — **통신할 PC 의 IP 를 여기에 적는다.**

EC2 는 멀티캐스트가 막혀 있어 자동 발견이 안 된다. `<initialPeersList>` 에
상대 PC 의 IP 를 직접 넣어야 서로를 찾는다. 현재 등록: `127.0.0.1`,
`172.31.60.70` (이 서버 사설 IP).

> ⚠ `interfaceWhiteList` 를 participant 하위에 넣으면 안 된다. Fast DDS 2.6
> 에서는 transport_descriptor 소속이라 **XML 파싱이 통째로 실패하고 이 파일이
> 조용히 무시된다.** 처음에 그렇게 넣었다가 걸렸다. 파싱 실패는
> `ros2 run demo_nodes_cpp talker` 로그의 `[XMLPARSER Error]` 로 확인한다.

---

## 워크스페이스 빌드

```bash
ros_set
cd ~/cobot3_ws && colcon build --symlink-install
```

빌드되는 패키지 — `pipe_comm`, `pipe_inspect_demo`, `color_interfaces`,
`color_detector`.

> 2026-08-06 변경: `src/dongmin` 의 `M0609` / `pipe_inspect` 를 지우고
> **`pipe_comm`** 하나로 다시 만들었다. 통신 규약(토픽 이름·JSON 스키마)이
> `pipe_comm/contract.py` 한 곳에 모여 있고, Isaac 쪽(3.11)도 그 파일을
> 경로로 직접 읽는다 — 규약을 양쪽에 베껴 적어 갈라지는 것을 막기 위해서다.

> `pipe_msgs` 는 레포에 없고 **앞으로도 만들지 않는다.** 커스텀 msg 는
> rosidl 이 만든 3.10 용 `.so` 에 묶여 있어 Isaac(3.11) 쪽에서 못 쓴다.
> Isaac ↔ ROS 경계는 표준 메시지만 쓰고, 구조가 필요한 값은 `std_msgs/String`
> 에 JSON 으로 싣는다(`contract.py` 머리말). `condition/node.py` 와
> `driver/node.py` 의 JSON 폴백이 이미 그 방식이다.

---

## 검증 결과 — 전부 통과

### python 3.10 쪽 (Isaac Sim 불필요)

```
tools/build_parts.py                    STL 전부 생성
test_code/camera/test_probe_scene       8/8
test_code/condition/test_detector       통과
test_code/driver/test_control           19/19
test_code/driver/test_odometry          통과
test_code/driver/test_traction          14/14
test_code/localization/test_deadreckon  5/5
test_code/pipe/test_crack_inject        57/57
test_code/robot/preview_assembly        통과
test_code/robot/test_wheel_crown        8/8
test_code/spec/test_design_match        대조 19건
test_code/welder/test_audit             12/12
test_code/welder/test_weld              10/10
test_code/welder/test_ring_clearance    12/12
test_code/welder/test_part_paths        통과
```

### Isaac Sim 쪽 (드라이버 교체 후)

| | 결과 |
|---|---|
| ① `camera/depth_probe.py` | **40프레임 정상 수집** (1280x720). `invalid_mode: empty_is_zero`, 근접벽 45.73mm 유효. HANDOFF 가 경고한 "headless 는 카메라 프레임 0" 문제 없음 |
| ② `robot/articulate.py --headless` | 링크14/DOF13, 스프링 drive 6개 전부 상한 신장, 바퀴 6개 전부 회전 → `robot_2seg.usd` |
| ③ `welder/articulate.py --headless` | 토치 J1 ±90° 오차 0.00°, J2 8mm 오차 0.00mm → `welder_2seg.usd` |
| ④ `camera/rig.py --save` | front/rear 양쪽 rgb 3,686,400px + depth 921,600px 유효 → **`robot_2seg_cam.usd`** |
| ⑤ `robot/state_bridge.py` | 357회 발행. **3.11 발행 → 3.10 수신 확인** (아래) |

**핵심 검증 — 파이썬 버전이 달라도 DDS 로 통한다:**

```
발행측 python 3.11 (Isaac Sim)  →  수신측 python 3.10 (ROS 2 Humble)
  /imu_roll  /imu_yaw_rate  /joint_angle
  /suspension  /wheel_speed  /wheel_speeds      6개 전부 수신됨
```

> ①과 ⑥은 GUI 대기 상태로 남으므로 `timeout` 으로 끊거나 스트리밍
> 클라이언트에서 창을 닫아야 종료된다. 진단 출력은 그 전에 이미 나온다.

`camera/camera_probe_result.json` 의 `invalid_mode` 가
`condition/config/pipe_condition.yaml` 의 값과 이미 일치한다 — 수정 불필요.

---

## Isaac Sim 실행 시 반드시 필요한 플래그

| 증상 | 원인 | 대응 |
|---|---|---|
| 즉시 죽음, `IWindowing 획득 실패` | X 디스플레이 없음 | **`--no-window`** |
| `carb.audio` segfault | 오디오 장치 없음 | **`--/app/audio/enabled=false`** |
| 31초 뒤 스스로 종료(exit 0) | `isaacsim.exp.full.streaming` 이 물고 오는 nvcf 의 `quitOnSessionEnded=true` | **`isaacsim.exp.full` + `--enable omni.kit.livestream.webrtc`** 로 띄운다 |
| `ROS2 Bridge startup failed` | 브리지 라이브러리 경로 없음 | `isaac_ros` 를 먼저 실행 |
| 실행한 디렉터리에 `NvStreamer-*.etli` 가 쌓임 | NvStreamer 추적 로그가 기본 켜짐 | `livestream.py` 가 `/app/livestream/webrtcEtli=False` 로 끈다 |

`isaac` / `isaac_stream` 별칭에 이미 다 들어가 있다.

---

## WebRTC 스트리밍

```bash
isaac_ros
isaac_stream
```

기동 확인됨 — `Streaming server started`, **TCP 49100 리슨**, 크래시 없음.

### 보안그룹에서 열어야 하는 포트 (`launch-wizard-6`)

| 포트 | 프로토콜 | 용도 |
|---|---|---|
| **49100** | TCP | WebRTC 시그널링 (websocket) |
| **47998–48020** | UDP | 미디어 스트림 |

> 이 인스턴스에는 IAM 역할이 없어(`aws sts` → NoCredentials) 보안그룹을 서버
> 안에서 열 수 없다. **AWS 콘솔에서 직접 열어야 한다.**

### 클라이언트 — 브라우저가 아니라 전용 앱이다

**pip 배포판에는 브라우저용 웹 클라이언트 페이지가 들어 있지 않다.**
(`omni.kit.livestream.webrtc` 는 스트리밍 서버만 제공한다. 예전 Isaac Sim 이
8211 포트로 서빙하던 `omni.services.streamclient.webrtc` 는 번들에 없고,
`@nvidia/omniverse-webrtc-streaming-library` 도 공개 npm 에 없다.)

NVIDIA 가 배포하는 전용 클라이언트를 쓴다:

```
Windows : https://download.isaacsim.omniverse.nvidia.com/isaacsim-webrtc-streaming-client-1.1.4-windows-x64.exe
Linux   : https://download.isaacsim.omniverse.nvidia.com/isaacsim-webrtc-streaming-client-1.1.4-linux-x64.AppImage
```

실행 후 서버 주소에 **그때그때의 퍼블릭 IP** 를 넣는다. 서버 쪽에서

```bash
isaac_pubip          # 예: 3.38.216.197
```

로 확인하거나, `isaac_stream` / `curve_demo_v2.py --stream` 이 기동할 때 찍는
`WebRTC 엔드포인트: <IP>` 줄을 그대로 쓴다. 포트는 넣지 않는다 — IP 만 넣는다.

> 옛 주소를 넣으면 **아무 오류 없이 검은 화면에서 멈춘다.** 이 증상이 나오면
> 십중팔구 IP 가 바뀐 것이다.

### isaac_python 은 스트리밍이 기본으로 켜진다

```bash
PYTHONUNBUFFERED=1 isaac_python <스크립트>      # --stream 없이도 GUI 가 뜬다
ISAAC_STREAM=0 isaac_python <스크립트>          # 끈다. 배치로 산출물만 뽑을 때
```

`isaac_python` 은 `tools/isaac_autostream` 을 PYTHONPATH 앞에 끼우는 함수다.
파이썬은 본문을 실행하기 전에 거기 있는 `sitecustomize.py` 를 읽는데, 그 파일이
`isaacsim.SimulationApp` 을 가로채 experience 를 `isaacsim.exp.full.kit` 으로
바꾸고 `hide_ui=False` 를 넣은 뒤, 앱이 뜬 직후 스트리밍을 켠다. 그래서
**스크립트를 하나도 안 고쳐도 된다.**

> ⚠ **두 개를 동시에 띄우지 말 것.** WebRTC 시그널링 소켓은 SO_REUSEPORT 로
> 열려서 두 프로세스가 오류 없이 동시에 49100 을 리슨한다. 커널이 접속을 둘에
> 나눠 주므로 클라이언트가 엉뚱한 쪽에 붙어 "아무것도 안 뜨는" 증상이 된다.
> `sitecustomize.py` 가 이미 리슨 중이면 건너뛰지만, 확인은 이렇게 한다:
>
> ```bash
> pgrep -af "isaacsim_venv/bin/python"
> ```

### 씬만 내보내려면 — 스크립트 쪽 `--stream`

`isaac_stream` 별칭은 **빈 Isaac Sim 앱**을 띄운다. 우리가 만든 씬을 보려면
스크립트에 `--stream` 을 준다.

```bash
cd ~/cobot3_ws/src/dongmin
PYTHONUNBUFFERED=1 isaac_python graphic_file/scripts/curve_demo_v2.py --stream --steps 4000
```

내부적으로 `graphic_file/scripts/livestream.py` 가 `SimulationApp` 생성 **뒤**
carb 설정(IMDS 로 읽은 IP + 포트)을 넣고 `omni.kit.livestream.webrtc` 를 켠다.
순서가 바뀌면 기본 포트로 열려 보안그룹과 어긋난다.

주행이 끝나도 앱이 안 죽고 남으므로 클라이언트에서 계속 볼 수 있다.

---

## 실행 순서 (HANDOFF.md 기준)

```bash
isaac_ros                       # 먼저 (rclpy 경로 때문에)
cd ~/cobot3_ws/src/son

PYTHONUNBUFFERED=1 isaac_python camera/depth_probe.py            # ① 깊이 진단
PYTHONUNBUFFERED=1 isaac_python robot/articulate.py --headless   # ② 정찰기
PYTHONUNBUFFERED=1 isaac_python welder/articulate.py --headless  # ③ 수리기
PYTHONUNBUFFERED=1 isaac_python camera/rig.py --save             # ④ 최종 자산
PYTHONUNBUFFERED=1 isaac_python robot/state_bridge.py            # ⑤ 상태 발행
PYTHONUNBUFFERED=1 isaac_python pipe/curve_demo.py --cameras     # ⑥ 곡관 주행
```

ROS 노드는 **다른 터미널**에서:

```bash
ros_set
cd ~/cobot3_ws/src/son
python3 condition/node.py    --ros-args --params-file condition/config/pipe_condition.yaml
python3 localization/node.py --ros-args --params-file localization/config/localization.yaml
python3 driver/node.py       --ros-args --params-file driver/config/driver.yaml
```

> `.usd` 는 gitignore 대상이다. **pull 로 형상이나 상수가 바뀌면 ②③④를 다시
> 돌려야 한다.** 미리 구워 배포하면 코드를 고쳐도 그 파일은 안 바뀐다.

---

## 아직 안 해본 것

- ⑥ `pipe/curve_demo.py --cameras` — 곡관 주행 + 영상 발행
- `condition` / `localization` / `driver` 노드를 Isaac 과 동시에 띄운 전체 파이프라인

### 외부 PC 와의 DDS 통신은 **시연 구성에서 필요 없다** (2026-08-06 확정)

시연은 **RTX 5080 MSI PC 한 대**에서 Isaac 과 ROS 2 노드를 같이 돌린다.
같은 PC 안이라 화이트리스트의 `127.0.0.1` 로 그대로 통하고, 멀티캐스트도
NAT 도 문제가 안 된다. 이 EC2 서버는 개발·검증용이다.

그래도 PC 를 갈라야 할 일이 생기면 순서는 이렇다:

1. 양쪽 `ROS_DOMAIN_ID=143` — 다르면 `ros2 topic list` 에 **아무것도 안 보인다**
2. 양쪽 `RMW_IMPLEMENTATION=rmw_fastrtps_cpp` — 구현이 다르면 서로 못 찾는다
3. 같은 랜이면 멀티캐스트로 자동 발견된다 (화이트리스트 불필요)
4. EC2 ↔ 외부 PC 는 **화이트리스트로 못 푼다.** 상대가 사설망(192.168.x.x)
   NAT 뒤라 EC2 에서 그 주소로 가는 경로가 없다 — VPN(Tailscale 등)이나
   Fast DDS Discovery Server 가 필요하다
5. WAN 을 건널 때 `depth` 32FC1 원본(1280x720 10Hz ≈ 300 Mbps)은 못 쓴다.
   `depth/compressed`(16UC1 PNG ≈ 10 Mbps)만 쓸 것 — 규약이 압축을 기본으로
   둔 이유다

---

## 로그 위치

```
~/isaacsim_venv/lib/python3.11/site-packages/isaacsim/kit/logs/Kit/
~/.nvidia-omniverse/logs/
크래시 덤프: .../isaacsim/kit/data/Kit/Isaac-Sim Python/5.1/*.dmp
드라이버 설치: /var/log/nvidia-installer.log
```
