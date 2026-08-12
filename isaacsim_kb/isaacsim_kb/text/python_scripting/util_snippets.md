<!-- source: python_scripting/util_snippets.html | title: Util Snippets — Isaac Sim Documentation -->

# Util Snippets

## Simple Async Task

```
1import asyncio
2import omni
3
4# Async task that pauses simulation once the incoming task is complete
5async def pause_sim(task):
6 done, pending = await asyncio.wait({task})
7 if task in done:
8 print("Waited until next frame, pausing")
9 omni.timeline.get_timeline_interface().pause()
10
11# Start simulation, then wait a frame and run the pause_sim task
12omni.timeline.get_timeline_interface().play()
13task = asyncio.ensure_future(omni.kit.app.get_app().next_update_async())
14asyncio.ensure_future(pause_sim(task))
```

## Get Camera Parameters
The below script show how to get the camera parameters associated with a viewport.

```
1import omni
2from omni.syntheticdata import helpers
3import math
4
5stage = omni.usd.get_context().get_stage()
6viewport_api = omni.kit.viewport.utility.get_active_viewport()
7# Set viewport resolution, changes will occur on next frame
8viewport_api.set_texture_resolution((512, 512))
9# get resolution
10(width, height) = viewport_api.get_texture_resolution()
11aspect_ratio = width / height
12# get camera prim attached to viewport
13camera = stage.GetPrimAtPath(viewport_api.get_active_camera())
14focal_length = camera.GetAttribute("focalLength").Get()
15horiz_aperture = camera.GetAttribute("horizontalAperture").Get()
16vert_aperture = camera.GetAttribute("verticalAperture").Get()
17# Pixels are square so we can also do:
18# vert_aperture = height / width * horiz_aperture
19near, far = camera.GetAttribute("clippingRange").Get()
20fov = 2 * math.atan(horiz_aperture / (2 * focal_length))
21# helper to compute projection matrix
22proj_mat = helpers.get_projection_matrix(fov, aspect_ratio, near, far)
23
24# compute focal point and center
25focal_x = height * focal_length / vert_aperture
26focal_y = width * focal_length / horiz_aperture
27center_x = height * 0.5
28center_y = width * 0.5
```

## Rendering
There are three primary APIs you should use when making frequent updates to large amounts of geometry: `UsdGeom.Points`, `UsdGeom.PointInstancer`, and `DebugDraw`. The different advantages and limitations of each of these methods are explained below, and can help guide you on which method to use.

### UsdGeom.Points
Use the `UsdGeom.Points` API when the geometry needs to interact with the renderer. The `UsdGeom.Points` API is the most efficient method to render large amounts of point geometry.

```
1import random
2import omni.usd
3from pxr import UsdGeom
4class Example():
5 def create(self):
6 # Create Point List
7 N = 500
8 self.point_list = [(random.uniform(-2.0, 2.0), random.uniform(-0.1, 0.1), random.uniform(-1.0, 1.0)) for _ in range(N)]
9 self.sizes = [.05 for _ in range(N)]
10
11 points_path = "/World/Points"
12 stage = omni.usd.get_context().get_stage()
13 self.points = UsdGeom.Points.Define(stage, points_path)
14 self.points.CreatePointsAttr().Set(self.point_list)
15 self.points.CreateWidthsAttr().Set(self.sizes)
16 self.points.CreateDisplayColorPrimvar("constant").Set([(1, 0, 1)])
17
18 def update(self):
19 # modify the point list
20 for i in range(len(self.point_list)):
21 self.point_list[i] = (random.uniform(-2.0, 2.0), random.uniform(-0.1, 0.1), random.uniform(-1.0, 1.0))
22 # update the points
23 self.points.GetPointsAttr().Set(self.point_list)
24
25import asyncio
26import omni
27example = Example()
28example.create()
29
30async def update_points():
31 # Update 10 times, waiting 10 frames between each update
32 for _ in range(10):
33 for _ in range(10):
34 await omni.kit.app.get_app().next_update_async()
35 example.update()
36
37asyncio.ensure_future(update_points())
```

[image: Output when using UsdGeom.Points]

### UsdGeom.PointInstancer
Use the `UsdGeom.PointInstancer` API when the geometry needs to interact with the physics scene. The `UsdGeom.PointInstancer` API lets you efficiently replicate an instance of a prim — with all of its USD properties — and update all instances with a list of positions, colors, and sizes.
See the PointInstancer Reference for more information regarding the PointInstancer API.
Below are code snippets for how to create and update geometry with `UsdGeom.PointInstancer`:

```
1import random
2import omni.usd
3from pxr import UsdGeom, Gf
4import random
5
6class Example():
7 def create(self):
8 # Create Point List
9 N = 500
10 scale = 0.05
11 self.point_list = [(random.uniform(-2.0, 2.0), random.uniform(-0.1, 0.1), random.uniform(-1.0, 1.0)) for _ in range(N)]
12 self.colors = [(1, 1, 1, 1) for _ in range(N)]
13 self.sizes = [(1.0,1.0,1.0) for _ in range(N)]
14
15 # Set up Geometry to be Instanced
16 cube_path = "/World/Cube"
17 stage = omni.usd.get_context().get_stage()
18 cube = UsdGeom.Cube(stage.DefinePrim(cube_path, "Cube"))
19 cube.AddScaleOp().Set(Gf.Vec3d(1, 1, 1) * scale)
20 cube.CreateDisplayColorPrimvar().Set([(0, 1, 1)])
21 # Set up Point Instancer
22
23 instance_path = "/World/PointInstancer"
24 self.point_instancer = UsdGeom.PointInstancer(stage.DefinePrim(instance_path, "PointInstancer"))
25 # Create & Set the Positions Attribute
26 self.positions_attr = self.point_instancer.CreatePositionsAttr()
27 self.positions_attr.Set(self.point_list)
28 self.scale_attr = self.point_instancer.CreateScalesAttr()
29 self.scale_attr.Set(self.sizes)
30 # Set the Instanced Geometry
31 self.point_instancer.CreatePrototypesRel().SetTargets([cube.GetPath()])
32
33 self.proto_indices_attr = self.point_instancer.CreateProtoIndicesAttr()
34 self.proto_indices_attr.Set([0] * len(self.point_list))
35
36 def update(self):
37 # modify the point list
38 for i in range(len(self.point_list)):
39 self.point_list[i] = (random.uniform(-2.0, 2.0), random.uniform(-0.1, 0.1), random.uniform(-1.0, 1.0))
40 # update the points
41 self.positions_attr.Set(self.point_list)
42
43import asyncio
44import omni
45example = Example()
46example.create()
47
48async def update_points():
49 # Update 10 times, waiting 10 frames between each update
50 for _ in range(10):
51 for _ in range(10):
52 await omni.kit.app.get_app().next_update_async()
53 example.update()
54
55asyncio.ensure_future(update_points())
```

[image: Output when using UsdGeom.PointInstancer]

### DebugDraw
The Debug Drawing Extension API API is useful for purely visualizing geometry in the Viewport. Geometry drawn with the `debug_draw_interface` cannot be rendered and does not interact with the physics scene. However, it is the most performance-efficient method of visualizing geometry.
See the API documentation for complete usage information.

Below are code snippets for how to create and update geometry visualed with `DebugDraw`:

```
1import random
2from isaacsim.util.debug_draw import _debug_draw
3
4class Example():
5 def create(self):
6 self.draw = _debug_draw.acquire_debug_draw_interface()
7 N = 500
8 self.point_list = [(random.uniform(-2.0, 2.0), random.uniform(-0.1, 0.1), random.uniform(-1.0, 1.0)) for _ in range(N)]
9 self.color_list = [(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1), 1) for _ in range(N)]
10 self.size_list = [10.0 for _ in range(N)]
11
12 def update(self):
13 # modify the point list
14 for i in range(len(self.point_list)):
15 self.point_list[i] = (random.uniform(-2.0, 2.0), random.uniform(-0.1, 0.1), random.uniform(-1.0, 1.0))
16
17 # draw the points
18 self.draw.clear_points()
19 self.draw.draw_points(self.point_list, self.color_list, self.size_list)
20
21import asyncio
22import omni
23example = Example()
24example.create()
25
26async def update_points():
27 # Update 10 times, waiting 10 frames between each update
28 for _ in range(10):
29 for _ in range(10):
30 await omni.kit.app.get_app().next_update_async()
31 example.update()
32
33asyncio.ensure_future(update_points())
```

[image: Output when using isaacsim.util.debug_draw]

### Rendering Frame Delay
The default rendering pipeline in the app experiences have upto 3 frames in flight to be rendered, which results in higher FPS since the simulation is not blocked until the latest state is rendered completely.
For applications that need the rendered data to correspond to the latest simulation state with no delay, the following experience file should be used `apps/omni.isaac.sim.zero_delay.python.kit`. Below is an example of how to use the experience file in a standlone workflow.

```
SimulationApp({"headless": True}, experience="apps/omni.isaac.sim.zero_delay.python.kit")
```
Alternatively, if you would like to use the specific settings instead, you can set them with extra_args as well:

```
SimulationApp(
{
"headless": True,
"extra_args": [
"--/app/hydraEngine/waitIdle=1",
"--/app/updateOrder/checkForHydraRenderComplete=1000",
"--/exts/isaacsim.ros2.bridge/publish_multithreading_disabled=1",
],
},
)
```
