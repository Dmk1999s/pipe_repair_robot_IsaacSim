<!-- source: py/source/extensions/isaacsim.core.nodes/docs/ogn/OgnIsaacReadEnvVar.html | title: Isaac Read Env Var — Isaac Sim -->

# Isaac Read Env Var
Loads in environment variable if present

## Installation
To use this node enable isaacsim.core.nodes in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Input String ( inputs:envVar ) | string | Input OS environment variable name as string |
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Output Value ( outputs:value ) | string | Output OS environment variable value, returns empty string if variable is not found |
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.core.nodes.IsaacReadEnvVar
Version | 1
Extension | isaacsim.core.nodes
Icon | ogn/icons/isaacsim.core.nodes.IsaacReadEnvVar.svg
Has State? | False
Implementation Language | Python
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Isaac Read Env Var
Categories | isaacCore
Generated Class Name | OgnIsaacReadEnvVarDatabase
Python Module | isaacsim.core.nodes
[/TABLE]
