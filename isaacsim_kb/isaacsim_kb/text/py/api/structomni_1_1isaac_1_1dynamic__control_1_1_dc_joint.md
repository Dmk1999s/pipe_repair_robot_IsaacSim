<!-- source: py/api/structomni_1_1isaac_1_1dynamic__control_1_1_dc_joint.html | title: DcJoint — Isaac Sim -->

# DcJoint
Fully qualified name: `omni::isaac::dynamic_control::DcJoint`
structDcJoint

Represents a joint in the physics simulation.
Contains all the information needed to represent and manipulate a joint, including its PhysX representation, name, path, and relationships to other objects.
Public Members
DcHandle handle=kDcInvalidHandle

Handle to this joint.

DcContext *ctx=nullptr

Pointer to the context this joint belongs to.

DcJointType type=DcJointType ::eNone

Type of the joint.

DcArticulation *art=nullptr

Pointer to the articulation this joint belongs to, if any.
Will only be set if joint is an articulation joint

std ::stringname

Name of the joint.

pxr ::SdfPathpath

USD path of the joint.

::physx ::PxArticulationJointReducedCoordinate*pxArticulationJoint=nullptr

Pointer to the PhysX articulation joint.
Only reduced coordinate articulation joints are supported for now

DcHandle parentBody=kDcInvalidHandle

Handle to the parent body of this joint.

DcHandle childBody=kDcInvalidHandle

Handle to the child body of this joint.

std ::vector<DcHandle >dofs

Handles to the degrees of freedom of this joint.
