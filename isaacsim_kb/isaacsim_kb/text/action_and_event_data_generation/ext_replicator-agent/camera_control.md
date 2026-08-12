<!-- source: action_and_event_data_generation/ext_replicator-agent/camera_control.html | title: Camera Control — Isaac Sim Documentation -->

# Camera Control
`Isaacsim.Replicator.Agent` (IRA) provides randomization for the cameras. By default, the cameras spawned by IRA will look at the characters in the stage. Additionally, IRA includes a camera calibration extension that provides the intrinsic and extrinsic matrices of the virtual fixed cameras in the simulation.

## Camera Placement Randomization

### Introduction
IRA can automate the camera layout adjustment progress by spawning cameras that look at the characters with certain attributes. Before setting up the simulation with IRA, you can adjust the camera randomization settings, including the camera’s heights, viewing angles, and the distances to characters.
Note

- The randomization feature can be turned off by setting `aim_camera_to_character` to `False` and the cameras will be looking at the world origin instead.

- If there are no valid positions to place the camera due to no NavMesh or occlusions, all cameras will be looking at the world origin.

### Attributes

#### Illustration

#### Attributes
`aim_camera_to_character`

- Whether to enable the randomization features. If this is set to `False`, the cameras will be looking at the World origin.

- Default Value: `True`

`character_focus_height`

- This attribute determines where the camera looks. The camera’s focus point is `character_focus_height + character_root_position`.

- Default Value (meter): `0.7`

`max_camera_distance`

- Camera’s max distance from the character that it’s looking at.

- Default Value (meter): `14`

`max_camera_focallength`

- Camera’s max focal length range.

- Default Value (meter): `23`

`max_camera_height`

- Camera’s max height value (translation’s z axis value) range.

- Default Value (meter): `3`

Note
`max_camera_height` must be lower than `max_camera_distance`.

`max_camera_look_down_angle`

- The Max angle between camera and the ground.

- Default Value (degree): `60`

`min_camera_distance`

- Camera’s minimum distance from the character that it’s looking at.

- Default Value (meter): `6.5`

`min_camera_focallength`

- Camera’s minimum focal length range.

- Default Value (meter): `13`

`min_camera_height`

- Camera’s minimum height value (translation’s z axis value) range.

- Default Value (meter): `2`

Note

- `min_camera_height` must be higher than `character_focus_height`.

- If `min_camera_height == max_camera_height`, all the cameras will be placed at the same height.

`min_camera_look_down_angle`

- The minimum angle between camera and the ground.

- Default Value (degree): `0`

Note
If `min_camera_look_down_angle == max_camera_look_down_angle`, all the cameras will be placed at the same angle.

`randomize_camera_info`

- Whether to randomize the camera’s focal length. If this is turned off, all cameras will have the same focal length.

- Default Value: `True`

### Setting Attributes
The attributes mentioned above can be set based on your simulation requirement. You can set it from the UI or using a script.

#### From the UI

- Go to Window > Extension, and search “debug settings”

- Install and enable the extension `omni.kit.debug.settings` and a Debug Setting UI window will appear.

- Search `isaacsim.replicator.agent`, then go to the “persistent” tab to find all the IRA settings.

- Adjust the camera randomization settings as you like.

#### From the Script

- Set `target_[attribute name]` to the value you want in the following script.

- Run the script from the Script Editor, which can be accessed from Window > Script Editor.

```
import carb

# activate the feature by setting aim_camera_to_character to true
my_setting = carb.settings.get_settings()

# set your target value in here
target_aim_camera_to_character = True
target_character_focus_height = 0.7
target_max_camera_distance = 14
target_min_camera_distance = 6.5
target_max_camera_focallength = 23
target_min_camera_focallength = 13
target_max_camera_height = 3
target_min_camera_height = 2
target_max_camera_look_down_angle = 60
target_min_camera_look_down_angle = 0
target_randomize_camera_info = True

# set whether to turn on the "aim_camera_to_character" randomization
aim_camera_to_character = "/persistent/exts/isaacsim.replicator.agent/aim_camera_to_character"
my_setting.set(aim_camera_to_character, target_aim_camera_to_character)

# set camera focus height
character_focus_height = "/persistent/exts/isaacsim.replicator.agent/character_focus_height"
my_setting.set(character_focus_height, target_character_focus_height)

# set max camera distance
max_camera_distance = "/persistent/exts/isaacsim.replicator.agent/max_camera_distance"
my_setting.set(max_camera_distance, target_max_camera_distance)

# set min camera distance
min_camera_distance = "/persistent/exts/isaacsim.replicator.agent/min_camera_distance"
my_setting.set(min_camera_distance, target_min_camera_distance)

# set max camera focal length
max_camera_focallength = "/persistent/exts/isaacsim.replicator.agent/max_camera_focallength"
my_setting.set(max_camera_focallength, target_max_camera_focallength)

# set min camera focal length
min_camera_focallength = "/persistent/exts/isaacsim.replicator.agent/min_camera_focallength"
my_setting.set(min_camera_focallength, target_min_camera_focallength)

# set min camera height
min_camera_height = "/persistent/exts/isaacsim.replicator.agent/min_camera_height"
my_setting.set(min_camera_height , target_min_camera_height)

# set max camera height
max_camera_height = "/persistent/exts/isaacsim.replicator.agent/max_camera_height"
my_setting.set(max_camera_height , target_max_camera_height)

# set max camera look down angle
max_camera_look_down_angle = "/persistent/exts/isaacsim.replicator.agent/max_camera_look_down_angle"
my_setting.set(max_camera_look_down_angle, target_max_camera_look_down_angle)

# set min camera look down angle
min_camera_look_down_angle = "/persistent/exts/isaacsim.replicator.agent/min_camera_look_down_angle"
my_setting.set(min_camera_look_down_angle, target_min_camera_look_down_angle)

# set whether to randomize the camera focal length
randomize_camera_info = "/persistent/exts/isaacsim/replicator.agent/randomize_camera_info"
my_setting.set(randomize_camera_info, target_randomize_camera_info)
```

## Advanced Camera Tools
There are a set of advanced camera tools to help you with camera placement and calibration by an extension called `isaacsim.sensors.rtx.placement`. For more information, refer to the RTX Sensors Placement and Calibration documentation.
