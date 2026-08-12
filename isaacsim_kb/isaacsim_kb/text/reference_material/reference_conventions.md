<!-- source: reference_material/reference_conventions.html | title: Isaac Sim Conventions — Isaac Sim Documentation -->

# Isaac Sim Conventions
This section provides a reference for the units, representations, and coordinate conventions used within NVIDIA Isaac Sim.

## Default Units

[TABLE]
Measurement | Units | Notes
Length | Meter |
Mass | Kilogram |
Time | Seconds |
Physics Time-Step | Seconds | Configurable by User. Default is 1/60.
Force | Newton |
Frequency | Hertz |
Linear Drive Stiffness | \(kg/s^2\) |
Angular Drive Stiffness | \((kg*m^2)/(s^2*angle)\) |
Linear Drive Damping | \(kg/s\) |
Angular Drive Damping | \((kg*m^2)/(s*angle)\) |
Diagonal of Inertia | \((kg*m^2)\) |
[/TABLE]

## Default Rotation Representations

### Quaternions

[TABLE]
API | Representation
Isaac Sim Core | (QW, QX, QY, QZ)
USD | (QW, QX, QY, QZ)
PhysX | (QX, QY, QZ, QW)
Dynamic Control | (QX, QY, QZ, QW)
[/TABLE]

### Angles

[TABLE]
API | Representation
Isaac Sim Core | Radians
USD | Degrees
PhysX | Radians
Dynamic Control | Radians
[/TABLE]
Note
UI elements that show attributes from USD should always display angles in Degrees, even if the value comes from Physics.

### Matrix Order

[TABLE]
API | Representation
Isaac Sim Core | Row Major
USD | Row Major
[/TABLE]

### World Axes
NVIDIA Isaac Sim follows the right-handed coordinate conventions.
[image: ../_images/isaac_conventions_world_frame.png]
[TABLE]
Direction | Axis | Notes
Up | +Z |
Forward | +X |
[/TABLE]

### Default Camera Axes
[image: ../_images/isaac_conventions_camera_frame.png]
[TABLE]
Direction | Axis | Notes
Up | +Y |
Forward | -Z |
[/TABLE]
Note
Isaac Sim to ROS Conversion: To convert from Isaac Sim Camera Coordinates to ROS Camera Coordinates, rotate 180 degrees about the X-Axis.

### Image Frames (Synthetic Data)

[TABLE]
Coordinate | Corner
(0,0) | Top Left
[/TABLE]

## Sensor Axes Representation (LiDAR, Cameras)
Cameras in Isaac Sim are subject to three different types of axes definition, depending on the context of use. Here, we introduce the three conventions and how it’s used in different contexts.

### World Axes
The world axes uses the +X forward, +Z up convention. The origin of the world prim is always represented in the World axes. The camera prim, represented in the world axes, is shown in the figure below.

### USD Axes
In the computer graphics community, the USD convention is used. The USD axes uses the +Y up, -Z forward convention . In an Isaac Sim application, the Property panel displays the poses of objects in the USD stage. The poses of all objects in the stage are displayed in the world axes, with the exception of camera prims, which is displayed in the +Y up, -Z forward convention. Therefore, this convention is referred to as USD Axes in the context of camera prims. The camera prim, represented in the USD axes convention, is shown in the figure below.

### ROS Axes
The ROS axes uses the -Y up, +Z forward convention . Therefore, any camera data including transforms published to ROS 2( ROS 2 Cameras ) will be represented in this convention. The camera prim, represented in the ROS axes convention, is shown in the figure below.

### Transforms Between These Frames
For observing poses of camera prims in the proper axes convention, see the Camera Inspector tutorial.
