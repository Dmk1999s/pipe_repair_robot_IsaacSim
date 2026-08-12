<!-- source: py/api/structomni_1_1isaac_1_1dynamic__control_1_1_dynamic_control.html | title: DynamicControl — Isaac Sim -->

# DynamicControl
Fully qualified name: `omni::isaac::dynamic_control::DynamicControl`
structDynamicControl

Interface for controlling physics objects in Isaac Sim.
The Dynamic Control extension provides a set of utilities to control physics objects. It provides opaque handles for different physics objects that remain valid between PhysX scene resets, which occur whenever play or stop is pressed.
Public Members
bool(*isSimulating)()

Checks if the physics simulation is currently running.
Return:
True if simulation is running, false otherwise

DcHandle (*getRigidBody)(constchar*usdPath)

Gets a handle to a rigid body at the specified USD path.
Param usdPath:
[in] Path to the rigid body in the USD stage

Return:
Handle to the rigid body, or an invalid handle if not found

DcHandle (*getJoint)(constchar*usdPath)

Gets a handle to a joint at the specified USD path.
Param usdPath:
[in] Path to the joint in the USD stage

Return:
Handle to the joint, or an invalid handle if not found

DcHandle (*getDof)(constchar*usdPath)

Gets a handle to a degree of freedom at the specified USD path.
Param usdPath:
[in] Path to the degree of freedom in the USD stage

Return:
Handle to the degree of freedom, or an invalid handle if not found

DcHandle (*getArticulation)(constchar*usdPath)

Gets a handle to an articulation at the specified USD path.
Param usdPath:
[in] Path to the articulation in the USD stage

Return:
Handle to the articulation, or an invalid handle if not found

DcHandle (*getD6Joint)(constchar*usdPath)

Gets a handle to a D6 joint at the specified USD path.
Param usdPath:
[in] Path to the D6 joint in the USD stage

Return:
Handle to the D6 joint, or an invalid handle if not found

DcHandle (*getObject)(constchar*usdPath)

Gets a handle to a physics object at the specified USD path.
Param usdPath:
[in] Path to the physics object in the USD stage

Return:
Handle to the physics object, or an invalid handle if not found

DcObjectType (*peekObjectType)(constchar*usdPath)

Checks the type of a physics object at the specified USD path without creating a handle.
Param usdPath:
[in] Path to the physics object in the USD stage

Return:
Type of the physics object

DcObjectType (*getObjectType)(DcHandle handle)

Gets the type of a physics object from its handle.
Param handle:
[in] Handle to the physics object

Return:
Type of the physics object

constchar*(*getObjectTypeName)(DcHandle handle)

Gets the type name of a physics object from its handle.
Param handle:
[in] Handle to the physics object

Return:
Type name of the physics object as a string

bool(*wakeUpRigidBody)(DcHandle bodyHandle)

Wakes up a rigid body for simulation.
Param bodyHandle:
[in] Handle to the rigid body

Return:
True if successful, false otherwise

bool(*wakeUpArticulation)(DcHandle artHandle)

Wakes up an articulation for simulation.
Param artHandle:
[in] Handle to the articulation

Return:
True if successful, false otherwise

bool(*sleepRigidBody)(DcHandle bodyHandle)

Puts a rigid body to sleep.
Param bodyHandle:
[in] Handle to the rigid body

Return:
True if successful, false otherwise

bool(*sleepArticulation)(DcHandle artHandle)

Puts an articulation to sleep.
Param artHandle:
[in] Handle to the articulation

Return:
True if successful, false otherwise

constchar*(*getArticulationName)(DcHandle artHandle)

Gets the name of an articulation.
Param artHandle:
[in] Handle to the articulation

Return:
Name of the articulation

constchar*(*getArticulationPath)(DcHandle artHandle)

Gets the USD path of an articulation.
Param artHandle:
[in] Handle to the articulation

Return:
USD path of the articulation

size_t(*getArticulationBodyCount)(DcHandle artHandle)

Gets the number of rigid bodies in an articulation.
Param artHandle:
[in] Handle to the articulation

Return:
Number of rigid bodies in the articulation

DcHandle (*getArticulationBody)(DcHandle artHandle,size_tbodyIdx)

Gets a rigid body in an articulation by its index.
Param artHandle:
[in] Handle to the articulation

Param bodyIdx:
[in] Index of the rigid body

Return:
Handle to the rigid body

DcHandle (*findArticulationBody)(DcHandle artHandle,constchar*bodyName)

