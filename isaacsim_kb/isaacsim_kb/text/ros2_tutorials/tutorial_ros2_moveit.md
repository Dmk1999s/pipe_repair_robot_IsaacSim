<!-- source: ros2_tutorials/tutorial_ros2_moveit.html | title: MoveIt 2 — Isaac Sim Documentation -->

# MoveIt 2

## Learning Objectives
Run a manipulation scene in Isaac Sim with MoveIt 2.

## Getting Started
Prerequisite

- This tutorial requires `isaac_moveit`,ROS 2 packages, which are provided as part of your NVIDIA Isaac Sim download. These ROS 2 packages are located inside the appropriate `humble_ws` or `jazzy_ws`. They contain the required launch file and moveit configs. Complete ROS 2 Installation to ensure the ROS 2 workspace environment is setup correctly.

- If using multiple systems, set the `FASTRTPS_DEFAULT_PROFILES_FILE` environment variable as per instructions in ROS 2 Installation before launching Isaac Sim, as well as any terminal where ROS messages will be sent or received, and ROS2 Extension is enabled.

- Completed ROS2 Joint Control: Extension Python Scripting .

## Running MoveIt 2

- Load the environment by going to Window > Examples > Robotics Examples, and then click on the Robotics Examples tab and expand the sections on the left hand side and open the example: ROS2 > MoveIt > Franka MoveIt. Then hit Play to start simulation.

- Run the launch file to start MoveIt 2.

```
ros2 launch isaac_moveit isaac_moveit.launch.py
```

- After Rviz is launched, you can start playing with the planner. Under `Planning Group`, the `hand` option should be selected. Under `Goal State`, select `open`.
Note
On certain machines, selecting close under Goal State for hand planning group will cause the execution to fail/abort, and execute the action later with a delay or on the next execution.

- Under Commands, click Plan. The planned movement of the hand will now be visualized.

- Click Execute. The hand will start moving as planned earlier.

- To plan the movement for the arm, under `Planning Group`, select `panda_arm`. Use the displayed arrows and rotation disks to set a goal position for the robot. Alternatively you can choose to select `<random_valid>` under `Goal State`.

- Under Commands, click on Plan followed by Execute to visualize the planned motion of the arm and then move it.

## TroubleShooting
If your Rviz window is showing a black screen for where the robot should be, you can update your mesa driver. Run the following commands in a new terminal.

```
# update mesa driver
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:kisak/kisak-mesa
sudo apt install -y mesa-utils
sudo apt -y upgrade
```

## Summary
Tips for running MoveIt2’s Isaac Sim tutorial.

### Next Steps
Continue on to the next tutorial in our ROS2 Tutorials series, ROS 2 Generic Publisher and Subscriber to learn how to publish and subscribe to and from any ROS 2 topic.

### Further Learning

- Learn more about MoveIt 2 .
