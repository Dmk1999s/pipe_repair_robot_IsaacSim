"""[Isaac 3.11 / 순수 python] 지그재그 훅 R100 코스 기하 — **단일 출처**.

`test_pipe_zigzag_hook_R100.usda` 의 중심선을 해석적으로 기술한다. 주행 진행도,
결함 배치, 유체력 방향, 스파크 가둠이 전부 이 한 파일을 쓴다.

## 왜 새로 쓰나

`repair_demo.py` 의 `path_s`/`path_dist_tangent`/`path_point` 는 **직선-곡선-직선
3구간을 손으로 펼쳐 쓴 식**이다. 이 코스는 직선 4 + 곡선 3 = 7구간이라 그 방식
으로는 식이 감당이 안 된다. 그래서 구간을 **자료로 두고 일반 코드로** 푼다.

## 두 가지 코스 — `ZIGZAG_COURSE` 로 고른다

    long (기본)  5049.56mm  훅 7구간 + 연장 9구간 = 16구간, 굽힘 7개
    hook         1771.24mm  원래 훅만. 옛 실측·README 수치를 재현할 때

🔑 **의존 방향이 뒤집혔다 (2026-08-06).** 원래는 CATIA 변환본
   `test_pipe_zigzag_hook_R100.usda` 를 메시에서 역산해 이 파일을 썼다.
   지금은 반대다 — 여기 `_SEGS` 가 정본이고 배관 usda 를 `build_pipe.py` 가
   **여기서 생성한다.** 그래서 구간을 늘리면 관도 같이 늘어난다.
   `hook` 코스는 원본 usda 를 그대로 쓰므로 옛 실측과 계속 대조할 수 있다.

## 실측 근거 (원본 메시에서 역산, 오차 0.0000mm — hook 코스)

    정점 22,560 = 안쪽 링 235 + 바깥 링 235, 링당 48점
    내반경 50.000mm  외반경 56.000mm  벽두께 6.00mm
    중심선은 **z=0 평면**에 있다 (upAxis=Z 인데 굽힘은 수평면 XY 에서 일어난다)
    중심선 총길이 1771.24mm = 직선 1300 + 호 471.24 (= 3 × ¼원 × R100)

    구간   종류  시작(mm)        끝(mm)          길이mm   비고
      0   직선  (   0,   0)  → ( 350,   0)     350.00   +X 진행
      1   곡선  중심( 350, 100) R=100  −90°→0°  157.08   좌회전 +90°
      2   직선  ( 450, 100)  → ( 450, 400)     300.00   +Y 진행
      3   곡선  중심( 550, 400) R=100  180°→90° 157.08   우회전 −90°
      4   직선  ( 550, 500)  → ( 850, 500)     300.00   +X 진행
      5   곡선  중심( 850, 400) R=100   90°→0°  157.08   우회전 −90°
      6   직선  ( 950, 400)  → ( 950,  50)     350.00   −Y 진행 (훅)

## 연장 구간 (2026-08-06 추가 — long 코스에서만)

훅 끝 (950, 50) 에서 −Y 로 이어 받아 굽힘 4개를 더 돈다. 곡률은 전부 R100 으로
같게 두었다 — 로봇 주파 한계(벨로우즈)가 이미 R100 에 맞춰 검증돼 있어서
반경을 섞으면 어디서 막혔는지 못 가린다.

    구간   종류  시작(mm)         끝(mm)           길이mm   비고
      7   직선  ( 950,   50) → ( 950, -250)      300.00   −Y 진행
      8   곡선  중심( 850,-250) R=100    0°→−90°  157.08   우회전 −90°
      9   직선  ( 850, -350) → ( 250, -350)      600.00   −X 진행
     10   곡선  중심( 250,-450) R=100   90°→180°  157.08   좌회전 +90°
     11   직선  ( 150, -450) → ( 150, -900)      450.00   −Y 진행
     12   곡선  중심( 250,-900) R=100  180°→270°  157.08   좌회전 +90°
     13   직선  ( 250,-1000) → (1000,-1000)      750.00   +X 진행
     14   곡선  중심(1000,-900) R=100  −90°→  0°  157.08   좌회전 +90°
     15   직선  (1100, -900) → (1100, -350)      550.00   +Y 진행 (훅)

    연장 3278.32mm = 직선 2650 + 호 628.32 (= 4 × ¼원 × R100)
    합계 5049.56mm

🚨 **기존 구간 0~6 은 한 좌표도 안 건드렸다.** 결함 기본 위치 s=1600mm 과
   README 의 주파 실측(굽힘 3곳)이 그대로 성립해야 하기 때문이다. 연장은
   전부 s>1771.24mm 뒤에 붙는다.

🔑 자기간섭 여유 — 중심선끼리 최소 141mm 떨어져 있다(외반경 56×2 = 112mm 필요).
   가장 가까운 곳은 구간 9(y=−350)와 구간 11(x=150)의 모서리인데 그 둘은
   굽힘 10 으로 이어진 안쪽 모서리라 원리적으로 안 겹친다. 그 다음이
   구간 15(x=1100)와 구간 7(x=950)의 150mm 다 — y 범위가 안 겹친다.

🚨 **R=100 은 LR150 곡관보다 훨씬 타이트하다.** R/D 가 1.5 → 1.0 이다.
   로봇 강체 몸통이 64mm 라 굽힘 하나에서 벨로우즈가 약 64° 를 접어야 하고,
   가용량은 4관절 × ±20° = 80° 다. 여유 16° — 설계상 통과하지만 좁다.
   (실측은 ±20° 로 첫 굽힘에서 정지 — `scene.relax_bellows()` 가 ±30° 로 푼다.)

## 좌표 규약

  s      중심선 진행거리(m). 관 입구 (0, 0) 이 s=0, 훅 끝이 s=1.77124
  d      중심선까지의 거리(m). 관 내벽이면 0.050
  시계각 중심선 점에서 **+Z(위) 에서 진행방향 왼쪽으로** 잰 각(deg).
         0°=천장, 180°=바닥. `repair_demo.py` 규약("+Z 에서 +Y 로")을 굽힘까지
         일반화한 것이다 — 진행이 +X 일 때 왼쪽이 +Y 라 그 자리에서 같다.
"""

