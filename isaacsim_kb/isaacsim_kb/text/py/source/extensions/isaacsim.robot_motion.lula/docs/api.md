<!-- source: py/source/extensions/isaacsim.robot_motion.lula/docs/api.html | title: API — Isaac Sim -->

# API

## Python API
The lula module provides a high-level interface to the Lula library, with classes exposing routines for forward and inverse kinematics, sampling-based global planning, and smooth reactive motion generation via RMPflow and geometric fabrics.
Logging

[TABLE]
LogLevel | Logging levels, ordered from least to most verbose.
[/TABLE]
Rotations and Poses

[TABLE]
Rotation3 | Representation of a rotation (i.e. element of SO(3)) in 3D.
Pose3 | Representation of a pose (i.e. element of SE(3)) in 3D.
[/TABLE]
Robot Specification

[TABLE]
RobotDescription | Robot description, consisting of geometric and kinematic properties of a robot.
load_robot | Load a robot description from a YAML file ( robot_description_file ) and a URDF ( robot_urdf ).
load_robot_from_memory | Load a robot description from the contents of a YAML file ( robot_description_file ) and the contents of a URDF ( robot_urdf ).
[/TABLE]
World Specification

[TABLE]
Obstacle | Geometric primitive.
create_obstacle | Create an obstacle.
World | Represents a collection of obstacles.
create_world | Create a new, empty world.
WorldView | Represents a view of a lula.World .
[/TABLE]
Kinematics

[TABLE]
CyclicCoordDescentIkConfig | Configuration parameters for CCD inverse kinematics solver.
CyclicCoordDescentIkResults | Results returned by CCD inverse kinematics solver.
compute_ik_ccd | Attempt to solve inverse kinematics using cyclic coordinate descent.
[/TABLE]
Path Specification

[TABLE]
CSpacePathSpec | Procedurally specify a CSpacePathSpec from a series of configuration space waypoints
create_c_space_path_spec | Create a 'CSpacePathSpec' with the specified 'initial_c_space_position'.
TaskSpacePathSpec | Procedurally compose a TaskSpacePathSpec from a series of continuous task space segments
create_task_space_path_spec | Create a 'TaskSpacePathSpec' with the specified 'initial_pose'.
CompositePathSpec | Procedurally compose 'CSpacePathSpec' and 'TaskSpacePathSpec' segments into a single path specification.
create_composite_path_spec | Create a 'CompositePathSpec' with the specified 'initial_c_space_position'.
load_c_space_path_spec_from_file | Load a 'CSpacePathSpec' from file with absolute path 'c_space_path_spec_file'.
load_c_space_path_spec_from_memory | Load a 'CSpacePathSpec' from the contents of a YAML file ('c_space_path_spec_yaml').
export_c_space_path_spec_to_memory | Export 'c_space_path_spec' as a string.
load_task_space_path_spec_from_file | Load a 'TaskSpacePathSpec' from file with absolute path 'task_space_path_spec_file'.
load_task_space_path_spec_from_memory | Load a 'TaskSpacePathSpec' from the contents of a YAML file ('task_space_path_spec_yaml').
export_task_space_path_spec_to_memory | Export 'task_space_path_spec' as a string.
load_composite_path_spec_from_file | Load a 'CompositePathSpec' from file with absolute path 'composite_path_spec_file'.
load_composite_path_spec_from_memory | Load a 'CompositePathSpec' from the contents of a YAML file ('composite_path_spec_yaml').
export_composite_path_spec_to_memory | Export 'composite_path_spec' as a string.
[/TABLE]
Path Generation

[TABLE]
CSpacePath | Represent a path through configuration space (i.e., c-space or "joint space").
LinearCSpacePath | Represent a path linearly interpolated through configuration space (i.e., c-space) waypoints.
create_linear_c_space_path | Create a 'LinearCSpacePath' from a c-space path specification.
TaskSpacePath | Represent a path through task space (i.e., SE(3) group representing 6-dof poses).
TaskSpacePathConversionConfig | Configuration parameters for converting a 'TaskSpacePathSpec' into a series of c-space configurations.
convert_composite_path_spec_to_c_space | Convert a composite_path_spec into a linear c-space path.
convert_task_space_path_spec_to_c_space | Convert a task_space_path_spec into a linear c-space path.
[/TABLE]
Trajectory Generation

[TABLE]
Trajectory | Represent a path through configuration space (i.e., "c-space") parameterized by time.
CSpaceTrajectoryGenerator | Configure a trajectory generator that can compute smooth trajectories.
create_c_space_trajectory_generator | Overloaded function.
[/TABLE]
Collision Sphere Generation

[TABLE]
CollisionSphereGenerator | Configure a generator that can generate spheres to approximate mesh volumes.
create_collision_sphere_generator | Create a CollisionSphereGenerator to generate spheres that approximate the volume of a mesh represented by vertices and triangles .
[/TABLE]
Motion Planning

[TABLE]
MotionPlanner | Interface for planning collision-free paths for robotic manipulators.
create_motion_planner | Overloaded function.
[/TABLE]
RmpFlow

[TABLE]
RmpFlowConfig | RMPflow configuration, including parameters and robot description.
create_rmpflow_config | Create an RMPflow configuration object.
create_rmpflow_config_from_memory |
RmpFlow | Interface for building and evaluating an RMPflow motion policy.
create_rmpflow | Create an instance of the RmpFlow interface from an RMPflow configuration.
[/TABLE]

### Logging
classLogLevel
Logging levels, ordered from least to most verbose.
Members:
FATAL
ERROR
WARNING
INFO
VERBOSE

FATAL
Logging level for nonrecoverable errors (minimum level, so always enabled).

ERROR
Logging level for recoverable errors.

WARNING
Logging level for warnings, indicating possible cause for concern.

INFO
Logging level for informational messages.

VERBOSE
Logging level for highly verbose informational messages.

set_log_level(level:lula.LogLevel=<LogLevel.ERROR:1>)→None
Suppress output for all log messages with associated verbosity higher than log_level.

### Rotations and Poses
classRotation3
Bases: `pybind11_object`
Representation of a rotation (i.e. element of SO(3)) in 3D.
staticdistance(
rotation0:lula.Rotation3 ,
rotation1:lula.Rotation3 ,
)→floatCompute the minimum angular distance (in radians) between two rotations.

staticfrom_scaled_axis(
scaled_axis:numpy.ndarray[numpy.float64[3,1]],
)→lula.Rotation3 Construct a rotation from a scaled axis, where the magnitude of scaled_axis represents the rotation angle in radians.

staticidentity()→lula.Rotation3
Create identity rotation.

inverse(self:lula.Rotation3 )→lula.Rotation3
Returns the inverse rotation.

