"""[Isaac 3.11] 지그재그 훅 R100 점검·수리 시연 — 12륜 벨로우즈 용접로봇.

`src/son/repair_demo.py` 를 본떠 만들었으나 **로봇도 배관도 다르다.** 무엇이 왜
달라졌는지 아래에 다 적는다. 그대로 베끼면 안 되는 자리마다 🚨 를 달았다.

    배관  test_pipe_zigzag_hook_R100.usda  (워크스페이스 루트)
          직선4 + 90°굽힘3, 굽힘 R=100mm, 내반경 50mm, 벽 6mm, 중심선 1771.2mm
          평면은 XY(수평), 중심선 z=0. 기하는 전부 `course.py` 가 쥐고 있다.
    로봇  robot_from_bot_welder_art_v2.usda (워크스페이스 루트)
          12륜(전후 본체 × 3줄 × 2단) · 벨로우즈 4관절 · 용접링+토치
          DOF 35, 질량 2.04kg, 장축 = 로컬 **+X**(FrontBody 가 앞)

시퀀스
    DRIVE(주행하며 **카메라로 훑기**) → 구멍 검출·확정 → 목표 앞 정지
    → ALIGN(링 회전) → CREEP(축 미세정렬) → EXTEND(토치) → ARC(아크 2초)
    → SWAP(결함→비드+마개) → RETRACT → REPOSITION(140mm 후진)
    → VERIFY(카메라·Depth 로 확인) → RUNOUT(코스 끝까지)

## 🚨 이 로봇은 **출고 상태로 이 배관을 통과하지 못한다** — 가장 중요한 발견

`robot_from_bot_welder_art_v2.usda` 의 벨로우즈 D6 4개는 스윙 리밋이 ±20° 다.
그 값으로는 **첫 굽힘 입구 s=388mm 에서 멈춘다**(실측). 관절 4개가 전부 리밋에
붙은 채로 본체 사이 꺾임이 **25° 밖에 안 나오는데**, R100 굽힘은 본체 중심간
124mm 에 대해 약 71° 를 요구하기 때문이다.

리밋을 바꿔 가며 실측한 임계값:

    ±20°  ❌ s= 379mm 정지 (굽힘 1 입구)      ← usda 출고값
    ±22°  ❌ s= 388mm 정지
    ±23°  ❌ s= 394mm 정지
    ±24°  ❌ s= 394mm 정지
    ±25°  ✅ 완주 42.4초
    ±27°  ✅ 완주 41.0초
    ±30°  ✅ 완주 41.1초                       ← 기본값(임계 대비 20% 여유)
    ±40°  ✅ 완주 39.3초

→ 기본을 **±30°** 로 둔다. `--flex D` 로 바꿀 수 있고, `--flex 20` 을 주면
   출고 상태를 재현한다(막히는 것을 눈으로 확인할 때 쓸 것).
🚨 **usda 원본 파일은 건드리지 않는다.** 스테이지에 올린 뒤 속성만 덮어쓴다.
   실기 반영이 필요하면 벨로우즈 관절 설계를 바꿔야 한다는 뜻이다.

## repair_demo.py 와 결정적으로 다른 점 — 값을 옮겨 쓰기 전에 읽을 것

| 항목 | repair_demo (son 1세대) | 여기 |
|---|---|---|
| 로봇 장축 | 로컬 **−Z** (seg1 이 앞) | 로컬 **+X** (FrontBody 가 앞) |
| 배치 | `Ry(−90)` 로 눕힘 | 접선 방향 **Rz(yaw)** 만 |
| 질량 | 0.81 kg | **2.04 kg** (2.5배) |
| 다리 | 6개 × 예압 9N | **12개 × 예압 18N** |
| 휠 | r10mm, 폭 4mm (궤도 ±2.9°) | **r8mm, 폭 12mm (궤도 ±8.5°)** |
| 굽힘 | LR150 1개 (R/D 1.5) | **R100 3개** (R/D 1.0) |
| 코스 | 0.921 m | **1.771 m** |
| DOF 이름 | `_piston_`/`_wheel_` 로 구분 | 🚨 **겹친다** — `scene.py` 머리말 |
| 좌표 | x·y 를 손으로 편 3구간 식 | **`course.py` 의 (s, 시계각)** |

🚨 **물리 스텝 1/240 은 여기서도 필수다.** PHYSICS_HZ 로 바꿀 수 있으나 내리지 말 것.

🚨 **토치는 관벽에 닿지 않는다.** 토치 팁 끝 반경은 33(링) + 8(팁) + 0~5(신장)
   = 41~46mm 이고 관 내벽은 50mm 다. 즉 **최소 간극 4mm** 로, 설계 용접 간극
   2mm 에 못 미친다. repair_demo 가 겪은 "팁이 개구로 새어 나간다" 문제는
   원리적으로 안 생기지만, 간극은 로봇 설계값 그대로 두고 로그에 실측을 남긴다.

## 🚨 정지만으로는 정렬이 안 된다 — 스테이션 키핑이 필수다

휠 드라이브는 강성 0 · 감쇠 0.012 N·m·s/rad · maxForce 0.08 N·m 인 **순수 속도
드라이브**라 정지 토크가 거의 없다. 굽힘을 지나며 12~14° 접힌 벨로우즈가 펴지려는
복원력이 로봇을 계속 밀어서, 목표속도를 0 으로 둬도 **2~4mm 뒤로 이완한다**
(정렬 허용치 1.5mm 보다 크다). 실측 경과:

    정지만 함            축오차 −8.23mm  ❌ (첫 통합 실행)
    비례 제어만          16.8 deg/s 명령에 로봇이 **꿈쩍도 안 함** — 토크 5.3N
                         (감쇠 × 속도오차라 작은 명령엔 토크가 안 나온다)
    최소명령 25 deg/s 깔기  축오차 −0.29mm  ✅

그래서 `hold_station()` 이 데드밴드 밖에서 **최소 명령을 깔고**, CREEP 뿐 아니라
EXTEND·ARC 내내 계속 부른다. 아크 2초 동안 밀리면 그만큼 그대로 오차이기 때문이다.

## 카메라 — 이 로봇의 주 센서

전방 카메라 1대(어안 140°, 640x360, FrontBody 로컬 x=+33mm). 하는 일이 셋이다.

  ① **찾기**  주행하며 10Hz 로 훑어 벽면 구멍을 찾는다. 여기서 나온 (진행거리,
     시계각)만 주행·정렬에 쓴다. 정답 좌표는 **점수 매기기에만** 쓴다.
  ② **겨누기** ALIGN·CREEP 의 목표가 검출값이다.
  ③ **확인**  용접 뒤 140mm 후진해서 다시 본다.

🚨 **굽힘에서 "관 저 끝" 이 가짜 구멍으로 잡힌다 — repair_demo 의 필터로는 못 막는다.**
   그쪽의 "화면 중앙에 걸리는 라벨은 관 저 끝" 규칙은 직관 전제라, 굽은 관에서는
   터널 끝이 중앙을 크게 벗어나 그냥 통과한다. 실측: 첫 굽힘 입구에서 면적
   **44,085px**(화면의 19%, 25% 상한 아래) 짜리 덩어리가 확정돼 로봇이 굽힘
   한가운데로 용접하러 갔다.
   → **크기로 가른다.** 광선이 벽에 닿는 거리를 알면 화소 반지름에서 실제 지름이
     나온다: `지름 = 2·r_eq_px·거리/f_px`. 위 가짜는 ø169~175mm 로 계산돼
     걸러지고, 진짜 ø28 구멍은 ø28 근처로 나온다. **결함 위치를 전혀 안 쓰는**
     판별식이다.

🚨 **카메라가 토치보다 33mm 앞이라 용접 자리는 제자리에서 안 보인다.**
   세로 반화각 39.4° · 판정 창 36px 를 만족하려면 카메라가 결함에서 최소
   81.5mm 떨어져야 한다 → **140mm 후진**(그때 107mm, r_px ≈ 114px).

🚨 **검증에서 RGB 와 Depth 는 서로 다른 조건에서 실패한다 — 어느 한쪽을 주
   판정으로 고정하면 안 된다.** 실측 두 건이 정반대로 나왔다:

       --no-weld (불투명)    RGB   "구멍 없음"            ❌ 놓쳤다
                             Depth "파임 +3.69mm (447px)"  ✅ 잡았다
       --glass (수리 실패)   RGB   "구멍 있음 4,509px"     ✅ 잡았다
                             Depth "메워짐 −1.66mm"        ❌ 놓쳤다

   RGB 가 놓치는 이유 — 결함이 화면 아래 가장자리라 관 저 끝의 큰 암부와
   이어져 버려 중앙 원판 필터가 그 라벨을 통째로 제외한다.
   Depth 가 놓치는 이유 — **비드 조각이 그 자리 벽을 다시 채워** 깊이가 멀쩡한
   벽면으로 읽힌다(비드 STL 은 44×47mm 벽 조각이다).

   → **비대칭 규칙**을 쓴다. "구멍이 보인다" 는 결정적 증거지만 "안 보인다" 는
     아니다(가려졌을 수도 있다):
       ① 예상 자리에 구멍이 보이면  → 미수리 (확정)
       ② 아니면 Depth 판정을 따른다
       ③ Depth 도 없으면 비드 유무로 본다
     이 규칙이면 위 두 건이 **모두** 물리 실제와 일치한다.

   반대로 **찾을 때**는 RGB 가 맞다 — 관통 구멍의 깊이는 inf 라 Depth 로는
   위치를 못 잡는다.

## 🚨 --glass 는 검출 정확도를 6배 떨어뜨린다 — 용접까지는 못 본다

관이 반투명해지면 로봇 조명이 벽에서 반사돼 돌아오지 않아 대비가 죽는다.
같은 씬을 두 번 돌린 실측:

    불투명    검출 오차 축 −0.4mm  → 정렬 오차 0.79mm  ✅ 수리 성공
    --glass   검출 오차 축 −2.3mm  → 정렬 오차 2.55mm  ❌ 수리 실패 (허용 1.5mm)

검출 자체는 살아남지만(기울기 0.011 로 확정) **정확도가 허용치를 넘긴다.**
밖에서 들여다보며 용접까지 보려면 `--glass --no-vision` 으로 정답 좌표를
겨누게 할 것.

물리에는 영향이 없다 — 물리 재질은 `materialPurpose="physics"` 로 따로
바인딩되고 유리는 표시 재질만 덮는다. 굽힘 3곳의 주행 수치(s, 시각, 벨로우즈
각)가 불투명 실행과 **소수점까지 같게** 나오는 것으로 확인했다.

## 검증이 자기충족이 되지 않게 하는 장치

아크가 끝났다고 무조건 결함을 지우면 성공률이 항상 100% 다(설계 7.2 가 경고).
여기서는 **정렬 오차를 관벽 좌표 (진행거리, 시계각) 에서 재서** 허용치(1.5mm)
안일 때만 결함을 없앤다. 비드는 성공·실패와 무관하게 **토치가 실제로 있던
자리**에 생기므로, 빗나가면 비드가 엉뚱한 데 남고 결함은 그대로 뚫려 있다.

대조군 4종으로 확인했다 (정렬 판정 = 물리 실제, 검증 = 카메라가 본 것):

    조건          정렬 오차   물리 실제   카메라가 본 것              검증 판정
    기본            0.70mm    ✅ 수리    구멍 없음 / Depth 메워짐    ✅ 일치
    --no-creep     11.87mm    ❌ 실패    구멍 없음 / Depth 메워짐    🚨 불일치
    --no-weld     (아크 생략)  미수리    구멍 없음 / Depth 파임      ✅ 일치
    --glass         2.55mm    ❌ 실패    **구멍 있음** / Depth 메워짐 ✅ 일치

**정렬 판정은 4건 모두 물리 실제와 맞았다** — 자기충족 검증이 아니라는 뜻이다.

🚨 **`--no-creep` 의 검증 불일치는 검출기 잘못이 아니라 시각 모델의 한계다.**
   비드 STL 은 44×47mm **벽 조각**이라 어디에 놓이든 그 자리 벽을 메운 것처럼
   보인다. 11.87mm 어긋나도 ø28 구멍이 조각 안에 들어가 RGB·Depth 둘 다 가려진다.
   수리 여부 자체는 정렬 판정이 제대로 잡으므로 틀리지 않는다 — **검증층만**
   이 경우를 못 가린다. 실기에서는 비드가 토치 자리에만 쌓이므로 안 생긴다.
   (`--glass` 는 2.55mm 로 어긋남이 작은데도 잡혔다 — 그쪽은 대비가 죽어
    결함 프림이 어두운 덩어리로 살아났기 때문이다.)

⚠ **위 표의 "검증 판정" 열은 비대칭 규칙을 적용한 결과이지만, 규칙을 바꾼 뒤
   `--no-weld`·`--no-creep` 를 다시 돌리지는 않았다.** 각 행의 "카메라가 본 것"
   은 실측이고 규칙은 결정적(구멍이 보이면 미수리)이라 결과가 뒤집힐 여지는
   없지만, 회귀 확인이 필요하면 세 조건을 다시 돌릴 것.

## 실측 결과 (기본 설정, --headless)

    안착        휠 밀착 12/12, 반경 41.56~41.61mm (목표 42.0), 축 이동 +0.1mm
    굽힘 1      11.6초 통과, 벨로우즈 최대 30.1°
    굽힘 2      22.9초 통과, 벨로우즈 최대 30.6°
    굽힘 3      34.0초 통과, 벨로우즈 최대 30.5°
    카메라      자세 실측 광축↔접선 0.32° / 화면위↔관위 0.25°
    후보 기각   굽힘의 터널 끝 3회 (ø169~175mm — 크기로 걸러냄)
    검출        s=1481mm 에서 첫 검출(결함 119mm 앞), 2회 일치로 확정
                목표 s=1599.5mm / 179.3°  vs 정답 1600 / 180
                **검출 오차 축 −0.50mm / 시계 −0.68°(원주 −0.60mm)**
    정렬        링 −180.2° → 팁 시계각 180.0° (검출 목표 대비 +0.74°)
    미세정렬    축오차 −0.24mm
    토치 신장   팁 반경 46.60mm — 관벽까지 간극 3.40mm
    용접        정렬 오차 0.70mm ≤ 1.5mm → ✅ 수리 성공
    검증        140mm 후진 → 구멍 없음 / 비드 있음 / Depth "메워짐 −1.78mm"
                → 판정 '수리됨' vs 물리 실제 '수리됨' ✅ 일치
    완주        45초 안팎, s=1652mm, 휠 밀착 12/12
    덩어리 내역 {작음 5, 큼 6, 중앙(관저끝) 151, 화면가장자리 94,
                 테두리어두움 0, 통과 25}  ← 임계를 손보려면 이 숫자를 볼 것

    ※ "코스의 93.3%" 는 `GOAL_S = S_TOTAL − 120mm` 이기 때문이다. 로봇이 관
      끝으로 굴러 나가지 않게 훅 끝 120mm 앞을 완주선으로 둔다.

실행 (WebRTC 스트리밍은 isaac_python 이 자동으로 켠다):
    PYTHONUNBUFFERED=1 isaac_python zigzag_demo.py --hold      # 화면으로 본다
    ISAAC_STREAM=0 isaac_python zigzag_demo.py --headless      # 로그만
    isaac_python zigzag_demo.py --glass --no-vision --hold     # 밖에서 들여다본다
    isaac_python zigzag_demo.py --flex 20 --headless           # 출고 상태 재현
    isaac_python zigzag_demo.py --no-weld --headless           # 검증층만 시험

🚨 밖에서 보려고 `--glass` 만 주면 **검출 정확도가 6배 나빠져 용접이 실패한다**
   (위 절 참조). 용접까지 보려면 `--no-vision` 을 같이 줄 것.

옵션
    --headless   렌더를 끈다. 🚨 스트리밍으로 볼 거면 주지 말 것 —
                 world.step(render=False) 가 되어 화면이 검게 멈춘다.
    --hold       끝나고 창을 열어 둔다
    --glass      배관을 반투명으로 (표시 전용, 물리 무관)
                 🚨 검출 정확도가 6배 나빠진다 — `--no-vision` 과 같이 쓸 것
    --fluid      만관 — 마찰이 0.30/0.25 로 바뀐다 (해석적 유체력은 미구현)
    --flex D     벨로우즈 스윙 리밋 ±D° (기본 30, 출고값 20)
    --no-defect  결함 없이 주행만
    --no-creep   축 미세정렬을 끈다 — 대조군. 수리가 실패해야 정상이다
    --no-weld    아크·SWAP 을 건너뛴다 — **검증층 대조군**. Depth 가 "파임" 을
                 내야 정상이다
    --no-vision  카메라를 끄고 정답 좌표로 간다 (물리만 볼 때)
    --shots      판정 프레임을 zigzag/out/ 에 저장
    --steps N    물리 스텝 수 (기본 20000 ≈ 83초. 카메라가 렌더를 더 굽는다)

환경변수
    SPEED_MPS=0.05   주행 속도          START_S=0.20     출발 진행거리(m)
    DEFECT_S=1.60    결함 진행거리(m)   DEFECT_CLOCK=180 결함 시계각(deg)
    PHYSICS_HZ=240   물리 주파수 (내리지 말 것)
    CAM_RES=640x360  카메라 해상도. 🚨 바꾸면 화소 기준 면적 임계가 같이 움직인다
"""

