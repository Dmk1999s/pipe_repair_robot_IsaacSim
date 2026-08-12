<!-- source: py/source/extensions/isaacsim.replicator.domain_randomization/docs/index.html | title: [isaacsim.replicator.domain_randomization] Isaac Sim Replicator Domain Randomization — Isaac Sim -->

# [isaacsim.replicator.domain_randomization] Isaac Sim Replicator Domain Randomization
Version: 1.0.16
The extension provides various Domain Randomization scripts and OmniGraph nodes for randomizing simulation environments.

## Enable Extension
The extension can be enabled (if not already) in one of the following ways:

## Reinforcement Learning Domain Randomization
The following methods provide randomization functionalities of various parameters pertaining to `isaacsim.core.prims.RigidPrim`, `isaacsim.core.prims.Articulation`, and `isaacsim.core.api.SimulationContext`. These methods are designed to perform randomizations in simulations where update to USD is disabled for faster simulation speed. These methods directly set randomized values to PhysX as opposed to existing methods in omni.replicator.core, such as `omni.replicator.core.modify.pose` or `omni.replicator.core.physics.physics_material`, which utilizes USD APIs to set values and hence cannot be used when update to USD is disabled. Therefore, the following methods provided in `isaacsim.replicator.domain_randomization` are particularly useful for domain randomization in Reinforcement Learning (RL) as RL use cases benefit immensely from disabling update to USD to achieve faster simulation speed.
The following is a simple demo that showcases the workflow and the various features of `isaacsim.replicator` for domain randomization. This demo script can be launched as a standalone example, which can be found by going to Isaac Sim’s root directory and go to `standalone_examples/api/isaacsim.replicator.domain_randomization/randomization_demo.py`.
The `isaacsim.replicator` extension for domain randomization functions by constructing an OmniGraph action graph, which consists of nodes that generate random values, regulate frequency intervals of various randomization properties, and write the random values to PhysX. This action graph gets executed according to the way in which the triggers are set up. Note that it is necessary to register the views to be randomized before constructing this action graph.
The first step is to create an entry point of the action graph using `with dr.trigger.on_rl_frame(num_envs=num_envs):`. It is worth noting that all views to be used with this extension must have the same number of encapsulated prims, equaling `num_envs` that is passed as an argument to the `on_rl_frame` trigger.
After creating this entry point, there are two types of gates that determine when the nodes can write to PhysX: `on_interval(interval)` and `on_env_reset()`; these gates work in conjunction with `isaacsim.replicator.physics_view.step_randomization(reset_inds)`. There exists an internal step counter for every environment in the views. Every time the `step_randomization` method is called, it resets the counter to zero for every environment listed in the `reset_inds` argument while incrementing the counter for every other environment. The `on_interval(interval)` gate then ensures the nodes to write to PhysX whenever the counter for an environment is a multiple of the `interval` argument. The `on_env_reset()` gate writes to PhysX whenever an environment’s counter gets reset by the `reset_inds` argument passed in the `step_randomization` method.
Within each gate, the following methods can be used to randomize view properties: `randomize_simulation_context`, `randomize_rigid_prim_view` and `randomize_articulation_view`. For each of these methods, there exists an `operation` argument, which can be set to `direct`, `additive`, or `scaling`. `direct` sets the random values directly to PhysX, while the behavior of `additive` and `scaling` depends on the gate it is controlled by. Under `on_env_reset()`, `additive` adds the random values to the default values of a given attribute of the view, and `scaling` multiplies the random values to the default values. Under `on_interval(interval)`, `additive` and `scaling` adds or multiplies the random values to the last values set during `on_env_reset()`. In essence, `on_env_reset()` randomization should be treated as correlated noise that lasts until the next reset, while `on_interval(interval)` randomization should be treated as uncorrelated noise.
After setting up this action graph, it is necessary to run `omni.replicator.core.orchestrator.run()`.

