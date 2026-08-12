<!-- source: action_and_event_data_generation/ext_replicator-agent/ext_isaacsim.anim.robot.html | title: Animated Robot Controller — Isaac Sim Documentation -->

# Animated Robot Controller
The `isaacsim.anim.robot` extension provides functionality for generating animated robots in Isaac Sim Replicator Agent (IRA). This extension is powered by Behavior Script , which enables reactive behavior based on USD stage events.
`isaacsim.anim.robot` generates animated robots by first simulating the robot, capturing its motion data, and then playing it back in the form of commands. Robots are simulated by `isaacsim.robot.wheeled_robots` for motions such as moving forward and turning round, which is recorded by `omni.kit.stagerecorder.core`. Then, these motion capture data are converted into commands such as `GoTo` and `Idle`.
`isaacsim.anim.robot` supports Nova Carter and `iw.hub` robots, However, custom actors can be added by setting up its `dataclass`. Refer to IRA Robot Behaviors for more information.

## Customization
Robot behavior and animation can be customized by modifying the agent `dataclass` configuration located at: `{Isaac Sim App Path}/extcache/isaacsim.anim.robot/isaacsim/anim/robot/agent/{robot type}`

## Robot Attributes
The following attributes can be configured for each robot actor:

- agent_name (str): Unique identifier for the agent

- linear_velocity (float): Forward movement speed in meters per second (m/s)

- angular_velocity (float): Turning speed in degrees per second (deg/s)

- forward_vec (list): Initial forward direction vector

- joints (list): List of USD prims that can be animated. For example, `iw.hub` uses:

```
[
"/chassis/lift",
"/chassis/left_wheel",
"/chassis/right_wheel",
"/chassis/left_swivel/left_caster",
"/chassis/right_swivel/right_caster",
"/chassis/left_swivel",
"/chassis/right_swivel"
]
```

- drive_base (str): Robot’s drive system type. Supported values: `differential`, `omni_directional`

- transitions (dict): State transition graph defining robot behavior

- animation_paths (dict): Mapping of joint names to animation file paths

- asset_path (str): Path to the robot’s USD asset file

## Customizing Animations
To create custom animations:

- Simulate the robot in Isaac Sim.

- Use `omni.kit.stagerecorder.core` to capture motion data.

- Update the `animation_paths` attribute with new animation file paths.

Animation files should be organized in state-specific folders. For example, `iw.hub`’s turn-left animation is located at: `{Isaac Sim App Path}/extcache/isaacsim.anim.robot/data/iw_hub/turn_left/`
Store each joint’s animation data in a file named after the joint.
For more information about robot behaviors, see IRA Robot Behaviors .
