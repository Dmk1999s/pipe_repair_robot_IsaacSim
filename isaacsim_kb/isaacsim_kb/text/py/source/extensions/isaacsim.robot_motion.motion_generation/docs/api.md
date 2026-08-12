<!-- source: py/source/extensions/isaacsim.robot_motion.motion_generation/docs/api.html | title: API — Isaac Sim -->

# API

## Python API
World Interface

[TABLE]
WorldInterface | Interface for translating USD world to a generic world-aware algorithm such as a MotionPolicy
[/TABLE]
Motion Policy Interface

[TABLE]
MotionPolicy | Interface for implementing a MotionPolicy: a collision-aware algorithm for dynamically moving a robot to a target.
RmpFlow | RMPflow is a real-time, reactive motion policy that smoothly guides a robot to task space targets while avoiding dynamic obstacles.
[/TABLE]
Articulation Motion Policy

[TABLE]
ArticulationMotionPolicy | Wrapper class for running MotionPolicy on simulated robots.
[/TABLE]
Kinematics Solver

[TABLE]
KinematicsSolver | An limitted interface for computing robot kinematics that includes forward and inverse kinematics.
LulaKinematicsSolver | A Lula-based implementaion of the KinematicsSolver interface.
[/TABLE]
Articulation Kinematics Solver

[TABLE]
ArticulationKinematicsSolver | Wrapper class for computing robot kinematics in a way that is easily transferable to the simulated robot Articulation.
[/TABLE]
Path Planning Interface

[TABLE]
PathPlanner | Interface for implementing a PathPlanner: An algorithm that outputs a series of configuration space waypoints, which when linearly interpolated, produce a collision-free path from a starting c-space pose to a c-space or task-space target pose.
RRT | RRT is a stochastic algorithm for quickly finding a feasible path in cspace to move a robot from a starting pose to a target pose.
[/TABLE]
Trajectory

[TABLE]
Trajectory | Interface class for defining a continuous-time trajectory for a robot in Isaac Sim.
LulaTrajectory | Instance of Trajectory interface class for handling lula.Trajectory objects
[/TABLE]
Lula Trajectory Generators

[TABLE]
LulaCSpaceTrajectoryGenerator | LulaCSpaceTrajectoryGenerator is a class for generating time-optimal trajectories that connect a series of provided c-space waypoints.
LulaTaskSpaceTrajectoryGenerator |
[/TABLE]
Articulation Trajectory

[TABLE]
ArticulationTrajectory | Wrapper class which takes in a Trajectory object and converts the output to discrete ArticulationActions that may be sent to the provided robot Articulation.
[/TABLE]
Motion Policy Base Controller

[TABLE]
MotionPolicyController | A Controller that steps using an arbitrary MotionPolicy
[/TABLE]

### World Interface
classWorldInterface
Bases: `object`
Interface for translating USD world to a generic world-aware algorithm such as a MotionPolicy
add_capsule(
capsule:DynamicCapsule |VisualCapsule ,
static:bool=False,
)→boolAdd a capsule obstacle.
Parameters:

- capsule (core.objects.capsule) – Wrapper object for handling capsule Usd Prims.

- static (bool, optional) – If True, indicate that capsule will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_capsule()

Return type:
bool

add_cone(
cone:DynamicCone |VisualCone ,
static:bool=False,
)→boolAdd a cone obstacle.
Parameters:

- cone (core.objects.cone) – Wrapper object for handling cone Usd Prims.

- static (bool, optional) – If True, indicate that cone will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_cone()

Return type:
bool

add_cuboid(
cuboid:DynamicCuboid |FixedCuboid |VisualCuboid ,
static:bool=False,
)→boolAdd a block obstacle.
Parameters:

- cuboid (core.objects.cuboid) – Wrapper object for handling rectangular prism Usd Prims.

- static (bool, optional) – If True, indicate that cuboid will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_cuboid()

Return type:
bool

add_cylinder(
cylinder:DynamicCylinder |VisualCylinder ,
static:bool=False,
)→boolAdd a cylinder obstacle.
Parameters:

- cylinder (core.objects.cylinder) – Wrapper object for handling rectangular prism Usd Prims.

- static (bool, optional) – If True, indicate that cuboid will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_cylinder()

Return type:
bool

add_ground_plane(
ground_plane:GroundPlane ,
)→boolAdd a ground_plane
Parameters:
ground_plane (core.objects.ground_plane.GroundPlane) – Wrapper object for handling ground_plane Usd Prims.

Returns:
Return True if underlying WorldInterface has implemented add_ground_plane()

Return type:
bool

add_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
static:bool|None=False,
)→boolAdd an obstacle
Parameters:

- obstacle (isaacsim.core.api.objects) – An obstacle from the package isaacsim.core.api.obstacles The type of the obstacle will be checked, and the appropriate add function will be called

- static (Optional[bool]) – When True, the obstacle will be assumed to remain stationary relative to the USD global frame over time

Returns:
Returns True if the obstacle type is valid and the appropriate add function has been implemented

Return type:
success (bool)

add_sphere(
sphere:DynamicSphere |VisualSphere ,
static:bool=False,
)→boolAdd a sphere obstacle.
Parameters:

- sphere (core.objects.sphere) – Wrapper object for handling sphere Usd Prims.

- static (bool, optional) – If True, indicate that sphere will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_sphere()

Return type:
bool

disable_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
)→boolDisable collision avoidance for obstacle.
Parameters:
obstacle (core.object) – obstacle to be disabled.

Returns:
Return True if obstacle was identified and successfully disabled.

Return type:
bool

enable_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
)→boolEnable collision avoidance for obstacle.
Parameters:
obstacle (core.object) – obstacle to be enabled.

Returns:
Return True if obstacle was identified and successfully enabled.

Return type:
bool

remove_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
)→boolRemove obstacle from collision avoidance. Obstacle cannot be re-enabled via enable_obstacle() after removal.
Parameters:
obstacle (core.object) – obstacle to be removed.

Returns:
Return True if obstacle was identified and successfully removed.

Return type:
bool

reset()→None
Reset all state inside the WorldInterface to its initial values

update_world(
updated_obstacles:List|None =None,
)→None Applies all necessary updates to the internal world representation.
Parameters:
updated_obstacles (list, optional) – If provided, only the given obstacles will have their poses updated. For motion policies that use obstacle poses relative to the robot base (e.g. Lula based policies), this list will be ignored if the robot base has moved because all object poses will have changed relative to the robot. Defaults to None.

Returns:
None

### Motion Policy Interface
classMotionPolicy
Bases: WorldInterface
Interface for implementing a MotionPolicy: a collision-aware algorithm for dynamically moving a robot to a target. The MotionPolicy interface inherits from the WorldInterface class. A MotionPolicy can be passed to an ArticulationMotionPolicy to streamline moving the simulated robot.
add_capsule(
capsule:DynamicCapsule |VisualCapsule ,
static:bool=False,
)→boolAdd a capsule obstacle.
Parameters:

- capsule (core.objects.capsule) – Wrapper object for handling capsule Usd Prims.

- static (bool, optional) – If True, indicate that capsule will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_capsule()

Return type:
bool

add_cone(
cone:DynamicCone |VisualCone ,
static:bool=False,
)→boolAdd a cone obstacle.
Parameters:

- cone (core.objects.cone) – Wrapper object for handling cone Usd Prims.

- static (bool, optional) – If True, indicate that cone will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_cone()

Return type:
bool

add_cuboid(
cuboid:DynamicCuboid |FixedCuboid |VisualCuboid ,
static:bool=False,
)→boolAdd a block obstacle.
Parameters:

- cuboid (core.objects.cuboid) – Wrapper object for handling rectangular prism Usd Prims.

- static (bool, optional) – If True, indicate that cuboid will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_cuboid()

Return type:
bool

add_cylinder(
cylinder:DynamicCylinder |VisualCylinder ,
static:bool=False,
)→boolAdd a cylinder obstacle.
Parameters:

- cylinder (core.objects.cylinder) – Wrapper object for handling rectangular prism Usd Prims.

- static (bool, optional) – If True, indicate that cuboid will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_cylinder()

Return type:
bool

add_ground_plane(
ground_plane:GroundPlane ,
)→boolAdd a ground_plane
Parameters:
ground_plane (core.objects.ground_plane.GroundPlane) – Wrapper object for handling ground_plane Usd Prims.

Returns:
Return True if underlying WorldInterface has implemented add_ground_plane()

Return type:
bool

add_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
static:bool|None=False,
)→boolAdd an obstacle
Parameters:

- obstacle (isaacsim.core.api.objects) – An obstacle from the package isaacsim.core.api.obstacles The type of the obstacle will be checked, and the appropriate add function will be called

- static (Optional[bool]) – When True, the obstacle will be assumed to remain stationary relative to the USD global frame over time

Returns:
Returns True if the obstacle type is valid and the appropriate add function has been implemented

Return type:
success (bool)

add_sphere(
sphere:DynamicSphere |VisualSphere ,
static:bool=False,
)→boolAdd a sphere obstacle.
Parameters:

- sphere (core.objects.sphere) – Wrapper object for handling sphere Usd Prims.

- static (bool, optional) – If True, indicate that sphere will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_sphere()

Return type:
bool

compute_joint_targets(
active_joint_positions:array,
active_joint_velocities:array,
watched_joint_positions:array,
watched_joint_velocities:array,
frame_duration:float,
)→Tuple[array,array]Compute position and velocity targets for the next frame given the current robot state. Position and velocity targets are used in Isaac Sim to generate forces using the PD equation kp*(joint_position_targets-joint_positions) + kd*(joint_velocity_targets-joint_velocities).
Parameters:

- active_joint_positions (np.array) – current positions of joints specified by get_active_joints()

- active_joint_velocities (np.array) – current velocities of joints specified by get_active_joints()

- watched_joint_positions (np.array) – current positions of joints specified by get_watched_joints()

- watched_joint_velocities (np.array) – current velocities of joints specified by get_watched_joints()

- frame_duration (float) – duration of the physics frame

Returns:
joint position targets for the active robot joints for the next frame
joint velocity targets for the active robot joints for the next frame

Return type:
Tuple[np.array,np.array]

disable_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
)→boolDisable collision avoidance for obstacle.
Parameters:
obstacle (core.object) – obstacle to be disabled.

Returns:
Return True if obstacle was identified and successfully disabled.

Return type:
bool

enable_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
)→boolEnable collision avoidance for obstacle.
Parameters:
obstacle (core.object) – obstacle to be enabled.

Returns:
Return True if obstacle was identified and successfully enabled.

Return type:
bool

get_active_joints()→List[str]
Active joints are directly controlled by this MotionPolicy
Some articulated robot joints may be ignored by some policies. E.g., the gripper of the Franka arm is not used to follow targets, and the RMPflow config files excludes the joints in the gripper from the list of articulated joints.
Returns:
names of active joints. The order of joints in this list determines the order in which a MotionPolicy expects joint states to be specified in functions like compute_joint_targets(active_joint_positions,…)

Return type:
List[str]

get_watched_joints()→List[str]
Watched joints are joints whose position/velocity matters to the MotionPolicy, but are not directly controlled. e.g. A MotionPolicy may control a robot arm on a mobile robot. The joint states in the rest of the robot directly affect the position of the arm, but they are not actively controlled by this MotionPolicy
Returns:
Names of joints that are being watched by this MotionPolicy. The order of joints in this list determines the order in which a MotionPolicy expects joint states to be specified in functions like compute_joint_targets(…,watched_joint_positions,…)

Return type:
List[str]

remove_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
)→boolRemove obstacle from collision avoidance. Obstacle cannot be re-enabled via enable_obstacle() after removal.
Parameters:
obstacle (core.object) – obstacle to be removed.

Returns:
Return True if obstacle was identified and successfully removed.

Return type:
bool

reset()→None
Reset all state inside the WorldInterface to its initial values

set_cspace_target(
active_joint_targets:array,
)→None Set configuration space target for the robot.
Parameters:
active_joint_target (np.array) – Desired configuration for the robot as (m x 1) vector where m is the number of active joints.

Returns:
None

set_end_effector_target(
target_translation=None,
target_orientation=None,
)→None Set end effector target.
Parameters:

- target_translation (nd.array) – Translation vector (3x1) for robot end effector. Target translation should be specified in the same units as the USD stage, relative to the stage origin.

- target_orientation (nd.array) – Quaternion of desired rotation for robot end effector relative to USD stage global frame

Returns:
None

