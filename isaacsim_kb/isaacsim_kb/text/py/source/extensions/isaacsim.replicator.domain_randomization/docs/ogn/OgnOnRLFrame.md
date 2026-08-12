<!-- source: py/source/extensions/isaacsim.replicator.domain_randomization/docs/ogn/OgnOnRLFrame.html | title: On Frame — Isaac Sim -->

# On Frame
Triggered every frame in an Rl setting

## Installation
To use this node enable isaacsim.replicator.domain_randomization in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Num Envs ( inputs:num_envs ) | int | number of RL environments | 0
Run ( inputs:run ) | bool | Run | False
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Exec Out ( outputs:execOut ) | execution | Output Execution | None
Frame Num ( outputs:frameNum ) | int[] | frame number for every environment | None
Reset Inds ( outputs:resetInds ) | int[] | indices of environments to be reset | None
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.replicator.domain_randomization.OgnOnRLFrame
Version | 1
Extension | isaacsim.replicator.domain_randomization
Has State? | True
Implementation Language | Python
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | On Frame
Categories | Replicator
__categoryDescriptions | Replicator,On Frame
Generated Class Name | OgnOnRLFrameDatabase
Python Module | isaacsim.replicator.domain_randomization
[/TABLE]
