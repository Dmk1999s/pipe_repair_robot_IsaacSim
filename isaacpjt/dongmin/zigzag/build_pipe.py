"""[자산생성] 지그재그 배관 메시 — `course.py` 의 `_SEGS` 에서 관을 만든다.

## 왜 필요한가

원래 `test_pipe_zigzag_hook_R100.usda` 는 CATIA 변환본이고 생성기가 없었다.
`course.py` 는 그 메시를 **역산해서** 쓴 기술(記述)이었다. 그래서 코스를 늘리면
좌표만 길어지고 실제 관은 그대로라 **로봇이 관 밖 허공을 달린다.**

→ 의존 방향을 뒤집는다. `course._SEGS` 가 정본이고 관을 여기서 만든다.

## 원본과 같게 맞춘 것 (드롭인이어야 한다)

    링당 48점, 시계각 270° 에서 +7.5° 씩          — 원본 점 배열과 같은 순서
    안쪽 링 전부 → 바깥 링 전부                    — 인덱스 배치도 같다
    안쪽 껍질 법선은 **관 축을 향한다**            — 카메라가 안에서 본다
    양 끝은 도넛 마개(annulus)로 닫는다            — watertight
    physics 속성·doubleSided·subdivisionScheme     — 원본 값 그대로

🚨 **안쪽 껍질 감김 방향을 틀리면 조용히 망가진다.** `doubleSided = 0` 이라
   법선이 밖을 보면 관 안에서는 뒷면이라 **아무것도 안 보인다** — 물리는
   멀쩡한데 카메라 검출만 전멸한다. 아래 `_check_winding` 이 매번 검산한다.

## 링 간격

원본은 직선에서 14.58mm 였다(평균 7.57mm). 여기서는 **8mm 균일**로 촘촘하게
간다. 결함 개구를 삼각형 단위로 파내기 때문이다(`defect.install`) — 링이
성기면 ø28 개구가 링 2장에 걸쳐 테두리가 각지고, TODO_WATER 의 ø38.1 은 더
심하다. 8mm 면 ø28 이 축방향 3.5장에 걸친다.

실행:
    python3 build_pipe.py                 # ZIGZAG_COURSE 기본(long)
    ZIGZAG_COURSE=hook python3 build_pipe.py --out /tmp/hook_regen.usda   # 원본 대조용
"""

import argparse
import math
from pathlib import Path

import numpy as np

import course

WS = Path("/home/ubuntu/cobot3_ws")

N_RING = 48                  # 링당 점 수 (원본과 같다)
CLOCK0_DEG = 270.0           # 첫 점의 시계각 (원본 점 배열에서 역산)
RING_STEP_M = 0.008          # 링 간격 목표


def _ring_positions(step, branch=0):
    """한 가지 안에서 구간 경계가 링에 정확히 얹히도록 s 목록을 만든다.

    경계를 넘겨 균일 분할하면 굽힘 시작점이 링 사이에 떨어져 관이 미세하게
    각진다. 구간마다 따로 나누고 이음매를 한 번만 넣는다.
    """
    b = course.BRANCHES[branch]
    bounds = course._S0[b.i0:b.i1 + 1]
    ss = [bounds[0]]
    for s0, s1 in zip(bounds[:-1], bounds[1:]):
        n = max(2, int(round((s1 - s0) / step)))
        ss.extend(s0 + (s1 - s0) * k / n for k in range(1, n + 1))
    return np.array(ss)