import math
import os
import sys
from pathlib import Path

HEADLESS = "--headless" in sys.argv
HOLD = "--hold" in sys.argv
GLASS = "--glass" in sys.argv
FLUID = "--fluid" in sys.argv
NO_DEFECT = "--no-defect" in sys.argv
# --no-creep : 축 미세정렬을 건너뛴다. **검증이 살아 있는지 보는 대조군**이다.
# 이걸 주면 개루프 정지 위치 그대로 용접하므로 축오차가 −8mm 대로 남고
# 수리가 실패해야 정상이다. 실패하지 않으면 판정이 자기충족이라는 뜻이다.
NO_CREEP = "--no-creep" in sys.argv
# --no-vision : 카메라를 끄고 정답 좌표로 간다. 카메라 없이 물리만 볼 때만 쓸 것.
NO_VISION = "--no-vision" in sys.argv
# --no-weld : 아크·SWAP 을 건너뛴다. **검증층만 따로 시험하는 대조군**이다.
# 결함이 손대지 않은 채로 남으므로 VERIFY 가 "구멍 있음 / 미수리" 를 내야 정상이다.
NO_WELD = "--no-weld" in sys.argv
SHOTS = "--shots" in sys.argv        # 판정 프레임을 out/ 에 저장
# 스텝 상한은 **코스 길이에서 유도한다** (아래 course import 뒤). 여기서는
# 손으로 준 값만 받아 둔다 — course 는 Isaac 모듈보다 뒤에 import 되기 때문이다.
STEPS = (int(sys.argv[sys.argv.index("--steps") + 1])
         if "--steps" in sys.argv else None)