import math
import os
from collections import namedtuple

import numpy as np

PIPE_IR = 0.050          # 내반경
PIPE_OR = 0.056          # 외반경
WALL = PIPE_OR - PIPE_IR
BEND_R = 0.100           # 굽힘 반경 (파일명 R100)

# ── 분기(T) 규격 ────────────────────────────────────────────────────
# 🚨 **직각 T 는 로봇이 못 지난다 — 곡률 반경이 0 이다.** README 실측이 근거다:
#    R100(완만한 90°) 조차 본체 중심간 124mm 에 대해 71° 를 요구해서 출고
#    ±20° 로는 못 지나고 ±25° 가 임계다. 직각 분기는 ø100 보어 안에서 64mm
#    강체가 코너를 도는 것 자체가 기하적으로 불가능하다 — 제어 문제가 아니다.
#
# → **45° 측면 분기(lateral) + R100 아크로 수직 복귀** 로 만든다. 실제 배관의
#   스윕 티/Y피스이고, 밖에서 보면 T 이며, 안에서는 크로치가 길어 R100 굽힘보다
#   오히려 완만하다. 아래 각을 90 으로 두면 날카로운 T 가 되고 — 그건 못 지나는
#   것을 **실측으로 보이기 위한** 대조군이다.
TEE_LATERAL_DEG = float(os.environ.get("ZIGZAG_TEE_ANGLE", 45.0))
TEE_RUN_M = 0.200        # 이탈 직후 직진 — 크로치가 끝날 때까지 (아래 검산)
TEE_ARC_R = BEND_R       # 수직 복귀 아크 반경. R100 로 통일한다
TEE_STUB_M = 0.250       # 수직이 된 뒤의 가지 길이

# 🔑 크로치(두 관이 겹쳐 있는 구간) 길이 — 중심선 간격이 2·외반경 에 이를 때까지다.
#    `TEE_RUN_M` 이 이보다 짧으면 아크가 크로치 안에서 시작해 개구가 찢어진다.
TEE_CROTCH_M = 2.0 * PIPE_OR / math.sin(math.radians(TEE_LATERAL_DEG))
if TEE_RUN_M < TEE_CROTCH_M:
    raise SystemExit(
        f"[중단] 분기 이탈 직진 {TEE_RUN_M * 1000:.0f}mm 가 크로치 "
        f"{TEE_CROTCH_M * 1000:.0f}mm 보다 짧다 (이탈각 {TEE_LATERAL_DEG:.0f}°). "
        f"아크가 겹침 구간 안에서 시작해 개구가 찢어진다.")

