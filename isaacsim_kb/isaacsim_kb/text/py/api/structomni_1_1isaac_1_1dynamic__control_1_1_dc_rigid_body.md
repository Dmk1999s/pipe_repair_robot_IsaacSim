<!-- source: py/api/structomni_1_1isaac_1_1dynamic__control_1_1_dc_rigid_body.html | title: DcRigidBody — Isaac Sim -->

# DcRigidBody
Fully qualified name: `omni::isaac::dynamic_control::DcRigidBody`
structDcRigidBody

Represents a rigid body in the physics simulation.
Contains all the information needed to represent and manipulate a rigid body, including its PhysX representation, name, path, and relationships to other objects.
Public Members
DcHandle handle=kDcInvalidHandle

Handle to this rigid body.

DcContext *ctx=nullptr

Pointer to the context this rigid body belongs to.

DcArticulation *art=nullptr

Pointer to the articulation this rigid body belongs to, if any.
Will only be set if body is an articulation link

std ::stringname

Name of the rigid body.

pxr ::SdfPathpath

USD path of the rigid body.

::physx ::PxRigidBody*pxRigidBody=nullptr

Pointer to the PhysX rigid body.

DcHandle parentJoint=kDcInvalidHandle

Handle to the parent joint of this rigid body.

std ::vector<DcHandle >childJoints

Handles to the child joints of this rigid body.
Contains a list of joints for which this rigid body is the parent

carb::Float3origin={0.0f,0.0f,0.0f}

Origin offset for the rigid body.
Location with respect to which the body poses are set/get
