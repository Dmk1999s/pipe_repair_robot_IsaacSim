<!-- source: py/index.html | title: Isaac Sim: Extensions API — Isaac Sim -->

# Isaac Sim: Extensions API

## API Reference

- C++ API

- Python API reference can be found on the individual pages of each extension.

## Extensions

### Extensions (App)

[TABLE]
Extension | Title | Description
isaacsim.app.about | Isaac Sim About Window | Show application/build information.
isaacsim.app.selector | Isaac Sim App Selector | Mini Launch Pad app for Isaac Sim Sub Apps
isaacsim.app.setup | Isaac Sim Setup | This Extension does the setup of the Isaac Sim App
[/TABLE]

### Extensions (Asset)

[TABLE]
Extension | Title | Description
isaacsim.asset.browser | Isaac Sim Asset Browser | The Isaac Sim Asset Browser extension provides an user interface for loading isaac sim assets and files.
isaacsim.asset.exporter.urdf | Isaac Sim USD to URDF exporter | Extension that exports USD files to URDF
isaacsim.asset.gen.conveyor | Isaac Sim Conveyor belt utility | The Conveyor Belt Utility Extension provides an utility to turn Rigid bodies into conveyors in Omniverse Isaac Sim. It provides an Omnigraph Node that support configuring a mesh asset into a conveyor belt Rigid Body in simulation, and commands to create the conveyor belt Omnigraph programatically.
isaacsim.asset.gen.conveyor.ui | Isaac Sim Conveyor belt utility UI | UI components for isaacsim.asset.gen.conveyor. It provides menu entries to support UI-based creation of Custom Conveyor Bodies, and a Conveyor Track tool that creates a system of fixed conveyor belts from a dataset.
isaacsim.asset.gen.omap | Isaac Sim Occupancy Map | The Isaac Sim Occupancy Map extension provides tools to generate occupancy maps for a Scene
isaacsim.asset.gen.omap.ui | UI components for the Isaac Sim Occupancy Map | UI components for the Isaac Sim Occupancy Map provides UI for 2D Occupancy Map Generation
isaacsim.asset.importer.heightmap | Height Map extension for Isaac Sim Occupancy Map | The Height Map extension provides tools for 2D Occupancy Map generation
isaacsim.asset.importer.urdf | Urdf Importer Extension | URDF Importer
isaacsim.asset.importer.mjcf | Omniverse MJCF Importer | MJCF Importer
[/TABLE]

### Extensions (Benchmark)

[TABLE]
Extension | Title | Description
isaacsim.benchmark.examples | Benchmark | This extension provides benchmarking utilities
isaacsim.benchmark.services | Benchmark Services | This extension provides benchmarking utilities
[/TABLE]

### Extensions (Code Editor)

[TABLE]
Extension | Title | Description
isaacsim.code_editor.jupyter | Jupyter notebook integration | Jupyter notebook version of Omniverse’s script editor
isaacsim.code_editor.vscode | VS Code integration | VS Code version of Omniverse’s script editor
[/TABLE]

### Extensions (Core)

