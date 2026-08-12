<!-- source: py/api/structomni_1_1isaac_1_1dynamic__control_1_1_dc_rigid_body_properties.html | title: DcRigidBodyProperties — Isaac Sim -->

# DcRigidBodyProperties
Fully qualified name: `omni::isaac::dynamic_control::DcRigidBodyProperties`
structDcRigidBodyProperties

Properties of a rigid body.
Contains settings that control the behavior of a rigid body
Public Members
floatmass

Mass of the rigid body.

carb::Float3moment

Moment of inertia of the rigid body.

carb::Float3cMassLocalPose

Local pose of the center of mass.

floatmaxDepenetrationVelocity=std ::numeric_limits<float>::max()

Maximum velocity used for depenetration.

floatmaxContactImpulse=std ::numeric_limits<float>::max()

Maximum impulse that can be applied at a contact.

uint32_tsolverPositionIterationCount=16

Number of position iterations for the solver.

uint32_tsolverVelocityIterationCount=1

Number of velocity iterations for the solver.
