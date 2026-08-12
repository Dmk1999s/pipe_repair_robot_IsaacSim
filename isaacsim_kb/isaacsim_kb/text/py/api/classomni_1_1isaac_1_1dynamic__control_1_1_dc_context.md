<!-- source: py/api/classomni_1_1isaac_1_1dynamic__control_1_1_dc_context.html | title: DcContext — Isaac Sim -->

# DcContext
Fully qualified name: `omni::isaac::dynamic_control::DcContext`
classDcContext

Context for managing dynamic control objects in a physics scene.
Provides functionality for creating, retrieving, and managing physics objects such as rigid bodies, joints, articulations, and attractors. Maintains the mapping between USD paths and physics objects.
Public Functions
explicitDcContext(uint32_tctxId)

Constructs a DcContext with the given context ID.
Parameters:
ctxId – [in] The unique identifier for this context

uint32_tgetId()const

Gets the ID of this context.
Returns:
The context ID

DcHandle registerRigidBody(constpxr ::SdfPath&usdPath)

Registers a rigid body at the specified USD path.
Parameters:
usdPath – [in] The USD path to register

Returns:
Handle to the registered rigid body

DcHandle registerArticulation(constpxr ::SdfPath&usdPath)

Registers an articulation at the specified USD path.
Parameters:
usdPath – [in] The USD path to register

Returns:
Handle to the registered articulation

DcHandle registerD6Joint(constpxr ::SdfPath&usdPath)

Registers a D6 joint at the specified USD path.
Parameters:
usdPath – [in] The USD path to register

Returns:
Handle to the registered D6 joint

DcHandle addRigidBody(
std ::unique_ptr<DcRigidBody >&&rb,
constpxr ::SdfPath&usdPath,
)
Adds a rigid body to the context.
Parameters:

- rb – [in] The rigid body to add

- usdPath – [in] The USD path to associate with the rigid body

Returns:
Handle to the added rigid body

DcHandle addJoint(
std ::unique_ptr<DcJoint >&&joint,
constpxr ::SdfPath&usdPath,
)
Adds a joint to the context.
Parameters:

- joint – [in] The joint to add

- usdPath – [in] The USD path to associate with the joint

Returns:
Handle to the added joint

DcHandle addDof(
std ::unique_ptr<DcDof >&&dof,
constpxr ::SdfPath&usdPath,
)
Adds a degree of freedom to the context.
Parameters:

- dof – [in] The degree of freedom to add

- usdPath – [in] The USD path to associate with the degree of freedom

Returns:
Handle to the added degree of freedom

DcHandle addArticulation(
std ::unique_ptr<DcArticulation >&&art,
constpxr ::SdfPath&usdPath,
)
Adds an articulation to the context.
Parameters:

- art – [in] The articulation to add

- usdPath – [in] The USD path to associate with the articulation

Returns:
Handle to the added articulation

DcHandle addAttractor(
std ::unique_ptr<DcAttractor >&&attractor,
constpxr ::SdfPath&usdPath,
)
Adds an attractor to the context.
Parameters:

- attractor – [in] The attractor to add

- usdPath – [in] The USD path to associate with the attractor

Returns:
Handle to the added attractor

DcHandle addD6Joint(
std ::unique_ptr<DcD6Joint >&&dc_joint,
constpxr ::SdfPath&usdPath,
)
Adds a D6 joint to the context.
Parameters:

- dc_joint – [in] The D6 joint to add

- usdPath – [in] The USD path to associate with the D6 joint

Returns:
Handle to the added D6 joint

DcHandle getRigidBodyHandle(constpxr ::SdfPath&usdPath)const

Gets the handle of a rigid body at the specified USD path.
Parameters:
usdPath – [in] The USD path of the rigid body

Returns:
Handle to the rigid body, or an invalid handle if not found

DcHandle getJointHandle(constpxr ::SdfPath&usdPath)const

Gets the handle of a joint at the specified USD path.
Parameters:
usdPath – [in] The USD path of the joint

Returns:
Handle to the joint, or an invalid handle if not found

DcHandle getDofHandle(constpxr ::SdfPath&usdPath)const

