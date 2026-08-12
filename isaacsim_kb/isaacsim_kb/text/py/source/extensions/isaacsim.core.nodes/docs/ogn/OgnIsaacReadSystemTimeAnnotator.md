<!-- source: py/source/extensions/isaacsim.core.nodes/docs/ogn/OgnIsaacReadSystemTimeAnnotator.html | title: Isaac Read System Time Annotator — Isaac Sim -->

# Isaac Read System Time Annotator
Holds values related to system timestamps

## Installation
To use this node enable isaacsim.core.nodes in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Exec In ( inputs:execIn ) | execution | The input execution port | None
Reference Time Denominator ( inputs:referenceTimeDenominator ) | uint64 | Reference time represented as a rational number : denominator | 0
Reference Time Numerator ( inputs:referenceTimeNumerator ) | int64 | Reference time represented as a rational number : numerator | 0
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Exec Out ( outputs:execOut ) | execution | The output execution port | None
System Time ( outputs:systemTime ) | double | Current system time in seconds | None
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.core.nodes.IsaacReadSystemTimeAnnotator
Version | 1
Extension | isaacsim.core.nodes
Icon | ogn/icons/isaacsim.core.nodes.IsaacReadSystemTimeAnnotator.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Isaac Read System Time Annotator
Categories | isaacCore
Generated Class Name | OgnIsaacReadSystemTimeAnnotatorDatabase
Python Module | isaacsim.core.nodes
[/TABLE]
