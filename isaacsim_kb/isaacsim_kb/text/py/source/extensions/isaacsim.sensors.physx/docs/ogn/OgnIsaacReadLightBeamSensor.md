<!-- source: py/source/extensions/isaacsim.sensors.physx/docs/ogn/OgnIsaacReadLightBeamSensor.html | title: Isaac Read LightBeam Sensor Node — Isaac Sim -->

# Isaac Read LightBeam Sensor Node
Node that reads out light beam sensor data

## Installation
To use this node enable isaacsim.sensors.physx in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Exec In ( inputs:execIn ) | execution | The input execution port | None
Light Beam Prim ( inputs:lightbeamPrim ) | target | Usd prim reference to the light beam prim | None
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Beam End Points ( outputs:beamEndPoints ) | pointf[3][] | Array containing end points of each beam | []
Beam Hit Data ( outputs:beamHitData ) | bool[] | Array of bools that registers if a light beam is broken | []
Beam Origins ( outputs:beamOrigins ) | pointf[3][] | Array containing origins of each beam | []
Exec Out ( outputs:execOut ) | execution | Output execution triggers when sensor has data | None
Hit Pos Data ( outputs:hitPosData ) | pointf[3][] | Array containing hit position data | []
Linear Depth Data ( outputs:linearDepthData ) | float[] | Array containing linear depth data | []
Num Rays ( outputs:numRays ) | int | The number of rays in light curtain | 0
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.sensors.physx.IsaacReadLightBeam
Version | 1
Extension | isaacsim.sensors.physx
Icon | ogn/icons/isaacsim.sensors.physx.IsaacReadLightBeam.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Isaac Read LightBeam Sensor Node
Categories | isaacPhysxSensor
Generated Class Name | OgnIsaacReadLightBeamSensorDatabase
Python Module | isaacsim.sensors.physx
[/TABLE]
