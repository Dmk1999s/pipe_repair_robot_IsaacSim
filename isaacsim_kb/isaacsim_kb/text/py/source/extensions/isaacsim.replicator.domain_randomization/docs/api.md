<!-- source: py/source/extensions/isaacsim.replicator.domain_randomization/docs/api.html | title: API — Isaac Sim -->

# API

## Python API

[TABLE]
scripts.trigger |
scripts.gate |
scripts.physics_view |
scripts.utils |
[/TABLE]

### trigger
on_rl_frame(num_envs:int)
Parameters:
num_envs (int) – The number of environments corresponding to the number of prims encapsulated in the RigidPrimViews and ArticulationViews.

### gate
on_env_reset()
on_interval(interval)
Parameters:
interval (int) – The frequency interval for randomization. The interval is incremented by isaacsim.replicator.domain_randomization.physics_view.step_randomization() call.

### physics_view
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

### utils
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