FLEX = float(sys.argv[sys.argv.index("--flex") + 1]) if "--flex" in sys.argv else 30.0

sys.path.insert(0, str(Path(__file__).resolve().parent))

from isaacsim import SimulationApp                        # noqa: E402

simulation_app = SimulationApp({"headless": HEADLESS})

import numpy as np                                        # noqa: E402
from isaacsim.core.api import World                       # noqa: E402
from isaacsim.core.prims import SingleArticulation        # noqa: E402
from isaacsim.core.utils.types import ArticulationAction  # noqa: E402
from pxr import Gf, UsdGeom, UsdLux, UsdPhysics           # noqa: E402

import course                                             # noqa: E402
import defect as defect_mod                               # noqa: E402
import scene                                              # noqa: E402
import vision                                             # noqa: E402

PHYSICS_HZ = float(os.environ.get("PHYSICS_HZ", 240))
PHYSICS_DT = 1.0 / PHYSICS_HZ

TARGET_SPEED_MPS = float(os.environ.get("SPEED_MPS", 0.05))
SPIN_DEG_S = math.degrees(TARGET_SPEED_MPS / scene.WHEEL_R)
CONTACT_OFFSET = max(0.0005, 1.2 * TARGET_SPEED_MPS / PHYSICS_HZ)

START_S = float(os.environ.get("START_S", 0.20))
SETTLE_STEPS = 600
GOAL_S = course.S_TOTAL - 0.12

# 🚨 스텝 상한을 **코스 길이에서 유도한다.** 예전 상수 20000 은 훅(1.77m)
#    기준이라 연장 코스(long, 5.05m)에서는 로봇이 결함에 닿기도 전에 루프가
#    끝난다. 주행분에 15% 여유(굽힘 감속·이완)와 시퀀스 몫 6000 스텝을 더한다.
#    훅에서는 예전과 같은 ~20000 이 나온다.
if STEPS is None:
    STEPS = int((GOAL_S - START_S) / TARGET_SPEED_MPS * PHYSICS_HZ * 1.15) + 6000

# ── 결함 ────────────────────────────────────────────────────────────
# 마지막 직선(s 1421~1771mm) 한가운데. 굽힘 3개를 다 지난 뒤에 만나므로
# 주파 능력과 수리 능력을 한 번에 보여 준다.
# 🚨 결함 STL 은 직관 전용이다 — `defect.install()` 이 굽힘이면 중단시킨다.
DEFECT_S = float(os.environ.get("DEFECT_S", 1.60))
# 시계각 180° = 바닥. 휠 궤도(90/210/330°, 각 ±8.5°)와 ø28 개구(±16.3°)의
# 최소 여유가 5.21° 다 (`build_defect_w56.py` 가 검산해서 찍는다).
DEFECT_CLOCK_DEG = float(os.environ.get("DEFECT_CLOCK", 180.0))
DEFECT_DIA_MM = 28.0
ALIGN_TOL_MM = 1.5           # welder/config/weld.yaml 의 align_tol_mm
ARC_S = 2.0                  # 같은 파일 arc_s
# Depth 판정 임계도 같은 파일에서 가져온다 (`welder/config/weld.yaml`)
WELD_K = {"band_px": 36, "median_px": 3, "min_deep_px": 6,
          "depth_defect_mm": 0.6, "depth_repaired_mm": 0.25,
          "profile_min_px": 60, "bore_r_mm": 50.0}
_res = os.environ.get("CAM_RES", "640x360").lower().split("x")
CAM_RES = (int(_res[0]), int(_res[1]))
OUT = Path(__file__).resolve().parent / "out"

FLOODED = FLUID

print("=" * 78)
print(course.describe())
print("=" * 78)

world = World(stage_units_in_meters=1.0,
              physics_dt=PHYSICS_DT, rendering_dt=1.0 / 60.0)
stage = scene.build_stage(world, contact_offset=CONTACT_OFFSET,
                          flooded=FLOODED, glass=GLASS)
yaw = scene.place_robot(stage, START_S)

_n_rel = scene.relax_bellows(stage, FLEX)
print(f"[준비] 벨로우즈 스윙 리밋 ±{FLEX:.0f}° (D6 {_n_rel}개) — usda 출고값은 "
      f"±20°, 실측 통과 임계는 ±25°"
      + ("  🚨 출고값으로는 첫 굽힘에서 멈춘다" if FLEX < 25 else ""))

# ── 결함 설치 ───────────────────────────────────────────────────────
dfc = None
if not NO_DEFECT:
    dfc = defect_mod.install(stage, DEFECT_S, DEFECT_CLOCK_DEG,
                             dia_mm=DEFECT_DIA_MM,
                             contact_offset=CONTACT_OFFSET)
    print(f"[준비] 결함 ø{DEFECT_DIA_MM:g}mm  s={DEFECT_S * 1000:.0f}mm "
          f"시계각 {DEFECT_CLOCK_DEG:.0f}°({'바닥' if DEFECT_CLOCK_DEG == 180 else '기타'}) "
          f"— 배관 삼각형 {dfc.n_removed}개 제거 "
          f"({dfc.n_tris} → {dfc.n_tris - dfc.n_removed})")
    print(f"       비드·마개는 숨김. 결함 중심 월드 "
          f"{np.round(dfc.world * 1000, 1)}mm")

_n_off, _n_wheel = scene.apply_contact_offset(stage, CONTACT_OFFSET)
print(f"[준비] 관 상태 {'만관' if FLOODED else '배수'} — 마찰 "
      f"{0.30 if FLOODED else 0.40}/{0.25 if FLOODED else 0.35}"
      f"   배관 표시 {'반투명(유리)' if GLASS else '불투명'}")
if GLASS:
    # 🚨 `repair_demo.py` 가 남긴 경고와 같은 이유다. 관이 반투명해지면 로봇
    #    조명이 벽에서 반사돼 돌아오지 않아 **영상이 어두워지고 대비가 죽는다.**
    #    이 데모는 결함을 **카메라로 찾아가므로** 검출이 실패할 수 있다.
    #    물리에는 아무 영향이 없다 — 물리 재질은 materialPurpose="physics" 로
    #    따로 바인딩되고 유리는 표시 재질만 덮는다.
    print("[경고] --glass 는 **밖에서 들여다보기 위한 표시 옵션**이다. "
          "관이 반투명해지면")
    print("       조명이 벽에 반사돼 돌아오지 않아 **카메라 검출을 믿을 수 없다.**")
    print("       검출이 실패하면 결함을 못 찾고 지나친다 — 촬영·시연용으로만 쓸 것.")
    print("       검출까지 보려면 --glass 를 빼거나, 위치를 알고 가는 "
          "--no-vision 과 함께 줄 것.")