# ── 구간 자료 ────────────────────────────────────────────────────────
# 직선: ("S", 시작점, 끝점)
# 곡선: ("A", 중심, R, 시작각deg, 끝각deg)   각은 중심에서 본 방위각, 부호가 회전 방향
_SEGS_HOOK = [
    ("S", (0.000, 0.000), (0.350, 0.000)),
    ("A", (0.350, 0.100), BEND_R, -90.0, 0.0),
    ("S", (0.450, 0.100), (0.450, 0.400)),
    ("A", (0.550, 0.400), BEND_R, 180.0, 90.0),
    ("S", (0.550, 0.500), (0.850, 0.500)),
    ("A", (0.850, 0.400), BEND_R, 90.0, 0.0),
    ("S", (0.950, 0.400), (0.950, 0.050)),
]

# 연장 — 훅 끝 (950, 50) 에서 −Y 로 이어 받는다. 위 머리말의 표와 같은 순서다.
_SEGS_EXT = [
    ("S", (0.950, 0.050), (0.950, -0.250)),
    ("A", (0.850, -0.250), BEND_R, 0.0, -90.0),
    ("S", (0.850, -0.350), (0.250, -0.350)),
    ("A", (0.250, -0.450), BEND_R, 90.0, 180.0),
    ("S", (0.150, -0.450), (0.150, -0.900)),
    ("A", (0.250, -0.900), BEND_R, 180.0, 270.0),
    ("S", (0.250, -1.000), (1.000, -1.000)),
    ("A", (1.000, -0.900), BEND_R, -90.0, 0.0),
    ("S", (1.100, -0.900), (1.100, -0.350)),
]

def _seg_len(sg):
    if sg[0] == "S":
        a, b = np.array(sg[1]), np.array(sg[2])
        return float(np.linalg.norm(b - a))
    return sg[2] * math.radians(abs(sg[4] - sg[3]))


def _prefix(segs):
    """구간 목록 → 구간 시작 s 누적. 망을 조립하기 전에도 쓴다."""
    out = [0.0]
    for sg in segs:
        out.append(out[-1] + _seg_len(sg))
    return out


def _point_at_segs(segs, S0, s):
    """`point_at` 의 일반판 — 아직 전역 `_SEGS` 가 없을 때 부모 코스에 쓴다."""
    s = float(np.clip(s, 0.0, S0[-1]))
    for sg, a, b in zip(segs, S0[:-1], S0[1:]):
        if s <= b or sg is segs[-1]:
            t = s - a
            if sg[0] == "S":
                p0, p1 = np.array(sg[1]), np.array(sg[2])
                u = (p1 - p0) / np.linalg.norm(p1 - p0)
                p = p0 + t * u
                return float(p[0]), float(p[1]), float(u[0]), float(u[1])
            (cx0, cy0), R, a0, a1 = sg[1], sg[2], sg[3], sg[4]
            sweep = math.radians(a1 - a0)
            th = math.radians(a0) + (t / R) * np.sign(sweep)
            return (cx0 + R * math.cos(th), cy0 + R * math.sin(th),
                    -math.sin(th) * float(np.sign(sweep)),
                    math.cos(th) * float(np.sign(sweep)))
    raise AssertionError("도달 불가")