matrix(
self:lula.Rotation3 ,
)→numpy.ndarray[numpy.float64[3,3]]Return matrix representation of the rotation.

scaled_axis(
self:lula.Rotation3 ,
)→numpy.ndarray[numpy.float64[3,1]]Return scaled axis represetation of the rotation where magnitude of the returned vector represents the rotation angle in radians.

staticslerp(
rotation0:lula.Rotation3 ,
rotation1:lula.Rotation3 ,
t:float,
)→lula.Rotation3 Smoothly interpolate between two rotations using spherical linear interpolation (“slerp”).

w(self:lula.Rotation3 )→float
Return w component of the quaternion represention of the rotation.

x(self:lula.Rotation3 )→float
Return x component of the quaternion represention of the rotation.

y(self:lula.Rotation3 )→float
Return y component of the quaternion represention of the rotation.

z(self:lula.Rotation3 )→float
Return z component of the quaternion represention of the rotation.

classPose3
Bases: `pybind11_object`
Representation of a pose (i.e. element of SE(3)) in 3D.
staticfrom_rotation(rotation:lula::Rotation3)→lula.Pose3
Create a pure rotational pose

staticfrom_translation(
translation:numpy.ndarray[numpy.float64[3,1]],
)→lula.Pose3 Create a pure translational pose.

staticidentity()→lula.Pose3
Create identity pose.

inverse(self:lula.Pose3 )→lula.Pose3
Return the inverse pose.

matrix(self:lula.Pose3 )→numpy.ndarray[numpy.float64[4,4]]
Return matrix representation of the pose.

propertyrotation
Rotation component of pose.

propertytranslation
Translation component of pose.

### Robot Specification
classRobotDescription
Bases: `pybind11_object`
Robot description, consisting of geometric and kinematic properties of a robot.
c_space_coord_name(
self:lula.RobotDescription ,
coord_index:int,
)→strReturn the name of a given joint of the robot.

default_c_space_configuration(
self:lula.RobotDescription ,
)→numpy.ndarray[numpy.float64[m,1]]Return default joint positions for the robot.

kinematics(
self:lula.RobotDescription ,
)→lula.Kinematics Return the robot kinematics.

num_c_space_coords(
self:lula.RobotDescription ,
)→intReturn the number of actuated joints for the robot.

load_robot(
robot_description_file:str,
robot_urdf:str,
)→lula.RobotDescription Load a robot description from a YAML file (robot_description_file) and a URDF (robot_urdf).

load_robot_from_memory(
robot_description:str,
robot_urdf:str,
)→lula.RobotDescription Load a robot description from the contents of a YAML file (robot_description_file) and the contents of a URDF (robot_urdf).

### World Specification
classObstacle
Bases: `pybind11_object`
Geometric primitive.
Note
Currently, the CYLINDER obstacle type is internally represented as a capsule (i.e., a cylinder with two hemispherical end caps) extending beyond the nominal HEIGHT. This will be corrected in a future release.
classAttribute
Bases: `pybind11_object`
Members:
HEIGHT
RADIUS
SIDE_LENGTHS
HEIGHT=<Attribute.HEIGHT:0>
RADIUS=<Attribute.RADIUS:1>
SIDE_LENGTHS=<Attribute.SIDE_LENGTHS:2>
propertyname
propertyvalue

classAttributeValue
Bases: `pybind11_object`

classType
Bases: `pybind11_object`
Members:
CUBE
CYLINDER
SPHERE
CUBE=<Type.CUBE:0>
CYLINDER=<Type.CYLINDER:1>
SPHERE=<Type.SPHERE:2>
propertyname
propertyvalue

set_attribute(
self:lula.Obstacle,
attribute:lula::Obstacle::Attribute,
value:lula::Obstacle::AttributeValue,
)→None Set attribute for obstacle

type(self:lula.Obstacle )→lula::Obstacle::Type
Return the type of the obstacle.

create_obstacle(type:lula.Obstacle.Type )→lula.Obstacle
Create an obstacle.

classWorld
Bases: `pybind11_object`
Represents a collection of obstacles.
classObstacleHandle
Bases: `pybind11_object`

add_obstacle(
self:lula.World ,
obstacle:lula.Obstacle ,
pose:lula.Pose3 |None =None,
)→lula::World::ObstacleHandleAdd obstacle to the world.

add_world_view(self:lula.World )→lula::WorldView
Create a view into the world that can be used for collision checks and distance evaluations.

disable_obstacle(
self:lula.World,
obstacle:lula::World::ObstacleHandle,
)→None Disable an obstacle for the purpose of collision checks and distance evaluations.

enable_obstacle(
self:lula.World,
obstacle:lula::World::ObstacleHandle,
)→None Enable an obstacle for the purpose of collision checks and distance evaluations.

remove_obstacle(
self:lula.World,
obstacle:lula::World::ObstacleHandle,
)→None Permanently remove obstacle, invalidating its handle.

set_pose(
self:lula.World,
obstacle:lula::World::ObstacleHandle,
pose:lula.Pose3,
)→None Set the pose of the given obstacle.

create_world()→lula.World
Create a new, empty world.

classWorldView
Bases: `pybind11_object`
Represents a view of a lula.World.
distance_to(
self:lula.WorldView ,
obstacle:lula.World.ObstacleHandle ,
point:numpy.ndarray[numpy.float64[3,1]],
gradient:numpy.ndarray[numpy.float64[3,1],flags.writeable]|None =None,
)→floatCalculate the distance from point to the obstacle specified by obstacle.

distances_to(
self:lula.WorldView ,
point:numpy.ndarray[numpy.float64[3,1]],
compute_distance_gradients:bool=True,
)→tuple[list[float],list[numpy.ndarray[numpy.float64[3,1]]]|None ]Calculate distances from point to all enabled obstacles.

in_collision(*args, **kwargs)
Overloaded function.

- in_collision(self: lula.WorldView, center: numpy.ndarray[numpy.float64[3, 1]], radius: float) -> bool

Test whether a sphere defined by center and radius is in collision with any enabled obstacles in the world.

- in_collision(self: lula.WorldView, obstacle: lula.World.ObstacleHandle, center: numpy.ndarray[numpy.float64[3, 1]], radius: float) -> bool

Test whether a sphere defined by center and radius is in collision with the obstacle specified by obstacle.

num_enabled_obstacles(self:lula.WorldView )→int
Return the number of enabled obstacles in the current view of the world.

update(self:lula.WorldView )→None
Update WorldView such that any changes to the underlying world are reflected in this view.

### Kinematics
classKinematics
Bases: `pybind11_object`
Kinematics interface class.
classLimits
Bases: `pybind11_object`
Simple class consisting of upper and lower limits for a given c-space coordinate.
propertylower
propertyupper

