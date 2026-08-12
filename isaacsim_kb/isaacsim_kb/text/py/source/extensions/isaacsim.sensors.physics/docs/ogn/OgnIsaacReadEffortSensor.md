<!-- source: py/source/extensions/isaacsim.sensors.physics/docs/ogn/OgnIsaacReadEffortSensor.html | title: Isaac Read Effort Node — Isaac Sim -->

# Isaac Read Effort Node
Node that reads out joint effort values

## Installation
To use this node enable isaacsim.sensors.physics in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Enabled ( inputs:enabled ) | bool | True to enable sensor, False to disable the sensor | True
Exec In ( inputs:execIn ) | execution | The input execution port | None
Prim Path ( inputs:prim ) | target | Path to the joint getting measured | None
Sensor Period ( inputs:sensorPeriod ) | float | Downtime between sensor readings | 0
Use Latest Data ( inputs:useLatestData ) | bool | True to use the latest data from the physics step, False to use the data measured by the sensor | False
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Exec Out ( outputs:execOut ) | execution | Output execution triggers when sensor has data | None
Sensor Time ( outputs:sensorTime ) | float | Timestamp of the sensor reading | 0
Effort Value ( outputs:value ) | float | Effort value reading | 0.0
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.sensors.physics.IsaacReadEffortSensor
Version | 1
Extension | isaacsim.sensors.physics
Icon | ogn/icons/isaacsim.sensors.physics.IsaacReadEffortSensor.svg
Has State? | False
Implementation Language | Python
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Isaac Read Effort Node
Categories | isaacPhysicsSensor
Generated Class Name | OgnIsaacReadEffortSensorDatabase
Python Module | isaacsim.sensors.physics
[/TABLE]
