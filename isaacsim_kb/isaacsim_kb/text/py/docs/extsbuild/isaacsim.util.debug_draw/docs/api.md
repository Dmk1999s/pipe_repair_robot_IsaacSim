<!-- source: py/docs/extsbuild/isaacsim.util.debug_draw/docs/api.html | title: API — Isaac Sim -->

# API

## Python API

[TABLE]
DebugDraw |
[/TABLE]

### Debug Drawing
This submodule provides bindings to draw debug lines and points
Point Example:
drawn points to the screen with random colors and sizes

```
import random
from isaacsim.util.debug_draw import _debug_draw
draw = _debug_draw.acquire_debug_draw_interface()
N = 10000
point_list_1 = [
(random.uniform(-1000, 1000), random.uniform(-1000, 1000), random.uniform(-1000, 1000)) for _ in range(N)
]
point_list_2 = [
(random.uniform(-1000, 1000), random.uniform(1000, 3000), random.uniform(-1000, 1000)) for _ in range(N)
]
point_list_3 = [
(random.uniform(-1000, 1000), random.uniform(-3000, -1000), random.uniform(-1000, 1000)) for _ in range(N)
]
colors = [(random.uniform(0.5, 1), random.uniform(0.5, 1), random.uniform(0.5, 1), 1) for _ in range(N)]
sizes = [random.randint(1, 50) for _ in range(N)]
draw.draw_points(point_list_1, [(1, 0, 0, 1)] * N, [10] * N)
draw.draw_points(point_list_2, [(0, 1, 0, 1)] * N, [10] * N)
draw.draw_points(point_list_3, colors, sizes)
```

Line Example:
drawn lines to the screen with random colors and widths

```
import random
from isaacsim.util.debug_draw import _debug_draw
draw = _debug_draw.acquire_debug_draw_interface()
N = 10000
point_list_1 = [
(random.uniform(1000, 3000), random.uniform(-1000, 1000), random.uniform(-1000, 1000)) for _ in range(N)
]
point_list_2 = [
(random.uniform(1000, 3000), random.uniform(-1000, 1000), random.uniform(-1000, 1000)) for _ in range(N)
]
colors = [(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1), 1) for _ in range(N)]
sizes = [random.randint(1, 25) for _ in range(N)]
draw.draw_lines(point_list_1, point_list_2, colors, sizes)
```

Spline Example:
drawn splines to the screen with random colors and widths

```
from isaacsim.util.debug_draw import _debug_draw
draw = _debug_draw.acquire_debug_draw_interface()
point_list_1 = [
(random.uniform(-300, -100), random.uniform(-100, 100), random.uniform(-100, 100)) for _ in range(10)
]
draw.draw_lines_spline(point_list_1, (1, 1, 1, 1), 10, False)
point_list_2 = [
(random.uniform(-300, -100), random.uniform(-100, 100), random.uniform(-100, 100)) for _ in range(10)
]
draw.draw_lines_spline(point_list_2, (1, 1, 1, 1), 5, True)
```

classDebugDraw
Bases: `pybind11_object`
clear_lines(
self:isaacsim.util.debug_draw._debug_draw.DebugDraw ,
)→None Clear lines

clear_points(
self:isaacsim.util.debug_draw._debug_draw.DebugDraw ,
)→None Clear points

draw_lines(
self:isaacsim.util.debug_draw._debug_draw.DebugDraw ,
arg0:List[carb::Float3],
arg1:List[carb::Float3],
arg2:List[carb::ColorRgba],
arg3:List[float],
)→None Draw a set of lines to the screen

draw_lines_spline(self:isaacsim.util.debug_draw._debug_draw.DebugDraw,arg0:List[carb::Float3],arg1:carb::ColorRgba,arg2:float,arg3:bool)→None
Draw spline between a list of points as line segments

draw_points(
self:isaacsim.util.debug_draw._debug_draw.DebugDraw ,
arg0:List[carb::Float3],
arg1:List[carb::ColorRgba],
arg2:List[float],
)→None Draw a set of points to the screen

get_num_lines(
self:isaacsim.util.debug_draw._debug_draw.DebugDraw ,
)→intReturn the current number of lines being drawn

get_num_points(
self:isaacsim.util.debug_draw._debug_draw.DebugDraw ,
)→intReturn the current number of points being drawn

acquire_debug_draw_interface(
plugin_name:str=None,
library_path:str=None,
)→isaacsim.util.debug_draw._debug_draw.DebugDraw release_debug_draw_interface(
arg0:isaacsim.util.debug_draw._debug_draw.DebugDraw ,
)→None
