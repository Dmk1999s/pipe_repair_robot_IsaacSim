#!/usr/bin/env bash
#
# cobot3_ws 환경 설치 — 새 머신(Ubuntu 22.04 + NVIDIA GPU)에서 이 레포를 돌릴 수 있게 만든다.
#
#   ./setup/install.sh              # driver 를 뺀 전부 (system → isaac → pyros → env → build)
#   ./setup/install.sh check        # 지금 상태만 점검, 아무것도 안 고침
#   ./setup/install.sh isaac build  # 단계만 골라서
#   ./setup/install.sh driver       # ⚠ GPU 드라이버 교체 + 재부팅 필요 (EC2 g5 전용, 별도 실행)
#
# 단계는 전부 멱등이다 — 이미 돼 있으면 건너뛴다. 중간에 끊겨도 다시 돌리면 된다.
#
# 검증된 조합 (2026-08 EC2 g5.2xlarge 에서 실측):
#   Ubuntu 22.04.5 / ROS 2 Humble desktop / python 3.10.12(ROS) + 3.11(Isaac)
#   Isaac Sim 5.1.0.0 (pip) / NVIDIA GRID 580.65.06 / A10G
#
set -euo pipefail

WS="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ISAACSIM_VENV="${ISAACSIM_VENV:-$HOME/isaacsim_venv}"
ISAAC_VER="5.1.0.0"
GRID_DRIVER="NVIDIA-Linux-x86_64-580.65.06-grid-aws.run"

say()  { printf '\n\033[1;36m▶ %s\033[0m\n' "$*"; }
ok()   { printf '  \033[32m✓\033[0m %s\n' "$*"; }
warn() { printf '  \033[33m!\033[0m %s\n' "$*"; }
die()  { printf '\n\033[31m✗ %s\033[0m\n' "$*" >&2; exit 1; }

[ "$(id -u)" -ne 0 ] || die "root 로 돌리지 말 것. 일반 사용자로 실행하면 필요할 때만 sudo 를 부른다."

# ============================================================
#  system — apt 로 들어가는 것 전부
# ============================================================
step_system() {
    say "시스템 패키지 (apt)"
    sudo apt-get update -qq

    # 공통 빌드 도구
    sudo apt-get install -y -qq \
        build-essential cmake git curl wget gnupg lsb-release \
        python3-pip python3-dev software-properties-common

    # --- ROS 2 Humble ---------------------------------------------------
    # 키가 한 번 회전한 적이 있어, 공식 배포판인 ros2-apt-source .deb 로 등록한다
    # (예전 문서의 `apt-key add` 방식은 만료된 키를 넣는다).
    if [ ! -d /opt/ros/humble ]; then
        if [ ! -f /etc/apt/sources.list.d/ros2.sources ]; then
            local ver codename
            ver=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest \
                  | grep -F '"tag_name"' | awk -F'"' '{print $4}')
            codename=$(. /etc/os-release && echo "$VERSION_CODENAME")
            curl -fsSL -o /tmp/ros2-apt-source.deb \
                "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ver}/ros2-apt-source_${ver}.${codename}_all.deb"
            sudo apt-get install -y -qq /tmp/ros2-apt-source.deb
            sudo apt-get update -qq
        fi
        sudo apt-get install -y -qq ros-humble-desktop
    fi
    # desktop 에 딸려 오지만 명시해 둔다 — 코드가 직접 import 하는 것들이다.
    sudo apt-get install -y -qq \
        ros-humble-cv-bridge ros-humble-vision-opencv ros-humble-image-transport \
        ros-humble-message-filters ros-humble-rmw-fastrtps-cpp \
        python3-colcon-common-extensions python3-rosdep python3-opencv
    ok "ROS 2 Humble"

    # --- Isaac Sim 용 python 3.11 (deadsnakes) --------------------------
    # 22.04 의 기본 파이썬은 3.10 이다. Isaac Sim 5.1 은 3.11 전용이라 따로 받는다.
    if ! command -v python3.11 >/dev/null; then
        sudo add-apt-repository -y ppa:deadsnakes/ppa
        sudo apt-get update -qq
    fi
    sudo apt-get install -y -qq python3.11 python3.11-venv python3.11-dev
    ok "python3.11 ($(python3.11 --version 2>&1))"

    # --- Isaac Sim 렌더링에 필요한 라이브러리 ---------------------------
    # 창을 안 띄워도(--no-window) Vulkan 으로 렌더한다 — libvulkan1 과 ICD 가 있어야 한다.
    sudo apt-get install -y -qq \
        libvulkan1 vulkan-tools mesa-vulkan-drivers \
        libgl1 libglu1-mesa libxrandr2 libxinerama1 libxcursor1 libxi6 xvfb
    ok "Vulkan / GL 라이브러리"
}

