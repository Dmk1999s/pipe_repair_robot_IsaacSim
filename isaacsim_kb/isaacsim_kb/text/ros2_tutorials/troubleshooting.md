<!-- source: ros2_tutorials/troubleshooting.html | title: ROS 2 Troubleshooting — Isaac Sim Documentation -->

# ROS 2 Troubleshooting
This page consolidates troubleshooting information for ROS 2 components in Isaac Sim.

## ROS 2 Multi-Navigation Issues
The ROS 2 Multi-Navigation tutorial has high CPU usage. If you observe instances of robots colliding or experiencing localization issues, it’s likely because the Nav2 stack is unable to properly synchronize with sensor data, resulting in missed controller commands.
To improve Nav2 performance:

- Try enabling the Publish Full Scan checkbox accessible through the publish_front_3d_lidar_scan OmniGraph node found in the ros_lidars action graph under each robot.

- If the previous step still results in issues, try running Isaac Sim from the terminal using the following command:

```
./isaac-sim.sh --/app/asyncRendering=true --/app/renderFrameTimeout=60 --/app/asyncPhysics=true
```

## ROS 2 Camera Issues
If your depth image only shows black and white sections, it is likely due to somewhere in the field of view having “infinite” depth, which skews the contrast. Adjust your field of view so that the depth range in the image is limited.
If your RGB camera images appear distorted or have incorrect coloring, check the following:

- Ensure proper camera parameters are set in the ROS 2 camera publisher node

- Verify that the render product resolution matches your expected output

- Check if anti-aliasing settings are affecting the image quality

## MoveIt Integration Issues
If your Rviz window is showing a black screen where the robot should be, you can update your mesa driver. Add the following commands to `moveit2_tutorials/doc/how_to_guides/isaac_panda/.docker/Dockerfile` after line 17:

```
# update mesa driver
RUN apt update && apt install -y software-properties-common && add-apt-repository ppa:kisak/kisak-mesa && apt install -y mesa-utils
RUN apt -y upgrade
```

## ROS 2 TurtleBot Movement Issues
For TurtleBot movement issues, make sure your robot is on the ground. The table has different properties, making it difficult for the robot to move on it.
Potential solutions: 1. Change the properties of either the ground or the wheels 2. Adjust the friction coefficients on the robot’s wheels 3. Verify that the correct controller parameters are being used

## ROS 2 Publish Rate Issues
If you observe publish rates that differ from the target simulation frame rate, try:

- Running Isaac Sim with factory settings to clear any persistent simulation frame rate settings:

```
./isaac-sim.sh --reset-user
```

- Check your computer’s CPU usage to identify bottlenecks. If Isaac Sim is exhibiting incredibly high usage, try running with Fabric enabled.

If you observe that the /camera_1/rgb/image_raw topic is publishing at a slower rate than anticipated, it can be because the large size of each image message is causing bottlenecks in network traffic or DDS queue management. To improve the publish rate, try reducing the dimensions of the render product resolution by modifying the dimensions in the render product node attached to the image publisher.

## ROS 2 QoS Profile Issues
The ROS 2 QoS Profile OmniGraph node is unable to save custom profiles unless you manually change the createProfile input to “Custom” first before updating the other fields.
When using sensor data with RViz, be aware that all sensors and images in Isaac Sim are being published with Sensor Data QoS . If you wish to visualize the images in RViz, expand the image tab, navigate to Topic > Reliability Policy and change the policy to Best Effort.

## General ROS 2 Issues

- If you encounter warnings similar to the following when running ROS 2 sample assets, they can be ignored:

```
[Warning] [omni.graph.core.plugin] /iw_hub/front_hawk/left_camera_publish_camera_info: [/iw_hub/front_hawk] OmniGraph Warning: OgnROS2CameraHelper:sensor_type == camera_info is deprecated as of Isaac Sim 4.1.0 in favour of OgnROS2CameraInfoHelper.
(from compute() at line 208 in ./_build/linux-x86_64/release/exts/isaacsim.ros2.bridge/isaacsim/ros2/bridge/ogn/python/nodes/OgnROS2CameraHelper.py)
```

- In certain instances, prolonged execution of the ROS 2 `carter_warehouse_navigation.usd` sample scene or the ROS 2 Joint State publisher with the `franka_alt_fingers.usd` asset can lead to a memory leak.

- When using OmniGraph nodes with ROS 2, make sure to save your scene after setting up the nodes and before hitting play to ensure all values are correctly set.

- The ROS 2 Auto Namespace feature can not correctly apply to all nodes in complex hierarchies. Review your node namespaces in ROS 2 command line tools to ensure they’re behaving as expected.