def _check_continuity():
    """구간이 실제로 이어지는가 — 끝점과 접선이 둘 다 맞아야 한다.

    좌표를 손으로 적는 자료라 오타 하나면 관이 끊긴 채 생성된다. 그 상태는
    시뮬레이터를 띄워야 드러나므로 여기서 막는다.

    🚨 **가지가 시작하는 경계는 건너뛴다.** 거기서는 중심선이 이탈각만큼
       일부러 꺾이고(분기), 앞 구간의 끝점과도 이어지지 않는다 — 가지의 첫
       점은 본관 **중간**에 있다. 검사에 넣으면 정상인데 매번 걸린다.
    """
    bad = []
    for k in range(len(course._SEGS) - 1):
        if (k + 1) in course.SEG_BRANCH_START:
            continue
        s = course._S0[k + 1]
        x0, y0, tx0, ty0 = course.point_at(s - 1e-7)
        x1, y1, tx1, ty1 = course.point_at(s + 1e-7)
        gap = math.hypot(x1 - x0, y1 - y0) * 1000.0
        turn = math.degrees(math.acos(max(-1.0, min(1.0, tx0 * tx1 + ty0 * ty1))))
        if gap > 0.01 or turn > 0.1:
            bad.append(f"  구간 {k}→{k + 1} (s={s * 1000:.1f}mm): "
                       f"틈 {gap:.3f}mm, 접선 꺾임 {turn:.3f}°")
    if bad:
        raise SystemExit("[중단] 코스가 이어지지 않는다 —\n" + "\n".join(bad))


def build_points(ss):
    """(2, 링수, 48, 3) — [안/바깥][링][둘레][xyz]."""
    th = np.radians(CLOCK0_DEG + np.arange(N_RING) * (360.0 / N_RING))
    sin_t, cos_t = np.sin(th), np.cos(th)
    out = np.empty((2, len(ss), N_RING, 3))
    for k, s in enumerate(ss):
        x, y, tx, ty = course.point_at(float(s))
        lx, ly = -ty, tx                      # 진행 방향 왼쪽 (course 규약)
        for shell, r in enumerate((course.PIPE_IR, course.PIPE_OR)):
            out[shell, k, :, 0] = x + lx * r * sin_t
            out[shell, k, :, 1] = y + ly * r * sin_t
            out[shell, k, :, 2] = r * cos_t
    return out


# 삼각형 종류 — 합집합 절단이 안/바깥을 **다른 반경**으로 견주기 때문에 필요하다
KIND_INNER, KIND_OUTER, KIND_CAP = 0, 1, 2


def build_faces(n_rings):
    """삼각형 인덱스 (M, 3) 과 종류 (M,). 감김은 원본 메시에서 역산한 것과 같다."""
    NJ, NR = N_RING, n_rings

    def inn(k, j):
        return k * NJ + (j % NJ)

    def out(k, j):
        return NR * NJ + k * NJ + (j % NJ)

    tris, kind = [], []
    for k in range(NR - 1):
        for j in range(NJ):
            # 안쪽 — 법선이 관 축을 향한다
            tris.append((inn(k + 1, j + 1), inn(k + 1, j), inn(k, j)))
            tris.append((inn(k, j + 1), inn(k + 1, j + 1), inn(k, j)))
            # 바깥 — 반대 감김
            tris.append((out(k + 1, j), out(k + 1, j + 1), out(k, j)))
            tris.append((out(k + 1, j + 1), out(k, j + 1), out(k, j)))
            kind += [KIND_INNER, KIND_INNER, KIND_OUTER, KIND_OUTER]
    K = NR - 1
    for j in range(NJ):
        # 시작 마개 (도넛)
        tris.append((inn(0, j), out(0, j + 1), inn(0, j + 1)))
        tris.append((inn(0, j), out(0, j), out(0, j + 1)))
        # 끝 마개
        tris.append((inn(K, j + 1), out(K, j), inn(K, j)))
        tris.append((inn(K, j + 1), out(K, j + 1), out(K, j)))
        kind += [KIND_CAP] * 4
    return np.array(tris, dtype=np.int64), np.array(kind, dtype=np.int8)


