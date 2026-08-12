<!-- source: py/source/extensions/isaacsim.sensors.physics/docs/ogn/OgnIsaacReadIMU.html | title: Isaac Read IMU Node — Isaac Sim -->

# Isaac Read IMU Node
Node that reads out IMU linear acceleration, angular velocity and orientation data

## Installation
To use this node enable isaacsim.sensors.physics in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Exec In ( inputs:execIn ) | execution | The input execution port | None
IMU Prim ( inputs:imuPrim ) | target | Usd prim reference to the IMU prim | None
Read Gravity ( inputs:readGravity ) | bool | True to read gravitational acceleration in the measurement, False to ignore gravitational acceleration | True
Use Latest Data ( inputs:useLatestData ) | bool | True to use the latest data from the physics step, False to use the data measured by the sensor | False
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Angular Velocity Vector ( outputs:angVel ) | vectord[3] | Angular velocity IMU reading | [0.0, 0.0, 0.0]
Exec Out ( outputs:execOut ) | execution | Output execution triggers when sensor has data | None
Linear Acceleration Vector ( outputs:linAcc ) | vectord[3] | Linear acceleration IMU reading | [0.0, 0.0, 0.0]
Sensor Orientation Quaternion ( outputs:orientation ) | quatd[4] | Sensor orientation as quaternion | [0.0, 0.0, 0.0, 1.0]
Sensor Time ( outputs:sensorTime ) | float | Timestamp of the sensor reading | 0
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.sensors.physics.IsaacReadIMU
Version | 1
Extension | isaacsim.sensors.physics
Icon | ogn/icons/isaacsim.sensors.physics.IsaacReadIMU.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Isaac Read IMU Node
Categories | isaacPhysicsSensor
Generated Class Name | OgnIsaacReadIMUDatabase
Python Module | isaacsim.sensors.physics
[/TABLE]
