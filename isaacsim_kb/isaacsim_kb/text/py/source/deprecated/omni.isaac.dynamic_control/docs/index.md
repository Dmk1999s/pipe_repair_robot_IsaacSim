<!-- source: py/source/deprecated/omni.isaac.dynamic_control/docs/index.html | title: [omni.isaac.dynamic_control] Isaac Sim Dynamic Control — Isaac Sim -->

# [omni.isaac.dynamic_control] Isaac Sim Dynamic Control
Warning
Deprecation: Extension deprecated since Isaac Sim 4.5.0.
Version: 2.0.7
The Dynamic Control extension provides a set of utilities to control physics objects. It provides opaque handles for different physics objects that remain valid between PhysX scene resets, which occur whenever play or stop is pressed.

## Enable Extension
The extension can be enabled (if not already) in one of the following ways:

## Basic Usage
Start physics simulation, at least one frame of simulation must occur before the Dynamic Control interface will become fully active.

```
1import omni
2omni.timeline.get_timeline_interface().play()
```
Acquire the Dynamic Control interface and interact with an articulation. The code block below assumes a Franka Emika Panda robot is in the stage with a base path of `/Franka`

```
1from omni.isaac.dynamic_control import _dynamic_control
2dc = _dynamic_control.acquire_dynamic_control_interface()
3
4# Get a handle to the Franka articulation
5# This handle will automatically update if simulation is stopped and restarted
6art = dc.get_articulation("/Franka")
7
8# Get information about the structure of the articulation
9num_joints = dc.get_articulation_joint_count(art)
10num_dofs = dc.get_articulation_dof_count(art)
11num_bodies = dc.get_articulation_body_count(art)
12
13# Get a specific degree of freedom on an articulation
14dof_ptr = dc.find_articulation_dof(art, "panda_joint2")
15
16dof_state = dc.get_dof_state(dof_ptr)
17# print position for the degree of freedom
18print(dof_state.pos)
19
20# This should be called each frame of simulation if state on the articulation is being changed.
21dc.wake_up_articulation(art)
22dc.set_dof_position_target(dof_ptr, -1.5)
```

## API
The Dynamic Control extension provides a set of utilities to control physics objects. It provides opaque handles for different physics objects that remain valid between PhysX scene resets, which occur whenever play or stop is pressed.
INVALID_HANDLE
This value is returned when trying to acquire a dynamic control handle for an invalid usd path

The following attributes correspond to states that can be get/set from Degrees of Freedom and Rigid Bodies
STATE_NONE
No state selected

STATE_POS
Position states

STATE_VEL
Velocity states

STATE_EFFORT
Force/Torque states

STATE_ALL
All states

The following attributes correspond to joint axes when specifying a 6 Dof (D6) Joint
AXIS_NONE
No axis selected

AXIS_X
Corresponds to translation around the body x-axis

AXIS_Y
Corresponds to translation around the body y-axis

AXIS_Z
Corresponds to translation around the body z-axis

AXIS_TWIST
Corresponds to rotation around the body x-axis

AXIS_SWING_1
Corresponds to rotation around the body y-axis

AXIS_SWING_2
Corresponds to rotation around the body z-axis

AXIS_ALL_TRANSLATION
Corresponds to all Translation axes

AXIS_ALL_ROTATION
Corresponds to all Rotation axes

AXIS_ALL
Corresponds to all axes

classArticulationProperties
Articulation Properties
propertyenable_self_collisions
Allow links in articulation to collide with each other (`bool`)

propertysolver_position_iteration_count
Position solver iterations (`int`)

propertysolver_velocity_iteration_count
Velocity solver iterations (`int`)

classAttractorProperties
The Attractor is used to pull a rigid body towards a pose. Each pose axis can be individually selected.
propertyaxes
Axes to set the attractor, using DcAxisFlags. Multiple axes can be selected using bitwise combination of each axis flag. if axis flag is set to zero, the attractor will be disabled and won’t impact in solver computational complexity.

