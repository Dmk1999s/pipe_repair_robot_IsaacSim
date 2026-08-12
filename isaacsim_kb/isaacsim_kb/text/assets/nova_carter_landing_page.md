<!-- source: assets/nova_carter_landing_page.html | title: Nova Carter — Isaac Sim Documentation -->

# Nova Carter
Powered by the Nova Orin™ sensor and compute architecture, Nova Carter is a complete robotics development platform that accelerates the development and deployment of next-generation Autonomous Mobile Robots (AMRs).
Nova Carter is being used as a reference platform for both Isaac AMR and Isaac ROS software, enabling real-world and simulation-based development. Nova Carter robots may be purchased from Segway Robotics .
The robot features the full Nova Orin sensor set, including four Leopard Imaging Hawk stereo cameras, four Leopard Imaging Owl fisheye cameras, IMUs, two 2D RPLidars, and one XT-32 3D Lidar. The robot digital twins with the cameras, Lidars, and IMU sensors are simulated in NVIDIA Isaac Sim and connected to the ROS 2 bridge for different robotics applications.

## Assets

### Nova Carter
The Nova Carter assets can be found on nucleus after NVIDIA Isaac Sim is installed, the Nova Carter assets are in the `/Isaac/Robots/NVIDIA/NovaCarter` folder, the ROS 2 assets are in the `/Isaac/Samples` folder, and the sample environments are in the `/Isaac/Sampls/ROS2/Scenarios/` folder.
Nova Carter

- `/Isaac/Robots/NVIDIA/NovaCarter/nova_carter.usd`, the Nova Carter robot with no sensors attached.

- `/Isaac/Samples/ROS2/Robots/Nova_Carter_ROS.usd`, the Nova Carter robot with sensors attached and ROS 2 action graph enabled. This asset has been tested and verified before release.

Furthermore the nova_carter.usd asset in NVIDIA Isaac Sim also contains prebuilt variants for different simulation and animation applications.

- Configuration:

- Base: The Nova Carter robot all individual parts assembled

- Fully Merged: The Nova Carter robot with all fixed parts merged into a single mesh for faster simulation

- No_Internals: The Nova Carter robot with no internal components like circuit board, battery.

- Skirt_only: The Nova Carter robot with only the skirt and wheels, useful for simulating the robot base without the upper structure or to mount custom parts on top.

- Physics:

- No_Physics: The Nova Carter robot with no physics, useful for visual only applications like animation

- Physics_Base: The Nova Carter robot with physics enabled

- Sensors

- None: The Nova Carter robot with no sensors attached.

- All_Sensors: The Nova Carter robot with all sensors attached.

Frames and Topic names
[TABLE]
Device Name | Frame ID | Topic name
Front Hawk | front_stereo_camera_left_optical | front_stereo_camera/left/image_raw
front_stereo_camera/left/camera_info
Front Hawk | front_stereo_camera_right_optical | front_stereo_camera/right/image_raw
front_stereo_camera/right/camera_info
Front Hawk | front_stereo_camera_imu | /front_stereo_imu/imu
Front Hawk | front_stereo_camera_left |
Front Hawk | front_stereo_camera_right |
Front Hawk | front_stereo_camera |
Back Hawk | back_stereo_camera_left_optical | back_stereo_camera/left/image_raw
back_stereo_camera/left/camera_info
Back Hawk | back_stereo_camera_right_optical | back_stereo_camera/right/image_raw
back_stereo_camera/right/camera_info
Back Hawk | back_stereo_camera_imu | back_stereo_imu/imu
Back Hawk | back_stereo_camera_left |
Back Hawk | back_stereo_camera_right |
Back Hawk | back_stereo_camera |
Left Hawk | left_stereo_camera_left_optical | left_stereo_camera/left/image_raw
left_stereo_camera/left/camera_info
Left Hawk | left_stereo_camera_right_optical | left_stereo_camera/right/image_raw
left_stereo_camera/right/camera_info
Left Hawk | left_stereo_camera_imu | left_stereo_imu/imu
Left Hawk | left_stereo_camera_left |
Left Hawk | left_stereo_camera_right |
Left Hawk | left_stereo_camera |
Right Hawk | right_stereo_camera_left_optical | right_stereo_camera/left/image_raw
right_stereo_camera/left/camera_info
Right Hawk | right_stereo_camera_right_optical | right_stereo_camera/right/image_raw
right_stereo_camera/right/camera_info
Right Hawk | right_stereo_camera_imu | right_stereo_imu/imu
Right Hawk | right_stereo_camera_left |
Right Hawk | right_stereo_camera_right |
Right Hawk | right_stereo_camera |
Front RP lidar | front_2d_lidar | front_2d_lidar/scan
Back RP lidar | back_2d_lidar | back_2d_lidar/scan
XT 32 | front_3d_lidar | front_3d_lidar/lidar_points
Front owl | front_fisheye_camera_optical | front_fisheye_camera/left/image_raw
front_fisheye_camera/left/camera_info
Front owl | front_fisheye_camera |
Back owl | back_fisheye_camera_optical | back_fisheye_camera/left/image_raw
back_fisheye_camera/left/camera_info
Back owl | back_fisheye_camera |
Left owl | left_fisheye_camera_optical | left_fisheye_camera/left/image_raw
left_fisheye_camera/left/camera_info
Left owl | left_fisheye_camera |
Right owl | right_fisheye_camera_optical | right_fisheye_camera/left/image_raw
right_fisheye_camera/left/camera_info
Right owl | right_fisheye_camera |
Chassis IMU | chassis_imu | /chassis/imu
Odometry | | /chassis/odom
TF | | /tf
[/TABLE]

