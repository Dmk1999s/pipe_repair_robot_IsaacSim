"""[아이작심] 맵에서 층별 배관만 골라 띄운다 — 라이브로 보거나 PNG 로 뜬다.

    # ① 라이브 (WebRTC 클라이언트로 접속해 마우스로 돌려 본다)
    isaac_python tools/view_pipes.py --only floor1
    isaac_python tools/view_pipes.py --only floor2
    isaac_python tools/view_pipes.py --only pipes        # 두 층을 겹쳐 본다

    # ② 배치 (그림만 뽑는다 — 스트리밍은 매 프레임 실제로 그리므로 꺼 준다)
    ISAAC_STREAM=0 isaac_python tools/view_pipes.py --only floor1 --shot

🎯 **맵을 자르지 않는다.** `restroom_map_straight290.usda` 는 이미 층별로 프림이
   갈라져 있어(`Floor1_Pipes`/`Floor2_Pipes`/`..._Room`/`Aisle_*`) 나머지를
   **안 보이게**(`UsdGeom.Imageable.MakeInvisible`) 하면 그것이 곧 분리본이다.
   좌표가 원본 그대로이므로 여기서 읽은 값을 임무 스크립트에 바로 쓸 수 있다.
   파일로 떠서 남기고 싶으면 `tools/split_map.py` 를 쓴다(같은 기하, 단독 USD).

🚨 **맵에는 조명이 없다.** 머티리얼만 있고 광원 프림이 하나도 없어서, 그냥 열면
   RTX 가 새까만 화면을 낸다("맵이 안 열렸나" 로 오해하기 쉽다). 그래서 여기서
   돔+태양광을 얹는다 — 원본 USD 에는 쓰지 않는다(스테이지 메모리에만 있다).

🚨 **이 맵은 `metersPerUnit 1.0`(m)** 이다. 예전 실전 맵(restroom_pipe150_final_
   fixed.usd)은 0.001(mm) 이라 스테이지에 얹을 때 scale 0.001 을 줬다 — 그 관례를
   여기 쓰면 관이 1/1000 이 된다. 이 스크립트는 맵을 스테이지로 **직접 열기**
   때문에 스케일을 건드리지 않는다.

라이브로 볼 때 주의: 화면은 브라우저가 아니라 **Isaac Sim WebRTC Streaming
Client**(데스크톱 앱)로 본다. 주소 칸에 인스턴스 퍼블릭 IP 만 넣는다.
자세한 것은 `tools/isaac_autostream/livestream.py` 의 docstring 에 있다.
"""

import os
import sys
import time
from pathlib import Path

SON = Path(__file__).resolve().parent.parent
DEFAULT_MAP = SON / "maps" / "restroom_map_straight290.usda"

# --only 프리셋 → 보일 프림 이름. 나머지는 전부 숨긴다.
PRESETS = {
    "floor1": ["Floor1_Pipes"],
    "floor2": ["Floor2_Pipes"],
    "pipes": ["Floor1_Pipes", "Floor2_Pipes"],
    "floor1+": ["Floor1_Pipes", "Floor1_Sump", "Floor1_Room"],
    "floor2+": ["Floor2_Pipes", "Floor2_Room"],
    "all": None,                                  # 아무것도 숨기지 않는다
}


def _arg(name, default=None):
    """`--name 값` 을 꺼낸다. Kit 이 argv 를 같이 읽으므로 소비하지 않는다."""
    if name in sys.argv:
        i = sys.argv.index(name)
        if i + 1 < len(sys.argv) and not sys.argv[i + 1].startswith("--"):
            return sys.argv[i + 1]
        return True
    return default


ONLY = str(_arg("--only", "floor1"))
MAP = Path(str(_arg("--map", DEFAULT_MAP))).resolve()
SHOT = _arg("--shot", False)
RES = (1600, 1000)
_HOLD = float(_arg("--hold", 0) or 0)

if ONLY not in PRESETS:
    raise SystemExit(f"--only 는 {'/'.join(PRESETS)} 중 하나 (받은 값: {ONLY})")
if not MAP.exists():
    raise SystemExit(f"맵이 없다: {MAP}")

_T0 = time.time()


def tick(what):
    print(f"[기동 {time.time() - _T0:6.1f}s] {what}")
    sys.stdout.flush()


# ── Isaac 기동 ────────────────────────────────────────────────────────
# 창은 못 만든다(디스플레이 없음) — UI 는 오프스크린으로 그려 WebRTC 로 나간다.
from isaacsim import SimulationApp                              # noqa: E402

