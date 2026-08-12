<!-- source: robot_simulation/articulation_controller.html | title: Articulation Controller — Isaac Sim Documentation -->

# Articulation Controller

## Overview
Articulation controller is the low level controller that controls joint position, joint velocity, and joint effort in Isaac Sim. The articulation controller can be interfaced using Python and Omnigraph.
Note
Angular units are expressed in radians while angles in USD are expressed in degrees and will be adjusted accordingly by the articulation controller.

## Python Interface

### Create the articulation controller
There are several ways to create the articulation controller. The articulation controller is usually created implicitly by applying articulation on a robot prim through the `SingleArticulation` class. However, the articulation controller can be created directly by importing the controller class before the simulation starts, but this approach will require you to create or pass in the `Articulation` during initialization.

### Initialize the controller
After the simulation is started, the robot articulation must be initialized before any commands can be passed to the robot.

### Articulation Action
Joint controls commands are packaged in `ArticulationAction` objects first, before sending them to the articulation controller. The articulation controller allows you to specify the command joint postion, velocity and effort, as well as joint indicies of the joints actuated.
If the joint indice is empty, the articulation action will assume the command will apply to all joints of the robot, and if any of the command is 0, articulation action will assume it is unactuated.
For example, the snippet below creates the command that closes the franka robot fingers: panda_finger_joint1 (7) and panda_finger_joint2 (8) to 0.0

```
1import numpy as np
2from isaacsim.core.utils.types import ArticulationAction
3
4action = ArticulationAction(joint_positions=np.array([0.0, 0.0]), joint_indices=np.array([7, 8]))
```
This snippet creates the command that moves all the robot joints to the indicated position

```
1import numpy as np
2from isaacsim.core.utils.types import ArticulationAction
3
4action = ArticulationAction(joint_positions=np.array([0.0, -1.0, 0.0, -2.2, 0.0, 2.4, 0.8, 0.04, 0.04]))
```
Important
Make sure the joint commands matches the order and the number of joint indices passed in to the articulation action. If joint indice is not passed in, make sure the command matches the number of joints in the robot.
Note
A joint can only be controlled by one control method. For example a joint cannot be controlled by both desired position and desired torque

### Apply Action
The `apply_action` function in both `SingleArticulation` and `ArticulationController` classes will apply the `ArticulationAction` you created earlier to the robot.

### Script Editor Example
You can try out basic articulation controller examples by running the following code snippets in the Script Editor. For more advanced usage, it is recommended to follow the Core API Tutorial Series .

## Omnigraph Interface
The articulation controller can also be accessed through Omnigraph nodes, providing a visual, node-based approach to robot control.

### Input Parameters
The articulation controller Omnigraph node accepts the following input parameters:

[TABLE]
Input Parameter | Description
execIn | Input execution trigger - connects to other nodes to control when the articulation controller runs
targetPrim | The prim containing the robot articulation root. Leave empty if using robotPath
robotPath | String path to the robot articulation root. Leave empty if using targetPrim
jointIndices | Array of joint indices to control. Leave empty to control all joints or use jointNames
jointNames | Array of joint names to control. Leave empty to control all joints or use jointIndices
positionCommand | Desired joint positions. Leave empty if not using position control
velocityCommand | Desired joint velocities. Leave empty if not using velocity control
effortCommand | Desired joint efforts/torques. Leave empty if not using effort control
[/TABLE]

### Usage Guidelines
Important
Parameter Validation: Ensure joint commands match the order and number of joint indices or joint names. If neither joint indices nor joint names are specified, the command must match the total number of joints in the robot.
Note
Control Method Limitation: A joint can only be controlled by one method at a time. For example, a joint cannot be controlled by both position and effort commands simultaneously.

### Example Usage
For a complete example of the articulation controller Omnigraph node in action, see the `mock_robot_rigged` asset in the Content Browser at Isaac Sim > Samples > Rigging > MockRobot > mock_robot_rigged.usd.
