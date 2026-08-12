<!-- source: action_and_event_data_generation/ext_replicator-object/camera.html | title: Camera — Isaac Sim Documentation -->

# Camera
If a mutable has an attribute `type` of `camera`, it’s a camera. Typically, a basic pinhole camera model is used.
Required attributes of a camera:

[TABLE]
Name | Type
camera_parameters | dict
[/TABLE]
`camera_parameters` is a dictionary with the following six required keys:

[TABLE]
Name | Type
screen_width | int
screen_height | int
focal_length | numeric
horizontal_aperture | numeric
near_clip | numeric
far_clip | numeric
[/TABLE]

## Pinhole Model
3D objects are projected onto a 2D plane, like this:
Looking from a top view, towards the negative Y-axis:
In the picture, f, which is the distance from the camera to the projection plane, is `focal_length`. hA is the distance from the left edge (upper end) to the right edge (lower end) and stands for `horizontal_aperture`.
`near_clip` and `far_clip` define two planes perpendicular to the line of vision between which you can observe things.

## Assumptions
The following assumptions are made in frame of reference and conversion from/to other common representations.
If no transform operator is applied on the camera, the Y-axis points upwards and X-axis points to the right. The camera looks towards negative direction of the Z-axis.
