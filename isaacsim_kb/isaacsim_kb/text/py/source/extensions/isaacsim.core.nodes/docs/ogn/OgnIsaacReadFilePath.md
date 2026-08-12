<!-- source: py/source/extensions/isaacsim.core.nodes/docs/ogn/OgnIsaacReadFilePath.html | title: Isaac Read File Path — Isaac Sim -->

# Isaac Read File Path
Loads contents of file when given path, if file exists

## Installation
To use this node enable isaacsim.core.nodes in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Input Path ( inputs:path ) | path | Input path to file |
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Output File Contents ( outputs:fileContents ) | ['string', 'token'] | Output contents of file at path, returns empty string if file is not found |
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.core.nodes.IsaacReadFilePath
Version | 1
Extension | isaacsim.core.nodes
Icon | ogn/icons/isaacsim.core.nodes.IsaacReadFilePath.svg
Has State? | False
Implementation Language | Python
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Isaac Read File Path
Categories | isaacCore
Generated Class Name | OgnIsaacReadFilePathDatabase
Python Module | isaacsim.core.nodes
[/TABLE]