base_frame_name(self:lula.Kinematics )→str
Return the name of the base frame of the kinematic structure.

c_space_coord_acceleration_limit(
self:lula.Kinematics ,
coord_index:int,
)→floatReturn the acceleration limit of a given configuration space coordinate of the kinematic structure.

c_space_coord_jerk_limit(
self:lula.Kinematics ,
coord_index:int,
)→floatReturn the jerk limit of a given configuration space coordinate of the kinematic structure.

c_space_coord_limits(
self:lula.Kinematics ,
coord_index:int,
)→lula.Kinematics.Limits Return the limits of a given configuration space coordinate of the kinematic structure.

c_space_coord_name(
self:lula.Kinematics ,
coord_index:int,
)→strReturn the name of a given configuration space coordinate of the kinematic structure.

c_space_coord_velocity_limit(
self:lula.Kinematics ,
coord_index:int,
)→floatReturn the velocity limit of a given configuration space coordinate of the kinematic structure.

frame_names(self:lula.Kinematics )→list[str]
Return all of the frame names in the kinematic structure.

has_c_space_acceleration_limit(
self:lula.Kinematics ,
coord_index:int,
)→boolReturn true if the given configuration space coordinate has an associated acceleration limit.

has_c_space_jerk_limit(
self:lula.Kinematics ,
coord_index:int,
)→boolReturn true if the given configuration space coordinate has an associated jerk limit.

jacobian(
self:lula.Kinematics ,
cspace_position:numpy.ndarray[numpy.float64[m,1]],
frame:str,
)→numpy.ndarray[numpy.float64[6,n]]Return the Jacobian of the origin of the given frame with respect to the base frame (i.e., base_frame_name()) at the given cspace_position.
The returned Jacobian is a 6 x N matrix where N is the c-space dimension (i.e., num_c_space_coords()). Column i of the returned Jacobian corresponds to the derivative of the origin of frame with respect to the ith c-space coordinate in the coordinates of the base frame. For each column, the first three elements correspond to the translational portion, and the last three elements correspond to the rotational portion.

num_c_space_coords(self:lula.Kinematics )→int
Return the number of configuration space coordinates for the kinematic structure.

orientation(*args, **kwargs)
Overloaded function.

- orientation(self: lula.Kinematics, cspace_position: numpy.ndarray[numpy.float64[m, 1]], frame: str, reference_frame: str) -> lula::Rotation3

Return the orientation of the given frame with respect to reference_frame at the given cspace_position.

- orientation(self: lula.Kinematics, cspace_position: numpy.ndarray[numpy.float64[m, 1]], frame: str) -> lula::Rotation3

Return the orientation of the given frame with respect to the base frame (i.e., base_frame_name()) at the given cspace_position.

orientation_jacobian(
self:lula.Kinematics ,
cspace_position:numpy.ndarray[numpy.float64[m,1]],
frame:str,
)→numpy.ndarray[numpy.float64[3,n]]Return the Jacobian of the orientation of the given frame with respect to the base frame (i.e., base_frame_name()) at the given cspace_position.
The returned Jacobian is a 3 x N matrix where N is the c-space dimension (i.e., num_c_space_coords()). Column i of the returned Jacobian corresponds to the derivative of the orientation of frame with respect to the ith c-space coordinate in the coordinates of the base frame.

pose(*args, **kwargs)
Overloaded function.

- pose(self: lula.Kinematics, cspace_position: numpy.ndarray[numpy.float64[m, 1]], frame: str, reference_frame: str) -> lula::Pose3

Return the pose of the given frame with respect to reference_frame at the given cspace_position.

- pose(self: lula.Kinematics, cspace_position: numpy.ndarray[numpy.float64[m, 1]], frame: str) -> lula::Pose3

Return the pose of the given frame with respect to the base frame (i.e., base_frame_name()) at the given cspace_position.

position(*args, **kwargs)
Overloaded function.

- position(self: lula.Kinematics, cspace_position: numpy.ndarray[numpy.float64[m, 1]], frame: str, reference_frame: str) -> numpy.ndarray[numpy.float64[3, 1]]

Return the position of the origin of the given frame with respect to reference_frame at the given cspace_position.

- position(self: lula.Kinematics, cspace_position: numpy.ndarray[numpy.float64[m, 1]], frame: str) -> numpy.ndarray[numpy.float64[3, 1]]

Return the position of the origin of the given frame with respect to the base frame (i.e., base_frame_name()) at the given cspace_position.

position_jacobian(
self:lula.Kinematics ,
cspace_position:numpy.ndarray[numpy.float64[m,1]],
frame:str,
)→numpy.ndarray[numpy.float64[3,n]]Return the Jacobian of the position of the origin of the given frame with respect to the base frame (i.e., base_frame_name()) at the given cspace_position.
The returned Jacobian is a 3 x N matrix where N is the c-space dimension (i.e., num_c_space_coords()). Column i of the returned Jacobian corresponds to the derivative of the position of the origin of frame with respect to the ith c-space coordinate in the coordinates of the base frame.

within_cspace_limits(
self:lula.Kinematics ,
cspace_position:numpy.ndarray[numpy.float64[m,1]],
log_warnings:bool,
)→boolDetermine whether a specified configuration space position is within limits.

### Inverse Kinematics
classCyclicCoordDescentIkConfig
Bases: `pybind11_object`
Configuration parameters for CCD inverse kinematics solver.
classCSpaceLimitBiasing
Bases: `pybind11_object`
Members:
AUTO
ENABLE
DISABLE
AUTO=<CSpaceLimitBiasing.AUTO:0>
DISABLE=<CSpaceLimitBiasing.DISABLE:2>
ENABLE=<CSpaceLimitBiasing.ENABLE:1>
propertyname
propertyvalue

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

propertycspace_seeds
Optional parameter to set the initial c-space configurations for descent.

propertyirwin_hall_sampling_order
Sampling distribution for initial c-space positions.

propertymax_num_descents
Maximum number of c-space positions that will be used as seeds.

propertyorientation_tolerance
Maximum orientation error (per-axis L2-norm) for a successful IK solution

propertyposition_tolerance
Maximum position error (L2-norm) for a successful IK solution

propertysampling_seed
Seed for Irwin-Hall sampling of initial c-space positions

classCyclicCoordDescentIkResults
Bases: `pybind11_object`
Results returned by CCD inverse kinematics solver.
propertycspace_position
If success is true, joint configuration corresponding to target_pose.

propertynum_descents
Number of unique c-sapce positions used for CCD prior to termination.

propertyposition_error
Position error (L2-norm) of returned c-space position

propertysuccess
Indicate whether a cspace_position within the tolerances has been found.