Gets the handle of a degree of freedom at the specified USD path.
Parameters:
usdPath – [in] The USD path of the degree of freedom

Returns:
Handle to the degree of freedom, or an invalid handle if not found

DcHandle getArticulationHandle(constpxr ::SdfPath&usdPath)const

Gets the handle of an articulation at the specified USD path.
Parameters:
usdPath – [in] The USD path of the articulation

Returns:
Handle to the articulation, or an invalid handle if not found

DcHandle getAttractorHandle(constpxr ::SdfPath&usdPath)const

Gets the handle of an attractor at the specified USD path.
Parameters:
usdPath – [in] The USD path of the attractor

Returns:
Handle to the attractor, or an invalid handle if not found

DcRigidBody *getRigidBody(DcHandle handle)const

Gets a rigid body by its handle.
Parameters:
handle – [in] The handle of the rigid body

Returns:
Pointer to the rigid body, or nullptr if not found

DcJoint *getJoint(DcHandle handle)const

Gets a joint by its handle.
Parameters:
handle – [in] The handle of the joint

Returns:
Pointer to the joint, or nullptr if not found

DcDof *getDof(DcHandle handle)const

Gets a degree of freedom by its handle.
Parameters:
handle – [in] The handle of the degree of freedom

Returns:
Pointer to the degree of freedom, or nullptr if not found

DcArticulation *getArticulation(DcHandle handle)const

Gets an articulation by its handle.
Parameters:
handle – [in] The handle of the articulation

Returns:
Pointer to the articulation, or nullptr if not found

DcAttractor *getAttractor(DcHandle handle)const

Gets an attractor by its handle.
Parameters:
handle – [in] The handle of the attractor

Returns:
Pointer to the attractor, or nullptr if not found

DcD6Joint *getD6Joint(DcHandle handle)const

Gets a D6 joint by its handle.
Parameters:
handle – [in] The handle of the D6 joint

Returns:
Pointer to the D6 joint, or nullptr if not found

voidremoveRigidBody(DcHandle handle)

Removes a rigid body from the context.
Parameters:
handle – [in] The handle of the rigid body to remove

voidremoveJoint(DcHandle handle)

Removes a joint from the context.
Parameters:
handle – [in] The handle of the joint to remove

voidremoveArticulation(DcHandle handle)

Removes an articulation from the context.
Parameters:
handle – [in] The handle of the articulation to remove

voidremoveAttractor(DcHandle handle)

Removes an attractor from the context.
Parameters:
handle – [in] The handle of the attractor to remove

voidremoveD6Joint(DcHandle handle)

Removes a D6 joint from the context.
Parameters:
handle – [in] The handle of the D6 joint to remove

voidremove(DcHandle handle)

Removes an object from the context based on its handle.
Parameters:
handle – [in] The handle of the object to remove

voidremoveUsdPath(constpxr ::SdfPath&usdPath)

Removes all objects associated with the specified USD path.
Parameters:
usdPath – [in] The USD path to remove

intnumAttractors()const

Gets the number of attractors in the context.
Returns:
The number of attractors

intnumD6Joints()const

Gets the number of D6 joints in the context.
Returns:
The number of D6 joints

voidrefreshPhysicsPointers(boolverbose)

Refreshes the physics pointers after a reset.
Parameters:
verbose – [in] Whether to print verbose output

Public Members
omni ::physx ::IPhysx*physx=nullptr

Pointer to the PhysX interface.

omni ::physx ::IPhysxSceneQuery*physxSceneQuery=nullptr

Pointer to the PhysX scene query interface.

boolisSimulating=false

Flag indicating whether the simulation is currently running.

pxr ::UsdStageWeakPtrmStage=nullptr

Weak pointer to the USD stage.

boolwasPaused=false

Flag indicating whether the simulation was paused.

Public Static Functions
staticDcHandle registerJoint(constpxr ::SdfPath&usdPath)

Registers a joint at the specified USD path.
Parameters:
usdPath – [in] The USD path to register

Returns:
Handle to the registered joint

staticDcHandle registerDof(constpxr ::SdfPath&usdPath)

Registers a degree of freedom at the specified USD path.
Parameters:
usdPath – [in] The USD path to register

Returns:
Handle to the registered degree of freedom
