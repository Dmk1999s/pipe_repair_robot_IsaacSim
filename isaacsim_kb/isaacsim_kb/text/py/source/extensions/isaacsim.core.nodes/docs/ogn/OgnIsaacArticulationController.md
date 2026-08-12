<!-- source: py/source/extensions/isaacsim.core.nodes/docs/ogn/OgnIsaacArticulationController.html | title: Articulation Controller — Isaac Sim -->

# Articulation Controller
Controller for articulated robots. The controller takes either joint names or joint indices, and move them by the given position/velocity/effort commands. Note angular units are expressed in radians while angles in USD are expressed in degrees and will be adjusted accordingly by the articulation controller.

## Installation
To use this node enable isaacsim.core.nodes in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Effort Command ( inputs:effortCommand ) | double[] | effort commands Force Units: linear (kg*m/s^2) i.e. a force angular (kg*m^2/s^2) i.e. a torque Acceleration Units: linear (m/s^2), i.e. a linear acceleration angular (rad/s^2) i.e. an angular acceleration | []
Exec In ( inputs:execIn ) | execution | The input execution | None
Joint Indices ( inputs:jointIndices ) | int[] | commanded joint indices, use either Joint Names or Joint Indices, if neither is given, default to all joints | []
Joint Names ( inputs:jointNames ) | token[] | commanded joint names, use either Joint Names or Joint Indices, if neither is given, default to all joints | []
Position Command ( inputs:positionCommand ) | double[] | position commands Units: linear (m) angular (rad) | []
Robot Path ( inputs:robotPath ) | string | path to the robot articulation root. If this is populated, targetPrim is ignored. |
Target Prim ( inputs:targetPrim ) | target | The target robot prim with robot articulation root. Ensure robotPath is empty for this to be considered. | None
Velocity Command ( inputs:velocityCommand ) | double[] | velocity commands Units: linear (m/s) angular (rad/s) | []
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.core.nodes.IsaacArticulationController
Version | 1
Extension | isaacsim.core.nodes
Has State? | False
Implementation Language | Python
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Articulation Controller
Categories | isaacSim
__categoryDescriptions | isaacSim,robot controller inside Isaac Sim
Generated Class Name | OgnIsaacArticulationControllerDatabase
Python Module | isaacsim.core.nodes
[/TABLE]
