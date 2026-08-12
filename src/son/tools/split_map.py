"""[오프라인] 맵 USD 에서 층별 배관만 뽑아 단독 USD 로 뜬다. Isaac 불필요.

    python3 tools/split_map.py                       # 기본 맵 → floor1/floor2 배관
    python3 tools/split_map.py --list                # 어떤 프림이 있는지만 본다
    python3 tools/split_map.py --part Floor1_Pipes Floor1_Sump --out 1층.usda

🎯 **자르는 작업이 아니다.** `restroom_map_straight290.usda` 는 이미 층별로
   프림이 갈라져 있다(`Floor1_Pipes` / `Floor2_Pipes` / `..._Room` / `Aisle_*`).
   그래서 이 도구는 기하를 다시 계산하지 않고 **레이어 스펙을 그대로 복사**한다
   (`Sdf.CopySpec`). 정점이 한 개도 바뀌지 않으니 분리본으로 잰 치수는 원본으로
   잰 것과 같다 — 분리본에서 확인한 결함을 원본 좌표로 그대로 쓸 수 있다.

🚨 **원본은 절대 덮어쓰지 않는다** (`fix_map.py` 와 같은 규칙). Isaac GUI 에서
   맵 USD 에 저장했다가 형상 없는 껍데기가 원본을 날린 사고가 기록돼 있다.
   출력 파일이 이미 있으면 `--force` 없이는 멈춘다.

같이 담는 것: 배관을 복사하면 그것이 물고 있는 머티리얼(`/World/Looks/Pipe`,
`/World/Looks_PhysicsMaterials/PipeSteel`)도 함께 담는다. 안 담으면 relationship
이 끊긴 프림이 되어 Isaac 이 회색 기본 재질로 그린다.

⚠ 이 맵은 `metersPerUnit 1.0` **(m)** 이다. 예전 실전 맵(`restroom_pipe150_
   final_fixed.usd`)은 0.001(mm) 이었다 — 스테이지에 얹을 때 scale 0.001 을
   주던 관례를 이 맵에 그대로 쓰면 관이 1/1000 로 쪼그라든다. 분리본은 원본의
   단위 메타데이터를 그대로 물려받으므로 여기서도 m 이다.
"""

import argparse
import sys
from pathlib import Path

from pxr import Sdf, Usd, UsdGeom

SON = Path(__file__).resolve().parent.parent
DEFAULT_MAP = SON / "maps" / "restroom_map_straight290.usda"

# 배관을 복사하면 딸려가야 하는 것들 — 없으면 재질이 끊긴다.
LOOKS = ["/World/Looks", "/World/Looks_PhysicsMaterials"]

# 기본 분리 대상. 이름은 맵의 프림 이름 그대로다.
PRESETS = {
    "floor1": ["Floor1_Pipes"],
    "floor2": ["Floor2_Pipes"],
}


def parts_of(stage):
    """/World/Restroom 아래의 부품 프림 이름과 크기를 훑는다."""
    out = []
    root = stage.GetPrimAtPath("/World/Restroom")
    if not root:
        raise SystemExit("/World/Restroom 이 없다 — 다른 구조의 맵인가?")
    for prim in root.GetChildren():
        pts = tris = 0
        for d in Usd.PrimRange(prim):
            if d.IsA(UsdGeom.Mesh):
                m = UsdGeom.Mesh(d)
                pts += len(m.GetPointsAttr().Get() or [])
                tris += len(m.GetFaceVertexCountsAttr().Get() or [])
        ext = None
        for d in Usd.PrimRange(prim):
            if d.IsA(UsdGeom.Mesh):
                ext = UsdGeom.Mesh(d).GetExtentAttr().Get()
                break
        out.append((prim.GetName(), pts, tris, ext))
    return out


