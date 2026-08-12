<!-- source: py/source/extensions/isaacsim.core.nodes/docs/ogn/OgnIsaacGenerateRGBA.html | title: Isaac Generate RGBA — Isaac Sim -->

# Isaac Generate RGBA
Isaac Sim Node that generates a constant rgba buffer

## Installation
To use this node enable isaacsim.core.nodes in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Color ( inputs:color ) | colorf[4] | Color for output image | [0.0, 0.0, 0.0, 0.0]
Height ( inputs:height ) | uint | Height for output image | 100
Width ( inputs:width ) | uint | Width for output image | 100
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Data ( outputs:data ) | uchar[] | Buffer rgba array data | []
Encoding ( outputs:encoding ) | token | Encoding as a token | None
Height ( outputs:height ) | uint | Height for output image | None
Width ( outputs:width ) | uint | Width for output image | None
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.core.nodes.IsaacGenerateRGBA
Version | 1
Extension | isaacsim.core.nodes
Icon | ogn/icons/isaacsim.core.nodes.IsaacGenerateRGBA.svg
Has State? | False
Implementation Language | Python
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Isaac Generate RGBA
Categories | isaacCore
Generated Class Name | OgnIsaacGenerateRGBADatabase
Python Module | isaacsim.core.nodes
[/TABLE]