set_robot_base_pose(
robot_translation:array,
robot_orientation:array,
)Update position of the robot base.
Parameters:

- robot_translation (np.array) – (3 x 1) translation vector describing the translation of the robot base relative to the USD stage origin. The translation vector should be specified in the units of the USD stage

- robot_orientation (np.array) – (4 x 1) quaternion describing the orientation of the robot base relative to the USD stage global frame

update_world(
updated_obstacles:List|None =None,
)→None Applies all necessary updates to the internal world representation.
Parameters:
updated_obstacles (list, optional) – If provided, only the given obstacles will have their poses updated. For motion policies that use obstacle poses relative to the robot base (e.g. Lula based policies), this list will be ignored if the robot base has moved because all object poses will have changed relative to the robot. Defaults to None.

Returns:
None

classRmpFlow(
robot_description_path:str,
urdf_path:str,
rmpflow_config_path:str,
end_effector_frame_name:str,
maximum_substep_size:float,
ignore_robot_state_updates=False,
)Bases: `LulaInterfaceHelper`, MotionPolicy
RMPflow is a real-time, reactive motion policy that smoothly guides a robot to task space targets while avoiding dynamic obstacles. This class implements the MotionPolicy interface, as well as providing a number of RmpFlow-specific functions such as visualizing the believed robot position and changing internal settings.
Parameters:

- robot_description_path (str) – Path to a robot description yaml file

- urdf_path (str) – Path to robot urdf

- rmpflow_config_path (str) – Path to an rmpflow parameter yaml file

- end_effector_frame_name (str) – Name of the robot end effector frame (must be present in the robot urdf)

- maximum_substep_size (float) –
Maximum substep size [sec] that RmpFlow will use when internally integrating between steps of a simulation. For stability and performance, RmpFlow rolls out the robot actions at a higher framerate than Isaac Sim. For example, while Isaac Sim may be running at 60 Hz, RmpFlow can be set to take internal steps that are no larger than 1/300 seconds. In this case, RmpFlow will perform 5 sub-steps every time it returns an action to the 60 Hz simulation.
In general, the maximum_substep_size argument should be at most 1/200. Choosing a very small maximum_substep_size such as 1/1000 is unnecessary, as the resulting actions will not significantly differ from a choice of 1/500, but it will internally require twice the steps to compute.

- ignore_robot_state_updates (bool) – Defaults to False. If False: RmpFlow will set the internal robot state to match the arguments to compute_joint_targets(). When paired with ArticulationMotionPolicy, this means that RMPflow uses the simulated robot’s state at every frame. If True: RmpFlow will roll out the robot state internally after it is initially specified in the first call to compute_joint_targets().

add_capsule(
capsule:DynamicCapsule |VisualCapsule ,
static:bool=False,
)→boolAdd a capsule obstacle.
Parameters:

- capsule (core.objects.capsule) – Wrapper object for handling capsule Usd Prims.

- static (bool, optional) – If True, indicate that capsule will never change pose, and may be ignored in internal world updates. Since Lula specifies object positions relative to the robot’s frame of reference, static obstacles will have their positions queried any time that set_robot_base_pose() is called. Defaults to False.

Returns:
Always True, indicating that this function has been implemented

Return type:
bool

add_cone(
cone:DynamicCone |VisualCone ,
static:bool=False,
)→boolAdd a cone obstacle.
Parameters:

- cone (core.objects.cone) – Wrapper object for handling cone Usd Prims.

- static (bool, optional) – If True, indicate that cone will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_cone()

Return type:
bool

add_cuboid(
cuboid:DynamicCuboid |FixedCuboid |VisualCuboid ,
static:bool=False,
)→boolAdd a block obstacle.
Parameters:

- cuboid (core.objects.cuboid) – Wrapper object for handling rectangular prism Usd Prims.

- static (bool, optional) – If True, indicate that cuboid will never change pose, and may be ignored in internal world updates. Since Lula specifies object positions relative to the robot’s frame of reference, static obstacles will have their positions queried any time that set_robot_base_pose() is called. Defaults to False.

Returns:
Always True, indicating that this adder has been implemented

Return type:
bool

add_cylinder(
cylinder:DynamicCylinder |VisualCylinder ,
static:bool=False,
)→boolAdd a cylinder obstacle.
Parameters:

- cylinder (core.objects.cylinder) – Wrapper object for handling rectangular prism Usd Prims.

- static (bool, optional) – If True, indicate that cuboid will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_cylinder()

Return type:
bool

add_ground_plane(
ground_plane:GroundPlane ,
)→boolAdd a ground_plane. Lula does not support ground planes directly, and instead internally creates a cuboid with an expansive face (dimensions 200x200 stage units) coplanar to the ground_plane.
Parameters:

- ground_plane (core.objects.ground_plane.GroundPlane) – Wrapper object for handling ground_plane Usd Prims.

- plane_width (Optional[float]) – The width of the ground plane (in meters) that Lula creates to constrain this robot. Defaults to 50.0 m

Returns:
Always True, indicating that this adder has been implemented

Return type:
bool

add_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
static:bool=False,
)→boolAdd an obstacle
Parameters:

- obstacle (isaacsim.core.api.objects) – An obstacle from the package isaacsim.core.api.obstacles The type of the obstacle will be checked, and the appropriate add function will be called

- static (Optional[bool]) – When True, the obstacle will be assumed to remain stationary relative to the USD global frame over time

Returns:
Returns True if the obstacle type is valid and the appropriate add function has been implemented

Return type:
success (bool)

add_sphere(
sphere:DynamicSphere |VisualSphere ,
static:bool=False,
)→boolAdd a sphere obstacle.
Parameters:

- sphere (core.objects.sphere) – Wrapper object for handling sphere Usd Prims.

- static (bool, optional) – If True, indicate that sphere will never change pose, and may be ignored in internal world updates. Since Lula specifies object positions relative to the robot’s frame of reference, static obstacles will have their positions queried any time that set_robot_base_pose() is called. Defaults to False.

Returns:
Always True, indicating that this adder has been implemented

Return type:
bool

compute_joint_targets(
active_joint_positions:array,
active_joint_velocities:array,
watched_joint_positions:array,
watched_joint_velocities:array,
frame_duration:float,
)→Tuple[array,array]Compute robot joint targets for the next frame based on the current robot position. RmpFlow will ignore active joint positions and velocities if it has been set to ignore_robot_state_updates RmpFlow does not currently support watching joints that it is not actively controlling.
Parameters:

- active_joint_positions (np.array) – current positions of joints specified by get_active_joints()

- active_joint_velocities (np.array) – current velocities of joints specified by get_active_joints()

- watched_joint_positions (np.array) – current positions of joints specified by get_watched_joints() This will always be empty for RmpFlow.

- watched_joint_velocities (np.array) – current velocities of joints specified by get_watched_joints() This will always be empty for RmpFlow.

- frame_duration (float) – duration of the physics frame

Returns:
active_joint_position_targets : Position targets for the robot in the next frame
active_joint_velocity_targets : Velocity targets for the robot in the next frame

Return type:
Tuple[np.array,np.array]

delete_collision_sphere_prims()→None
An RmpFlow specific debugging method. This function deletes any prims that have been created by RmpFlow to visualize its internal collision spheres

delete_end_effector_prim()→None
An RmpFlow specific debugging method. If RmpFlow is maintaining a prim for its believed end effector position, this function will delete the prim.

disable_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
)→boolDisable collision avoidance for obstacle.
Parameters:
obstacle (core.objects) – obstacle to be disabled.

Returns:
Return True if obstacle was identified and successfully disabled.

Return type:
bool

enable_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
)→boolEnable collision avoidance for obstacle.
Parameters:
obstacle (core.objects) – obstacle to be enabled.

Returns:
Return True if obstacle was identified and successfully enabled.

Return type:
bool

get_active_joints()→List[str]
Returns a list of joint names that RmpFlow is controlling.
Some articulated robot joints may be ignored by some policies. E.g., the gripper of the Franka arm is not used to follow targets, and the RmpFlow config files excludes the joints in the gripper from the list of active joints.
Returns:
Names of active joints.
The order of the joints in this list matches the order that the joints are expected in functions like RmpFlow.compute_joint_targets(active_joint_positions, active_joint_velocities,…)

Return type:
active_joints (List[str])

get_collision_spheres_as_prims()→List
An RmpFlow specific debugging method. This function is similar to RmpFlow.visualize_collision_spheres(). If the collision spheres have already been added to the stage as prims, they will be returned. If the collision spheres have not been added to the stage as prims, they will be created and returned. If created in this function, the spheres will be invisible until RmpFlow.visualize_collision_spheres() is called.
Visualizing collision spheres on the stage is likely to significantly slow down the framerate of the simulation. This function should only be used for debugging purposes
Returns:
List of prims representing RmpFlow’s internal collision spheres

Return type:
collision_spheres (List[core.objects.sphere.VisualSphere])

get_default_cspace_position_target()
An RmpFlow specific method; this function returns the default cspace position specified in the
Lula robot_description YAML file

Returns:
Default cspace position target used by RMPflow when none is specified.

Return type:
np.array

get_end_effector_as_prim()→VisualCuboid
An RmpFlow specific debugging method. This function is similar to RmpFlow.visualize_end_effector_position(). If the end effector has already been visualized as a prim, it will be returned. If the end effector is not being visualized, a cuboid will be created and returned. If created in this function, the end effector will be invisible until RmpFlow.visualize_end_effector_position() is called.
Returns:
Cuboid whose translation and orientation match RmpFlow’s believed robot end effector position.

Return type:
end_effector_prim (objects.cuboid.VisualCuboid )

get_end_effector_pose(
active_joint_positions:array,
)→Tuple[array,array]Return pose of robot end effector given current joint positions. The end effector position will be transformed into world coordinates based on the believed position of the robot base. See set_robot_base_pose()
Parameters:
active_joint_positions (np.array) – positions of the active joints in the robot

Returns:
end_effector_translation: (3x1) translation vector for the robot end effector
relative to the USD stage origin

end_effector_rotation: (3x3) rotation matrix describing the orientation of the
robot end effector relative to the USD global frame

Return type:
Tuple[np.array,np.array]

get_internal_robot_joint_states()→Tuple[array,array,array,array]
An RmpFlow specific method; this function returns the internal robot state that is believed by RmpFlow
Returns:
active_joint_positions: believed positions of active joints
active_joint_velocities: believed velocities of active joints
watched_joint_positions: believed positions of watched robot joints. This will always be empty for RmpFlow.
watched_joint_velocities: believed velocities of watched robot joints. This will always be empty for RmpFlow.

Return type:
Tuple[np.array,np.array,np.array,np.array]

get_kinematics_solver()→LulaKinematicsSolver
Return a LulaKinematicsSolver that uses the same robot description as RmpFlow. The robot base pose of the LulaKinematicsSolver will be set to the same base pose as RmpFlow, but the two objects must then have their base poses updated separately.
Returns:
Kinematics solver using the same cspace as RmpFlow

Return type:
LulaKinematicsSolver

get_watched_joints()→List[str]
Currently, RmpFlow is not capable of watching joint states that are not being directly controlled (active joints) If RmpFlow is controlling a robot arm at the end of an externally controlled body, set_robot_base_pose() can be used to make RmpFlow aware of the robot position This means that RmpFlow is not currently able to support controlling a set of DOFs in a robot that are not sequentially linked to each other or are not connected via fixed transforms to the end effector.
Returns:
Empty list

Return type:
watched_joints (List[str])

remove_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
)→boolRemove obstacle from collision avoidance. Obstacle cannot be re-enabled via enable_obstacle() after removal.
Parameters:
obstacle (core.objects) – obstacle to be removed.

Returns:
Return True if obstacle was identified and successfully removed.

Return type:
bool

reset()→None
Reset RmpFlow to its initial state

set_cspace_target(active_joint_targets)→None
Set a cspace target for RmpFlow. RmpFlow always has a cspace target, and setting a new cspace target does not override a position target. RmpFlow uses the cspace target to help resolve null space behavior when a position target can be acheived in a variety of ways. If the end effector target is explicitly set to None, RmpFlow will move the robot to the cspace target
Parameters:
active_joint_targets (np.array) – cspace position target for active joints in the robot

set_end_effector_target(
target_position=None,
target_orientation=None,
)→None Set end effector target.
Parameters:

- target_translation (nd.array) – Translation vector (3x1) for robot end effector. Target translation should be specified in the same units as the USD stage, relative to the stage origin.

- target_orientation (nd.array) – Quaternion of desired rotation for robot end effector relative to USD stage global frame

Returns:
None

set_ignore_state_updates(ignore_robot_state_updates)→None
An RmpFlow specific method; set an internal flag in RmpFlow: ignore_robot_state_updates
Parameters:
ignore_robot_state_updates (bool) –
If False:
RmpFlow will set the internal robot state to match the arguments to compute_joint_targets(). When paired with ArticulationMotionPolicy, this means that RMPflow uses the simulated robot’s state at every frame.

If True:
RmpFlow will roll out the robot state internally after it is initially specified in the first call to compute_joint_targets(). The caller may override this flag and directly change the internal robot state with RmpFlow.set_internal_robot_joint_states().

set_internal_robot_joint_states(
active_joint_positions:array,
active_joint_velocities:array,
watched_joint_positions:array,
watched_joint_velocities:array,
)→None An RmpFlow specific method; this function overwrites the robot state regardless of the ignore_robot_state_updates flag. RmpFlow does not currently support watching joints that it is not actively controlling.
Parameters:

- active_joint_positions (np.array) – current positions of joints specified by get_active_joints()

- active_joint_velocities (np.array) – current velocities of joints specified by get_active_joints()

- watched_joint_positions (np.array) – current positions of joints specified by get_watched_joints(). This will always be empty for RmpFlow.

- watched_joint_velocities (np.array) – current velocities of joints specified by get_watched_joints() This will always be empty for RmpFlow.

set_robot_base_pose(
robot_position:array,
robot_orientation:array,
)→None Update position of the robot base. Until this function is called, Lula will assume the base pose to be at the origin with identity rotation.
Parameters:

- robot_position (np.array) – (3 x 1) translation vector describing the translation of the robot base relative to the USD stage origin. The translation vector should be specified in the units of the USD stage

- robot_orientation (np.array) – (4 x 1) quaternion describing the orientation of the robot base relative to the USD stage global frame

stop_visualizing_collision_spheres()→None
An RmpFlow specific debugging method. This function removes the collision sphere prims created by either RmpFlow.visualize_collision_spheres() or RmpFlow.get_collision_spheres_as_prims(). Rather than making the prims invisible, they are deleted from the stage to increase performance

stop_visualizing_end_effector()→None
An RmpFlow specific debugging method. This function removes the end effector prim that can be created by visualize_end_effector_position() or get_end_effector_position_as_prim()

update_world(updated_obstacles:List=None)→None
Update the internal world state of Lula. This function automatically tracks the positions of obstacles that have been added with add_obstacle()
Parameters:
updated_obstacles (List[core.objects], optional) – Obstacles that have been added by add_obstacle() that need to be updated. If not specified, all non-static obstacle positions will be updated. If specified, only the obstacles that have been listed will have their positions updated

visualize_collision_spheres()→None
An RmpFlow specific debugging method. This function creates visible sphere prims that match the locations and radii of the collision spheres that RmpFlow uses to prevent robot collisions. Once created, RmpFlow will update the sphere locations whenever its internal robot state changes. This can be used alongside RmpFlow.ignore_robot_state_updates(True) to validate RmpFlow’s internal representation of the robot as well as help tune the PD gains on the simulated robot; i.e. the simulated robot should match the positions of the RmpFlow collision spheres over time.
Visualizing collision spheres as prims on the stage is likely to significantly slow down the framerate of the simulation. This function should only be used for debugging purposes

visualize_end_effector_position()→None
An RmpFlow specific debugging method. This function creates a visible cube whose translation and orientation match where RmpFlow believes the robot end effector to be. Once created, RmpFlow will update the position of the cube whenever its internal robot state changes.

### Articulation Motion Policy
classArticulationMotionPolicy(
robot_articulation:SingleArticulation ,
motion_policy:MotionPolicy ,
default_physics_dt:float=0.016666666666666666,
)Bases: `object`
Wrapper class for running MotionPolicy on simulated robots.
Parameters:

- robot_articulation (SingleArticulation ) – an initialized robot Articulation object

- motion_policy (MotionPolicy ) – an instance of a class that implements the MotionPolicy interface

- default_physics_dt (float) – Default physics step size to use when computing actions. A MotionPolicy computes a target position/velocity for the next frame of the simulation using the provided physics dt to know how far in the future that will be. Isaac Sim can be run with a constant or variable physics framerate. When not specified on an individual frame, the dt of the frame is assumed to be the provided default value.

Returns:
None

get_active_joints_subset()→ArticulationSubset
Get view into active joints
Returns:
returns robot states for active joints in an order compatible with the MotionPolicy

Return type:
ArticulationSubset

get_default_physics_dt()→float
Get the default value of the physics dt that is used to compute actions when none is provided
Returns:
Default physics dt

Return type:
float

get_motion_policy()→MotionPolicy
Get MotionPolicy that is being used to compute ArticulationActions
Returns:
MotionPolicy being used to compute ArticulationActions

Return type:
MotionPolicy

get_next_articulation_action(
physics_dt:float=None,
)→ArticulationAction Use underlying MotionPolicy to compute joint targets for the robot over the next frame.
Parameters:
physics_dt (float) – Physics dt to use on this frame to calculate the next action. This overrides the default_physics_dt argument, but does not change the default on future calls.

Returns:
Desired position/velocity target for the robot in the next frame

Return type:
ArticulationAction

get_robot_articulation()→SingleArticulation
Get the underlying Articulation object representing the robot.
Returns:
Articulation object representing the robot.

Return type:
SingleArticulation

get_watched_joints_subset()→ArticulationSubset
Get view into watched joints
Returns:
returns robot states for watched joints in an order compatible with the MotionPolicy

Return type:
ArticulationSubset

move(physics_dt:float=None)→None
Use underlying MotionPolicy to compute and apply joint targets to the robot over the next frame.
Parameters:
physics_dt (float) – Physics dt to use on this frame to calculate the next action. This overrides the default_physics_dt argument, but does not change the default on future calls.

Returns:
None

set_default_physics_dt(
physics_dt:float,
)→None Set the default value of the physics dt that is used to compute actions when none is provided
Parameters:
physics_dt (float) – Default physics dt

Returns:
None

### Kinematics Solver
classKinematicsSolver
Bases: WorldInterface
An limitted interface for computing robot kinematics that includes forward and inverse kinematics. This interface ommits more advanced kinematics such as Jacobians, as they are not required for most use-cases.
This interface inherits from the WorldInterface to standardize the inputs to collision-aware IK solvers, but it is not necessary for all implementations to implement the WorldInterface. See KinematicsSolver.supports_collision_avoidance()
add_capsule(
capsule:DynamicCapsule |VisualCapsule ,
static:bool=False,
)→boolAdd a capsule obstacle.
Parameters:

- capsule (core.objects.capsule) – Wrapper object for handling capsule Usd Prims.

- static (bool, optional) – If True, indicate that capsule will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_capsule()

Return type:
bool

add_cone(
cone:DynamicCone |VisualCone ,
static:bool=False,
)→boolAdd a cone obstacle.
Parameters:

- cone (core.objects.cone) – Wrapper object for handling cone Usd Prims.

- static (bool, optional) – If True, indicate that cone will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_cone()

Return type:
bool

add_cuboid(
cuboid:DynamicCuboid |FixedCuboid |VisualCuboid ,
static:bool=False,
)→boolAdd a block obstacle.
Parameters:

- cuboid (core.objects.cuboid) – Wrapper object for handling rectangular prism Usd Prims.

- static (bool, optional) – If True, indicate that cuboid will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_cuboid()

Return type:
bool

add_cylinder(
cylinder:DynamicCylinder |VisualCylinder ,
static:bool=False,
)→boolAdd a cylinder obstacle.
Parameters:

- cylinder (core.objects.cylinder) – Wrapper object for handling rectangular prism Usd Prims.

- static (bool, optional) – If True, indicate that cuboid will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_cylinder()

Return type:
bool

add_ground_plane(
ground_plane:GroundPlane ,
)→boolAdd a ground_plane
Parameters:
ground_plane (core.objects.ground_plane.GroundPlane) – Wrapper object for handling ground_plane Usd Prims.

Returns:
Return True if underlying WorldInterface has implemented add_ground_plane()

Return type:
bool

add_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
static:bool|None=False,
)→boolAdd an obstacle
Parameters:

- obstacle (isaacsim.core.api.objects) – An obstacle from the package isaacsim.core.api.obstacles The type of the obstacle will be checked, and the appropriate add function will be called

- static (Optional[bool]) – When True, the obstacle will be assumed to remain stationary relative to the USD global frame over time

Returns:
Returns True if the obstacle type is valid and the appropriate add function has been implemented

Return type:
success (bool)

add_sphere(
sphere:DynamicSphere |VisualSphere ,
static:bool=False,
)→boolAdd a sphere obstacle.
Parameters:

- sphere (core.objects.sphere) – Wrapper object for handling sphere Usd Prims.

- static (bool, optional) – If True, indicate that sphere will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_sphere()

Return type:
bool

compute_forward_kinematics(
frame_name:str,
joint_positions:array,
position_only:bool|None =False,
)→Tuple[array,array]Compute the position of a given frame in the robot relative to the USD stage global frame
Parameters:

- frame_name (str) – Name of robot frame on which to calculate forward kinematics

- joint_positions (np.array) – Joint positions for the joints returned by get_joint_names()

- position_only (bool) – If True, only the frame positions need to be calculated and the returned rotation may be left undefined.

Returns:
frame_positions: (3x1) vector describing the translation of the frame relative to the USD stage origin
frame_rotation: (3x3) rotation matrix describing the rotation of the frame relative to the USD stage global frame

Return type:
Tuple[np.array,np.array]

compute_inverse_kinematics(
frame_name:str,
target_positions:array,
target_orientation:array|None =None,
warm_start:array|None =None,
position_tolerance:float|None =None,
orientation_tolerance:float|None =None,
)→Tuple[array,bool]Compute joint positions such that the specified robot frame will reach the desired translations and rotations
Parameters:

- frame_name (str) – name of the target frame for inverse kinematics

- target_position (np.array) – target translation of the target frame (in stage units) relative to the USD stage origin

- target_orientation (np.array) – target orientation of the target frame relative to the USD stage global frame. Defaults to None.

- warm_start (np.array) – a starting position that will be used when solving the IK problem. Defaults to None.

- position_tolerance (float) – l-2 norm of acceptable position error (in stage units) between the target and achieved translations. Defaults to None.

- tolerance (orientation) – magnitude of rotation (in radians) separating the target orientation from the achieved orienatation. orientation_tolerance is well defined for values between 0 and pi. Defaults to None.

Returns:
joint_positions: in the order specified by get_joint_names() which result in the target frame acheiving the desired position
success: True if the solver converged to a solution within the given tolerances

Return type:
Tuple[np.array,bool]

disable_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
)→boolDisable collision avoidance for obstacle.
Parameters:
obstacle (core.object) – obstacle to be disabled.

Returns:
Return True if obstacle was identified and successfully disabled.

Return type:
bool

enable_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
)→boolEnable collision avoidance for obstacle.
Parameters:
obstacle (core.object) – obstacle to be enabled.

Returns:
Return True if obstacle was identified and successfully enabled.

Return type:
bool

get_all_frame_names()→List[str]
Return a list of all the frame names in the given kinematic structure
Returns:
All frame names in the kinematic structure. Any of which can be used to compute forward or inverse kinematics.

Return type:
List[str]

get_joint_names()→List[str]
Return a list containing the names of all joints in the given kinematic structure. The order of this list determines the order in which the joint positions are expected in compute_forward_kinematics(joint_positions,…) and the order in which they are returned in compute_inverse_kinematics()
Returns:
Names of all joints in the robot

Return type:
List[str]

remove_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
)→boolRemove obstacle from collision avoidance. Obstacle cannot be re-enabled via enable_obstacle() after removal.
Parameters:
obstacle (core.object) – obstacle to be removed.

Returns:
Return True if obstacle was identified and successfully removed.

Return type:
bool

reset()→None
Reset all state inside the WorldInterface to its initial values

set_robot_base_pose(
robot_positions:array,
robot_orientation:array,
)→None Update position of the robot base. This will be used to compute kinematics relative to the USD stage origin.
Parameters:

- robot_positions (np.array) – (3 x 1) translation vector describing the translation of the robot base relative to the USD stage origin. The translation vector should be specified in the units of the USD stage

- robot_orientation (np.array) – (4 x 1) quaternion describing the orientation of the robot base relative to the USD stage global frame

supports_collision_avoidance()→bool
Returns a bool describing whether the inverse kinematics support collision avoidance. If the policy does not support collision avoidance, none of the obstacle add/remove/enable/disable functions need to be implemented.
Returns:
If True, the IK solver will avoid any obstacles that have been added

Return type:
bool

update_world(
updated_obstacles:List|None =None,
)→None Applies all necessary updates to the internal world representation.
Parameters:
updated_obstacles (list, optional) – If provided, only the given obstacles will have their poses updated. For motion policies that use obstacle poses relative to the robot base (e.g. Lula based policies), this list will be ignored if the robot base has moved because all object poses will have changed relative to the robot. Defaults to None.

Returns:
None

classLulaKinematicsSolver(
robot_description_path:str,
urdf_path:str,
robot_description:RobotDescription |None =None,
)Bases: KinematicsSolver
A Lula-based implementaion of the KinematicsSolver interface. Lula uses a URDF file describing the robot and a custom yaml file that specifies the cspace of the robot and other parameters.
This class provides functions beyond the KinematicsSolver interface for getting and setting solver parameters. Inverse kinematics is solved quickly by first approximating a solution with cyclic coordinate descent (CCD) and then refining the solution with a second-order method (bfgs). As such, parameters for both solvers are available and changable as properties of this class.
Parameters:

- robot_description_path (str) – path to a robot description yaml file describing the cspace of the robot and other relevant parameters

- urdf_path (str) – path to a URDF file describing the robot

- robot_description (Optional[lula.RobotDescription ]) – An initialized lula.RobotDescription object. Other Lula-based classes such as RmpFlow may use a lula.RobotDescription object that they have already created to initialize a LulaKinematicsSolver. When specified, the provided file paths are unused. Defaults to None.

add_capsule(
capsule:DynamicCapsule |VisualCapsule ,
static:bool=False,
)→boolAdd a capsule obstacle.
Parameters:

- capsule (core.objects.capsule) – Wrapper object for handling capsule Usd Prims.

- static (bool, optional) – If True, indicate that capsule will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_capsule()

Return type:
bool

add_cone(
cone:DynamicCone |VisualCone ,
static:bool=False,
)→boolAdd a cone obstacle.
Parameters:

- cone (core.objects.cone) – Wrapper object for handling cone Usd Prims.

- static (bool, optional) – If True, indicate that cone will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_cone()

Return type:
bool

add_cuboid(
cuboid:DynamicCuboid |FixedCuboid |VisualCuboid ,
static:bool=False,
)→boolAdd a block obstacle.
Parameters:

- cuboid (core.objects.cuboid) – Wrapper object for handling rectangular prism Usd Prims.

- static (bool, optional) – If True, indicate that cuboid will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_cuboid()

Return type:
bool

add_cylinder(
cylinder:DynamicCylinder |VisualCylinder ,
static:bool=False,
)→boolAdd a cylinder obstacle.
Parameters:

- cylinder (core.objects.cylinder) – Wrapper object for handling rectangular prism Usd Prims.

- static (bool, optional) – If True, indicate that cuboid will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_cylinder()

Return type:
bool

add_ground_plane(
ground_plane:GroundPlane ,
)→boolAdd a ground_plane
Parameters:
ground_plane (core.objects.ground_plane.GroundPlane) – Wrapper object for handling ground_plane Usd Prims.

Returns:
Return True if underlying WorldInterface has implemented add_ground_plane()

Return type:
bool

add_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
static:bool|None=False,
)→boolAdd an obstacle
Parameters:

- obstacle (isaacsim.core.api.objects) – An obstacle from the package isaacsim.core.api.obstacles The type of the obstacle will be checked, and the appropriate add function will be called

- static (Optional[bool]) – When True, the obstacle will be assumed to remain stationary relative to the USD global frame over time

Returns:
Returns True if the obstacle type is valid and the appropriate add function has been implemented

Return type:
success (bool)

add_sphere(
sphere:DynamicSphere |VisualSphere ,
static:bool=False,
)→boolAdd a sphere obstacle.
Parameters:

- sphere (core.objects.sphere) – Wrapper object for handling sphere Usd Prims.

- static (bool, optional) – If True, indicate that sphere will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_sphere()

Return type:
bool

compute_forward_kinematics(
frame_name:str,
joint_positions:array,
position_only:bool|None =False,
)→Tuple[array,array]Compute the position of a given frame in the robot relative to the USD stage global frame
Parameters:

- frame_name (str) – Name of robot frame on which to calculate forward kinematics

- joint_positions (np.array) – Joint positions for the joints returned by get_joint_names()

- position_only (bool) – Lula Kinematics ignore this flag and always computes both position and orientation

Returns:
frame_positions: (3x1) vector describing the translation of the frame relative to the USD stage origin
frame_rotation: (3x3) rotation matrix describing the rotation of the frame relative to the USD stage global frame

Return type:
Tuple[np.array,np.array]

compute_inverse_kinematics(
frame_name:str,
target_position:array,
target_orientation:array=None,
warm_start:array=None,
position_tolerance:float=None,
orientation_tolerance:float=None,
)→Tuple[array,bool]Compute joint positions such that the specified robot frame will reach the desired translations and rotations. Lula Kinematics interpret the orientation tolerance as being the maximum rotation separating any standard axes. e.g. For a tolerance of .1: The X axes, Y axes, and Z axes of the rotation matrices may independently be as far as .1 radians apart
Default values for position and orientation tolerances may be seen and changed with setter and getter functions.
Parameters:

- frame_name (str) – name of the target frame for inverse kinematics

- target_position (np.array) – target translation of the target frame (in stage units) relative to the USD stage origin

- target_orientation (np.array) – target orientation of the target frame relative to the USD stage global frame. Defaults to None.

- warm_start (np.array) – a starting position that will be used when solving the IK problem. If default cspace seeds have been set, the warm start will be given priority, but the default seeds will still be used. Defaults to None.

- position_tolerance (float) – l-2 norm of acceptable position error (in stage units) between the target and achieved translations. Defaults to None.

- tolerance (orientation) – magnitude of rotation (in radians) separating the target orientation from the achieved orienatation. orientation_tolerance is well defined for values between 0 and pi. Defaults to None.

Returns:
joint_positions: in the order specified by get_joint_names() which result in the target frame acheiving the desired position
success: True if the solver converged to a solution within the given tolerances

Return type:
Tuple[np.array,bool]

disable_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
)→boolDisable collision avoidance for obstacle.
Parameters:
obstacle (core.object) – obstacle to be disabled.

Returns:
Return True if obstacle was identified and successfully disabled.

Return type:
bool

enable_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
)→boolEnable collision avoidance for obstacle.
Parameters:
obstacle (core.object) – obstacle to be enabled.

Returns:
Return True if obstacle was identified and successfully enabled.

Return type:
bool

get_all_frame_names()→List[str]
Return a list of all the frame names in the given kinematic structure
Returns:
All frame names in the kinematic structure. Any of which can be used to compute forward or inverse kinematics.

Return type:
List[str]

get_cspace_acceleration_limits()→array
Get the default acceleration limits of the active joints. Default acceleration limits are read from the robot_description YAML file. Any acceleration limits that are not specified in the robot_description YAML file will be None.
Returns:
Default acceleration limits of the active joints.

Return type:
np.array

get_cspace_jerk_limits()→array
Get the default jerk limits of the active joints. Default jerk limits are read from the robot_description YAML file. Any jerk limits that are not specified in the robot_description YAML file will be None.
Returns:
Default jerk limits of the active joints.

Return type:
np.array

get_cspace_position_limits()→Tuple[array,array]
Get the default upper and lower joint limits of the active joints.
Returns:
default_lower_joint_position_limits : Default lower position limits of active joints
default_upper_joint_position_limits : Default upper position limits of active joints

Return type:
Tuple[np.array, np.array]

get_cspace_velocity_limits()→array
Get the default velocity limits of the active joints
Returns:
Default velocity limits of the active joints

Return type:
np.array

get_default_cspace_seeds()→List[array]
Get a list of cspace seeds that the solver may use as starting points for solutions
Returns:
An N x num_dof list of cspace seeds

Return type:
List[np.array]

get_default_orientation_tolerance()→float
Get the default orientation tolerance to be used when calculating IK when none is specified
Returns:
magnitude of rotation (in radians) separating the target orientation from the achieved orienatation.
orientation_tolerance is well defined for values between 0 and pi.

Return type:
float

get_default_position_tolerance()→float
Get the default position tolerance to be used when calculating IK when none is specified
Returns:
l-2 norm of acceptable position error (in stage units) between the target and achieved translations

Return type:
float

get_joint_names()→List[str]
Return a list containing the names of all joints in the given kinematic structure. The order of this list determines the order in which the joint positions are expected in compute_forward_kinematics(joint_positions,…) and the order in which they are returned in compute_inverse_kinematics()
Returns:
Names of all joints in the robot

Return type:
List[str]

remove_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
)→boolRemove obstacle from collision avoidance. Obstacle cannot be re-enabled via enable_obstacle() after removal.
Parameters:
obstacle (core.object) – obstacle to be removed.

Returns:
Return True if obstacle was identified and successfully removed.

Return type:
bool

reset()→None
Reset all state inside the WorldInterface to its initial values

set_default_cspace_seeds(
seeds:array,
)→None Set a list of cspace seeds that the solver may use as starting points for solutions
Parameters:
seeds (np.array) – An N x num_dof list of cspace seeds

set_default_orientation_tolerance(
tolerance:float,
)→None Default orientation tolerance to be used when calculating IK when none is specified
Parameters:
tolerance (float) – magnitude of rotation (in radians) separating the target orientation from the achieved orienatation. orientation_tolerance is well defined for values between 0 and pi.

set_default_position_tolerance(
tolerance:float,
)→None Default position tolerance to be used when calculating IK when none is specified
Parameters:
tolerance (float) – l-2 norm of acceptable position error (in stage units) between the target and achieved translations

set_robot_base_pose(
robot_position:array,
robot_orientation:array,
)→None Update position of the robot base. This will be used to compute kinematics relative to the USD stage origin.
Parameters:

- robot_positions (np.array) – (3 x 1) translation vector describing the translation of the robot base relative to the USD stage origin. The translation vector should be specified in the units of the USD stage

- robot_orientation (np.array) – (4 x 1) quaternion describing the orientation of the robot base relative to the USD stage global frame

supports_collision_avoidance()→bool
Lula Inverse Kinematics do not support collision avoidance with USD obstacles
Returns:
Always False

Return type:
bool

update_world(
updated_obstacles:List|None =None,
)→None Applies all necessary updates to the internal world representation.
Parameters:
updated_obstacles (list, optional) – If provided, only the given obstacles will have their poses updated. For motion policies that use obstacle poses relative to the robot base (e.g. Lula based policies), this list will be ignored if the robot base has moved because all object poses will have changed relative to the robot. Defaults to None.

Returns:
None

propertybfgs_cspace_limit_biasing
Indicate whether c-space limit avoidance is active for BFGS descent

propertybfgs_cspace_limit_biasing_weight
Relative weight applied to c-space limit error (if active).

propertybfgs_cspace_limit_penalty_region
Region near c-space limits which will induce penalties when c-space limit biasing is active.

propertybfgs_gradient_norm_termination
Minimal change in L2-norm of the error function gradient for early descent termination from BFGS descent.

propertybfgs_gradient_norm_termination_coarse_scale_factor
Ratio between ‘bfgs_gradient_norm_termination’ for coarse and fine stagesof BFGS descent.

propertybfgs_max_iterations
Number of iterations used for each BFGS descent.

propertybfgs_orientation_weight
Weight for the relative importance of orientation error during BFGS descent.

propertybfgs_position_weight
Weight for the relative importance of position error during BFGS descent.

propertyccd_bracket_search_num_uniform_samples
Number of samples used to identify valid three-point bracket for numerical optimization of c-space updates.

propertyccd_descent_termination_delta
Minimal change in c-space coordinates for early descent termination.

propertyccd_max_iterations
Number of iterations used for each cyclic coordinate descent.

propertyccd_orientation_weight
Weight for the relative importance of orientation error during CCD.

propertyccd_position_weight
Weight for the relative importance of position error during CCD.

propertyirwin_hall_sampling_order
Sampling distribution for initial c-space positions.

propertymax_num_descents
Maximum number of c-space positions that will be used as seeds.

propertysampling_seed
Seed for Irwin-Hall sampling of initial c-space positions

### Articulation Kinematics Solver
classArticulationKinematicsSolver(
robot_articulation:SingleArticulation ,
kinematics_solver:KinematicsSolver ,
end_effector_frame_name:str,
)Bases: `object`
Wrapper class for computing robot kinematics in a way that is easily transferable to the simulated robot Articulation. A KinematicsSolver computes FK and IK at any frame, possibly only using a subset of joints available on the simulated robot. This wrapper simplifies computing the current position of the simulated robot’s end effector, as well as wrapping an IK result in an ArticulationAction that is recognized by the robot Articulation
Parameters:

- robot_articulation (SingleArticulation ) – Initialized robot Articulation object representing the simulated USD robot

- kinematics_solver (KinematicsSolver ) – An instance of a class that implements the KinematicsSolver

- end_effector_frame_name (str) – The name of the robot’s end effector frame. This frame must appear in kinematics_solver.get_all_frame_names()

compute_end_effector_pose(
position_only=False,
)→Tuple[array,array]Compute the pose of the robot end effector using the simulated robot’s current joint positions
Parameters:
position_only (bool) – If True, only the frame positions need to be calculated. The returned rotation may be left undefined.

Returns:
position: Translation vector describing the translation of the robot end effector relative to the USD global frame (in stage units)
rotation: (3x3) rotation matrix describing the rotation of the frame relative to the USD stage global frame

Return type:
Tuple[np.array,np.array]

compute_inverse_kinematics(
target_position:array,
target_orientation:array|None =None,
position_tolerance:float|None =None,
orientation_tolerance:float|None =None,
)→Tuple[ArticulationAction ,bool]Compute inverse kinematics for the end effector frame using the current robot position as a warm start. The result is returned in an articulation action that can be directly applied to the robot.
Parameters:

- target_position (np.array) – target translation of the target frame (in stage units) relative to the USD stage origin

- target_orientation (np.array) – target orientation of the target frame relative to the USD stage global frame. Defaults to None.

- position_tolerance (float) – l-2 norm of acceptable position error (in stage units) between the target and achieved translations. Defaults to None.

- tolerance (orientation) – magnitude of rotation (in radians) separating the target orientation from the achieved orienatation. orientation_tolerance is well defined for values between 0 and pi. Defaults to None.

Returns:
ik_result: An ArticulationAction that can be applied to the robot to move the end effector frame to the desired position.
success: Solver converged successfully

Return type:
Tuple[ArticulationAction , bool]

get_end_effector_frame()→str
Get the end effector frame
Returns:
Name of the end effector frame

Return type:
str

get_joints_subset()→ArticulationSubset
Returns:
A wrapper class for querying USD robot joint states in the order expected by the kinematics solver

Return type:
ArticulationSubset

get_kinematics_solver()→KinematicsSolver
Get the underlying KinematicsSolver instance used by this class.
Returns:
A class that can solve forward and inverse kinematics for a specified robot.

Return type:
KinematicsSolver

set_end_effector_frame(
end_effector_frame_name:str,
)→None Set the name for the end effector frame. If the frame is not recognized by the internal KinematicsSolver instance, an error will be thrown
Parameters:
end_effector_frame_name (str) – Name of the robot end effector frame.

### Path Planning Interface
classPathPlanner
Bases: WorldInterface
Interface for implementing a PathPlanner: An algorithm that outputs a series of configuration space waypoints, which when linearly interpolated, produce a collision-free path from a starting c-space pose to a c-space or task-space target pose.
add_capsule(
capsule:DynamicCapsule |VisualCapsule ,
static:bool=False,
)→boolAdd a capsule obstacle.
Parameters:

- capsule (core.objects.capsule) – Wrapper object for handling capsule Usd Prims.

- static (bool, optional) – If True, indicate that capsule will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_capsule()

Return type:
bool

add_cone(
cone:DynamicCone |VisualCone ,
static:bool=False,
)→boolAdd a cone obstacle.
Parameters:

- cone (core.objects.cone) – Wrapper object for handling cone Usd Prims.

- static (bool, optional) – If True, indicate that cone will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_cone()

Return type:
bool

add_cuboid(
cuboid:DynamicCuboid |FixedCuboid |VisualCuboid ,
static:bool=False,
)→boolAdd a block obstacle.
Parameters:

- cuboid (core.objects.cuboid) – Wrapper object for handling rectangular prism Usd Prims.

- static (bool, optional) – If True, indicate that cuboid will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_cuboid()

Return type:
bool

add_cylinder(
cylinder:DynamicCylinder |VisualCylinder ,
static:bool=False,
)→boolAdd a cylinder obstacle.
Parameters:

- cylinder (core.objects.cylinder) – Wrapper object for handling rectangular prism Usd Prims.

- static (bool, optional) – If True, indicate that cuboid will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_cylinder()

Return type:
bool

add_ground_plane(
ground_plane:GroundPlane ,
)→boolAdd a ground_plane
Parameters:
ground_plane (core.objects.ground_plane.GroundPlane) – Wrapper object for handling ground_plane Usd Prims.

Returns:
Return True if underlying WorldInterface has implemented add_ground_plane()

Return type:
bool

add_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
static:bool|None=False,
)→boolAdd an obstacle
Parameters:

- obstacle (isaacsim.core.api.objects) – An obstacle from the package isaacsim.core.api.obstacles The type of the obstacle will be checked, and the appropriate add function will be called

- static (Optional[bool]) – When True, the obstacle will be assumed to remain stationary relative to the USD global frame over time

Returns:
Returns True if the obstacle type is valid and the appropriate add function has been implemented

Return type:
success (bool)

add_sphere(
sphere:DynamicSphere |VisualSphere ,
static:bool=False,
)→boolAdd a sphere obstacle.
Parameters:

- sphere (core.objects.sphere) – Wrapper object for handling sphere Usd Prims.

- static (bool, optional) – If True, indicate that sphere will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_sphere()

Return type:
bool

compute_path(
active_joint_positions:array,
watched_joint_positions:array,
)→arrayCompute a set of c-space waypoints, which when linearly interpolated, produce a collision-free path from a starting c-space pose to a c-space or task-space target pose.
Parameters:

- active_joint_positions (np.array) – current positions of joints specified by get_active_joints()

- watched_joint_positions (np.array) – current positions of joints specified by get_watched_joints()

Returns:
path: An (N x m) sequence of joint positions for the active joints in the robot where N is the path length and
m is the number of active joints in the robot. If no plan is found, or no target positions have been set, None is returned

Return type:
np.array or None

disable_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
)→boolDisable collision avoidance for obstacle.
Parameters:
obstacle (core.object) – obstacle to be disabled.

Returns:
Return True if obstacle was identified and successfully disabled.

Return type:
bool

enable_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
)→boolEnable collision avoidance for obstacle.
Parameters:
obstacle (core.object) – obstacle to be enabled.

Returns:
Return True if obstacle was identified and successfully enabled.

Return type:
bool

get_active_joints()→List[str]
Active joints are directly controlled by this PathPlanner
Some articulated robot joints may be ignored by some policies. E.g., the gripper of the Franka arm is not used to follow targets, and the RMPflow config files excludes the joints in the gripper from the list of articulated joints.
Returns:
names of active joints. The order of joints in this list determines the order in which a PathPlanner expects joint states to be specified in functions like compute_path(active_joint_positions,…)

Return type:
List[str]

get_watched_joints()→List[str]
Watched joints are joints whose position matters to the PathPlanner, but are not directly controlled. e.g. A robot may have a watched joint in the middle of its kinematic chain. Watched joints will be assumed to remain watched during the rollout of a path.
Returns:
Names of joints that are being watched by this PathPlanner. The order of joints in this list determines the order in which a PathPlanner expects joint states to be specified in functions like compute_path(…,watched_joint_positions,…).

Return type:
List[str]

remove_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
)→boolRemove obstacle from collision avoidance. Obstacle cannot be re-enabled via enable_obstacle() after removal.
Parameters:
obstacle (core.object) – obstacle to be removed.

Returns:
Return True if obstacle was identified and successfully removed.

Return type:
bool

reset()→None
Reset all state inside the WorldInterface to its initial values

set_cspace_target(
active_joint_targets:array,
)→None Set configuration space target for the robot.
Parameters:
active_joint_target (np.array) – Desired configuration for the robot as (m x 1) vector where m is the number of active joints.

Returns:
None

set_end_effector_target(
target_translation,
target_orientation=None,
)→None Set end effector target.
Parameters:

- target_translation (nd.array) – Translation vector (3x1) for robot end effector. Target translation should be specified in the same units as the USD stage, relative to the stage origin.

- target_orientation (nd.array) – Quaternion of desired rotation for robot end effector relative to USD stage global frame

Returns:
None

set_robot_base_pose(
robot_translation:array,
robot_orientation:array,
)Set the position of the robot base. Computed paths will assume that the robot base remains stationary.
Parameters:

- robot_translation (np.array) – (3 x 1) translation vector describing the translation of the robot base relative to the USD stage origin. The translation vector should be specified in the units of the USD stage

- robot_orientation (np.array) – (4 x 1) quaternion describing the orientation of the robot base relative to the USD stage global frame

update_world(
updated_obstacles:List|None =None,
)→None Applies all necessary updates to the internal world representation.
Parameters:
updated_obstacles (list, optional) – If provided, only the given obstacles will have their poses updated. For motion policies that use obstacle poses relative to the robot base (e.g. Lula based policies), this list will be ignored if the robot base has moved because all object poses will have changed relative to the robot. Defaults to None.

Returns:
None

classRRT(
robot_description_path:str,
urdf_path:str,
rrt_config_path:str,
end_effector_frame_name:str,
)Bases: `LulaInterfaceHelper`, PathPlanner
RRT is a stochastic algorithm for quickly finding a feasible path in cspace to move a robot from a starting pose to a target pose. This class implements the PathPlanner interface, as well as exposing RRT-specific parameters.
Parameters:

- robot_description_path (str) – path to a robot description yaml file

- urdf_path (str) – path to robot urdf

- rrt_config_path (str) – path to an rrt parameter yaml file

- end_effector_frame_name (str) – name of the robot end effector frame (must be present in the robot urdf)

add_capsule(
capsule:DynamicCapsule |VisualCapsule ,
static:bool=False,
)→boolAdd a capsule obstacle.
Parameters:

- capsule (core.objects.capsule) – Wrapper object for handling capsule Usd Prims.

- static (bool, optional) – If True, indicate that capsule will never change pose, and may be ignored in internal world updates. Since Lula specifies object positions relative to the robot’s frame of reference, static obstacles will have their positions queried any time that set_robot_base_pose() is called. Defaults to False.

Returns:
Always True, indicating that this function has been implemented

Return type:
bool

add_cone(
cone:DynamicCone |VisualCone ,
static:bool=False,
)→boolAdd a cone obstacle.
Parameters:

- cone (core.objects.cone) – Wrapper object for handling cone Usd Prims.

- static (bool, optional) – If True, indicate that cone will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_cone()

Return type:
bool

add_cuboid(
cuboid:DynamicCuboid |FixedCuboid |VisualCuboid ,
static:bool=False,
)→boolAdd a block obstacle.
Parameters:

- cuboid (core.objects.cuboid) – Wrapper object for handling rectangular prism Usd Prims.

- static (bool, optional) – If True, indicate that cuboid will never change pose, and may be ignored in internal world updates. Since Lula specifies object positions relative to the robot’s frame of reference, static obstacles will have their positions queried any time that set_robot_base_pose() is called. Defaults to False.

Returns:
Always True, indicating that this adder has been implemented

Return type:
bool

add_cylinder(
cylinder:DynamicCylinder |VisualCylinder ,
static:bool=False,
)→boolAdd a cylinder obstacle.
Parameters:

- cylinder (core.objects.cylinder) – Wrapper object for handling rectangular prism Usd Prims.

- static (bool, optional) – If True, indicate that cuboid will never change pose, and may be ignored in internal world updates. Defaults to False.

Returns:
Return True if underlying WorldInterface has implemented add_cylinder()

Return type:
bool

add_ground_plane(
ground_plane:GroundPlane ,
)→boolAdd a ground_plane. Lula does not support ground planes directly, and instead internally creates a cuboid with an expansive face (dimensions 200x200 stage units) coplanar to the ground_plane.
Parameters:

- ground_plane (core.objects.ground_plane.GroundPlane) – Wrapper object for handling ground_plane Usd Prims.

