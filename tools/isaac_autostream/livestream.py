"""WebRTC 스트리밍 규칙 한 곳 — `sitecustomize.py` 가 이 파일만 읽는다.

`isaac_python` 으로 스크립트를 띄우면 창 대신 **브라우저로 화면을 본다.**
이 서버에는 디스플레이가 없어서 창을 만들려 하면 IWindowing 획득 실패로 즉시
죽는다. 창이 없는 것과 UI 가 없는 것은 다른 얘기다 — UI 는 오프스크린으로
그려져 WebRTC 로 실려 나간다.

🚨 **브라우저로는 못 본다.** `omni.kit.livestream.webrtc` 는 이름 그대로
   백엔드 전용이고(`title = "Livestream WebRTC Backend"`), HTML 클라이언트가
   번들에 **없다**(확장 전체에 `.html` 0개). 49100 은 웹페이지가 아니라
   **WebSocket 시그널링 포트**라 브라우저로 열면 아무것도 안 나온다.

   → NVIDIA 가 따로 배포하는 **Isaac Sim WebRTC Streaming Client**(데스크톱
     앱)를 쓴다. 앱의 **서버 주소 칸에 IP 만** 넣는다 — 포트도 `http://` 도
     붙이지 않는다.

    TCP 49100 (시그널링) / UDP 47998-48020 (미디어) 이 보안그룹에 열려 있어야 한다.

🚨 **이 파일이 없으면 스트리밍이 조용히 꺼진다.** `sitecustomize.py` 는 못
   찾으면 경고 한 줄만 찍고 그냥 뜬다 — 그래서 "WebRTC 에 아무것도 안 뜬다"
   가 된다. 실제로 한 번 사라진 적이 있다(`src/dongmin/graphic_file/scripts/`
   에 두었다가 그 디렉터리를 비우면서 같이 지워졌고, git 에도 없었다).
   → 그래서 지금은 **`sitecustomize.py` 바로 옆**에 둔다. 둘은 한 몸이다.

🚨 **`isaacsim.exp.full.streaming` 을 쓰지 않는다.** 그 experience 는
   `omni.services.livestream.nvcf` 를 물고 오는데, nvcf 의
   `quitOnSessionEnded=true` 때문에 **클라이언트가 안 붙으면 30초쯤 뒤 스스로
   종료한다.** 우리는 `isaacsim.exp.full` 에 `omni.kit.livestream.webrtc` 만
   직접 얹는다(`~/.bashrc` 의 `isaac_stream` 과 같은 구성).

🚨 **publicEndpointAddress 를 하드코딩하면 안 된다.** 이 인스턴스에는 EIP 가
   없어서 정지·시작할 때마다 퍼블릭 IP 가 바뀐다. 옛 IP 가 박혀 있으면
   시그널링(TCP 49100)은 붙는데 ICE 후보가 옛 주소라 **영상이 영영 안 뜬다**
   (클라이언트는 검은 화면에서 멈춘다). 그래서 실행 시점에 IMDS 에서 읽는다.
   다른 주소로 강제하려면  `ISAAC_PUB_IP=1.2.3.4 isaac_python ...`

끄는 법:  `ISAAC_STREAM=0 isaac_python <스크립트>`
"""

import os

PORT = 49100
MIN_HOST_PORT = 47998
MAX_HOST_PORT = 48020
EXT_WEBRTC = "omni.kit.livestream.webrtc"


# 🚨 **`isaacsim.exp.full` 을 쓰면 안 된다** (2026-08-06 실측). full 은
#    `isaacsim.ros2.bridge` 를 물고 오고(`isaacsim.exp.full.kit:144,166,168`),
#    그 확장이 자기 rclpy 를 로드하는 순간 **세그폴트가 난다**:
#        [12.1s] Using backup internal ROS2 humble distro
#        [12.2s] rclpy loaded
#        → crash (코어 덤프)
#    PYTHONPATH 로 rclpy 를 넣든 안 넣든 똑같이 죽는다 — 이중 로드 문제가
#    아니라 그 확장 자체가 이 환경에서 못 뜬다.
# 🔑 `isaacsim.exp.base` 는 **UI 는 있고 ros2 bridge 는 없다.** 우리는 rclpy 를
#    `isaac_ros`(PYTHONPATH)로 직접 잡으므로 브리지 확장이 필요 없다.
EXPERIENCE = os.environ.get("ISAAC_EXPERIENCE", "isaacsim.exp.base.kit")


