<!-- source: py/source/extensions/isaacsim.asset.gen.conveyor/docs/ogn/OgnIsaacConveyor.html | title: Conveyor Belt — Isaac Sim -->

# Conveyor Belt
Conveyor Belt

## Installation
To use this node enable isaacsim.asset.gen.conveyor in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Animate Direction ( inputs:animateDirection ) | float[2] | relative direction to apply to UV texture | [1.0, 0.0]
Animate Scale ( inputs:animateScale ) | float | how fast to scale animate texture | 1.0
Animate Texture ( inputs:animateTexture ) | bool | If configured, Animates the texture based on the conveyor velocity. may affect performance specially if multiple instances are added to a scene. | False
Conveyor Prim ( inputs:conveyorPrim ) | target | the prim reference to the conveyor | None
Curved ( inputs:curved ) | bool | If the conveyor belt is curved, check this box to apply angular velocities. The rotation origin will be the rigid body origin. | False
Delta ( inputs:delta ) | float | time since last step in seconds | 0.0
Direction ( inputs:direction ) | float[3] | relative direction to apply velocity | [1.0, 0.0, 0.0]
Enabled ( inputs:enabled ) | bool | node does not execute if disabled | True
On Step ( inputs:onStep ) | execution | step to animate textures | None
Velocity ( inputs:velocity ) | float | the velocity of the conveyor unit | 0.0
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.asset.gen.conveyor.IsaacConveyor
Version | 1
Extension | isaacsim.asset.gen.conveyor
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Conveyor Belt
Categories | isaacConveyor
__categoryDescriptions | isaacConveyor,Conveyor belt controller inside Isaac Sim
Generated Class Name | OgnIsaacConveyorDatabase
Python Module | isaacsim.asset.gen.conveyor
[/TABLE]
