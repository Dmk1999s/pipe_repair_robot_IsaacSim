<!-- source: py/source/extensions/isaacsim.robot.manipulators/docs/index.html | title: [isaacsim.robot.manipulators] Isaac Sim Manipulators — Isaac Sim -->

# [isaacsim.robot.manipulators] Isaac Sim Manipulators
Version: 3.3.6
Manipulators

## Enable Extension
The extension can be enabled (if not already) in one of the following ways:

## API

### Python API
manipulators

[TABLE]
SingleManipulator | Provides high level functions to set/ get properties and actions of a manipulator with a single end effector and optionally a gripper.
[/TABLE]
controllers

[TABLE]
PickPlaceController | A simple pick and place state machine for tutorials
StackingController | [summary]
[/TABLE]
grippers

[TABLE]
Gripper | Provides high level functions to set/ get properties and actions of a gripper.
ParallelGripper | Provides high level functions to set/ get properties and actions of a parallel gripper (a gripper that has two fingers).
SurfaceGripper | Provides high level functions to set/ get properties and actions of a surface gripper (a suction cup for example).
[/TABLE]

#### Manipulators
classSingleManipulator(
prim_path:str,
end_effector_prim_path:str,
name:str='single_manipulator',
position:Sequence[float]|None =None,
translation:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
scale:Sequence[float]|None =None,
visible:bool|None =None,
gripper:Gripper =None,
)Bases: SingleArticulation
Provides high level functions to set/ get properties and actions of a manipulator with a single end effector and optionally a gripper.
Parameters:

- prim_path (str) – prim path of the Prim to encapsulate or create.

