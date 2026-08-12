<!-- source: utilities/debugging/ext_isaacsim_util_debug_draw.html | title: Debug Drawing Extension API — Isaac Sim Documentation -->

# Debug Drawing Extension API

## About
This Debug Drawing Extension API API is used to coordinate groups of lines and points on the screen. Use this API instead of Omniverse’s built-in debug drawing API to have greater control over how the geometry is drawn. The 3D geometry drawn by this remains persistent across frames and is only cleared when desired (unlike the built-in debug drawer).

## API Documentation
See the API Documentation for complete usage information.

## Tutorials & Examples
The following screenshots showcase how the different geometries are drawn:

### Points
Drawing batches of points with different RGBA and radius values:

```
1import random
2from isaacsim.util.debug_draw import _debug_draw
3
4draw = _debug_draw.acquire_debug_draw_interface()
5
6N = 10000
7point_list_1 = [
8 (random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(N)
9]
10point_list_2 = [
11 (random.uniform(-10, 10), random.uniform(10, 30), random.uniform(-10, 10)) for _ in range(N)
12]
13point_list_3 = [
14 (random.uniform(-10, 10), random.uniform(-30, -10), random.uniform(-10, 10)) for _ in range(N)
15]
16colors = [(random.uniform(0.5, 1), random.uniform(0.5, 1), random.uniform(0.5, 1), 1) for _ in range(N)]
17sizes = [random.randint(1, 50) for _ in range(N)]
18draw.draw_points(point_list_1, [(1, 0, 0, 1)] * N, [10] * N)
19draw.draw_points(point_list_2, [(0, 1, 0, 1)] * N, [10] * N)
20draw.draw_points(point_list_3, colors, sizes)
```

[image: Draw Points]

### Lines
Drawing batches of lines with different RGBA and width values:

```
1import random
2from isaacsim.util.debug_draw import _debug_draw
3
4draw = _debug_draw.acquire_debug_draw_interface()
5
6N = 10000
7point_list_1 = [
8 (random.uniform(10, 30), random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(N)
9]
10point_list_2 = [
11 (random.uniform(10, 30), random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(N)
12]
13colors = [(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1), 1) for _ in range(N)]
14sizes = [random.randint(1, 25) for _ in range(N)]
15draw.draw_lines(point_list_1, point_list_2, colors, sizes)
```

[image: Draw Lines]

### Splines
Drawing splines as filled or dashed between a set of points:

```
1import random
2from isaacsim.util.debug_draw import _debug_draw
3
4draw = _debug_draw.acquire_debug_draw_interface()
5
6point_list_1 = [
7 (random.uniform(-30, -10), random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(10)
8]
9draw.draw_lines_spline(point_list_1, (1, 1, 1, 1), 10, False)
10point_list_2 = [
11 (random.uniform(-30, -10), random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(10)
12]
13draw.draw_lines_spline(point_list_2, (1, 1, 1, 1), 1, True)
```

[image: Draw Splines]
