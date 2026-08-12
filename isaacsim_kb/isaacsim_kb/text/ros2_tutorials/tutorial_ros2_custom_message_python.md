<!-- source: ros2_tutorials/tutorial_ros2_custom_message_python.html | title: ROS 2 Python Custom Messages — Isaac Sim Documentation -->

# ROS 2 Python Custom Messages
Note
ROS 2 Python Custom Messages with Isaac Sim is fully supported on Linux. On Windows (WSL), this workflow is not supported.

## Learning Objectives
In this example, you learn how to use ROS 2 `rclpy` Python interface with Isaac Sim for a custom message.

## Getting Started
Prerequisite

- Basic understanding of building ROS 2 packages .

## Using Custom Messages with Python
For using `rclpy` with Isaac Sim the packages must be built with `Python3.11`. You can create your own package and build it with the ROS 2 workspace
Isaac Sim only supports Python 3.11. Packages built can be used directly with `rclpy` in Isaac Sim, if they are built with Python 3.11.
For demonstrating the workflow, the tutorial uses a `custom_message` package, which is a part of the Isaac Sim ROS Workspace repository. This repository contains a custom message under `custom_message/msg/SampleMsg.msg` with the following definition:

```
std_msgs/String my_string
int64 my_num
```
To build your own ROS 2 custom message packages for use with Isaac Sim, you can place the package under `humble_ws/src` or `jazzy_ws/src` in your `Isaac Sim ROS Workspace` folder. Then run `./build_ros.sh` and source your workspaces before running Isaac Sim. Ensure you have completed the steps in the ROS Installation Guide following the installation track for custom packages.

- Run Isaac Sim from the same terminal, the sourced workspace contains the minimal ROS 2 dependencies needed to enable the ROS 2 bridge and the `custom_message` package, which contains our sample message.

Using the `custom_message` package with Python in Isaac Sim:

## Summary
This tutorial covered the following topics:

- Building a ROS 2 custom message package with `Python3.11`

- Using the custom message with `rclpy` in Isaac Sim

- Overview of steps to build and use your own custom message package with `rclpy` and Isaac Sim

### Next Steps
Continue on to the next tutorial in our ROS2 Tutorials series, ROS 2 Python Custom OmniGraph Node .