- end_effector_prim_path (str) – end effector prim path to be used to track the rigid body that corresponds to the end effector. One of the following args can be specified only: end_effector_prim_name or end_effector_prim_path.

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “single_manipulator”.

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- translation (Optional[Sequence[float]], optional) – translation in the local frame of the prim (with respect to its parent prim). shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world/ local frame of the prim (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

- scale (Optional[Sequence[float]], optional) – local scale to be applied to the prim’s dimensions. shape is (3, ). Defaults to None, which means left unchanged.

- visible (Optional[bool], optional) – set to false for an invisible prim in the stage while rendering. Defaults to True.

- gripper (Gripper , optional) – Gripper to be used with the manipulator. Defaults to None.

apply_action(
control_actions:ArticulationAction ,
)→None Apply joint positions, velocities and/or efforts to control an articulation
Parameters:

- control_actions (ArticulationAction ) – actions to be applied for next physics step.

- indices (Optional[Union[list, np.ndarray]], optional) – degree of freedom indices to apply actions to. Defaults to all degrees of freedom.

Hint
High stiffness makes the joints snap faster and harder to the desired target, and higher damping smoothes but also slows down the joint’s movement to target

- For position control, set relatively high stiffness and low damping (to reduce vibrations)

- For velocity control, stiffness must be set to zero with a non-zero damping

- For effort control, stiffness and damping must be set to zero

Example:

```
>>> from isaacsim.core.utils.types import ArticulationAction
>>>
>>> # move all the robot joints to the indicated position
>>> action = ArticulationAction(joint_positions=np.array([0.0, -1.0, 0.0, -2.2, 0.0, 2.4, 0.8, 0.04, 0.04]))
>>> prim.apply_action(action)
>>>
>>> # close the robot fingers: panda_finger_joint1 (7) and panda_finger_joint2 (8) to 0.0
>>> action = ArticulationAction(joint_positions=np.array([0.0, 0.0]), joint_indices=np.array([7, 8]))
>>> prim.apply_action(action)
```

apply_visual_material(
visual_material:VisualMaterial ,
weaker_than_descendants:bool=False,
)→None Apply visual material to the held prim and optionally its descendants.
Parameters:

- visual_material (VisualMaterial ) – visual material to be applied to the held prim. Currently supports PreviewSurface, OmniPBR and OmniGlass.

- weaker_than_descendants (bool, optional) – True if the material shouldn’t override the descendants materials, otherwise False. Defaults to False.

Example:

```
>>> from isaacsim.core.api.materials import OmniGlass
>>>
>>> # create a dark-red glass visual material
>>> material = OmniGlass(
... prim_path="/World/material/glass", # path to the material prim to create
... ior=1.25,
... depth=0.001,
... thin_walled=False,
... color=np.array([0.5, 0.0, 0.0])
... )
>>> prim.apply_visual_material(material)
```

disable_gravity()→None
Keep gravity from affecting the robot
Example:

```
>>> prim.disable_gravity()
```

enable_gravity()→None
Gravity will affect the robot
Example:

```
>>> prim.enable_gravity()
```

get_angular_velocity()→ndarray
Get the angular velocity of the root articulation prim
Returns:
3D angular velocity vector. Shape (3,)

Return type:
np.ndarray

Example:

```
>>> prim.get_angular_velocity()
[0. 0. 0.]
```

get_applied_action()→ArticulationAction
Get the last applied action
Returns:
last applied action. Note: a dictionary is used as the object’s string representation

Return type:
ArticulationAction

Example:

```
>>> # last applied action: joint_positions -> [0.0, -1.0, 0.0, -2.2, 0.0, 2.4, 0.8, 0.04, 0.04]
>>> prim.get_applied_action()
{'joint_positions': [0.0, -1.0, 0.0, -2.200000047683716, 0.0, 2.4000000953674316,
0.800000011920929, 0.03999999910593033, 0.03999999910593033],
'joint_velocities': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
'joint_efforts': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}
```

get_applied_joint_efforts(
joint_indices:List|ndarray|None =None,
)→ndarrayGet the efforts applied to the joints set by the `set_joint_efforts` method
Parameters:
joint_indices (Optional[Union[List, np.ndarray]], optional) – indices to specify which joints to read. Defaults to None (all joints)

Raises:
Exception – If the handlers are not initialized

Returns:
all or selected articulation joint applied efforts

Return type:
np.ndarray

Example:

```
>>> # get all applied joint efforts
>>> prim.get_applied_joint_efforts()
[ 0. 0. 0. 0. 0. 0. 0. 0. 0.]
>>>
>>> # get finger applied efforts: panda_finger_joint1 (7) and panda_finger_joint2 (8)
>>> prim.get_applied_joint_efforts(joint_indices=np.array([7, 8]))
[0. 0.]
```

get_applied_visual_material()→VisualMaterial
Return the current applied visual material in case it was applied using apply_visual_material or it’s one of the following materials that was already applied before: PreviewSurface, OmniPBR and OmniGlass.
Returns:
the current applied visual material if its type is currently supported.

Return type:
VisualMaterial

Example:

```
>>> # given a visual material applied
>>> prim.get_applied_visual_material()
<isaacsim.core.api.materials.omni_glass.OmniGlass object at 0x7f36263106a0>
```

get_articulation_body_count()→int
Get the number of bodies (links) that make up the articulation
Returns:
amount of bodies

Return type:
int

Example:

```
>>> prim.get_articulation_body_count()
12
```

get_articulation_controller()→ArticulationController
Get the articulation controller
Note
If no `articulation_controller` was passed during class instantiation, a default controller of type `ArticulationController` (a Proportional-Derivative controller that can apply position targets, velocity targets and efforts) will be used
Returns:
articulation controller

Return type:
ArticulationController

Example:

```
>>> prim.get_articulation_controller()
<isaacsim.core.api.controllers.articulation_controller.ArticulationController object at 0x7f04a0060190>
```

get_default_state()→XFormPrimState
Get the default prim states (spatial position and orientation).
Returns:
an object that contains the default state of the prim (position and orientation)

Return type:
XFormPrimState

Example:

```
>>> state = prim.get_default_state()
>>> state
<isaacsim.core.utils.types.XFormPrimState object at 0x7f33addda650>
>>>
>>> state.position
[-4.5299529e-08 -1.8347054e-09 -2.8610229e-08]
>>> state.orientation
[1. 0. 0. 0.]
```

get_dof_index(dof_name:str)→int
Get a DOF index given its name
Parameters:
dof_name (str) – name of the DOF

Returns:
DOF index

Return type:
int

Example:

```
>>> prim.get_dof_index("panda_finger_joint2")
8
```

get_enabled_self_collisions()→int
Get the enable self collisions flag (`physxArticulation:enabledSelfCollisions`)
Returns:
self collisions flag (boolean interpreted as int)

Return type:
int

Example:

```
>>> prim.get_enabled_self_collisions()
0
```

get_joint_positions(
joint_indices:List|ndarray|None =None,
)→ndarrayGet the articulation joint positions
Parameters:
joint_indices (Optional[Union[List, np.ndarray]], optional) – indices to specify which joints to read. Defaults to None (all joints)

Returns:
all or selected articulation joint positions

Return type:
np.ndarray

Example:

```
>>> # get all joint positions
>>> prim.get_joint_positions()
[ 1.1999920e-02 -5.6962633e-01 1.3480479e-08 -2.8105433e+00 6.8284894e-06
3.0301569e+00 7.3234749e-01 3.9912373e-02 3.9999999e-02]
>>>
>>> # get finger positions: panda_finger_joint1 (7) and panda_finger_joint2 (8)
>>> prim.get_joint_positions(joint_indices=np.array([7, 8]))
[0.03991237 3.9999999e-02]
```

get_joint_velocities(
joint_indices:List|ndarray|None =None,
)→ndarrayGet the articulation joint velocities
Parameters:
joint_indices (Optional[Union[List, np.ndarray]], optional) – indices to specify which joints to read. Defaults to None (all joints)

Returns:
all or selected articulation joint velocities

Return type:
np.ndarray

Example:

```
>>> # get all joint velocities
>>> prim.get_joint_velocities()
[ 1.91603772e-06 -7.67638255e-03 -2.19138826e-07 1.10636465e-02 -4.63412944e-05
3.48245539e-02 8.84692147e-02 5.40335372e-04 1.02849208e-05]
>>>
>>> # get finger velocities: panda_finger_joint1 (7) and panda_finger_joint2 (8)
>>> prim.get_joint_velocities(joint_indices=np.array([7, 8]))
[5.4033537e-04 1.0284921e-05]
```

get_joints_default_state()→JointsState
Get the default joint states (positions and velocities).
Returns:
an object that contains the default joint positions and velocities

Return type:
JointsState

Example:

```
>>> state = prim.get_joints_default_state()
>>> state
<isaacsim.core.utils.types.JointsState object at 0x7f04a0061240>
>>>
>>> state.positions
[ 0.012 -0.57000005 0. -2.81 0. 3.037 0.785398 0.04 0.04 ]
>>> state.velocities
[0. 0. 0. 0. 0. 0. 0. 0. 0.]
```

get_joints_state()→JointsState
Get the current joint states (positions and velocities)
Returns:
an object that contains the current joint positions and velocities

Return type:
JointsState

Example:

```
>>> state = prim.get_joints_state()
>>> state
<isaacsim.core.utils.types.JointsState object at 0x7f02f6df57b0>
>>>
>>> state.positions
[ 1.1999920e-02 -5.6962633e-01 1.3480479e-08 -2.8105433e+00 6.8284894e-06
3.0301569e+00 7.3234749e-01 3.9912373e-02 3.9999999e-02]
>>> state.velocities
[ 1.91603772e-06 -7.67638255e-03 -2.19138826e-07 1.10636465e-02 -4.63412944e-05
245539e-02 8.84692147e-02 5.40335372e-04 1.02849208e-05]
```

get_linear_velocity()→ndarray
Get the linear velocity of the root articulation prim
Returns:
3D linear velocity vector. Shape (3,)

Return type:
np.ndarray

Example:

```
>>> prim.get_linear_velocity()
[0. 0. 0.]
```

get_local_pose()→Tuple[ndarray,ndarray]
Get prim’s pose with respect to the local frame (the prim’s parent frame)
Returns:
first index is the position in the local frame (with shape (3, )). Second index is quaternion orientation (with shape (4, )) in the local frame

Return type:
Tuple[np.ndarray, np.ndarray]

Example:

```
>>> # if the prim is in position (1.0, 0.5, 0.0) with respect to the world frame
>>> position, orientation = prim.get_local_pose()
>>> position
[0. 0. 0.]
>>> orientation
[0. 0. 0.]
```

get_local_scale()→ndarray
Get prim’s scale with respect to the local frame (the parent’s frame)
Returns:
scale applied to the prim’s dimensions in the local frame. shape is (3, ).

Return type:
np.ndarray

Example:

```
>>> prim.get_local_scale()
[1. 1. 1.]
```

get_measured_joint_efforts(
joint_indices:List|ndarray|None =None,
)→ndarrayReturns the efforts computed/measured by the physics solver of the joint forces in the DOF motion direction
Parameters:
joint_indices (Optional[Union[List, np.ndarray]], optional) – indices to specify which joints to read. Defaults to None (all joints)

Raises:
Exception – If the handlers are not initialized

Returns:
all or selected articulation joint measured efforts

Return type:
np.ndarray

Example:

```
>>> # get all joint efforts
>>> prim.get_measured_joint_efforts()
[ 2.7897308e-06 -6.9083519e+00 -3.6398471e-06 1.9158335e+01 -4.3552645e-06
1.1866090e+00 -4.7079347e-06 3.2339853e-04 -3.2044132e-04]
>>>
>>> # get finger efforts: panda_finger_joint1 (7) and panda_finger_joint2 (8)
>>> prim.get_measured_joint_efforts(joint_indices=np.array([7, 8]))
[ 0.0003234 -0.00032044]
```

get_measured_joint_forces(
joint_indices:List|ndarray|None =None,
)→ndarrayGet the measured joint reaction forces and torques (link incoming joint forces and torques) to external loads.
Forces and torques are reported in the local body reference frame (child joint frame of the link’s incoming joint).
Note
Since the name->index map for joints has not been exposed yet, it is possible to access the joint names and their indices through the articulation metadata.

```
prim._articulation_view._metadata.joint_names # list of names
prim._articulation_view._metadata.joint_indices # dict of name: index
```
To retrieve a specific row for the link incoming joint force/torque use `joint_index + 1`
Parameters:
joint_indices (Optional[Union[List, np.ndarray]], optional) – indices to specify which joints to read. Defaults to None (all joints)

Raises:
Exception – If the handlers are not initialized

Returns:
measured joint forces and torques. Shape is (num_joint + 1, 6). Row index 0 is the incoming joint of the base link. For the last dimension the first 3 values are for forces and the last 3 for torques

Return type:
np.ndarray

Example:

```
>>> # get all measured joint forces and torques
>>> prim.get_measured_joint_forces()
[[ 0.0000000e+00 0.0000000e+00 0.0000000e+00 0.0000000e+00 0.0000000e+00 0.0000000e+00]
[ 1.4995076e+02 4.2574748e-06 5.6364370e-04 4.8701895e-05 -6.9072924e+00 3.1881387e-05]
[-2.8971717e-05 -1.0677823e+02 -6.8384506e+01 -6.9072924e+00 -5.4927128e-05 6.1222494e-07]
[ 8.7120995e+01 -4.3871860e-05 -5.5795174e+01 5.3687054e-05 -2.4538563e+01 1.3333466e-05]
[ 5.3519474e-05 -4.8109909e+01 6.0709282e+01 1.9157074e+01 -5.9258469e-05 8.2744418e-07]
[-3.1691040e+01 2.3313689e-04 3.9990173e+01 -5.8968733e-05 -1.1863431e+00 2.2335558e-05]
[-1.0809851e-04 1.5340537e+01 -1.5458489e+01 1.1863426e+00 6.1094368e-05 -1.5940281e-05]
[-7.5418940e+00 -5.0814648e+00 -5.6512990e+00 -5.6385466e-05 3.8859999e-01 -3.4943256e-01]
[ 4.7421460e+00 -3.1945827e+00 3.5528181e+00 5.5852943e-05 8.4794536e-03 7.6405057e-03]
[ 4.0760727e+00 2.1640673e-01 -4.0513167e+00 -5.9565349e-04 1.1407082e-02 2.1432268e-06]
[ 5.1680198e-03 -9.7754575e-02 -9.7093947e-02 -8.4155556e-12 -1.2910691e-12 -1.9347857e-11]
[-5.1910793e-03 9.7588278e-02 -9.7106412e-02 8.4155573e-12 1.2910637e-12 -1.9347855e-11]]
>>>
>>> # get measured joint force and torque for the fingers
>>> metadata = prim._articulation_view._metadata
>>> joint_indices = 1 + np.array([
... metadata.joint_indices["panda_finger_joint1"],
... metadata.joint_indices["panda_finger_joint2"],
... ])
>>> joint_indices
[10 11]
>>> prim.get_measured_joint_forces(joint_indices)
[[ 5.1680198e-03 -9.7754575e-02 -9.7093947e-02 -8.4155556e-12 -1.2910691e-12 -1.9347857e-11]
[-5.1910793e-03 9.7588278e-02 -9.7106412e-02 8.4155573e-12 1.2910637e-12 -1.9347855e-11]]
```

get_position_residual(
report_max:bool|None =True,
)→floatGet physics solver position residuals for articulations. This is the residual across all joints that are part of articulations.
The solver residuals are computed according to impulse variation normalized by the effective mass.
Parameters:
report_max (Optional[bool]) – whether to report max or RMS residual. Defaults to True, i.e. max criteria

Returns:
solver position/velocity max/rms residual.

Return type:
float

get_sleep_threshold()→float
Get the threshold for articulations to enter a sleep state
Search for Articulations and Sleeping in PhysX docs for more details
Returns:
sleep threshold

Return type:
float

Example:

```
>>> prim.get_sleep_threshold()
0.005
```

get_solver_position_iteration_count()→int
Get the solver (position) iteration count for the articulation
The solver iteration count determines how accurately contacts, drives, and limits are resolved. Search for Solver Iteration Count in PhysX docs for more details.
Returns:
position iteration count

Return type:
int

Example:

```
>>> prim.get_solver_position_iteration_count()
32
```

get_solver_velocity_iteration_count()→int
Get the solver (velocity) iteration count for the articulation
The solver iteration count determines how accurately contacts, drives, and limits are resolved. Search for Solver Iteration Count in PhysX docs for more details.
Returns:
velocity iteration count

Return type:
int

Example:

```
>>> prim.get_solver_velocity_iteration_count()
32
```

get_stabilization_threshold()→float
Get the mass-normalized kinetic energy below which the articulation may participate in stabilization
Search for Stabilization Threshold in PhysX docs for more details
Returns:
stabilization threshold

Return type:
float

Example:

```
>>> prim.get_stabilization_threshold()
0.0009999999
```

get_velocity_residual(
report_max:bool|None =True,
)→floatGet physics solver velocity residuals for articulations. This is the residual across all joints that are part of articulations.
The solver residuals are computed according to impulse variation normalized by the effective mass.
Parameters:
report_max (Optional[bool]) – whether to report max or RMS residual. Defaults to True, i.e. max criteria

Returns:
solver velocity max/rms residual.

Return type:
float

get_visibility()→bool
Returns:
true if the prim is visible in stage. false otherwise.

Return type:
bool

Example:

```
>>> # get the visible state of an visible prim on the stage
>>> prim.get_visibility()
True
```

get_world_pose()→Tuple[ndarray,ndarray]
Get prim’s pose with respect to the world’s frame
Returns:
first index is the position in the world frame (with shape (3, )). Second index is quaternion orientation (with shape (4, )) in the world frame

Return type:
Tuple[np.ndarray, np.ndarray]

Example:

```
>>> # if the prim is in position (1.0, 0.5, 0.0) with respect to the world frame
>>> position, orientation = prim.get_world_pose()
>>> position
[1. 0.5 0. ]
>>> orientation
[1. 0. 0. 0.]
```

get_world_scale()→ndarray
Get prim’s scale with respect to the world’s frame
Returns:
scale applied to the prim’s dimensions in the world frame. shape is (3, ).

Return type:
np.ndarray

Example:

```
>>> prim.get_world_scale()
[1. 1. 1.]
```

get_world_velocity()→ndarray
Get the articulation root velocity
Returns:
current velocity of the the root prim. Shape (3,).

Return type:
np.ndarray

initialize(
physics_sim_view:omni.physics.tensors.SimulationView=None,
)→None Create a physics simulation view if not passed and creates an articulation view using physX tensor api.
This needs to be called after each hard reset (i.e stop + play on the timeline) before interacting with any of the functions of this class.

Parameters:
physics_sim_view (omni.physics.tensors.SimulationView, optional) – current physics simulation view. Defaults to None.

is_valid()→bool
Check if the prim path has a valid USD Prim at it
Returns:
True is the current prim path corresponds to a valid prim in stage. False otherwise.

Return type:
bool

Example:

```
>>> # given an existing and valid prim
>>> prims.is_valid()
True
```

is_visual_material_applied()→bool
Check if there is a visual material applied
Returns:
True if there is a visual material applied. False otherwise.

Return type:
bool

Example:

```
>>> # given a visual material applied
>>> prim.is_visual_material_applied()
True
```

post_reset()→None
Resets the manipulator, the end effector and the gripper to its default state.

set_angular_velocity(
velocity:ndarray,
)→None Set the angular velocity of the root articulation prim
Warning
This method will immediately set the articulation state
Parameters:
velocity (np.ndarray) – 3D angular velocity vector. Shape (3,)

Hint
This method belongs to the methods used to set the articulation kinematic state:
`set_linear_velocity`, `set_angular_velocity`, `set_joint_positions`, `set_joint_velocities`, `set_joint_efforts`
Example:

```
>>> prim.set_angular_velocity(np.array([0.1, 0.0, 0.0]))
```

set_default_state(
position:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
)→None Set the default state of the prim (position and orientation), that will be used after each reset.
Parameters:

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world frame of the prim. quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

Example:

```
>>> # configure default state
>>> prim.set_default_state(position=np.array([1.0, 0.5, 0.0]), orientation=np.array([1, 0, 0, 0]))
>>>
>>> # set default states during post-reset
>>> prim.post_reset()
```

set_enabled_self_collisions(flag:bool)→None
Set the enable self collisions flag (`physxArticulation:enabledSelfCollisions`)
Parameters:
flag (bool) – whether to enable self collisions

Example:

```
>>> prim.set_enabled_self_collisions(True)
```

set_joint_efforts(
efforts:ndarray,
joint_indices:List|ndarray|None =None,
)→None Set the articulation joint efforts
Note
This method can be used for effort control. For this purpose, there must be no joint drive or the stiffness and damping must be set to zero.
Parameters:

- efforts (np.ndarray) – articulation joint efforts

- joint_indices (Optional[Union[list, np.ndarray]], optional) – indices to specify which joints to manipulate. Defaults to None (all joints)

Hint
This method belongs to the methods used to set the articulation kinematic state:
`set_linear_velocity`, `set_angular_velocity`, `set_joint_positions`, `set_joint_velocities`, `set_joint_efforts`
Example:

```
>>> # set all the robot joint efforts to 0.0
>>> prim.set_joint_efforts(np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]))
>>>
>>> # set only the fingers efforts: panda_finger_joint1 (7) and panda_finger_joint2 (8) to 10
>>> prim.set_joint_efforts(np.array([10, 10]), joint_indices=np.array([7, 8]))
```

set_joint_positions(
positions:ndarray,
joint_indices:List|ndarray|None =None,
)→None Set the articulation joint positions
Warning
This method will immediately set (teleport) the affected joints to the indicated value. Use the `apply_action` method to control robot joints.
Parameters:

- positions (np.ndarray) – articulation joint positions

- joint_indices (Optional[Union[list, np.ndarray]], optional) – indices to specify which joints to manipulate. Defaults to None (all joints)

Hint
This method belongs to the methods used to set the articulation kinematic state:
`set_linear_velocity`, `set_angular_velocity`, `set_joint_positions`, `set_joint_velocities`, `set_joint_efforts`
Example:

```
>>> # set all the robot joints
>>> prim.set_joint_positions(np.array([0.0, -1.0, 0.0, -2.2, 0.0, 2.4, 0.8, 0.04, 0.04]))
>>>
>>> # set only the fingers in closed position: panda_finger_joint1 (7) and panda_finger_joint2 (8) to 0.0
>>> prim.set_joint_positions(np.array([0.04, 0.04]), joint_indices=np.array([7, 8]))
```

set_joint_velocities(
velocities:ndarray,
joint_indices:List|ndarray|None =None,
)→None Set the articulation joint velocities
Warning
This method will immediately set the affected joints to the indicated value. Use the `apply_action` method to control robot joints.
Parameters:

- velocities (np.ndarray) – articulation joint velocities

- joint_indices (Optional[Union[list, np.ndarray]], optional) – indices to specify which joints to manipulate. Defaults to None (all joints)

Hint
This method belongs to the methods used to set the articulation kinematic state:
`set_linear_velocity`, `set_angular_velocity`, `set_joint_positions`, `set_joint_velocities`, `set_joint_efforts`
Example:

```
>>> # set all the robot joint velocities to 0.0
>>> prim.set_joint_velocities(np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]))
>>>
>>> # set only the fingers velocities: panda_finger_joint1 (7) and panda_finger_joint2 (8) to -0.01
>>> prim.set_joint_velocities(np.array([-0.01, -0.01]), joint_indices=np.array([7, 8]))
```

set_joints_default_state(
positions:ndarray|None =None,
velocities:ndarray|None =None,
efforts:ndarray|None =None,
)→None Set the joint default states (positions, velocities and/or efforts) to be applied after each reset.
Note
The default states will be set during post-reset (e.g., calling `.post_reset()` or `world.reset()` methods)
Parameters:

- positions (Optional[np.ndarray], optional) – joint positions. Defaults to None.

- velocities (Optional[np.ndarray], optional) – joint velocities. Defaults to None.

- efforts (Optional[np.ndarray], optional) – joint efforts. Defaults to None.

Example:

```
>>> # configure default joint states
>>> prim.set_joints_default_state(
... positions=np.array([0.0, -1.0, 0.0, -2.2, 0.0, 2.4, 0.8, 0.04, 0.04]),
... velocities=np.zeros(shape=(prim.num_dof,)),
... efforts=np.zeros(shape=(prim.num_dof,))
... )
>>>
>>> # set default states during post-reset
>>> prim.post_reset()
```

set_linear_velocity(
velocity:ndarray,
)→None Set the linear velocity of the root articulation prim
Warning
This method will immediately set the articulation state
Parameters:
velocity (np.ndarray) – 3D linear velocity vector. Shape (3,).

Hint
This method belongs to the methods used to set the articulation kinematic state:
`set_linear_velocity`, `set_angular_velocity`, `set_joint_positions`, `set_joint_velocities`, `set_joint_efforts`
Example:

```
>>> prim.set_linear_velocity(np.array([0.1, 0.0, 0.0]))
```

set_local_pose(
translation:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
)→None Set prim’s pose with respect to the local frame (the prim’s parent frame).
Warning
This method will change (teleport) the prim pose immediately to the indicated value
Parameters:

- translation (Optional[Sequence[float]], optional) – translation in the local frame of the prim (with respect to its parent prim). shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the local frame of the prim. quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

Hint
This method belongs to the methods used to set the prim state
Example:

```
>>> prim.set_local_pose(translation=np.array([1.0, 0.5, 0.0]), orientation=np.array([1., 0., 0., 0.]))
```

set_local_scale(
scale:Sequence[float]|None ,
)→None Set prim’s scale with respect to the local frame (the prim’s parent frame).
Parameters:
scale (Optional[Sequence[float]]) – scale to be applied to the prim’s dimensions. shape is (3, ). Defaults to None, which means left unchanged.

Example:

```
>>> # scale prim 10 times smaller
>>> prim.set_local_scale(np.array([0.1, 0.1, 0.1]))
```

set_sleep_threshold(threshold:float)→None
Set the threshold for articulations to enter a sleep state
Search for Articulations and Sleeping in PhysX docs for more details
Parameters:
threshold (float) – sleep threshold

Example:

```
>>> prim.set_sleep_threshold(0.01)
```

set_solver_position_iteration_count(
count:int,
)→None Set the solver (position) iteration count for the articulation
The solver iteration count determines how accurately contacts, drives, and limits are resolved. Search for Solver Iteration Count in PhysX docs for more details.
Warning
Setting a higher number of iterations may improve the fidelity of the simulation, although it may affect its performance.
Parameters:
count (int) – position iteration count

Example:

```
>>> prim.set_solver_position_iteration_count(64)
```

set_solver_velocity_iteration_count(count:int)
Set the solver (velocity) iteration count for the articulation
The solver iteration count determines how accurately contacts, drives, and limits are resolved. Search for Solver Iteration Count in PhysX docs for more details.
Warning
Setting a higher number of iterations may improve the fidelity of the simulation, although it may affect its performance.
Parameters:
count (int) – velocity iteration count

Example:

```
>>> prim.set_solver_velocity_iteration_count(64)
```

set_stabilization_threshold(
threshold:float,
)→None Set the mass-normalized kinetic energy below which the articulation may participate in stabilization
Search for Stabilization Threshold in PhysX docs for more details
Parameters:
threshold (float) – stabilization threshold

Example:

```
>>> prim.set_stabilization_threshold(0.005)
```

set_visibility(visible:bool)→None
Set the visibility of the prim in stage
Parameters:
visible (bool) – flag to set the visibility of the usd prim in stage.

Example:

```
>>> # make prim not visible in the stage
>>> prim.set_visibility(visible=False)
```

set_world_pose(
position:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
)→None Ses prim’s pose with respect to the world’s frame
Warning
This method will change (teleport) the prim pose immediately to the indicated value
Parameters:

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world frame of the prim. quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

Hint
This method belongs to the methods used to set the prim state
Example:

```
>>> prim.set_world_pose(position=np.array([1.0, 0.5, 0.0]), orientation=np.array([1., 0., 0., 0.]))
```

set_world_velocity(velocity:ndarray)
Set the articulation root velocity
Parameters:
velocity (np.ndarray) – linear and angular velocity to set the root prim to. Shape (6,).

propertydof_names:List[str]
List of prim names for each DOF.
Returns:
prim names

Return type:
list(string)

Example:

```
>>> prim.dof_names
['panda_joint1', 'panda_joint2', 'panda_joint3', 'panda_joint4', 'panda_joint5',
'panda_joint6', 'panda_joint7', 'panda_finger_joint1', 'panda_finger_joint2']
```

propertydof_properties:ndarray
Articulation DOF properties

[TABLE]
Index | Property name | Description
0 | type | DOF type: invalid/unknown/uninitialized (0), rotation (1), translation (2)
1 | hasLimits | Whether the DOF has limits
2 | lower | Lower DOF limit (in radians or meters)
3 | upper | Upper DOF limit (in radians or meters)
4 | driveMode | Drive mode for the DOF: force (1), acceleration (2)
5 | maxVelocity | Maximum DOF velocity. In radians/s, or stage_units/s
6 | maxEffort | Maximum DOF effort. In N or N*stage_units
7 | stiffness | DOF stiffness
8 | damping | DOF damping
[/TABLE]
Returns:
named NumPy array of shape (num_dof, 9)

Return type:
np.ndarray

Example:

```
>>> # get properties for all DOFs
>>> prim.dof_properties
[(1, True, -2.8973, 2.8973, 1, 1.0000000e+01, 5220., 60000., 3000.)
(1, True, -1.7628, 1.7628, 1, 1.0000000e+01, 5220., 60000., 3000.)
(1, True, -2.8973, 2.8973, 1, 5.9390470e+36, 5220., 60000., 3000.)
(1, True, -3.0718, -0.0698, 1, 5.9390470e+36, 5220., 60000., 3000.)
(1, True, -2.8973, 2.8973, 1, 5.9390470e+36, 720., 25000., 3000.)
(1, True, -0.0175, 3.7525, 1, 5.9390470e+36, 720., 15000., 3000.)
(1, True, -2.8973, 2.8973, 1, 1.0000000e+01, 720., 5000., 3000.)
(2, True, 0. , 0.04 , 1, 3.4028235e+38, 720., 6000., 1000.)
(2, True, 0. , 0.04 , 1, 3.4028235e+38, 720., 6000., 1000.)]
>>>
>>> # property names
>>> prim.dof_properties.dtype.names
('type', 'hasLimits', 'lower', 'upper', 'driveMode', 'maxVelocity', 'maxEffort', 'stiffness', 'damping')
>>>
>>> # get DOF upper limits
>>> prim.dof_properties["upper"]
[ 2.8973 1.7628 2.8973 -0.0698 2.8973 3.7525 2.8973 0.04 0.04 ]
>>>
>>> # get the last DOF (panda_finger_joint2) upper limit
>>> prim.dof_properties["upper"][8] # or prim.dof_properties[8][3]
0.04
```

propertyend_effector:SingleRigidPrim
Returns: SingleRigidPrim: end effector of the manipulator (can be used to get its world pose, angular velocity..etc).

propertygripper:Gripper
Returns: Gripper: gripper of the manipulator (can be used to open or close the gripper, get its world pose or angular velocity..etc).

propertyhandles_initialized:bool
Check if articulation handler is initialized
Returns:
whether the handler was initialized

Return type:
bool

Example:

```
>>> prim.handles_initialized
True
```

propertyname:str|None
Returns: str: name given to the prim when instantiating it. Otherwise None.

propertynon_root_articulation_link:bool
Used to query if the prim is a non root articulation link
Returns:
True if the prim itself is a non root link

Return type:
bool

Example:

```
>>> # for a wrapped articulation (where the root prim has the Physics Articulation Root property applied)
>>> prim.non_root_articulation_link
False
```

propertynum_bodies:int
Number of articulation links
Returns:
number of links

Return type:
int

Example:

```
>>> prim.num_bodies
9
```

propertynum_dof:int
Number of DOF of the articulation
Returns:
amount of DOFs

Return type:
int

Example:

```
>>> prim.num_dof
9
```

propertyprim:pxr.Usd.Prim
Returns: Usd.Prim: USD Prim object that this object holds.

propertyprim_path:str
Returns: str: prim path in the stage

#### Controllers
classPickPlaceController(
name:str,
cspace_controller:BaseController ,
gripper:Gripper ,
end_effector_initial_height:float|None =None,
events_dt:List[float]|None =None,
)Bases: BaseController
A simple pick and place state machine for tutorials
Each phase runs for 1 second, which is the internal time of the state machine
Dt of each phase/ event step is defined

- Phase 0: Move end_effector above the cube center at the ‘end_effector_initial_height’.

- Phase 1: Lower end_effector down to encircle the target cube

- Phase 2: Wait for Robot’s inertia to settle.

- Phase 3: close grip.

- Phase 4: Move end_effector up again, keeping the grip tight (lifting the block).

- Phase 5: Smoothly move the end_effector toward the goal xy, keeping the height constant.

- Phase 6: Move end_effector vertically toward goal height at the ‘end_effector_initial_height’.

- Phase 7: loosen the grip.

- Phase 8: Move end_effector vertically up again at the ‘end_effector_initial_height’

- Phase 9: Move end_effector towards the old xy position.

Parameters:

- name (str) – Name id of the controller

- cspace_controller (BaseController ) – a cartesian space controller that returns an ArticulationAction type

- gripper (Gripper ) – a gripper controller for open/ close actions.

- end_effector_initial_height (Optional[float], optional) – end effector initial picking height to start from (more info in phases above). If not defined, set to 0.3 meters. Defaults to None.

- events_dt (Optional[List[float]], optional) – Dt of each phase/ event step. 10 phases dt has to be defined. Defaults to None.

Raises:

- Exception – events dt need to be list or numpy array

- Exception – events dt need have length of 10

forward(
picking_position:ndarray,
placing_position:ndarray,
current_joint_positions:ndarray,
end_effector_offset:ndarray|None =None,
end_effector_orientation:ndarray|None =None,
)→ArticulationAction Runs the controller one step.
Parameters:

- picking_position (np.ndarray) – The object’s position to be picked in local frame.

- placing_position (np.ndarray) – The object’s position to be placed in local frame.

- current_joint_positions (np.ndarray) – Current joint positions of the robot.

- end_effector_offset (Optional[np.ndarray], optional) – offset of the end effector target. Defaults to None.

- end_effector_orientation (Optional[np.ndarray], optional) – end effector orientation while picking and placing. Defaults to None.

Returns:
action to be executed by the ArticulationController

Return type:
ArticulationAction

get_current_event()→int
Returns:
Current event/ phase of the state machine

Return type:
int

is_done()→bool
Returns:
True if the state machine reached the last phase. Otherwise False.

Return type:
bool

is_paused()→bool
Returns:
True if the state machine is paused. Otherwise False.

Return type:
bool

pause()→None
Pauses the state machine’s time and phase.

reset(
end_effector_initial_height:float|None =None,
events_dt:List[float]|None =None,
)→None Resets the state machine to start from the first phase/ event
Parameters:

- end_effector_initial_height (Optional[float], optional) – end effector initial picking height to start from. If not defined, set to 0.3 meters. Defaults to None.

- events_dt (Optional[List[float]], optional) – Dt of each phase/ event step. 10 phases dt has to be defined. Defaults to None.

Raises:

- Exception – events dt need to be list or numpy array

- Exception – events dt need have length of 10

resume()→None
Resumes the state machine’s time and phase.

classStackingController(
name:str,
pick_place_controller:PickPlaceController ,
picking_order_cube_names:List[str],
robot_observation_name:str,
)Bases: BaseController
[summary]
Parameters:

- name (str) – [description]

- pick_place_controller (PickPlaceController ) – [description]

- picking_order_cube_names (List[str]) – [description]

- robot_observation_name (str) – [description]

forward(
observations:dict,
end_effector_orientation:ndarray|None =None,
end_effector_offset:ndarray|None =None,
)→ArticulationAction A controller should take inputs and returns an ArticulationAction to be then passed to the
ArticulationController.

Parameters:
observations (dict) – [description]

Raises:
NotImplementedError – [description]

Returns:
[description]

Return type:
ArticulationAction

is_done()→bool
[summary]
Returns:
[description]

Return type:
bool

reset(
picking_order_cube_names:List[str]|None =None,
)→None [summary]
Parameters:
picking_order_cube_names (Optional[List[str]], optional) – [description]. Defaults to None.

#### Grippers
classGripper(end_effector_prim_path:str)
Bases: SingleRigidPrim
Provides high level functions to set/ get properties and actions of a gripper.
Parameters:
end_effector_prim_path (str) – prim path of the Prim that corresponds to the gripper root/ end effector.

apply_visual_material(
visual_material:VisualMaterial ,
weaker_than_descendants:bool=False,
)→None Apply visual material to the held prim and optionally its descendants.
Parameters:

- visual_material (VisualMaterial ) – visual material to be applied to the held prim. Currently supports PreviewSurface, OmniPBR and OmniGlass.

- weaker_than_descendants (bool, optional) – True if the material shouldn’t override the descendants materials, otherwise False. Defaults to False.

Example:

```
>>> from isaacsim.core.api.materials import OmniGlass
>>>
>>> # create a dark-red glass visual material
>>> material = OmniGlass(
... prim_path="/World/material/glass", # path to the material prim to create
... ior=1.25,
... depth=0.001,
... thin_walled=False,
... color=np.array([0.5, 0.0, 0.0])
... )
>>> prim.apply_visual_material(material)
```

abstractclose()→None
Applies actions to the articulation that closes the gripper (ex: to hold an object).

disable_rigid_body_physics()→None
Disable the rigid body physics
When disabled, the object will not be moved by external forces such as gravity and collisions
Example:

```
>>> prim.disable_rigid_body_physics()
```

enable_rigid_body_physics()→None
Enable the rigid body physics
When enabled, the object will be moved by external forces such as gravity and collisions
Example:

```
>>> prim.enable_rigid_body_physics()
```

abstractforward(
*args,
**kwargs,
)→ArticulationAction calculates the ArticulationAction for all of the articulation joints that corresponds to a specific action
such as “open” for an example.

Returns:
articulation action to be passed to the articulation itself
(includes all joints of the articulation).

Return type:
ArticulationAction

get_angular_velocity()
Get the angular velocity of the rigid body
Returns:
current angular velocity of the the rigid prim. Shape (3,).

Return type:
np.ndarray

get_applied_visual_material()→VisualMaterial
Return the current applied visual material in case it was applied using apply_visual_material or it’s one of the following materials that was already applied before: PreviewSurface, OmniPBR and OmniGlass.
Returns:
the current applied visual material if its type is currently supported.

Return type:
VisualMaterial

Example:

```
>>> # given a visual material applied
>>> prim.get_applied_visual_material()
<isaacsim.core.api.materials.omni_glass.OmniGlass object at 0x7f36263106a0>
```

get_com()→float
Get the center of mass pose of the rigid body
Returns:
position of the center of mass of the rigid body. np.ndarray: orientation of the center of mass of the rigid body.

Return type:
np.ndarray

get_current_dynamic_state()→DynamicState
Get the current rigid body state (position, orientation and linear and angular velocities)
Returns:
the dynamic state of the rigid body prim

Return type:
DynamicState

Example:

```
>>> # for the example the rigid body is in free fall
>>> state = prim.get_current_dynamic_state()
>>> state
<isaacsim.core.utils.types.DynamicState object at 0x7f740b36f670>
>>> state.position
[ 0.99999857 2.0000017 -74.2862 ]
>>> state.orientation
[ 1.0000000e+00 -2.3961178e-07 -4.9891562e-09 4.9388258e-09]
>>> state.linear_velocity
[ 0. 0. -38.09554]
>>> state.angular_velocity
[0. 0. 0.]
```

abstractget_default_state(*args, **kwargs)
Gets the default state of the gripper

get_density()→float
Get the density of the rigid body
Returns:
density of the rigid body.

Return type:
float

Example:

```
>>> prim.get_density()
0
```

get_linear_velocity()→ndarray
Get the linear velocity of the rigid body
Returns:
current linear velocity of the the rigid prim. Shape (3,).

Return type:
np.ndarray

Example:

```
>>> prim.get_linear_velocity()
[ 1.0812164e-04 6.1415871e-05 -2.1341663e-04]
```

get_local_pose()→Tuple[ndarray,ndarray]
Get prim’s pose with respect to the local frame (the prim’s parent frame)
Returns:
first index is the position in the local frame (with shape (3, )). Second index is quaternion orientation (with shape (4, )) in the local frame

Return type:
Tuple[np.ndarray, np.ndarray]

Example:

```
>>> # if the prim is in position (1.0, 0.5, 0.0) with respect to the world frame
>>> position, orientation = prim.get_local_pose()
>>> position
[0. 0. 0.]
>>> orientation
[0. 0. 0.]
```

get_local_scale()→ndarray
Get prim’s scale with respect to the local frame (the parent’s frame)
Returns:
scale applied to the prim’s dimensions in the local frame. shape is (3, ).

Return type:
np.ndarray

Example:

```
>>> prim.get_local_scale()
[1. 1. 1.]
```

get_mass()→float
Get the mass of the rigid body
Returns:
mass of the rigid body in kg.

Return type:
float

Example:

```
>>> prim.get_mass()
0
```

get_sleep_threshold()→float
Get the threshold for the rigid body to enter a sleep state
Search for Rigid Body Dynamics > Sleeping in PhysX docs for more details
Returns:
Mass-normalized kinetic energy threshold below which
an actor may go to sleep. Range: [0, inf) Defaults: 0.00005 * tolerancesSpeed* tolerancesSpeed Units: distance^2 / second^2.

Return type:
float

Example:

```
>>> prim.get_sleep_threshold()
5e-05
```

get_visibility()→bool
Returns:
true if the prim is visible in stage. false otherwise.

Return type:
bool

Example:

```
>>> # get the visible state of an visible prim on the stage
>>> prim.get_visibility()
True
```

get_world_pose()→Tuple[ndarray,ndarray]
Get prim’s pose with respect to the world’s frame
Returns:
first index is the position in the world frame (with shape (3, )). Second index is quaternion orientation (with shape (4, )) in the world frame

Return type:
Tuple[np.ndarray, np.ndarray]

Example:

```
>>> # if the prim is in position (1.0, 0.5, 0.0) with respect to the world frame
>>> position, orientation = prim.get_world_pose()
>>> position
[1. 0.5 0. ]
>>> orientation
[1. 0. 0. 0.]
```

get_world_scale()→ndarray
Get prim’s scale with respect to the world’s frame
Returns:
scale applied to the prim’s dimensions in the world frame. shape is (3, ).

Return type:
np.ndarray

Example:

```
>>> prim.get_world_scale()
[1. 1. 1.]
```

initialize(
physics_sim_view:omni.physics.tensors.SimulationView=None,
)→None Create a physics simulation view if not passed and creates a rigid prim view using physX tensor api.
This needs to be called after each hard reset (i.e stop + play on the timeline) before interacting with any of the functions of this class.

Parameters:
physics_sim_view (omni.physics.tensors.SimulationView, optional) – current physics simulation view. Defaults to None.

is_valid()→bool
Check if the prim path has a valid USD Prim at it
Returns:
True is the current prim path corresponds to a valid prim in stage. False otherwise.

Return type:
bool

Example:

```
>>> # given an existing and valid prim
>>> prims.is_valid()
True
```

is_visual_material_applied()→bool
Check if there is a visual material applied
Returns:
True if there is a visual material applied. False otherwise.

Return type:
bool

Example:

```
>>> # given a visual material applied
>>> prim.is_visual_material_applied()
True
```

abstractopen()→None
Applies actions to the articulation that opens the gripper (ex: to release an object held).

post_reset()→None
Reset the prim to its default state (position and orientation).
Note
For an articulation, in addition to configuring the root prim’s default position and spatial orientation (defined via the `set_default_state` method), the joint’s positions, velocities, and efforts (defined via the `set_joints_default_state` method) are imposed
Example:

```
>>> prim.post_reset()
```

set_angular_velocity(velocity:ndarray)→None
Set the angular velocity of the rigid body in stage
Warning
This method will immediately set the articulation state
Parameters:
velocity (np.ndarray) – angular velocity to set the rigid prim to. Shape (3,).

set_com(
position:ndarray,
orientation:ndarray,
)→None Set the center of mass pose of the rigid body
Parameters:

- position (np.ndarray) – center of mass position. Shape (3,).

- orientation (np.ndarray) – center of mass orientation. Shape (4,).

abstractset_default_state(*args, **kwargs)
Sets the default state of the gripper

set_density(density:float)→None
Set the density of the rigid body
Parameters:
mass (float) – density of the rigid body.

Example:

```
>>> prim.set_density(0.9)
```

set_linear_velocity(velocity:ndarray)
Set the linear velocity of the rigid body in stage
Warning
This method will immediately set the rigid prim state
Parameters:
velocity (np.ndarray) – linear velocity to set the rigid prim to. Shape (3,).

set_local_pose(
translation:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
)→None Set prim’s pose with respect to the local frame (the prim’s parent frame).
Warning
This method will change (teleport) the prim pose immediately to the indicated value
Parameters:

- translation (Optional[Sequence[float]], optional) – translation in the local frame of the prim (with respect to its parent prim). shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the local frame of the prim. quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

Hint
This method belongs to the methods used to set the prim state
Example:

```
>>> prim.set_local_pose(translation=np.array([1.0, 0.5, 0.0]), orientation=np.array([1., 0., 0., 0.]))
```

set_local_scale(scale:Sequence[float]|None )→None
Set prim’s scale with respect to the local frame (the prim’s parent frame).
Parameters:
scale (Optional[Sequence[float]]) – scale to be applied to the prim’s dimensions. shape is (3, ). Defaults to None, which means left unchanged.

Example:

```
>>> # scale prim 10 times smaller
>>> prim.set_local_scale(np.array([0.1, 0.1, 0.1]))
```

set_mass(mass:float)→None
Set the mass of the rigid body
Parameters:
mass (float) – mass of the rigid body in kg.

Example:

```
>>> prim.set_mass(1.0)
```

set_sleep_threshold(threshold:float)→None
Set the threshold for the rigid body to enter a sleep state
Search for Rigid Body Dynamics > Sleeping in PhysX docs for more details
Parameters:
threshold (float) – Mass-normalized kinetic energy threshold below which an actor may go to sleep. Range: [0, inf) Defaults: 0.00005 * tolerancesSpeed* tolerancesSpeed Units: distance^2 / second^2.

Example:

```
>>> prim.set_sleep_threshold(1e-5)
```

set_visibility(visible:bool)→None
Set the visibility of the prim in stage
Parameters:
visible (bool) – flag to set the visibility of the usd prim in stage.

Example:

```
>>> # make prim not visible in the stage
>>> prim.set_visibility(visible=False)
```

set_world_pose(
position:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
)→None Ses prim’s pose with respect to the world’s frame
Warning
This method will change (teleport) the prim pose immediately to the indicated value
Parameters:

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world frame of the prim. quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

Hint
This method belongs to the methods used to set the prim state
Example:

```
>>> prim.set_world_pose(position=np.array([1.0, 0.5, 0.0]), orientation=np.array([1., 0., 0., 0.]))
```

propertyname:str|None
Returns: str: name given to the prim when instantiating it. Otherwise None.

propertynon_root_articulation_link:bool
Used to query if the prim is a non root articulation link
Returns:
True if the prim itself is a non root link

Return type:
bool

Example:

```
>>> # for a wrapped articulation (where the root prim has the Physics Articulation Root property applied)
>>> prim.non_root_articulation_link
False
```

propertyprim:pxr.Usd.Prim
Returns: Usd.Prim: USD Prim object that this object holds.

propertyprim_path:str
Returns: str: prim path in the stage

classParallelGripper(
end_effector_prim_path:str,
joint_prim_names:List[str],
joint_opened_positions:ndarray,
joint_closed_positions:ndarray,
action_deltas:ndarray=None,
use_mimic_joints:bool=False,
)Bases: Gripper
Provides high level functions to set/ get properties and actions of a parallel gripper (a gripper that has two fingers).
Parameters:

- end_effector_prim_path (str) – prim path of the Prim that corresponds to the gripper root/ end effector.

- joint_prim_names (List[str]) – the left finger joint prim name and the right finger joint prim name respectively.

- joint_opened_positions (np.ndarray) – joint positions of the left finger joint and the right finger joint respectively when opened.

- joint_closed_positions (np.ndarray) – joint positions of the left finger joint and the right finger joint respectively when closed.

- action_deltas (np.ndarray, optional) – deltas to apply for finger joint positions when openning or closing the gripper. Defaults to None.

- use_mimic_joints (bool, optional) – whether to use mimic joints. Defaults to False. If True, only the drive joint is used

apply_action(
control_actions:ArticulationAction ,
)→None Applies actions to all the joints of an articulation that corresponds to the ArticulationAction of the finger joints only.
Parameters:
control_actions (ArticulationAction ) – ArticulationAction for the left finger joint and the right finger joint respectively.

apply_visual_material(
visual_material:VisualMaterial ,
weaker_than_descendants:bool=False,
)→None Apply visual material to the held prim and optionally its descendants.
Parameters:

- visual_material (VisualMaterial ) – visual material to be applied to the held prim. Currently supports PreviewSurface, OmniPBR and OmniGlass.

- weaker_than_descendants (bool, optional) – True if the material shouldn’t override the descendants materials, otherwise False. Defaults to False.

Example:

```
>>> from isaacsim.core.api.materials import OmniGlass
>>>
>>> # create a dark-red glass visual material
>>> material = OmniGlass(
... prim_path="/World/material/glass", # path to the material prim to create
... ior=1.25,
... depth=0.001,
... thin_walled=False,
... color=np.array([0.5, 0.0, 0.0])
... )
>>> prim.apply_visual_material(material)
```

close()→None
Applies actions to the articulation that closes the gripper (ex: to hold an object).

disable_rigid_body_physics()→None
Disable the rigid body physics
When disabled, the object will not be moved by external forces such as gravity and collisions
Example:

```
>>> prim.disable_rigid_body_physics()
```

enable_rigid_body_physics()→None
Enable the rigid body physics
When enabled, the object will be moved by external forces such as gravity and collisions
Example:

```
>>> prim.enable_rigid_body_physics()
```

forward(
action:str,
)→ArticulationAction calculates the ArticulationAction for all of the articulation joints that corresponds to “open”
or “close” actions.

Parameters:
action (str) – “open” or “close” as an abstract action.

Raises:
Exception – _description_

Returns:
articulation action to be passed to the articulation itself
(includes all joints of the articulation).

Return type:
ArticulationAction

get_action_deltas()→ndarray
Returns:
deltas that will be applied for finger joint positions when openning or closing the gripper.
[left, right]. Defaults to None.

Return type:
np.ndarray

get_angular_velocity()
Get the angular velocity of the rigid body
Returns:
current angular velocity of the the rigid prim. Shape (3,).

Return type:
np.ndarray

get_applied_visual_material()→VisualMaterial
Return the current applied visual material in case it was applied using apply_visual_material or it’s one of the following materials that was already applied before: PreviewSurface, OmniPBR and OmniGlass.
Returns:
the current applied visual material if its type is currently supported.

Return type:
VisualMaterial

Example:

```
>>> # given a visual material applied
>>> prim.get_applied_visual_material()
<isaacsim.core.api.materials.omni_glass.OmniGlass object at 0x7f36263106a0>
```

get_com()→float
Get the center of mass pose of the rigid body
Returns:
position of the center of mass of the rigid body. np.ndarray: orientation of the center of mass of the rigid body.

Return type:
np.ndarray

get_current_dynamic_state()→DynamicState
Get the current rigid body state (position, orientation and linear and angular velocities)
Returns:
the dynamic state of the rigid body prim

Return type:
DynamicState

Example:

```
>>> # for the example the rigid body is in free fall
>>> state = prim.get_current_dynamic_state()
>>> state
<isaacsim.core.utils.types.DynamicState object at 0x7f740b36f670>
>>> state.position
[ 0.99999857 2.0000017 -74.2862 ]
>>> state.orientation
[ 1.0000000e+00 -2.3961178e-07 -4.9891562e-09 4.9388258e-09]
>>> state.linear_velocity
[ 0. 0. -38.09554]
>>> state.angular_velocity
[0. 0. 0.]
```

get_default_state()→ndarray
Gets the default state of the gripper
Returns:
joint positions of the left finger joint and the right finger joint respectively.

Return type:
np.ndarray

get_density()→float
Get the density of the rigid body
Returns:
density of the rigid body.

Return type:
float

Example:

```
>>> prim.get_density()
0
```

get_joint_positions()→ndarray
Returns:
joint positions of the left finger joint and the right finger joint respectively.

Return type:
np.ndarray

get_linear_velocity()→ndarray
Get the linear velocity of the rigid body
Returns:
current linear velocity of the the rigid prim. Shape (3,).

Return type:
np.ndarray

Example:

```
>>> prim.get_linear_velocity()
[ 1.0812164e-04 6.1415871e-05 -2.1341663e-04]
```

get_local_pose()→Tuple[ndarray,ndarray]
Get prim’s pose with respect to the local frame (the prim’s parent frame)
Returns:
first index is the position in the local frame (with shape (3, )). Second index is quaternion orientation (with shape (4, )) in the local frame

Return type:
Tuple[np.ndarray, np.ndarray]

Example:

```
>>> # if the prim is in position (1.0, 0.5, 0.0) with respect to the world frame
>>> position, orientation = prim.get_local_pose()
>>> position
[0. 0. 0.]
>>> orientation
[0. 0. 0.]
```

get_local_scale()→ndarray
Get prim’s scale with respect to the local frame (the parent’s frame)
Returns:
scale applied to the prim’s dimensions in the local frame. shape is (3, ).

Return type:
np.ndarray

Example:

```
>>> prim.get_local_scale()
[1. 1. 1.]
```

get_mass()→float
Get the mass of the rigid body
Returns:
mass of the rigid body in kg.

Return type:
float

Example:

```
>>> prim.get_mass()
0
```

get_sleep_threshold()→float
Get the threshold for the rigid body to enter a sleep state
Search for Rigid Body Dynamics > Sleeping in PhysX docs for more details
Returns:
Mass-normalized kinetic energy threshold below which
an actor may go to sleep. Range: [0, inf) Defaults: 0.00005 * tolerancesSpeed* tolerancesSpeed Units: distance^2 / second^2.

Return type:
float

Example:

```
>>> prim.get_sleep_threshold()
5e-05
```

get_visibility()→bool
Returns:
true if the prim is visible in stage. false otherwise.

Return type:
bool

Example:

```
>>> # get the visible state of an visible prim on the stage
>>> prim.get_visibility()
True
```

get_world_pose()→Tuple[ndarray,ndarray]
Get prim’s pose with respect to the world’s frame
Returns:
first index is the position in the world frame (with shape (3, )). Second index is quaternion orientation (with shape (4, )) in the world frame

Return type:
Tuple[np.ndarray, np.ndarray]

Example:

```
>>> # if the prim is in position (1.0, 0.5, 0.0) with respect to the world frame
>>> position, orientation = prim.get_world_pose()
>>> position
[1. 0.5 0. ]
>>> orientation
[1. 0. 0. 0.]
```

get_world_scale()→ndarray
Get prim’s scale with respect to the world’s frame
Returns:
scale applied to the prim’s dimensions in the world frame. shape is (3, ).

Return type:
np.ndarray

Example:

```
>>> prim.get_world_scale()
[1. 1. 1.]
```

initialize(
articulation_apply_action_func:Callable,
get_joint_positions_func:Callable,
set_joint_positions_func:Callable,
dof_names:List,
physics_sim_view:omni.physics.tensors.SimulationView=None,
)→None Create a physics simulation view if not passed and creates a rigid prim view using physX tensor api.
This needs to be called after each hard reset (i.e stop + play on the timeline) before interacting with any of the functions of this class.

Parameters:

- articulation_apply_action_func (Callable) – apply_action function from the Articulation class.

- get_joint_positions_func (Callable) – get_joint_positions function from the Articulation class.

- set_joint_positions_func (Callable) – set_joint_positions function from the Articulation class.

- dof_names (List) – dof names from the Articulation class.

- physics_sim_view (omni.physics.tensors.SimulationView, optional) – current physics simulation view. Defaults to None

Raises:
Exception – _description_

is_valid()→bool
Check if the prim path has a valid USD Prim at it
Returns:
True is the current prim path corresponds to a valid prim in stage. False otherwise.

Return type:
bool

Example:

```
>>> # given an existing and valid prim
>>> prims.is_valid()
True
```

is_visual_material_applied()→bool
Check if there is a visual material applied
Returns:
True if there is a visual material applied. False otherwise.

Return type:
bool

Example:

```
>>> # given a visual material applied
>>> prim.is_visual_material_applied()
True
```

open()→None
Applies actions to the articulation that opens the gripper (ex: to release an object held).

post_reset()
Reset the gripper to its default state.

set_action_deltas(value:ndarray)→None
Parameters:
value (np.ndarray) – deltas to apply for finger joint positions when openning or closing the gripper. [left, right]. Defaults to None.

set_angular_velocity(velocity:ndarray)→None
Set the angular velocity of the rigid body in stage
Warning
This method will immediately set the articulation state
Parameters:
velocity (np.ndarray) – angular velocity to set the rigid prim to. Shape (3,).

set_com(
position:ndarray,
orientation:ndarray,
)→None Set the center of mass pose of the rigid body
Parameters:

- position (np.ndarray) – center of mass position. Shape (3,).

- orientation (np.ndarray) – center of mass orientation. Shape (4,).

set_default_state(
joint_positions:ndarray,
)→None Sets the default state of the gripper
Parameters:
joint_positions (np.ndarray) – joint positions of the left finger joint and the right finger joint respectively.

set_density(density:float)→None
Set the density of the rigid body
Parameters:
mass (float) – density of the rigid body.

Example:

```
>>> prim.set_density(0.9)
```

set_joint_positions(positions:ndarray)→None
Parameters:
positions (np.ndarray) – joint positions of the left finger joint and the right finger joint respectively.

set_linear_velocity(velocity:ndarray)
Set the linear velocity of the rigid body in stage
Warning
This method will immediately set the rigid prim state
Parameters:
velocity (np.ndarray) – linear velocity to set the rigid prim to. Shape (3,).

set_local_pose(
translation:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
)→None Set prim’s pose with respect to the local frame (the prim’s parent frame).
Warning
This method will change (teleport) the prim pose immediately to the indicated value
Parameters:

- translation (Optional[Sequence[float]], optional) – translation in the local frame of the prim (with respect to its parent prim). shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the local frame of the prim. quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

Hint
This method belongs to the methods used to set the prim state
Example:

```
>>> prim.set_local_pose(translation=np.array([1.0, 0.5, 0.0]), orientation=np.array([1., 0., 0., 0.]))
```

set_local_scale(
scale:Sequence[float]|None ,
)→None Set prim’s scale with respect to the local frame (the prim’s parent frame).
Parameters:
scale (Optional[Sequence[float]]) – scale to be applied to the prim’s dimensions. shape is (3, ). Defaults to None, which means left unchanged.

Example:

```
>>> # scale prim 10 times smaller
>>> prim.set_local_scale(np.array([0.1, 0.1, 0.1]))
```

set_mass(mass:float)→None
Set the mass of the rigid body
Parameters:
mass (float) – mass of the rigid body in kg.

Example:

```
>>> prim.set_mass(1.0)
```

set_sleep_threshold(threshold:float)→None
Set the threshold for the rigid body to enter a sleep state
Search for Rigid Body Dynamics > Sleeping in PhysX docs for more details
Parameters:
threshold (float) – Mass-normalized kinetic energy threshold below which an actor may go to sleep. Range: [0, inf) Defaults: 0.00005 * tolerancesSpeed* tolerancesSpeed Units: distance^2 / second^2.

Example:

```
>>> prim.set_sleep_threshold(1e-5)
```

set_visibility(visible:bool)→None
Set the visibility of the prim in stage
Parameters:
visible (bool) – flag to set the visibility of the usd prim in stage.

Example:

```
>>> # make prim not visible in the stage
>>> prim.set_visibility(visible=False)
```

set_world_pose(
position:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
)→None Ses prim’s pose with respect to the world’s frame
Warning
This method will change (teleport) the prim pose immediately to the indicated value
Parameters:

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world frame of the prim. quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

Hint
This method belongs to the methods used to set the prim state
Example:

```
>>> prim.set_world_pose(position=np.array([1.0, 0.5, 0.0]), orientation=np.array([1., 0., 0., 0.]))
```

propertyactive_joint_count
Get the number of active joints based on the use_mimic_joints setting.
Returns:
Number of active joints (1 or 2).

Return type:
int

propertyactive_joint_indices
Get the indices of active joints based on the use_mimic_joints setting.
Returns:
List of active joint indices.

Return type:
List[int]

propertyjoint_closed_positions:ndarray
Returns: np.ndarray: joint positions of the left finger joint and the right finger joint respectively when closed.

propertyjoint_dof_indicies:ndarray
Returns: np.ndarray: joint dof indices in the articulation of the left finger joint and the right finger joint respectively.

propertyjoint_opened_positions:ndarray
Returns: np.ndarray: joint positions of the left finger joint and the right finger joint respectively when opened.

propertyjoint_prim_names:List[str]
Returns: List[str]: the left finger joint prim name and the right finger joint prim name respectively.

propertyname:str|None
Returns: str: name given to the prim when instantiating it. Otherwise None.

propertynon_root_articulation_link:bool
Used to query if the prim is a non root articulation link
Returns:
True if the prim itself is a non root link

Return type:
bool

Example:

```
>>> # for a wrapped articulation (where the root prim has the Physics Articulation Root property applied)
>>> prim.non_root_articulation_link
False
```

propertyprim:pxr.Usd.Prim
Returns: Usd.Prim: USD Prim object that this object holds.

propertyprim_path:str
Returns: str: prim path in the stage

classSurfaceGripper(end_effector_prim_path:str, surface_gripper_path:str)
Bases: Gripper
Provides high level functions to set/ get properties and actions of a surface gripper (a suction cup for example).
Parameters:

- end_effector_prim_path (str) – prim path of the Prim that corresponds to the gripper root/ end effector.

- translate (float, optional) – _description_. Defaults to 0.

- direction (str, optional) – _description_. Defaults to “x”.

- grip_threshold (float, optional) – _description_. Defaults to 0.01.

- force_limit (float, optional) – _description_. Defaults to 1.0e6.

- torque_limit (float, optional) – _description_. Defaults to 1.0e4.

- bend_angle (float, optional) – _description_. Defaults to np.pi/24.

- kp (float, optional) – _description_. Defaults to 1.0e2.

- kd (float, optional) – _description_. Defaults to 1.0e2.

- disable_gravity (bool, optional) – _description_. Defaults to True.

apply_visual_material(
visual_material:VisualMaterial ,
weaker_than_descendants:bool=False,
)→None Apply visual material to the held prim and optionally its descendants.
Parameters:

- visual_material (VisualMaterial ) – visual material to be applied to the held prim. Currently supports PreviewSurface, OmniPBR and OmniGlass.

- weaker_than_descendants (bool, optional) – True if the material shouldn’t override the descendants materials, otherwise False. Defaults to False.

Example:

```
>>> from isaacsim.core.api.materials import OmniGlass
>>>
>>> # create a dark-red glass visual material
>>> material = OmniGlass(
... prim_path="/World/material/glass", # path to the material prim to create
... ior=1.25,
... depth=0.001,
... thin_walled=False,
... color=np.array([0.5, 0.0, 0.0])
... )
>>> prim.apply_visual_material(material)
```

close()→None
Applies actions to the articulation that closes the gripper (ex: to hold an object).

disable_rigid_body_physics()→None
Disable the rigid body physics
When disabled, the object will not be moved by external forces such as gravity and collisions
Example:

```
>>> prim.disable_rigid_body_physics()
```

enable_rigid_body_physics()→None
Enable the rigid body physics
When enabled, the object will be moved by external forces such as gravity and collisions
Example:

```
>>> prim.enable_rigid_body_physics()
```

forward(
action:str,
)→ArticulationAction calculates the ArticulationAction for all of the articulation joints that corresponds to “open”
or “close” actions.

Parameters:
action (str) – “open” or “close” as an abstract action.

Raises:
Exception – _description_

Returns:
articulation action to be passed to the articulation itself
(includes all joints of the articulation).

Return type:
ArticulationAction

get_angular_velocity()
Get the angular velocity of the rigid body
Returns:
current angular velocity of the the rigid prim. Shape (3,).

Return type:
np.ndarray

get_applied_visual_material()→VisualMaterial
Return the current applied visual material in case it was applied using apply_visual_material or it’s one of the following materials that was already applied before: PreviewSurface, OmniPBR and OmniGlass.
Returns:
the current applied visual material if its type is currently supported.

Return type:
VisualMaterial

Example:

```
>>> # given a visual material applied
>>> prim.get_applied_visual_material()
<isaacsim.core.api.materials.omni_glass.OmniGlass object at 0x7f36263106a0>
```

get_com()→float
Get the center of mass pose of the rigid body
Returns:
position of the center of mass of the rigid body. np.ndarray: orientation of the center of mass of the rigid body.

Return type:
np.ndarray

get_current_dynamic_state()→DynamicState
Get the current rigid body state (position, orientation and linear and angular velocities)
Returns:
the dynamic state of the rigid body prim

Return type:
DynamicState

Example:

```
>>> # for the example the rigid body is in free fall
>>> state = prim.get_current_dynamic_state()
>>> state
<isaacsim.core.utils.types.DynamicState object at 0x7f740b36f670>
>>> state.position
[ 0.99999857 2.0000017 -74.2862 ]
>>> state.orientation
[ 1.0000000e+00 -2.3961178e-07 -4.9891562e-09 4.9388258e-09]
>>> state.linear_velocity
[ 0. 0. -38.09554]
>>> state.angular_velocity
[0. 0. 0.]
```

get_default_state()→dict
Gets the default state of the gripper
Returns:
key is “opened” and value would be true if the surface gripper should start in an opened state. False otherwise.

Return type:
dict

get_density()→float
Get the density of the rigid body
Returns:
density of the rigid body.

Return type:
float

Example:

```
>>> prim.get_density()
0
```

get_linear_velocity()→ndarray
Get the linear velocity of the rigid body
Returns:
current linear velocity of the the rigid prim. Shape (3,).

Return type:
np.ndarray

Example:

```
>>> prim.get_linear_velocity()
[ 1.0812164e-04 6.1415871e-05 -2.1341663e-04]
```

get_local_pose()→Tuple[ndarray,ndarray]
Get prim’s pose with respect to the local frame (the prim’s parent frame)
Returns:
first index is the position in the local frame (with shape (3, )). Second index is quaternion orientation (with shape (4, )) in the local frame

Return type:
Tuple[np.ndarray, np.ndarray]

Example:

```
>>> # if the prim is in position (1.0, 0.5, 0.0) with respect to the world frame
>>> position, orientation = prim.get_local_pose()
>>> position
[0. 0. 0.]
>>> orientation
[0. 0. 0.]
```

get_local_scale()→ndarray
Get prim’s scale with respect to the local frame (the parent’s frame)
Returns:
scale applied to the prim’s dimensions in the local frame. shape is (3, ).

Return type:
np.ndarray

Example:

```
>>> prim.get_local_scale()
[1. 1. 1.]
```

get_mass()→float
Get the mass of the rigid body
Returns:
mass of the rigid body in kg.

Return type:
float

Example:

```
>>> prim.get_mass()
0
```

get_sleep_threshold()→float
Get the threshold for the rigid body to enter a sleep state
Search for Rigid Body Dynamics > Sleeping in PhysX docs for more details
Returns:
Mass-normalized kinetic energy threshold below which
an actor may go to sleep. Range: [0, inf) Defaults: 0.00005 * tolerancesSpeed* tolerancesSpeed Units: distance^2 / second^2.

Return type:
float

Example:

```
>>> prim.get_sleep_threshold()
5e-05
```

get_visibility()→bool
Returns:
true if the prim is visible in stage. false otherwise.

Return type:
bool

Example:

```
>>> # get the visible state of an visible prim on the stage
>>> prim.get_visibility()
True
```

get_world_pose()→Tuple[ndarray,ndarray]
Get prim’s pose with respect to the world’s frame
Returns:
first index is the position in the world frame (with shape (3, )). Second index is quaternion orientation (with shape (4, )) in the world frame

Return type:
Tuple[np.ndarray, np.ndarray]

Example:

```
>>> # if the prim is in position (1.0, 0.5, 0.0) with respect to the world frame
>>> position, orientation = prim.get_world_pose()
>>> position
[1. 0.5 0. ]
>>> orientation
[1. 0. 0. 0.]
```

get_world_scale()→ndarray
Get prim’s scale with respect to the world’s frame
Returns:
scale applied to the prim’s dimensions in the world frame. shape is (3, ).

Return type:
np.ndarray

Example:

```
>>> prim.get_world_scale()
[1. 1. 1.]
```

initialize(
physics_sim_view:omni.physics.tensors.SimulationView=None,
articulation_num_dofs:int=None,
)→None Create a physics simulation view if not passed and creates a rigid prim view using physX tensor api.
This needs to be called after each hard reset (i.e stop + play on the timeline) before interacting with any of the functions of this class.

Parameters:

- physics_sim_view (omni.physics.tensors.SimulationView, optional) – current physics simulation view. Defaults to None

- articulation_num_dofs (int, optional) – num of dofs of the Articulation. Defaults to None.

is_closed()→bool
is_open()→bool
is_valid()→bool
Check if the prim path has a valid USD Prim at it
Returns:
True is the current prim path corresponds to a valid prim in stage. False otherwise.

Return type:
bool

Example:

```
>>> # given an existing and valid prim
>>> prims.is_valid()
True
```

is_visual_material_applied()→bool
Check if there is a visual material applied
Returns:
True if there is a visual material applied. False otherwise.

Return type:
bool

Example:

```
>>> # given a visual material applied
>>> prim.is_visual_material_applied()
True
```

open()→None
Applies actions to the articulation that opens the gripper (ex: to release an object held).

post_reset()
Reset the prim to its default state (position and orientation).
Note
For an articulation, in addition to configuring the root prim’s default position and spatial orientation (defined via the `set_default_state` method), the joint’s positions, velocities, and efforts (defined via the `set_joints_default_state` method) are imposed
Example:

```
>>> prim.post_reset()
```

set_angular_velocity(velocity:ndarray)→None
Set the angular velocity of the rigid body in stage
Warning
This method will immediately set the articulation state
Parameters:
velocity (np.ndarray) – angular velocity to set the rigid prim to. Shape (3,).

set_com(
position:ndarray,
orientation:ndarray,
)→None Set the center of mass pose of the rigid body
Parameters:

- position (np.ndarray) – center of mass position. Shape (3,).

- orientation (np.ndarray) – center of mass orientation. Shape (4,).

set_default_state(opened:bool)
Sets the default state of the gripper
Parameters:
opened (bool) – True if the surface gripper should start in an opened state. False otherwise.

set_density(density:float)→None
Set the density of the rigid body
Parameters:
mass (float) – density of the rigid body.

Example:

```
>>> prim.set_density(0.9)
```

set_linear_velocity(velocity:ndarray)
Set the linear velocity of the rigid body in stage
Warning
This method will immediately set the rigid prim state
Parameters:
velocity (np.ndarray) – linear velocity to set the rigid prim to. Shape (3,).

set_local_pose(
translation:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
)→None Set prim’s pose with respect to the local frame (the prim’s parent frame).
Warning
This method will change (teleport) the prim pose immediately to the indicated value
Parameters:

- translation (Optional[Sequence[float]], optional) – translation in the local frame of the prim (with respect to its parent prim). shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the local frame of the prim. quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

Hint
This method belongs to the methods used to set the prim state
Example:

```
>>> prim.set_local_pose(translation=np.array([1.0, 0.5, 0.0]), orientation=np.array([1., 0., 0., 0.]))
```

set_local_scale(
scale:Sequence[float]|None ,
)→None Set prim’s scale with respect to the local frame (the prim’s parent frame).
Parameters:
scale (Optional[Sequence[float]]) – scale to be applied to the prim’s dimensions. shape is (3, ). Defaults to None, which means left unchanged.

Example:

```
>>> # scale prim 10 times smaller
>>> prim.set_local_scale(np.array([0.1, 0.1, 0.1]))
```

set_mass(mass:float)→None
Set the mass of the rigid body
Parameters:
mass (float) – mass of the rigid body in kg.

Example:

```
>>> prim.set_mass(1.0)
```

set_sleep_threshold(threshold:float)→None
Set the threshold for the rigid body to enter a sleep state
Search for Rigid Body Dynamics > Sleeping in PhysX docs for more details
Parameters:
threshold (float) – Mass-normalized kinetic energy threshold below which an actor may go to sleep. Range: [0, inf) Defaults: 0.00005 * tolerancesSpeed* tolerancesSpeed Units: distance^2 / second^2.

Example:

```
>>> prim.set_sleep_threshold(1e-5)
```

set_visibility(visible:bool)→None
Set the visibility of the prim in stage
Parameters:
visible (bool) – flag to set the visibility of the usd prim in stage.

Example:

```
>>> # make prim not visible in the stage
>>> prim.set_visibility(visible=False)
```

set_world_pose(
position:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
)→None Ses prim’s pose with respect to the world’s frame
Warning
This method will change (teleport) the prim pose immediately to the indicated value
Parameters:

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world frame of the prim. quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

Hint
This method belongs to the methods used to set the prim state
Example:

```
>>> prim.set_world_pose(position=np.array([1.0, 0.5, 0.0]), orientation=np.array([1., 0., 0., 0.]))
```

update()→None
propertyname:str|None
Returns: str: name given to the prim when instantiating it. Otherwise None.

propertynon_root_articulation_link:bool
Used to query if the prim is a non root articulation link
Returns:
True if the prim itself is a non root link

Return type:
bool

Example:

```
>>> # for a wrapped articulation (where the root prim has the Physics Articulation Root property applied)
>>> prim.non_root_articulation_link
False
```

propertyprim:pxr.Usd.Prim
Returns: Usd.Prim: USD Prim object that this object holds.

propertyprim_path:str
Returns: str: prim path in the stage

## Omnigraph Nodes
The extension exposes the following Omnigraph nodes:
