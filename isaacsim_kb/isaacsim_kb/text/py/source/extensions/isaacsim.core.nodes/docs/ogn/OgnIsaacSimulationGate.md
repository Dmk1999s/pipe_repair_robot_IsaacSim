<!-- source: py/source/extensions/isaacsim.core.nodes/docs/ogn/OgnIsaacSimulationGate.html | title: Isaac Simulation Gate — Isaac Sim -->

# Isaac Simulation Gate
Gate node that only passes through execution if simulation is playing

## Installation
To use this node enable isaacsim.core.nodes in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Exec In ( inputs:execIn ) | execution | The input execution | None
Step ( inputs:step ) | uint | Number of ticks per execution output, default is 1, set to zero or negative numbers to disable execution of connected nodes | 1
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Exec Out ( outputs:execOut ) | execution | The output execution | None
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.core.nodes.IsaacSimulationGate
Version | 1
Extension | isaacsim.core.nodes
Icon | ogn/icons/isaacsim.core.nodes.IsaacSimulationGate.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Isaac Simulation Gate
Categories | isaacCore
Generated Class Name | OgnIsaacSimulationGateDatabase
Python Module | isaacsim.core.nodes
[/TABLE]