propertyx_axis_orientation_error
X-axis orientation error (L2-norm) of returned c-space position

propertyy_axis_orientation_error
Y-axis orientation error (L2-norm) of returned c-space position

propertyz_axis_orientation_error
Z-axis orientation error (L2-norm) of returned c-space position

compute_ik_ccd(
kinematics:lula::Kinematics,
target_pose:lula::Pose3,
target_frame:str,
config:lula.CyclicCoordDescentIkConfig,
)→lula.CyclicCoordDescentIkResults Attempt to solve inverse kinematics using cyclic coordinate descent.

### Path Specification
classCSpacePathSpec
Bases: `pybind11_object`
Procedurally specify a CSpacePathSpec from a series of configuration space waypoints
add_c_space_waypoint(
self:lula.CSpacePathSpec ,
waypoint:numpy.ndarray[numpy.float64[m,1]],
)→boolAdd a path to connect the previous configuration to the waypoint.

num_c_space_coords(self:lula.CSpacePathSpec )→int
Return the number of configuration space coordinates for the path specification.

create_c_space_path_spec(
initial_c_space_position:numpy.ndarray[numpy.float64[m,1]],
)→lula.CSpacePathSpec Create a ‘CSpacePathSpec’ with the specified ‘initial_c_space_position’.

classTaskSpacePathSpec
Bases: `pybind11_object`
Procedurally compose a TaskSpacePathSpec from a series of continuous task space segments
add_linear_path(
self:lula.TaskSpacePathSpec ,
target_pose:lula.Pose3 ,
blend_radius:float=0.0,
)→boolAdd a path to linearly connect the previous pose to the ‘target_pose’.

add_rotation(
self:lula.TaskSpacePathSpec ,
target_rotation:lula.Rotation3 ,
)→boolAdd a rotation-only path connecting the previous pose to the target_rotation.

add_tangent_arc(
self:lula.TaskSpacePathSpec ,
target_position:numpy.ndarray[numpy.float64[3,1]],
constant_orientation:bool=True,
)→boolAdd a path to connect the previous pose to the ‘target_position’ along a circular arc that is tangent to the previous segment.

add_tangent_arc_with_orientation_target(
self:lula.TaskSpacePathSpec ,
target_pose:lula.Pose3 ,
)→boolAdd a path to connect the previous pose to the ‘target_pose’ along a circular arc that is tangent to the previous segment.

add_three_point_arc(
self:lula.TaskSpacePathSpec ,
target_position:numpy.ndarray[numpy.float64[3,1]],
intermediate_position:numpy.ndarray[numpy.float64[3,1]],
constant_orientation:bool=True,
)→boolAdd a path to connect the previous pose to the ‘target_position’ along a circular arc that passes through ‘intermediate_position’.

add_three_point_arc_with_orientation_target(
self:lula.TaskSpacePathSpec ,
target_pose:lula.Pose3 ,
intermediate_position:numpy.ndarray[numpy.float64[3,1]],
)→boolAdd a path to connect the previous pose to the ‘target_pose’ along a circular arc that passes through ‘intermediate_position’.

add_translation(
self:lula.TaskSpacePathSpec ,
target_position:numpy.ndarray[numpy.float64[3,1]],
blend_radius:float=0.0,
)→boolAdd a translation-only path to linearly connect the previous pose to the ‘target_position’

generate_path(
self:lula.TaskSpacePathSpec ,
)→lula.TaskSpacePath Generate a continuous path between all of the procedurally added task space path segments.

create_task_space_path_spec(
initial_pose:lula.Pose3 ,
)→lula.TaskSpacePathSpec Create a ‘TaskSpacePathSpec’ with the specified ‘initial_pose’.

classCompositePathSpec
Bases: `pybind11_object`
Procedurally compose ‘CSpacePathSpec’ and ‘TaskSpacePathSpec’ segments into a single path specification.
classPathSpecType
Bases: `pybind11_object`
Members:
TASK_SPACE
CSPACE
CSPACE=<PathSpecType.CSPACE:1>
TASK_SPACE=<PathSpecType.TASK_SPACE:0>
propertyname
propertyvalue

classTransitionMode
Bases: `pybind11_object`
Members:
SKIP
FREE
LINEAR_TASK_SPACE
FREE=<TransitionMode.FREE:1>
LINEAR_TASK_SPACE=<TransitionMode.LINEAR_TASK_SPACE:2>
SKIP=<TransitionMode.SKIP:0>
propertyname
propertyvalue

add_c_space_path_spec(
self:lula.CompositePathSpec ,
path_spec:lula.CSpacePathSpec ,
transition_mode:lula.CompositePathSpec.TransitionMode ,
)→boolAdd a c-space ‘path_spec’ to the ‘CompositePathSpec’ with the specified ‘transition_mode’.

add_task_space_path_spec(
self:lula.CompositePathSpec,
path_spec:lula::TaskSpacePathSpec,
transition_mode:lula.CompositePathSpec.TransitionMode,
)→boolAdd a task space ‘path_spec’ to the ‘CompositePathSpec’ with the specified ‘transition_mode’.

c_space_path_spec(
self:lula.CompositePathSpec ,
path_spec_index:int,
)→lula.CSpacePathSpec Return the ‘CSpacePathSpec’ at the given ‘path_spec_index’.

num_c_space_coords(
self:lula.CompositePathSpec ,
)→intReturn the number of configuration space coordinates for the path specification.

num_path_specs(self:lula.CompositePathSpec )→int
Return the number of path specifications contained in the ‘CompositePathSpec’.

path_spec_type(
self:lula.CompositePathSpec ,
path_spec_index:int,
)→lula.CompositePathSpec.PathSpecType Given a ‘path_spec_index’ in range [0, ‘num_path_specs()’), return the type of the corresponding path specification.

task_space_path_spec(
self:lula.CompositePathSpec ,
path_spec_index:int,
)→lula::TaskSpacePathSpecReturn the ‘TaskSpacePathSpec’ at the given ‘path_spec_index’.

create_composite_path_spec(
initial_c_space_position:numpy.ndarray[numpy.float64[m,1]],
)→lula.CompositePathSpec Create a ‘CompositePathSpec’ with the specified ‘initial_c_space_position’.

load_c_space_path_spec_from_file(
c_space_path_spec_file:str,
)→lula.CSpacePathSpec Load a ‘CSpacePathSpec’ from file with absolute path ‘c_space_path_spec_file’.

load_c_space_path_spec_from_memory(
c_space_path_spec_yaml:str,
)→lula.CSpacePathSpec Load a ‘CSpacePathSpec’ from the contents of a YAML file (‘c_space_path_spec_yaml’).

