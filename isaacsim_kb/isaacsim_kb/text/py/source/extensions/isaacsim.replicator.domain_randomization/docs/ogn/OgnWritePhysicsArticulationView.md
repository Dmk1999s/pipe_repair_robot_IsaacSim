<!-- source: py/source/extensions/isaacsim.replicator.domain_randomization/docs/ogn/OgnWritePhysicsArticulationView.html | title: Write Physics Attribute using Tensor API — Isaac Sim -->

# Write Physics Attribute using Tensor API
This node writes physics attributes to TensorAPI views

## Installation
To use this node enable isaacsim.replicator.domain_randomization in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Attribute ( inputs:attribute ) | string | Name of attribute that is to be written |
Dist Param 1 ( inputs:dist_param_1 ) | float[] | Distribution parameter 1 | []
Dist Param 2 ( inputs:dist_param_2 ) | float[] | Distribution parameter 2 | []
Distribution ( inputs:distribution ) | string | Type of distribution used to sample values |
Exec In ( inputs:execIn ) | execution | exec | None
Indices ( inputs:indices ) | int[] | Indices of the environments to assign the physics attribute | []
Num Buckets ( inputs:num_buckets ) | int | Number of buckets to randomize from | 0
On Reset ( inputs:on_reset ) | bool | indicates whether an on_reset context triggered the execution | False
Operation ( inputs:operation ) | string | Type of randomization operation to be applied |
Prims ( inputs:prims ) | string | Name of registered view to randomize |
Values ( inputs:values ) | float[] | Values to be assigned to the physics attribute | []
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Exec Out ( outputs:execOut ) | execution | exec | None
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.replicator.domain_randomization.OgnWritePhysicsArticulationView
Version | 1
Extension | isaacsim.replicator.domain_randomization
Has State? | False
Implementation Language | Python
Default Memory Type | cpu
Generated Code Exclusions | tests
uiName | Write Physics Attribute using Tensor API
Categories | Replicator
__categoryDescriptions | Replicator,Write Attribute
Generated Class Name | OgnWritePhysicsArticulationViewDatabase
Python Module | isaacsim.replicator.domain_randomization
[/TABLE]