```
from isaacsim import SimulationApp
simulation_app = SimulationApp({"headless": False})

import numpy as np
from isaacsim.core.api import World
from isaacsim.core.prims import Articulation, RigidPrim
from isaacsim.core.utils.prims import get_prim_at_path, define_prim
from isaacsim.core.utils.stage import get_current_stage, add_reference_to_stage
from isaacsim.storage.native import get_assets_root_path
from isaacsim.core.api.objects import DynamicSphere
from isaacsim.core.cloner import GridCloner

# create the world
world = World(stage_units_in_meters=1.0, physics_prim_path="/physicsScene", backend="numpy")
world.scene.add_default_ground_plane()

# set up grid cloner
cloner = GridCloner(spacing=1.5)
cloner.define_base_env("/World/envs")
define_prim("/World/envs/env_0")

# set up the first environment
DynamicSphere(prim_path="/World/envs/env_0/object", radius=0.1, position=np.array([0.75, 0.0, 0.2]))
add_reference_to_stage(
usd_path=get_assets_root_path()+ "/Isaac/Robots/Franka/franka.usd",
prim_path="/World/envs/env_0/franka",
)

# clone environments
num_envs = 4
prim_paths = cloner.generate_paths("/World/envs/env", num_envs)
env_pos = cloner.clone(source_prim_path="/World/envs/env_0", prim_paths=prim_paths)

# creates the views and set up world
object_view = RigidPrim(prim_paths_expr="/World/envs/*/object", name="object_view")
franka_view = Articulation(prim_paths_expr="/World/envs/*/franka", name="franka_view")
world.scene.add(object_view)
world.scene.add(franka_view)
world.reset()

num_dof = franka_view.num_dof

# set up randomization with isaacsim.replicator, imported as dr
import isaacsim.replicator.domain_randomization as dr
import omni.replicator.core as rep

dr.physics_view.register_simulation_context(world)
dr.physics_view.register_rigid_prim_view(object_view)
dr.physics_view.register_articulation_view(franka_view)

with dr.trigger.on_rl_frame(num_envs=num_envs):
with dr.gate.on_interval(interval=20):
dr.physics_view.randomize_simulation_context(
operation="scaling",
gravity=rep.distribution.uniform((1, 1, 0.0), (1, 1, 2.0)),
)
with dr.gate.on_interval(interval=50):
dr.physics_view.randomize_rigid_prim_view(
view_name=object_view.name,
operation="direct",
force=rep.distribution.uniform((0, 0, 2.5), (0, 0, 5.0)),
)
with dr.gate.on_interval(interval=10):
dr.physics_view.randomize_articulation_view(
view_name=franka_view.name,
operation="direct",
joint_velocities=rep.distribution.uniform(tuple([-2]*num_dof), tuple([2]*num_dof)),
)
with dr.gate.on_env_reset():
dr.physics_view.randomize_rigid_prim_view(
view_name=object_view.name,
operation="additive",
position=rep.distribution.normal((0.0, 0.0, 0.0), (0.2, 0.2, 0.0)),
velocity=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
)
dr.physics_view.randomize_articulation_view(
view_name=franka_view.name,
operation="additive",
joint_positions=rep.distribution.uniform(tuple([-0.5]*num_dof), tuple([0.5]*num_dof)),
position=rep.distribution.normal((0.0, 0.0, 0.0), (0.2, 0.2, 0.0)),
)
rep.orchestrator.run()

frame_idx = 0
while simulation_app.is_running():
if world.is_playing():
reset_inds = list()
if frame_idx % 200 == 0:
# triggers reset every 200 steps
reset_inds = np.arange(num_envs)
dr.physics_view.step_randomization(reset_inds)
world.step(render=True)
frame_idx += 1
```

## API

### Python API

[TABLE]
scripts.trigger |
scripts.gate |
scripts.physics_view |
scripts.utils |
[/TABLE]

#### trigger
on_rl_frame(num_envs:int)
Parameters:
num_envs (int) – The number of environments corresponding to the number of prims encapsulated in the RigidPrimViews and ArticulationViews.

