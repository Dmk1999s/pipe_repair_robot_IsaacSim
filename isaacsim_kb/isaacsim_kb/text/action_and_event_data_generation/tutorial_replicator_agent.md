<!-- source: action_and_event_data_generation/tutorial_replicator_agent.html | title: Actor Simulation and Synthetic Data Generation — Isaac Sim Documentation -->

# Actor Simulation and Synthetic Data Generation
Detecting and tracking people in various environments offers a tremendous amount of value in many industries. Retail stores benefit from understanding customer traffic and customer trip patterns. The intelligence is used to influence the design of higher revenue driven floor plans, to run more detailed and frequent promotion events, and to improve customer shopping experience. Manufacturers and warehouse operators can use the generated data to optimize the interior layout and improve the throughput from the quantitative understanding of worker’s operation routines and potential workflow bottlenecks. As human and robot collaboration in the same space becomes common, ensuring workspace safety and efficiency, at the same time, is challenging. Typically, collecting real world data to train people detection and tracking models for different environments is costly and not scalable.
Synthetic data generation provides the flexibility and scalability to solve these exigent data problems. Also, evaluating model accuracy and robustness under abnormal or long-tail situations is critical, before the models are deployed in the real-world.
For example, when designing an airport, a warehouse, a factory, a shopping mall, a school campus, or residential home, you can simulate people and robots in that design to identify necessary changes before beginning to build it. The simulation can also be used to test normal and rare conditions, to offer unparalleled values in safety, efficiency, and eventually improving earnings.
The `Isaacsim.Replicator.Agent` (IRA) extension is designed to generate synthetic data on human characters and robots across a variety of 3D environments. It provides controls over the 3D environments, camera parameters, characters, and robot motions through the use of the configuration and command files. The extension includes a comprehensive set of 2D and 3D data annotation methods to support multiple modalities of sensors. For example, RGB camera, and stereo camera sensors. Its primary objective is to provide a GPU-accelerated, computational solution to the synthetic data acquisition problem in computer vision Deep Learning model training and software-in-the-loop testing tasks. In IRA, human characters and robots are classified by the term agent or actor. Prior to IRA, there was no integrated and easy-to-use application or extension in Omniverse to facilitate the synthetic data generation on human characters in various spaces.
IRA provides the following templates for how to customize a simulation with new environments, new characters, and new animations:

- Simplified initial setup and low learning curve: the extension is included in Isaac Sim. It provides a graphical user interface and scripting interface to facilitate both interactive development and scalable headless data production.

- High data quality and realism: leveraging Omniverse high quality sim-ready assets, flexible human animation backend, precision-built robot physics engine, and optimized Omniverse rendering engine, IRA produces ever-improving realistic imagery and 100% accurate annotations, to formulate high quality data, which is essential to efficiently training AI models.

- Integration and compatibility: IRA is a Kit extension in Omniverse. It leverages `omni.anim.graph`, `omni.anim.navigation`, and `omni.replicator.core`. Its design ensures the compatibility of IRA with the rest of the Omniverse ecosystem.

Prior to enabling this extension, read What Is Isaac Sim? to learn about Isaac Sim and follow Installation to install Isaac Sim.

Note
`Isaacsim.Replicator.Agent` is in beta. For more information on pre-release and beta terms, refer to the Omniverse License Agreement .

## Enable Isaacsim.Replicator.Agent

- Follow the Omniverse Extension Manager guide to enable the `isaacsim.replicator.agent.core` and `isaacsim.replicator.agent.ui` extensions.

- The extension fetches sample assets from Isaac Sim Assets during start. Refer to Isaac Sim Assets if you encounter issues for loading assets.

- If loading the UI appears to be hanging, try starting Isaac Sim with the flag `--/persistent/isaac/asset_root/timeout=1.0`.

- The IRA UI panel is accessible by Tools > Action and Event Data Generation > Actor SDG and it opens on the right side of the screen.

Note