def _check_winding(pts_flat, tris, n_rings):
    """안쪽 껍질 삼각형의 법선이 정말 관 축을 향하는가.

    옆면 삼각형만 본다(마개는 축 방향이라 판정 대상이 아니다). 중심선은
    course 가 주고, 삼각형 중심에서 중심선으로 향하는 방향과 법선의 내적이
    양수여야 한다.
    """
    n_side = (n_rings - 1) * N_RING * 4
    inner = tris[:n_side][::4]                     # 안쪽 T1 만 표본
    a, b, c = (pts_flat[inner[:, i]] for i in range(3))
    nrm = np.cross(b - a, c - a)
    cen = (a + b + c) / 3.0
    s, _, tx, ty, cx, cy = course.project(cen[:, 0], cen[:, 1])
    inward = np.stack([cx - cen[:, 0], cy - cen[:, 1], -cen[:, 2]], axis=-1)
    dot = np.sum(nrm * inward, axis=1)
    n_bad = int((dot <= 0).sum())
    if n_bad:
        raise SystemExit(
            f"[중단] 안쪽 껍질 법선이 뒤집혔다 — {n_bad}/{len(inner)}개가 "
            f"바깥을 본다. doubleSided=0 이라 관 안에서 아무것도 안 보이게 된다.")
    return len(inner)


USDA = """#usda 1.0
(
    defaultPrim = "{prim}"
    kilogramsPerUnit = 1
    metersPerUnit = 1
    upAxis = "Z"
)

def Xform "{prim}"
{{
    def Mesh "geom" (
        prepend apiSchemas = ["PhysicsCollisionAPI", "PhysicsMeshCollisionAPI", "PhysicsMaterialAPI"]
    )
    {{
        uniform bool doubleSided = 0
        float3[] extent = [({e0}), ({e1})]
        int[] faceVertexCounts = [{counts}]
        int[] faceVertexIndices = [{indices}]
        uniform token physics:approximation = "none"
        bool physics:collisionEnabled = 1
        float physics:density = 0
        float physics:dynamicFriction = 0.8
        float physics:restitution = 0
        float physics:staticFriction = 0.9
        custom float physxCollision:contactOffset = 0.0005
        custom float physxCollision:restOffset = 0
        point3f[] points = [{points}]
        uniform token subdivisionScheme = "none"
    }}
}}
"""


def main():
    ap = argparse.ArgumentParser(description="지그재그 배관 메시 생성")
    ap.add_argument("--out", default=None, help="기본은 course.PIPE_USDA_NAME")
    ap.add_argument("--step", type=float, default=RING_STEP_M * 1000,
                    help="링 간격(mm)")
    a = ap.parse_args()

    out = Path(a.out) if a.out else WS / course.PIPE_USDA_NAME

    print("=" * 78)
    print(course.describe())
    print("=" * 78)
    _check_continuity()
    print("연속성 ✅ — 구간 이음매 전부 틈 <0.01mm, 접선 꺾임 <0.1°")

    ss = _ring_positions(a.step / 1000.0)
    pts = build_points(ss)
    tris = build_faces(len(ss))
    flat = pts.reshape(-1, 3)
    n_chk = _check_winding(flat, tris, len(ss))
    print(f"감김 방향 ✅ — 안쪽 껍질 표본 {n_chk:,}개 전부 법선이 관 축을 향한다")

    lo, hi = flat.min(axis=0), flat.max(axis=0)
    prim = "TestPipeZigzag" + ("Long" if course.COURSE == "long" else "Hook")
    txt = USDA.format(
        prim=prim,
        e0=", ".join(f"{v:.6g}" for v in lo),
        e1=", ".join(f"{v:.6g}" for v in hi),
        counts=", ".join(["3"] * len(tris)),
        indices=", ".join(str(int(v)) for v in tris.reshape(-1)),
        points=", ".join(f"({p[0]:.6f}, {p[1]:.6f}, {p[2]:.6f})" for p in flat))
    out.write_text(txt)

    print("-" * 78)
    print(f"링 {len(ss):,}개 (간격 {a.step:.1f}mm)  정점 {len(flat):,}  "
          f"삼각형 {len(tris):,}")
    print(f"bbox  x {lo[0] * 1000:7.1f}~{hi[0] * 1000:7.1f}  "
          f"y {lo[1] * 1000:7.1f}~{hi[1] * 1000:7.1f}  "
          f"z {lo[2] * 1000:6.1f}~{hi[2] * 1000:5.1f} mm")
    print(f"저장  {out}  ({out.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
