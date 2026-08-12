<!-- source: py/source/extensions/isaacsim.robot.wheeled_robots/docs/ogn/OgnCheckGoal2D.html | title: Check Goal 2D — Isaac Sim -->

# Check Goal 2D
Check if wheeled robot has reached goal

## Installation
To use this node enable isaacsim.robot.wheeled_robots in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Current Orientation ( inputs:currentOrientation ) | quatd[4] | Current rotation of the robot as a quaternion (recommended to use Get Prim Local to World Transform node) | [0.0, 0.0, 0.0, 0.0]
Current Position ( inputs:currentPosition ) | vectord[3] | Current position of the robot (recommended to use Get Prim Local to World Transform node) | [0.0, 0.0, 0.0]
Exec In ( inputs:execIn ) | execution | The input execution | None
Target ( inputs:target ) | double[3] | Target position and orientation | [0, 0, 0]
Target Changed ( inputs:targetChanged ) | bool | Target position/orientation has changed | False
Thresholds ( inputs:thresholds ) | double[2] | Position and orientation thresholds at target | [0.1, 0.1]
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Exec Out ( outputs:execOut ) | execution | The output execution | None
Reached Goal ( outputs:reachedGoal ) | bool[] | Reached position and orientation goals | None
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.robot.wheeled_robots.CheckGoal2D
Version | 1
Extension | isaacsim.robot.wheeled_robots
Has State? | False
Implementation Language | Python
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Check Goal 2D
Categories | isaacWheeledRobots
__categoryDescriptions | isaacWheeledRobots,robot path planning inside Isaac Sim
Generated Class Name | OgnCheckGoal2DDatabase
Python Module | isaacsim.robot.wheeled_robots
[/TABLE]