print(f"[준비] 주행 {TARGET_SPEED_MPS * 1000:.0f} mm/s "
      f"(휠 {SPIN_DEG_S:.0f} deg/s, 한 스텝 "
      f"{TARGET_SPEED_MPS / PHYSICS_HZ * 1000:.3f}mm) → contactOffset "
      f"{CONTACT_OFFSET * 1000:.2f}mm, 프림 {_n_off}개 (휠 {_n_wheel}/12)")

art = SingleArticulation(prim_path=scene.ROBOT, name="zigzag_welder")
world.scene.add(art)
world.reset()

dof = list(art.dof_names or [])
idx = scene.resolve_dofs(dof)
wheel_idx = np.array(idx["wheel"])
RING_I, TORCH_I = idx["ring"], idx["torch"]

_links = [q for q in stage.Traverse()
          if str(q.GetPath()).startswith(scene.ROBOT + "/")
          and q.HasAPI(UsdPhysics.RigidBodyAPI)]
_mass = sum(float(UsdPhysics.MassAPI(q).GetMassAttr().Get() or 0.0)
            for q in _links if UsdPhysics.MassAPI(q).GetMassAttr())
_norm = scene.N_LEG * min(scene.PRELOAD_N, 60.0)
_fric = 0.30 if FLOODED else 0.40
print("=" * 78)
print(f"조립  DOF {len(dof)} = 휠 {len(idx['wheel'])} / 서스펜션 "
      f"{len(idx['susp'])} / 벨로우즈 {len(idx['bellows'])} / 링·토치 2"
      f"   물리 1/{PHYSICS_HZ:.0f}")
print(f"질량  {_mass * 1000:.0f} g (링크 {len(_links)}개)  중량 {_mass * 9.81:.2f} N")
print(f"견인  예압 {scene.PRELOAD_N:.0f} N × {scene.N_LEG} 다리 → 수직항력 "
      f"{_norm:.0f} N × 마찰 {_fric} = {_norm * _fric:.0f} N "
      f"(중량의 {_norm * _fric / (_mass * 9.81):.0f}배)")

# ── 아크 조명 · 스파크 ──────────────────────────────────────────────
arc_light = UsdLux.SphereLight.Define(stage, "/World/ArcLight")
arc_light.CreateIntensityAttr(0.0)
arc_light.CreateRadiusAttr(0.004)
arc_light.CreateColorAttr(Gf.Vec3f(0.75, 0.85, 1.0))
_arc_op = UsdGeom.Xformable(arc_light).AddTranslateOp()

sparks = None
if not HEADLESS:
    try:
        from spark_fx import SparkFX                       # noqa: E402
        sparks = SparkFX(stage, "/World/weld_sparks", flooded=FLOODED)
        print(f"[준비] 아크 스파크 — {'수중(급냉)' if FLOODED else '기중'} 조건, "
              f"시각 전용(물리·판정 무관)")
    except Exception as exc:
        print(f"[경고] 스파크 초기화 실패 — 없이 진행 ({exc})")


def spark_confine(pts):
    """스패터를 관 안에 가둔다. `course` 를 그대로 쓰므로 굽힘에서도 정확하다."""
    s, _, r = course.wall_uv_many(pts)
    cx, cy = [], []
    out = np.zeros_like(pts)
    for i, ss in enumerate(s):
        x, y, tx, ty = course.point_at(ss)
        out[i] = pts[i] - np.array([x, y, 0.0])
    rr = np.linalg.norm(out, axis=1)
    return rr, out / np.maximum(rr, 1e-12)[:, None], course.PIPE_IR


def wall_inward(p):
    """점 p 에서 관 **안쪽**을 향하는 단위벡터 (스패터가 튀는 쪽)."""
    s, clock, r = course.wall_uv(p)
    o, t, l, u = course.frame_at(s)
    th = math.radians(clock)
    outward = u * math.cos(th) + l * math.sin(th)
    return -outward


# ── 제어 ────────────────────────────────────────────────────────────
def drive(deg_s):
    art.apply_action(ArticulationAction(
        joint_velocities=np.full(len(wheel_idx), math.radians(deg_s)),
        joint_indices=wheel_idx))


def hold_station(d_ax):
    """토치 팁을 결함 축위치에 **능동으로** 붙잡는다.

    🚨 휠 목표속도를 0 으로 두는 것으로는 자리가 안 지켜진다. 휠 드라이브는
       강성 0 · 감쇠 0.012 · maxForce 0.08 N·m 인 **속도 드라이브**라 정지
       토크가 거의 없는데, 굽힘을 지나며 12~14° 접힌 벨로우즈가 펴지려는
       복원력으로 로봇을 계속 민다. 실측: 정지 직후 2~4mm 뒤로 이완했고,
       이는 정렬 허용치 1.5mm 보다 크다 — 정적 정렬로는 원리적으로 못 맞춘다.
    → 오차에 비례한 속도를 계속 준다. 실기의 스테이션 키핑과 같은 방식이고,
      아크가 도는 2초 동안에도 자리를 지켜야 하므로 EXTEND·ARC 에서도 부른다.
    """
    if NO_CREEP:
        drive(0.0)          # 대조군 — 잡지 않는다 (위 --no-creep 설명 참조)
        return
    if abs(d_ax) < HOLD_DEADBAND_MM:
        drive(0.0)
        return
    # 🚨 비례 제어만 쓰면 **정상상태 오차가 남는다.** 휠은 강성 0 · 감쇠
    #    0.012 N·m·s/rad 인 순수 속도 드라이브라 토크가 속도 오차에 비례한다:
    #      명령 17 deg/s → 0.0035 N·m ×12륜 ÷ 0.008m = 5.3 N  ← 못 움직인다
    #      명령 25 deg/s → 0.0052 N·m ×12륜 ÷ 0.008m = 7.9 N  ← 움직인다
    #    실측: 오차 1.2mm 에서 P 이득만으로 16.8 deg/s 가 나왔고 로봇은
    #    1536.8mm 에 **완전히 멈춰 있었다**(30초 상한까지). 그래서 데드밴드
    #    밖에서는 **최소 명령**을 깔아 항상 구동 권한을 확보한다.
    mag = min(max(HOLD_KP_DEG_S_PER_MM * abs(d_ax), HOLD_MIN_DEG_S),
              HOLD_VMAX_DEG_S)
    drive(-math.copysign(mag, d_ax))


def set_torch(ring_deg=None, extend_m=None):
    ii, vv = [], []
    if ring_deg is not None:
        ii.append(RING_I)
        vv.append(math.radians(ring_deg))
    if extend_m is not None:
        ii.append(TORCH_I)
        vv.append(extend_m)
    if ii:
        art.apply_action(ArticulationAction(joint_positions=np.array(vv),
                                            joint_indices=np.array(ii)))


_XC = UsdGeom.XformCache()
_torch_prim = stage.GetPrimAtPath(f"{scene.ROBOT}/WeldTorch")
_ring_prim = stage.GetPrimAtPath(f"{scene.ROBOT}/WeldRing")
# 🚨 팁 끝은 **프림 원점이 아니라 원뿔 꼭짓점**이다. 원점으로 재면 팁 길이
#    8mm 를 통째로 빼먹어 "간극 12mm" 같은 거짓 수치가 나온다.
#    Tip_Idle: 축 Z, 높이 4mm, 로컬 z=+6mm → 꼭짓점 z=+8mm.
TIP_LOCAL = Gf.Vec3d(0.0, 0.0, 0.008)


def wpos(prim):
    _XC.Clear()
    t = _XC.GetLocalToWorldTransform(prim).ExtractTranslation()
    return np.array([float(t[0]), float(t[1]), float(t[2])])


def tip_world():
    _XC.Clear()
    w = _XC.GetLocalToWorldTransform(_torch_prim).Transform(TIP_LOCAL)
    return np.array([float(w[0]), float(w[1]), float(w[2])])


_wheel_prims = [stage.GetPrimAtPath(f"{scene.ROBOT}/{side}Body_{g}{i}_Wheel")
                for side in ("Rear", "Front") for g in ("A", "B")
                for i in range(3)]
_WHEEL_NAMES = [f"{side}_{g}{i}" for side in ("R", "F")
                for g in ("A", "B") for i in range(3)]


def wheel_radii():
    _XC.Clear()
    out = []
    for p in _wheel_prims:
        t = _XC.GetLocalToWorldTransform(p).ExtractTranslation()
        w = np.array([float(t[0]), float(t[1]), float(t[2])])
        _, d, _, _, _, _ = course.project(w[0], w[1])
        out.append(math.hypot(d, w[2]) * 1000)
    return np.array(out)


def body_yaw(path):
    _XC.Clear()
    ax = _XC.GetLocalToWorldTransform(stage.GetPrimAtPath(path)).TransformDir(
        (1.0, 0.0, 0.0))
    return math.degrees(math.atan2(ax[1], ax[0]))


