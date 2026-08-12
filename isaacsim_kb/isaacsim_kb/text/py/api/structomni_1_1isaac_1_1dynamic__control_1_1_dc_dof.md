<!-- source: py/api/structomni_1_1isaac_1_1dynamic__control_1_1_dc_dof.html | title: DcDof — Isaac Sim -->

# DcDof
Fully qualified name: `omni::isaac::dynamic_control::DcDof`
structDcDof

Represents a degree of freedom in the physics simulation.
Contains all the information needed to represent and manipulate a degree of freedom, including its PhysX representation, name, path, and relationships to other objects.
Public Members
DcHandle handle=kDcInvalidHandle

Handle to this degree of freedom.

DcContext *ctx=nullptr

Pointer to the context this degree of freedom belongs to.

DcDofType type=DcDofType ::eNone

Type of the degree of freedom.

DcArticulation *art=nullptr

Pointer to the articulation this degree of freedom belongs to.

std ::stringname

Name of the degree of freedom.

pxr ::SdfPathpath

USD path of the degree of freedom.

::physx ::PxArticulationJointReducedCoordinate*pxArticulationJoint=nullptr

Pointer to the PhysX articulation joint this degree of freedom belongs to.

::physx ::PxArticulationAxis::EnumpxAxis=::physx ::PxArticulationAxis::eTWIST

PhysX axis of this degree of freedom.

DcDriveMode driveMode=DcDriveMode ::eAcceleration

Drive mode of this degree of freedom.

size_tcacheIdx=0

Index in the PhysX articulation cache.
Used to access this DOF’s data in the articulation cache

DcHandle joint=kDcInvalidHandle

Handle to the joint this degree of freedom belongs to.
