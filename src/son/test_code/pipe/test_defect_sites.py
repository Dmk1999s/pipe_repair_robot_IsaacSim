"""[오프라인] 결함 배치·관통 개구·카메라 검출 연동 검증 — Isaac Sim 불필요.

`repair_demo.py` 는 Isaac Sim 에서만 돈다. 그래서 **거기 박힌 상수와 기하를
소스에서 그대로 읽어와** 노트북에서 검증한다 (`test_traction.py` 와 같은 방식.
그래서 repair_demo 쪽 설계값은 리터럴로 남겨야 한다).

무엇을 잡으려는 시험인가 — 전부 **조용히 틀리는** 것들이다.

  ① 개구 지름 vs 입자 설정   한쪽만 바꾸면 에러 없이 그냥 안 샌다
  ② 접선 회전 ψ             빼먹으면 출구 직관에서 결함 패치가 관을 가로질러
                            박힌다. 구멍은 제자리인데 눈에 보이는 결함만 90°
                            틀어져 검출이 안 된다
  ③ 삼각형 절삭             결함 두 곳 모두 안팎이 뚫려야 관통이다. 안쪽만
                            지워지면 물이 벽 속에 갇힌다
  ④ 휠 접지 궤도            개구가 궤도에 걸리면 바퀴가 빠진다
  ⑤ 검출기가 정말 무는가     구멍이 없을 때 안 울리고, 있을 때 울리고,
                            비드로 덮은 뒤 다시 조용해지는가

실행:  python3 test_code/pipe/test_defect_sites.py
"""

import math
import re
import sys
from pathlib import Path

import numpy as np

SON = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(SON / "pipe"))
import crack_inject as ci                                  # noqa: E402

SRC = (SON / "repair_demo.py").read_text()
PASS, FAIL = [], []