def diagnose(s, mid, jp, bel_rot):
    """막혔을 때 원인을 좁히는 정보. 최대값만으로는 원인을 못 가린다."""
    print("       ── 벨로우즈 관절별 (리밋 ±%.0f°) ──" % FLEX)
    for nm, v in zip(idx["bellows_rot_names"], bel_rot):
        print(f"          {nm:10} {v:+7.2f}°"
              + (" 🚨리밋" if abs(v) > FLEX - 1.0 else ""))
    _, _, tx, ty, _, _ = course.project(mid[0], mid[1])
    tan = math.degrees(math.atan2(ty, tx))
    yr = body_yaw(f"{scene.ROBOT}/RearBody")
    yf = body_yaw(f"{scene.ROBOT}/FrontBody")
    print(f"       ── 자세 ── 접선 {tan:+.1f}°  후방 {yr:+.1f}°  전방 {yf:+.1f}°"
          f"  본체간 꺾임 {(yf - yr + 180) % 360 - 180:+.1f}°")
    rr = wheel_radii()
    print("       ── 휠 반경 (밀착 42.0mm) ──")
    print("          " + "  ".join(
        f"{n}:{v:5.1f}{'!' if abs(v - 42.0) > 3.0 else ' '}"
        for n, v in zip(_WHEEL_NAMES, rr)))
    su = jp[idx["susp"]] * 1000
    print("       ── 서스펜션 (리밋 −4.0~+6.0mm) ──")
    print("          " + "  ".join(
        f"{n}:{v:+5.2f}{'!' if v <= -3.95 or v >= 5.95 else ' '}"
        for n, v in zip(_WHEEL_NAMES, su)))


prog = scene.Progress(stage)

# ── 안착 ────────────────────────────────────────────────────────────
s_before, _, _, _ = prog.read()
for _ in range(SETTLE_STEPS):
    world.step(render=not HEADLESS)
s_after, mid, rear, front = prog.read()

for b in scene.verify_dof_roles(art, idx, dof):
    print(f"🚨 [DOF 검증] {b}")

r0 = wheel_radii()
_seat = scene.WHEEL_SEAT_R * 1000
print("=" * 78)
print(f"[안착] {SETTLE_STEPS} 스텝 — s {s_before * 1000:.1f} → "
      f"{s_after * 1000:.1f}mm ({(s_after - s_before) * 1000:+.1f}mm)")
print(f"       휠 밀착 {int(np.sum(np.abs(r0 - _seat) < 1.5))}/12  "
      f"반경 {r0.min():.2f}~{r0.max():.2f}mm (목표 {_seat:.1f})")
_tip0 = tip_world()
_, _, _tipr = course.wall_uv(_tip0)
print(f"       토치 팁 반경 {_tipr * 1000:.2f}mm (신장 0) — 관벽 50.0mm 까지 "
      f"{50.0 - _tipr * 1000:.2f}mm, 최대 신장 5mm 시 "
      f"{50.0 - _tipr * 1000 - 5.0:.2f}mm")

# ── 카메라 ──────────────────────────────────────────────────────────
# 🔑 **카메라는 옵션이 아니라 이 로봇의 주 센서다.** 결함을 찾아가는 것도,
#    수리를 확인하는 것도 이걸로 한다. 정답 좌표(DEFECT_S/DEFECT_CLOCK)는
#    **점수 매기기에만** 쓴다 — 주행·정렬에 쓰면 검증이 자기충족이 된다.
vis = None if NO_VISION else vision.Vision(
    stage, world, scene.ROBOT, res=CAM_RES, headless=HEADLESS)
if vis is not None and vis.ok:
    print(f"[준비] {vis.describe()}")
    _pv = vis.verify_pose()
    if _pv is not None:
        _ef, _eu = _pv
        print(f"       자세 실측 — 광축↔코스접선 {_ef:.2f}°, "
              f"화면위↔관위 {_eu:.2f}°"
              + ("  ✅" if max(_ef, _eu) < 5.0
                 else "  🚨 사원수 부호가 틀렸다 — 검출이 조용히 죽는다"))
elif not NO_VISION:
    print("[경고] 카메라 초기화 실패 — 정답 좌표로 대체 진행")

# ── 시퀀스 ──────────────────────────────────────────────────────────
# 개루프 정지는 **대략** 세우기만 한다. 정밀 정렬은 CREEP 이 폐루프로 한다.
STOP_LEAD = 0.004
# 스테이션 키핑 이득. 오차 1mm 에 14 deg/s(= 2 mm/s) 로 되돌린다.
# 🚨 상한을 크게 잡으면 안 된다. 상태기계가 12 스텝(0.05초)마다 도므로
#    10 mm/s 면 한 틱에 0.5mm 를 움직여 데드밴드를 통째로 뛰어넘고 진동한다
#    (실측: 20초간 1536~1538mm 왕복). 5 mm/s 면 한 틱 0.25mm 다.
HOLD_KP_DEG_S_PER_MM = 14.0
HOLD_MIN_DEG_S = 25.0         # 3.5 mm/s — 이 밑으로는 토크가 안 나온다(위 주석)
HOLD_VMAX_DEG_S = math.degrees(0.005 / scene.WHEEL_R)    # 5 mm/s
# 데드밴드는 **한 틱 이동량보다 커야** 채터링이 허용치를 안 넘는다.
#   최소명령 3.5 mm/s × 틱 0.05초 = 0.175mm  → 채터 진폭 ≈ 0.2 + 0.175
HOLD_DEADBAND_MM = 0.20
CREEP_TOL_MM = 0.5            # 이 안에 1초 이상 머물면 정렬 완료
CREEP_HOLD_TICKS = 20         # 12스텝 간격 × 20 = 1.0초
state = "DRIVE" if dfc is not None else "RUNOUT"
t_state = 0
creep_hold = 0
align_mm = float("nan")
swap_done = False
result = {}

# ── 카메라로 찾아가기 ───────────────────────────────────────────────
# 🚨 설계 카메라는 10Hz(=24스텝) 인데 그러면 결함이 보이는 구간에
#    **표본이 2개**뿐이라 기울기를 못 믿는다. 20Hz 로 올려 4개쯤 잡는다.
#    비용은 한 번당 warm_scan 렌더뿐이다.
SCAN_EVERY = 12               # 240Hz ÷ 12 = 20Hz
# 🚨 **검출을 몇 번 모았다고 확정하면 안 된다.** 처음엔 "서로 15mm 안에서
#    일치하는 검출 2회" 로 했는데 뚫렸다(GUI 실행 실측): 후보 목록을 계속
#    쌓기만 해서 **s=774mm 에서 본 것과 s≈1234mm 에서 본 것이 우연히 짝**이 됐고,
#    로봇이 정답(1600mm)에서 366mm 떨어진 자리에 용접하러 갔다.
#    → 두 가지를 같이 요구한다.
#      ① 최근 것만 본다 — 로봇이 SCAN_WINDOW_MM 이상 지난 후보는 버린다
#      ② **로봇이 움직이는 동안** 추정 s 가 고정돼야 한다
#         진짜 벽 구멍은 어디서 봐도 같은 s 를 준다. 굽힘 터널의 가장자리는
#         로봇이 가면 같이 흘러가므로 이 조건에서 떨어져 나간다.
#    실측으로 창이 좁다는 것도 확인했다: 관문을 통과한 덩어리 19개 중 데모
#    관문까지 넘은 것은 **3회**뿐이었다(가까워지면 구멍이 화면 아래 가장자리에
#    걸려 66회가 "화면가장자리" 로 버려진다 — 잘린 덩어리는 넓이·중심이 틀리므로
#    버리는 게 맞다). 그래서 기선은 10mm 로 잡고, 대신 **일치 폭을 6mm 로 조여**
#    "고정된 것인가" 를 직접 본다:  기울기 = s추정 흩어짐 / 로봇 이동 ≤ 0.6
SCAN_AGREE_MM = 0.020        # 같은 것으로 묶는 폭 (느슨하게 — 판별은 기울기가 한다)
SCAN_NEED = 2                # 최소 검출 수
SCAN_BASELINE_MM = 0.005     # 그 검출들이 걸쳐야 하는 **로봇 이동거리**
# 🔑 **판별은 기울기로 한다.**  기울기 = (추정 s 흩어짐) / (로봇 이동거리)
#      벽에 고정된 진짜 구멍  → 어디서 봐도 같은 s   → 기울기 ≈ 0 (실측 0.014)
#      굽힘 터널의 가장자리   → 로봇을 따라 흘러간다 → 기울기 ≈ 1
#    절대 임계(“기선 10mm 이상”)로는 못 가른다 — 검출 창이 원래 좁기 때문이다.
#    실측: 결함이 보이는 구간이 **2프레임(로봇 1481→1488mm, 기선 7mm)** 뿐이라
#    10mm 를 요구하니 진짜 구멍이 확정에서 떨어졌다.
SCAN_SLOPE_MAX = 0.40
SCAN_WINDOW_MM = 0.150       # 이보다 오래된 후보는 버린다
# 후보 거르기 임계 — **결함 위치를 모르는 채로** 쓸 수 있는 값만 쓴다.
HOLE_DIA_MIN_MM, HOLE_DIA_MAX_MM = 8.0, 60.0
HOLE_RANGE_MAX_M = 0.30
scan_hits = []
tgt_s = tgt_clock = None      # **검출로 얻은** 목표. 정답이 아니다.
ring_cmd = 0.0
VISION_ON = vis is not None and vis.ok
if not VISION_ON and dfc is not None:
    # 카메라가 없으면 갈 곳을 알 방법이 없다. 물리만 보려는 경우이므로 정답을
    # 쓰되 **로그에 분명히 남긴다** — 이 모드의 결과는 검출 성능이 아니다.
    tgt_s, tgt_clock = DEFECT_S, DEFECT_CLOCK_DEG
    ring_cmd = -tgt_clock
    print("[경고] 카메라 없음 — 정답 좌표로 조준한다 (검출 성능 평가 불가)")