Finds a rigid body in an articulation by its name.
Param artHandle:
[in] Handle to the articulation

Param bodyName:
[in] Name of the rigid body

Return:
Handle to the rigid body, or an invalid handle if not found

int(*findArticulationBodyIndex)(DcHandle artHandle,constchar*bodyName)

Finds the index of a rigid body in an articulation by its name.
Param artHandle:
[in] Handle to the articulation

Param bodyName:
[in] Name of the rigid body

Return:
Index of the rigid body, or -1 if not found

DcHandle (*getArticulationRootBody)(DcHandle artHandle)

Gets the root rigid body of an articulation.
Param artHandle:
[in] Handle to the articulation

Return:
Handle to the root rigid body

DcRigidBodyState *(*getArticulationBodyStates)(DcHandle artHandle,constDcStateFlags &flags)

Gets the states of all rigid bodies in an articulation.
Param artHandle:
[in] Handle to the articulation

Param flags:
[in] Flags indicating which states to get (position, velocity, etc.)

Return:
Array of rigid body states

bool(*getArticulationProperties)(DcHandle artHandle,DcArticulationProperties *properties)

```
\param actor the actor.
\param states the states to set.
\param flags flags for the state to obtain (kDcStatePos, kDcStateVel, or kDcStateAll)
&zwj;/
```
bool(CARB_ABI* setArticulationBodyStates)(DcHandle artHandle, const DcRigidBodyState* states, DcStateFlags flags);
```
/**
@brief Gets the properties of an articulation
@param[in] artHandle Handle to the articulation
@param[out] properties Articulation properties to be filled
@return True if successful, false otherwise
```

bool(*setArticulationProperties)(DcHandle artHandle,constDcArticulationProperties &properties)

Sets the properties of an articulation.
Param artHandle:
[in] Handle to the articulation

Param properties:
[in] Articulation properties to set

Return:
True if successful, false otherwise

size_t(*getArticulationJointCount)(DcHandle artHandle)

Gets the number of joints in an articulation.
Param artHandle:
[in] Handle to the articulation

Return:
Number of joints in the articulation

DcHandle (*getArticulationJoint)(DcHandle artHandle,size_tjointIdx)

Gets a joint in an articulation by its index.
Param artHandle:
[in] Handle to the articulation

Param jointIdx:
[in] Index of the joint

Return:
Handle to the joint

DcHandle (*findArticulationJoint)(DcHandle artHandle,constchar*jointName)

Finds a joint in an articulation by its name.
Param artHandle:
[in] Handle to the articulation

Param jointName:
[in] Name of the joint

Return:
Handle to the joint, or an invalid handle if not found

size_t(*getArticulationDofCount)(DcHandle artHandle)

Gets the number of degrees of freedom in an articulation.
Param artHandle:
[in] Handle to the articulation

Return:
Number of degrees of freedom in the articulation

DcHandle (*getArticulationDof)(DcHandle artHandle,size_tdofIdx)

Gets a degree of freedom in an articulation by its index.
Param artHandle:
[in] Handle to the articulation

Param dofIdx:
[in] Index of the degree of freedom

Return:
Handle to the degree of freedom

DcHandle (*findArticulationDof)(DcHandle artHandle,constchar*dofName)

Finds a degree of freedom in an articulation by its name.
Param artHandle:
[in] Handle to the articulation

Param dofName:
[in] Name of the degree of freedom

Return:
Handle to the degree of freedom, or an invalid handle if not found

int(*findArticulationDofIndex)(DcHandle artHandle,constchar*dofName)

Finds the index of a degree of freedom in an articulation by its name.
Param artHandle:
[in] Handle to the articulation

Param dofName:
[in] Name of the degree of freedom

Return:
Index of the degree of freedom, or -1 if not found

bool(*getArticulationDofProperties)(DcHandle artHandle,DcDofProperties *props)

Gets the properties of all degrees of freedom in an articulation.
Param artHandle:
[in] Handle to the articulation

Param props:
[out] Array of degree of freedom properties to be filled

Return:
True if successful, false otherwise

bool(*setArticulationDofProperties)(DcHandle artHandle,constDcDofProperties *props)

Sets the properties of all degrees of freedom in an articulation.
Param artHandle:
[in] Handle to the articulation

Param props:
[in] Array of degree of freedom properties to set

Return:
True if successful, false otherwise

DcDofState *(*getArticulationDofStates)(DcHandle artHandle,constDcStateFlags &flags)

