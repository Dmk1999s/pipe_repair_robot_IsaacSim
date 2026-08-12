<!-- source: py/source/extensions/isaacsim.core.nodes/docs/ogn/OgnIsaacGetViewportRenderProduct.html | title: Isaac Get Viewport Render Product — Isaac Sim -->

# Isaac Get Viewport Render Product
Isaac Sim node that returns the render product for a given viewport

## Installation
To use this node enable isaacsim.core.nodes in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Exec In ( inputs:execIn ) | execution | Input execution trigger | None
Viewport ( inputs:viewport ) | token | Name of the viewport to get renderproduct for |
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
Unique ID | isaacsim.core.nodes.IsaacGetViewportRenderProduct
Version | 1
Extension | isaacsim.core.nodes
Icon | ogn/icons/isaacsim.core.nodes.IsaacGetViewportRenderProduct.svg
Has State? | False
Implementation Language | Python
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Isaac Get Viewport Render Product
Categories | isaacCore
Generated Class Name | OgnIsaacGetViewportRenderProductDatabase
Python Module | isaacsim.core.nodes
[/TABLE]