detect_log = {"first_s": None, "n": 0, "rejected": 0}
# 용접 뒤 검증하려면 후진해야 한다 — 카메라가 토치보다 33mm 앞이라 용접 자리가
# 제자리에서는 화각 밖이다(vision.py 머리말의 계산). 140mm 물러나면 카메라가
# 결함 107mm 앞에 서고 r_px ≈ 114px 로 판정 창(≤144px) 안에 들어온다.
REPOSITION_MM = 140.0
repos_from = None
verify = {}
extra_steps = 0               # frames() 가 굽는 렌더 스텝 (시간 계산 보정)


def aim_error(tip, t_s, t_clock):
    """토치 끝과 **목표**(검출값)의 관벽 평면 어긋남. 판정이 아니라 조준용이다."""
    s_t, c_t, _ = course.wall_uv(tip)
    d_ax = (s_t - t_s) * 1000.0
    d_ci = course.PIPE_IR * math.radians(
        (c_t - t_clock + 180.0) % 360.0 - 180.0) * 1000.0
    return math.hypot(d_ax, d_ci), d_ax, d_ci

print("=" * 78)
print(f"[주행] 시작 — {TARGET_SPEED_MPS * 1000:.0f} mm/s  "
      + (f"결함 s={DEFECT_S * 1000:.0f}mm 에서 정지 예정"
         if dfc else "결함 없음 (주행만)"))
drive(SPIN_DEG_S)

t0 = SETTLE_STEPS
s_prev, stall, worst_bellows = s_after, 0, 0.0
bend_log = [None] * len(course.BEND_SPANS)
reached = False

