<!-- source: py/source/extensions/isaacsim.core.nodes/docs/ogn/OgnIsaacGenerate32FC1.html | title: Isaac Generate 32FC1 — Isaac Sim -->

# Isaac Generate 32FC1
Isaac Sim Node that generates a constant 32FC1 buffer

## Installation
To use this node enable isaacsim.core.nodes in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Height ( inputs:height ) | uint | Height for output image | 100
Value ( inputs:value ) | float | Value for output image | 0.0
Width ( inputs:width ) | uint | Width for output image | 100
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Data ( outputs:data ) | uchar[] | Buffer 32FC1 array data | []
Encoding ( outputs:encoding ) | token | Encoding as a token | None
Height ( outputs:height ) | uint | Height for output image | None
Width ( outputs:width ) | uint | Width for output image | None
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.core.nodes.IsaacGenerate32FC1
Version | 1
Extension | isaacsim.core.nodes
Icon | ogn/icons/isaacsim.core.nodes.IsaacGenerate32FC1.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Isaac Generate 32FC1
Categories | isaacCore
Generated Class Name | OgnIsaacGenerate32FC1Database
Python Module | isaacsim.core.nodes
[/TABLE]
