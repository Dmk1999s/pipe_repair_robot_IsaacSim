<!-- source: py/api/classisaacsim_1_1asset_1_1importer_1_1mjcf_1_1_m_j_c_f_actuator.html | title: MJCFActuator — Isaac Sim -->

# MJCFActuator
Fully qualified name: `isaacsim::asset::importer::mjcf::MJCFActuator`
classMJCFActuator

Actuator component for applying forces/torques to joints.
Represents an actuator that can control joint motion through various control modes including position, velocity, torque, and general control. Contains control limits, force limits, and gain parameters for different control strategies.
Public Types
enumType

Enumeration of actuator control types.
Values:
enumeratorMOTOR

Motor actuator that applies force/torque directly.

enumeratorPOSITION

Position controller actuator.

enumeratorVELOCITY

Velocity controller actuator.

enumeratorGENERAL

General purpose actuator with custom control.

enumeratorDEFAULT

Default actuator type when not specified.

Public Functions
inlineMJCFActuator()

Public Members
Type type

Type of actuator control.

boolctrllimited

Whether control input is limited to a range.

boolforcelimited

Whether force output is limited to a range.

Vec2 ctrlrange

Control input range [min, max].

Vec2 forcerange=Vec2 (-FLT_MAX,FLT_MAX)

Force output range [min, max].

floatgear

Gear ratio for force/torque transmission.

std ::stringjoint

Name of the joint this actuator controls.

std ::stringname

Name identifier for the actuator.

floatkp

Proportional gain for position control.

floatkv

Derivative gain for velocity control.
