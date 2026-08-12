<!-- source: py/docs/extsbuild/isaacsim.util.debug_draw/docs/ogn/OgnIsaacXPrimRadiusVisualizer.html | title: Isaac xPrim Radius Visualizer Node — Isaac Sim -->

# Isaac xPrim Radius Visualizer Node
displays the Radius of the xPrim for visualization.

## Installation
To use this node enable isaacsim.util.debug_draw in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Draw X Axis ( inputs:drawXAxis ) | bool | True to draw the x axis circle | True
Draw Y Axis ( inputs:drawYAxis ) | bool | True to draw the y axis circle | True
Draw Z Axis ( inputs:drawZAxis ) | bool | True to draw the z axis circle | True
Exec In ( inputs:execIn ) | execution | The input execution port | None
Radius ( inputs:radius ) | float | Radius of the sphere | 1
Segments ( inputs:segments ) | int | Number of segments in the circle | 30
Thickness ( inputs:thickness ) | float | Thickness of the radius lines | 1
X Axis Color ( inputs:xAxisColor ) | colorf[4] | Color of the x axis sphere points | [1, 0, 0, 1]
xPrim ( inputs:xPrim ) | target | Usd prim to visualize | None
Y Axis Color ( inputs:yAxisColor ) | colorf[4] | Color of the y axis sphere points | [0, 1, 0, 1]
Z Axis Color ( inputs:zAxisColor ) | colorf[4] | Color of the z axis sphere points | [0, 0, 1, 1]
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.util.debug_draw.IsaacXPrimRadiusVisualizer
Version | 1
Extension | isaacsim.util.debug_draw
Icon | ogn/icons/isaacsim.util.debug_draw.IsaacXPrimRadiusVisualizer.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Isaac xPrim Radius Visualizer Node
Categories | isaacDebugDraw
Generated Class Name | OgnIsaacXPrimRadiusVisualizerDatabase
Python Module | isaacsim.util.debug_draw
[/TABLE]