simulation_app = SimulationApp({"headless": True})
tick("SimulationApp 기동 완료")

import numpy as np                                              # noqa: E402
from isaacsim.core.utils.stage import open_stage                # noqa: E402
from pxr import Gf, Usd, UsdGeom, UsdLux                        # noqa: E402

open_stage(str(MAP))
import omni.usd                                                 # noqa: E402

stage = omni.usd.get_context().get_stage()
tick(f"맵 열기 완료: {MAP.name}")

# ── 골라 보이기 ───────────────────────────────────────────────────────
keep = PRESETS[ONLY]
root = stage.GetPrimAtPath("/World/Restroom")
if not root:
    raise SystemExit("/World/Restroom 이 없다 — 다른 구조의 맵이다")
shown = []
for prim in root.GetChildren():
    name = prim.GetName()
    if keep is None or name in keep:
        UsdGeom.Imageable(prim).MakeVisible()
        shown.append(name)
    else:
        UsdGeom.Imageable(prim).MakeInvisible()
print(f"[보이기] {ONLY}: {', '.join(shown)}"
      f"   (숨김 {len(root.GetChildren()) - len(shown)}개)")

# ── 보이는 것만의 경계상자 — 카메라 거리를 여기서 정한다 ──────────────
lo = np.full(3, +1e9)
hi = np.full(3, -1e9)
for prim in root.GetChildren():
    if keep is not None and prim.GetName() not in keep:
        continue
    for d in Usd.PrimRange(prim):
        if d.IsA(UsdGeom.Mesh):
            ext = UsdGeom.Mesh(d).GetExtentAttr().Get()
            if ext:
                lo = np.minimum(lo, np.array(ext[0], float))
                hi = np.maximum(hi, np.array(ext[1], float))
ctr = (lo + hi) / 2.0
span = float(np.max(hi - lo))
print(f"[범위] x {lo[0]:.3f}~{hi[0]:.3f}  y {lo[1]:.3f}~{hi[1]:.3f}  "
      f"z {lo[2]:.3f}~{hi[2]:.3f}   중심 {tuple(round(v, 3) for v in ctr)}  "
      f"최대변 {span:.3f} m")

# ── 조명 — 맵에 광원이 없다. 없으면 새까맣게 나온다 ───────────────────
lights = stage.DefinePrim("/World/ViewLights", "Xform")
dome = UsdLux.DomeLight.Define(stage, "/World/ViewLights/Dome")
dome.CreateIntensityAttr(900.0)
sun = UsdLux.DistantLight.Define(stage, "/World/ViewLights/Sun")
sun.CreateIntensityAttr(2200.0)
sun.CreateAngleAttr(1.0)
UsdGeom.Xformable(sun).AddRotateXYZOp().Set(Gf.Vec3f(-55.0, 12.0, 25.0))
UsdGeom.Imageable(lights).MakeVisible()
tick("조명 추가 (원본 USD 에는 쓰지 않는다)")

# ── 카메라 세 자리 — 배관은 위에서 본 그림이 경로를 가장 잘 보여 준다 ──
# 🔑 top 은 정확히 수직으로 두지 않는다 — up 축과 시선이 평행하면 롤이 불정해져
#    프레임마다 그림이 돌아 버린다. y 로 살짝 눕혀 고정한다.
VIEWS = {                          # 이름: (보는 방향 벡터, 초점거리 mm, 설명)
    "top": (np.array([0.0, -0.05, 1.0]), 30.0, "위에서 (경로)"),
    "iso": (np.array([0.75, -1.00, 0.55]), 24.0, "비스듬히"),
    "side": (np.array([0.0, -1.00, 0.08]), 30.0, "옆에서 (기울기)"),
}
# 🚨 거리를 "최대변 × 상수" 로 잡으면 **가늘고 긴 것이 잘린다.** 두 층을 같이
#    보면(--only pipes) z 로 2.8m 인데 x·y 는 1.4m 라, 최대변 기준 거리로는
#    위아래가 화면 밖으로 나간다(실제로 그렇게 잘렸다). 경계상자의 **대각
#    반지름**을 화각 안에 넣는 식으로 바꾼다 — 어느 방향에서 봐도 다 들어온다.
R = float(np.linalg.norm(hi - lo)) / 2.0
APERTURE = 15.2908                 # USD 카메라 기본 수직 aperture(mm). 좁은 쪽


def fit_distance(focal_mm, margin=1.12):
    half_fov = np.arctan(APERTURE / 2.0 / focal_mm)
    return max(R, 0.15) / np.sin(half_fov) * margin