[TABLE]
Extension | Title | Description
isaacsim.core.api | Isaac Sim Core | The Core extension provides a set of APIs to control the Simulation State as well as the physics scene. It also provides wrappers for USD objects, physics and visual materials.
isaacsim.core.cloner | Isaac Sim Cloner | The Cloner extension provides a set of APIs to clone prims and environments in an efficient way as well as filtering the collisions across the clones if needed.
isaacsim.core.deprecation_manager | Deprecation manager | Manage deprecated OmniGraph nodes and app/extension settings
isaacsim.core.experimental.materials | Isaac Sim Core (Materials) | The Core Materials extension provides a set of APIs to create and/or wrap one or more USD materials in the stage…
isaacsim.core.experimental.objects | Isaac Sim Core (Objects) | The Core Objects extension provides a set of APIs to create and/or wrap one or more USD objects in the stage…
isaacsim.core.experimental.prims | Isaac Sim Core (Prims) | The Core Prims extension provides a set of APIs to wrap one or more USD prims in the stage in order to manipulate (read/write) their attributes and perform other operations during the simulation.
isaacsim.core.experimental.utils | Isaac Sim Core (Utils) | The Core Utils extension provides a set of utility functions.
isaacsim.core.includes | Isaac Sim Common Includes | Extension containing common isaac sim headers
isaacsim.core.nodes | Isaac Sim Core OmniGraph Nodes | Common Isaac Sim OmniGraph nodes
isaacsim.core.prims | Isaac Sim Core API (Prims) | The Core Prims extension provides a set of APIs to read and write state information to the different types of prims.
isaacsim.core.simulation_manager | Isaac Sim Core Simulation Manager | The Core Simulation Manager extension provides a set of APIs to control and query the simulation’s state and the different callbacks available.
isaacsim.core.throttling | Isaac Sim Throttling | Control throttling behaviors for isaac sim
isaacsim.core.utils | Isaac Sim Utilities | The Core Utils extension provides useful utilities for USD, physics, math, rendering and carb.
isaacsim.core.version | Isaac Sim Version | Isaac Sim Version extension provides tools to query Isaac Sim version and build information.
[/TABLE]

### Extensions (Cortex)

[TABLE]
Extension | Title | Description
isaacsim.cortex.behaviors | Isaac Cortex Sample Behaviors | Library of Sample Behaviors for Isaac Cortex used in our core examples. It contains a pick and place state machine used on a UR10 for bin stacking, and six examples used on a Franka robot, namely a simple decider network and a state machine, block stacking, and Peck game, state machine and decider network behaviors.
isaacsim.cortex.framework | Omni Isaac Cortex | Isaac Cortex is a framework within NVIDIA’s Isaac Sim that integrates various robotics tools into a unified system, facilitating the development of collaborative robotic applications. It emphasizes reactivity and adaptability, enabling robots to operate safely alongside humans without the need for physical barriers.
[/TABLE]

### Extensions (Examples)

[TABLE]
Extension | Title | Description
isaacsim.examples.browser | Isaac Sim Example Browser | A browser for Isaac Sim assets
isaacsim.examples.extension | Generate Extension | UI tool for generating extension templates for different common workflows
isaacsim.examples.interactive | Isaac Sim Samples | Sample extensions for Isaac Sim
isaacsim.examples.ui | Isaac Sim UI Example | Example with all the Core UI Elements in Isaac Sim
[/TABLE]

### Extensions (GUI)

[TABLE]
Extension | Title | Description
isaacsim.gui.components | Isaac Sim UI Utilities | Core UI Elements for Isaac Sim
isaacsim.gui.menu | Isaac Sim Menus | Menus specific to Isaac Sim
isaacsim.gui.property | Isaac Sim Property Extensions | Adds Isaac Sim Specific Property Utils
[/TABLE]

### Extensions (Replicator)

[TABLE]
Extension | Title | Description
isaacsim.replicator.behavior | Isaac Sim Replicator Behavior Scripts | The extension provides various randomization and event scripts for Synthetic Data Generation (SDG) workflows. The scripts can be attached to prims providing modular, persitent, and shareable behaviors. The scripts use exposed variables as custom USD properties which can be modified throught the UI or programmatically.
isaacsim.replicator.behavior.ui | Isaac Sim Replicator Behavior Scripts UI | UI components for the Replicator Behavior Scripts exntension. It provides the UI Widget for the Property Panel for configuring the exposed variables of the scripts.
isaacsim.replicator.domain_randomization | Isaac Sim Replicator Domain Randomization | The extension provides various Domain Randomization scripts and OmniGraph nodes for randomizing simulation environments.
isaacsim.replicator.examples | Isaac Sim Replicator Examples | The extension provides various replicator snippets and examples for Synthetic Data Generation (SDG) workflows.
isaacsim.replicator.grasping | Replicator Grasping Workflow | Synthetic data generation workflow for grasping scenarios
isaacsim.replicator.mobility_gen | MobilityGen | A toolset for generating mobility data for robots.
isaacsim.replicator.synthetic_recorder | Isaac Sim Replicator Synthetic Data Recorder | The extension provides a UI to record synthetic data using Replicator writers. By default the UI uses the Replicator BasicWriter, it however also supports custom writers with custom parameters loaded through config files as key-value pairs.
isaacsim.replicator.writers | Isaac Sim Replicator Writers | The extension provides various custom Replicator based writers for Synthetic Data Generation (SDG) workflows. The writers are registered with Replicator at extension startup.
[/TABLE]

