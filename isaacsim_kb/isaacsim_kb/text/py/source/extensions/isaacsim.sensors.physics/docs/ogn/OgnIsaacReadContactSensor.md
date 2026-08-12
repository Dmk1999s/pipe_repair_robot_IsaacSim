<!-- source: py/source/extensions/isaacsim.sensors.physics/docs/ogn/OgnIsaacReadContactSensor.html | title: Isaac Read Contact Sensor Node — Isaac Sim -->

# Isaac Read Contact Sensor Node
Node that reads out contact sensor data

## Installation
To use this node enable isaacsim.sensors.physics in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Contact Sensor Prim ( inputs:csPrim ) | target | USD prim reference to contact sensor prim | None
Exec In ( inputs:execIn ) | execution | The input execution port | None
Use Latest Data ( inputs:useLatestData ) | bool | True to use the latest data from the physics step, False to use the data measured by the sensor | False
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Exec Out ( outputs:execOut ) | execution | Output execution triggers when sensor has data | None
In Contact ( outputs:inContact ) | bool | Bool that registers current sensor contact | False
Sensor Time ( outputs:sensorTime ) | float | Sensor reading timestamp | 0.0
Force Value ( outputs:value ) | float | Contact force value reading (N) | 0.0
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.sensors.physics.IsaacReadContactSensor
Version | 1
Extension | isaacsim.sensors.physics
Icon | ogn/icons/isaacsim.sensors.physics.IsaacReadContactSensor.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Isaac Read Contact Sensor Node
Categories | isaacPhysicsSensor
Generated Class Name | OgnIsaacReadContactSensorDatabase
Python Module | isaacsim.sensors.physics
[/TABLE]
