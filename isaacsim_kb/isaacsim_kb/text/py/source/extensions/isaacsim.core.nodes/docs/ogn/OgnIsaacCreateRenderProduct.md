<!-- source: py/source/extensions/isaacsim.core.nodes/docs/ogn/OgnIsaacCreateRenderProduct.html | title: Isaac Create Render Product — Isaac Sim -->

# Isaac Create Render Product
Isaac Sim node that creates a render product for use with offscreen rendering

## Installation
To use this node enable isaacsim.core.nodes in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Camera Prim ( inputs:cameraPrim ) | target | Usd prim reference to the camera associated with this render product | None
Enabled ( inputs:enabled ) | bool | Set to false to disable downstream execution and RP creation | True
Exec In ( inputs:execIn ) | execution | Input execution trigger | None
Height ( inputs:height ) | uint | Height of the render product, in pixels | 720
Width ( inputs:width ) | uint | Width of the render product, in pixels | 1280
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Exec Out ( outputs:execOut ) | execution | Output execution trigger | None
Render Product Path ( outputs:renderProductPath ) | token | Render product path for the created hydra texture | None
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.core.nodes.IsaacCreateRenderProduct
Version | 2
Extension | isaacsim.core.nodes
Icon | ogn/icons/isaacsim.core.nodes.IsaacCreateRenderProduct.svg
Has State? | False
Implementation Language | Python
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Isaac Create Render Product
Categories | isaacCore
Generated Class Name | OgnIsaacCreateRenderProductDatabase
Python Module | isaacsim.core.nodes
[/TABLE]