export_c_space_path_spec_to_memory(
c_space_path_spec:lula.CSpacePathSpec ,
)→strExport ‘c_space_path_spec’ as a string.

load_task_space_path_spec_from_file(
task_space_path_spec_file:str,
)→lula::TaskSpacePathSpecLoad a ‘TaskSpacePathSpec’ from file with absolute path ‘task_space_path_spec_file’.

load_task_space_path_spec_from_memory(
task_space_path_spec_yaml:str,
)→lula::TaskSpacePathSpecLoad a ‘TaskSpacePathSpec’ from the contents of a YAML file (‘task_space_path_spec_yaml’).

export_task_space_path_spec_to_memory(
task_space_path_spec:lula::TaskSpacePathSpec,
)→strExport ‘task_space_path_spec’ as a string.

load_composite_path_spec_from_file(
composite_path_spec_file:str,
)→lula.CompositePathSpec Load a ‘CompositePathSpec’ from file with absolute path ‘composite_path_spec_file’.

load_composite_path_spec_from_memory(
composite_path_spec_yaml:str,
)→lula.CompositePathSpec Load a ‘CompositePathSpec’ from the contents of a YAML file (‘composite_path_spec_yaml’).

export_composite_path_spec_to_memory(
composite_path_spec:lula.CompositePathSpec ,
)→strExport ‘composite_path_spec’ as a string.

### Path Generation
classCSpacePath
Bases: `pybind11_object`
Represent a path through configuration space (i.e., c-space or “joint space”).
classDomain
Bases: `pybind11_object`
Indicates the continuous range of independent values, ‘s’, for which the path is defined.
span(self:lula.CSpacePath.Domain )→float
Convenience function to return the span of ‘s’ values included in domain.

propertylower
propertyupper

domain(self:lula.CSpacePath )→lula.CSpacePath.Domain
Return the domain for the path.

eval(
self:lula.CSpacePath ,
s:float,
)→numpy.ndarray[numpy.float64[m,1]]Evaluate the path at the given ‘s’.

max_position(
self:lula.CSpacePath ,
)→numpy.ndarray[numpy.float64[m,1]]Return the maximum x, y, and z positions reached by the path (not necessarily simultaneously) within the defined ‘domain()’.

min_position(
self:lula.CSpacePath ,
)→numpy.ndarray[numpy.float64[m,1]]Return the minimum x, y, and z positions reached by the path (not necessarily simultaneously) within the defined ‘domain()’.

num_c_space_coords(self:lula.CSpacePath )→int
Return the number of configuration space coordinates for the path.

path_length(self:lula.CSpacePath )→float
Return the total translation distance accumulated along the path, where distance is computed using the L2-norm.

classLinearCSpacePath
Bases: `pybind11_object`
Represent a path linearly interpolated through configuration space (i.e., c-space) waypoints.
domain(
self:lula.LinearCSpacePath ,
)→lula.CSpacePath.Domain Return the domain for the path.

eval(
self:lula.LinearCSpacePath ,
s:float,
)→numpy.ndarray[numpy.float64[m,1]]Evaluate the path at the given ‘s’.

max_position(
self:lula.LinearCSpacePath ,
)→numpy.ndarray[numpy.float64[m,1]]Return the maximum x, y, and z positions reached by the path (not necessarily simultaneously) within the defined ‘domain()’.

min_position(
self:lula.LinearCSpacePath ,
)→numpy.ndarray[numpy.float64[m,1]]Return the minimum x, y, and z positions reached by the path (not necessarily simultaneously) within the defined ‘domain()’.

num_c_space_coords(
self:lula.LinearCSpacePath ,
)→intReturn the number of configuration space coordinates for the path.

path_length(self:lula.LinearCSpacePath )→float
Return the total translation distance accumulated along the path, where distance is computed using the L2-norm.

waypoints(
self:lula.LinearCSpacePath ,
)→list[numpy.ndarray[numpy.float64[m,1]]]Return all of the waypoints through which the path is linearly interpolated (including the initial and final c-space configurations).

create_linear_c_space_path(
c_space_path_spec:lula.CSpacePathSpec ,
)→lula.LinearCSpacePath Create a ‘LinearCSpacePath’ from a c-space path specification.

classTaskSpacePath
Bases: `pybind11_object`
Represent a path through task space (i.e., SE(3) group representing 6-dof poses).
classDomain
Bases: `pybind11_object`
Indicates the continuous range of independent values, ‘s’, for which the path is defined.
span(self:lula.TaskSpacePath.Domain )→float
Convenience function to return the span of ‘s’ values included in domain.

propertylower
propertyupper

accumulated_rotation(self:lula.TaskSpacePath )→float
Return the total angular distance (in radians) accumulated throughout the path.

domain(
self:lula.TaskSpacePath ,
)→lula.TaskSpacePath.Domain Return the domain for the path.

eval(self:lula.TaskSpacePath , s:float)→lula.Pose3
Evaluate the path at the given ‘s’.

max_position(
self:lula.TaskSpacePath ,
)→numpy.ndarray[numpy.float64[3,1]]Return the maximum x, y, and z positions reached by the path (not necessarily simultaneously) within the defined ‘domain()’.

min_position(
self:lula.TaskSpacePath ,
)→numpy.ndarray[numpy.float64[3,1]]Return the minimum x, y, and z positions reached by the path (not necessarily simultaneously) within the defined ‘domain()’.

path_length(self:lula.TaskSpacePath )→float
Return the total translation distance accumulated along the path.

classTaskSpacePathConversionConfig
Bases: `pybind11_object`
Configuration parameters for converting a ‘TaskSpacePathSpec’ into a series of c-space configurations.
propertyalpha
“alpha” is used to exponentially scale the ‘s’ step size “delta” to speed convergence when the ‘s’ step size is being successively increased or successively decreased. When an increase is followed by a decrease, or vice versa, “alpha” is used to decrease the ‘s’ step size “delta” to reduce overshoot. The default value is generally recommended. ‘alpha’ must be greater than 1. Default value is 1.4.

propertyinitial_s_step_size
Initial step size in the domain value ‘s’ used to sample poses from the task space path to be converted to c-space waypoints. The ‘s’ step size will be adaptively updated throughout the path conversion and the default value for initialization is generally recommended. ‘initial_s_step_size’ must be positive. Default value is 0.05.

propertyinitial_s_step_size_delta
Initial step size “delta” that is used to adaptively adjust the ‘s’ step size; ‘s’ is the domain value ‘s’ used to sample poses from the task space path to be converted to c-space waypoints. The ‘s’ step size “delta” will be adaptively updated throughout the path conversion and the default value for initialization is generally recommended. ‘initial_s_step_size_delta’ must be positive. Default value is 0.005.