def _branch_segs(px, py, tx, ty, side, *, lateral_deg=TEE_LATERAL_DEG,
                 run_m=TEE_RUN_M, arc_r=TEE_ARC_R, stub_m=TEE_STUB_M):
    """부모 중심선 위 점 (px,py)/접선 (tx,ty) 에서 갈라지는 가지의 구간 목록.

    side  +1 진행방향 **왼쪽** / −1 **오른쪽**

    🔑 가지의 첫 점이 부모 중심선 **위**다. 두 중심선이 한 점에서 만나고 접선만
       `lateral_deg` 만큼 꺾인다 — 철도 분기기와 같은 배치다. 그래서 두 관이
       크로치에서 자연스럽게 합쳐지고, `build_pipe` 의 합집합 절단이 유한한
       각도로 교차해 수치적으로 안정된다. (탄젠트로 붙이면 두 면이 겹쳐
       절단면이 퇴화한다.)

    이탈 → `run_m` 직진 → `90−lateral_deg` 아크 → 부모에 **수직**으로 `stub_m`.
    그래서 밖에서 보면 T 이고 안에서는 굽힘이 R100 하나뿐이다.
    """
    yaw0 = math.atan2(ty, tx)
    d1 = yaw0 + side * math.radians(lateral_deg)
    p1 = (px + math.cos(d1) * run_m, py + math.sin(d1) * run_m)
    # 아크 중심은 도는 쪽 법선 위 — side>0 이면 진행방향 왼쪽
    nx, ny = -math.sin(d1) * side, math.cos(d1) * side
    c = (p1[0] + nx * arc_r, p1[1] + ny * arc_r)
    a0 = math.degrees(math.atan2(p1[1] - c[1], p1[0] - c[0]))
    a1 = a0 + side * (90.0 - lateral_deg)
    p2 = (c[0] + arc_r * math.cos(math.radians(a1)),
          c[1] + arc_r * math.sin(math.radians(a1)))
    d2 = yaw0 + side * math.radians(90.0)      # 설계상 부모에 수직
    p3 = (p2[0] + math.cos(d2) * stub_m, p2[1] + math.sin(d2) * stub_m)

    segs = [("S", (px, py), p1)]
    if abs(a1 - a0) > 1e-9:
        segs.append(("A", c, arc_r, a0, a1))
    segs.append(("S", p2, p3))
    return segs


# ── 코스 선택 ────────────────────────────────────────────────────────
# 🔑 배관 usda 도 이 선택을 따라간다 — scene.py / probe_robot.py 가 여기서 읽는다.
#    long 쪽 파일은 `build_pipe.py` 가 이 `_SEGS` 에서 생성한 것이다.
#
# 🚨 **long 과 hook 은 한 좌표도 안 건드렸다.** 분기는 새 코스 두 개로만 들어간다.
#    기존 실측(굽힘 3곳 주파, 결함 s=1600mm)이 그대로 성립해야 하기 때문이다.
_MAIN_OF = {
    "hook": lambda: list(_SEGS_HOOK),
    "long": lambda: _SEGS_HOOK + _SEGS_EXT,
    # 분기 기하만 떼어 보는 코스 — 본관은 직선 하나뿐이라 굽힘이 변수로 안 낀다
    "tee": lambda: [("S", (0.0, 0.0), (1.2, 0.0))],
    "longtee": lambda: _SEGS_HOOK + _SEGS_EXT,
}
# (본관 구간번호, 그 구간 안 offset m, 기본 side)
# 🔑 longtee 의 자리는 구간 13 (250,−1000)→(1000,−1000) 의 350mm 지점이고
#    **오른쪽(−Y)** 이다. 거기만 아래가 비어 있다 — 왼쪽으로 내면 구간 2(x=450)
#    와 겹친다. 겹치면 `test_course.py` 의 자기간섭 검사가 잡는다.
_TEE_SPEC = {
    "tee": [(0, 0.500, +1)],
    "longtee": [(13, 0.350, -1)],
}
_USDA_OF = {
    "hook": "test_pipe_zigzag_hook_R100.usda",
    "long": "test_pipe_zigzag_long_R100.usda",
    "tee": "test_pipe_zigzag_tee_R100.usda",
    "longtee": "test_pipe_zigzag_longtee_R100.usda",
}

COURSE = os.environ.get("ZIGZAG_COURSE", "long").lower()
if COURSE not in _MAIN_OF:
    raise SystemExit(f"[중단] ZIGZAG_COURSE 는 {'|'.join(_MAIN_OF)} 인데 "
                     f"{COURSE!r} 이다")
PIPE_USDA_NAME = _USDA_OF[COURSE]

_SIDE_ENV = os.environ.get("ZIGZAG_TEE_SIDE")
if _SIDE_ENV is not None and _SIDE_ENV.lower() not in ("left", "right"):
    raise SystemExit(f"[중단] ZIGZAG_TEE_SIDE 는 left|right 인데 {_SIDE_ENV!r} 이다")
_SIDE_OVERRIDE = ({"left": +1, "right": -1}[_SIDE_ENV.lower()]
                  if _SIDE_ENV else None)

