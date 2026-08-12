"""course.py 검증 — **실제 배관 메시로 대조한다.**

기하 모듈은 손으로 쓴 식이라 눈으로는 못 믿는다. 정점을 전부 투영해서 안쪽
링은 50.000mm, 바깥 링은 56.000mm 가 나오는지 본다. 하나라도 어긋나면 구간
자료(_SEGS)가 틀린 것이다.

🔑 **배관은 `course.PIPE_USDA_NAME` 을 따라간다** (2026-08-06). 예전에는 훅
   usda 를 박아 뒀는데, 코스를 연장한(long, 5.05m) 뒤에는 그 메시가 앞 1.77m
   밖에 안 덮어 "s 가 코스를 다 못 덮는다" 로 **엉뚱하게** 실패했다. 관과
   코스는 한 쌍이므로 같이 골라야 한다.

    python3 -m pytest test_code/test_course.py -q       # zigzag/ 에서
    python3 test_code/test_course.py                    # 직접 실행도 된다
    ZIGZAG_COURSE=hook python3 test_code/test_course.py  # 원본 훅으로 대조
"""

import math
import re
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import course                                              # noqa: E402

USDA = Path("/home/ubuntu/cobot3_ws") / course.PIPE_USDA_NAME


def _load_points():
    txt = USDA.read_text(encoding="utf-8")
    m = re.search(r"point3f\[\] points\s*=\s*\[(.*?)\]\s*\n", txt, re.S)
    return np.array([[float(v) for v in t.split(",")]
                     for t in re.findall(r"\(([^)]*)\)", m.group(1))])


PTS = _load_points()


def test_mesh_radii():
    """모든 정점이 중심선에서 정확히 50mm(안) / 56mm(밖) 떨어져 있다."""
    # z 성분까지 포함한 3차원 반경을 재야 한다 — project 는 xy 거리만 준다.
    s, d, tx, ty, cx, cy = course.project(PTS[:, 0], PTS[:, 1])
    r = np.hypot(d, PTS[:, 2]) * 1000

    H = len(PTS) // 2
    r_in, r_out = r[:H], r[H:]
    assert abs(r_in.mean() - 50.0) < 1e-3, f"안쪽 평균 {r_in.mean():.5f}"
    assert abs(r_out.mean() - 56.0) < 1e-3, f"바깥 평균 {r_out.mean():.5f}"
    assert r_in.std() < 1e-3, f"안쪽 산포 {r_in.std():.6f}"
    assert r_out.std() < 1e-3, f"바깥 산포 {r_out.std():.6f}"
    # 최악값도 본다 — 평균만 보면 구간 하나가 틀려도 묻힌다
    assert np.abs(r_in - 50.0).max() < 5e-3, \
        f"안쪽 최대 오차 {np.abs(r_in - 50.0).max():.5f}mm"
    assert np.abs(r_out - 56.0).max() < 5e-3, \
        f"바깥 최대 오차 {np.abs(r_out - 56.0).max():.5f}mm"


def test_s_covers_whole_course():
    """정점의 s 가 0 ~ S_TOTAL 을 빈틈없이 덮는다 (구간 누락 검출).

    🚨 히스토그램으로 세면 안 된다. 메시는 링 235개뿐이고 한 링의 48개 정점은
       **s 가 사실상 같다**(링 평면이 중심선에 수직). 즉 s 는 이산값 235개고,
       고정폭 bin 이 링 간격(최대 14.58mm)보다 좁으면 멀쩡한 코스에서도 빈
       bin 이 나온다. → **이웃한 s 사이의 간격**으로 본다.
    """
    s, *_ = course.project(PTS[:, 0], PTS[:, 1])
    assert s.min() < 1e-6, f"s 최소 {s.min()}"
    assert abs(s.max() - course.S_TOTAL) < 1e-3, \
        f"s 최대 {s.max():.6f} vs 총길이 {course.S_TOTAL:.6f}"
    u = np.unique(np.round(s, 6))
    gap = np.diff(np.concatenate([[0.0], u, [course.S_TOTAL]]))
    # 링 간격 실측 3.27~14.58mm. 그 두 배(30mm)를 넘으면 구간이 통째로 빠진 것이다.
    assert gap.max() < 0.030, \
        f"s {u[int(np.argmax(gap))] * 1000:.1f}mm 부근에 {gap.max() * 1000:.1f}mm 공백"
    assert len(u) >= 200, f"고유 s 가 {len(u)}개뿐 — 투영이 뭉개진다"