#### gate
on_env_reset()
on_interval(interval)
Parameters:
interval (int) – The frequency interval for randomization. The interval is incremented by isaacsim.replicator.domain_randomization.physics_view.step_randomization() call.

#### physics_view
randomize_articulation_view(
view_name:str,
operation:str='direct',
num_buckets:int=None,
stiffness:omni.replicator.core.utils.ReplicatorItem=None,
damping:omni.replicator.core.utils.ReplicatorItem=None,
joint_friction:omni.replicator.core.utils.ReplicatorItem=None,
position:omni.replicator.core.utils.ReplicatorItem=None,
orientation:omni.replicator.core.utils.ReplicatorItem=None,
linear_velocity:omni.replicator.core.utils.ReplicatorItem=None,
angular_velocity:omni.replicator.core.utils.ReplicatorItem=None,
velocity:omni.replicator.core.utils.ReplicatorItem=None,
joint_positions:omni.replicator.core.utils.ReplicatorItem=None,
joint_velocities:omni.replicator.core.utils.ReplicatorItem=None,
lower_dof_limits:omni.replicator.core.utils.ReplicatorItem=None,
upper_dof_limits:omni.replicator.core.utils.ReplicatorItem=None,
max_efforts:omni.replicator.core.utils.ReplicatorItem=None,
joint_armatures:omni.replicator.core.utils.ReplicatorItem=None,
joint_max_velocities:omni.replicator.core.utils.ReplicatorItem=None,
joint_efforts:omni.replicator.core.utils.ReplicatorItem=None,
body_masses:omni.replicator.core.utils.ReplicatorItem=None,
body_inertias:omni.replicator.core.utils.ReplicatorItem=None,
material_properties:omni.replicator.core.utils.ReplicatorItem=None,
tendon_stiffnesses:omni.replicator.core.utils.ReplicatorItem=None,
tendon_dampings:omni.replicator.core.utils.ReplicatorItem=None,
tendon_limit_stiffnesses:omni.replicator.core.utils.ReplicatorItem=None,
tendon_lower_limits:omni.replicator.core.utils.ReplicatorItem=None,
tendon_upper_limits:omni.replicator.core.utils.ReplicatorItem=None,
tendon_rest_lengths:omni.replicator.core.utils.ReplicatorItem=None,
tendon_offsets:omni.replicator.core.utils.ReplicatorItem=None,
)→None Parameters:

- view_name (str) – The name of a registered Articulation.

- operation (str) – Can be “direct”, “additive”, or “scaling”. “direct” means random values are directly written into the view. “additive” means random values are added to the default values. “scaling” means random values are multiplied to the default values.

- num_buckets (int) – Number of buckets to sample values from for material_properties randomization.

- stiffness (ReplicatorItem) – Randomizes the stiffness of the joints in the articulation prims.

- damping (ReplicatorItem) – Randomizes the damping of the joints in the articulation prims.

- joint_friction (ReplicatorItem) – Randomizes the friction of the joints in the articulation prims.

- position (ReplicatorItem) – Randomizes the root position of the prims.

- orientation (ReplicatorItem) – Randomizes the root orientation of the prims using euler angles (rad).

- linear_velocity (ReplicatorItem) – Randomizes the root linear velocity of the prims.

- angular_velocity (ReplicatorItem) – Randomizes the root angular velocity of the prims.

- velocity (ReplicatorItem) – Randomizes the root linear and angular velocity of the prims.

- joint_positions (ReplicatorItem) – Randomizes the joint positions of the articulation prims.

- joint_velocities (ReplicatorItem) – Randomizes the joint velocities of the articulation prims.

- lower_dof_limits (ReplicatorItem) – Randomizes the lower joint limits of the articulation prims.

- upper_dof_limits (ReplicatorItem) – Randomizes the upper joint limits of the articulation prims.

- max_efforts (ReplicatorItem) – Randomizes the maximum joint efforts of the articulation prims.