# ── 분기망 조립 ──────────────────────────────────────────────────────
# 🔑 **가지를 s 축에 이어 붙인다.** 본관이 [0, S_MAIN], 가지 k 가 그 뒤 구간을
#    통째로 차지한다. 그래서 `_SEGS` 는 여전히 평평한 목록이고
#    `project`·`point_at`·`wall_uv` 가 **서명도 구현도 그대로** 성립한다.
#    분기 때문에 고쳐야 하는 것은 "어느 순서로 달릴 것인가"(`legs()`) 뿐이다.
Branch = namedtuple("Branch", "name i0 i1 s0 s1 parent at_s side")
Junction = namedtuple("Junction", "parent at_s child child_s0 side span")
Leg = namedtuple("Leg", "s0 s1 branch")

_main = _MAIN_OF[COURSE]()
_S0_main = _prefix(_main)

_SEGS = list(_main)
BRANCHES = [Branch("main", 0, len(_main), 0.0, _S0_main[-1], None, None, 0)]
JUNCTIONS = []
for _k, (_si, _off, _side_def) in enumerate(_TEE_SPEC.get(COURSE, [])):
    _side = _SIDE_OVERRIDE if _SIDE_OVERRIDE is not None else _side_def
    _at = _S0_main[_si] + _off
    _bs = _branch_segs(*_point_at_segs(_main, _S0_main, _at), _side)
    _s0 = _prefix(_SEGS)[-1]
    _s1 = _s0 + sum(_seg_len(sg) for sg in _bs)
    BRANCHES.append(Branch(f"tee{_k}", len(_SEGS), len(_SEGS) + len(_bs),
                           _s0, _s1, 0, _at, _side))
    # 기하가 애매한 s 반경 — 크로치 안에서는 어느 관의 벽인지 정의가 안 된다
    JUNCTIONS.append(Junction(0, _at, _k + 1, _s0, _side, TEE_CROTCH_M + 0.05))
    _SEGS += _bs

_S0 = _prefix(_SEGS)
S_TOTAL = _S0[-1]
S_MAIN = BRANCHES[0].s1                 # 본관만의 길이 (진행률 표시용)
N_BRANCH = len(BRANCHES)
HAS_BRANCH = N_BRANCH > 1

# 🚨 가지가 시작하는 구간 번호 — 여기서는 중심선이 **일부러** 꺾인다(이탈각).
#    `build_pipe._check_continuity` 가 이 경계를 건너뛰어야 한다.
SEG_BRANCH_START = {b.i0 for b in BRANCHES[1:]}

# 자유단 — (s, 바깥을 향하는 부호). 물 마개·끝 처리가 여기서 읽는다.
# 🚨 `S_TOTAL` 하나만 막으면 안 된다. 가지가 생긴 뒤로 S_TOTAL 은 **마지막
#    가지의 끝**이라 본관 출구가 열린 채로 남는다.
OPEN_ENDS = ([(0.0, -1.0), (S_MAIN, +1.0)]
             + [(b.s1, +1.0) for b in BRANCHES[1:]])

# 구간 경계 s (진단·로그용)
SEG_START_S = _S0[:-1]
SEG_KIND = [sg[0] for sg in _SEGS]
# 곡선 구간의 s 범위 — "지금 굽힘 안인가" 판정에 쓴다
BEND_SPANS = [(_S0[i], _S0[i + 1]) for i, sg in enumerate(_SEGS) if sg[0] == "A"]


def branch_at(s):
    """s → 가지 번호 (0 = 본관)."""
    for b in BRANCHES:
        if b.s0 <= s <= b.s1:
            return BRANCHES.index(b)
    return 0


def in_junction(s):
    """s 가 분기 크로치 안인가 — **그 안에서는 (s, 시계각) 이 애매하다.**

    두 관이 겹친 구간이라 벽 위 한 점이 본관에도 가지에도 속한다. `project` 의
    argmin 이 둘 중 하나를 고르는데 그 선택이 s 를 크게 튀게 한다. 결함을 여기
    두거나 여기서 검출 좌표를 믿으면 안 된다.
    """
    for j in JUNCTIONS:
        if abs(s - j.at_s) < j.span:                       # 부모 쪽
            return True
        if 0.0 <= s - j.child_s0 < j.span:                 # 가지 쪽
            return True
    return False