- plane_width (Optional[float]) – The width of the ground plane (in meters) that Lula creates to constrain this robot. Defaults to 50.0 m

Returns:
Always True, indicating that this adder has been implemented

Return type:
bool

add_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
static:bool=False,
)→boolAdd an obstacle
Parameters:

- obstacle (isaacsim.core.api.objects) – An obstacle from the package isaacsim.core.api.obstacles The type of the obstacle will be checked, and the appropriate add function will be called

- static (Optional[bool]) – When True, the obstacle will be assumed to remain stationary relative to the USD global frame over time

Returns:
Returns True if the obstacle type is valid and the appropriate add function has been implemented

Return type:
success (bool)

add_sphere(
sphere:DynamicSphere |VisualSphere ,
static:bool=False,
)→boolAdd a sphere obstacle.
Parameters:

- sphere (core.objects.sphere) – Wrapper object for handling sphere Usd Prims.

- static (bool, optional) – If True, indicate that sphere will never change pose, and may be ignored in internal world updates. Since Lula specifies object positions relative to the robot’s frame of reference, static obstacles will have their positions queried any time that set_robot_base_pose() is called. Defaults to False.

Returns:
Always True, indicating that this adder has been implemented

Return type:
bool

compute_path(
active_joint_positions,
watched_joint_positions,
)→arrayCompute a set of c-space waypoints, which when linearly interpolated, produce a collision-free path from a starting c-space pose to a c-space or task-space target pose.
Parameters:

- active_joint_positions (np.array) – current positions of joints specified by get_active_joints()

- watched_joint_positions (np.array) – current positions of joints specified by get_watched_joints()

Returns:
path: An (N x m) sequence of joint positions for the active joints in the robot where N is the path length and
m is the number of active joints in the robot. If no plan is found, or no target positions have been set, None is returned

Return type:
np.array or None

disable_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
)→boolDisable collision avoidance for obstacle.
Parameters:
obstacle (core.objects) – obstacle to be disabled.

Returns:
Return True if obstacle was identified and successfully disabled.

Return type:
bool

enable_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
)→boolEnable collision avoidance for obstacle.
Parameters:
obstacle (core.objects) – obstacle to be enabled.

Returns:
Return True if obstacle was identified and successfully enabled.

Return type:
bool

get_active_joints()→List
Active joints are directly controlled by this PathPlanner
Some articulated robot joints may be ignored by some policies. E.g., the gripper of the Franka arm is not used to follow targets, and the RMPflow config files excludes the joints in the gripper from the list of articulated joints.
Returns:
names of active joints. The order of joints in this list determines the order in which a PathPlanner expects joint states to be specified in functions like compute_path(active_joint_positions,…)

Return type:
List[str]

get_end_effector_pose(
active_joint_positions:array,
frame_name:str,
)→Tuple[array,array]Return pose of robot end effector given current joint positions. The end effector position will be transformed into world coordinates based on the believed position of the robot base. See set_robot_base_pose()
Parameters:
active_joint_positions (np.array) – positions of the active joints in the robot

Returns:
end_effector_translation: (3x1) translation vector for the robot end effector
relative to the USD stage origin

end_effector_rotation: (3x3) rotation matrix describing the orientation of the
robot end effector relative to the USD global frame

Return type:
Tuple[np.array,np.array]

get_watched_joints()→List
Lula does not currently support watching joint states that are not controllable
Returns:
Always returns an empty list.

Return type:
(List)

remove_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
)→boolRemove obstacle from collision avoidance. Obstacle cannot be re-enabled via enable_obstacle() after removal.
Parameters:
obstacle (core.objects) – obstacle to be removed.

Returns:
Return True if obstacle was identified and successfully removed.

Return type:
bool

reset()→None
reset the world to its initial state

set_cspace_target(active_joint_targets:array)→None
Set configuration space target for the robot.
Parameters:
active_joint_target (np.array) – Desired configuration for the robot as (m x 1) vector where m is the number of active joints.

Returns:
None

set_end_effector_target(
target_translation,
target_orientation=None,
)→None Set end effector target.
Parameters:

- target_translation (nd.array) – Translation vector (3x1) for robot end effector. Target translation should be specified in the same units as the USD stage, relative to the stage origin.

- target_orientation (nd.array) – Quaternion of desired rotation for robot end effector relative to USD stage global frame

Returns:
None

set_max_iterations(max_iter:int)→None
Set the maximum number of iterations of RRT before a failure is returned
Parameters:
max_iter (int) – Maximum number of iterations of RRT before a failure is returned. The time it takes to return a failure scales quadratically with max_iter

set_param(
param_name:str,
value:array|float|int|str,
)→boolSet a parameter for the RRT algorithm. The parameters and their appropriate values are enumerated below:
seed (int):
-Used to initialize random sampling. -seed must be positive. -This parameter may also be set through the set_random_seed() function

step_size (float):
-Step size for tree extension. -It is assumed that a straight path connecting two valid c-space configurations with separation distance <= step_size is a valid edge, where separation distance is defined as the L2-norm of the difference between the two configurations. -step_size must be positive.

max_iterations (int)

- Maximum number of iterations of tree extensions that will be attempted.

- If max_iterations is reached without finding a valid path, the Results will indicate path_found is false and path will be an empty vector.

- max_iterations must be positive.

distance_metric_weights (np.array[np.float64[num_dof,]])

- When selecting a node for tree extension, the closest node is defined using a weighted, squared L2-norm:
distance = (q0 - q1)^T * W * (q0 - q1) where q0 and q1 represent two configurations and W is a diagonal matrix formed from distance_metric_weights.

- The length of the distance_metric_weights must be equal to the number of c-space coordinates for the robot and each weight must be positive.

task_space_frame_name (string)

- Indicate the name (from URDF) of the frame to be used for task space planning.

- With current implementation, setting a task_space_frame_name that is not found in the kinematics will throw an exception rather than failing gracefully.

task_space_limits (np.array[np.float64[3,2]])

- Task space limits define a bounding box used for sampling task space when planning a path to a task space target.

- The specified task_space_limits should be a (3 x 2) matrix. Rows correspond to the xyz dimensions of the bounding box, and columns 0 and 1 correspond to the lower and upper limit repectively.

- Each upper limit must be >= the corresponding lower limit.

c_space_planning_params/exploration_fraction (float)

- The c-space planner uses RRT-Connect to try to find a path to a c-space target.

- RRT-Connect attempts to iteratively extend two trees (one from the initial configuration and one from the target configuration)
until the two trees can be connected. The configuration to which a tree is extended can be either a random sample (i.e., exploration) or a node on the tree to which connection is desired (i.e., exploitation). The exploration_fraction controls the fraction of steps that are exploration steps. It is generally recommended to set exploration_fraction in range [0.5, 1), where 1 corresponds to a single initial exploitation step followed by only exploration steps. Values of between [0, 0.5) correspond to more exploitation than exploration and are not recommended. If a value outside range [0, 1] is provided, a warning is logged and the value is clamped to range [0, 1].

- A default value of 0.5 is recommended as a starting value for initial testing with a given
system.

task_space_planning_params/translation_target_zone_tolerance (float)

- A configuration has reached the task space translation target when task space position has an L2 Norm within translation_target_zone_tolerance of the target.

- It is assumed that a valid configuration within the target tolerance can be moved directly to the target configuration using an inverse kinematics solver and linearly stepping towards the solution.

- In general, it is recommended that the size of the translation target zone be on the same order of magnitude as the translational distance in task-space corresponding to moving the robot in configuration space by one step with an L2 norm of step_size.

task_space_planning_params/orientation_target_zone_tolerance (float)

- A configuration has reached the task space pose target when task space orientation is within orientation_target_zone_tolerance radians and an L2 norm translation within translation_target_zone_tolerance of the target.

- It is assumed that a valid configuration within the target tolerances can be moved directly to the target configuration using an inverse kinematics solver and linearly stepping towards the solution.

- In general, it is recommended that the size of the orientation target zone be on the same order of magnitude as the rotational distance in task-space corresponding to moving the robot in configuration space by one step with an L2 norm of step_size.

task_space_planning_params/translation_target_final_tolerance (float)

- Once a path is found that terminates within translation_target_zone_tolerance, an IK solver is used to find a configuration space solution corresponding to the task space target. This solver terminates when the L2-norm of the corresponding task space position is within translation_target_final_tolerance of the target.

- Note: This solver assumes that if a c-space configuration within translation_target_zone_tolerance is found then this c-space configuration can be moved linearly in cspace to the IK solution. If this assumption is NOT met, the returned path will not reach the task space target within the translation_target_final_tolerance and an error is logged.

- The recommended default value is 1e-4, but in general this value should be set to a positive value that is considered “good enough” precision for the specific system.

task_space_planning_params/orientation_target_final_tolerance (float)

- For pose targets, once a path is found that terminates within orientation_target_zone_tolerance and translation_target_zone_tolerance of the target, an IK solver is used to find a configuration space solution corresponding to the task space target. This solver terminates when the L2-norm of the corresponding task space position is within orientation_target_final_tolerance and translation_target_final_tolerance of the target.

- Note: This solver assumes that if a c-space configuration within the target zone tolerances is found then this c-space configuration can be moved linearly in cspace to the IK solution. If this assumption is NOT met, the returned path will not reach the task space target within the the final target tolerances and an error is logged.

- The recommended default value is 1e-4, but in general this value should be set to a positive value that is considered “good enough” precision for the specific system.

task_space_planning_params/translation_gradient_weight (float)

- For pose targets, computed translation and orientation gradients are linearly weighted by translation_gradient_weight and orientation_gradient_weight to compute a combined gradient step when using the Jacobian Transpose method to guide tree expansion towards a task space target.

- A default value of 1.0 is recommended as a starting value for initial testing with a given system.

- Must be > 0.

task_space_planning_params/orientation_gradient_weight (float)

- For pose targets, computed translation and orientation gradients are linearly weighted by translation_gradient_weight and orientation_gradient_weight to compute a combined gradient step when using the Jacobian Transpose method to guide tree expansion towards a task space target.

- A default value of 0.125 is recommended as a starting value for initial testing with a given system.

- Must be > 0.

task_space_planning_params/nn_translation_distance_weight (float)

- For pose targets, nearest neighbor distances are computed by linearly weighting translation and orientation distance by nn_translation_distance_weight and nn_orientation_distance_weight.

- Nearest neighbor search is used to select the node from which the tree of valid configurations will be expanded.

- A default value of 1.0 is recommended as a starting value for initial testing with a given system.

- Must be > 0.

task_space_planning_params/nn_orientation_distance_weight (float)

- For pose targets, nearest neighbor distances are computed by linearly weighting translation and orientation distance by nn_translation_distance_weight and nn_orientation_distance_weight.

- Nearest neighbor search is used to select the node from which the tree of valid configurations will be expanded.

- A default value of 0.125 is recommended as a starting value for initial testing with a given system.

- Must be > 0.

task_space_planning_params/task_space_exploitation_fraction (float)

- Fraction of iterations for which tree is extended towards target position in task space.

- Must be in range [0, 1]. Additionally, the sum of task_space_exploitation_fraction and task_space_exploration_fraction must be <= 1.

- A default value of 0.4 is recommended as a starting value for initial testing with a given system.

task_space_planning_params/task_space_exploration_fraction (float)

- Fraction of iterations for which tree is extended towards random position in task space.

- Must be in range [0, 1]. Additionally, the sum of task_space_exploitation_fraction and task_space_exploration_fraction must be <= 1.

- A default value of 0.1 is recommended as a starting value for initial testing with a given system.

The remaining fraction beyond task_space_exploitation_fraction and task_space_exploration_fraction is a c_space_exploration_fraction that is implicitly defined as:
1 - (task_space_exploitation_fraction + task_space_exploration_fraction)
In general, easier path searches will take less time with higher exploitation fraction while more difficult searches will waste time if the exploitation fraction is too high and benefit from greater combined exploration fraction.

task_space_planning_params/max_extension_substeps_away_from_target (int)

- Maximum number of Jacobian transpose gradient descent substeps that may be taken while the end effector is away from the task-space target.

- The threshold for nearness is determined by the extension_substep_target_region_scale_factor parameter.

- A default value of 6 is recommended as a starting value for initial testing with a given system.

task_space_planning_params/max_extension_substeps_near_target (int)

- Maximum number of Jacobian transpose gradient descent substeps that may be taken while the end effector is near the task-space target.

- The threshold for nearness is determined by the extension_substep_target_region_scale_factor parameter.

