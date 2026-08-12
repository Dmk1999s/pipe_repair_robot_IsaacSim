"""[자산생성] 지그재그 배관용 결함/비드 STL — **벽 두께만 다르다.**

`wall_patch.py` 의 `hole_patch()` 를 그대로 쓴다. 다른 것은
바깥 반경 하나뿐이다:

    son 배관   내 50.0 / 외 57.0 mm  (벽 7mm)  → 기존 defect_hole28.stl
    지그재그   내 50.0 / 외 56.0 mm  (벽 6mm)  → 여기서 만드는 것

기존 STL 을 그대로 쓰면 조각 바깥면이 관 바깥으로 **1mm 튀어나온다.** 관
안쪽에서 보는 카메라에는 안 보이지만 `--glass` 로 밖에서 보면 드러나고,
무엇보다 "관벽 조각을 제자리에 끼운다" 는 전제가 깨진다.

실행:
    python3 build_defect_w56.py            # ø28 (기본)
    python3 build_defect_w56.py --dia 20
"""

import argparse
from pathlib import Path

import numpy as np

from wall_patch import hole_patch, measured_hole_dia

BORE_R = 50.0
WALL_R = 56.0        # 🔑 지그재그 배관 실측 (test_pipe_zigzag_hook_R100.usda)

# 이 로봇의 휠 궤도 — son 로봇(폭 4mm)과 다르다
TRACKS_DEG = (90.0, 210.0, 330.0)
TRACK_HALF_DEG = np.degrees(np.arctan(6.0 / 40.0))     # 폭 12mm @ r40 → 8.53°


def main():
    ap = argparse.ArgumentParser(description="지그재그 배관용 결함/비드 STL")
    ap.add_argument("--dia", type=float, default=28.0)
    ap.add_argument("--grid", type=int, default=80)
    ap.add_argument("--clock", type=float, default=180.0,
                    help="놓을 시계각 (간섭 검사에만 쓴다)")
    ap.add_argument("--out", default=str(Path(__file__).resolve().parent / "meshes"))
    a = ap.parse_args()

    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    # 셀 중심으로 뚫으므로 실제 구멍이 요청보다 작다 → 재서 맞춘다
    cut = a.dia
    defect = bead = None
    for _ in range(12):
        defect, bead, half_len, half_ang = hole_patch(
            a.dia, BORE_R, WALL_R, grid=a.grid, cut_dia_mm=cut)
        err = a.dia - measured_hole_dia(defect, BORE_R)
        if abs(err) <= 0.02:
            break
        cut += err

    tag = f"{a.dia:g}".replace(".", "p")
    names = {f"defect_hole{tag}_w56": defect, f"bead_hole{tag}_w56": bead}
    print("=" * 78)
    print(f"구멍 결함 ø{a.dia:g}mm — 내 {BORE_R} / 외 {WALL_R} mm (벽 "
          f"{WALL_R - BORE_R:.0f}mm)")
    print("=" * 78)
    for name, m in names.items():
        m.merge_vertices()
        m.export(str(out / f"{name}.stl"))
        b = m.bounds
        print(f"  {name:24s} 삼각형 {len(m.faces):6,d}  "
              f"bbox {np.round(b[1] - b[0], 2)}  watertight={m.is_watertight}")
    print(f"  실측 구멍 지름 {measured_hole_dia(defect, BORE_R):.3f}mm "
          f"(요청 {a.dia:g}, 판정지름 {cut:.3f})")

    # ── 휠 궤도 간섭 ────────────────────────────────────────────────
    # 🚨 son 로봇 기준(폭 4mm → ±2.9°)으로 판단하면 안 된다. 이 로봇은 휠이
    #    12mm 라 궤도가 ±8.53° 로 3배 가까이 넓다.
    port_half = np.degrees(np.arcsin(min(1.0, a.dia / 2.0 / BORE_R)))
    lo, hi = a.clock - port_half, a.clock + port_half
    print("-" * 78)
    print(f"휠 궤도 간섭 — 개구 시계각 {lo:.1f}~{hi:.1f}° "
          f"(중심 {a.clock:.0f}°, 반각 {port_half:.2f}°)")
    worst = 1e9
    for t in TRACKS_DEG:
        tl, th = t - TRACK_HALF_DEG, t + TRACK_HALF_DEG
        gap = min(abs(tl - hi), abs(lo - th))
        overlap = not (hi < tl or lo > th)
        worst = min(worst, -1.0 if overlap else gap)
        print(f"  궤도 {t:5.0f}° ({tl:6.1f}~{th:6.1f}°)  "
              + ("🚨 겹친다 — 바퀴가 구멍에 빠진다"
                 if overlap else f"여유 {gap:.2f}°"))
    print("-" * 78)
    print(("✅ 통과" if worst > 0 else "❌ 겹침") +
          f" — 최소 여유 {worst:.2f}°")
    print(f"저장  {out}")


if __name__ == "__main__":
    main()