def legs():
    """전지점 주파 계획 — 가지마다 들어갔다 **후진으로** 나온다.

    반환: `Leg(s0, s1, 가지번호)` 목록. `s1 < s0` 이면 후진 구간이다. 이어지는
    두 다리 사이에서 월드 위치는 연속이다(분기점이 두 중심선의 공통점이라).
    바뀌는 것은 접선뿐이고, 그 각이 곧 로봇이 꺾어야 하는 조향각이다.

    🚨 가지에서 또 갈라지는 경우는 안 다룬다. 지금 코스에는 없고, 생기면
       여기서 재귀로 풀어야 한다.
    """
    out, cur = [], 0.0
    for j in sorted(JUNCTIONS, key=lambda x: x.at_s):
        b = BRANCHES[j.child]
        out.append(Leg(cur, j.at_s, 0))
        out.append(Leg(b.s0, b.s1, j.child))       # 진입
        out.append(Leg(b.s1, b.s0, j.child))       # 후진 복귀
        cur = j.at_s
    out.append(Leg(cur, S_MAIN, 0))
    return [lg for lg in out if abs(lg.s1 - lg.s0) > 1e-9]


def is_reverse(leg):
    """이 다리를 **후진**으로 지나는가 (가지에서 빠져나올 때)."""
    return leg.s1 < leg.s0


def heading_deg(s, branch=None):
    """s 에서 관 축의 방위각(deg) — 항상 **+s 방향**이다.

    🚨 후진한다고 이 값이 뒤집히지 않는다. 로봇이 가지에서 후진으로 나올 때
       몸통은 여전히 가지 쪽을 향하고 있다 — 뒤집어 재면 분기점의 조향각이
       180° 어긋나 로봇을 반대로 꺾는다.

    🚨 분기점에서는 s 하나가 본관 끝이자 가지 시작이라 답이 둘이다. `branch`
       를 주면 그 가지 **안쪽으로** 살짝 들어가서 잰다.
    """
    if branch is not None:
        b = BRANCHES[branch]
        eps = 1e-6
        s = min(max(s, b.s0 + eps), b.s1 - eps) if b.s1 - b.s0 > 2 * eps else s
    _, _, tx, ty = point_at(s)
    return math.degrees(math.atan2(ty, tx))


def steer_deg(leg_from, leg_to):
    """두 다리 사이에서 로봇이 꺾어야 하는 **몸통 방위각 변화**(deg). 왼쪽이 +.

    가지 진입은 `+lateral`, 복귀는 `−lateral` 이 나온다. 방향 전환(전진↔후진)
    자체는 0° 다 — 휠만 거꾸로 돌리면 되고 몸통은 안 꺾는다.
    """
    d = (heading_deg(leg_to.s0, leg_to.branch)
         - heading_deg(leg_from.s1, leg_from.branch))
    return (d + 180.0) % 360.0 - 180.0


def _project_seg(sg, s0, px, py):
    """한 구간에 대한 (거리, s, 접선x, 접선y, 중심선x, 중심선y). 전부 벡터."""
    if sg[0] == "S":
        a = np.array(sg[1])
        b = np.array(sg[2])
        u = b - a
        L = float(np.linalg.norm(u))
        u = u / L
        t = np.clip((px - a[0]) * u[0] + (py - a[1]) * u[1], 0.0, L)
        cx, cy = a[0] + t * u[0], a[1] + t * u[1]
        return (np.hypot(px - cx, py - cy), s0 + t,
                np.full_like(px, u[0]), np.full_like(px, u[1]), cx, cy)

    (cx0, cy0), R, a0, a1 = sg[1], sg[2], sg[3], sg[4]
    sweep = math.radians(a1 - a0)          # 부호 있는 회전량
    ang = np.arctan2(py - cy0, px - cx0)
    # a0 기준 회전 방향으로 편 각도 (0 ~ |sweep|)
    da = (ang - math.radians(a0)) * np.sign(sweep)
    da = np.mod(da, 2 * math.pi)
    da = np.clip(da, 0.0, abs(sweep))
    th = math.radians(a0) + da * np.sign(sweep)
    cx, cy = cx0 + R * np.cos(th), cy0 + R * np.sin(th)
    # 접선 = 진행 방향. 반시계(sweep>0)면 (-sinθ, cosθ)
    tx, ty = -np.sin(th) * np.sign(sweep), np.cos(th) * np.sign(sweep)
    return np.hypot(px - cx, py - cy), s0 + R * da, tx, ty, cx, cy