- A default value of 50 is recommended as a starting value for initial testing with a given system.

task_space_planning_params/extension_substep_target_region_scale_factor(float)

- A scale factor used to determine whether the end effector is close enough to the target to change the amount of gradient descent substeps allowed when adding a node in RRT.

- The max_extension_substeps_near_target parameter is used when the distance (i.e., L2 norm) between the end effector and target position is less than extension_substep_target_region_scale_factor * x_zone_target_tolerance.

- Must be greater than or equal to 1.0; a value of 1.0 effectively disables the max_extension_substeps_near_target parameter.

- A default value of 2.0 is recommended as a starting value for initial testing with a given system.

Parameters:

- param_name (str) – Name of parameter

- value (Union[np.ndarray[np.float64],float,int,str]) – value of parameter

Returns:
True if the parameter was set successfully

Return type:
bool

set_random_seed(random_seed:int)→None
Set the random seed that RRT uses to generate a solution
Parameters:
random_seed (int) – Used to initialize random sampling. random_seed must be positive.

set_robot_base_pose(
robot_position:array,
robot_orientation:array,
)→None Update position of the robot base. Until this function is called, Lula will assume the base pose to be at the origin with identity rotation.
Parameters:

- robot_position (np.array) – (3 x 1) translation vector describing the translation of the robot base relative to the USD stage origin. The translation vector should be specified in the units of the USD stage

- robot_orientation (np.array) – (4 x 1) quaternion describing the orientation of the robot base relative to the USD stage global frame

update_world(updated_obstacles:List=None)→None
Update the internal world state of Lula. This function automatically tracks the positions of obstacles that have been added with add_obstacle()
Parameters:
updated_obstacles (List[core.objects], optional) – Obstacles that have been added by add_obstacle() that need to be updated. If not specified, all non-static obstacle positions will be updated. If specified, only the obstacles that have been listed will have their positions updated

### Trajectory
classTrajectory
Bases: `object`
Interface class for defining a continuous-time trajectory for a robot in Isaac Sim. A Trajectory may be passed to an ArticulationTrajectory to have its continuous-time output discretized and converted to a ArticulationActions.
get_active_joints()→List[str]
Active joints are directly controlled by this Trajectory
A Trajectory may be specified for only a subset of the joints in a robot Articulation. For example, it may include the DOFs in a robot arm, but not in the gripper.
Returns:
Names of active joints. The order of joints in this list determines the order in which a
Trajectory will return joint targets for the robot.

Return type:
List[str]

get_joint_targets(
time:float,
)→Tuple[array,array]Return joint targets for the robot at the given time. The Trajectory interface assumes trajectories to be represented continuously between a start time and end time. In instance of this class that internally generates discrete time trajectories will need to implement some form of interpolation for times that have not been computed.
Parameters:
time (float) – Time in trajectory at which to return joint targets.

Returns:
joint position targets for the active robot joints
joint velocity targets for the active robot joints

Return type:
Tuple[np.array,np.array]

propertyend_time:float
Return the end time of the trajectory
Returns:
End time of the trajectory

Return type:
float

propertystart_time:float
Return the start time of the trajectory.
Returns:
Start time of the trajectory.

Return type:
float

classLulaTrajectory(trajectory, active_joints)
Bases: Trajectory
Instance of Trajectory interface class for handling lula.Trajectory objects
Parameters:
trajectory (lula.Trajectory ) – C-space trajectory defined continuously

get_active_joints()→List[str]
Active joints are directly controlled by this Trajectory
A Trajectory may be specified for only a subset of the joints in a robot Articulation. For example, it may include the DOFs in a robot arm, but not in the gripper.
Returns:
Names of active joints. The order of joints in this list determines the order in which a
Trajectory will return joint targets for the robot.

Return type:
List[str]

get_joint_targets(
time,
)→Tuple[array,array]Return joint targets for the robot at the given time. The Trajectory interface assumes trajectories to be represented continuously between a start time and end time. In instance of this class that internally generates discrete time trajectories will need to implement some form of interpolation for times that have not been computed.
Parameters:
time (float) – Time in trajectory at which to return joint targets.

Returns:
joint position targets for the active robot joints
joint velocity targets for the active robot joints

Return type:
Tuple[np.array,np.array]

propertyend_time:float
Return the end time of the trajectory
Returns:
End time of the trajectory

Return type:
float

propertystart_time:float
Return the start time of the trajectory.
Returns:
Start time of the trajectory.

Return type:
float

### Lula Trajectory Generators
classLulaCSpaceTrajectoryGenerator(
robot_description_path:str,
urdf_path:str,
)Bases: `object`
LulaCSpaceTrajectoryGenerator is a class for generating time-optimal trajectories that connect a series of provided c-space waypoints.
Parameters:

- robot_description_path (str) – path to a robot description yaml file

- urdf_path (str) – path to robot urdf

compute_c_space_trajectory(
waypoint_positions:array,
)→LulaTrajectory Produce a trajectory from a set of provided c_space waypoint positions. The resulting trajectory will use spline-based interpolation to connect the waypoints with an initial and final velocity of 0. The trajectory is time-optimal: i.e. either the velocity, acceleration, or jerk limits are saturated at any given time to produce as trajectory with as short a duration as possible.
Parameters:
waypoint_positions (np.array) – Set of c-space coordinates cooresponding to the output of get_active_joints(). The expected shape is (N x k) where N is the number of waypoints and k is the number of active joints.

Returns:
Instance of the Trajectory class which specifies continuous joint_targets for the active joints over a span of time.
If a trajectory could not be produced, None will be returned.

Return type:
LulaTrajectory

compute_timestamped_c_space_trajectory(
waypoint_positions:array,
timestamps:array,
interpolation_mode:str='cubic_spline',
)→LulaTrajectory Compute a trajectory where each c_space waypoint has a corresponding timestamp that will be exactly matched. The resulting trajectory will use spline-based interpolation to connect the waypoints with an initial and final velocity of 0.
Parameters:

- waypoint_positions (np.array) – Set of c-space coordinates cooresponding to the output of get_active_joints(). The expected shape is (N x k) where N is the number of waypoints and k is the number of active joints.

- timestamps (np.array) – Set of timestamps corresponding to the waypoint positions argument with an expected shape of (Nx1).

- interpolation_mode (str, optional) – The type of interpolation to be used between waypoints. The available options are “cubic_spline” and “linear”. Defaults to “cubic”.

Returns:
Instance of the Trajectory class which specifies continuous joint_targets for the active joints over a span of time.
If a trajectory could not be produced, None will be returned.

Return type:
LulaTrajectory

get_active_joints()→List[str]
Return the list of joints by name that are considered to be controllable by the TrajectoryGenerator. All inputs and outputs of the LulaTrajectoryGenerator correspond to the joints specified by get_active_joints().
Returns:
List of joints that are used to generate the desired trajectory.

Return type:
List[str]

get_c_space_acceleration_limits()
Get the acceleration limits of the active joints that are used when generating a trajectory
Returns:
Acceleration limits of active joints.

Return type:
acceleration limits (np.array)

get_c_space_jerk_limits()
Get the jerk limits of the active joints that are used when generating a trajectory
Returns:
Jerk limits of active joints.

Return type:
jerk limits (np.array)

get_c_space_position_limits()
Get the position limits of the active joints that are used when generating a trajectory
Returns:
Position limits of active joints.

Return type:
position limits (np.array)

get_c_space_velocity_limits()
Get the velocity limits of the active joints that are used when generating a trajectory
Returns:
Velocity limits of active joints.

Return type:
velocity limits (np.array)

set_c_space_acceleration_limits(
acceleration_limits:array,
)→None Set the acceleration limits of the active joints to be used when generating a trajectory.
Parameters:
acceleration_limits (np.array) – Acceleration limits of active joints.

set_c_space_jerk_limits(
jerk_limits:array,
)→None Set the jerk limits of the active joints to be used when generating a trajectory.
Parameters:
jerk_limits (np.array) – Jerk limits of active joints.

set_c_space_position_limits(
lower_position_limits:array,
upper_position_limits:array,
)→None Set the lower and upper position limits of the active joints to be used when generating a trajectory.
Parameters:

- lower_position_limits (np.array) – Lower position limits of active joints.

- upper_position_limits (np.array) – Upper position limits of active joints.

set_c_space_velocity_limits(
velocity_limits:array,
)→None Set the velocity limits of the active joints to be used when generating a trajectory.
Parameters:
velocity_limits (np.array) – Velocity limits of active joints.

set_solver_param(
param_name:str,
param_val:int|float|str,
)Set solver parameters for the cspace trajectory generator. A complete list of parameters is provided in this docstring.
‘max_segment_iterations’: (int)
In general, a trajectory is locally time-optimal if at least one derivative for one of the c-space coordinates is fully saturated, with no derivative limits for any of the c-space coordinates exceeded.
This time-optimality can be enforced for each CubicSpline segment or for each PiecewiseCubicSpline as a whole. The former will, in general, generate trajectories with smaller spans, but will require more expensive iterations (and thus more time) to converge. The latter will, in general, require less iterations (and thus less time) to converge, but the generated trajectories will tend to have longer spans.
When attempting to find a time-optimal trajectory, the (more expensive) per-segment method will first be attempted for max_per_segment_iterations. Then, if not yet converged, the method acting on the entire spline will be attempted for max_aggregate_iterations.
To maximize speed, max_segment_iterations should be relatively low (or even zero to remove this search completely). To maximize time-optimality of the generated trajectory, max_segment_iterations should be relatively high.
The sum of max_segment_iterations and max_aggregate_iterations must be at least 1

‘max_aggragate_iterations’: (int)
See max_segment_iterations

‘convergence_dt’: (float)
The search for optimal time values will terminate if the maximum change to any time value during a given iteration is less than the convergence_dt.
convergence_dt must be positive.

‘max_dilation_iterations’: (int)
After the segment-wise and/or aggregate time-optimal search has converged or reached maximum iterations, the resulting set of splines will be tested to see if any derivative limits are exceeded.
If any derivative limits are exceeded, the splines will be iteratively scaled in time to reduce the maximum achieved derivative. This process will repeat until no derivative limits are exceeded (success) or max_dilation_iterations_ are reached (failure). For a well-tuned set of solver parameters, very few dilation steps should be required (often none will be required or a single iteration is sufficient to bring a slightly over-saturated trajectory within the derivative limits).

‘dilation_dt’: (float)
For the iterative dilation step described in setMaxDilationIterations() documentation, the dilation_dt is the “epsilon” value added to the span of the trajectory that exceeds derivative limits.
dilation_dt must be positive.

‘min_time_span’: (float)
Specify the minimum allowable time span between adjacent waypoints/endpoints. min_time_span must be positive.
This is most likely to affect the time span between the endpoints and “free-position” points that are used to enable acceleration bound constraints. If no jerk limit is provided, these free-position points may tend to become arbitrarily close in position and time to the endpoints. This min_time_span prevents this time span from approaching zero.
In general, a jerk limit is recommended for preventing abrupt changes in acceleration rather than relying on the min_time_span for this purpose.

‘time_split_method’: (string)
Often waypoints for a trajectory may specify positions without providing time values for when these waypoint position should be attained. In this case, we can use the distance between waypoints to assign time values for each waypoint.
Assuming a unitary time domain s.t. t_0 = 0 and t_N = 1, we can assign the intermediate time values according to:
t_k = t_(k-1) + (d_k / d),