# ============================================================
#  isaac — python 3.11 venv + Isaac Sim 5.1 (pip)
# ============================================================
step_isaac() {
    say "Isaac Sim $ISAAC_VER  →  $ISAACSIM_VENV"

    [ -d "$ISAACSIM_VENV" ] || python3.11 -m venv "$ISAACSIM_VENV"
    "$ISAACSIM_VENV/bin/python" -m pip install -q --upgrade pip setuptools

    if "$ISAACSIM_VENV/bin/pip" show isaacsim >/dev/null 2>&1; then
        ok "이미 설치됨 ($("$ISAACSIM_VENV/bin/pip" show isaacsim | awk '/^Version/{print $2}'))"
    else
        # ~15 GB 내려받는다. pypi.nvidia.com 에만 있는 휠이다.
        warn "약 15GB 를 내려받는다 — 회선에 따라 20~40분"
        "$ISAACSIM_VENV/bin/pip" install "isaacsim[all]==$ISAAC_VER" \
            --extra-index-url https://pypi.nvidia.com
        ok "Isaac Sim 설치 완료"
    fi

    # trimesh · matplotlib · opencv-headless · fastapi 는 isaacsim 의 의존성으로 같이 들어온다.
    # 별도 pip 는 필요 없다 (확인: pip list --not-required 에 pip 밖에 안 남는다).
}

# ============================================================
#  pyros — ROS 노드 쪽(python 3.10) 파이썬 패키지
# ============================================================
step_pyros() {
    say "ROS 쪽 python 3.10 패키지"

    # 🚨 numpy 2.x 를 쓰면 안 된다.
    #    ROS Humble 의 확장 모듈(cv_bridge)과 apt/pip 로 깔린 scipy 가 numpy 1.x
    #    헤더로 빌드돼 있어, numpy 2 를 올리면
    #      - `import trimesh` → ValueError: numpy.dtype size changed  (scipy 경유)
    #      - cv_bridge import → AttributeError: _ARRAY_API not found
    #    로 조용히 깨진다. 그래서 제약 파일로 못박는다.
    local cons=/tmp/cobot3-constraints.txt
    cat > "$cons" <<'EOF'
numpy<2
EOF

    python3 -m pip install -q --user -c "$cons" \
        "numpy==1.26.4" "scipy==1.11.4" \
        trimesh networkx shapely rtree pycollada \
        matplotlib pyyaml
    ok "형상·수치 (numpy 1.26.4 / scipy 1.11.4 / trimesh)"

    # web_panel (pipe_comm) 이 쓰는 웹 서버 — ROS 노드 쪽 3.10 전용이다.
    python3 -m pip install -q --user -c "$cons" fastapi uvicorn
    ok "web_panel (fastapi / uvicorn)"

    # YOLO 결함 검출 (pipe_inspect_demo). torch 를 끌고 와 2~3GB 를 더 받는다.
    if [ "${SKIP_YOLO:-0}" = "1" ]; then
        warn "SKIP_YOLO=1 — ultralytics 건너뜀 (결함 검출 노드는 못 돈다)"
    else
        warn "ultralytics + torch — 2~3GB 를 더 받는다 (SKIP_YOLO=1 로 건너뛸 수 있다)"
        python3 -m pip install -q --user -c "$cons" ultralytics
        ok "YOLO (ultralytics)"
    fi
}