- To have the extension auto-loaded on startup, check the autoload checkbox in the extension manager.

- Because of extension dependencies, a restart of the Isaac Sim app might be required.

## Getting Started
To launch data generation with IRA, load the a YAML configuration file. Or use the default configuration file that comes with the extension and follow the steps below. For a more detailed walkthrough, refer to the Data Generation section.

- Enable the IRA extension and open the UI panel.

- Load the configuration file or use the default configuration file.

- A default config file is provided in `[Isaac Sim App Path]/extscache/isaacsim.replicator.agent.core-[current-version]/config/default_config.yaml`, which comes with the core extension and is automatically loaded when the extension starts.

- Click the Set Up Simulation button from the top of the UI and it will start loading simulation assets, which can take a while.

- Click the Generate Random Commands button from the Character panel to create commands.

- Click the button with the disk icon in the Character panel to save commands in the previous step.

- Click the Start Data Generation button from the top of the UI and the simulation and data generation will start. It can take a while to finish.

- Simulation lasts according to the Simulation Length field in the SDG Setup panel.

- The output data can be found from the Output Directory according to the Replicator panel.

## Configuration File
Configuration contains the essential data that defines a simulation. Understanding what each section and row in the configuration file represents helps you understand what IRA can offer. The config file has the following sections:

- global

- scene

- sensor

- character

- robot

- response

- incident

- replicator

The structure of the configuration file is fixed, but the order of each property and section can vary. For example `seed` can be below the `simulation_length`. Properties not listed in the format are ignored by our extension.
Some sections are optional, meaning the configuration file is still valid without their presence, and default values for these sections will not be added unless sections are present.
The following is an example configuration file:

```
isaacsim.replicator.agent:
version: 0.7.1
global:
seed: 123456
simulation_length: 300
scene:
asset_path: [Isaac Sim Assets Path]/Isaac/Environments/Simple_Warehouse/full_warehouse.usd
sensor:
camera_num: 5
character: # Optional
asset_path: [Isaac Sim Assets Path]/Isaac/People/Characters/
command_file: default_command.txt
filters:
- "male"
- "medical"
num: 10
spawn_area:
- "Walkable"
navigation_area:
- "Walkable"
robot: # Optional
command_file: default_robot_command.txt
nova_carter_num: 0
iw_hub: 0
write_data: false
response: # Optional
response_list: []
incident: # Optional
incident_list: []
replicator:
writer: IRABasicWriter
parameters:
output_dir:
rgb: true
object_info_bounding_box_2d_tight: true
object_info_bounding_box_2d_loose: true
object_info_bounding_box_3d: true
```
Note
`[Isaac Sim Assets Path]` is the path to Isaac Sim Assets .Refer to Isaac Sim Assets Check for how to verify the assets access and how to retrieve the asset path.

### Global Properties
seedThe random seed that is used in all the randomization features. The same seed guarantees the reproducibility of the same output. If the seed section is left empty, the current system time is used as the seed.
simulation_lengthThis specifies the simulation length in the number of frames and thus determines the amount of data to be captured. It assumes that the simulation runs at 30 frames per second (FPS). For example, if `simulation_length` is set to 300 frames, then `10` seconds of data is generated per camera. It also determines the duration of commands for the actors, which are generated after clicking Generate Random Command in the Character Settings panel or the Robot Settings panel. The commands guarantee that actors move for at least `simulation_length` seconds.

### Scene Properties
asset_pathThe path to the scene environment USD. It must contain the environment of the simulation, but it can also contain some characters and cameras used for data generation. If you like the randomized result for a certain scene, it can be saved as USD and be reused again by providing its path to this field.

