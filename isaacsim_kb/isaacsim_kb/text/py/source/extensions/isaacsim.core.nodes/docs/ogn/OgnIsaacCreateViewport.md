<!-- source: py/source/extensions/isaacsim.core.nodes/docs/ogn/OgnIsaacCreateViewport.html | title: Isaac Create Viewport — Isaac Sim -->

# Isaac Create Viewport
Isaac Sim node that creates a unique viewport

## Installation
To use this node enable isaacsim.core.nodes in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Exec In ( inputs:execIn ) | execution | Input execution trigger | None
Name ( inputs:name ) | token | Name of the viewport window |
Viewport Id ( inputs:viewportId ) | uint | If name is empty, ID is used as the name, ID == 0 is the default viewport | 0
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Exec Out ( outputs:execOut ) | execution | Input execution trigger | None
Viewport ( outputs:viewport ) | token | Name of the created viewport | None
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.core.nodes.IsaacCreateViewport
Version | 2
Extension | isaacsim.core.nodes
Icon | ogn/icons/isaacsim.core.nodes.IsaacCreateViewport.svg
Has State? | False
Implementation Language | Python
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Isaac Create Viewport
Categories | isaacCore
Generated Class Name | OgnIsaacCreateViewportDatabase
Python Module | isaacsim.core.nodes
[/TABLE]