# ============================================================
#  env — ~/.bashrc 연결 + Fast DDS 화이트리스트
# ============================================================
step_env() {
    say "셸 환경"

    local marker="# cobot3_ws 환경 (setup/install.sh 가 추가)"
    if grep -qF "$marker" "$HOME/.bashrc" 2>/dev/null; then
        ok "~/.bashrc 에 이미 연결돼 있다"
    else
        cp "$HOME/.bashrc" "$HOME/.bashrc.bak.$(date +%Y%m%d_%H%M%S)"
        {
            echo ""
            echo "$marker"
            echo "[ -f \"$WS/setup/env.sh\" ] && source \"$WS/setup/env.sh\""
        } >> "$HOME/.bashrc"
        ok "~/.bashrc 에 추가 (원본은 ~/.bashrc.bak.* 로 백업)"
    fi

    # Fast DDS 초기 피어 목록.
    # EC2 는 멀티캐스트가 막혀 있어 자동 발견이 안 된다 — 통신할 PC 의 IP 를 직접 적는다.
    # ⚠ interfaceWhiteList 를 participant 하위에 넣으면 안 된다. Fast DDS 2.6 에서는
    #   transport_descriptor 소속이라 XML 파싱이 통째로 실패하고 이 파일이 조용히 무시된다.
    mkdir -p "$HOME/.ros"
    if [ -f "$HOME/.ros/fastdds_whitelist.xml" ]; then
        ok "fastdds_whitelist.xml 이미 있음 (덮어쓰지 않는다)"
    else
        local myip; myip=$(hostname -I | awk '{print $1}')
        cat > "$HOME/.ros/fastdds_whitelist.xml" <<EOF
<?xml version="1.0" encoding="UTF-8" ?>
<!--
  Fast DDS 통신 대상 PC 목록 (initial peers)

  ▸ PC 를 추가하려면 <locator> 블록을 통째로 복사해서 IP 만 바꾼다.
  ▸ 양쪽 PC 가 같은 ROS_DOMAIN_ID(=143) 를 써야 한다.
  ▸ 상대 PC 의 방화벽/보안그룹에서 UDP 7400-7500 이 열려 있어야 한다.
  ▸ 수정 후에는 실행 중인 모든 ROS 노드를 재시작해야 반영된다.
  ▸ 파싱 실패는 \`ros2 run demo_nodes_cpp talker\` 로그의 [XMLPARSER Error] 로 확인한다.
-->
<dds xmlns="http://www.eprosima.com/XMLSchemas/fastRTPS_Profiles">
  <profiles>
    <participant profile_name="whitelist_participant" is_default_profile="true">
      <rtps>
        <builtin>
          <initialPeersList>
            <!-- 자기 자신 (같은 PC 안의 노드끼리) -->
            <locator><udpv4><address>127.0.0.1</address></udpv4></locator>
            <!-- 이 머신 -->
            <locator><udpv4><address>$myip</address></udpv4></locator>
            <!-- ▼ 통신할 PC 를 여기에 추가 ▼
            <locator><udpv4><address>192.168.0.OO</address></udpv4></locator>
            ▲ 추가 끝 ▲ -->
          </initialPeersList>
        </builtin>
      </rtps>
    </participant>
  </profiles>
</dds>
EOF
        ok "~/.ros/fastdds_whitelist.xml 생성 (127.0.0.1 + $myip)"
    fi
}

# ============================================================
#  build — colcon 워크스페이스
# ============================================================
step_build() {
    say "colcon 빌드"
    # 🚨 워크스페이스 루트에서 그냥 `colcon build` 하면 실패한다.
    #    color_detector / color_interfaces 가 src/son 과
    #    src/dongyeon/integration_test 에 같은 이름으로 두 벌 있어
    #    colcon 이 "Duplicate package names not supported" 로 멈춘다
    #    (두 벌은 내용이 동일하다). 그래서 base-paths 로 경로를 못박는다.
    #    빌드되는 패키지: pipe_comm, pipe_inspect_demo, color_interfaces, color_detector
    #
    #    ⚠ --symlink-install 이어도 ament_python 패키지의 .py 는 복사된다.
    #      pipe_comm 을 고치면 매번 다시 빌드해야 반영된다.
    ( set +u
      source /opt/ros/humble/setup.bash
      cd "$WS"
      colcon build --symlink-install \
          --base-paths src/dongmin src/dongyeon/pipe_inspect_demo src/son )
    ok "install/setup.bash 생성됨 — 새 터미널에서 ros_set"
}

# ============================================================
#  driver — NVIDIA GRID 드라이버 (EC2 g5 전용, 재부팅 필요)
# ============================================================
step_driver() {
    say "NVIDIA GRID 드라이버 교체"
    cat <<'EOF'
  왜 필요한가: AWS DLAMI 기본 드라이버(595 계열)는 연산용(datacenter)이라
  nvidia-drm.ko 가 없다. /dev/dri 에 NVIDIA 렌더 노드가 안 생기고,
  Isaac Sim 이 첫 프레임에서 librtx.scenedb.plugin.so 세그폴트로 **반드시** 죽는다.
  headless·RayTracedLighting·텍스처스트리밍off 등 설정으로는 우회되지 않는다.

  이 단계는 되돌리기 어렵다: 드라이버를 교체하고 재부팅해야 한다.
  부작용 — nvidia-fabricmanager / libnvidia-nscq / efa-nv-peermem / nvidia_fs /
  gdrdrv 는 기존 버전에 맞춰져 있어 더 이상 안 맞는다 (이 프로젝트는 쓰지 않는다).
EOF
    if [ -e /dev/dri/renderD128 ] && lsmod | grep -q '^nvidia_drm'; then
        ok "이미 nvidia_drm 로드 + /dev/dri/renderD128 있음 — 교체 불필요"
        return 0
    fi
    read -r -p $'\n  계속할까? (yes 입력) ' ans
    [ "$ans" = "yes" ] || { warn "건너뜀"; return 0; }

    # 버킷은 익명 접근이 된다 (IAM 자격증명 불필요).
    aws s3 cp --no-sign-request "s3://ec2-linux-nvidia-drivers/grid-19.0/$GRID_DRIVER" /tmp/
    sudo sh "/tmp/$GRID_DRIVER" --silent --dkms --no-questions --accept-license

    # 재부팅해도 유지되도록 못박는다.
    echo 'options nvidia-drm modeset=1' | sudo tee /etc/modprobe.d/nvidia-drm-modeset.conf >/dev/null
    printf 'nvidia\nnvidia-modeset\nnvidia-drm\nnvidia-uvm\n' | sudo tee /etc/modules-load.d/nvidia.conf >/dev/null
    # 렌더 노드 접근 권한 — 재로그인해야 반영된다.
    sudo usermod -aG render "$USER"

    warn "재부팅 필요:  sudo reboot   (그 뒤 /dev/dri/renderD128 이 생겼는지 확인)"
}

# ============================================================
#  check — 점검만 한다
# ============================================================
step_check() {
    say "점검"
    printf '  %-34s %s\n' "OS"        "$(lsb_release -ds 2>/dev/null || echo '?')"
    printf '  %-34s %s\n' "GPU"       "$(nvidia-smi --query-gpu=name,driver_version --format=csv,noheader 2>/dev/null || echo '없음')"
    printf '  %-34s %s\n' "/dev/dri/renderD128" "$([ -e /dev/dri/renderD128 ] && echo 있음 || echo '없음 ← driver 단계 필요')"
    printf '  %-34s %s\n' "ROS 2"     "$([ -d /opt/ros/humble ] && echo humble || echo '없음')"
    printf '  %-34s %s\n' "python3 (ROS)"   "$(python3 --version 2>&1)"
    printf '  %-34s %s\n' "python3.11 (Isaac)" "$(python3.11 --version 2>&1 || echo '없음')"
    printf '  %-34s %s\n' "Isaac Sim" "$("$ISAACSIM_VENV/bin/pip" show isaacsim 2>/dev/null | awk '/^Version/{print $2}' || echo '없음')"
    printf '  %-34s %s\n' "colcon install/" "$([ -f "$WS/install/setup.bash" ] && echo 있음 || echo '없음 ← build 단계 필요')"

    echo
    # stderr 를 버린다 — 깨진 확장 모듈이 import 중에 긴 트레이스백을 뱉어 결과가 묻힌다.
    python3 - 2>/dev/null <<'PY'
mods = ["numpy", "scipy", "trimesh", "cv2", "yaml", "matplotlib", "fastapi", "ultralytics"]
for m in mods:
    try:
        mod = __import__(m)
        print(f"  \033[32m✓\033[0m {m:<12} {getattr(mod, '__version__', '?')}")
    except Exception as e:
        print(f"  \033[31m✗\033[0m {m:<12} {type(e).__name__}: {e}")
PY

    # 가중치는 *.pt 라 .gitignore 에 걸려 레포에 안 들어간다 — 클론만으로는 없다.
    if [ ! -f "$WS/src/dongyeon/pipe_inspect_demo/resource/yolov8n_seg_best.pt" ]; then
        echo
        warn "YOLO 가중치 없음: src/dongyeon/pipe_inspect_demo/resource/yolov8n_seg_best.pt"
        warn "  *.pt 는 .gitignore 대상이라 레포에 안 들어간다. 따로 받아 넣거나 다시 학습해야"
        warn "  결함 검출 노드(pipe_vision)가 돈다. 학습 데이터 생성은"
        warn "  src/dongyeon/integration_test/training/generate_dataset.py 참고."
    fi
}

# ============================================================
#  실행
# ============================================================
STEPS=("$@")
[ ${#STEPS[@]} -gt 0 ] || STEPS=(system isaac pyros env build check)

for s in "${STEPS[@]}"; do
    case "$s" in
        system|isaac|pyros|env|build|driver|check) "step_$s" ;;
        *) die "모르는 단계: $s   (system isaac pyros env build driver check)" ;;
    esac
done

say "끝. 새 터미널을 열거나  source ~/.bashrc  후:"
cat <<'EOF'
    ros_set        ROS 2 노드 터미널 (python 3.10)
    isaac_ros      Isaac Sim 터미널  (python 3.11) — 여기서 ros_set 을 쓰면 안 된다
    pyver          지금 터미널이 어느 쪽인지 확인
EOF