def split(src_path, names, out_path, force=False):
    """`names` 프림만 담은 단독 USD 를 만든다. 원본은 읽기만 한다."""
    src = Sdf.Layer.FindOrOpen(str(src_path))
    if src is None:
        raise SystemExit(f"USD 를 못 열었다: {src_path}")
    if out_path.exists() and not force:
        raise SystemExit(f"이미 있다 (덮어쓰려면 --force): {out_path}")

    dst = Sdf.Layer.CreateNew(str(out_path))
    # 단위·업축·defaultPrim 을 원본에서 그대로 가져온다 (m/Z 유지).
    # 🚨 단위를 안 옮기면 분리본이 metersPerUnit 기본값(0.01)으로 읽혀 관이
    #    100배로 들어온다 — 분리본만 열어 보면 멀쩡해 보여서 알아채기 어렵다.
    for key in ("metersPerUnit", "upAxis"):
        if src.pseudoRoot.HasInfo(key):
            dst.pseudoRoot.SetInfo(key, src.pseudoRoot.GetInfo(key))
    if src.defaultPrim:
        dst.defaultPrim = src.defaultPrim
    dst.documentation = (
        f"{src_path.name} 에서 {', '.join(names)} 만 분리한 사본 "
        f"(tools/split_map.py). 좌표·정점은 원본과 동일하다.")

    copied = []
    for path in LOOKS + [f"/World/Restroom/{n}" for n in names]:
        sp = Sdf.Path(path)
        if not src.GetPrimAtPath(sp):
            if path in LOOKS:
                continue                      # 머티리얼 없는 맵도 있을 수 있다
            raise SystemExit(f"그런 프림이 없다: {path}  (--list 로 확인)")
        # 부모 스펙(World, Restroom)을 먼저 만들어 둬야 자식을 복사할 수 있다
        for anc in sp.GetPrefixes()[:-1]:
            if not dst.GetPrimAtPath(anc):
                parent = src.GetPrimAtPath(anc)
                Sdf.PrimSpec(                 # 생성자가 부모 레이어에 등록한다
                    dst.pseudoRoot if anc.pathElementCount == 1
                    else dst.GetPrimAtPath(anc.GetParentPath()),
                    anc.name, Sdf.SpecifierDef,
                    parent.typeName if parent else "Xform")
        Sdf.CopySpec(src, sp, dst, sp)
        copied.append(path)
    dst.Save()
    return copied


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("map", nargs="?", default=str(DEFAULT_MAP))
    ap.add_argument("--list", action="store_true", help="프림 목록만 출력")
    ap.add_argument("--part", nargs="+", metavar="NAME",
                    help="분리할 프림 이름 (기본: floor1/floor2 배관 각각)")
    ap.add_argument("--out", help="--part 와 함께 쓸 출력 경로")
    ap.add_argument("--force", action="store_true", help="출력 파일 덮어쓰기 허용")
    a = ap.parse_args(argv)

    src = Path(a.map).resolve()
    stage = Usd.Stage.Open(str(src))
    if stage is None:
        raise SystemExit(f"USD 를 못 열었다: {src}")

    print(f"원본  {src}")
    print(f"단위  metersPerUnit={UsdGeom.GetStageMetersPerUnit(stage)} "
          f"upAxis={UsdGeom.GetStageUpAxis(stage)}")
    print(f"{'프림':16s} {'정점':>7s} {'삼각형':>7s}  범위 (m)")
    for name, pts, tris, ext in parts_of(stage):
        rng = "" if ext is None else \
            f"  x {ext[0][0]:7.3f}~{ext[1][0]:7.3f}  " \
            f"y {ext[0][1]:7.3f}~{ext[1][1]:7.3f}  " \
            f"z {ext[0][2]:7.3f}~{ext[1][2]:7.3f}"
        print(f"{name:16s} {pts:7d} {tris:7d}{rng}")
    if a.list:
        return 0

    jobs = ([(a.part, Path(a.out).resolve())] if a.part else
            [(names, src.with_name(f"{src.stem}_{key}_pipes.usda"))
             for key, names in PRESETS.items()])
    if a.part and not a.out:
        raise SystemExit("--part 를 쓰면 --out 도 줘야 한다")

    print()
    for names, out in jobs:
        copied = split(src, names, out, a.force)
        size = out.stat().st_size / 1e6
        print(f"✅ {out.name:44s} {size:6.2f} MB  ← {', '.join(copied[-len(names):])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
