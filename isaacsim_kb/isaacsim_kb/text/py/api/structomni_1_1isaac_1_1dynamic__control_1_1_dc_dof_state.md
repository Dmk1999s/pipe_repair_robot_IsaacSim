<!-- source: py/api/structomni_1_1isaac_1_1dynamic__control_1_1_dc_dof_state.html | title: DcDofState — Isaac Sim -->

# DcDofState
Fully qualified name: `omni::isaac::dynamic_control::DcDofState`
structDcDofState

State of a degree of freedom.
Contains the position, velocity, and effort of a degree of freedom
Public Members
floatpos

DOF position, in radians if it’s a revolute DOF, or meters, if it’s a prismatic DOF.

floatvel

DOF velocity, in radians/s if it’s a revolute DOF, or m/s, if it’s a prismatic DOF.

floateffort

DOF effort, torque if it’s a revolute DOF, or force if it’s a prismatic DOF.
