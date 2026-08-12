<!-- source: py/source/extensions/isaacsim.core.nodes/docs/ogn/OgnIsaacSetCameraOnRenderProduct.html | title: Isaac Set Camera — Isaac Sim -->

# Isaac Set Camera
Isaac Sim node that sets the camera prim of an existing render product

## Installation
To use this node enable isaacsim.core.nodes in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Camera Prim ( inputs:cameraPrim ) | target | Usd prim reference to the camera associated with this render product | None
Exec In ( inputs:execIn ) | execution | Input execution trigger | None
Render Product Path ( inputs:renderProductPath ) | token | Path of the render product |
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Exec Out ( outputs:execOut ) | execution | Output execution trigger | None
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.core.nodes.IsaacSetCameraOnRenderProduct
Version | 1
Extension | isaacsim.core.nodes
Icon | ogn/icons/isaacsim.core.nodes.IsaacSetCameraOnRenderProduct.svg
Has State? | False
Implementation Language | Python
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Isaac Set Camera
Categories | isaacCore
Generated Class Name | OgnIsaacSetCameraOnRenderProductDatabase
Python Module | isaacsim.core.nodes
[/TABLE]
