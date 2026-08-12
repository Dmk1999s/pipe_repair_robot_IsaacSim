<!-- source: py/source/extensions/isaacsim.core.nodes/docs/ogn/OgnIsaacJointNameResolver.html | title: Isaac Joint Name Resolver — Isaac Sim -->

# Isaac Joint Name Resolver
Checks for any joint prims with isaac:nameOverride attributes that match the provided names and updates those names to their corresponding original prim names.

## Installation
To use this node enable isaacsim.core.nodes in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Exec In ( inputs:execIn ) | execution | The input execution port | None
Joint Names ( inputs:jointNames ) | token[] | list of prim names in the given articulation | []
Robot Path ( inputs:robotPath ) | string | path to the robot articulation root. If this is populated, targetPrim is ignored. |
Target Prim ( inputs:targetPrim ) | target | The target robot prim with robot articulation root. Ensure robotPath is empty for this to be considered. | None
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Exec Out ( outputs:execOut ) | execution | The output execution port | None
Joint Names ( outputs:jointNames ) | token[] | A list of prim names in the given articulation, where prims with isaac:nameOverride attributes have been replaced with their real names. | None
Robot Path ( outputs:robotPath ) | string | path to the robot articulation root. | None
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.core.nodes.IsaacJointNameResolver
Version | 1
Extension | isaacsim.core.nodes
Icon | ogn/icons/isaacsim.core.nodes.IsaacJointNameResolver.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Isaac Joint Name Resolver
Categories | isaacCore
Generated Class Name | OgnIsaacJointNameResolverDatabase
Python Module | isaacsim.core.nodes
[/TABLE]
