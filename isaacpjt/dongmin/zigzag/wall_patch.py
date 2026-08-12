"""[자산생성·기반] 관벽 조각 기하 — `build_defect_w56.py` 가 딛고 서는 바닥.

## 왜 여기 있나

원본은 `src/son` 에 있다. 이 폴더를 `src/son` 에서 떼어 낼 때(2026-08-06),
`build_defect_w56.py` 만이 유일하게 남은 바깥 의존이었다:

    build_defect_w56.py → src/son/pipe/build_hole_defect.py  (hole_patch)
                              → src/son/tools/build_parts.py (_wall_patch)

**세 함수만 옮겨 왔다.** `build_hole_defect.py` 의 나머지(`leak_report`,
`track_clearance_deg`, `main`)는 son 로봇·son 관벽(외반경 57mm) 전용이라 여기
쓰이지 않는다 — 이 폴더는 벽 6mm(외반경 56mm) 를 쓰고, 휠 궤도 간섭 검산은
`build_defect_w56.py` 가 제 값(휠 폭 12mm)으로 따로 한다.

🚨 **원본이 바뀌면 여기는 안 따라온다.** 사본이지 링크가 아니다. 다만 이
기하는 "관벽 조각을 개구부에 끼운다" 는 고정된 규약이라 흔들릴 값이 아니다.

## 조각 프레임 (배관과 같다)

    축 = X,  조각 중심이 +Z 방향(시계각 0)

`defect.py` 가 `Rx(-시계각)` 만 걸어 관 원하는 자리에 놓는다.
"""

import math

import numpy as np
import trimesh

# ── 기본 치수 (원본 build_hole_defect.py 와 같다) ─────────────────────
# 조각 테두리 여유. 구멍 지름에 이만큼씩 더한 것이 조각 크기다.
# 축방향·원주방향을 같게 둬서 조각이 거의 정사각(호 기준)이 된다.
PATCH_MARGIN_MM = 8.0
# 비드가 구멍 테두리를 물고 넘어가는 폭. ø6 시절 1.6mm 는 ø28 에서 실오라기라
# 용접부처럼 안 보인다. 구멍이 커진 만큼 같이 키운다.
BEAD_MARGIN_MM = 3.0
# 비드가 관 안쪽으로 솟는 높이. Depth 판정은 "관벽보다 바깥으로 파이지
# 않았는가" 를 보므로 안쪽 돌출은 그대로 통과한다.
BEAD_PROUD_MM = 0.8
# 격자 분할. ø6 기본값(40)을 ø28 에 그대로 쓰면 셀이 1.1mm 라 구멍 테두리가
# 눈에 띄게 각진다. 0.55mm 로 잘라 원형으로 보이게 한다.
GRID = 80


def _wall_patch(r_in_fn, half_len, half_ang, r_out, nu=40, nv=40,
                drop_fn=None):
    """관벽 조각. 결함·비드를 같은 개구부에 끼우기 위한 공통 형상.

    로컬 프레임은 배관과 같다. 축 = X, 조각 중심은 +Z 방향(각도 0).
    r_in_fn(u, v) 가 안쪽 반경을 준다. drop_fn 이 True 인 셀은 뚫는다.
    """
    us = np.linspace(-half_len, half_len, nu + 1)
    vs = np.linspace(-half_ang, half_ang, nv + 1)
    U, V = np.meshgrid(us, vs, indexing='ij')
    RI = r_in_fn(U, V)

    def ring(r):
        return np.stack([U, r * np.sin(V), r * np.cos(V)], axis=-1)

    inner = ring(RI)
    outer = ring(np.full_like(RI, r_out))
    verts = np.concatenate([inner.reshape(-1, 3), outer.reshape(-1, 3)])
    n = (nu + 1) * (nv + 1)

    def idx(i, j):
        return i * (nv + 1) + j

    faces = []
    live = np.ones((nu, nv), dtype=bool)
    if drop_fn is not None:
        cu = 0.5 * (us[:-1] + us[1:])
        cv = 0.5 * (vs[:-1] + vs[1:])
        CU, CV = np.meshgrid(cu, cv, indexing='ij')
        live = ~drop_fn(CU, CV)

    for i in range(nu):
        for j in range(nv):
            if not live[i, j]:
                continue
            a, b = idx(i, j), idx(i, j + 1)
            c, d = idx(i + 1, j), idx(i + 1, j + 1)
            faces += [[a, c, b], [b, c, d]]                    # 안쪽 면
            faces += [[n + a, n + b, n + c], [n + b, n + d, n + c]]  # 바깥 면

    # 뚫린 구멍의 옆벽과 조각 테두리를 막는다
    def wall(a, b):
        faces.append([a, b, n + a])
        faces.append([b, n + b, n + a])

    for i in range(nu):
        for j in range(nv):
            if not live[i, j]:
                continue
            if i == 0 or not live[i - 1, j]:
                wall(idx(i, j + 1), idx(i, j))
            if i == nu - 1 or not live[i + 1, j]:
                wall(idx(i + 1, j), idx(i + 1, j + 1))
            if j == 0 or not live[i, j - 1]:
                wall(idx(i, j), idx(i + 1, j))
            if j == nv - 1 or not live[i, j + 1]:
                wall(idx(i + 1, j + 1), idx(i, j + 1))

    m = trimesh.Trimesh(vertices=verts, faces=np.array(faces))
    m.remove_unreferenced_vertices()
    m.fix_normals()
    return m


def hole_patch(hole_dia_mm, bore_r, wall_r, margin_mm=PATCH_MARGIN_MM,
               bead_margin_mm=BEAD_MARGIN_MM, proud_mm=BEAD_PROUD_MM,
               grid=GRID, cut_dia_mm=None):
    """결함 조각과 비드 조각을 한 쌍으로 만든다.

    두 조각은 같은 프레임·같은 크기라 자리를 옮기지 않고 가시성만 뒤집으면
    된다 (`zigzag_demo.py` 의 SWAP 단계).

    `cut_dia_mm` 은 **셀을 지울 때 쓰는 판정 지름**이다. 셀 *중심*으로
    판정하므로 남은 셀의 모서리가 안쪽으로 튀어나와 실제 구멍이 요청보다
    작아진다(격자 0.55mm 에서 -0.77mm 실측). 조각 크기·비드는 요청 지름을
    그대로 쓰고 이 판정 지름만 키워 보정한다.
    """
    rad = (hole_dia_mm if cut_dia_mm is None else cut_dia_mm) / 2.0
    half_len = (hole_dia_mm + 2.0 * margin_mm) / 2.0
    # 원주 방향도 같은 호 길이로 잡는다 → 각도로 환산
    half_ang = half_len / bore_r

    def flat(u, v):
        return np.full_like(u, bore_r)

    def hole(u, v):
        return np.hypot(u, v * bore_r) < rad

    def cap(u, v):
        # 비드는 **요청 지름** 기준이다 — 보정된 판정 지름을 쓰면 덮는 범위가
        # 격자 해상도에 따라 흔들린다.
        r = np.hypot(u, v * bore_r)
        w = hole_dia_mm / 2.0 + bead_margin_mm
        prof = np.clip(1.0 - (r / w) ** 2, 0.0, 1.0)
        return bore_r - proud_mm * prof

    defect = _wall_patch(flat, half_len, half_ang, wall_r,
                         nu=grid, nv=grid, drop_fn=hole)
    bead = _wall_patch(cap, half_len, half_ang, wall_r,
                       nu=grid, nv=grid)
    return defect, bead, half_len, math.degrees(half_ang)


def measured_hole_dia(mesh, bore_r, tol=0.05):
    """만들어진 메시에서 **실제** 구멍 지름을 되잰다.

    셀 중심으로 뚫으므로 요청 지름과 격자 해상도만큼 어긋난다. 요청값을
    그대로 믿지 않고 결과를 재서 남긴다 — 누수 판정이 이 값에 걸린다.
    """
    v = np.asarray(mesh.vertices)
    inner = v[np.abs(np.hypot(v[:, 1], v[:, 2]) - bore_r) < tol]
    if len(inner) == 0:
        return 0.0
    # 구멍 테두리 = 안쪽 면 정점 중 조각 중심에 가장 가까운 것들
    arc = np.arctan2(inner[:, 1], inner[:, 2]) * bore_r
    r = np.hypot(inner[:, 0], arc)
    return 2.0 * float(r.min())
