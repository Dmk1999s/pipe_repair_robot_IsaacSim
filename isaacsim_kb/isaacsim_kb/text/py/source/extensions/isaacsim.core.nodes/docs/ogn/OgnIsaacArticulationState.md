<!-- source: py/source/extensions/isaacsim.core.nodes/docs/ogn/OgnIsaacArticulationState.html | title: Articulation State — Isaac Sim -->

# Articulation State
Articulated robot state. The node takes either joint names or joint indices, and outputs the joint positions and velocities, as well as the measured joint efforts, forces, and torques.

## Installation
To use this node enable isaacsim.core.nodes in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Exec In ( inputs:execIn ) | execution | The input execution | None
Joint Indices ( inputs:jointIndices ) | int[] | Queried joint indices, use either Joint Names or Joint Indices, if neither is given, default to all joints | []
Joint Names ( inputs:jointNames ) | token[] | Queried joint names, use either Joint Names or Joint Indices, if neither is given, default to all joints | []
Robot Path ( inputs:robotPath ) | string | Path to the robot articulation root. If this is populated, targetPrim is ignored. |
Target Prim ( inputs:targetPrim ) | target | The target robot prim with robot articulation root. Ensure robotPath is empty for this to be considered. | None
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Joint Names ( outputs:jointNames ) | token[] | Joint names | None
Joint Positions ( outputs:jointPositions ) | double[] | Joint positions Units: linear (m) angular (rad) | None
Joint Velocities ( outputs:jointVelocities ) | double[] | Joint velocities Units: linear (m/s) angular (rad/s) | None
Measured Joint Efforts ( outputs:measuredJointEfforts ) | double[] | Measured joint efforts Force Units: linear (kg*m/s^2) i.e. a force angular (kg*m^2/s^2) i.e. a torque Acceleration Units: linear (m/s^2), i.e. a linear acceleration angular (rad/s^2) i.e. an angular acceleration | None
Measured Joint Forces ( outputs:measuredJointForces ) | double[3][] | Measured joint reaction forces Force Units: linear (kg*m/s^2) i.e. a force angular (kg*m^2/s^2) i.e. a torque Acceleration Units: linear (m/s^2), i.e. a linear acceleration angular (rad/s^2) i.e. an angular acceleration | None
Measured Joint Torques ( outputs:measuredJointTorques ) | double[3][] | Measured joint reaction torques Force Units: linear (kg*m/s^2) i.e. a force angular (kg*m^2/s^2) i.e. a torque Acceleration Units: linear (m/s^2), i.e. a linear acceleration angular (rad/s^2) i.e. an angular acceleration | None
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.core.nodes.IsaacArticulationState
Version | 1
Extension | isaacsim.core.nodes
Has State? | False
Implementation Language | Python
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Articulation State
Categories | isaacSim
__categoryDescriptions | isaacSim,robot state inside Isaac Sim
Generated Class Name | OgnIsaacArticulationStateDatabase
Python Module | isaacsim.core.nodes
[/TABLE]