propertymax_iterations
Maximum number of iterations to search for each c-space waypoint. If ‘max_iterations’ is reached for any c-space waypoint, then path conversion will fail. ‘max_iterations’ must be positive. Default value is 50.

propertymax_position_deviation
For each c-space waypoint that is generated, the position deviation between the desired task space path and a task space mapping of a straight-line interpolation in c-space is approximated. The maximum position deviation places an upper bound of deviation allowed to add a c-space waypoint. ‘max_position_deviation’ must be positive and greater than ‘min_position_deviation’. Default value is 0.003.

propertymin_position_deviation
For each c-space waypoint that is generated, the position deviation between the desired task space path and a task space mapping of a straight-line interpolation in c-space is approximated. The minimum position deviation places a lower bound of deviation required to add a c-space waypoint. While it is somewhat unintuitive that the deviation could be too small, this minimum deviation is used to control the minimum spacing between c-space configurations along the task space path domain. A (relatively) sparse series of c-space waypoints is desirable for trajectory generation; if the minimum deviation is arbitrarily small then the c-space points will be (in general) too close together to generate a time-optimal trajectory. Generation of excessive c-space waypoints will also be computationally expensive and is, in general, best avoided. ‘min_position_deviation’ must be positive and less than ‘max_position_deviation’. Default value is 0.001.

propertymin_s_step_size
Minimum allowable interval in domain value ‘s’ that can separate poses from the task space path to be converted to c-space waypoints. The minimum ‘s’ step size serves to limit the number of c-space configurations that can be returned in the converted path. Specifically, the upper bound for the number of returned c-space configurations is (“span of the task space path domain” / min_s_step_size) + 1. ‘min_s_step_size’ must be positive. Default value is 1e-5.

