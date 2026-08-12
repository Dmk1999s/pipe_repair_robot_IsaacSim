<!-- source: py/api/structomni_1_1isaac_1_1dynamic__control_1_1_dc_articulation.html | title: DcArticulation — Isaac Sim -->

# DcArticulation
Fully qualified name: `omni::isaac::dynamic_control::DcArticulation`
structDcArticulation

Represents an articulation in the physics simulation.
Contains all the information needed to represent and manipulate an articulation, including its PhysX representation, name, path, and relationships to other objects. An articulation is a collection of rigid bodies connected by joints.
Public Functions
inlinesize_tnumRigidBodies()const

Gets the number of rigid bodies in this articulation.
Returns:
The number of rigid bodies

inlinesize_tnumJoints()const

Gets the number of joints in this articulation.
Returns:
The number of joints

inlinesize_tnumDofs()const

Gets the number of degrees of freedom in this articulation.
Returns:
The number of degrees of freedom

boolrefreshCache(
const::physx ::PxArticulationCacheFlags&flags=::physx ::PxArticulationCacheFlag::eALL,
)const
Refreshes the PhysX articulation cache.
Parameters:
flags – [in] Flags indicating which parts of the cache to refresh

Returns:
True if successful, false otherwise

Public Members
DcHandle handle=kDcInvalidHandle

Handle to this articulation.

DcContext *ctx=nullptr

Pointer to the context this articulation belongs to.

::physx ::PxArticulationReducedCoordinate*pxArticulation=nullptr

Pointer to the PhysX articulation.

std ::stringname

Name of the articulation.

pxr ::SdfPathpath

USD path of the articulation.

std ::set<pxr ::SdfPath>componentPaths

USD paths of the components of this articulation.

std ::vector<DcRigidBody *>rigidBodies

Handles to the rigid bodies in this articulation.

std ::vector<DcJoint *>joints

Handles to the joints in this articulation.

std ::vector<DcDof *>dofs

Handles to the degrees of freedom in this articulation.

std ::map<std ::string,DcRigidBody *>rigidBodyMap

Map from rigid body names to handles.

std ::map<std ::string,DcJoint *>jointMap

Map from joint names to handles.

std ::map<std ::string,DcDof *>dofMap

Map from degree of freedom names to handles.

mutable::physx ::PxArticulationCache*pxArticulationCache=nullptr

Pointer to the PhysX articulation cache.

mutableint64_tcacheAge=-1

Age of the cache, used to determine when to refresh.

mutablestd ::vector<DcRigidBodyState >rigidBodyStateCache

Cache of rigid body states.

mutablestd ::vector<DcDofState >dofStateCache

Cache of degree of freedom states.