- joint_armatures (ReplicatorItem) – Randomizes the joint armatures of the articulation prims.

- joint_max_velocities (ReplicatorItem) – Randomizes the maximum joint velocities of the articulation prims.

- joint_efforts (ReplicatorItem) – Randomizes the joint efforts of the articulation prims.

- body_masses (ReplicatorItem) – Randomizes the mass of each body in the articulation prims. The replicator distribution takes in K values, where K is the number of bodies in the articulation.

- body_inertias (ReplicatorItem) – Randomizes the inertia of each body in the articulation prims. The replicator distribution takes in K * 3 values, where K is the number of bodies in the articulation.

- material_properties (ReplicatorItem) – Randomizes the material properties of the bodies in the articulation.

- tendon_stiffnesses (ReplicatorItem) – Randomizes the stiffnesses of the fixed tendons in the articulation. The replicator distribution takes in T values, where T is the number of tendons in the articulation.

- tendon_dampings (ReplicatorItem) – Randomizes the dampings of the fixed tendons in the articulation. The replicator distribution takes in T values, where T is the number of tendons in the articulation.

- tendon_limit_stiffnesses (ReplicatorItem) – Randomizes the limit stiffnesses of the fixed tendons in the articulation. The replicator distribution takes in T values, where T is the number of tendons in the articulation.

- tendon_lower_limits (ReplicatorItem) – Randomizes the lower limits of the fixed tendons in the articulation. The replicator distribution takes in T values, where T is the number of tendons in the articulation.

- tendon_upper_limits (ReplicatorItem) – Randomizes the upper limits of the fixed tendons in the articulation. The replicator distribution takes in T values, where T is the number of tendons in the articulation.

- tendon_rest_lengths (ReplicatorItem) – Randomizes the rest lengths of the fixed tendons in the articulation. The replicator distribution takes in T values, where T is the number of tendons in the articulation.

- tendon_offsets (ReplicatorItem) – Randomizes the offsets of the fixed tendons in the articulation. The replicator distribution takes in T values, where T is the number of tendons in the articulation.

randomize_rigid_prim_view(
view_name:str,
operation:str='direct',
num_buckets:int=None,
position:omni.replicator.core.utils.ReplicatorItem=None,
orientation:omni.replicator.core.utils.ReplicatorItem=None,
linear_velocity:omni.replicator.core.utils.ReplicatorItem=None,
angular_velocity:omni.replicator.core.utils.ReplicatorItem=None,
velocity:omni.replicator.core.utils.ReplicatorItem=None,
force:omni.replicator.core.utils.ReplicatorItem=None,
mass:omni.replicator.core.utils.ReplicatorItem=None,
inertia:omni.replicator.core.utils.ReplicatorItem=None,
material_properties:omni.replicator.core.utils.ReplicatorItem=None,
contact_offset:omni.replicator.core.utils.ReplicatorItem=None,
rest_offset:omni.replicator.core.utils.ReplicatorItem=None,
)→None Parameters:

- view_name (str) – The name of a registered RigidPrimView.

- operation (str) – Can be “direct”, “additive”, or “scaling”. “direct” means random values are directly written into the view. “additive” means random values are added to the default values. “scaling” means random values are multiplied to the default values.

- num_buckets (int) – Number of buckets to sample values from for material_properties randomization.

- position (ReplicatorItem) – Randomizes the position of the prims.

- orientation (ReplicatorItem) – Randomizes the orientation of the prims using euler angles (rad).

- linear_velocity (ReplicatorItem) – Randomizes the linear velocity of the prims.

- angular_velocity (ReplicatorItem) – Randomizes the angular velocity of the prims.

- velocity (ReplicatorItem) – Randomizes the linear and angular velocity of the prims.

- force (ReplicatorItem) – Applies a random force to the prims.

- mass (ReplicatorItem) – Randomizes the mass of the prims. CPU pipeline only.