def project(px, py):
    """xy 점 → (s, d, tx, ty, cx, cy). 스칼라도 배열도 받는다.

    s  진행거리(m)          d  중심선까지 거리(m)
    tx,ty 진행 방향 단위벡터  cx,cy 가장 가까운 중심선 점
    """
    scalar = np.isscalar(px)
    px = np.atleast_1d(np.asarray(px, float))
    py = np.atleast_1d(np.asarray(py, float))
    res = [_project_seg(sg, s0, px, py) for sg, s0 in zip(_SEGS, _S0[:-1])]
    d = np.stack([r[0] for r in res])
    w = np.argmin(d, axis=0)
    i = np.arange(px.size)
    # 🚨 `_project_seg` 는 (거리, s, ...) 순으로 준다 — argmin 을 거리로 하려면
    #    그 순서가 편하다. 하지만 **이 함수의 계약은 (s, 거리, ...)** 다.
    #    여기서 뒤집지 않으면 호출부가 전부 조용히 뒤바뀐 값을 쓴다.
    pick = [np.stack([r[k] for r in res])[w, i] for k in range(6)]
    out = (pick[1], pick[0], pick[2], pick[3], pick[4], pick[5])
    return tuple(float(v[0]) for v in out) if scalar else out


def project_branch(branch, px, py):
    """`project` 를 **한 가지 안에서만** 한다. 반환 규약은 `project` 와 같다.

    전역 `project` 는 분기점 근처에서 본관과 가지가 경쟁해 argmin 이 튄다.
    합집합 절단과 감김 검산은 "이 가지 기준으로" 재야 하므로 따로 둔다.
    """
    b = BRANCHES[branch]
    px = np.atleast_1d(np.asarray(px, float))
    py = np.atleast_1d(np.asarray(py, float))
    res = [_project_seg(sg, s0, px, py)
           for sg, s0 in zip(_SEGS[b.i0:b.i1], _S0[b.i0:b.i1])]
    d = np.stack([r[0] for r in res])
    w = np.argmin(d, axis=0)
    i = np.arange(px.size)
    pick = [np.stack([r[k] for r in res])[w, i] for k in range(6)]
    return (pick[1], pick[0], pick[2], pick[3], pick[4], pick[5])


def radius_to(branch, pts):
    """(N,3) 점 → 그 가지 중심선까지의 **3차원** 반경(m).

    중심선이 z=0 평면에 있으므로 `hypot(평면거리, z)` 다. 합집합 절단의 판정식
    이 전부 이 값으로 쓰인다 — 안쪽 껍질은 내반경, 바깥 껍질·마개는 외반경과
    견준다.
    """
    pts = np.asarray(pts, float)
    _, d, _, _, _, _ = project_branch(branch, pts[:, 0], pts[:, 1])
    return np.hypot(d, pts[:, 2])


def point_at(s):
    """진행거리 s(m) → (x, y, tx, ty). 코스 밖이면 끝점으로 물린다.

    🔑 가지도 같은 s 축에 얹혀 있어서 분기망에서도 이 함수 하나로 끝난다.
       다만 s 를 **연속으로 늘리면** 본관 끝에서 가지 시작으로 순간이동한다 —
       주행은 `legs()` 가 준 구간 안에서만 s 를 움직여야 한다.
    """
    return _point_at_segs(_SEGS, _S0, s)


def wall_uv(p):
    """월드 점 → (s, 시계각deg, 반경m). 정렬 오차는 **이 좌표에서** 재야 한다.

    🚨 3차원 직선거리로 정렬 오차를 재면 안 된다 — 용접 간극 2mm 가 그대로
       오차로 잡힌다(`repair_demo.py` 가 같은 함정을 주석으로 남겼다).
       "토치가 결함을 겨누고 있는가" 는 **관벽을 펼친 평면에서의 어긋남**이다.
    """
    px, py, pz = float(p[0]), float(p[1]), float(p[2])
    s, _, tx, ty, cx, cy = project(px, py)
    # 진행 방향 왼쪽 = e_z × t  (e_z = 월드 +Z)
    lx, ly = -ty, tx
    vx, vy, vz = px - cx, py - cy, pz
    left = vx * lx + vy * ly
    up = vz
    return s, math.degrees(math.atan2(left, up)) % 360.0, math.hypot(left, up)


