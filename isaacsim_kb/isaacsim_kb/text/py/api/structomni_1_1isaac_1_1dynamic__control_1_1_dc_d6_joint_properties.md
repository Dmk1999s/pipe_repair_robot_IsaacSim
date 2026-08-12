<!-- source: py/api/structomni_1_1isaac_1_1dynamic__control_1_1_dc_d6_joint_properties.html | title: DcD6JointProperties — Isaac Sim -->

# DcD6JointProperties
Fully qualified name: `omni::isaac::dynamic_control::DcD6JointProperties`
structDcD6JointProperties

Properties to set up a D6 Joint.
Properties to set up a D6 Joint
The Joint is used to connect two rigid bodies.
Public Members
char*name={nullptr}

Name of the joint.

DcHandle body0=kDcInvalidHandle

Rigid body to set the joint to.

DcHandle body1=kDcInvalidHandle

Rigid body to set the joint to.

DcAxisFlags axes=kDcAxisNone

Joint Axes, using DcTransformAxesFlags. Multiple axes can be selected using bitwise combination of each axis flag. if axis flag is set to zero, the joint will be disabled and won’t impact in solver computational complexity.

DcTransform pose0={kTransformIdentity }

Offset from Rigid Body 0 to Joint.

DcTransform pose1={kTransformIdentity }

Offset from Rigid Body 1 to Joint.

DcJointType jointType

Joint type being defined.

boolhasLimits[6]

Flag for determining if joint has limits or is locked.

boolsoftLimit={true}

Whether joint limits are progressively harder (soft limits) or rigid.

floatlowerLimit

lower joint limit, same for all axes

floatupperLimit

upper joint limit, same for all axes

floatlimitStiffness={1e5f}

Joint Stiffness.

floatlimitDamping={1e3f}

Joint Damping.

floatstiffness={1e5f}

Joint Stiffness.

floatdamping={1e3f}

Joint Damping.

floatforceLimit=std ::numeric_limits<float>::max()

Joint Breaking Force.

floattorqueLimit=std ::numeric_limits<float>::max()

Joint Breaking torque.