### Sensor Properties
camera_numThe number of cameras to be captured for data. If `camera_num (n)` is greater than the number of cameras in the stage, only the cameras in the stage and under `/World/Cameras` are used for generating data. If `camera_num (n)` is smaller than the number of cameras in the stage, only the first `n` cameras in the stage are used for generating data. If `camera_num` is `-1`, IRA uses all the existing cameras in the USD under `/World/Cameras`.When clicking Set Up Simulation in the UI, IRA spawns more cameras to make sure that enough cameras are present in the stage. If the `camera_num` value of cameras for the stage under `/World/Cameras` with the naming convention Camera, Camera_01, Camera_02, …, is reached or exceeded, no additional cameras are added.To learn more about simulating cameras in Omniverse, refer to Cameras .camera_listThe list of cameras (prim paths) for data generation. You can toggle in the UI to switch from camera_num to camera_list. In this case, IRA assumes cameras are already in the scene and Setup Simulation will not create new cameras.
Note

- The number of cameras for a data generation job is bounded by the VRAM of the system. If you encounter error messages like `Cannot create cuda external memory for resource`, try to reduce `camera_num`.

- The complexity of a scene impacts the file descriptor resources. This could limit the number of cameras for a data generation job as well. If you encounter error messages like `dup failed for resourceType` and `Too many open files`, try increasing the amount of file descriptors that individual users can consume. For example, `HARD_LIMIT=`ulimit -Hn`; ulimit -Sn $HARD_LIMIT` increases your open file descriptor limit to the highest value allowed by the OS.

- `camera_num` and `camera_list` are mutually exclusive. You can toggle the Camera Property Type in the UI to choose between number and list.

### Character Properties
numThe number of the characters for the simulation. When clicking Set Up Simulation in the UI, IRA spawns more characters to make sure that enough characters are present on the stage. If the `num` value of characters for the stage is reached or exceeded, no additional characters are added.
asset_pathThe path to the character asset folder. It must be a directory that stores the USD files for the character assets. Sub-directory and custom assets are allowed.
command_fileThe path to the command file that controls the behavior of the characters. It must be a `.txt` file where each line starts with the name of the character and is followed by the name of the command and the parameters for this command.
filtersA list of labels separated by `,`. This filters the characters to be spawned from the given asset path. It is a map of a filter label and the list of characters that belong to this label. Filters must be stored as a JSON file named `filter.json` and it must be under the root directory of the asset path folder. When using the UI, you can hover the mouse on the filter label, which shows the currently available labels for this asset folder. Refer to `[Isaac Sim Assets Path]/Isaac/People/Characters/filter.json` for an example filter file.
spawn_areaA list of navmesh areas where character agents will be spawned at. If nothing is set, characters will be spawned uniform across all areas. The navmesh areas are defined in the navmesh property panel. Refer to Building the NavMesh for more information on how to setup navmesh areas.
navigation_areaA list of navmesh areas where characters can GoTo . If nothing is set, characters can GoTo all areas. The navmesh areas are defined in the navmesh property panel. Refer to Building the NavMesh for more information on how to setup navmesh areas.
Note
If `spawn_area` and `navigation_area` are different, the first command of the character will be to go to the `navigation_area`.

### Robot Properties
nova_carter_numThe number of Nova Carter robots for the simulation. When clicking Set Up Simulation in the UI, IRA spawns more Nova Carter robots to make sure that enough of them are present on the stage. If `nova_carter_num` value of Nova Carter robots for the stage under `/World/Robots` with the naming convention Nova_Carter, Nova_Carter_01, Nova_Carter_02, …, is reached or exceeded, no additional Nova Carter robots are added.
iw_hub_numThe number of `iw.hub` robots for the simulation. When clicking Set Up Simulation in the UI, IRA spawns more `iw.hub` robots to make sure that enough of them are present on the stage. If `iw_hub_num` value of `iw.hub` robots for the stage under `/World/Robots` with the naming convention iw_hub, iw_hub_01, iw_hub_02, …, is reached or exceeded, no additional `iw.hub` robots are added.
command_fileThe path to the command file that controls the behavior of the robots. It must be a `.txt` file where each line starts with the stage name of the robot and is followed by the name of the command and the parameters for this command.
write_dataA Boolean value that determines whether to write the camera output data for the robots. If this is set to `true`, IRA outputs the data for the first two cameras on each robot. If this is set to `false`, the robots are still controlled according to the command file, but their cameras won’t write any data.
Note
Enabling `write_data` increases the number of cameras to be written. If the VRAM is running out, reduce the number of the cameras in stage.
spawn_areaA list of navmesh areas where robots will be spawned at. If nothing is set, robots will be spawned uniform across all areas. The navmesh areas are defined in the navmesh property panel. Refer to Building the NavMesh for more information on how to setup navmesh areas.
navigation_areaA list of navmesh areas where robots can GoTo . If nothing is set, robots can GoTo all areas. The navmesh areas are defined in the navmesh property panel. Refer to Building the NavMesh for more information on how to setup navmesh areas.
Note
If `spawn_area` and `navigation_area` are different, the first command of the robot will be to go to the `navigation_area`.

