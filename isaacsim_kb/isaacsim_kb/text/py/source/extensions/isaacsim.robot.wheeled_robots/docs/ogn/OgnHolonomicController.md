<!-- source: py/source/extensions/isaacsim.robot.wheeled_robots/docs/ogn/OgnHolonomicController.html | title: Holonomic Controller — Isaac Sim -->

# Holonomic Controller
Holonomic Controller

## Installation
To use this node enable isaacsim.robot.wheeled_robots in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Angular Gain ( inputs:angularGain ) | double | Angular gain | 1
Exec In ( inputs:execIn ) | execution | The input execution | None
Velocity Commands for the vehicle ( inputs:inputVelocity ) | double[3] | Velocity in x and y (m/s) and rotation (rad/s) | [0.0, 0.0, 0.0]
Linear Gain ( inputs:linearGain ) | double | Linear gain | 1
Max Angular Speed ( inputs:maxAngularSpeed ) | double | Maximum angular rotation speed allowed for the vehicle in rad/s | 100000
Max Linear Speed ( inputs:maxLinearSpeed ) | double | Maximum speed allowed for the vehicle in m/s | 100000
Max Wheel Speed ( inputs:maxWheelSpeed ) | double | Maximum rotation speed allowed for the wheel joints in rad/s | 100000
Mecanum Angles ( inputs:mecanumAngles ) | double[] | Angles of the mecanum wheels with respect to wheel’s rotation axis in radians | []
Up Axis ( inputs:upAxis ) | double[3] | The rotation axis of the vehicle | [0.0, 0.0, 1.0]
Wheel Axis ( inputs:wheelAxis ) | double[3] | The rotation axis of the wheels | [1.0, 0.0, 0.0]
Wheel Orientations ( inputs:wheelOrientations ) | double[4][] | Orientation of the wheel with respect to chassis’ center of mass frame | []
Wheel Positions ( inputs:wheelPositions ) | double[3][] | Position of the wheel with respect to chassis’ center of mass in meters | []
Wheel Radius ( inputs:wheelRadius ) | double[] | An array of wheel radius in meters | []
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Joint Velocity Command ( outputs:jointVelocityCommand ) | double[] | Velocity commands for the wheels joints | None
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.robot.wheeled_robots.HolonomicController
Version | 2
Extension | isaacsim.robot.wheeled_robots
Has State? | False
Implementation Language | Python
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Holonomic Controller
Categories | isaacWheeledRobots
__categoryDescriptions | isaacWheeledRobots,robot controller inside Isaac Sim
Generated Class Name | OgnHolonomicControllerDatabase
Python Module | isaacsim.robot.wheeled_robots
[/TABLE]
