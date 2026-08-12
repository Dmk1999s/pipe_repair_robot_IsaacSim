#!/usr/bin/env bash
# cobot3_ws 셸 환경 — `~/.bashrc` 에서 source 한다 (setup/install.sh env 가 그 줄을 넣는다).
#
# 🚨 **파이썬이 두 개다.** Isaac Sim 5.1 은 3.11 전용이고 ROS 2 Humble 은 시스템
#    3.10 으로 빌드돼 있다. 확장 모듈 ABI 가 달라 서로의 라이브러리를 못 읽는다.
#    그래서 자동으로 소싱하지 않고, 터미널마다 별칭으로 고른다.
#
#        ROS 노드 터미널    ros_set      (python 3.10)
#        Isaac Sim 터미널   isaac_ros    (python 3.11)  ← ros_set 을 쓰면 안 된다
#
#    지금 터미널이 어느 쪽인지는 `pyver` 로 확인한다.

# 이 파일 위치에서 워크스페이스를 역산한다 — 클론 위치가 달라도 따라간다.
export COBOT3_WS="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")/.." && pwd)"
export ISAACSIM_VENV="${ISAACSIM_VENV:-$HOME/isaacsim_venv}"
export ISAACSIM_ROOT="$ISAACSIM_VENV/lib/python3.11/site-packages/isaacsim"

# ------------------------------------------------------------
#  ROS 2 통신 설정
# ------------------------------------------------------------
export ROS_DISTRO=humble
export ROS_DOMAIN_ID=143            # 그룹 번호. 양쪽 PC 가 같아야 토픽이 보인다
export RMW_IMPLEMENTATION=rmw_fastrtps_cpp
# EC2 는 멀티캐스트가 막혀 있어 자동 발견이 안 된다. 통신할 PC 의 IP 를
# 이 파일 <initialPeersList> 에 직접 적는다. (install.sh env 가 초안을 만든다)
export FASTRTPS_DEFAULT_PROFILES_FILE=$HOME/.ros/fastdds_whitelist.xml

# NVIDIA Omniverse EULA 동의 — 없으면 Isaac Sim 이 대화형으로 물어보다 헤드리스에서 멈춘다.
# https://docs.omniverse.nvidia.com/platform/latest/common/NVIDIA_Omniverse_License_Agreement.html
export OMNI_KIT_ACCEPT_EULA=YES

# ------------------------------------------------------------
#  순수 ROS 소싱  (python 3.10)
# ------------------------------------------------------------
alias ros_set="source /opt/ros/humble/setup.bash && [ -f \$COBOT3_WS/install/setup.bash ] && source \$COBOT3_WS/install/setup.bash; echo 'ROS 2 humble sourced (python 3.10)'"

# ------------------------------------------------------------
#  아이작심용 ROS 소싱  (python 3.11 / ROS 를 소싱하지 말 것)
# ------------------------------------------------------------
# Isaac Sim 5.1 은 python 3.11 용 humble rclpy 를 번들로 갖고 있다. 아래 두 경로만
# 잡으면 rclpy / sensor_msgs / std_msgs / geometry_msgs 가 전부 import 된다 —
# IsaacSim-ros_workspaces 도커 빌드는 필요 없다. (cv_bridge 는 없지만 Isaac 쪽은 안 쓴다)
#
# 🚨 LD_LIBRARY_PATH 는 **앞에 붙인다.** 뒤에 붙이면 셸에 이미 들어 있는
#    /opt/ros/humble/lib 이 먼저 잡혀, 3.11 rclpy 가 3.10 용
#    librcl_logging_spdlog.so 를 물고 `undefined symbol: ...spdlog...` 로 죽는다.
#    그러면 시연이 SystemExit 하고 Kit 이 세그폴트로 끝나 원인이 안 보인다.
alias isaac_ros="export LD_LIBRARY_PATH=\$ISAACSIM_ROOT/exts/isaacsim.ros2.bridge/humble/lib:\$LD_LIBRARY_PATH; export PYTHONPATH=\$ISAACSIM_ROOT/exts/isaacsim.ros2.bridge/humble/rclpy:\$PYTHONPATH; echo 'Isaac ROS2 bridge + rclpy 경로 설정 완료 (python 3.11)'"

# 아이작심 실행 — headless 서버이므로 --no-window 가 필수다.
#   빼면 X 디스플레이가 없어 IWindowing 획득 실패로 즉시 죽는다.
#   오디오 장치가 없어 carb.audio 가 죽으므로 audio/enabled=false 도 필수다.
alias isaac="\$ISAACSIM_VENV/bin/isaacsim isaacsim.exp.full --no-window --/app/audio/enabled=false"

# 지금 터미널이 어느 쪽인지 확인
alias pyver="python3 \$COBOT3_WS/src/son/pyver.py"

# ------------------------------------------------------------
#  WebRTC 스트리밍
# ------------------------------------------------------------
# TCP 49100 시그널링 / UDP 47998-48020 미디어 — 보안그룹에서 열어야 한다.
#   isaacsim.exp.full.streaming 은 쓰지 말 것 — nvcf 의 quitOnSessionEnded=true
#   때문에 클라이언트가 안 붙으면 31초쯤 뒤 스스로 종료한다.
# ⚠ publicEndpointAddress 를 하드코딩하면 안 된다. EIP 가 없으면 정지·시작마다
#   퍼블릭 IP 가 바뀌고, 옛 IP 가 박혀 있으면 시그널링은 붙는데 ICE 후보가 옛
#   주소라 **영상이 영영 안 뜬다**(검은 화면). 그래서 실행 시점에 IMDS 에서 읽는다.
#   EC2 가 아니거나 다른 주소로 강제하려면  ISAAC_PUB_IP=1.2.3.4 isaac_stream
isaac_pubip() {
    if [ -n "$ISAAC_PUB_IP" ]; then echo "$ISAAC_PUB_IP"; return 0; fi
    local tok
    tok=$(curl -s -X PUT --max-time 2 "http://169.254.169.254/latest/api/token" \
              -H "X-aws-ec2-metadata-token-ttl-seconds: 60" 2>/dev/null)
    if [ -n "$tok" ]; then
        curl -s --max-time 2 -H "X-aws-ec2-metadata-token: $tok" \
             http://169.254.169.254/latest/meta-data/public-ipv4
    else
        curl -s --max-time 2 http://169.254.169.254/latest/meta-data/public-ipv4
    fi
}

isaac_stream() {
    local ip; ip=$(isaac_pubip)
    if [ -z "$ip" ]; then
        echo "퍼블릭 IP 를 못 읽었다.  ISAAC_PUB_IP=<주소> isaac_stream  으로 지정할 것" >&2
        return 1
    fi
    echo "WebRTC 엔드포인트: $ip   (클라이언트 주소창에 이 IP 만 넣는다)"
    "$ISAACSIM_VENV/bin/isaacsim" isaacsim.exp.full --no-window \
        --enable omni.kit.livestream.webrtc \
        --/app/audio/enabled=false \
        --/app/livestream/publicEndpointAddress="$ip" \
        --/app/livestream/port=49100 \
        --/app/livestream/fixedHostPort=0 \
        --/app/livestream/minHostPort=47998 \
        --/app/livestream/maxHostPort=48020 "$@"
}

# 아이작심용 Python 3.11
#
# PYTHONPATH 앞에 tools/isaac_autostream 을 끼워, 파이썬이 본문을 실행하기 전에
# 거기 있는 sitecustomize.py 를 읽게 한다. 그 파일이 SimulationApp 을 가로채
# WebRTC 스트리밍(GUI 포함)을 자동으로 켠다 — 스크립트에 --stream 을 안 붙여도 된다.
#
#   isaac_python foo.py                  스트리밍 켜짐 (기본)
#   ISAAC_STREAM=0 isaac_python foo.py   끔. 배치로 산출물만 뽑을 때
#
# 별칭이 아니라 함수인 이유: PYTHONPATH 가 비어 있을 때 별칭으로 이어붙이면
# 끝에 ':' 이 남아 빈 항목(=현재 디렉터리)이 sys.path 에 들어간다.
# isaac_ros 가 세운 rclpy 경로도 이 방식이라야 안 지워진다.
# 옛 별칭이 살아 있는 터미널에서는 별칭이 함수보다 먼저 잡히므로 먼저 지운다.
unalias isaac_python 2>/dev/null

isaac_python() {
    PYTHONPATH="$COBOT3_WS/tools/isaac_autostream${PYTHONPATH:+:$PYTHONPATH}" \
        "$ISAACSIM_VENV/bin/python" "$@"
}
