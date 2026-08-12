<!-- source: sensors/isaacsim_sensors_rtx.html | title: RTX Sensors — Isaac Sim Documentation -->

# RTX Sensors
RTX sensors in Isaac Sim use the Omniverse RTX Renderer’s RTX Sensor SDK to sense the environment, enabling interaction with materials in visual and non-visual spectra. This means an RTX-based Lidar can model returns from light interaction with transparent or reflective surfaces, and an RTX-based Radar can model returns accounting for material emissivity and reflectivity in the radio spectrum.
Isaac Sim organizes utilities supporting RTX sensors into the `isaacsim.sensors.rtx` extension, which includes the following sensors:
RTX sensors are built using the `omni.sensors` extension suite. To understand more about how RTX sensors are modeled, and how to build your own, review the following documentation:

- Omniverse Common Extension

- Omniverse Lidar Extension

- Omniverse Radar Extension

- Omniverse Materials Extension

## Motion BVH
RTX sensors use Motion BVH to improve accuracy when modeling motion-related sensor effects, for example, the motion of objects during sensor exposure, or the motion of the sensor itself as it collects data.
By default, Motion BVH is disabled in Isaac Sim to improve performance. The following RTX Sensor features are affected by Motion BVH:

- RTX Lidar

- Motion BVH must be enabled for RTX Lidar motion compensation to work correctly.

- RTX Radar

- Motion BVH must be enabled for the Doppler effect, and therefore RTX Radar entirely, to be modeled correctly.

### How to Enable Motion BVH
Note
Enabling Motion BVH can significantly increase rendering time by increasing VRAM usage for all sensors and must be left disabled when not needed.
There are two ways to enable Motion BVH:

- In standalone Python workflows, you can enable Motion BVH by specifying `enable_motion_bvh` as `True` in the `SimulationApp` constructor:

```
from isaacsim import SimulationApp

simulation_app = SimulationApp({"enable_motion_bvh": True})
```

- In all workflows, you can enable Motion BVH by specifying the following settings on the command line:

```
--/renderer/raytracingMotion/enabled=true \
--/renderer/raytracingMotion/enableHydraEngineMasking=true \
--/renderer/raytracingMotion/enabledForHydraEngines='0,1,2,3,4'
```