Gets the states of all degrees of freedom in an articulation.
Param artHandle:
[in] Handle to the articulation

Param flags:
[in] Flags indicating which states to get (position, velocity, etc.)

Return:
Array of degree of freedom states

DcDofState *(*getArticulationDofStateDerivatives)(DcHandle artHandle,constDcDofState *states,constfloat*efforts)

Gets the state derivatives of all degrees of freedom in an articulation.
Note
Sets the articulation DoFs and efforts to the values provided
Param artHandle:
[in] Handle to the articulation

Param states:
[in] States at which derivatives are evaluated

Param efforts:
[in] Efforts at which derivatives are evaluated

Return:
Array of degree of freedom state derivatives

bool(*setArticulationDofStates)(DcHandle artHandle,constDcDofState *states,constDcStateFlags &flags)

Sets the states of all degrees of freedom in an articulation.
Param artHandle:
[in] Handle to the articulation

Param states:
[in] Array of degree of freedom states to set

Param flags:
[in] Flags indicating which states to set (position, velocity, etc.)

Return:
True if successful, false otherwise

bool(*setArticulationDofPositionTargets)(DcHandle artHandle,constfloat*targets)

Sets the position targets of all degrees of freedom in an articulation.
Param artHandle:
[in] Handle to the articulation

Param targets:
[in] Array of position targets to set

Return:
True if successful, false otherwise

bool(*getArticulationDofPositionTargets)(DcHandle artHandle,float*targets)

Gets the position targets of all degrees of freedom in an articulation.
Param artHandle:
[in] Handle to the articulation

Param targets:
[out] Array to be filled with position targets

Return:
True if successful, false otherwise

bool(*setArticulationDofVelocityTargets)(DcHandle artHandle,constfloat*targets)

Sets the velocity targets of all degrees of freedom in an articulation.
Param artHandle:
[in] Handle to the articulation

Param targets:
[in] Array of velocity targets to set

Return:
True if successful, false otherwise

bool(*getArticulationDofVelocityTargets)(DcHandle artHandle,float*targets)

Gets the velocity targets of all degrees of freedom in an articulation.
Param artHandle:
[in] Handle to the articulation

Param targets:
[out] Array to be filled with velocity targets

Return:
True if successful, false otherwise

bool(*setArticulationDofEfforts)(DcHandle artHandle,constfloat*efforts)

Sets the efforts of all degrees of freedom in an articulation.
Param artHandle:
[in] Handle to the articulation

Param efforts:
[in] Array of efforts to set

Return:
True if successful, false otherwise

bool(*getArticulationDofEfforts)(DcHandle artHandle,float*efforts)

Gets the efforts of all degrees of freedom in an articulation.
Param artHandle:
[in] Handle to the articulation

Param efforts:
[out] Array to be filled with efforts

Return:
True if successful, false otherwise

bool(*getArticulationDofMasses)(DcHandle artHandle,float*masses)

Gets the effective masses of all degrees of freedom in an articulation.
Param artHandle:
[in] Handle to the articulation

Param masses:
[out] Array to be filled with effective masses

Return:
True if successful, false otherwise

constchar*(*getRigidBodyName)(DcHandle bodyHandle)

Gets the name of a rigid body.
Param bodyHandle:
[in] Handle to the rigid body

Return:
Name of the rigid body

constchar*(*getRigidBodyPath)(DcHandle bodyHandle)

Gets the USD path of a rigid body.
Param bodyHandle:
[in] Handle to the rigid body

Return:
USD path of the rigid body

DcHandle (*getRigidBodyParentJoint)(DcHandle bodyHandle)

Gets the parent joint of a rigid body.
Param bodyHandle:
[in] Handle to the rigid body

Return:
Handle to the parent joint, or an invalid handle if none

size_t(*getRigidBodyChildJointCount)(DcHandle bodyHandle)

Gets the number of child joints of a rigid body.
Param bodyHandle:
[in] Handle to the rigid body

Return:
Number of child joints

DcHandle (*getRigidBodyChildJoint)(DcHandle bodyHandle,size_tjointIdx)

Gets a child joint of a rigid body by its index.
Param bodyHandle:
[in] Handle to the rigid body

Param jointIdx:
[in] Index of the child joint

Return:
Handle to the child joint

DcTransform (*getRigidBodyPose)(DcHandle bodyHandle)

Gets the pose of a rigid body.
Param bodyHandle:
[in] Handle to the rigid body