### Extensions (Robot Motion & Setup)

[TABLE]
Extension | Title | Description
isaacsim.robot_motion.lula | Isaac Sim Lula | Extension that provides lula python interface
isaacsim.robot_motion.lula_test_widget | Lula Test Widget | Run Simple Tests Using Lula Algorithms
isaacsim.robot_motion.motion_generation | Isaac Sim Motion Generation | Extension that provides support for generating motion with Lula-based motion policies and an interface for writing arbitrary motion policies
isaacsim.robot_setup.assembler | Robot Assembler | Alpha version of Robot Assembler Extension: Assemble multiple Articulations into a single robot
isaacsim.robot_setup.gain_tuner | Gain Tuner | Gain Tuner for Articulation PD Gains
isaacsim.robot_setup.grasp_editor | Grasp Editor | Author grasps by hand for a specific robot gripper and USD asset.
isaacsim.robot_setup.wizard | Isaac Sim Robot Wizard [Beta] | Wizard to guide through robot import and configuration
isaacsim.robot_setup.xrdf_editor | Robot Description Editor | Generates and edit Lula robot_description YAML files
[/TABLE]

### Extensions (Robot)

[TABLE]
Extension | Title | Description
isaacsim.robot.manipulators | Isaac Sim Manipulators | Manipulators
isaacsim.robot.manipulators.examples | Manipulators Examples | examples of manipulators and grippers
isaacsim.robot.manipulators.ui | Isaac Sim Manipulators UI | Manipulators
isaacsim.robot.policy.examples | Reinforcement Learning Inference Example for Robots in Isaac Sim | The Policy Based Robot Control Examples extension provides utilities for deploying reinforcement learning policies in Isaac Sim, as well as locomotion examples for humanoid and quadruped robots.
isaacsim.robot.schema | Isaac USD schema | Extension used to host all USD schemas made for robots. Provides the generated schema USDA. and a few utility functions used for informal schemas.
isaacsim.robot.surface_gripper | Isaac Sim Surface Gripper | Helper to model Suction and Distance based grippers
isaacsim.robot.surface_gripper.ui | Isaac Sim Surface Gripper UI Components | UI components for the Surface Gripper extension
isaacsim.robot.wheeled_robots | Wheeled Robots | This extension provides wheeled robot utilities
isaacsim.robot.wheeled_robots.ui | Wheeled Robots UI | This extension provides the UI elements for the wheeled_robots extension
[/TABLE]

### Extensions (ROS 2)

[TABLE]
Extension | Title | Description
isaacsim.ros2.bridge | ROS 2 Bridge | The ROS 2 Bridge extension enables communication between the Isaac Sim and ROS 2 systems. It allows for the publishing and subscribing of ROS 2 topics and services via OmniGraph nodes and Action graphs. ROS 2 publishers, subscribers and services are only active when play is pressed. To enable this extension, ensure ROS 2 libraries are sourced in the terminal before running Isaac Sim or source the lightweight ROS 2 libraries included with Isaac Sim as an alternative.
isaacsim.ros2.tf_viewer | TF Viewer | Show the tf transform tree in the viewport
isaacsim.ros2.urdf | Ros2 Robot Description URDF Importer | This extensions expands the URDF Importer by enabling importing the robot description from a given ROS node
[/TABLE]

