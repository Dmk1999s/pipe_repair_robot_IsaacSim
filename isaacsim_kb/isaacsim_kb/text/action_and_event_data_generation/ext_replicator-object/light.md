<!-- source: action_and_event_data_generation/ext_replicator-object/light.html | title: Light — Isaac Sim Documentation -->

# Light
If a mutable has attribute `type` of `light`, it’s a light. There are directional light and dome light. A light has an `intensity` attribute. Specially, a dome light has a `texture_path` attribute.
Aside from ordinary attributes of mutables, additional available attributes of lights are:

[TABLE]
Name | Type
intensity | numeric
color | numeric, dimension three list
[/TABLE]
Direct light
In the default pose, a direct light shines towards negative Z-direction.
Dome light
A dome light has light beams coming from all directions.
Additionally, available attributes of dome light are:

[TABLE]
Name | Type
texture_path | string
[/TABLE]
`texture_path` is a path to a spherical image that is a skybox. It has a color value in all directions, so that when the camera is rotated, you can observe different parts of the image.
