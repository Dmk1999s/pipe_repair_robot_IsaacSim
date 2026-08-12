<!-- source: action_and_event_data_generation/index.html | title: Action and Event Data Generation — Isaac Sim Documentation -->

# Action and Event Data Generation
Action and Event Data Generation is a reference application for Isaac Sim, featuring a wide array of extensions for realistic indoor simulation and large-scale synthetic data generation. This application is suited for simulating indoor environments such as warehouses, retail facilities, factories and more. It can simulate intricate scenarios involving people, robots, and objects, with advanced controls over behaviors, environments, and sensor setups. The platform supports customizable assets, automated camera systems, and comprehensive data annotation, enabling you to create realistic ground truth datasets, which makes it ideal for training and validating Vision AI models.
You can launch the app with `./isaac-sim.action_and_event_data_generation.sh` for Linux and `.\isaac-sim.action_and_event_data_generation.bat` for Windows. The Action and Event Data Generation app will have the action and event SDG extensions pre-enabled and a custom workspace layout.

## Action and Event Data Generation Stack

### Extensions

[TABLE]
Extension | Extension APIs | Description
Actor Simulation and SDG | Isaacsim.Replicator.Agent | The Isaacsim.Replicator.Agent (IRA) extension is a synthetic data generation tool that simulates human characters and robots in 3D environments to create high-quality training data for computer vision models, with applications in retail, manufacturing, and human-robot collaboration scenarios.
Object Simulation and SDG | Isaacsim.Replicator.Object | The isaacsim.replicator.object (IRO) is a no-code-change-required extension that generates synthetic data for model training that can be used on a range of tasks from retail object detection to robotics. The extension can be run from the UI or the isaac-sim container.
VLM Scene Captioning | Isaacsim.Replicator.Caption | The Isaacsim.Replicator Caption (IRC) extension operates on a stage and produces a human readable prose which is a natural language description of the stage, either as a long and/or short caption. It also produces the corresponding image and a 3D spatial representation of the objects of interest in the scene.
Animated People Controller | Omni.Anim.People | The omni.anim.people (OAP) extension is a tool to control character behaviors through animation.
Animated Robot Controller | Isaacsim.Anim.Robot | The Isaacsim.Anim.Robot (IAR) is an extension that enables realistic robot animation through the playback of captured simulation motion data. This module bridges the gap between physics-based simulation and animation, allowing users to recreate precise robot movements without the computational overhead of real-time physics calculations. It provides tools for converting physics-enabled robot models into animated representations while preserving their kinematic accuracy and visual fidelity.
RTX Sensor Placement and Calibration | Isaacsim.Sensors.RTX.Placement | isaacsim.sensors.rtx.placement (ISP) enables users to automatically determine optimal camera locations based on scene layout and coverage requirements. It also provides detailed camera metadata for generated cameras and generates the stage layout visualization with each camera’s FOV coverage.
Action and Event Generation Utilities | Omni.Metropolis.Utils | The shared utilities across the Action and Event Generation extension stack.
[/TABLE]

## Extension Tutorials