### Actor Response Properties
response_listA list of responses for IRA actors to be executed.
Note
Refer to Actor Response and Triggers for details.

### Incident Properties
incident_listA list of the incidents to happen.
Note
It is the same structure as the incident section in the config file of `isaacsim.replicator.incident`. Refer to Actor Response and Triggers for details.

### Replicator Properties
writerThe writer that Replicator uses when generating data. For the writers provided by IRA, they are registered to Replicator at the start. For other writers, it is up to you to register them before usage.
parametersParameters for the writer’s initialize function. The names of each parameter must be the same as the input argument of the initialize function.

### Minimum Configuration File
The minimum data required for the configuration file is the header of the extension `isaacsim.replicator.agent` and the version of the extension. Other fields have default values, if they are not specified explicitly, the default values are generated automatically.
The version in the config file must match the minor version of the current extension. For example, 0.1.12 works with 0.1.11 but 0.0.12 won’t work with 0.1.12. Refer to Semantic Versioning for the version convention.
A default config file is provided in `[Isaac Sim App Path]/extscache/isaacsim.replicator.agent.core-[current-version]/config/default_config.yaml`, which comes with the core extension and is automatically loaded when the extension starts. When no command file is specified in the config file, the `default_command.txt` and `default_robot_command.txt` are created at the system default location and its path is added to the config file.
The following is an example of the minimum config file:

```
isaacsim.replicator.agent:
version: 0.7.1
```

## Simulation Control
To further understand how to control the simulation result, review:

## Data Generation

### Data Generation from UI
The IRA UI provides control for all the attributes of the simulation and data generation configuration. The attributes provide you with fine grain control over the simulation result. The following steps launch the data generation with simulation configurations:

- Enable the IRA extension to open the Actor SDG window.

- A default config file is provided in `[Isaac Sim App Path]/extscache/isaacsim.replicator.agent.core-[current-version]/config/default_config.yaml`, which comes with the core extension and is automatically loaded when the extension starts.

- To load a different configuration file, click the folder icon next to the Config File Path text field in the Global Settings panel or directly enter the path to the config file in the Config File Path textfield.

- Modify other simulation properties in the UI. All the fields in the configuration file can be directly edited through the UI. All the UI fields have their respective fields in the configuration file. Refer to the Configuration File to review what each field means.

- When changes in the UI are made, the “*” symbol appears on the Save File button. Changes are not written to the config file until the Save File button is clicked. Unsaved changes will be shown in blue in the UI, whereas invalid input will be shown in red.

- When there are unsaved changes, Set Up Simulation and Start Data Generation buttons run according to the information displayed in the UI rather than from the configuration file on disk.

- Assets (scene, characters, cameras) are not loaded until the Set Up Simulation button is clicked.

- Extension will spawn characters and cameras to ensure enough characters and cameras are present in the scene based on the configuration file.

- If there are enough characters or cameras in the scene already, the extension does not remove any assets and it uses the first N cameras for the data output, where N is the requested camera number from the config file.