for step in range(STEPS - SETTLE_STEPS):
    world.step(render=not HEADLESS)
    t_state += 1
    now = (step + t0 + extra_steps) / PHYSICS_HZ

    if sparks is not None:
        on = state == "ARC"
        o = tip_world() if on else None
        sparks.step(PHYSICS_DT, emitting=on, origin=o,
                    normal=wall_inward(o) if on else None,
                    light=arc_light if on else None,
                    confine=spark_confine if on else None)

    if step % 12:
        continue

    s, mid, rear, front = prog.read()
    jp = np.asarray(art.get_joint_positions())
    bel_rot = np.degrees(jp[idx["bellows_rot"]])
    bel_deg = float(np.abs(bel_rot).max())
    worst_bellows = max(worst_bellows, bel_deg)

    for k, (a, b) in enumerate(course.BEND_SPANS):
        if bend_log[k] is None and s > b:
            bend_log[k] = (now, bel_deg)
            print(f"  [굽힘 {k + 1}/3 통과] s={s * 1000:.0f}mm  {now:.1f}초  "
                  f"벨로우즈 최대 {bel_deg:.1f}°/{FLEX:.0f}°")

    # ── 상태 기계 ───────────────────────────────────────────────────
    if state == "DRIVE":
        s_ring, _, _ = course.wall_uv(wpos(_ring_prim))

        # ── 훑기 — 정답을 **전혀** 안 쓰는 순수 검출 ─────────────────
        if tgt_s is None and vis is not None and vis.ok and step % SCAN_EVERY == 0:
            rgb, _ = vis.frames(warm=vis.warm_scan)
            extra_steps += vis.warm_scan
            hole = None if rgb is None else vis.find_wall_hole(rgb)
            m = vis.hole_measure(hole) if hole else None
            hit = None
            if m is not None:
                # ── 후보 거르기 (전부 **위치를 모르는 채로** 판단한다) ──
                #  ① 크기 — 관 내경 100mm 짜리 관에 ø60 넘는 구멍은 없고,
                #     ø8 미만은 용접 대상이 아니다. 굽힘의 어두운 터널 끝은
                #     여기서 ø225mm 로 계산돼 걸러진다(실측).
                #  ② 사거리 — 너무 멀면 화소가 몇 개 안 돼 위치가 안 나온다.
                #  ③ 굽힘 — 결함 STL 이 직관 전용이라 굽힘에는 못 놓는다.
                #     🚨 **알려진 한계다.** 굽힘 안 결함은 이 데모가 못 고친다.
                #  ④ 이미 지나친 자리는 버린다.
                why = None
                if not (HOLE_DIA_MIN_MM <= m["dia_mm"] <= HOLE_DIA_MAX_MM):
                    why = f"크기 ø{m['dia_mm']:.0f}mm (허용 {HOLE_DIA_MIN_MM:.0f}~{HOLE_DIA_MAX_MM:.0f})"
                elif m["range_m"] > HOLE_RANGE_MAX_M:
                    why = f"사거리 {m['range_m'] * 1000:.0f}mm"
                elif course.in_bend(m["s"]):
                    why = "굽힘 구간 (결함 STL 은 직관 전용)"
                elif m["s"] <= s_ring + 0.02:
                    why = "이미 지나침"
                if why is None:
                    hit = (m["s"], m["clock"])
                elif detect_log["rejected"] < 3:
                    detect_log["rejected"] += 1
                    print(f"  [검출] 후보 기각 — {why}  "
                          f"(면적 {hole['area_px']:,}px, s={m['s'] * 1000:.0f}mm, "
                          f"사거리 {m['range_m'] * 1000:.0f}mm)  {now:.1f}초")
            if hit is not None:
                if detect_log["first_s"] is None:
                    detect_log["first_s"] = s_ring
                detect_log["n"] += 1
                scan_hits.append((hit[0], hit[1], s_ring))
                # ① 오래된 후보 버리기
                scan_hits[:] = [h for h in scan_hits
                                if s_ring - h[2] <= SCAN_WINDOW_MM]
                # ② 같은 자리를 가리키면서 ③ 로봇이 움직이는 동안 유지된 것만
                agree = [h for h in scan_hits
                         if abs(h[0] - hit[0]) < SCAN_AGREE_MM]
                base = (max(h[2] for h in agree) - min(h[2] for h in agree)
                        if agree else 0.0)
                spread = (max(h[0] for h in agree) - min(h[0] for h in agree)
                          if agree else 0.0)
                slope = spread / base if base > 1e-9 else 9.9
                if detect_log["n"] <= 12:
                    print(f"  [검출] 후보 #{detect_log['n']} 면적 "
                          f"{hole['area_px']:,}px → s={hit[0] * 1000:.1f}mm "
                          f"시계각 {hit[1]:.1f}° (로봇 {s_ring * 1000:.0f}mm) "
                          f"| 묶음 {len(agree)}/{SCAN_NEED} 기선 "
                          f"{base * 1000:.1f}mm 기울기 {slope:.3f}"
                          f"/{SCAN_SLOPE_MAX}  {now:.1f}초")
                if (len(agree) >= SCAN_NEED and base >= SCAN_BASELINE_MM
                        and slope <= SCAN_SLOPE_MAX):
                    tgt_s = float(np.median([h[0] for h in agree]))
                    tgt_clock = float(np.median([h[1] for h in agree]))
                    ring_cmd = -tgt_clock       # 개루프 초기값 (ALIGN 주석 참조)
                    print(f"  [검출] ✅ 확정 — 묶음 {len(agree)}회 / 기선 "
                          f"{base * 1000:.1f}mm / 기울기 {slope:.3f} → 목표 "
                          f"s={tgt_s * 1000:.1f}mm 시계각 {tgt_clock:.1f}°"
                          f"   (정답 {DEFECT_S * 1000:.0f}mm / "
                          f"{DEFECT_CLOCK_DEG:.0f}° — 오차 축 "
                          f"{(tgt_s - DEFECT_S) * 1000:+.1f}mm / 시계 "
                          f"{(tgt_clock - DEFECT_CLOCK_DEG + 180) % 360 - 180:+.1f}°)")

        if tgt_s is not None and s_ring >= tgt_s - STOP_LEAD:
            drive(0.0)
            state, t_state = "ALIGN", 0
            print(f"  [정지] 목표 앞 — 링 s={s_ring * 1000:.1f}mm  {now:.1f}초")
        elif s >= GOAL_S:
            print(f"  🚨 [놓침] 결함을 못 찾고 코스 끝에 도달 "
                  f"(검출 시도 {detect_log['n']}회)  {now:.1f}초")
            state, t_state = "RUNOUT", 0

    elif state == "ALIGN":
        # 🔑 토치는 링 각 0 에서 로봇 로컬 +Z(시계각 0)를 본다. 링을 로컬 X 축
        #    둘레로 φ 만큼 돌리면 방향은 (0, −sinφ, cosφ) 가 되므로
        #    **시계각 = −φ** 다. 개루프로 φ = −θ 를 준 뒤 실측으로 닫는다
        #    (로봇 자체의 롤이 조금 있어서 개루프만으로는 안 맞는다).
        # 🔑 목표는 **검출값** `tgt_clock` 이다. 정답을 쓰지 않는다.
        set_torch(ring_deg=ring_cmd, extend_m=0.0)
        if t_state > 60:
            _, c_tip, _ = course.wall_uv(tip_world())
            err = (c_tip - tgt_clock + 180.0) % 360.0 - 180.0
            if abs(err) < 1.0 or t_state > 720:
                state, t_state = ("EXTEND" if NO_CREEP else "CREEP"), 0
                creep_hold = 0
                print(f"  [ALIGN] 링 {ring_cmd:.1f}° → 팁 시계각 {c_tip:.1f}° "
                      f"(검출 목표 {tgt_clock:.1f}°, 오차 {err:+.2f}°)  {now:.1f}초")
            else:
                ring_cmd += err * 0.5
                t_state = 0

    elif state == "CREEP":
        # 🚨 축방향 정렬은 **개루프로 세우면 반드시 빗나간다.** 실측(첫 통합
        #    실행): 링 s 가 결함 2.6mm 앞일 때 정지했는데, 휠 목표속도를 0 으로
        #    만든 뒤 로봇이 **4mm 뒤로 밀려** 최종 축오차가 −8.23mm 였다
        #    (허용 1.5mm 의 5.5배). 예압 216N 이 걸린 다리 12개가 자세를 다시
        #    잡으면서 생기는 이완이라 정지 위치를 앞으로 당겨도 재현되지 않는다.
        # → 팁 실측 위치로 **닫는다.** 실기에서도 이 되먹임은 카메라가 준다.
        # 🔑 겨누는 곳은 **검출 목표** `tgt_s` 다. 정답이 아니다.
        _, d_ax, _ = aim_error(tip_world(), tgt_s, tgt_clock)
        hold_station(d_ax)
        creep_hold = creep_hold + 1 if abs(d_ax) <= CREEP_TOL_MM else 0
        if creep_hold >= CREEP_HOLD_TICKS or t_state > 30 * PHYSICS_HZ:
            state, t_state = "EXTEND", 0
            print(f"  [CREEP] 축 정렬 — 오차 {d_ax:+.2f}mm "
                  f"(허용 ±{CREEP_TOL_MM}mm)  {now:.1f}초"
                  + ("  ⚠ 30초 상한으로 진행" if creep_hold < CREEP_HOLD_TICKS
                     else ""))

    elif state == "EXTEND":
        # 🚨 스테이션 키핑을 놓으면 안 된다 — 벨로우즈 복원력이 계속 민다.
        hold_station(aim_error(tip_world(), tgt_s, tgt_clock)[1])
        set_torch(extend_m=0.005)
        if t_state > 180:
            tp = tip_world()
            _, _, rr = course.wall_uv(tp)
            state, t_state = ("RETRACT" if NO_WELD else "ARC"), 0
            print(f"  [EXTEND] 팁 반경 {rr * 1000:.2f}mm — 관벽까지 간극 "
                  f"{50.0 - rr * 1000:.2f}mm  {now:.1f}초"
                  + ("  ⚠ --no-weld: 아크 생략, 결함을 그대로 둔다"
                     if NO_WELD else ""))

    elif state == "ARC":
        # 아크가 도는 2초 내내 자리를 지켜야 한다. SWAP 은 **끝난 시점의**
        # 팁 위치로 판정하므로, 여기서 놓으면 그동안 밀린 만큼 그대로 오차다.
        hold_station(aim_error(tip_world(), tgt_s, tgt_clock)[1])
        _arc_op.Set(Gf.Vec3d(*tip_world()))
        arc_light.GetIntensityAttr().Set(3.0e5)
        if t_state >= ARC_S * PHYSICS_HZ:
            arc_light.GetIntensityAttr().Set(0.0)
            if sparks is not None:
                sparks.clear()
            tp = tip_world()
            align_mm, d_ax, d_ci = dfc.align_error_mm(tp)
            ok = align_mm <= ALIGN_TOL_MM
            repaired = dfc.swap(tp, ok)
            swap_done = True
            result = {"align_mm": align_mm, "d_ax": d_ax, "d_ci": d_ci,
                      "ok": ok, "repaired": repaired}
            print(f"  [SWAP] 정렬 오차 {align_mm:.2f}mm "
                  f"(축 {d_ax:+.2f} / 원주 {d_ci:+.2f}) "
                  f"{'≤' if ok else '>'} 허용 {ALIGN_TOL_MM}mm → "
                  + ("✅ 결함 제거 + 마개 착좌"
                     if repaired else "❌ 수리 실패 — 결함 그대로, 비드만 남음"))
            state, t_state = "RETRACT", 0

    elif state == "RETRACT":
        hold_station(aim_error(tip_world(), tgt_s, tgt_clock)[1])
        set_torch(extend_m=0.0)
        if t_state > 180:
            if vis is not None and vis.ok:
                repos_from, _, _ = course.wall_uv(wpos(_ring_prim))
                state, t_state = "REPOSITION", 0
                drive(-SPIN_DEG_S)
                print(f"  [RETRACT] 토치 수납 — 검증 위해 "
                      f"{REPOSITION_MM:.0f}mm 후진  {now:.1f}초")
            else:
                state, t_state = "RUNOUT", 0
                drive(SPIN_DEG_S)
                print(f"  [RETRACT] 토치 수납 — 주행 재개  {now:.1f}초")

    elif state == "REPOSITION":
        # 🚨 후진하는 이유는 **카메라가 토치보다 33mm 앞**이기 때문이다. 용접
        #    자리는 제자리에서 어느 화소로도 안 보인다(vision.py 머리말 계산).
        s_ring, _, _ = course.wall_uv(wpos(_ring_prim))
        if (repos_from - s_ring) * 1000.0 >= REPOSITION_MM:
            drive(0.0)
            state, t_state = "VERIFY", 0

    elif state == "VERIFY":
        if t_state < 120:                 # 이완이 끝나기를 기다린다
            drive(0.0)
        else:
            rgb, dep = vis.frames()
            extra_steps += vis.warm_judge
            px = vis.project(dfc.world)
            print(f"  [VERIFY] 수리 후 촬영 — 카메라가 결함 "
                  f"{(dfc.s - course.wall_uv(wpos(_ring_prim))[0]) * 1000 - 33:.0f}mm "
                  f"뒤에서 봄"
                  + (f", 예상 화소 ({px[0]:.0f},{px[1]:.0f})" if px else
                     ", 🚨 화각 밖"))
            hole = bead = None
            if rgb is not None and px is not None:
                hole = vis.find_wall_hole(rgb, expect_px=px)
                bead = vis.find_weld_bead(rgb, expect_px=px)
                if hole is not None and not hole.get("matched", False):
                    hole = None
                if bead is not None and not bead.get("matched", False):
                    bead = None
                print(f"           구멍 "
                      + (f"**있음** {hole['area_px']:,}px "
                         f"(예상자리와 {hole['dist_px']:.0f}px)" if hole
                         else "없음 — 벽면이 이어져 있다")
                      + "   비드 "
                      + (f"있음 {bead['area_px']:,}px "
                         f"(예상자리와 {bead['dist_px']:.0f}px)" if bead
                         else "없음"))
            dv = dmsg = None
            if dep is not None and px is not None:
                dv, peak, dmsg = vis.wall_verdict(dep, px, WELD_K)
                print(f"           Depth 프로파일 — {dmsg}")
            if SHOTS and rgb is not None:
                OUT.mkdir(parents=True, exist_ok=True)
                print(f"           저장 → "
                      f"{vision.save_png(rgb, OUT / 'verify_front_rgb.png')}")
            verify = {"hole": hole, "bead": bead, "depth_ok": dv,
                      "depth_msg": dmsg}
            state, t_state = "RUNOUT", 0
            drive(SPIN_DEG_S)

    elif state == "RUNOUT":
        if s >= GOAL_S:
            reached = True
            print(f"  [완주] s={s * 1000:.1f}mm  {now:.1f}초")
            break

    if step % 240 == 0:
        rr = wheel_radii()
        print(f"  t={now:5.1f}초  s={s * 1000:7.1f}mm "
              f"({s / course.S_TOTAL * 100:5.1f}%)  "
              f"{'곡선' if course.in_bend(s) else '직선'}  "
              f"밀착 {int(np.sum(np.abs(rr - _seat) < 1.5)):2}/12  "
              f"벨로우즈 {bel_deg:4.1f}°  [{state}]")

    if step % 240 == 0 and state in ("DRIVE", "RUNOUT"):
        if s - s_prev < TARGET_SPEED_MPS * 0.20:
            stall += 1
            if stall >= 3:
                print(f"  🚨 [정지] s={s * 1000:.1f}mm 에서 3초째 진행 없음 "
                      f"({'곡선' if course.in_bend(s) else '직선'} 구간)")
                diagnose(s, mid, jp, bel_rot)
                break
        else:
            stall = 0
        s_prev = s