Return:
Pose of the rigid body

carb::Float3(*getRigidBodyLinearVelocity)(DcHandle bodyHandle)

Gets the linear velocity of a rigid body in world coordinates.
Param bodyHandle:
[in] Handle to the rigid body

Return:
Linear velocity of the rigid body

carb::Float3(*getRigidBodyLocalLinearVelocity)(DcHandle bodyHandle)

Gets the linear velocity of a rigid body in local coordinates.
Param bodyHandle:
[in] Handle to the rigid body

Return:
Linear velocity of the rigid body in local coordinates

carb::Float3(*getRigidBodyAngularVelocity)(DcHandle bodyHandle)

Gets the angular velocity of a rigid body.
Param bodyHandle:
[in] Handle to the rigid body

Return:
Angular velocity of the rigid body

bool(*setRigidBodyDisableGravity)(DcHandle bodyHandle,constbooldisableGravity)

Enables or disables gravity for a rigid body.
Param bodyHandle:
[in] Handle to the rigid body

Param disableGravity:
[in] True to disable gravity, false to enable

Return:
True if successful, false otherwise

bool(*setRigidBodyDisableSimulation)(DcHandle bodyHandle,constbooldisableSimulation)

Enables or disables simulation for a rigid body.
Param bodyHandle:
[in] Handle to the rigid body

Param disableSimulation:
[in] True to disable simulation, false to enable

Return:
True if successful, false otherwise

bool(*setRigidBodyPose)(DcHandle bodyHandle,constDcTransform &pose)

Sets the pose of a rigid body.
Param bodyHandle:
[in] Handle to the rigid body

Param pose:
[in] Pose to set

Return:
True if successful, false otherwise

bool(*setRigidBodyLinearVelocity)(DcHandle bodyHandle,constcarb::Float3&linvel)

Sets the linear velocity of a rigid body.
Param bodyHandle:
[in] Handle to the rigid body

Param linvel:
[in] Linear velocity to set

Return:
True if successful, false otherwise

bool(*setRigidBodyAngularVelocity)(DcHandle bodyHandle,constcarb::Float3&angvel)

Sets the angular velocity of a rigid body.
Param bodyHandle:
[in] Handle to the rigid body

Param angvel:
[in] Angular velocity to set

Return:
True if successful, false otherwise

bool(*applyBodyForce)(DcHandle bodyHandle,constcarb::Float3&force,constcarb::Float3&pos,constboolglobalCoordinates)

Applies a force to a rigid body at a specific position.
Param bodyHandle:
[in] Handle to the rigid body

Param force:
[in] Force to apply

Param pos:
[in] Position at which to apply the force

Param globalCoordinates:
[in] True if force and position are in global coordinates, false if in local coordinates

Return:
True if successful, false otherwise

bool(*applyBodyTorque)(DcHandle bodyHandle,constcarb::Float3&torque,constboolglobalCoordinates)

Applies a torque to a rigid body.
Param bodyHandle:
[in] Handle to the rigid body

Param torque:
[in] Torque to apply

Param globalCoordinates:
[in] True if torque is in global coordinates, false if in local coordinates

Return:
True if successful, false otherwise

bool(*getRelativeBodyPoses)(DcHandle parentHandle,size_tnumBodies,constDcHandle *bodyHandles,DcTransform *bodyTransforms)

Gets the poses of multiple rigid bodies relative to a parent body.
Param parentHandle:
[in] Handle to the parent rigid body

Param numBodies:
[in] Number of rigid bodies

Param bodyHandles:
[in] Array of handles to the rigid bodies

Param bodyTransforms:
[out] Array to be filled with relative poses

Return:
True if successful, false otherwise

bool(*getRigidBodyProperties)(DcHandle bodyHandle,DcRigidBodyProperties *props)

Gets the properties of a rigid body.
Param bodyHandle:
[in] Handle to the rigid body

Param props:
[out] Rigid body properties to be filled

Return:
True if successful, false otherwise

bool(*setRigidBodyProperties)(DcHandle bodyHandle,constDcRigidBodyProperties &properties)

Sets the properties of a rigid body.
Param bodyHandle:
[in] Handle to the rigid body

Param properties:
[in] Rigid body properties to set

Return:
True if successful, false otherwise

constchar*(*getJointName)(DcHandle jointHandle)

Gets the name of a joint.
Param jointHandle:
[in] Handle to the joint

Return:
Name of the joint

constchar*(*getJointPath)(DcHandle jointHandle)

Gets the USD path of a joint.
Param jointHandle:
[in] Handle to the joint

Return:
USD path of the joint

DcJointType (*getJointType)(DcHandle jointHandle)

Gets the type of a joint.
Param jointHandle:
[in] Handle to the joint

Return:
Type of the joint

size_t(*getJointDofCount)(DcHandle jointHandle)

Gets the number of degrees of freedom in a joint.
Param jointHandle:
[in] Handle to the joint

Return:
Number of degrees of freedom in the joint

DcHandle (*getJointDof)(DcHandle jointHandle,size_tdofIdx)

Gets a degree of freedom in a joint by its index.
Param jointHandle:
[in] Handle to the joint

Param dofIdx:
[in] Index of the degree of freedom

Return:
Handle to the degree of freedom

DcHandle (*getJointParentBody)(DcHandle jointHandle)

Gets the parent rigid body of a joint.
Param jointHandle:
[in] Handle to the joint

Return:
Handle to the parent rigid body

DcHandle (*getJointChildBody)(DcHandle jointHandle)

Gets the child rigid body of a joint.
Param jointHandle:
[in] Handle to the joint

Return:
Handle to the child rigid body

constchar*(*getDofName)(DcHandle dofHandle)

Gets the name of a degree of freedom.
Param dofHandle:
[in] Handle to the degree of freedom

Return:
Name of the degree of freedom

constchar*(*getDofPath)(DcHandle dofHandle)

Gets the USD path of a degree of freedom.
Param dofHandle:
[in] Handle to the degree of freedom

Return:
USD path of the degree of freedom

DcDofType (*getDofType)(DcHandle dofHandle)

Gets the type of a degree of freedom.
Param dofHandle:
[in] Handle to the degree of freedom

Return:
Type of the degree of freedom

DcHandle (*getDofJoint)(DcHandle dofHandle)

Gets the joint that a degree of freedom belongs to.
Param dofHandle:
[in] Handle to the degree of freedom

Return:
Handle to the joint

DcHandle (*getDofParentBody)(DcHandle dofHandle)

Gets the parent rigid body of a degree of freedom.
Param dofHandle:
[in] Handle to the degree of freedom

Return:
Handle to the parent rigid body

DcHandle (*getDofChildBody)(DcHandle dofHandle)

Gets the child rigid body of a degree of freedom.
Param dofHandle:
[in] Handle to the degree of freedom

Return:
Handle to the child rigid body

DcDofState (*getDofState)(DcHandle dofHandle,constDcStateFlags &flags)

Gets the state of a degree of freedom.
Param dofHandle:
[in] Handle to the degree of freedom

Param flags:
[in] Flags indicating which states to get (position, velocity, etc.)

Return:
State of the degree of freedom

bool(*setDofState)(DcHandle dofHandle,constDcDofState *state,constDcStateFlags &flags)

Sets the state of a degree of freedom.
Param dofHandle:
[in] Handle to the degree of freedom

Param state:
[in] State to set

Param flags:
[in] Flags indicating which states to set (position, velocity, etc.)

Return:
True if successful, false otherwise

float(*getDofPosition)(DcHandle dofHandle)

Gets the position of a degree of freedom.
Param dofHandle:
[in] Handle to the degree of freedom

Return:
Position of the degree of freedom

bool(*setDofPosition)(DcHandle dofHandle,floatpos)

Sets the position of a degree of freedom.
Param dofHandle:
[in] Handle to the degree of freedom

Param pos:
[in] Position to set

Return:
True if successful, false otherwise

float(*getDofVelocity)(DcHandle dofHandle)

Gets the velocity of a degree of freedom.
Param dofHandle:
[in] Handle to the degree of freedom

Return:
Velocity of the degree of freedom

bool(*setDofVelocity)(DcHandle dofHandle,floatvel)

Sets the velocity of a degree of freedom.
Param dofHandle:
[in] Handle to the degree of freedom

Param vel:
[in] Velocity to set

Return:
True if successful, false otherwise

bool(*getDofProperties)(DcHandle dofHandle,DcDofProperties *props)

Gets the properties of a degree of freedom.
Param dofHandle:
[in] Handle to the degree of freedom

Param props:
[out] Degree of freedom properties to be filled

Return:
True if successful, false otherwise

bool(*setDofProperties)(DcHandle dofHandle,constDcDofProperties *props)

Sets the properties of a degree of freedom.
Param dofHandle:
[in] Handle to the degree of freedom

