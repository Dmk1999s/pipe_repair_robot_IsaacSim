<!-- source: sensors/isaacsim_sensors_physics_proximity.html | title: Proximity Sensor — Isaac Sim Documentation -->

# Proximity Sensor
The Proximity Sensor is a wrapper around a physics callback that can be attached to any prim in the scene. During simulation execution, the sensor will record collisions between the prim it’s attached to and other prims in the scene each frame; that data can be accessed using a callback function.

## Standalone Python
Execute the following script using `python.sh`. This will create a scene with two cubes, attaching a proximity sensor to one of the cubes. At the start of the simulation, the two cubes will overlap and then move apart; the callback function in the script will print the proximity sensor’s output to the screen.

```
1import numpy as np
2
3from isaacsim import SimulationApp
4
5simulation_app = SimulationApp({"headless": False})
6
7import carb
8import omni
9from isaacsim.core.api.objects import DynamicCuboid, GroundPlane
10from isaacsim.core.api.world import World
11from isaacsim.core.utils.extensions import enable_extension
12from isaacsim.core.utils.prims import get_prim_at_path
13from pxr import Sdf, UsdLux
14
15# Set up scene
16world = World()
17ground_plane = GroundPlane('/World/GroundPlane')
18
19# Add lighting
20stage = omni.usd.get_context().get_stage()
21distantLight = UsdLux.DistantLight.Define(stage, Sdf.Path("/DistantLight"))
22distantLight.CreateIntensityAttr(500)
23
24# Add cubes
25cube_1 = DynamicCuboid(
26 prim_path="/cube_1",
27 name="cube_1",
28 position=np.array([0.4, 0, 5.0]),
29 scale=np.array([1, 1, 1]),
30 size=1.0,
31 color=np.array([255, 0, 0]),
32 )
33
34cube_2 = DynamicCuboid(
35 prim_path="/cube_2",
36 name="cube_2",
37 position=np.array([-0.4, 0, 5.0]),
38 scale=np.array([1, 1, 1]),
39 size=1.0,
40 color=np.array([0, 0, 255]),
41 )
42
43# Enable isaacsim.sensors.physx extension
44enable_extension("isaacsim.sensors.physx")
45simulation_app.update()
46
47# Attach sensor to cube 1
48from isaacsim.sensors.physx import ProximitySensor, register_sensor, clear_sensors
49s = ProximitySensor(cube_1.prim)
50register_sensor(s)
51
52# Add callback to print proximity sensor data
53def print_proximity_sensor_data_on_update(_):
54 data = s.get_data()
55 if '/cube_2' in data:
56 # /cube_1 is colliding with /cube_2
57 distance = data['/cube_2']["distance"]
58 duration = data['/cube_2']["duration"]
59 carb.log_warn(f"distance: {distance}, duration: {duration}")
60
61
62# Play simulation
63world.add_physics_callback("print_sensor_data", print_proximity_sensor_data_on_update)
64simulation_app.update()
65simulation_app.update()
66world.play()
67
68for i in range(100):
69 # Run with a fixed step size
70 world.step(render=True)
```
Example proximity sensor output is shown below; there might be small numerical differences in your output run-to-run.

```
distance: 0.8995118804137266, duration: 0.03952527046203613
distance: 0.9490971672498862, duration: 0.04244112968444824
distance: 0.9978315307718298, duration: 0.045195579528808594
distance: 1.0952793930211249, duration: 0.00010466575622558594
distance: 1.0952880909233123, duration: 0.004382610321044922
distance: 1.0952874949586842, duration: 0.008539199829101562
distance: 1.095288806188406, duration: 0.012722015380859375
```
After the cubes land, the scene will look like below:
[image: ../_images/isaac_proximity_sensor_example.png]