propertybody
Rigid body to set the attractor to

propertydamping
Damping to be used on attraction solver. (`float`)

propertyforce_limit
Maximum force to be applied by drive. (`float`)

propertyoffset
Offset from rigid body origin to set the attractor pose. (`omni.isaac.dynamic_control._dynamic_control.Transform`)

propertystiffness
Stiffness to be used on attraction for solver. Stiffness value should be larger than the largest agent kinematic chain stifness (`float`)

propertytarget
Target pose to attract to. (`omni.isaac.dynamic_control._dynamic_control.Transform`)

classD6JointProperties
Creates a general D6 Joint between two rigid Bodies.
propertyaxes
Axes to set the attractor, using DcAxisFlags. Multiple axes can be selected using bitwise combination of each axis flag. if axis flag is set to zero, the attractor will be disabled and won’t impact in solver computational complexity.

propertybody0
parent body

propertybody1
child body

propertydamping
Joint Damping. (`float`)

propertyforce_limit
Joint Breaking Force. (`float`)

propertyname
Joint Name (`str`)

propertypose0
Transform from body 0 to joint. (`omni.isaac.dynamic_control._dynamic_control.Transform`)

propertypose1
Transform from body 1 to joint. (`omni.isaac.dynamic_control._dynamic_control.Transform`)

propertystiffness
Joint Stiffness. Stiffness value should be larger than the largest agent kinematic chain stifness (`float`)

propertytorque_limit
Joint Breaking torque. (`float`)

classDofProperties
Properties of a degree-of-freedom (DOF)
propertydamping
Damping of DOF (`float`)

propertydrive_mode
Drive mode for the DOF (`omni.isaac.dynamic_control._dynamic_control.DriveMode`)

propertyhas_limits
Flags whether the DOF has limits (read only) (`bool`)

propertylower
lower limit of DOF. In radians or meters (read only) (`float`)

propertymax_effort
Maximum effort of DOF. in N or N*stage_units (`float`)

propertymax_velocity
Maximum velocity of DOF. In Radians/s, or stage_units/s (`float`)

propertystiffness
Stiffness of DOF (`float`)

propertytype
Type of joint (read only) (`omni.isaac.dynamic_control._dynamic_control.DofType`)

propertyupper
upper limit of DOF. In radians or meters (read only) (`float`)

classDofState
States of a Degree of Freedom in the Asset architecture
dtype=dtype([('pos','<f4'),('vel','<f4'),('effort','<f4')])
propertyeffort
DOF effort due to gravity, torque if it’s a revolute DOF, or force if it’s a prismatic DOF (`float`)

propertypos
DOF position, in radians if it’s a revolute DOF, or stage_units (m, cm, etc), if it’s a prismatic DOF (`float`)

propertyvel
DOF velocity, in radians/s if it’s a revolute DOF, or stage_units/s (m/s, cm/s, etc), if it’s a prismatic DOF (`float`)

classDofType
Types of degree of freedom
Members:
DOF_NONE : invalid/unknown/uninitialized DOF type
DOF_ROTATION : The degrees of freedom correspond to a rotation between bodies
DOF_TRANSLATION : The degrees of freedom correspond to a translation between bodies.

DOF_NONE=<DofType.DOF_NONE:0>
DOF_ROTATION=<DofType.DOF_ROTATION:1>
DOF_TRANSLATION=<DofType.DOF_TRANSLATION:2>
propertyname
propertyvalue

classDriveMode
DOF drive mode
Members:
DRIVE_FORCE : Use Force Based Drive Controller
DRIVE_ACCELERATION : Use Acceleration Based Drive Controller

DRIVE_ACCELERATION=<DriveMode.DRIVE_ACCELERATION:1>
DRIVE_FORCE=<DriveMode.DRIVE_FORCE:0>
propertyname
propertyvalue