def look_at(eye, target, up=(0, 0, 1)):
    """eye→target 을 보는 카메라 변환행렬. USD 카메라는 −Z 를 본다."""
    eye = np.asarray(eye, float)
    fwd = np.asarray(target, float) - eye
    fwd /= np.linalg.norm(fwd)
    up = np.asarray(up, float)
    right = np.cross(fwd, up)
    if np.linalg.norm(right) < 1e-6:                  # 시선이 up 과 평행
        right = np.cross(fwd, np.array([0.0, 1.0, 0.0]))
    right /= np.linalg.norm(right)
    true_up = np.cross(right, fwd)
    m = Gf.Matrix4d(1.0)
    for col, v in enumerate((right, true_up, -fwd)):  # −Z 가 시선
        for row in range(3):
            m[col, row] = float(v[row])
    m.SetTranslateOnly(Gf.Vec3d(*eye))
    return m


cams = {}
for key, (direction, focal, _label) in VIEWS.items():
    path = f"/World/ViewCams/{key}"
    dist = fit_distance(focal)
    eye = ctr + direction / np.linalg.norm(direction) * dist
    cam = UsdGeom.Camera.Define(stage, path)
    cam.CreateFocalLengthAttr(focal)
    cam.CreateClippingRangeAttr(Gf.Vec2f(0.01, float(dist * 4)))
    UsdGeom.Xformable(cam).AddTransformOp().Set(look_at(eye, ctr))
    cams[key] = path
    print(f"[카메라] {key:5s} 초점 {focal:4.0f}mm  거리 {dist:5.2f} m")
tick(f"카메라 {len(cams)}대 배치 (대각반지름 {R:.3f} m, 최대변 {span:.3f} m)")

if SHOT:
    # ── 그림 뜨기 ─────────────────────────────────────────────────────
    # replicator 로 카메라마다 렌더프로덕트를 만들어 rgb 를 받는다. RTX 는 몇
    # 프레임 누적해야 노이즈가 가라앉으므로 rt_subframes 를 넉넉히 준다.
    import omni.replicator.core as rep                          # noqa: E402
    from PIL import Image                                       # noqa: E402

    out_dir = Path(SHOT if isinstance(SHOT, str) else SON / "maps" / "views")
    out_dir.mkdir(parents=True, exist_ok=True)

    annots = {}
    for key, path in cams.items():
        rp = rep.create.render_product(path, RES)
        an = rep.AnnotatorRegistry.get_annotator("rgb")
        an.attach(rp)
        annots[key] = an
    for _ in range(3):
        rep.orchestrator.step(rt_subframes=24)
    tick("렌더 완료")

    for key, an in annots.items():
        rgba = np.asarray(an.get_data())
        if rgba.size == 0:
            print(f"⚠ {key}: 빈 프레임 — 렌더가 아직 안 붙었다")
            continue
        img = Image.fromarray(rgba[..., :3].astype("uint8"))
        f = out_dir / f"{MAP.stem}_{ONLY}_{key}.png"
        img.save(f)
        print(f"✅ {f}  ({img.width}x{img.height}, {VIEWS[key][2]})")
else:
    # ── 라이브 ────────────────────────────────────────────────────────
    # 첫 화면을 iso 로 맞춰 준다 — 안 맞추면 원점 밖을 보고 있어서 "아무것도
    # 안 뜬다" 로 보인다. 접속한 뒤에는 마우스로 자유롭게 돌리면 된다.
    try:
        from omni.kit.viewport.utility import get_active_viewport
        vp = get_active_viewport()
        if vp is not None:
            vp.camera_path = cams["iso"]
            print(f"[뷰포트] 카메라 = {cams['iso']}")
    except Exception as e:                    # 뷰포트가 없는 experience 일 때
        print(f"[뷰포트] 카메라 지정 생략: {e}")

    print("\n▶ WebRTC Streaming Client 로 접속해서 본다 "
          "(주소 칸에 인스턴스 퍼블릭 IP 만).")
    print("  Ctrl-C 로 종료.  다른 층: --only floor2 / 겹쳐 보기: --only pipes\n")
    sys.stdout.flush()
    t_end = (time.time() + _HOLD) if _HOLD else None
    try:
        while simulation_app.is_running():
            simulation_app.update()
            if t_end and time.time() > t_end:
                print("[종료] --hold 시간 경과")
                break
    except KeyboardInterrupt:
        print("\n[종료] Ctrl-C")

simulation_app.close()
tick("종료")
