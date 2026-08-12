<!-- source: py/source/extensions/isaacsim.core.nodes/docs/ogn/OgnIsaacSetViewportResolution.html | title: Isaac Set Viewport Resolution — Isaac Sim -->

# Isaac Set Viewport Resolution
Isaac Sim node that sets the resolution on a viewport

## Installation
To use this node enable isaacsim.core.nodes in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Exec In ( inputs:execIn ) | execution | Input execution trigger | None
Height ( inputs:height ) | uint | Height of the viewport, in pixels | 720
Viewport ( inputs:viewport ) | token | Name of viewport to set resolution of |
Width ( inputs:width ) | uint | Width of the viewport, in pixels | 1280
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Exec Out ( outputs:execOut ) | execution | Input execution trigger | None
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.core.nodes.IsaacSetViewportResolution
Version | 1
Extension | isaacsim.core.nodes
Icon | ogn/icons/isaacsim.core.nodes.IsaacSetViewportResolution.svg
Has State? | False
Implementation Language | Python
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Isaac Set Viewport Resolution
Categories | isaacCore
Generated Class Name | OgnIsaacSetViewportResolutionDatabase
Python Module | isaacsim.core.nodes
[/TABLE]
