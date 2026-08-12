<!-- source: py/source/extensions/isaacsim.robot.wheeled_robots/docs/ogn/OgnHolonomicRobotUsdSetup.html | title: Usd Setup Holonomic Robot — Isaac Sim -->

# Usd Setup Holonomic Robot
setup any robot to be ready to be used by the holonomic controller by extract attributes from USD

## Installation
To use this node enable isaacsim.robot.wheeled_robots in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Com Prim ( inputs:comPrim ) | target | prim for the center of mass xform | None
Com Prim Path ( inputs:comPrimPath ) | token | prim path to the robot’s center of mass xform |
Robot Prim ( inputs:robotPrim ) | target | prim for the robot’s articulation root | None
Robot Prim Path ( inputs:robotPrimPath ) | token | prim path to the robot’s articulation root link when usdPath is true |
Use Path ( inputs:usePath ) | bool | use prim path instead of prim target | False
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Mecanum Angles ( outputs:mecanumAngles ) | double[] | angles of the mechanum wheels with respect to wheel’s rotation axis | None
Up Axis ( outputs:upAxis ) | double[3] | the rotation axis of the vehicle | None
Wheel Axis ( outputs:wheelAxis ) | double[3] | the rotation axis of the wheels, assuming all wheels have the same | None
Wheel Dof Names ( outputs:wheelDofNames ) | token[] | name of the left wheel joint | None
Wheel Orientations ( outputs:wheelOrientations ) | double[4][] | orientation of the wheel with respect to chassis’ center of mass frame | None
Wheel Positions ( outputs:wheelPositions ) | double[3][] | position of the wheel with respect to chassis’ center of mass | None
Wheel Radius ( outputs:wheelRadius ) | double[] | an array of wheel radius | None
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.robot.wheeled_robots.HolonomicRobotUsdSetup
Version | 1
Extension | isaacsim.robot.wheeled_robots
Has State? | False
Implementation Language | Python
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Usd Setup Holonomic Robot
Categories | isaacWheeledRobots
__categoryDescriptions | isaacWheeledRobots,robot controller prep inside Isaac Sim
Generated Class Name | OgnHolonomicRobotUsdSetupDatabase
Python Module | isaacsim.robot.wheeled_robots
[/TABLE]
