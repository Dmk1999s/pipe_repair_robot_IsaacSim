<!-- source: py/api/namespace_omni__isaac__dynamic__control.html | title: dynamic_control — Isaac Sim -->

# dynamic_control
Fully qualified name: `omni::isaac::dynamic_control`
namespacedynamic_control

## Classes
Bucket
A container for managing objects with unique IDs.

DcContext
Context for managing dynamic control objects in a physics scene.

## Enumerations
int32_tDcDofType
Types of degree of freedom.

int32_tDcDriveMode
Drive modes for degrees-of-freedom.

DcDtype
Data types for tensors.

int32_tDcJointType
Types of joint.

uint32_tDcObjectType
Types of objects that can be controlled via dynamic control.

## Functions
constexpr uint32_tgetHandleContextId (DcHandle h)
constexpr uint32_tgetHandleObjectId (DcHandle h)
constexpr uint32_tgetHandleTypeId (DcHandle h)
constexpr DcHandlemakeHandle (uint64_t objectId, uint64_t typeId, uint64_t contextId)

## Namespaces
conversions
math

## Structs
DcArticulation
Represents an articulation in the physics simulation.

DcArticulationProperties
Properties of an articulation.

DcAttractor
Represents an attractor in the physics simulation.

DcAttractorProperties
Properties to set up a pose attractor.

DcD6Joint
Represents a D6 joint in the physics simulation.

DcD6JointProperties
Properties to set up a D6 Joint.

DcDof
Represents a degree of freedom in the physics simulation.

DcDofProperties
Properties of a degree-of-freedom.

DcDofState
State of a degree of freedom.

DcJoint
Represents a joint in the physics simulation.

DcRayCastResult
Result of a Raycast.

DcRigidBody
Represents a rigid body in the physics simulation.

DcRigidBodyProperties
Properties of a rigid body.

DcRigidBodyState
State of a rigid body.

DcShape
Shape descriptor for tensors.

DcTransform
Transform .

DcVelocity
Velocity.

DynamicControl
Interface for controlling physics objects in Isaac Sim.

## Typedefs
DcAxisFlags
Type for axis flags.

DcHandle
Handle type for dynamic control objects.

DcStateFlags
Type for state flags.

## Variables
constexpr DcAxisFlagskDcAxisAll
Corresponds to all axes.

constexpr DcAxisFlagskDcAxisAllRotation
Corresponds to all Rotation axes.

constexpr DcAxisFlagskDcAxisAllTranslation
Corresponds to all Translation axes.

constexpr DcAxisFlagskDcAxisNone
No axis selected.

constexpr DcAxisFlagskDcAxisSwing1
Corresponds to rotation around the body y-axis.

constexpr DcAxisFlagskDcAxisSwing2
Corresponds to rotation around the body z-axis.

constexpr DcAxisFlagskDcAxisTwist
Corresponds to rotation around the body x-axis.

constexpr DcAxisFlagskDcAxisX
Corresponds to translation around the body x-axis.

constexpr DcAxisFlagskDcAxisY
Corresponds to translation around the body y-axis.

constexpr DcAxisFlagskDcAxisZ
Corresponds to translation around the body z-axis.

constexpr DcHandlekDcInvalidHandle
Invalid handle constant.

constexpr DcStateFlagskDcStateAll
All states.

constexpr DcStateFlagskDcStateEffort
Forces/Torques states.

constexpr DcStateFlagskDcStateNone
No state selected.

constexpr DcStateFlagskDcStatePos
Position states.

constexpr DcStateFlagskDcStateVel
Velocity states.

constexpr carb::Float3kFloat3Zero
Zero vector constant.

constexpr uint64_tkHandleContextMask
constexpr uint64_tkHandleObjectMask
constexpr uint64_tkHandleTypeMask
constexpr intkMaxDims
Maximum number of dimensions for a shape.

constexpr carb::Float4kQuatIdentity
Identity quaternion constant.

constexpr carb::Float4kQuatZero
Zero quaternion constant.

constexpr DcTransformkTransformIdentity
Identity transform constant.

constexpr DcTransformkTransformZero
Zero transform constant.

constexpr DcVelocitykVelocityZero
Zero velocity constant.