classDynamicControl
The following functions are provided on the dynamic control interface
apply_body_force(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:carb::Float3,
arg2:carb::Float3,
arg3:bool,
)→boolApply a force to a rigid body at a position, coordinates can be specified in global or local coordinates

apply_body_torque(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:carb::Float3,
arg2:bool,
)→boolApply a torque to a rigid body, can be specified in global or local coordinates

create_d6_joint(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:omni.isaac.dynamic_control._dynamic_control.D6JointProperties,
)→intCreate a D6 joint

create_rigid_body_attractor(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:omni.isaac.dynamic_control._dynamic_control.AttractorProperties,
)→intGreate an attractor for ridig body

destroy_d6_joint(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→boolDestroy D6 joint

destroy_rigid_body_attractor(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→boolDestroy attractor

find_articulation_body(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:str,
)→intFinds actor rigid body given its name

find_articulation_body_index(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:str,
)→intFind index in articulation body array, -1 on error

find_articulation_dof(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:str,
)→intFinds actor degree-of-freedom given its name

find_articulation_dof_index(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:str,
)→intget index in articulation DOF array, -1 on error

find_articulation_joint(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:str,
)→intGet the joint from an atriculation given their name

get_articulation(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:str,
)→intReturns:
Handle to the articulation, INVALID_HANDLE otherwise

Return type:
handle

get_articulation_body(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:int,
)→intGets actor rigid body given its index

get_articulation_body_count(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→intGets number of rigid bodies for an actor

get_articulation_body_states(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:int,
)→objectGet array of an actor’s rigid body states

get_articulation_dof(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:int,
)→intGets actor degree-of-freedom given its index

get_articulation_dof_count(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→intGets number of degrees-of-freedom for an actor

get_articulation_dof_efforts(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→objectGet array of efforts for articulation

get_articulation_dof_masses(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→objectGet array of an actor’s degree-of-freedom effective masses

get_articulation_dof_position_targets(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→objectGet array of position targets for articulation

get_articulation_dof_properties(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→objectGet array of an actor’s degree-of-freedom properties

get_articulation_dof_states(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:int,
)→objectGet array of an actor’s degree-of-freedom states

get_articulation_dof_velocity_targets(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→objectGet array of velocity targets for articulation

get_articulation_joint(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:int,
)→intGets the joint from an articulation given an index

get_articulation_joint_count(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→intGet the number of joints in an articulation

get_articulation_name(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→strReturns:
The name of the articulation

Return type:
string

get_articulation_path(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→strReturns:
The path to the articulation

Return type:
string

get_articulation_properties(*args, **kwargs)
Overloaded function.

- get_articulation_properties(self: omni.isaac.dynamic_control._dynamic_control.DynamicControl, arg0: int, arg1: omni.isaac.dynamic_control._dynamic_control.ArticulationProperties) -> bool

Get Properties for an articulation

- get_articulation_properties(self: omni.isaac.dynamic_control._dynamic_control.DynamicControl, arg0: int) -> object

Get Properties for an articulation

get_articulation_root_body(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→intGet the root rigid body of an actor

get_attractor_properties(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→objectGet properties for attractor

get_d6_joint(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:str,
)→intReturns:
Handle to the d6 joint, INVALID_HANDLE otherwise

Return type:
handle

get_dof(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:str,
)→intReturns:
Handle to the degree of freedom, INVALID_HANDLE otherwise

Return type:
handle

get_dof_child_body(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→intGet child rigid body for degree of freedom

get_dof_effort(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→floatGet effort applied to degree of freedom

get_dof_joint(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→intGet joint associated with the degree of freedom

get_dof_name(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→strGet Name of this degree of freedom

get_dof_parent_body(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→intGet parent rigid body for degree of freedom

get_dof_path(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→strGet path to degree of freedom

get_dof_position(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→floatGet position/rotation for this degree of freedom

get_dof_position_target(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→floatGet position target for degree of freedom

get_dof_properties(*args, **kwargs)
Overloaded function.

- get_dof_properties(self: omni.isaac.dynamic_control._dynamic_control.DynamicControl, arg0: int, arg1: omni.isaac.dynamic_control._dynamic_control.DofProperties) -> bool

Get degree of freedom properties

- get_dof_properties(self: omni.isaac.dynamic_control._dynamic_control.DynamicControl, arg0: int) -> object

Get degree of freedom properties

get_dof_state(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:int,
)→omni.isaac.dynamic_control._dynamic_control.DofStateGet current state for degree of freedom

get_dof_type(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→omni.isaac.dynamic_control._dynamic_control.DofTypeGet type of degree of freedom

get_dof_velocity(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→floatGet linear/angular velocity of degree of freedom

get_dof_velocity_target(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→floatGet velocity target for degree of freedom

get_joint(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:str,
)→intReturns:
Handle to the joint, INVALID_HANDLE otherwise

Return type:
handle

get_joint_child_body(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→intGet child rigid body for joint

get_joint_dof(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:int,
)→intGet a degree of freedom for joint give its index

get_joint_dof_count(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→intGet number of degrees of freedon constrained by joint

get_joint_name(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→strGet name of joint

get_joint_parent_body(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→intGet parent rigid body for joint

get_joint_path(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→strGet path for joint

get_joint_type(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→omni.isaac.dynamic_control._dynamic_control.JointTypeGet joint type

get_object(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:str,
)→intReturns:
Handle to the physics object defined by the usd path, INVALID_HANDLE otherwise

Return type:
handle

get_object_type(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→omni.isaac.dynamic_control._dynamic_control.ObjectTypeReturns:
`omni.isaac.dynamic_control._dynamic_control.ObjectType`: Type of object returned by get_object

get_object_type_name(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→strReturns:
The object type name as a string

Return type:
string

get_relative_body_poses(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:List[int],
)→List[omni.isaac.dynamic_control._dynamic_control.Transform]given a list of body handles, return poses relative to the parent

get_rigid_body(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:str,
)→intReturns:
Handle to the rigid body, INVALID_HANDLE otherwise

Return type:
handle

get_rigid_body_angular_velocity(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→carb::Float3Get the angular velocity of this rigid body

get_rigid_body_child_joint(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:int,
)→intGet the child joint of a rigid body given its index

get_rigid_body_child_joint_count(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→intGets the number of joints that are children to this rigid body

get_rigid_body_linear_velocity(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→carb::Float3Get the linear velocity of this rigid body in global coordinates

get_rigid_body_local_linear_velocity(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→carb::Float3Get the linear velocity of this rigid body in local coordinates

get_rigid_body_name(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→strGets the rigid body name given a handle

get_rigid_body_parent_joint(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→intGets parent joint to a rigid body

get_rigid_body_path(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→strGets the path to a rigid body given its handle

get_rigid_body_pose(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→omni.isaac.dynamic_control._dynamic_control.TransformGet the pose of a rigid body

get_rigid_body_properties(*args, **kwargs)
Overloaded function.

- get_rigid_body_properties(self: omni.isaac.dynamic_control._dynamic_control.DynamicControl, arg0: int, arg1: omni.isaac.dynamic_control._dynamic_control.RigidBodyProperties) -> bool

Get Properties for a rigid body

- get_rigid_body_properties(self: omni.isaac.dynamic_control._dynamic_control.DynamicControl, arg0: int) -> object

Get Properties for a rigid body

is_simulating(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
)→boolReturns:
True if simulating, False otherwise

Return type:
bool

peek_object_type(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:str,
)→omni.isaac.dynamic_control._dynamic_control.ObjectTypeReturns:
The object type name as a string

Return type:
string

set_articulation_dof_efforts(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:numpy.ndarray[numpy.float32],
)→boolSets efforts on an actor’s degrees-of-freedom.

set_articulation_dof_position_targets(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:numpy.ndarray[numpy.float32],
)→boolSets an actor’s degree-of-freedom position targets.

set_articulation_dof_properties(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:numpy.ndarray[omni.isaac.dynamic_control._dynamic_control.DofProperties],
)→boolSets properties for an actor’s degrees-of-freedom.

set_articulation_dof_states(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:numpy.ndarray[omni.isaac.dynamic_control._dynamic_control.DofState],
arg2:int,
)→boolSets states for an actor’s degrees-of-freedom.

set_articulation_dof_velocity_targets(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:numpy.ndarray[numpy.float32],
)→boolSets an actor’s degree-of-freedom velocity targets.

set_articulation_properties(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:omni.isaac.dynamic_control._dynamic_control.ArticulationProperties,
)→boolSets properties for articulation

set_attractor_properties(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:omni.isaac.dynamic_control._dynamic_control.AttractorProperties,
)→boolSet properties for this attractor

set_attractor_target(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:omni.isaac.dynamic_control._dynamic_control.Transform,
)→boolSet target pose for attractor

set_d6_joint_properties(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:omni.isaac.dynamic_control._dynamic_control.D6JointProperties,
)→boolModifies properties of the selected joint.

set_dof_effort(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:float,
)→boolSet effort on degree of freedom

set_dof_position(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:float,
)→boolSet position/rotation for this degree of freedom

set_dof_position_target(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:float,
)→boolSet position target for degree of freedom

set_dof_properties(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:omni.isaac.dynamic_control._dynamic_control.DofProperties,
)→boolSet degree of freedom properties

set_dof_state(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:omni.isaac.dynamic_control._dynamic_control.DofState,
arg2:int,
)→boolSet degree of freedom state

set_dof_velocity(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:float,
)→boolSet linear angular velocity of degree of freedom

set_dof_velocity_target(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:float,
)→boolSet velocity target for degree of freedom

set_origin_offset(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:carb::Float3,
)→boolOffset origin for a rigid body

set_rigid_body_angular_velocity(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:carb::Float3,
)→boolSet the angular velocity of this rigid body

set_rigid_body_disable_gravity(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:bool,
)→boolenables or disables the force of gravity from the given body

set_rigid_body_disable_simulation(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:bool,
)→boolenables or disables Simulation of a given rigid body

set_rigid_body_linear_velocity(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:carb::Float3,
)→boolSet the linear velocity of the rigid body

set_rigid_body_pose(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:omni.isaac.dynamic_control._dynamic_control.Transform,
)→boolSet the pose of a rigid body

set_rigid_body_properties(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
arg1:omni.isaac.dynamic_control._dynamic_control.RigidBodyProperties,
)→boolSet Properties for a rigid body

sleep_articulation(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→boolPut articulation to sleep

sleep_rigid_body(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→boolPut rigid body to sleep

wake_up_articulation(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→boolEnable physics for a articulation

wake_up_rigid_body(
self:omni.isaac.dynamic_control._dynamic_control.DynamicControl,
arg0:int,
)→boolEnable physics for a rigid body

classJointType
Joint Types that can be specified
Members:
JOINT_NONE : invalid/unknown/uninitialized joint type
JOINT_FIXED : Fixed Joint
JOINT_REVOLUTE : Revolute Joint
JOINT_PRISMATIC : Prismatic Joint
JOINT_SPHERICAL : Spherical Joint

JOINT_FIXED=<JointType.JOINT_FIXED:1>
JOINT_NONE=<JointType.JOINT_NONE:0>
JOINT_PRISMATIC=<JointType.JOINT_PRISMATIC:3>
JOINT_REVOLUTE=<JointType.JOINT_REVOLUTE:2>
JOINT_SPHERICAL=<JointType.JOINT_SPHERICAL:4>
propertyname
propertyvalue

classObjectType
Types of Objects
Members:
OBJECT_NONE : Invalid/unknown/uninitialized object type
OBJECT_RIGIDBODY : The object is a rigid body or a link on an articulation
OBJECT_JOINT : The object is a joint
OBJECT_DOF : The object is a degree of freedon
OBJECT_ARTICULATION : The object is an articulation
OBJECT_ATTRACTOR : The object is an attractor
OBJECT_D6JOINT : The object is a generic D6 joint

OBJECT_ARTICULATION=<ObjectType.OBJECT_ARTICULATION:4>
OBJECT_ATTRACTOR=<ObjectType.OBJECT_ATTRACTOR:5>
OBJECT_D6JOINT=<ObjectType.OBJECT_D6JOINT:6>
OBJECT_DOF=<ObjectType.OBJECT_DOF:3>
OBJECT_JOINT=<ObjectType.OBJECT_JOINT:2>
OBJECT_NONE=<ObjectType.OBJECT_NONE:0>
OBJECT_RIGIDBODY=<ObjectType.OBJECT_RIGIDBODY:1>
propertyname
propertyvalue

classRigidBodyProperties
Rigid Body Properties
propertycMassLocalPose
Local center of mass position (`carb._carb.Float3`)

propertymass
Mass of rigid body (`float`)

propertymax_contact_impulse
Sets a limit on the impulse that may be applied at a contact. (`float`)

propertymax_depeneration_velocity
This value controls how much velocity the solver can introduce to correct for penetrations in contacts. (`float`)

propertymoment
Diagonal moment of inertia (`carb._carb.Float3`)

propertysolver_position_iteration_count
Position solver iterations (`int`)

propertysolver_velocity_iteration_count
Velocity solver iterations (`int`)

classRigidBodyState
Containing states to get/set for a rigid body in the simulation
dtype=dtype([('pose',[('p',[('x','<f4'),('y','<f4'),('z','<f4')]),('r',[('x','<f4'),('y','<f4'),('z','<f4'),('w','<f4')])]),('vel',[('linear',[('x','<f4'),('y','<f4'),('z','<f4')]),('angular',[('x','<f4'),('y','<f4'),('z','<f4')])])])
propertypose
Transform with position and orientation of rigid body (`omni.isaac.dynamic_control._dynamic_control.Transform`)

propertyvel
Linear and angular velocities of rigid body (`omni.isaac.dynamic_control._dynamic_control.Velocity`)

classTransform
Represents a 3D transform in the system
staticfrom_buffer(arg0:buffer)→object
assign a transform from an array of 7 values [p.x, p.y, p.z, r.x, r.y, r.z, r.w]

dtype=dtype([('p',[('x','<f4'),('y','<f4'),('z','<f4')]),('r',[('x','<f4'),('y','<f4'),('z','<f4'),('w','<f4')])])
propertyp
Position as a tuple of (x,y,z) (`carb._carb.Float3`)

propertyr
Rotation Quaternion, represented in the format \(x\hat{i} + y\hat{j} + z\hat{k} + w\) (`carb._carb.Float4`)

classVelocity
Linear and angular velocity
propertyangular
Angular 3D velocity as a tuple (x,y,z), (`carb._carb.Float3`)

dtype=dtype([('linear',[('x','<f4'),('y','<f4'),('z','<f4')]),('angular',[('x','<f4'),('y','<f4'),('z','<f4')])])
propertylinear
Linear 3D velocity as a tuple (x,y,z) , (`carb._carb.Float3`)

acquire_dynamic_control_interface(
plugin_name:str=None,
library_path:str=None,
)→omni::isaac::dynamic_control::DynamicControlAcquire dynamic control interface. This is the base object that all of the dynamic control functions are defined on

release_dynamic_control_interface(
arg0:omni::isaac::dynamic_control::DynamicControl,
)→None Release dynamic control interface. Generally this does not need to be called, the dynamic control interface is released on extension shutdown
