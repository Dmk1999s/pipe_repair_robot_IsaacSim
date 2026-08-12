<!-- source: action_and_event_data_generation/ext_replicator-agent/actor_control.html | title: Actor Control — Isaac Sim Documentation -->

# Actor Control
`Isaacsim.Replicator.Agent` (IRA) supports controlling two different actors:

- human characters

- autonomous mobile robots, including the Nova Carter and `iw.hub`

This section discusses supported commands for each actor, how to add custom commands, how to customize the randomization of the commands, and how to inject commands during simulation.The IRA UI provides command editors under the actor setting panel, so you can edit the commands for each actor and control the behaviors for the actors in the simulation. IRA also has the ability to randomize the commands.Additionally, the IRA UI allows you to inject commands into a running simulation to control the actors during runtime.

## Actor Behaviors
All the actors are controlled by Behavior Script , which subscribes to USD stage events and reacts to them. You can use your own Behavior Scripts to control the actors. You can run the following script from the Script Editor to change the path to behavior scripts of the actors spawned by IRA.

```
import carb
my_setting = carb.settings.get_settings()
my_character_script_path = "ENTER YOUR CHARACTER SCRIPT PATH HERE"
my_carter_script_path = "ENTER YOUR CARTER SCRIPT PATH HERE"
my_iw_hub_script_path = "ENTER YOUR IW_HUB SCRIPT PATH HERE"

character_behavior_path = "/exts/isaacsim/replicator/agent/behavior_script_settings/behavior_script_path"
nova_carter_behavior_path = "/exts/isaacsim/replicator/agent/behavior_script_settings/nova_carter_behavior_script_path"
iw_hub_behavior_path = "/exts/isaacsim/replicator/agent/behavior_script_settings/iw_hub_behavior_script_path"
my_setting.set(character_behavior_path, script_path)
my_setting.set(nova_carter_behavior_path, my_carter_script_path)
my_setting.set(iw_hub_behavior_path, my_iw_hub_script_path)
```

### Character
The Character Behavior control is based on the `Omni.Anim.People` extension. Review below for more details.The GoTo, Idle, and LookAround commands can be randomized. Characters can also Sit and Queue, but these commands require a manual input.

#### GoTo
GoTo moves the character to a location. It can be followed by a single point or a sequence of points, where the last point specifies the ending rotation that the character must have upon reaching its destination. If you would prefer to not set a rotation, you can use “_” for the ending rotation.
When a sequence of points is given, the character crosses every point. If Navmesh Navigation and Dynamic Obstacle Avoidance is on, then the character tries to avoid static and dynamic obstacles.
Example: `Character_02 GoTo 10 10 0 90`
Note

- Character rotation in a fixed spot is done by rotating the whole character body.

- Depending on the navigation mesh of the stage, characters might collide with static obstacles while walking. If this is observed, rebuild the navigation mesh with a higher agent radius.

- Character dynamic avoidance is best effort and not guaranteed. In some scenarios where static and dynamic obstacles are present together, dynamic avoidance might cause erratic movement leading characters to walk into another character or into a static obstacle.

#### Idle
Idle makes the character stand still. It takes a duration value in seconds and performs the action for that duration.
Example: `Character_02 Idle 10`

#### LookAround
LookAround makes the character stand in the same spot, while moving its head from left to right. It takes a duration value in seconds and performs the action for that duration.
Example: `Character_03 LookAround 10`

#### Sit
Sit makes the character go to a prim and attempt to sit on it. After the specified duration ends, the character stands back up. It takes a `prim_path` for the seat and a duration value in seconds and performs the action on that prim for that duration.
Example: `Character_03 Sit /World/Chair 5`
The `Sit` action plays a fixed animation, so the `seat_prim` must be scaled to fit the animation. Additionally, the `seat_prim` must contain two child `xform` prims:

- `walk_to_offset`: translation specifies the location where the character will walk to and its rotation defines the character’s final orientation before interacting with the chair.

- `interact_offset`: specifies the character’s location and rotation when the sitting animation is played. If offsets are not present, it will fallback to use seat_prim’s transform.

#### Queue
For the Queue command, you must define a queue. A queue can be defined in the command file as follows:

```
command structure:

# defines the queue
Queue Example_Queue

# Defines each spot in the queue. Structure Queue_Spot 'Queue_name' 'Spot_Index' x y z rotation
Queue_Spot Example_Queue -1 11 0 0 90

Queue_Spot Example_Queue 0 9 0 0 0

Queue_Spot Example_Queue 1 7 0 0 0

Queue_Spot Example_Queue 2 5 0 0 0
```

After defining the queue, characters can be moved to the queue using the following command structure:

```
# make the character enter the queue
Character_01 Queue Example_Queue

# action to perform when the character becomes the first in queue
Character_01 LookAround 10

# destination to go to when leaving the queue. In this example, Character_01 will go to 10, 10, 0.
Character_01 Dequeue Example_Queue 10 10 0 _
```

Note

- All three commands listed above are mandatory for the queue command to work correctly.

- When constructing a queue, each queue spot must be at least `0` meter apart from each other.

### Robot
The Robot Behavior control is based on the `isaacsim.anim.robot` extension. Review below for more details.
The GoTo and Idle commands can be randomized by IRA. The `iw.hub` robot supports the additional LiftUp and LiftDown commands, which both require manual input.

#### GoTo
The GoTo command moves the robot from its current location to a target location. The command expects the `X Y Z` world coordinate of the target location.
Example: `Nova_Carter_01 GoTo 10.02 5.9 0`

#### Idle
The Idle command makes the robot stay where it is for a given duration in seconds. It can be combined with the GoTo command to make the robot go to a position, stay there for a while, and then go to another position.
Example: `Nova_Carter_01 Idle 5`

#### LiftUp/LiftDown
The `iw.hub` robot also supports the LiftUp and LiftDown commands, which move the loader on the `iw.hub` up or down by `4 cm`.
Example: `iw_hub_02 LiftUp`

### General Command Control
You can configure general behaviors for commands created by “Generate Random Commands” in the General Command Settings panel in Tools > Action and Event Data Generation > Command Settings.
Character command settings:

- `GoTo Min Distance`: The minimal distance (in meters) between the picked location and the character’s current location for “GoTo” and “GoToBlend”. Default is `5.0`.

- `GoTo Max Distance`: The maximum distance (in meters) between the picked location and the character’s current location for “GoTo” and “GoToBlend”. Default is `20.0`.

- `Interact Object Root Path`: The root prim path to search for interactable objects for “Sit” and “TimingToObject”. This can help with faster random command generation in a complex scene. Invalid prim path will fallback to searching from scene root prim. Default is “False”.

Robot command settings:

- `GoTo Min Distance`: The minimal distance (in meters) between the picked location and the robot’s current location for “GoTo” and “GoToBlend”. Default is `5.0`.

- `GoTo Max Distance`: The maximum distance (in meters) between the picked location and the robot’s current location for “GoTo” and “GoToBlend”. Default is `20.0`.

## Custom Commands and Randomization
IRA supports adding animation USDs as custom commands using `custom_command_tracking.json`. You can further define the randomization rules for “Generate Random Commands” using `character_command_transition_map.json`.

### Custom Command Tracking File
IRA uses `custom_command_tracking.json` to track all registered external animations by their asset paths as custom command types.
By default, IRA loads from `[omni.anim.people]/data/custom_command_tracking.json`. You can modify the file directly in text editor or using the Custom Command Panel in Tools > Action and Event Data Generation > Command Settings.
You can also load another JSON file as long as it follows below structure:

```
{
"animations": ["anim_01.usd", "anim_02.usd"]
}
```
For animations USDs in the loaded `custom_command_tracking.json`, IRA will create animation graph nodes to `Biped_Setup` every time when clicking Set Up Simulation.
A valid animations USD to add needs to satisfy:

- Animation is retargeted to the `Biped_Setup`. `Biped_Setup` can play it as expected.

- Root prim is the `SkelAnimation`.

- Root prim has below required custom USD attributes:

- `CustomCo`mmandName` The name of the custom command. Data type is string.

- `CustomCommandTemplate` The command template used to register this animation. Data type is string.

For `CustomCommandTemplate`, there are three options:

- `Timing` Plays the animation for a given time. The command structure is the same as `Idle` command.

- `TimingToObject` Walks the character to an object and plays animation. The command structure is the same as `Sit` command.

- `GoToBlend` Blends the animation into current walking animations. The command structure is the same as `GoTo` command.

Below are attributes that overwrite values to the generated animation graph nodes.

- `CustomCommandAnimStartTime` Corresponding to Start Time in AnimationClip. Data type is float. Default value is 0.

- `CustomCommandAnimEndTime` Corresponding to Start Time in AnimationClip. Data type is float. Default value is 0.

- `CustomCommandAnimLoop` Corresponding to Loop in AnimationClip. Data type is bool. Default value is True.

- `CustomCommandAnimBackwards` Corresponding to Backwards in AnimationClip. Data type is bool. Default value is False.

- `CustomCommandFilterJoint` The joint to filter animation into the walk animations. Data type is string. Default value is None. Only being used in “GoToBlend”.

Refer to the set attribute guide for how to add and set USD attributes in Omniverse.

#### Example Usage

- Open `[Isaac Sim Asset Path]/Isaac/People/Animations/push_button.skelanim.usd`, add USD attributes as follows.

- Go to the Custom Command Panel, click Add and select the animation USD in step 1. IRA will now recognize this new command by CustomCommandName.

- After clicking Set Up Simulation in the AgentSDG Window, new animation graph nodes will be added to `Biped_Setup` and characters will perform the new command in Command Textbox.

Note
The following animation assets have been configured as custom commands. You can directly load them for testing.

- `[Isaac Sim Asset Path]/Isaac/People/Animations/push_button.skelanim.usd`

- `[Isaac Sim Asset Path]/Isaac/People/Animations/type_keyboard.skelanim.usd`

### Command Transition Map
IRA command randomization rule is defined by `character_command_transition_map.json`. It holds key-value pairs in which key is the command name and value defines how to randomize it.
By default, IRA loads from `[isaacsim.replicator.agent]/data/character_command_transition_map.json`.
You can modify the file directly in text editor or using the Command Randomization Panel in Tools > Action and Event Data Generation > Command Settings.
You can also load another JSON file as long as it follows below file structure:

```
{
"GoTo": {
"weight": 1.0,
"transitions": {
"Idle": 5.0,
"LookAround": 5.0
}
},
"Idle": {
"weight": 1.0,
"transitions": {
"GoTo": 6.0,
"LookAround": 4.0
}
},
"LookAround": {
"weight": 1.0,
"transitions": {
"GoTo": 7.0,
"Idle": 3.0
}
},
"Sit": {
"weight": 0.0,
"transitions": {}
}
}
```
In the above example, `GoTo`, `Idle`, `LookAround` and `Sit` will be used in command random generation.
weight define their chance to be picked as the first generated command, so there will be 1/3 chance that a character’s first command is `GoTo`, `Idle` or `LookAround` while `Sit` has `0` chance.
transitions define what would be the next generated command after this command, so `GoTo` has equal chances to be either followed by `Idle` or `LookAround`.
Commands themselves define how they want to be randomized each time. For built-in commands:

- `Idle` Random duration ranges from 2 to 6 seconds.

- `LookAround` Random duration ranges from 2 to 4 seconds.

- `GoTo` Randomly pick location away from 5 to 20 meters by default. You can also config it in General Command Settings Panel in Command Settings Window.

- `Sit` Randomly pick interactable object with `{class:Sittable}` semantic labels. Random duration ranges from 4 to 8 seconds.

For custom commands, extra USD attributes are needed:

- `Timing`

- Needs `CustomCommandRandomMinTime` and `CustomCommandRandomMaxTime` to define random duration bound. Both data types are float.

- `TimingToObject`

- Needs `CustomCommandRandomMinTime` and `CustomCommandRandomMaxTime` like `Timing`.

- Needs `CustomCommandInteractObjectFilter` to define randomly picking interactable objects with semantic label of `{class:CustomCommandInteractObjectFilter}`. Data type is string.

- `GoToBlend`

- Uses the same setting as `GoTo`. No need for extra setups.

Note

- It is not required to list all available commands in command transition map.

- Commands needs to be built-in commands or custom commands that list in the `custom_command_tracking.json`.

## Command Injection
IRA allows you to inject commands into a running simulation to control the agents in real time. This enables you to adjust the simulation during runtime to create emergent events or simulate a particular scenario.
To enable the Command Injection UI window:

- Click Tools on the menu bar.

- Click Replicator and Command Injection.

Command injection works similar to regular commands. The format is `agent_name command params` and there is one panel for all the agents. This feature only works while the simulation is running.
To inject commands:

- Type the commands in the Command Injection UI textbox.

- Click the Inject button.

When a command is injected, the agent stops whatever command it is currently executing and starts the injected command immediately.
Note

- If a character is performing the Sit command and a new command is injected, the character stands up first and then executes the injected command.

- Command injection only works with controlling the agents individually. Global command like Queue will not work.

Below is an image of the command injection UI. When clicking the Inject button, `Character_01` will stop whatever it’s doing and execute the `GoTo` the world coordinate `(1, 1, 0)`. Similarly, Nova_Carter_02 will stop whatever it’s doing and `Idle` for `10 seconds`.

## Actor Response and Triggers
A `Response` is a pre-defined behavior to be activated by `Trigger` and it picks actor (characters and robots) to perform during play. Each response can only have one trigger. Each actor can have multiple responses.
Response is applied to scene by its order in the config file. If multiple responses are set to be trigger at the same time, responses early in the list will be triggered first.
Once triggered, a response is assigned by priority (higher number represents higher priority). IRA will pick actors that have no response or are running lower-priority responses. In latter case, actors will push unfinished responses into queue and start executing the new response. A lower-priority response will not pick actors that are running higher-priority responses.
`CommandResponse` is the only implementation of `Response` because IRA actors are mostly controlled by commands. Config file format:

```
CommandResponse:
name: [str_value]
priority: [int_value]
pick_agent: [enum_value]
resume: [bool_value]
position: (x,y,z)
trigger: [trigger_dict]
commands: [list_of_commands]
```
One example of a response to have all actors in the scene perform a LookAround command for `10 seconds` at `5 seconds` after play:

```
CommandResponse:
name: "MyCommandResponse"
priority: 1
pick_agent: all
resume: True
position: (0, 0, 0)
trigger:
type: time
time: 5.0
commands:
- LookAround 10
```

- `name`: The name of the response instance. Each response instance should have an unique name.

- `priority`: The execution priority of the response.

- `pick_agent`: The rule to pick actors for executing the response. All rules:

- `first_available`: Pick the first available actor in the scene (by stage hierarchy). Available means the actor does not have any response or have a lower-priority response.

- `all`: Pick all available actors in the scene.

- `nearest`: Pick the nearest available actor by the response position parameter (not by the actor initial position).

- `furthest`: Pick the furthest available actor by the response position parameter (not by the actor initial position).

- `resume`: If picked agents resume to its rest commands, then they finish the response.

- `position`: The response position. Used in picking actors by distance.

- `trigger`: The trigger to start the response.

- `commands`: The commands to be executed when the response happens. Because actors are picked during play, commands must not include the actor names.

Note
Multi-Type Actors: both characters and robots can be picked by same response while some of their supported commands are in different formats (for example, GoTo command format differs). Ensure that you use commands they both support and are in same format in those scenarios (for example, Idle). This is a limitation.
There are three types of `Trigger` available:

```
# Time Trigger
trigger:
type: time
time: [float_value_of_time_in_seconds]

# Carb Event Trigger
trigger:
type: carb_event
event_name: [carb_event_str]

# Incident Trigger
trigger:
type: incident
incident_name: [incident_name_str]
```

- `Time Trigger`: Trigger by timeline. The parameter is the time value in seconds.

- `Carb Event Trigger`: Trigger by a Carb Event . The parameter is the Carb event name.

- `Incident Trigger`: Trigger by an incident set up by isaacsim.replicator.incident . The parameter is the incident instance name.