- inertia (ReplicatorItem) – Randomizes the inertia of the prims. Takes in three values for the replicator distribution, corresponding to the diagonal elements of the inertia matrix. CPU pipeline only.

- material_properties (ReplicatorItem) – Takes in three values for the replicator distriution, corresponding to static friction, dynamic friction, and restitution.

- contact_offset (ReplicatorItem) – Randomizes the contact offset of the prims.

- rest_offset (ReplicatorItem) – Randomizes the rest offset of the prims.

randomize_simulation_context(
operation:str='direct',
gravity:omni.replicator.core.utils.ReplicatorItem=None,
)Parameters:

- operation (str) – Can be “direct”, “additive”, or “scaling”. “direct” means random values are directly written into the view. “additive” means random values are added to the default values. “scaling” means random values are multiplied to the default values.

- gravity (ReplicatorItem) – Randomizes the gravity vector of the simulation.

register_articulation_view(
articulation_view:Articulation ,
)→None Parameters:
articulation_view (Articulation ) – Registering the Articulation to be randomized.

register_rigid_prim_view(
rigid_prim_view:RigidPrim ,
)→None Parameters:
rigid_prim_view (isaacsim.core.prims.RigidPrim ) – Registering the RigidPrim to be randomized.

register_simulation_context(
simulation_context:SimulationContext |World ,
)→None Parameters:
simulation_context (Union[isaacsim.core.api.SimulationContext, isaacsim.core.api.World]) – Registering the SimulationContext.

step_randomization(
reset_inds:list|ndarray|Tensor|None =[],
)→None Parameters:
reset_inds (Optional[Union[list, np.ndarray, torch.Tensor]]) – The indices corresonding to the prims to be reset in the views.

#### utils
classNumpyEncoder(
*,
skipkeys=False,
ensure_ascii=True,
check_circular=True,
allow_nan=True,
sort_keys=False,
indent=None,
separators=None,
default=None,
)Bases: `JSONEncoder`
default(obj)
Implement this method in a subclass such that it returns a serializable object for `o`, or calls the base implementation (to raise a `TypeError`).
For example, to support arbitrary iterators, you could implement default like this:

```
def default(self, o):
try:
iterable = iter(o)
except TypeError:
pass
else:
return list(iterable)
# Let the base class default method raise the TypeError
return super().default(o)
```

calculate_truncation_ratio_simple(corners, img_width, img_height)
Calculate the truncation ratio of a cuboid using a simplified bounding box method. :param corners: (9, 2) numpy array containing the projected corners of the cuboid. :param img_width: width of image :param img_height: height of image
Returns:
The truncation ratio of the cuboid. 1 means object is fully truncated and 0 means object is fully within screen.

get_distribution_params(
distribution:omni.replicator.core.utils.ReplicatorItem,
parameters:List[str],
)→ListParameters:

- distribution (ReplicatorItem) – A replicator distribution object.

- parameters (List[str]) – A list of the names of the replicator distribution parameters.

Returns:
A list of the distribution parameters of the given replicator distribution object.

Return type:
List[str]

get_image_space_points(points, view_proj_matrix)
Parameters:

- points – numpy array of N points (N, 3) in the world space. Points will be projected into the image space.

- view_proj_matrix – Desired view projection matrix, transforming points from world frame to image space of desired camera

Returns:
numpy array of shape (N, 3) of points projected into the image space.

get_semantics(
num_semantics,
num_semantic_tokens,
instance_semantic_map,
min_semantic_idx,
max_semantic_hierarchy_depth,
semantic_token_map,
required_semantic_types,
)set_distribution_params(
distribution:omni.replicator.core.utils.ReplicatorItem,
parameters:Dict,
)→None Parameters:

- distribution (ReplicatorItem) – The replicator distribution object to be modified.

- parameters (Dict) – A dictionary where the keys are the names of the replicator distribution parameters and the values are the parameter values to be set.

## Omnigraph Nodes
The extension exposes the following Omnigraph nodes:
