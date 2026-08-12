"""[Isaac 3.11] 전방 카메라와 결함 검출 — 이 로봇의 주 센서.

`src/son/repair_demo.py` 의 검출 층을 지그재그 코스로 옮긴 것이다. 원리(어안
등거리 투영, 어둠 덩어리로 구멍 찾기, 채도로 비드 찾기)는 그대로 두고,
**관 형상에 기대던 부분만** 코스 일반 기하로 바꿨다.

## repair_demo 와 다른 곳 — 여기가 이식의 핵심이다

    hole_target()   repair_demo: 광선과 **직선 원기둥**(축 X, 중심선 y=IN_Y)의
                    2차방정식 교차. 굽은 코스에는 원리적으로 못 쓴다.
                    여기: **광선 행진 + 이분법**. 2mm 간격으로 전진하며
                    `course` 기준 반경이 50mm 를 넘는 첫 지점을 찾고 30회
                    이분한다(수렴 오차 < 2e-6 mm). 어떤 형상이든 성립한다.

    wall_radius_map()  repair_demo: `hypot(y − IN_Y, z)` 로 반경을 잰다.
                    여기: `course.wall_uv_many()` 로 중심선까지의 거리를 잰다.

🚨 **깊이(Depth)로 결함 위치를 정하지 않는다.** 두 가지 이유는 repair_demo 가
   실측으로 남겼고 여기서도 그대로다:
     ① 구멍 자리는 진짜 관통이라 그 화소의 깊이가 관 **너머**로 빠진다(inf).
     ② 이 조건의 Depth 역투영은 ±5mm 흩어진다 — 반경 50mm 에서 5mm 면 시계각
        5.7° 이고, 정렬 허용치 1.5mm(원주 1.7°)를 통째로 넘는다.
   → 위치는 **어안 광선 × 관 내벽 교차**로만 구한다. 깊이는 "메워졌는가" 판정
     (`wall_verdict`)에만 쓴다.

## 🚨 카메라가 토치보다 **앞**에 있다 — 용접 자리는 제자리에서 안 보인다

    로봇 원점 기준   용접링·토치 x=+62mm,  전방 카메라 x=+95mm
                     → 카메라가 토치보다 **33mm 앞**

즉 토치를 결함에 맞추면 결함은 카메라 **뒤**로 간다. 그래서 용접 뒤 검증하려면
반드시 후진해야 한다(repair_demo 의 REPOSITION 과 같은 이유, 거리만 다르다).

필요한 후진량은 화각에서 나온다. 결함은 관벽(반경 50mm)에 있고 카메라는 축
근처에 있으므로, 카메라에서 축방향으로 L 만큼 떨어지면 광축에서의 각도가
θ = atan(50/L) 이다. 세로 반화각이 39.4°(180px ÷ f 261.9px)이고 판정 창
band_px=36 까지 들어와야 하므로

    r_px + 36 ≤ 180  →  θ ≤ 31.5°  →  L ≥ 50/tan(31.5°) = 81.5mm

카메라가 토치보다 33mm 앞이므로 로봇은 **최소 48.5mm**, 여유를 봐서 140mm
후진한다(그때 L = 107mm, r_px ≈ 114px).
"""

import math

import numpy as np
from pxr import Gf, UsdGeom, UsdLux

import course

# ── 카메라 제원 (son camera.yaml 규약) ───────────────────────────────
# 🚨 해상도를 바꾸면 **화소 개수로 잡은 임계가 조용히 깨진다.** 초점거리는
#    화각에서 유도하므로 자동으로 따라가지만 면적 임계는 손으로 같이 줄여야
#    한다 → `AREA_SCALE` 을 곱한다.
CAM_HFOV = 140.0
DESIGN_W, DESIGN_H = 1280.0, 720.0

# ── 결함 검출 임계 ──────────────────────────────────────────────────
# 밝기 임계는 **고정값으로 박지 않는다.** 조명이 카메라 위치 종속이고 노출도
# 변한다. 그 프레임의 5~90분위 사이에서 유도한다.
HOLE_DARK_FRAC = 0.12
BEAD_SAT_MIN = 60          # HSV 채도 하한 — 관벽(회색)·관 저 끝(검정)은 0 이다
BEAD_VAL_MIN = 40
# 테두리 검사 — 덩어리를 이만큼 부풀린 띠가 얼마나 밝아야 "벽에 둘러싸였다" 인가.
# 🚨 이 검사가 없으면 굽힘의 어두운 터널 **가장자리 조각**이 통과한다(실측).
RING_K = 9                 # 팽창 커널 → 약 4px 폭의 띠
RING_BRIGHT_FRAC = 0.75    # 띠 화소의 75% 이상이 임계보다 밝아야 한다
#   0.85 는 너무 빡빡했다 — 결함이 화면 아래 가장자리로 내려가면 벽면
#   조도가 떨어져 진짜 구멍도 떨어졌다(실측: 23번 중 3번만 통과).


class Vision:
    """전방 카메라 한 대 + 검출·판정. `zigzag_demo.py` 가 하나만 만든다."""

    def __init__(self, stage, world, robot_path, res=(640, 360),
                 headless=True, cam_local_x=0.033):
        self.stage = stage
        self.world = world
        self.headless = headless
        self.W, self.H = int(res[0]), int(res[1])
        self.area_scale = (self.W * self.H) / (DESIGN_W * DESIGN_H)
        self.f_px = (self.W / 2.0) / math.radians(CAM_HFOV / 2.0)
        self.ppx, self.ppy = self.W / 2.0, self.H / 2.0
        self.hole_min_px = max(60, 300 * self.area_scale)
        self.bead_min_px = max(20, 100 * self.area_scale)
        self.cam_path = f"{robot_path}/FrontBody/front_camera_rig/front_camera"
        self._xc = UsdGeom.XformCache()
        self._ann = self._dep = None
        self.ok = False
        # 기각 사유 계측 — 임계를 손으로 맞추려면 숫자가 있어야 한다
        self.rej = {"작음": 0, "큼": 0, "중앙(관저끝)": 0, "화면가장자리": 0,
                    "테두리어두움": 0, "통과": 0}
        # 헤드리스는 메인 루프가 render=False 로 돌아 어노테이터가 빈다.
        # 판정하는 순간에만 몇 프레임 강제로 굽는다.
        self.warm_scan = 4 if headless else 2
        self.warm_judge = 24 if headless else 4
        self._build(robot_path, cam_local_x)

    # ── 생성 ────────────────────────────────────────────────────────
    def _build(self, robot_path, cam_local_x):
        base = f"{robot_path}/FrontBody/front_camera_rig"
        UsdGeom.Xform.Define(self.stage, base)
        # 관 내부는 로봇 조명이 유일한 광원이다. 센서보다 4mm 앞, 광축 둘레 대칭.
        for k in range(2):
            lg = UsdLux.SphereLight.Define(self.stage, f"{base}/light_{k}")
            lg.CreateIntensityAttr(4.0e5)
            lg.CreateRadiusAttr(0.002)
            UsdGeom.Xformable(lg).AddTranslateOp().Set(
                Gf.Vec3d(cam_local_x + 0.004, 0.0,
                         0.012 * (1 if k == 0 else -1)))
        try:
            import omni.replicator.core as rep
            from isaacsim.sensors.camera import Camera
        except Exception as exc:
            print(f"[경고] 카메라 모듈 없음 — 검출 불가 ({exc})")
            return

        cam = Camera(prim_path=self.cam_path,
                     translation=np.array([cam_local_x, 0.0, 0.0]),
                     frequency=10, resolution=(self.W, self.H))
        cam.initialize()
        # 🚨 자세를 **손으로 유도해서** 준다. USD 카메라는 로컬 −Z 를 보고
        #    +X 가 화면 오른쪽, +Y 가 화면 위다. 이 로봇의 전방은 로컬 +X 이고
        #    위는 로컬 +Z 이므로 항등이 아니다(son 로봇은 전방이 −Z 라 항등이었다).
        #        Z_cam → −X_robot     (−Z_cam 이 전방 +X 를 본다)
        #        Y_cam → +Z_robot     (화면 위 = 관 위 → 바닥 결함이 화면 아래)
        #        X_cam →  Y_cam×Z_cam = −Y_robot
        #    이 회전행렬의 사원수가 (w,x,y,z) = (0.5, 0.5, −0.5, −0.5) 다.
        #    ⚠ 부호를 헷갈리기 쉬우므로 `verify_pose()` 가 실측으로 대조한다.
        cam.set_local_pose(orientation=np.array([0.5, 0.5, -0.5, -0.5]),
                           camera_axes="usd")
        cam.set_clipping_range(0.005, 5.0)
        cam.set_focal_length(3.0 * self.f_px * 1e-6)
        cam.set_horizontal_aperture(3.0 * self.W * 1e-6)
        try:
            cam.set_opencv_fisheye_properties(
                cx=self.ppx, cy=self.ppy, fx=self.f_px, fy=self.f_px,
                fisheye=[0.0, 0.0, 0.0, 0.0])
        except Exception as exc:
            print(f"[경고] 어안 설정 실패({exc}) — 핀홀로 진행")
        rp = cam.get_render_product_path()
        self._ann = rep.AnnotatorRegistry.get_annotator("rgb")
        self._ann.attach(rp)
        # 🔑 `distance_to_image_plane` 이 아니라 **`distance_to_camera`** 다.
        #    관 내부는 방사형이라 광축 투영 거리가 아니라 실제 광선 거리가 필요하다.
        self._dep = rep.AnnotatorRegistry.get_annotator("distance_to_camera")
        self._dep.attach(rp)
        self.ok = True

    def describe(self):
        return (f"전방 카메라 1대 (어안 {CAM_HFOV:.0f}°, {self.W}x{self.H} "
                f"= 설계 대비 화소 {self.area_scale * 100:.0f}%, "
                f"f={self.f_px:.1f}px) + 조명 2 — FrontBody 로컬 x=+33mm"
                f"  세로 반화각 {math.degrees(self.ppy / self.f_px):.1f}°")

    def verify_pose(self):
        """🚨 카메라 자세를 **실측으로** 대조한다.

        사원수 부호를 틀리면 영상은 멀쩡히 나오는데 결함이 화면 반대쪽에 찍혀
        검출이 조용히 죽는다(repair_demo 가 롤 90° 어긋남으로 같은 일을 겪었다).
        광축이 코스 접선과 같은 쪽인지, 화면 위가 관 위인지 각도로 찍는다.
        반환: (전방 오차 deg, 위쪽 오차 deg)
        """
        M = self._cam_matrix()
        if M is None:
            return None
        fwd = -M[2, :3] / max(np.linalg.norm(M[2, :3]), 1e-12)   # −Z_cam
        up = M[1, :3] / max(np.linalg.norm(M[1, :3]), 1e-12)     # +Y_cam
        C = M[3, :3]
        s, _, tx, ty, _, _ = course.project(C[0], C[1])
        tan = np.array([tx, ty, 0.0])
        e_fwd = math.degrees(math.acos(np.clip(float(fwd @ tan), -1, 1)))
        e_up = math.degrees(math.acos(np.clip(float(up @ np.array([0, 0, 1.0])),
                                              -1, 1)))
        return e_fwd, e_up

    # ── 프레임 ──────────────────────────────────────────────────────
    def _cam_matrix(self):
        p = self.stage.GetPrimAtPath(self.cam_path)
        if not p.IsValid():
            return None
        self._xc.Clear()
        m = self._xc.GetLocalToWorldTransform(p)
        return np.array([[m[i][j] for j in range(4)] for i in range(4)],
                        dtype=float)

    def frames(self, warm=None):
        """(rgb uint8, depth float32). 없으면 (None, None).

        🚨 **어노테이터는 마지막으로 렌더된 프레임을 그대로 들고 있다.**
           "데이터가 있으면 그만" 으로 짜면 두 번째 호출부터 렌더를 한 번도 안
           굽고 **직전 판정 때의 낡은 영상**을 다시 읽는다(repair_demo 실측:
           로봇이 120mm 후진했는데 두 판정이 화소 단위로 같은 영상을 봤다).
           → 조건 없이 **먼저 굽고 나서** 읽는다.
        """
        if not self.ok:
            return None, None
        for _ in range(self.warm_judge if warm is None else warm):
            self.world.step(render=True)
        c, z = self._ann.get_data(), self._dep.get_data()
        rgb = (np.asarray(c)[:, :, :3].astype(np.uint8)
               if c is not None and getattr(c, "size", 0) else None)
        depth = (np.asarray(z, dtype=np.float32)
                 if z is not None and getattr(z, "size", 0) else None)
        return rgb, depth

    # ── 검출 ────────────────────────────────────────────────────────
    def find_wall_hole(self, rgb, expect_px=None):
        """근접 벽면의 구멍 → dict 또는 None.

        🚨 **전방 개구부(관 저 끝)를 반드시 걸러야 한다.** 중앙 화소 하나만
           빼는 방식은 밝기 임계가 낮게 잡히면 중앙이 '어둡다' 에 안 걸려
           아무것도 안 걸러진다 — 관 저 끝이 통째로 "구멍" 이 된다.
           → ① 중앙 원판을 **격자로 훑어** 걸리는 라벨을 전부 제외
             ② 화면의 25% 를 넘는 덩어리는 벽면 구멍일 수 없으므로 제외
        """
        import cv2
        g = cv2.cvtColor(np.asarray(rgb)[:, :, :3].astype(np.uint8),
                         cv2.COLOR_RGB2GRAY)
        g = cv2.medianBlur(g, 5)
        h, w = g.shape
        lo, hi = np.percentile(g, 5), np.percentile(g, 90)
        thr = lo + HOLE_DARK_FRAC * (hi - lo)
        n, lab, st, ce = cv2.connectedComponentsWithStats(
            (g < thr).astype(np.uint8), 8)

        bore = set()
        rr = max(4, int(0.10 * min(h, w)))
        for yy in range(max(0, h // 2 - rr), min(h, h // 2 + rr), 3):
            for xx in range(max(0, w // 2 - rr), min(w, w // 2 + rr), 3):
                if lab[yy, xx]:
                    bore.add(int(lab[yy, xx]))
        big = 0.25 * h * w

        best = None
        for i in range(1, n):
            area = int(st[i, cv2.CC_STAT_AREA])
            if i in bore:
                self.rej["중앙(관저끝)"] += 1
                continue
            if area < self.hole_min_px:
                self.rej["작음"] += 1
                continue
            if area > big:
                self.rej["큼"] += 1
                continue
            # 🚨 **"밝은 벽에 둘러싸였는가" 를 실제로 검사한다.** 이 검출의 전제가
            #    그것인데, 예전에는 중앙 원판 필터로 **간접 추정**만 했다. 굽힘이
            #    가까우면 어두운 터널의 **가장자리 일부**가 따로 떨어져 나와
            #    작은 덩어리가 되고, 중앙에도 안 걸리고 크기도 그럴듯해서 그냥
            #    통과한다 — 실측(GUI 실행): 209px 덩어리가 후보로 잡혀 결국
            #    s=1234mm(정답 1600mm)에 용접하러 갔다.
            #    → 덩어리를 부풀려 만든 **테두리 띠**가 대부분 밝아야 한다.
            #      진짜 벽 구멍은 사방이 벽이라 통과하고, 터널 가장자리는
            #      한쪽이 계속 어두워 걸린다.
            x, y = int(st[i, cv2.CC_STAT_LEFT]), int(st[i, cv2.CC_STAT_TOP])
            bw, bh = int(st[i, cv2.CC_STAT_WIDTH]), int(st[i, cv2.CC_STAT_HEIGHT])
            # 화면 가장자리에 걸린 덩어리는 테두리를 다 볼 수 없다 → 판단 보류
            if x <= 1 or y <= 1 or x + bw >= w - 1 or y + bh >= h - 1:
                self.rej["화면가장자리"] += 1
                continue
            m_i = (lab == i).astype(np.uint8)
            ring = cv2.dilate(m_i, np.ones((RING_K, RING_K), np.uint8)) - m_i
            rp = g[ring > 0]
            bright = float((rp > thr).mean()) if rp.size else 0.0
            if bright < RING_BRIGHT_FRAC:
                self.rej["테두리어두움"] += 1
                continue
            self.rej["통과"] += 1
            if best is None or area > best["area_px"]:
                best = {"area_px": area, "cx": float(ce[i][0]),
                        "cy": float(ce[i][1]), "thr": float(thr),
                        "ring_bright": bright,
                        "r_eq_px": math.sqrt(area / math.pi)}
        if best and expect_px is not None:
            d = math.hypot(best["cx"] - expect_px[0], best["cy"] - expect_px[1])
            best["dist_px"] = d
            best["matched"] = d <= max(2.0 * best["r_eq_px"], 0.06 * w)
        return best

    def find_weld_bead(self, rgb, expect_px=None):
        """용접 비드를 **색**으로 찾는다 → dict 또는 None.

        🔑 어둠으로 어둠을 가르지 않는다. 관벽(회색)과 관 저 끝(검정)은 **둘 다
           채도 0** 이라, 채도만 보면 전방 개구부와 절대 헷갈리지 않는다.
        """
        import cv2
        hsv = cv2.cvtColor(np.asarray(rgb)[:, :, :3].astype(np.uint8),
                           cv2.COLOR_RGB2HSV)
        mask = ((hsv[:, :, 1] > BEAD_SAT_MIN)
                & (hsv[:, :, 2] > BEAD_VAL_MIN)).astype(np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
        n, lab, st, ce = cv2.connectedComponentsWithStats(mask, 8)
        best = None
        for i in range(1, n):
            area = int(st[i, cv2.CC_STAT_AREA])
            if area < self.bead_min_px:
                continue
            if best is None or area > best["area_px"]:
                best = {"area_px": area, "cx": float(ce[i][0]),
                        "cy": float(ce[i][1]),
                        "r_eq_px": math.sqrt(area / math.pi)}
        if best and expect_px is not None:
            d = math.hypot(best["cx"] - expect_px[0], best["cy"] - expect_px[1])
            best["dist_px"] = d
            best["matched"] = d <= max(3.0 * best["r_eq_px"], 0.08 * self.W)
        return best

    # ── 투영 / 역투영 ───────────────────────────────────────────────
    def project(self, world_pt):
        """월드 점 → 어안 화소 (px, py). 카메라 뒤면 None.

        등거리 어안이라 r = f·θ 다. 핀홀 tan 식을 쓰면 가장자리가 크게 틀어진다.
        """
        M = self._cam_matrix()
        if M is None:
            return None
        inv = np.linalg.inv(M)
        p = np.append(np.asarray(world_pt, float), 1.0) @ inv
        x, y, z = float(p[0]), float(p[1]), float(p[2])
        if -z <= 1e-9:
            return None
        theta = math.atan2(math.hypot(x, y), -z)
        r_px = self.f_px * theta
        rho = math.hypot(x, y)
        if rho < 1e-9:
            return self.ppx, self.ppy
        # USD 카메라 화면: +X 오른쪽, +Y 위. 화소 y 는 아래로 증가한다.
        return (self.ppx + r_px * x / rho, self.ppy - r_px * y / rho)

    def _ray(self, cx, cy, M):
        """화소 → (카메라 중심 C, 월드 방향 d). 등거리 어안 역투영."""
        ux = cx - self.ppx
        uy = -(cy - self.ppy)
        rr = math.hypot(ux, uy)
        th = rr / self.f_px
        if rr < 1e-9:
            d_cam = np.array([0.0, 0.0, -1.0])
        else:
            d_cam = np.array([ux / rr * math.sin(th), uy / rr * math.sin(th),
                              -math.cos(th)])
        d = d_cam @ M[:3, :3]
        return M[3, :3], d / max(float(np.linalg.norm(d)), 1e-12)

    def wall_hit(self, cx, cy, t_max=0.8, dt=0.002):
        """화소에서 쏜 광선이 **관 내벽에 닿는 점** → (s, 시계각, 반경m).

        🚨 repair_demo 는 여기서 직선 원기둥과 2차방정식을 풀었다. 굽은 코스
           에서는 성립하지 않으므로 **행진 + 이분법**으로 바꿨다. 관 형상에
           아무 가정도 안 하므로 굽힘 안에서도 그대로 맞는다.
        """
        M = self._cam_matrix()
        if M is None:
            return None
        C, d = self._ray(cx, cy, M)
        ts = np.arange(dt, t_max, dt)
        pts = C[None, :] + ts[:, None] * d[None, :]
        _, _, r = course.wall_uv_many(pts)
        out = np.nonzero(r >= course.PIPE_IR)[0]
        if len(out) == 0:
            return None
        i = int(out[0])
        lo = float(ts[i - 1]) if i > 0 else 0.0
        hi = float(ts[i])
        for _ in range(30):                     # 30회 → 2e-6 mm 수렴
            mid = 0.5 * (lo + hi)
            _, _, rm = course.wall_uv(C + mid * d)
            if rm < course.PIPE_IR:
                lo = mid
            else:
                hi = mid
        return course.wall_uv(C + hi * d)

    def hole_measure(self, hole):
        """검출된 덩어리를 **재서** dict 로 돌려준다 → 참/거짓을 여기서 가른다.

        🚨 **굽힘에서는 중앙 원판 필터가 통하지 않는다.** `repair_demo` 의
           "화면 중앙에 걸리는 라벨은 관 저 끝" 규칙은 **직관 전제**다. 굽은
           관에서는 관 저 끝(어두운 터널)이 화면 중앙을 크게 벗어나므로 그
           필터를 통과해 버린다 — 실측으로 걸렸다: 첫 굽힘 입구에서 면적
           **44,085px**(화면의 19%, 25% 상한 아래) 짜리 덩어리가 "구멍" 으로
           확정돼 로봇이 굽힘 한가운데로 용접하러 갔다.

        → **크기로 가른다.** 광선이 관벽에 닿는 거리를 알면 덩어리의 화소
          반지름에서 **실제 지름**이 나온다:

              지름[m] = 2 · r_eq_px · 거리[m] / f_px

          위 오검출은 거리 0.25m 에서 r_eq 118px → 지름 **225mm** 다. 내경이
          100mm 인 관에 그런 구멍은 있을 수 없다. 진짜 ø28 구멍은 거리 150mm
          에서 r_eq 24px → 지름 27.5mm 로 나온다.
          이 판별식은 **결함 위치를 전혀 안 쓴다** — 크기 등급만 쓴다.

        반환: {"s", "clock", "range_m", "dia_mm"} 또는 None
        """
        if hole is None:
            return None
        hit = self.wall_hit(hole["cx"], hole["cy"])
        if hit is None:
            return None
        M = self._cam_matrix()
        C, d = self._ray(hole["cx"], hole["cy"], M)
        P = course.wall_point(hit[0], hit[1])
        rng = float(np.linalg.norm(P - C))
        return {"s": hit[0], "clock": hit[1], "range_m": rng,
                "dia_mm": 2.0 * hole["r_eq_px"] * rng / self.f_px * 1000.0}

    # ── Depth 판정 ──────────────────────────────────────────────────
    def wall_radius_map(self, depth, centre_px, band_px):
        """창 안 화소를 3차원으로 되돌려 **중심선 기준 반경(mm)** 지도를 만든다.

        🚨 `welder/weld.py` 의 `radial_profile` 을 그대로 쓰면 안 된다. 그 식
           `D·sin θ` 는 **카메라가 관 축 위에 있다는 전제**라, 로봇이 편심한
           만큼(이 로봇은 다리 12개가 균형 잡은 자리에 서므로 수 mm) 그대로
           반경 오차가 된다. 재려는 파임은 1mm 안팎이라 오차가 신호보다 크다.
        → 어안 역투영으로 광선을 만들고 깊이를 곱해 월드 점을 만든 뒤
          **코스 중심선까지의 거리**를 잰다. 편심이 상쇄된다.
        """
        M = self._cam_matrix()
        if M is None or depth is None:
            return np.zeros((0, 0))
        d = np.asarray(depth, dtype=np.float64)
        h, w = d.shape
        cx, cy = centre_px
        x0, x1 = int(max(0, cx - band_px)), int(min(w, cx + band_px))
        y0, y1 = int(max(0, cy - band_px)), int(min(h, cy + band_px))
        sub = d[y0:y1, x0:x1]
        if sub.size == 0:
            return np.zeros((0, 0))

        # 🚨 관통 구멍 화소의 깊이는 **inf** 다(광선이 관 밖으로 빠진다). 그대로
        #    곱하면 inf×0 = nan 이 나와 numpy 가 경고를 쏟고, 뒤의 행렬곱까지
        #    오염된다. 여기서 한 번에 걷어 낸다 — **버리는 게 맞다.** 구멍
        #    한가운데를 재면 벽이 아니라 그 뒤 허공을 재는 것이기 때문이다.
        valid = np.isfinite(sub) & (sub > 0)
        sub = np.where(valid, sub, 0.0)

        yy, xx = np.mgrid[y0:y1, x0:x1]
        ux = xx - self.ppx
        uy = -(yy - self.ppy)
        r = np.hypot(ux, uy)
        theta = r / self.f_px
        with np.errstate(invalid="ignore", divide="ignore"):
            sx = np.where(r > 1e-9, ux / r, 0.0) * np.sin(theta)
            sy = np.where(r > 1e-9, uy / r, 0.0) * np.sin(theta)
        sz = -np.cos(theta)
        pts = np.stack([sx * sub, sy * sub, sz * sub], axis=-1)
        flat = pts.reshape(-1, 3)
        world = (np.hstack([flat, np.ones((flat.shape[0], 1))]) @ M)[:, :3]
        _, _, rad = course.wall_uv_many(world)
        rad = (rad * 1000.0).reshape(sub.shape)
        return np.where(np.isfinite(rad) & valid, rad, np.nan)

    def wall_verdict(self, depth, centre_px, k):
        """파임/메움 판정. 임계는 `welder/config/weld.yaml`(= sequencer.k) 그대로.

        분위수를 쓰지 않는다 — 결함은 화면에서 몇 화소뿐이라 창 전체의 99분위에
        묻혀 사라진다(실측). 중앙값 필터로 단발 잡음만 걷고 최댓값을 본다.
        """
        from scipy.ndimage import median_filter
        b = int(k["band_px"])
        rad = self.wall_radius_map(depth, centre_px, b)
        n_valid = int(np.isfinite(rad).sum())
        if n_valid < k["profile_min_px"]:
            return None, 0.0, f"프로파일 표본 부족 ({n_valid})"
        bore = float(k["bore_r_mm"])
        sm = median_filter(np.where(np.isfinite(rad), rad, bore),
                           size=int(k["median_px"]))
        peak = float(sm.max() - bore)
        deep = int((sm - bore >= k["depth_defect_mm"] * 0.5).sum())
        if peak >= k["depth_defect_mm"] and deep >= k["min_deep_px"]:
            return False, peak, f"여전히 파임 {peak:+.2f}mm ({deep}px)"
        if peak <= k["depth_repaired_mm"]:
            return True, peak, f"메워짐 {peak:+.2f}mm"
        return None, peak, f"판정 애매 {peak:+.2f}mm ({deep}px)"


def save_png(img, path):
    try:
        from PIL import Image
        Image.fromarray(img).save(path)
        return path
    except Exception:
        path = path.with_suffix(".ppm")
        with open(path, "wb") as f:
            f.write(b"P6\n%d %d\n255\n" % (img.shape[1], img.shape[0]))
            f.write(np.ascontiguousarray(img[:, :, :3]).tobytes())
        return path
