<!-- source: py/api/structomni_1_1isaac_1_1dynamic__control_1_1_dc_d6_joint.html | title: DcD6Joint — Isaac Sim -->

# DcD6Joint
Fully qualified name: `omni::isaac::dynamic_control::DcD6Joint`
structDcD6Joint

Represents a D6 joint in the physics simulation.
Contains all the information needed to represent and manipulate a D6 joint, which is a general-purpose joint that can have up to 6 degrees of freedom. D6 joints can be configured to represent various joint types by constraining specific degrees of freedom.
Public Members
DcHandle handle=kDcInvalidHandle

Handle to this D6 joint.

DcContext *ctx=nullptr

Pointer to the context this D6 joint belongs to.

::physx ::PxD6Joint*pxJoint=nullptr

Pointer to the PhysX D6 joint.

DcD6JointProperties props={}

Properties of the D6 joint.

pxr ::SdfPathpath

USD path of the D6 joint.