def test_point_at_roundtrip():
    """point_at(s) 를 다시 project 하면 같은 s 가 나온다."""
    for s in np.linspace(0, course.S_TOTAL, 401):
        x, y, tx, ty = course.point_at(s)
        s2, d2, *_ = course.project(x, y)
        assert abs(s2 - s) < 1e-6, f"s={s:.4f} → {s2:.4f}"
        assert d2 < 1e-9, f"s={s:.4f} 에서 중심선 거리 {d2:.3e}"
        assert abs(math.hypot(tx, ty) - 1.0) < 1e-9


def test_wall_uv_roundtrip():
    """wall_point → wall_uv 왕복이 일치한다 (굽힘 안쪽·바깥 포함)."""
    for s in np.linspace(0.01, course.S_TOTAL - 0.01, 97):
        for clock in (0.0, 90.0, 180.0, 270.0, 37.5):
            p = course.wall_point(s, clock)
            s2, c2, r2 = course.wall_uv(p)
            assert abs(s2 - s) < 1e-6, f"s {s:.4f} → {s2:.4f} (시계각 {clock})"
            assert abs((c2 - clock + 180) % 360 - 180) < 1e-6, \
                f"시계각 {clock} → {c2}"
            assert abs(r2 - course.PIPE_IR) < 1e-9


def test_tangent_continuity():
    """구간 경계에서 접선이 튀지 않는다 (곡선-직선 접합 검증)."""
    for s0 in course.SEG_START_S[1:]:
        _, _, ax, ay = course.point_at(s0 - 1e-5)
        _, _, bx, by = course.point_at(s0 + 1e-5)
        ang = math.degrees(math.acos(np.clip(ax * bx + ay * by, -1, 1)))
        assert ang < 0.02, f"s={s0:.4f} 경계에서 접선이 {ang:.4f}° 꺾인다"


def test_bend_spans():
    """굽힘 개수는 코스가 정하고, 각각 정확히 ¼원 호 길이여야 한다."""
    n_bend = sum(1 for sg in course._SEGS if sg[0] == "A")
    assert len(course.BEND_SPANS) == n_bend
    assert n_bend == (7 if course.COURSE == "long" else 3), \
        f"{course.COURSE} 코스의 굽힘이 {n_bend}개다"
    for a, b in course.BEND_SPANS:
        assert abs((b - a) - course.BEND_R * math.pi / 2) < 1e-9
    assert course.in_bend(course.BEND_SPANS[0][0] + 0.01)
    assert not course.in_bend(0.1)


def test_no_self_intersection():
    """관이 자기 자신과 겹치지 않는다 — 중심선 간격 ≥ 외경(112mm).

    🚨 이게 깨지면 시뮬레이터에서만 드러난다. 두 구간의 벽이 서로 파고들어
       로봇이 "벽이 없는 벽" 을 통과하거나 반대로 허공에서 막힌다. 구간
       좌표는 손으로 적는 자료라(_SEGS) 연장할 때마다 검산이 필요하다.

    이웃한 구간(굽힘으로 이어진 안쪽 모서리)은 원리적으로 붙어 있으므로
    **s 가 충분히 떨어진 쌍만** 본다. 굽힘 하나를 완전히 돌아 나가는 데
    드는 호 길이(¼원 157mm)의 2배를 문턱으로 잡았다.
    """
    ss = np.arange(0.0, course.S_TOTAL, 0.005)
    pts = np.array([course.point_at(float(s))[:2] for s in ss])
    d = np.hypot(pts[:, None, 0] - pts[None, :, 0],
                 pts[:, None, 1] - pts[None, :, 1])
    far = np.abs(ss[:, None] - ss[None, :]) > 2 * course.BEND_R * math.pi / 2
    worst = d[far].min() if far.any() else float("inf")
    i, j = np.unravel_index(np.where(far, d, np.inf).argmin(), d.shape)
    assert worst >= 2 * course.PIPE_OR, (
        f"중심선이 {worst * 1000:.1f}mm 까지 접근한다 "
        f"(s={ss[i] * 1000:.0f}mm ↔ {ss[j] * 1000:.0f}mm, "
        f"필요 {2 * course.PIPE_OR * 1000:.0f}mm) — 관끼리 겹친다")


if __name__ == "__main__":
    fails = 0
    for nm, fn in sorted(globals().items()):
        if nm.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"  ✅ {nm}")
            except AssertionError as exc:
                fails += 1
                print(f"  ❌ {nm}: {exc}")
    print(course.describe())
    print(f"\n정점 {len(PTS):,}개로 검증 — 실패 {fails}건")
    sys.exit(1 if fails else 0)