- Click the Set Up Simulation button to load the simulation assets and wait the loading to finish. Loading can take a while, depending on the complexity of the assets.
Note

- Before setting up the simulation, IRA requires a NavMesh in the stage to spawn actors and control them correctly. Learn how to create your NavMesh from Navigation Mesh .

- You can also go to Window > Navigation > NavMesh and turn off Auto-Bake in the NavMesh settings. Turning it off can increase the performance.

- Modify the actor (character, robot) commands as you want. Refer to Actor Control for how to control the actor behaviors.

- A Generate Random Commands button is provided to generate random commands for actors in the scene. When you click Save Commands, it overwrites the existing commands in the command file.

- When commands are modified, the disk icon in the Character and Robot panels will be highlighted in blue to indicate that the commands have been modified and are unsaved.

- Commands must be saved in order to take effects.

- IRA provide a command editor for each actor. You can select the actor name on the tab and use the text editor to edit the command for it.

- [Optional] Click the Save or Save As button from the top UI panel, if you want the configuration for this simulation to be saved.

- When clicking Save for the configuration file, it also triggers the saving of command files.

- After the assets have been loaded and modified, and the command files have been generated and saved, press the Start Data Generation button from the top UI panel to start the simulation and data generation.

- The simulation automatically stops when enough data has been generated to cover `simulation_length`.

- To end the data generation early, click Stop Data Generation from the top UI panel.

Note
After clicking Stop Data Generation, Replicator may take some time to fully stop. Immediately clicking Start Data Generation again may cause the program to get stuck. Wait until stopping completes before starting again.

- The output data can be found from the Output Directory according to the Replicator panel.

### Data Generation from Script
For large-scale data generation, it can be more efficient to launch it from script. IRA provides an automatic script (`sdg_scheduler.py`) to run offline data generation. To run from script, open a terminal from where Isaac Sim is installed and run the following commands.

- For Linux:
`./python.sh tools/actor_sdg/sdg_scheduler.py -c [config file path]`

- For Windows:
`.\python.bat tools\actor_sdg\sdg_scheduler.py -c [config file path]`

Note

- `[config file path]` is the path to the IRA configuration file.

- You must use the `python.sh` or `python.bat` bundled with Isaac Sim to run the script.

- An example config file is also provided in the `/tools/actor_sdg` folder. For a sample Linux run, execute: `./python.sh tools/actor_sdg/sdg_scheduler.py -c tools/actor_sdg/default_config.yaml`

- `sdg_scheduler` also supports a `--save_usd` flag, which will write out the USD file after “Set Up Simulation” to the output directory. This is useful for recovering the agent and sensor positions

## Customization

## Terminology
Isaacsim.Replicator.Agent.CoreThe core extension that manages the simulation state. It contains the essential API and modules for setting up the simulation and capturing the synthetic data. Its modules can be called independently.
Isaacsim.Replicator.Agent.UIThe UI extension for IRA. When this extension loads, the core extension is loaded automatically. This extension contains the UI components for easy interaction with the extension.
Configuration FileA `.yaml` file that contains configuration data that defines the key components of a simulation, including the randomization seed, duration of the simulation, number of the actors, and output format. To use the extension, you must load a configuration file or use the UI to generate a YAML file first.
Command FileA `.txt` file that contains commands for the agents. The actors (characters, robots) perform actions based on the given commands. The extension controls the actors through the `omni.anim.people` and `isaacsim.anim.robot` extensions. Different agents have different command files.
ActorActors are controlled by the respective command files and perform actions in the simulation. The extension supports human characters and robots (Nova Carter, iw.hub) as actors. We use both “actor” and “agent” interchangeably in this documentation.
SeedRandomization seed. Given the same seed, the extension can generate the same randomized result for camera and agent location and agent behaviors. With the same seed and the same sequence of operations, the same data is guaranteed to be generated.
Replicator (Omni.Replicator.Core)The data capturing extension that our extension is based on. More information about the Replicator extension can be found in Replicator Official Documentation .