### Nova Dev Kit
The Nova Dev Kit is a development platform consist of 3 hawk stereo cameras and 3 owl fisheye cameras.
Nova Dev Kit

- `/Isaac/Robots/NVIDIA/NovaCarterDevKit/nova_dev_kit_sensors.usd`, the Nova Dev Kit with sensors attached.

- `/Isaac/Samples/ROS2/Robots/Nova_Dev_Kit_ROS.usd`, the Nova Dev Kit with sensors attached and ROS 2 action graph enabled.

- `/Isaac/Samples/ROS2/Robots/Nova_Dev_Kit_On_Robot_ROS.usd`, the Nova Dev Kit ROS model attached to a Nova Carter base. This asset has been tested and verified before release.

Frames and Topic names
[TABLE]
Device Name | Frame ID | Topic name
Front Hawk | front_stereo_camera_left_optical | front_stereo_camera/left/image_raw
front_stereo_camera/left/camera_info
Front Hawk | front_stereo_camera_right_optical | front_stereo_camera/right/image_raw
front_stereo_camera/right/camera_info
Front Hawk | front_stereo_camera_imu | /front_stereo_imu/imu
Front Hawk | front_stereo_camera_left |
Front Hawk | front_stereo_camera_right |
Front Hawk | front_stereo_camera |
Left Hawk | left_stereo_camera_left_optical | left_stereo_camera/left/image_raw
left_stereo_camera/left/camera_info
Left Hawk | left_stereo_camera_right_optical | left_stereo_camera/right/image_raw
left_stereo_camera/right/camera_info
Left Hawk | left_stereo_camera_imu | left_stereo_imu/imu
Left Hawk | left_stereo_camera_left |
Left Hawk | left_stereo_camera_right |
Left Hawk | left_stereo_camera |
Right Hawk | right_stereo_camera_left_optical | right_stereo_camera/left/image_raw
right_stereo_camera/left/camera_info
Right Hawk | right_stereo_camera_right_optical | right_stereo_camera/right/image_raw
right_stereo_camera/right/camera_info
Right Hawk | right_stereo_camera_imu | right_stereo_imu/imu
Right Hawk | right_stereo_camera_left |
Right Hawk | right_stereo_camera_right |
Right Hawk | right_stereo_camera |
Front owl | front_fisheye_camera_optical | front_fisheye_camera/left/image_raw
front_fisheye_camera/left/camera_info
Front owl | front_fisheye_camera |
Left owl | left_fisheye_camera_optical | left_fisheye_camera/left/image_raw
left_fisheye_camera/left/camera_info
Left owl | left_fisheye_camera |
Right owl | right_fisheye_camera_optical | right_fisheye_camera/left/image_raw
right_fisheye_camera/left/camera_info
Right owl | right_fisheye_camera |
Odometry | | /chassis/odom
TF | | /tf
[/TABLE]

## Sensors

### Hawk Stereo Camera
The Hawk stereo camera features two RGB camera sensors and a 6 axis IMU, and it is located at `Isaac/Sensors/LeopardImaging/Hawk/hawk_v1.1_nominal.usd` The detailed specs can be found here .
Note: The front hawk is enabled by default for Nova_Carter_ROS.usd, additional hawk cameras can be enabled as needed, with increase load on computation.

- To enable to other hawk sensors, go to Window > Graph Editors > ActionGraph

- Click Edit Action Graph and select the action graph for the sensor to enable. (For example, /nova_carter_ros2_sensors/back_hawk)

- Select the Isaac Create Render Product Node for the camera (there is one for the left camera, and one for the right camera), click enabled

[image: ../_images/landing_page_carter_enable_sensor.gif]

### RPLidar
RP Lidar is a RTX based 2D lidar, that can be enabled by default and can be created by clicking Create > Isaac > Sensors > RTX Lidar > SLAMTEC > RPLIDAR S2E
Note
The RP Lidars are disabled by default, to enable them, follow the dropdown above and check `enabled`

### XT-32
XT-32 is a RTX based 3D lidar, that can be enabled by default and can be created by clicking Create > Isaac > Sensors > RTX Lidar > HESAI > PandarXT-32 10hz
Note
The XT-32 are enabled by default, to disable it, follow the dropdown above and uncheck `enabled`

## Getting Started
NVIDIA Isaac Sim has provided several ROS 2 samples with the Nova Carter robot for control and navigation.

### ROS 2 Sample Scene
First activate Windows > Examples > Robotics Examples which will open the `Robotics Examples` tab. The sample scene can be loaded after enabling the ROS 2 Bridge Extension by clicking Robotics Examples > ROS2 > Isaac ROS > Sample Scene.
This scene showcases a Nova Carter inside a small warehouse, with all Lidars and front hawk camera running from the robot frame. Please follow Multiple Sensors in RViz2 section for visualizing the sensors and install `teleop-twist-keyboard` by following the Driving Turtlebot Tutorial .

### ROS 2 Navigation Scene
The navigation scene can be loaded after enabling the ROS 2 Bridge Extension by clicking Robotics Examples > ROS2 > Navigation > Nova Carter.
Please follow ROS 2 Navigation tutorial for usage.

## Other Resources

- Nova Orin

- Isaac AMR

- Segway Nova Carter

- Isaac Sim Overview

- ROS 2 Tutorials

- Hawk Stereo Camera