### Extensions (Sensors)

[TABLE]
Extension | Title | Description
isaacsim.sensors.camera | Isaac Sim Camera Simulation | Provides APIs for camera prims, eg. setting lens distortion and enabling tiled rendering.
isaacsim.sensors.camera.ui | Isaac Sim Camera Simulation UI Components | Provides UI components for Isaac Sim camera simulation, eg. menu options.
isaacsim.sensors.physics | Isaac Sim Physics Sensor Simulation | Isaac Sim Physics Sensor Simulation extension provides APIs for physics-based sensors, including Contact Sensor, Effort Sensor, & IMU Sensor.
isaacsim.sensors.physics.examples | Isaac Sim Physics Sensor Simulation Examples | Isaac Sim Physics Sensor Simulation Examples extension provides example usage and snippets for Isaac Sim physics-based sensors.
isaacsim.sensors.physics.ui | Isaac Sim Physics Sensor Simulation UI Components | Isaac Sim Physics Sensor Simulation UI Components extension provides UI components for Isaac Sim physics-based sensor simulation, eg. menu options.
isaacsim.sensors.physx | Isaac Sim PhysX Sensors | Isaac Sim PhysX Sensors extension provides APIs for PhysX-raycast-based lidars and sensors including Proximity Sensor and Lightbeam Sensor.
isaacsim.sensors.physx.examples | Isaac Sim PhysX Sensor Examples | Provides example usage and snippets for Isaac Sim PhysX-raycast-based sensors.
isaacsim.sensors.physx.ui | Isaac Sim PhysX Sensor UI components | Isaac Sim PhysX Sensor UI components extension provides UI components for Isaac Sim PhysX-raycast-based sensor simulation, eg. menu options.
isaacsim.sensors.rtx | Isaac Sim Isaac Sensor Simulation | Provides APIs for RTX-based sensors, including RTX Lidar & RTX Radar.
isaacsim.sensors.rtx.ui | Isaac Sim RTX Sensor Simulation UI Components | Provides UI components for Isaac Sim RTX-based sensor simulation, eg. menu options.
[/TABLE]

### Extensions (Simulation)

[TABLE]
Extension | Title | Description
isaacsim.simulation_app | Isaac Sim Kit Helpers | This Extension that provides a way to launch a python app
[/TABLE]

### Extensions (Storage)

[TABLE]
Extension | Title | Description
isaacsim.storage.native | Isaac Sim Native Storage | Isaac Sim Native Storage
[/TABLE]

### Extensions (Test)

[TABLE]
Extension | Title | Description
isaacsim.test.collection | Isaac Sim Tests | Collection of tests for isaac sim that are not tied to a specific extension
isaacsim.test.docstring | Isaac Sim DocTest | Test interactive Python docstrings examples
[/TABLE]

### Extensions (Util)

[TABLE]
Extension | Title | Description
isaacsim.util.camera_inspector | Camera Inspector | This extension can inspect and modify the properties of cameras in the scene.
isaacsim.util.merge_mesh | Isaac Sim Merge Mesh | Isaac Sim tool to facilitate combining meshes together in a single USD Prim. It provides the ability to reset the mesh origin to world origin, and combining all materials into a single list, combining materials with the same characteristics.
isaacsim.util.physics | Isaac Sim Physics API Editor | Collision and Physics Utils
[/TABLE]

### Other Extensions

[TABLE]
Extension | Title | Description
omni.isaac.dynamic_control | Isaac Sim Dynamic Control | The Dynamic Control extension provides a set of utilities to control physics objects. It provides opaque handles for different physics objects that remain valid between PhysX scene resets, which occur whenever play or stop is pressed.
omni.kit.loop-isaac | Isaac Loop Runner | Custom Loop Runner for Isaac Sim
[/TABLE]
