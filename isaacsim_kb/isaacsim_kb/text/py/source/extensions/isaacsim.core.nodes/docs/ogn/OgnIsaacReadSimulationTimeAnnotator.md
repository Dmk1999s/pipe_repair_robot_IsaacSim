<!-- source: py/source/extensions/isaacsim.core.nodes/docs/ogn/OgnIsaacReadSimulationTimeAnnotator.html | title: Isaac Read Simulation Time Annotator — Isaac Sim -->

# Isaac Read Simulation Time Annotator
Holds values related to simulation timestamps

## Installation
To use this node enable isaacsim.core.nodes in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Exec In ( inputs:execIn ) | execution | The input execution port | None
Reference Time Denominator ( inputs:referenceTimeDenominator ) | uint64 | Reference time represented as a rational number : denominator | 0
Reference Time Numerator ( inputs:referenceTimeNumerator ) | int64 | Reference time represented as a rational number : numerator | 0
Reset On Stop ( inputs:resetOnStop ) | bool | If True the simulation time will reset when stop is pressed, False means time increases monotonically | False
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Exec Out ( outputs:execOut ) | execution | The output execution port | None
Simulation Time ( outputs:simulationTime ) | double | Current Simulation Time in Seconds | None
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.core.nodes.IsaacReadSimulationTimeAnnotator
Version | 1
Extension | isaacsim.core.nodes
Icon | ogn/icons/isaacsim.core.nodes.IsaacReadSimulationTimeAnnotator.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Isaac Read Simulation Time Annotator
Categories | isaacCore
Generated Class Name | OgnIsaacReadSimulationTimeAnnotatorDatabase
Python Module | isaacsim.core.nodes
[/TABLE]