def experience():
    """스트리밍용 experience 의 절대 경로.

    🔑 기본 experience(`isaacsim.exp.base.python.kit`)에는 **에디터 UI 가
       없다.** 그걸로 스트리밍하면 뷰포트도 스테이지 트리도 없는 빈 화면이
       나온다. 그래서 UI 가 있는 판으로 바꿔 준다.
    """
    import isaacsim
    return os.path.join(os.path.dirname(isaacsim.__file__), "apps", EXPERIENCE)


def app_config():
    """`SimulationApp(launch_config, experience=...)` 에 얹을 값.

    🚨 `headless` 는 **True 로 둔다.** 디스플레이가 없어 창을 만들려 하면
       죽는다. 대신 `hide_ui=False` 로 `--no-window` 가 자동으로 붙이는
       `--/app/window/hideUi=1` 을 되돌린다 — 이게 없으면 스트리밍은 되는데
       **UI 없이 검은 화면만** 나간다(simulation_app.py:460-468 참조).
    """
    return {"headless": True, "hide_ui": False}, experience()


def public_ip():
    """퍼블릭 IP 를 실행 시점에 읽는다. 못 읽으면 None."""
    if os.environ.get("ISAAC_PUB_IP"):
        return os.environ["ISAAC_PUB_IP"]
    import urllib.request
    base = "http://169.254.169.254/latest"
    try:                                        # IMDSv2 (토큰 필요)
        req = urllib.request.Request(
            f"{base}/api/token", method="PUT",
            headers={"X-aws-ec2-metadata-token-ttl-seconds": "60"})
        tok = urllib.request.urlopen(req, timeout=2).read().decode()
        req = urllib.request.Request(
            f"{base}/meta-data/public-ipv4",
            headers={"X-aws-ec2-metadata-token": tok})
        return urllib.request.urlopen(req, timeout=2).read().decode().strip()
    except Exception:
        pass
    try:                                        # IMDSv1
        return urllib.request.urlopen(
            f"{base}/meta-data/public-ipv4", timeout=2).read().decode().strip()
    except Exception:
        return None


def start():
    """앱이 뜬 **뒤에** 부른다. 설정 → 확장 순서라야 포트가 맞는다.

    🚨 순서를 뒤집으면(확장 먼저) 우리가 지정한 포트가 아니라 **기본 포트로
       열린다.** 그러면 보안그룹에 뚫어 둔 포트와 어긋나 접속이 안 된다.
    """
    import carb.settings
    s = carb.settings.get_settings()

    ip = public_ip()
    if ip:
        s.set("/app/livestream/publicEndpointAddress", ip)
    s.set("/app/livestream/port", PORT)
    # UDP 미디어 포트를 못박는다. 이 범위 설정은 원래 nvcf 확장에만 들어 있어
    # nvcf 를 안 쓰는 지금 구성에서는 지정하지 않으면 어떤 포트를 쓸지 정해지지
    # 않는다 — 보안그룹과 맞추려면 반드시 고정해야 한다.
    s.set("/app/livestream/fixedHostPort", 0)
    s.set("/app/livestream/minHostPort", MIN_HOST_PORT)
    s.set("/app/livestream/maxHostPort", MAX_HOST_PORT)
    s.set("/app/livestream/allowResize", True)
    s.set("/app/window/drawMouse", False)

    import omni.kit.app
    mgr = omni.kit.app.get_app().get_extension_manager()
    ok = mgr.set_extension_enabled_immediate(EXT_WEBRTC, True)

    print("=" * 78)
    if ok is False:
        print(f"  [자동스트리밍] ❌ {EXT_WEBRTC} 를 못 켰다 — 화면이 안 뜬다")
    elif ip:
        print(f"  [자동스트리밍] WebRTC 엔드포인트: {ip}")
        print(f"                 **Isaac Sim WebRTC Streaming Client** 앱의 "
              f"주소 칸에 이 IP 만 넣는다")
        print(f"                 (브라우저로는 안 된다 — {PORT} 은 웹페이지가 "
              f"아니라 WebSocket 시그널링이다)")
        print(f"                 TCP {PORT} / UDP {MIN_HOST_PORT}-{MAX_HOST_PORT} "
              f"가 보안그룹에 열려 있어야 한다")
    else:
        print("  [자동스트리밍] ⚠ 퍼블릭 IP 를 못 읽었다 — 시그널링은 붙어도 "
              "ICE 후보가 틀려 영상이 안 뜰 수 있다")
        print("                 ISAAC_PUB_IP=<주소> isaac_python ... 로 지정할 것")
    print("=" * 78)