Param props:
[in] Degree of freedom properties to set

Return:
True if successful, false otherwise

bool(*setDofPositionTarget)(DcHandle dofHandle,floattarget)

Sets the position target of a degree of freedom.
Param dofHandle:
[in] Handle to the degree of freedom

Param target:
[in] Position target to set

Return:
True if successful, false otherwise

bool(*setDofVelocityTarget)(DcHandle dofHandle,floattarget)

Sets the velocity target of a degree of freedom.
Param dofHandle:
[in] Handle to the degree of freedom

Param target:
[in] Velocity target to set

Return:
True if successful, false otherwise

float(*getDofPositionTarget)(DcHandle dofHandle)

Gets the position target of a degree of freedom.
Param dofHandle:
[in] Handle to the degree of freedom

Return:
Position target of the degree of freedom

float(*getDofVelocityTarget)(DcHandle dofHandle)

Gets the velocity target of a degree of freedom.
Param dofHandle:
[in] Handle to the degree of freedom

Return:
Velocity target of the degree of freedom

bool(*setDofEffort)(DcHandle dofHandle,floateffort)

Sets the effort of a degree of freedom.
Param dofHandle:
[in] Handle to the degree of freedom

Param effort:
[in] Effort to set

Return:
True if successful, false otherwise

float(*getDofEffort)(DcHandle dofHandle)

Gets the effort of a degree of freedom.
Param dofHandle:
[in] Handle to the degree of freedom

Return:
Effort of the degree of freedom

DcHandle (*createRigidBodyAttractor)(constDcAttractorProperties *props)

Creates a rigid body attractor.
Param props:
[in] Properties for the attractor

Return:
Handle to the created attractor

bool(*destroyRigidBodyAttractor)(DcHandle attHandle)

Destroys a rigid body attractor.
Param attHandle:
[in] Handle to the attractor to destroy

Return:
True if successful, false otherwise

bool(*getAttractorProperties)(DcHandle attHandle,DcAttractorProperties *props)

Gets the properties of an attractor.
Param attHandle:
[in] Handle to the attractor

Param props:
[out] Attractor properties to be filled

Return:
True if successful, false otherwise

bool(*setAttractorProperties)(DcHandle attHandle,constDcAttractorProperties *props)

Sets the properties of an attractor.
Param attHandle:
[in] Handle to the attractor

Param props:
[in] Attractor properties to set

Return:
True if successful, false otherwise

bool(*setAttractorTarget)(DcHandle attHandle,constDcTransform &target)

Sets the target pose of an attractor.
Param attHandle:
[in] Handle to the attractor

Param target:
[in] Target pose to set

Return:
True if successful, false otherwise

DcHandle (*createD6Joint)(constDcD6JointProperties *props)

Creates a D6 joint between two rigid bodies.
Param props:
[in] Properties for the D6 joint

Return:
Handle to the created D6 joint

bool(*destroyD6Joint)(DcHandle jointHandle)

Destroys a D6 joint.
Param jointHandle:
[in] Handle to the D6 joint to destroy

Return:
True if successful, false otherwise

bool(*getD6JointProperties)(DcHandle jointHandle,DcD6JointProperties *props)

Gets the properties of a D6 joint.
Param jointHandle:
[in] Handle to the D6 joint

Param props:
[out] D6 joint properties to be filled

Return:
True if successful, false otherwise

bool(*getD6JointConstraintIsBroken)(DcHandle jointHandle)

Checks if a D6 joint constraint is broken.
Param jointHandle:
[in] Handle to the D6 joint

Return:
True if the joint constraint is broken, false otherwise

bool(*setD6JointProperties)(DcHandle jointHandle,constDcD6JointProperties *props)

Sets the properties of a D6 joint.
Param jointHandle:
[in] Handle to the D6 joint

Param props:
[in] D6 joint properties to set

Return:
True if successful, false otherwise

bool(*setOriginOffset)(DcHandle handle,constcarb::Float3&origin)

Sets the origin offset for a physics object.
Param handle:
[in] Handle to the physics object

Param origin:
[in] Origin offset to set

Return:
True if successful, false otherwise

DcRayCastResult (*rayCast)(constcarb::Float3&origin,constcarb::Float3&direction,floatmax_distrance)

Performs a raycast in the physics scene.
Param origin:
[in] Origin point of the ray

Param direction:
[in] Direction of the ray

Param max_distrance:
[in] Maximum distance for the raycast

Return:
Result of the raycast
