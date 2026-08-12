<!-- source: sensors/isaacsim_sensors_physics_articulation_force.html | title: Articulation Joint Sensors — Isaac Sim Documentation -->

# Articulation Joint Sensors
Articulation sensors allow reading the active and passive components of the joint forces. To read articulation joint forces you can use Articulation or ArticulationView APIs. See Robot Simulation Snippets for more details about the Articulation and the ArticulationView classes. Specifically,

- get_applied_joint_efforts API will return a tensor that specifies the efforts set by the user through the set_joint_efforts .

- get_measured_joint_forces API will return a tensor that specifies 6-dimensional spatial forces per joints for all articulations (total overall joint forces). To mimic force-torque sensors, this API can be used to retrieve forces from a fixed joint.

- get_measured_joint_efforts API will return a tensor which specifies the active components (the projection of the joint forces on the motion direction) of the joint forces for all the joints and articulations.

Note
In an articulation tree, each link can have a single parent link. The joint forces reported by `get_measured_joint_forces` and `get_measured_joint_efforts` APIs correspond to the forces, torques, or efforts exerted by the joint connecting the child link to the parent link. In short, the forces reported by these API denote the link incoming joints forces.

## GUI

### Script Editor
This section describes how to add and customize the articulation sensor through the Script Editor, opened from Window > Script Editor.

```
1from isaacsim.core.prims import SingleArticulation
2import asyncio
3from isaacsim.core.api import World
4from isaacsim.core.utils.stage import (
5 add_reference_to_stage,
6 create_new_stage_async,
7 get_current_stage,
8)
9from isaacsim.storage.native import get_assets_root_path
10from pxr import UsdPhysics
11
12async def joint_force():
13 World.clear_instance()
14 await create_new_stage_async()
15 my_world = World(stage_units_in_meters=1.0, backend="torch", device="cpu")
16 await my_world.initialize_simulation_context_async()
17 await omni.kit.app.get_app().next_update_async()
18 assets_root_path = get_assets_root_path()
19 asset_path = assets_root_path + "/Isaac/Robots/IsaacSim/Ant/ant.usd"
20 add_reference_to_stage(usd_path=asset_path, prim_path="/World/Ant")
21 await omni.kit.app.get_app().next_update_async()
22 my_world.scene.add_default_ground_plane()
23 arti_view = SingleArticulation("/World/Ant/torso")
24 my_world.scene.add(arti_view)
25 await my_world.reset_async(soft=False)
26 stage = get_current_stage()
27
28 sensor_joint_forces = arti_view.get_measured_joint_forces()
29 sensor_actuation_efforts = arti_view.get_measured_joint_efforts()
30 # Iterates through the joint names in the articulation, retrieves information about the joints and their associated links,
31 # and creates a mapping between joint names and their corresponding link indices.
32 joint_link_id = dict()
33 for joint_name in arti_view._articulation_view.joint_names:
34 joint_path = "/World/Ant/joints/" + joint_name
35 joint = UsdPhysics.Joint.Get(stage, joint_path)
36 body_1_path = joint.GetBody1Rel().GetTargets()[0]
37 body_1_name = stage.GetPrimAtPath(body_1_path).GetName()
38 child_link_index = arti_view._articulation_view.get_link_index(body_1_name)
39 joint_link_id[joint_name] = child_link_index
40
41 print("joint link IDs", joint_link_id)
42 print(sensor_joint_forces[joint_link_id["front_left_leg"]])
43 print(sensor_actuation_efforts[joint_link_id["front_left_leg"]])
44
45asyncio.ensure_future(joint_force())
```
