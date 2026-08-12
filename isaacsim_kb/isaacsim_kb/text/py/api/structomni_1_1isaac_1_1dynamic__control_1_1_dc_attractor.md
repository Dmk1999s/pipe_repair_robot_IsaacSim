<!-- source: py/api/structomni_1_1isaac_1_1dynamic__control_1_1_dc_attractor.html | title: DcAttractor — Isaac Sim -->

# DcAttractor
Fully qualified name: `omni::isaac::dynamic_control::DcAttractor`
structDcAttractor

Represents an attractor in the physics simulation.
Contains all the information needed to represent and manipulate an attractor, which is used to apply forces to rigid bodies to attract them to a target pose.
Public Members
DcHandle handle=kDcInvalidHandle

Handle to this attractor.

DcContext *ctx=nullptr

Pointer to the context this attractor belongs to.

::physx ::PxD6Joint*pxJoint=nullptr

Pointer to the PhysX D6 joint used to implement the attractor.

DcAttractorProperties props={}

Properties of the attractor.

pxr ::SdfPathpath

USD path of the attractor.
