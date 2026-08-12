<!-- source: py/source/extensions/isaacsim.robot.wheeled_robots/docs/ogn/OgnAckermann.html | title: Ackermann Steering — Isaac Sim -->

# Ackermann Steering
NOTE: DEPRECATED as of Isaac Sim 4.1.0 in favour of OgnAckermannController Ackermann Steering Geometry

## Installation
To use this node enable isaacsim.robot.wheeled_robots in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
DT ( inputs:DT ) | double | Delta time for the simulation step | 0.0
Acceleration ( inputs:acceleration ) | double | Desired forward acceleration for the robot in m/s^2 | 0.0
Current Linear Velocity ( inputs:currentLinearVelocity ) | vectord[3] | Current linear velocity of the robot in m/s | [0.0, 0.0, 0.0]
Exec In ( inputs:execIn ) | execution | The input execution | None
Invert Steering Angle ( inputs:invertSteeringAngle ) | bool | Flips the sign of the steering angle, Set to true for rear wheel steering | False
Max Wheel Rotation ( inputs:maxWheelRotation ) | double | Maximum angle of rotation for the front wheels in radians | 0.0
Max Wheel Velocity ( inputs:maxWheelVelocity ) | double | Maximum angular velocity of the robot wheel in rad/s | 0.0
Speed ( inputs:speed ) | double | Desired forward speed in m/s | 0.0
Steering Angle ( inputs:steeringAngle ) | double | Desired virtual angle in radians. Corresponds to the yaw of a virtual wheel located at the center of the front axle. By default it is positive for turning left and negative for turning right for front wheel drive. | 0.0
Track Width ( inputs:trackWidth ) | double | Distance between the left and right rear wheels of the robot in meters | 0.0
Turning Wheel Radius ( inputs:turningWheelRadius ) | double | Radius of the front wheels of the robot in meters | 0.0
Use Acceleration ( inputs:useAcceleration ) | bool | Use acceleration as an input, Set to false to use speed as input instead | True
Wheel Base ( inputs:wheelBase ) | double | Distance between the front and rear axles of the robot in meters | 0.0
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Exec Out ( outputs:execOut ) | execution | The output execution | None
Left Wheel Angle ( outputs:leftWheelAngle ) | double | Angle for the left turning wheel in radians | None
Right Wheel Angle ( outputs:rightWheelAngle ) | double | Angle for the right turning wheel in radians | None
Wheel Rotation Velocity ( outputs:wheelRotationVelocity ) | double | Angular velocity for the turning wheels in rad/s | None
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.robot.wheeled_robots.AckermannSteering
Version | 1
Extension | isaacsim.robot.wheeled_robots
Has State? | False
Implementation Language | Python
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Ackermann Steering
hidden | true
Categories | isaacWheeledRobots
__categoryDescriptions | isaacWheeledRobots,Ackermann steering for robots in Isaac Sim
Generated Class Name | OgnAckermannDatabase
Python Module | isaacsim.robot.wheeled_robots
[/TABLE]