where d = sum(d_k) for k = [0, N-1] and N is the number of points.
Many options exist for the computing the distance metric d_k, with common options described below (and implemented in ComputeTimeValues(). See Eqn 4.37 in “Trajectory Planning for Automatic Machines and Robots” (2008) by Biagiotti & Melchiorri for more detailed motivations. Valid distribution choices are given below:
‘uniform’:
For a “uniform distribution” w.r.t time, the positions are ignored and d_k can simply be computed as:
d_k = 1 / (N - 1)

resulting in uniform time intervals between all points.

‘chord_length’:
For a “chord length distribution”, the time intervals between waypoints are proportional to the Euclidean distance between waypoints:
d_k = |q_(k+1) - q_k|

where q represents the position of the waypoint.

‘centripetal’:
For a “centripetal distribution”, the time intervals between waypoints are proportional to the square root of the Euclidean distance between waypoints:
d_k = |q_(k+1) - q_k|^(1/2)

where q represents the position of the waypoint.

Parameters:

- param_name (str) – Parameter name from the above list of parameters

- param_val (Union[int, float, str]) – Value to which the given parameter will be set

classLulaTaskSpaceTrajectoryGenerator(
robot_description_path:str,
urdf_path:str,
)Bases: `object`
compute_task_space_trajectory_from_path_spec(
path_spec:CompositePathSpec |TaskSpacePathSpec ,
frame_name:str,
)→LulaTrajectory Return a LulaTrajectory that follows the path specified by the provided TaskSpacePathSpec
Parameters:

- task_space_path_spec (lula.TaskSpacePathSpec , lula.CompositePathSpec ) – An object describing a taskspace path

- frame_name (str) – Name of the end effector frame

Returns:
Instance of the isaacsim.robot_motion.motion_generation.Trajectory class. If no trajectory could be generated, None is returned.

Return type:
LulaTrajectory

compute_task_space_trajectory_from_points(
positions:array,
orientations:array,
frame_name:str,
)→LulaTrajectory Return a LulaTrajectory that connects the provided positions and orientations at the specified frame in the robot. Points will be connected linearly in space.
Parameters:

- positions (np.array) – Taskspace positions that the robot end effector should pass through with shape (N x 3) where N is the number of provided positions. Positions is assumed to be in meters.

- orientations (np.array) – Taskspace quaternion orientations that the robot end effector should pass through with shape (N x 4) where N is the number of provided orientations. The length of this argument must match the length of the positions argument.

- frame_name (str) – Name of the end effector frame in the robot URDF.

Returns:
Instance of the isaacsim.robot_motion.motion_generation.Trajectory class. If no trajectory could be generated, None is returned.

Return type:
LulaTrajectory

get_active_joints()→List[str]
Return the list of joints by name that are considered to be controllable by the TrajectoryGenerator. All inputs and outputs of the LulaTrajectoryGenerator correspond to the joints specified by get_active_joints().
Returns:
List of joints that are used to generate the desired trajectory.

Return type:
List[str]

get_all_frame_names()→List[str]
Return a list of all frames in the robot URDF that may be used to follow a trajectory
Returns:
List of all frame names in the robot URDF

Return type:
List[str]

get_c_space_acceleration_limits()
Get the acceleration limits of the active joints that are used when generating a trajectory
Returns:
Acceleration limits of active joints.

Return type:
acceleration limits (np.array)

get_c_space_jerk_limits()
Get the jerk limits of the active joints that are used when generating a trajectory
Returns:
Jerk limits of active joints.

Return type:
jerk limits (np.array)

get_c_space_position_limits()
Get the position limits of the active joints that are used when generating a trajectory
Returns:
Position limits of active joints.

Return type:
position limits (np.array)

get_c_space_velocity_limits()
Get the velocity limits of the active joints that are used when generating a trajectory
Returns:
Velocity limits of active joints.

Return type:
velocity limits (np.array)

get_path_conversion_config()→TaskSpacePathConversionConfig
Get a reference to the config object that lula uses to convert task-space paths to c-space paths.
The values of the returned TaskSpacePathConversionConfig object can be modified directly to affect lula task-space path conversions. See help(lula.TaskSpacePathConversionConfig) for a detailed description of the editable parameters.
Returns:
Configuration class for converting from task-space paths to c-space paths.

Return type:
lula.TaskSpacePathConversionConfig

set_c_space_acceleration_limits(
acceleration_limits:array,
)→None Set the acceleration limits of the active joints to be used when generating a trajectory.
Parameters:
acceleration_limits (np.array) – Acceleration limits of active joints.

set_c_space_jerk_limits(
jerk_limits:array,
)→None Set the jerk limits of the active joints to be used when generating a trajectory.
Parameters:
jerk_limits (np.array) – Jerk limits of active joints.

set_c_space_position_limits(
lower_position_limits:array,
upper_position_limits:array,
)→None Set the lower and upper position limits of the active joints to be used when generating a trajectory.
Parameters:

- lower_position_limits (np.array) – Lower position limits of active joints.

- upper_position_limits (np.array) – Upper position limits of active joints.

set_c_space_trajectory_generator_solver_param(
param_name:str,
param_val:int|float|str,
)Set solver parameters for the cspace trajectory generator. A complete list of parameters is provided in this docstring.
‘max_segment_iterations’: (int)
In general, a trajectory is locally time-optimal if at least one derivative for one of the c-space coordinates is fully saturated, with no derivative limits for any of the c-space coordinates exceeded.
This time-optimality can be enforced for each CubicSpline segment or for each PiecewiseCubicSpline as a whole. The former will, in general, generate trajectories with smaller spans, but will require more expensive iterations (and thus more time) to converge. The latter will, in general, require less iterations (and thus less time) to converge, but the generated trajectories will tend to have longer spans.
When attempting to find a time-optimal trajectory, the (more expensive) per-segment method will first be attempted for max_per_segment_iterations. Then, if not yet converged, the method acting on the entire spline will be attempted for max_aggregate_iterations.
To maximize speed, max_segment_iterations should be relatively low (or even zero to remove this search completely). To maximize time-optimality of the generated trajectory, max_segment_iterations should be relatively high.
The sum of max_segment_iterations and max_aggregate_iterations must be at least 1

‘max_aggragate_iterations’: (int)
See max_segment_iterations

‘convergence_dt’: (float)
The search for optimal time values will terminate if the maximum change to any time value during a given iteration is less than the convergence_dt.
convergence_dt must be positive.

‘max_dilation_iterations’: (int)
After the segment-wise and/or aggregate time-optimal search has converged or reached maximum iterations, the resulting set of splines will be tested to see if any derivative limits are exceeded.
If any derivative limits are exceeded, the splines will be iteratively scaled in time to reduce the maximum achieved derivative. This process will repeat until no derivative limits are exceeded (success) or max_dilation_iterations_ are reached (failure). For a well-tuned set of solver parameters, very few dilation steps should be required (often none will be required or a single iteration is sufficient to bring a slightly over-saturated trajectory within the derivative limits).

‘dilation_dt’: (float)
For the iterative dilation step described in setMaxDilationIterations() documentation, the dilation_dt is the “epsilon” value added to the span of the trajectory that exceeds derivative limits.
dilation_dt must be positive.

‘min_time_span’: (float)
Specify the minimum allowable time span between adjacent waypoints/endpoints. min_time_span must be positive.
This is most likely to affect the time span between the endpoints and “free-position” points that are used to enable acceleration bound constraints. If no jerk limit is provided, these free-position points may tend to become arbitrarily close in position and time to the endpoints. This min_time_span prevents this time span from approaching zero.
In general, a jerk limit is recommended for preventing abrupt changes in acceleration rather than relying on the min_time_span for this purpose.

‘time_split_method’: (string)
Often waypoints for a trajectory may specify positions without providing time values for when these waypoint position should be attained. In this case, we can use the distance between waypoints to assign time values for each waypoint.
Assuming a unitary time domain s.t. t_0 = 0 and t_N = 1, we can assign the intermediate time values according to:
t_k = t_(k-1) + (d_k / d),

where d = sum(d_k) for k = [0, N-1] and N is the number of points.
Many options exist for the computing the distance metric d_k, with common options described below (and implemented in ComputeTimeValues(). See Eqn 4.37 in “Trajectory Planning for Automatic Machines and Robots” (2008) by Biagiotti & Melchiorri for more detailed motivations. Valid distribution choices are given below:
‘uniform’:
For a “uniform distribution” w.r.t time, the positions are ignored and d_k can simply be computed as:
d_k = 1 / (N - 1)

resulting in uniform time intervals between all points.

‘chord_length’:
For a “chord length distribution”, the time intervals between waypoints are proportional to the Euclidean distance between waypoints:
d_k = |q_(k+1) - q_k|

where q represents the position of the waypoint.

‘centripetal’:
For a “centripetal distribution”, the time intervals between waypoints are proportional to the square root of the Euclidean distance between waypoints:
d_k = |q_(k+1) - q_k|^(1/2)

where q represents the position of the waypoint.

Parameters:

- param_name (str) – Parameter name from the above list of parameters

- param_val (Union[int, float, str]) – Value to which the given parameter will be set

set_c_space_velocity_limits(
velocity_limits:array,
)→None Set the velocity limits of the active joints to be used when generating a trajectory.
Parameters:
velocity_limits (np.array) – Velocity limits of active joints.

### Articulation Trajectory
classArticulationTrajectory(
robot_articulation:SingleArticulation ,
trajectory:Trajectory ,
physics_dt:float,
)Bases: `object`
Wrapper class which takes in a Trajectory object and converts the output to discrete ArticulationActions that may be sent to the provided robot Articulation.
Parameters:

- robot_articulation (SingleArticulation ) – Initialized robot Articulation object representing the simulated USD robot

- trajectory (Trajectory ) – An instance of a class that implements the Trajectory interface.

- physics_dt (float) – Duration of a physics step in Isaac Sim (typically 1/60 s).

get_action_at_time(
time:float,
)→ArticulationAction Get an ArticulationAction that will send the robot to the desired position/velocity at a given time in the provided Trajectory.
Parameters:
time (float) – Time between the start and end times in the provided Trajectory. If the time is out of bounds, an error will be thrown.

Returns:
ArticulationAction that may be passed directly to the robot Articulation to send it to the desired position/velocity at the given time.

Return type:
ArticulationAction

get_action_sequence(
timestep:float=None,
)→List[ArticulationAction ]Get a sequence of ArticulationActions which sample the entire Trajectory according to the provided timestep.
Parameters:
timestep (float, optional) – Timestep used for sampling the provided Trajectory. A vlue of 1/60, for example, returns ArticulationActions that represent the desired position/velocity of the robot at 1/60 second intervals. I.e. a one second trajectory with timestep=1/60 would result in 60 ArticulationActions. When not provided, the framerate of Isaac Sim is used. Defaults to None.

Returns:
Sequence of ArticulationActions that may be passed to the robot Articulation to produce the desired trajectory.

Return type:
List[ArticulationAction ]

get_active_joints_subset()→ArticulationSubset
Get view into active joints
Returns:
Returns robot states for active joints in an order compatible with the TrajectoryGenerator

Return type:
ArticulationSubset

get_robot_articulation()→SingleArticulation
Get the robot Articulation
Returns:
Articulation object describing the robot.

Return type:
SingleArticulation

get_trajectory()→Trajectory
get_trajectory_duration()→float
Returns the duration of the provided Trajectory
Returns:
Duration of the provided trajectory

Return type:
float

### Motion Policy Base Controller
classMotionPolicyController(
name:str,
articulation_motion_policy:ArticulationMotionPolicy ,
)Bases: BaseController
A Controller that steps using an arbitrary MotionPolicy
Parameters:

- name (str) – name of this controller

- articulation_motion_policy (ArticulationMotionPolicy ) – a wrapper around a MotionPolicy for computing ArticulationActions that can be directly applied to the robot

add_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
static:bool=False,
)→None Add an object from isaacsim.core.api.objects as an obstacle to the motion_policy
Parameters:

- obstacle (isaacsim.core.api.objects) – Dynamic, Visual, or Fixed object from isaacsim.core.api.objects

- static (bool) – If True, the obstacle may be assumed by the MotionPolicy to remain stationary over time

forward(
target_end_effector_position:ndarray,
target_end_effector_orientation:ndarray|None =None,
)→ArticulationAction Compute an ArticulationAction representing the desired robot state for the next simulation frame
Parameters:

- target_translation (nd.array) – Translation vector (3x1) for robot end effector. Target translation should be specified in the same units as the USD stage, relative to the stage origin.

- target_orientation (Optional[np.ndarray], optional) – Quaternion of desired rotation for robot end effector relative to USD stage global frame. Target orientation defaults to None, which means that the robot may reach the target with any orientation.

Returns:
A wrapper object containing the desired next state for the robot

Return type:
ArticulationAction

get_articulation_motion_policy()→ArticulationMotionPolicy
Get ArticulationMotionPolicy that was passed to this class on initialization
Returns:
a wrapper around a MotionPolicy for computing ArticulationActions that can be directly applied to the robot

Return type:
ArticulationMotionPolicy

get_motion_policy()→MotionPolicy
Get MotionPolicy object that is being used to generate robot motions
Returns:
An instance of a MotionPolicy that is being used to compute robot motions

Return type:
MotionPolicy

remove_obstacle(
obstacle:<module'isaacsim.core.api.objects'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>,
)→None Remove and added obstacle from the motion_policy
Parameters:
obstacle (isaacsim.core.api.objects) – Object from isaacsim.core.api.objects that has been added to the motion_policy

reset()→None
