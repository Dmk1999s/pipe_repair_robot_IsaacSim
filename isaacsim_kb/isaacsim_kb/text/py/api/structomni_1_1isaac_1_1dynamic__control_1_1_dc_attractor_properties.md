<!-- source: py/api/structomni_1_1isaac_1_1dynamic__control_1_1_dc_attractor_properties.html | title: DcAttractorProperties — Isaac Sim -->

# DcAttractorProperties
Fully qualified name: `omni::isaac::dynamic_control::DcAttractorProperties`
structDcAttractorProperties

Properties to set up a pose attractor.
Properties to set up a pose attractor
The Attractor is used to pull a rigid body towards a pose. Each pose axis can be individually selected.
Public Members
DcHandle rigidBody=kDcInvalidHandle

Rigid body to set the attractor to.

DcAxisFlags axes=0

Axes to set the attractor, using DcTransformAxesFlags. Multiple axes can be selected using bitwise combination of each axis flag. if axis flag is set to zero, the attractor will be disabled and won’t impact in solver computational complexity.

DcTransform target={kTransformIdentity }

Target pose to attract to.

DcTransform offset={kTransformIdentity }

Offset from rigid body origin to set the attractor pose.

floatstiffness=1e5f

Stiffness to be used on attraction for solver. Stiffness value should be larger than the largest agent kinematic chain stifness.

floatdamping=1e3f

Damping to be used on attraction solver.

floatforceLimit=std ::numeric_limits<float>::max()

Maximum force to be applied by drive.
