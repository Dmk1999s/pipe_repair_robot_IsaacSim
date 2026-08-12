<!-- source: py/api/structomni_1_1isaac_1_1dynamic__control_1_1_dc_dof_properties.html | title: DcDofProperties — Isaac Sim -->

# DcDofProperties
Fully qualified name: `omni::isaac::dynamic_control::DcDofProperties`
structDcDofProperties

Properties of a degree-of-freedom.
Contains settings that control the behavior of a degree of freedom
Public Members
DcDofType type=DcDofType ::eNone

Type of dof (read-only property)

boolhasLimits=false

Flags whether the DOF has limits. (read-only property)

floatlower=0.0f

lower limit of DOF. In radians or meters (read-only property)

floatupper=0.0f

upper limit of DOF. In radians or meters (read-only property)

DcDriveMode driveMode=DcDriveMode ::eAcceleration

Drive mode for the DOF. See DcDriveMode.

floatmaxVelocity=std ::numeric_limits<float>::max()

Maximum velocity of DOF. In Radians/s, or m/s.

floatmaxEffort=std ::numeric_limits<float>::max()

Maximum effort of DOF. in N or Nm.

floatstiffness=0.0f

Stiffness of DOF.

floatdamping=0.0f

Damping of DOF.