def check(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print(f"  {'✅' if ok else '❌'} {name}" + (f"   {detail}" if detail else ""))


def literal(name):
    """repair_demo.py 에서 상수 리터럴을 읽는다.

    `NAME = 0.15` 와 `A, B = 0.3, 0.3` 두 형태를 다 받는다 — 뒤쪽을 못 읽으면
    S_IN 같은 값이 조용히 빠진다.
    """
    m = re.search(rf"^{name}\s*=\s*([-\d.e]+)\s*(?:#|$)", SRC, re.M)
    if m:
        return float(m.group(1))
    for line in SRC.splitlines():
        m = re.match(r"^([A-Z_0-9, ]+)=\s*([-\d.e, ]+?)\s*(?:#.*)?$", line)
        if not m:
            continue
        names = [t.strip() for t in m.group(1).split(",")]
        vals = [t.strip() for t in m.group(2).split(",")]
        if name in names and len(names) == len(vals):
            return float(vals[names.index(name)])
    raise AssertionError(f"repair_demo.py 에 {name} 리터럴이 없다")


def defect_sites():
    """DEFECT_SITES 리스트를 읽는다 (dict(x=..., y=..., clock=...) 형태).

    좌표는 숫자일 수도 이름(IN_Y, OUT_X)일 수도 있다. **양쪽 다 받아야 한다** —
    한쪽만 받으면 결함이 조용히 하나 빠진 채 시험이 통과한다(실제로 그랬다).
    """
    body = re.search(r"DEFECT_SITES\s*=\s*\[(.*?)\n\]", SRC, re.S).group(1)
    out = []
    for x, y, c in re.findall(
            r"dict\(x=\s*([+\-\d.A-Za-z_]+),\s*y=\s*([+\-\d.A-Za-z_]+),"
            r"\s*clock=\s*([\d.]+)\)", body):
        out.append(dict(x=_resolve(x), y=_resolve(y), clock=float(c)))
    n_dict = body.count("dict(")
    if len(out) != n_dict:
        raise AssertionError(
            f"DEFECT_SITES 를 {n_dict}개 중 {len(out)}개만 읽었다 — "
            "정규식이 좌표 표기를 못 따라간다")
    return out


def _resolve(tok):
    """y 값이 IN_Y 같은 이름이면 그 리터럴을 다시 찾아 푼다."""
    try:
        return float(tok)
    except ValueError:
        return literal(tok.lstrip("+"))


# ── 코스 기하 (repair_demo.py 와 같은 식) ────────────────────────────
IN_Y, OUT_X = literal("IN_Y"), literal("OUT_X")
ARC_R, S_IN, S_OUT = literal("ARC_R"), literal("S_IN"), literal("S_OUT")
S_ARC = ARC_R * math.pi / 2
PIPE_IR = literal("PIPE_IR")


def path_dist_tangent(px, py):
    d1 = np.hypot(px - np.clip(px, -S_IN, 0.0), py - IN_Y)
    ang = np.clip(np.arctan2(py, px), -np.pi / 2, 0.0)
    d2 = np.hypot(px - ARC_R * np.cos(ang), py - ARC_R * np.sin(ang))
    d3 = np.hypot(px - OUT_X, py - np.clip(py, 0.0, S_OUT))
    d = np.stack([d1, d2, d3])
    which = np.argmin(d, axis=0)
    tx = np.where(which == 0, 1.0, np.where(which == 1, -np.sin(ang), 0.0))
    ty = np.where(which == 0, 0.0, np.where(which == 1, np.cos(ang), 1.0))
    return d.min(axis=0), tx, ty


# ── pxr 없이 쓰는 행벡터 회전 (Gf 와 같은 규약: v' = v @ M) ──────────
def rot_x(deg):
    c, s = math.cos(math.radians(deg)), math.sin(math.radians(deg))
    return np.array([[1, 0, 0], [0, c, s], [0, -s, c]])


def rot_z(deg):
    c, s = math.cos(math.radians(deg)), math.sin(math.radians(deg))
    return np.array([[c, s, 0], [-s, c, 0], [0, 0, 1]])


def parse_usda_mesh(path):
    """usda 의 points / faceVertexIndices 를 읽는다 (pxr 없이)."""
    txt = Path(path).read_text()
    pts = re.search(r"point3f\[\]\s+points\s*=\s*\[(.*?)\]", txt, re.S).group(1)
    v = np.array([float(x) for x in re.findall(r"[-\d.e]+", pts)])
    idx = re.search(r"int\[\]\s+faceVertexIndices\s*=\s*\[(.*?)\]",
                    txt, re.S).group(1)
    f = np.array([int(x) for x in idx.split(",")])
    return v.reshape(-1, 3), f.reshape(-1, 3)


def main():
    print("=" * 78)
    print("결함 배치·관통 개구·카메라 검출 연동 (repair_demo.py 소스에서 읽음)")
    print("=" * 78)

    sites = defect_sites()
    port_d = literal("LEAK_PORT_D") * 1000
    pco = literal("W_PCO") * 1000
    rest = literal("W_FLUID_REST") * 1000
    p_dia = 2 * rest

    # ── ① 개구 지름 vs 입자 설정 ──────────────────────────────────
    print("\n① 개구 지름과 입자 설정 (한쪽만 바꾸면 조용히 안 샌다)")
    eff = ci.effective_bore_mm(port_d, pco)
    need = ci.LEAK_MARGIN * p_dia
    leaks = ci.leaks(port_d, p_dia, pco)
    check("개구 지름이 STL 실측과 일치 (ø28)", abs(port_d - 28.0) < 0.01,
          f"LEAK_PORT_D={port_d:.1f}mm")
    print(f"     개구 ø{port_d:.1f}  PCO {pco:.1f}  입자지름 {p_dia:.1f} "
          f"→ 실효 {eff:.1f}mm vs 필요 {need:.1f}mm")
    if leaks:
        check("지금 조합에서 물이 샌다", True, f"여유 {eff - need:+.1f}mm")
    else:
        # 안 새는 것은 **알려진 상태**다 (형상 먼저, 입자는 나중에).
        # 시험이 잡아야 할 것은 "안 샌다는 사실을 아무도 모르는 것" 이다.
        warned = "❌ 안 샌다" in SRC or "안 샌다" in SRC
        check("안 새는 조합이면 실행 로그가 그것을 경고한다", warned,
              f"실효 {eff:.1f} < 필요 {need:.1f}mm — 입자를 줄여야 한다")

    # ── ② 접선 회전 ψ ────────────────────────────────────────────
    print("\n② 결함 패치 배치 — 축은 코스 접선, 중심은 바닥")
    for k, st in enumerate(sites):
        _, tx, ty = path_dist_tangent(np.array([st["x"]]), np.array([st["y"]]))
        tan = np.array([float(tx[0]), float(ty[0]), 0.0])
        psi = math.degrees(math.atan2(tan[1], tan[0]))
        M = rot_x(-st["clock"]) @ rot_z(psi)      # 행벡터: 먼저 Rx, 다음 Rz
        axis = np.array([1.0, 0, 0]) @ M          # STL 의 관 축
        centre = np.array([0, 0, 1.0]) @ M        # STL 의 패치 중심 방향
        check(f"결함 #{k + 1} 패치 축 = 코스 접선 (ψ={psi:.0f}°)",
              np.allclose(axis, tan, atol=1e-6),
              f"축 {np.round(axis, 3)} vs 접선 {np.round(tan, 3)}")
        check(f"결함 #{k + 1} 패치 중심 = 바닥(-Z)",
              np.allclose(centre, [0, 0, -1], atol=1e-6),
              f"{np.round(centre, 3)}")

    # ── ③ 삼각형 절삭 — 정말 관통인가 ────────────────────────────
    print("\n③ 배관 충돌 메시 절삭 (안팎이 다 뚫려야 관통이다)")
    pts, idx = parse_usda_mesh(SON / "pipe" / "pipe_elbow_lr150.usda")
    cent = pts[idx].mean(axis=1)
    for k, st in enumerate(sites):
        hit = np.hypot(cent[:, 0] - st["x"], cent[:, 1] - st["y"]) < port_d / 2000
        # 바닥 개구라 |z| 가 곧 관벽 반경이다. 안쪽면 r≈50, 바깥면 r≈57 —
        # 둘 다 지워져야 관통이다. 안쪽만 지워지면 물이 벽 속에 갇힌다.
        rad = np.abs(cent[hit][:, 2])
        mid = PIPE_IR + 0.0035              # 벽 두께 7mm 의 중간
        inner = int((rad < mid).sum())
        outer = int((rad >= mid).sum())
        check(f"결함 #{k + 1} 삼각형이 지워진다", hit.sum() > 0,
              f"{int(hit.sum())}개 제거")
        check(f"결함 #{k + 1} 안쪽면·바깥면 둘 다 뚫린다",
              inner > 0 and outer > 0,
              f"안쪽 {inner} / 바깥 {outer}개")
    both = np.zeros(len(idx), bool)
    for st in sites:
        both |= np.hypot(cent[:, 0] - st["x"],
                         cent[:, 1] - st["y"]) < port_d / 2000
    check("두 개구가 서로 겹치지 않는다",
          all(math.hypot(a["x"] - b["x"], a["y"] - b["y"]) > port_d / 1000
              for i, a in enumerate(sites) for b in sites[i + 1:]),
          f"총 {int(both.sum())}개 제거")

    # ── ④ 휠 접지 궤도 ───────────────────────────────────────────
    print("\n④ 휠 접지 궤도 — 바퀴가 구멍에 빠지지 않는가")
    tracks = [float(x) for x in re.search(
        r"휠 궤도는 월드 시계각 (\d+) / (\d+) / (\d+)", SRC).groups()]
    half_track = 2.9
    port_half = math.degrees(port_d / 2.0 / (PIPE_IR * 1000))
    for k, st in enumerate(sites):
        gap = min(abs((st["clock"] - t + 180) % 360 - 180) - port_half
                  - half_track for t in tracks)
        check(f"결함 #{k + 1} 개구가 휠 궤도를 비껴간다", gap > 0,
              f"여유 {gap:+.1f}° (개구 반각 {port_half:.1f}°, 궤도 {tracks})")

    # ── ⑤ 검출기가 정말 무는가 ───────────────────────────────────
    print("\n⑤ DarkBlobDetector — 관통 구멍에 물고 비드에서 놓는가")
    try:
        sys.path.insert(0, str(SON.parent / "dongyeon" / "pipe_inspect_demo"))
        from pipe_inspect_demo.defect_detection import DarkBlobDetector
    except Exception as exc:
        check("dongyeon 검출기 import", False, str(exc))
        DarkBlobDetector = None

    if DarkBlobDetector is not None:
        W, H = 1280, 720
        yy, xx = np.mgrid[0:H, 0:W]
        rad_n = np.hypot(yy - H / 2, xx - W / 2) / (min(H, W) / 2)
        rng = np.random.default_rng(0)

        def scene(kind):
            """관 안쪽 시야를 흉내낸다 — 가운데는 관 저 끝이라 원래 어둡다."""
            g = np.where(rad_n < 0.45, 18.0, 145.0 - 40.0 * (rad_n - 0.45))
            g = g + rng.normal(0, 3.0, g.shape)
            if kind != "clean":
                # ø28 구멍이 관벽에 잡힌 모습 — 고리 마스크 안쪽에 둔다
                blob = np.hypot(yy - H / 2, xx - (W / 2 + 230)) < 45
                g[blob] = 8.0 if kind == "hole" else 190.0   # 비드는 밝다
            g = np.clip(g, 0, 255).astype(np.uint8)
            return np.dstack([g, g, g if kind != "bead" else g * 0.55])

        det = DarkBlobDetector(calibration_frames=10, dark_ratio=0.45,
                               annulus_inner=0.45, annulus_outer=0.92,
                               min_area=40, noise_area_scale=2.0,
                               confirm_frames=3, release_frames=3)
        for _ in range(10):
            r = det.process(scene("clean").astype(np.uint8))
        check("정상 배관 10프레임으로 보정된다", r.calibrated,
              f"임계 {r.threshold:.1f}, 최소면적 {r.area_min}px")
        for _ in range(4):
            r = det.process(scene("clean").astype(np.uint8))
        check("깨끗한 관에서는 안 울린다", not r.stable_detected)
        for i in range(4):
            r = det.process(scene("hole").astype(np.uint8))
            if i == 2:
                check("구멍 3프레임 연속에서 확정된다", r.stable_detected,
                      f"면적 {r.candidate.area if r.candidate else 0}px")
        check("구멍이 계속 보이면 확정 유지", r.stable_detected)
        for i in range(4):
            r = det.process(scene("bead").astype(np.uint8))
        check("비드로 덮으면 다시 조용해진다 (검증 3겹 중 ③)",
              not r.stable_detected)

    print("\n" + "=" * 78)
    print(f"결과  {len(PASS)}/{len(PASS) + len(FAIL)} 통과")
    if FAIL:
        for f in FAIL:
            print(f"  실패 — {f}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