propertymin_s_step_size_delta
Minimum allowable ‘s’ step size “delta” used to adaptively update the ‘s’ step size. The ‘min_s_step_size_delta’ serves to limit wasted iterations when (minimal) progress is being made towards path conversion. If ‘min_s_step_size_delta’ is reached during the search for any c-space waypoint, then path conversion will fail. The default value is generally recommended. ‘min_s_step_size_delta` must be positive’. Default value is 1e-5.

convert_composite_path_spec_to_c_space(
composite_path_spec:lula.CompositePathSpec,
kinematics:lula.Kinematics,
control_frame:str,
task_space_path_conversion_config:lula.TaskSpacePathConversionConfig=<lula.TaskSpacePathConversionConfigobjectat0x7fd7436ed830>,
ik_config:lula.CyclicCoordDescentIkConfig=<lula.CyclicCoordDescentIkConfigobjectat0x7fd6a2e89530>,
)→lula.LinearCSpacePath Convert a composite_path_spec into a linear c-space path.

convert_task_space_path_spec_to_c_space(
task_space_path_spec:lula::TaskSpacePathSpec,
kinematics:lula.Kinematics,
control_frame:str,
task_space_path_conversion_config:lula.TaskSpacePathConversionConfig=<lula.TaskSpacePathConversionConfigobjectat0x7fd6a2d54870>,
ik_config:lula.CyclicCoordDescentIkConfig=<lula.CyclicCoordDescentIkConfigobjectat0x7fd8e8856db0>,
)→lula.LinearCSpacePath Convert a task_space_path_spec into a linear c-space path.

### Trajectory Generation
classTrajectory
Bases: `pybind11_object`
Represent a path through configuration space (i.e., “c-space”) parameterized by time.
classDomain
Bases: `pybind11_object`
Indicates the continuous range of time values, ‘t’, for which the trajectory and its derivatives are defined.
span(self:lula.Trajectory.Domain )→float
Convenience function to return the span of time values included in domain.

propertylower
propertyupper

domain(self:lula.Trajectory )→lula.Trajectory.Domain
Return the domain for the trajectory.

eval(
self:lula.Trajectory ,
time:float,
derivative_order:int=0,
)→numpy.ndarray[numpy.float64[m,1]]Evaluate specified trajectory derivative at the given ‘time’ and return value.

eval_all(
self:lula.Trajectory ,
arg0:float,
)→tuple[numpy.ndarray[numpy.float64[m,1]],numpy.ndarray[numpy.float64[m,1]],numpy.ndarray[numpy.float64[m,1]],numpy.ndarray[numpy.float64[m,1]]]Evaluate the trajectory at the given ‘time’, returning position, velocity, acceleration, and jerk.

max_acceleration_magnitude(
self:lula.Trajectory ,
)→numpy.ndarray[numpy.float64[m,1]]Return the maximum magnitude of acceleration for each c-space coordinate within the defined ‘domain()’.

max_jerk_magnitude(
self:lula.Trajectory ,
)→numpy.ndarray[numpy.float64[m,1]]Return the maximum magnitude of jerk for each c-space coordinate within the defined ‘domain()’.

max_position(
self:lula.Trajectory ,
)→numpy.ndarray[numpy.float64[m,1]]Return the maximum position for each c-space coordinate within the defined ‘domain()’.

max_velocity_magnitude(
self:lula.Trajectory ,
)→numpy.ndarray[numpy.float64[m,1]]Return the maximum magnitude of velocity for each c-space coordinate within the defined ‘domain()’.

min_position(
self:lula.Trajectory ,
)→numpy.ndarray[numpy.float64[m,1]]Return the minimum position for each c-space coordinate within the defined ‘domain()’.

num_c_space_coords(self:lula.Trajectory )→int
Return the number of configuration space coordinates for the trajectory.

classCSpaceTrajectoryGenerator
Bases: `pybind11_object`
Configure a trajectory generator that can compute smooth trajectories.
classInterpolationMode
Bases: `pybind11_object`
Members:
LINEAR
CUBIC_SPLINE
CUBIC_SPLINE=<InterpolationMode.CUBIC_SPLINE:1>
LINEAR=<InterpolationMode.LINEAR:0>
propertyname
propertyvalue

classSolverParamValue
Bases: `pybind11_object`
Value for a given parameter.

generate_time_stamped_trajectory(self:lula.CSpaceTrajectoryGenerator,waypoints:list[numpy.ndarray[numpy.float64[m,1]]],times:list[float],interpolation_mode:lula.CSpaceTrajectoryGenerator.InterpolationMode=<InterpolationMode.CUBIC_SPLINE:1>)→lula.Trajectory
Attempt to interpolate a trajectory passing through the specified ‘waypoints’ at the specified ‘times’

generate_trajectory(
self:lula.CSpaceTrajectoryGenerator ,
waypoints:list[numpy.ndarray[numpy.float64[m,1]]],
)→lula.Trajectory Attempt to generate a time-optimal trajectory with the specified constraints.

num_c_space_coords(
self:lula.CSpaceTrajectoryGenerator ,
)→intReturn the number of configuration space coordinates for the trajectory generator

set_acceleration_limits(
self:lula.CSpaceTrajectoryGenerator ,
max_acceleration:numpy.ndarray[numpy.float64[m,1]],
)→None Set acceleration limits.

set_jerk_limits(
self:lula.CSpaceTrajectoryGenerator ,
max_jerk:numpy.ndarray[numpy.float64[m,1]],
)→None Set jerk limits.

set_position_limits(
self:lula.CSpaceTrajectoryGenerator ,
min_position:numpy.ndarray[numpy.float64[m,1]],
max_position:numpy.ndarray[numpy.float64[m,1]],
)→None Set position limits.

set_solver_param(
self:lula.CSpaceTrajectoryGenerator ,
param_name:str,
value:lula.CSpaceTrajectoryGenerator.SolverParamValue ,
)→boolSet the value of the solver parameter.

set_velocity_limits(
self:lula.CSpaceTrajectoryGenerator ,
max_velocity:numpy.ndarray[numpy.float64[m,1]],
)→None Set velocity limits.

create_c_space_trajectory_generator(*args, **kwargs)
Overloaded function.

- create_c_space_trajectory_generator(num_c_space_coords: int) -> lula.CSpaceTrajectoryGenerator

Create a CreateCSpaceTrajectoryGenerator with the specified number of configuration space coordinates.

- create_c_space_trajectory_generator(kinematics: lula.Kinematics) -> lula.CSpaceTrajectoryGenerator

Create a CreateCSpaceTrajectoryGenerator with the specified ‘kinematics’.

### Collision Sphere Generation
classCollisionSphereGenerator
Bases: `pybind11_object`
Configure a generator that can generate spheres to approximate mesh volumes.
classParamValue
Bases: `pybind11_object`
Value for a given parameter.

classSphere
Bases: `pybind11_object`
Simple representation of a sphere.
propertycenter
propertyradius

generate_spheres(
self:lula.CollisionSphereGenerator ,
num_spheres:int,
radius_offset:float,
)→list[lula.CollisionSphereGenerator.Sphere ]Generate a set of num_spheres that approximate the volume of the specified mesh

get_sampled_spheres(
self:lula.CollisionSphereGenerator ,
)→list[lula.CollisionSphereGenerator.Sphere ]Return all of the medial axis spheres used to approximate the volume of the mesh. The spheres returned by generateSpheres() are selected from this set.

num_triangles(
self:lula.CollisionSphereGenerator ,
)→intReturn the number of validated triangles that have been included in the mesh used for sampling spheres to approximate volume.

set_param(
self:lula.CollisionSphereGenerator ,
param_name:str,
value:lula.CollisionSphereGenerator.ParamValue ,
)→boolSet the value of the parameter.

create_collision_sphere_generator(
vertices:list[numpy.ndarray[numpy.float64[3,1]]],
triangles:list[numpy.ndarray[numpy.int32[3,1]]],
)→lula.CollisionSphereGenerator Create a CollisionSphereGenerator to generate spheres that approximate the volume of a mesh represented by vertices and triangles.

### Motion Planning
classMotionPlanner
Bases: `pybind11_object`
Interface for planning collision-free paths for robotic manipulators.
classLimit
Bases: `pybind11_object`
Simple class consisting of upper and lower limits for a variable.
propertylower
propertyupper

classParamValue
Bases: `pybind11_object`
Value for a given parameter.

classResults
Bases: `pybind11_object`
Results from a path search.
propertyinterpolated_path
propertypath
propertypath_found

plan_to_cspace_target(
self:lula.MotionPlanner ,
q_initial:numpy.ndarray[numpy.float64[m,1]],
q_target:numpy.ndarray[numpy.float64[m,1]],
generate_interpolated_path:bool=False,
)→lula::MotionPlanner::ResultsAttempt to find path to configuration space target

plan_to_pose_target(self:lula.MotionPlanner,q_initial:numpy.ndarray[numpy.float64[m,1]],pose_target:lula::Pose3,generate_interpolated_path:bool=False)→lula::MotionPlanner::Results
Attempt to find path to task space pose target using JtRRT.

plan_to_task_space_target(
self:lula.MotionPlanner ,
q_initial:numpy.ndarray[numpy.float64[m,1]],
x_target:numpy.ndarray[numpy.float64[3,1]],
generate_interpolated_path:bool=False,
)→lula::MotionPlanner::ResultsAttempt to find path to task space translation target. .. warning:

```
This function supports legacy code from before JtRRT supported full-pose
targets. This function has been deprecated and slated for removal in a
near-future release. Equivalent functionality is available in the
`plan_to_translation_target()` function.
```

plan_to_translation_target(
self:lula.MotionPlanner ,
q_initial:numpy.ndarray[numpy.float64[m,1]],
translation_target:numpy.ndarray[numpy.float64[3,1]],
generate_interpolated_path:bool=False,
)→lula::MotionPlanner::ResultsAttempt to find path to task space translation target using JtRRT.

set_param(*args, **kwargs)
Overloaded function.

- set_param(self: lula.MotionPlanner, param_name: str, value: list[float]) -> bool

Set parameter for motion planner.

- set_param(self: lula.MotionPlanner, param_name: str, value: list[lula::MotionPlanner::Limit]) -> bool

Set parameter for motion planner.

- set_param(self: lula.MotionPlanner, param_name: str, value: lula::MotionPlanner::ParamValue) -> bool

Set parameter for motion planner.

set_parame(
self:lula.MotionPlanner ,
param_name:str,
value:numpy.ndarray[numpy.float64[3,1]],
)→boolSet parameter for motion planner.

update_world_view(self:lula.MotionPlanner )→None
Update the internal WorldView to latest state of its underlying World.

create_motion_planner(*args, **kwargs)
Overloaded function.

- create_motion_planner(planning_config_file: str, robot_description: lula::RobotDescription, world_view: lula::WorldView) -> lula.MotionPlanner

Create an MotionPlanner interface from configuration parameters, robot description and world view.

- create_motion_planner(robot_description: lula::RobotDescription, world_view: lula::WorldView) -> lula.MotionPlanner

Create an MotionPlanner interface from robot description and world view, using default configuration parameters.

### RmpFlow
classRmpFlowConfig
Bases: `pybind11_object`
RMPflow configuration, including parameters and robot description.
get_all_params(
self:lula.RmpFlowConfig ,
names:list[str],
values:list[float],
)→None Get the names and values of all parameters.
The two lists will be overwritten if not empty.
Parameters:

- names (List[str]) – List of all parameter names.

- values (List[float]) – Values of all parameters, in same order as names.

Returns:
None

get_param(
self:lula.RmpFlowConfig ,
param_name:str,
)→floatGet the value of an RMPflow parameter.
Parameters:
param_name (str) – Fully-qualified parameter name of the form <rmp_name>/<parameter_name>.

Returns:
Current value of the parameter.

Return type:
float

set_all_params(
self:lula.RmpFlowConfig ,
names:list[str],
values:list[float],
)→None Set all parameters at once.
The lists names and values must have the same size. The parameter corresponding to names[i] will be set to the value given by values[i].
Parameters:

- names (List[str]) – List of all parameter names.

- values (List[float]) – Desired values for all parameters, in same order as names.

Returns:
None

set_param(
self:lula.RmpFlowConfig ,
param_name:str,
value:float,
)→None Set the value of an RMPflow parameter.
Parameters:

- param_name (str) – Fully-qualified parameter name of the form <rmp_name>/<parameter_name>.

- value (float) – New value for the parameter.

Returns:
None

set_world_view(
self:lula.RmpFlowConfig,
world_view:lula::WorldView,
)→None Set the world view that will be used for obstacle avoidance.
All enabled obstacles in world_view will be avoided by the RMPflow policy.
Parameters:
world_view (lula.WorldView ) – Input world view.

Returns:
None

create_rmpflow_config(
rmpflow_config_file:str,
robot_description:lula::RobotDescription,
end_effector_frame:str,
world_view:lula::WorldView,
)→lula.RmpFlowConfig Create an RMPflow configuration object.
This function loads a set of RMPflow parameters from a file and combines them with a robot description to create a configuration object for consumption by lula.create_rmpflow().
Parameters:

- rmpflow_config_file (str) – Path to RMPflow configuration file.

- robot_description (lula.RobotDescription ) – RobotDescription object, e.g. created by lula.load_robot().

- end_effector_frame (str) – This control frame name must correspond to a link name as specified in the original URDF used to create the robot description.

- world_view (lula.WorldView ) – World view that will be used for obstacle avoidance.

Returns:
RMPflow motion policy interface object.

Return type:
lula.RmpFlow

create_rmpflow_config_from_memory(
rmpflow_config:str,
robot_description:lula::RobotDescription,
end_effector_frame:str,
world_view:lula::WorldView,
)→lula.RmpFlowConfig Parameters:

- rmpflow_config (str) – RMPflow configuration as a single string (unparsed YAML).

- robot_description (lula.RobotDescription ) – RobotDescription object, e.g. created by lula.load_robot().

- end_effector_frame (str) – This control frame name must correspond to a link name as specified in the original URDF used to create the robot description.

- world_view (lula.WorldView ) – World view that will be used for obstacle avoidance.

Returns:
RMPflow motion policy interface object.

Return type:
lula.RmpFlow

classRmpFlow
Bases: `pybind11_object`
Interface for building and evaluating an RMPflow motion policy.
clear_end_effector_orientation_attractor(
self:lula.RmpFlow ,
)→None Clear end-effector orientation attractor.

clear_end_effector_position_attractor(
self:lula.RmpFlow ,
)→None Clear end-effector position attractor.

collision_sphere_positions(
self:lula.RmpFlow ,
cspace_position:numpy.ndarray[numpy.float64[m,1]],
)→list[numpy.ndarray[numpy.float64[3,1]]]Compute positions of all collision spheres on the robot at the specified cspace_position .. warning:

```
This function is part of a legacy interface for spatial queries that is deprecated
and slated for removal in a near-future release. It is recommended that this
function *NOT* be used. Equivalent functionality is available from
'lula.RobotWorldInspector'.
```

collision_sphere_radii(self:lula.RmpFlow )→list[float]
Return the radii of each collision sphere on the robot. .. warning:

```
This function is part of a legacy interface for spatial queries that is deprecated
and slated for removal in a near-future release. It is recommended that this
function *NOT* be used. Equivalent functionality is available from
'lula.RobotWorldInspector'.
```

distance_to_obstacle(self:lula.RmpFlow,obstacle:lula::World::ObstacleHandle,collision_sphere_index:int,cspace_position:numpy.ndarray[numpy.float64[m,1]])→float
Compute the distance between a given obstacle and collision sphere for the provided position in configuration space. .. warning:

```
This function is part of a legacy interface for spatial queries that is deprecated
and slated for removal in a near-future release. It is recommended that this
function *NOT* be used. Equivalent functionality is available from
'lula.RobotWorldInspector'.
```

eval_accel(
self:lula.RmpFlow ,
cspace_position:numpy.ndarray[numpy.float64[m,1]],
cspace_velocity:numpy.ndarray[numpy.float64[m,1]],
cspace_accel:numpy.ndarray[numpy.float64[m,1],flags.writeable],
)→None Compute configuration-space acceleration from motion policy, given input state.

eval_force_and_metric(
self:lula.RmpFlow ,
cspace_position:numpy.ndarray[numpy.float64[m,1]],
cspace_velocity:numpy.ndarray[numpy.float64[m,1]],
)→tuple[numpy.ndarray[numpy.float64[m,1]],numpy.ndarray[numpy.float64[m,n]]]Compute configuration-space force and metric from motion policy, given input state.

in_collision_with_obstacle(
self:lula.RmpFlow ,
cspace_position:numpy.ndarray[numpy.float64[m,1]],
)→boolDetermine whether a specified joint configuration puts the robot into collision with an obstacle. .. warning:

```
This function is part of a legacy interface for spatial queries that is deprecated
and slated for removal in a near-future release. It is recommended that this
function *NOT* be used. Equivalent functionality is available from
'lula.RobotWorldInspector'.
```

num_collision_spheres(self:lula.RmpFlow )→int
Return the number of collision spheres in the robot representation. .. warning:

```
This function is part of a legacy interface for spatial queries that is deprecated
and slated for removal in a near-future release. It is recommended that this
function *NOT* be used. Equivalent functionality is available from
'lula.RobotWorldInspector'.
```

set_cspace_attractor(
self:lula.RmpFlow ,
cspace_position:numpy.ndarray[numpy.float64[m,1]],
)→None Set an attractor in generalized coordinates (configuration space).

set_end_effector_orientation_attractor(
self:lula.RmpFlow,
orientation:lula::Rotation3,
)→None Set an end-effector orientation attractor.

set_end_effector_position_attractor(
self:lula.RmpFlow ,
position:numpy.ndarray[numpy.float64[3,1]],
)→None Set an end-effector position attractor.

update_world_view(self:lula.RmpFlow )→None
Update the internal WorldView to latest state of its underlying World.

create_rmpflow(config:lula.RmpFlowConfig )→lula.RmpFlow
Create an instance of the RmpFlow interface from an RMPflow configuration.
