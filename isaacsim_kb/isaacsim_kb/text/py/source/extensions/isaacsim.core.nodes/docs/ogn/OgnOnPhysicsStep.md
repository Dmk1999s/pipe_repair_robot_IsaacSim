<!-- source: py/source/extensions/isaacsim.core.nodes/docs/ogn/OgnOnPhysicsStep.html | title: On Physics Step — Isaac Sim -->

# On Physics Step
Executes an output execution pulse for every physics Simulation Step

## Installation
To use this node enable isaacsim.core.nodes in the Extension Manager.

## Outputs

[TABLE]
Name | Type | Descripton | Default
Simulation Delta Time ( outputs:deltaSimulationTime ) | double | Simulation Time elapsed since the last update (seconds) | None
System Delta Time ( outputs:deltaSystemTime ) | double | System Time elapsed since last update (seconds) | None
Step ( outputs:step ) | execution | The execution output | None
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.core.nodes.OnPhysicsStep
Version | 1
Extension | isaacsim.core.nodes
Icon | ogn/icons/isaacsim.core.nodes.OnPhysicsStep.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | On Physics Step
Categories | event,isaacCore
Generated Class Name | OgnOnPhysicsStepDatabase
Python Module | isaacsim.core.nodes
[/TABLE]