def wall_uv_many(pts):
    """`wall_uv` 의 벡터판. pts (N,3) → (s, 시계각deg, 반경m) 각각 (N,).

    배관 삼각형 45,120개를 하나씩 돌리면 파이썬 루프가 수십 초 걸린다.
    개구를 뚫을 때 쓴다.
    """
    pts = np.asarray(pts, float)
    s, _, tx, ty, cx, cy = project(pts[:, 0], pts[:, 1])
    lx, ly = -ty, tx
    vx, vy, vz = pts[:, 0] - cx, pts[:, 1] - cy, pts[:, 2]
    left = vx * lx + vy * ly
    up = vz
    return s, np.degrees(np.arctan2(left, up)) % 360.0, np.hypot(left, up)


def wall_point(s, clock_deg, r=PIPE_IR):
    """(진행거리, 시계각, 반경) → 월드 점. `wall_uv` 의 역함수."""
    x, y, tx, ty = point_at(s)
    lx, ly = -ty, tx
    th = math.radians(clock_deg)
    return np.array([x + lx * r * math.sin(th),
                     y + ly * r * math.sin(th),
                     r * math.cos(th)])


def frame_at(s):
    """진행거리 s → (원점, 접선, 왼쪽, 위) 4개 벡터. 로봇 배치·카메라용."""
    x, y, tx, ty = point_at(s)
    return (np.array([x, y, 0.0]), np.array([tx, ty, 0.0]),
            np.array([-ty, tx, 0.0]), np.array([0.0, 0.0, 1.0]))


def in_bend(s):
    """s 가 굽힘 구간 안인가. 주행 로그에서 '지금 곡선' 을 찍는 데 쓴다."""
    return any(a <= s <= b for a, b in BEND_SPANS)


def describe():
    _n_bend = sum(1 for sg in _SEGS if sg[0] == "A")
    lines = [f"지그재그 R{BEND_R * 1000:.0f} [{COURSE}] — 중심선 "
             f"{S_TOTAL * 1000:.2f}mm, 구간 {len(_SEGS)}개(굽힘 {_n_bend}), "
             f"내반경 {PIPE_IR * 1000:.0f}mm, 벽 {WALL * 1000:.0f}mm",
             f"  배관 {PIPE_USDA_NAME}"]
    if HAS_BRANCH:
        lines.append(f"  본관 {S_MAIN * 1000:.2f}mm + 가지 {N_BRANCH - 1}개 "
                     f"(이탈각 {TEE_LATERAL_DEG:.0f}°, 크로치 "
                     f"{TEE_CROTCH_M * 1000:.0f}mm)")
        for j in JUNCTIONS:
            b = BRANCHES[j.child]
            x, y, _, _ = point_at(j.at_s)
            lines.append(
                f"    분기 {b.name}: 본관 s={j.at_s * 1000:.1f}mm "
                f"({x * 1000:.0f},{y * 1000:.0f}) 에서 "
                f"{'왼쪽' if j.side > 0 else '오른쪽'}으로 — "
                f"가지 s {b.s0 * 1000:.1f}~{b.s1 * 1000:.1f}mm "
                f"(길이 {(b.s1 - b.s0) * 1000:.1f}mm)")
    for k, (sg, s0, s1) in enumerate(zip(_SEGS, _S0[:-1], _S0[1:])):
        if sg[0] == "S":
            lines.append(f"  [{k}] 직선 s {s0 * 1000:7.1f}~{s1 * 1000:7.1f}mm  "
                         f"({sg[1][0] * 1000:.0f},{sg[1][1] * 1000:.0f}) → "
                         f"({sg[2][0] * 1000:.0f},{sg[2][1] * 1000:.0f})")
        else:
            lines.append(f"  [{k}] 곡선 s {s0 * 1000:7.1f}~{s1 * 1000:7.1f}mm  "
                         f"중심({sg[1][0] * 1000:.0f},{sg[1][1] * 1000:.0f}) "
                         f"R={sg[2] * 1000:.0f} {sg[3]:+.0f}°→{sg[4]:+.0f}° "
                         f"({'좌' if sg[4] > sg[3] else '우'}회전)")
    return "\n".join(lines)


if __name__ == "__main__":
    print(describe())