drive(0.0)
s_end, mid, rear, front = prog.read()

# ── 결과 ────────────────────────────────────────────────────────────
print("=" * 78)
print(f"[결과] 주행 {'✅ 완주' if reached else '❌ 미완주'}  "
      f"s {START_S * 1000:.0f} → {s_end * 1000:.1f}mm "
      f"(코스의 {s_end / course.S_TOTAL * 100:.1f}%)")
for k, lg in enumerate(bend_log):
    print(f"       굽힘 {k + 1}: "
          + (f"통과 {lg[0]:.1f}초, 벨로우즈 {lg[1]:.1f}°" if lg else "미도달"))
print(f"       벨로우즈 최대 사용각 {worst_bellows:.1f}° / {FLEX:.1f}° "
      + ("(여유 있음)" if worst_bellows < FLEX - 2 else "🚨 리밋에 붙었다"))
rr = wheel_radii()
print(f"       종료 시 휠 밀착 {int(np.sum(np.abs(rr - _seat) < 1.5))}/12")

if dfc is not None:
    print("-" * 78)
    if swap_done:
        print(f"[수리] {'✅ 성공' if result['repaired'] else '❌ 실패'}  "
              f"정렬 오차 {result['align_mm']:.2f}mm "
              f"(허용 {ALIGN_TOL_MM}mm) — 축 {result['d_ax']:+.2f}mm / "
              f"원주 {result['d_ci']:+.2f}mm")
        print(f"       결함 프림 {'숨김' if result['repaired'] else '**그대로 보임**'} / "
              f"비드 보임 / 마개 "
              f"{'착좌(충돌 켬)' if result['repaired'] else '대기(충돌 끔)'}")
        if not result["repaired"]:
            print("       🚨 비드는 토치가 실제로 있던 자리에 남았다 — "
                  "결함 자리가 아니다. 검증이 살아 있다는 뜻이다.")
    else:
        print("[수리] 미실시 — "
              + ("--no-weld 로 아크를 건너뛰었다 (검증층 시험용 대조군)"
                 if NO_WELD else "결함까지 도달하지 못했다"))

    # ── 검출 성능 (정답 대조는 **여기서 처음** 한다) ─────────────────
    print("-" * 78)
    if not VISION_ON:
        print("[검출] 카메라 없음 — 정답 좌표로 조준했다 (검출 성능 평가 불가)")
    elif tgt_s is None:
        print(f"[검출] ❌ 결함을 못 찾았다 — 관문 통과 {detect_log['n']}회, "
              f"확정 조건({SCAN_NEED}회 + 기선 "
              f"{SCAN_BASELINE_MM * 1000:.0f}mm + 기울기 ≤{SCAN_SLOPE_MAX}) 미달")
    else:
        print(f"[검출] ✅ 카메라로 찾음 — 첫 검출 s="
              f"{detect_log['first_s'] * 1000:.0f}mm "
              f"(결함까지 {(DEFECT_S - detect_log['first_s']) * 1000:.0f}mm 앞), "
              f"확정 전 검출 {detect_log['n']}회")
        print(f"       검출 목표 s={tgt_s * 1000:.1f}mm 시계각 {tgt_clock:.1f}°"
              f"  vs 정답 {DEFECT_S * 1000:.0f}mm / {DEFECT_CLOCK_DEG:.0f}°")
        _es = (tgt_s - DEFECT_S) * 1000
        _ec = (tgt_clock - DEFECT_CLOCK_DEG + 180) % 360 - 180
        print(f"       검출 오차 축 {_es:+.2f}mm / 시계 {_ec:+.2f}° "
              f"(= 원주 {course.PIPE_IR * math.radians(_ec) * 1000:+.2f}mm)")

    if VISION_ON:
        print(f"       덩어리 판정 내역 {vis.rej}")

    if verify:
        print("-" * 78)
        _h, _b = verify["hole"], verify["bead"]
        _expect_repaired = result.get("repaired", False)
        # 🚨 **두 겹은 서로 다른 조건에서 실패한다 — 어느 한쪽을 주 판정으로
        #    고정하면 안 된다.** 실측 두 건이 정반대였다:
        #
        #      --no-weld (불투명)  RGB "구멍 없음"      ❌ 놓침
        #                          Depth "파임 +3.69mm"  ✅ 잡음
        #      --glass (수리 실패) RGB "구멍 있음 4,509px" ✅ 잡음
        #                          Depth "메워짐 −1.66mm"  ❌ 놓침
        #
        #    RGB 가 놓치는 이유는 결함이 화면 아래 가장자리라 관 저 끝의 큰
        #    암부와 이어져 버리기 때문이고, Depth 가 놓치는 이유는 **비드 조각이
        #    그 자리 벽을 다시 채워** 깊이가 멀쩡한 벽면으로 읽히기 때문이다.
        #
        # → **비대칭 규칙**을 쓴다. "구멍이 보인다" 는 결정적 증거지만
        #   "안 보인다" 는 아니다(가려졌을 수도 있다).
        #      ① 예상 자리에 구멍이 보이면   → 미수리 (확정)
        #      ② 아니면 Depth 판정을 따른다
        #      ③ Depth 도 없으면 비드 유무로 본다
        if _h is not None:
            _cam_says, _src = False, "RGB(구멍 확인)"
        elif verify["depth_ok"] is not None:
            _cam_says, _src = verify["depth_ok"], "Depth"
        else:
            _cam_says, _src = (_b is not None), "RGB(비드만)"
        print(f"[검증] 수리 후 카메라 — 구멍 "
              + ("없음" if _h is None else f"있음 {_h['area_px']:,}px")
              + "  비드 " + ("있음" if _b is not None else "없음")
              + f"  Depth {verify['depth_msg'] or '판정 없음'}")
        print(f"       {_src} 판정 '{'수리됨' if _cam_says else '미수리'}' vs "
              f"물리 실제 '{'수리됨' if _expect_repaired else '미수리'}' → "
              + ("✅ 일치" if _cam_says == _expect_repaired
                 else "🚨 불일치"))
        if not _expect_repaired and _cam_says:
            print("       ⚠ 원인: **비드 조각이 관벽 한 구간을 통째로 다시 채운다.**"
                  "\n         비드 STL 은 44×47mm 벽 조각이라 어디에 놓이든 그 자리"
                  " 벽을 메운 것처럼 보인다.\n         정렬이 11.75mm 어긋나도 ø28"
                  " 구멍이 조각 안에 들어가 카메라·Depth 둘 다 가려진다."
                  "\n         → **시각 모델의 한계**다. 정렬 판정(위 [수리])이"
                  " 실패를 제대로 잡았으므로\n           수리 여부 자체는 틀리지"
                  " 않는다. 검증층만 이 경우를 못 가린다.")
    elif VISION_ON and swap_done:
        print("[검증] 미실시 — 후진·촬영 전에 스텝이 끝났다")
print("=" * 78)

if HOLD and not HEADLESS:
    print("[유지] 창을 닫을 때까지 유지한다 (Ctrl+C 로 종료)")
    try:
        while simulation_app.is_running():
            world.step(render=True)
    except KeyboardInterrupt:
        pass

simulation_app.close()
