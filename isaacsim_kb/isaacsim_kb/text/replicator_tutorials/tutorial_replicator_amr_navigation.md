<!-- source: replicator_tutorials/tutorial_replicator_amr_navigation.html | title: Randomization in Simulation – AMR Navigation — Isaac Sim Documentation -->

# Randomization in Simulation – AMR Navigation
Example of using Isaac Sim and Replicator to capture synthetic data from simulated environments (AMR Navigation).

## Learning Objectives
The goal of this tutorial is to demonstrate how to setup an Isaac Sim simulation scenario together with the omni.replicator extension to capture synthetic data using diverse randomization techniques.
In this tutorial you:

- Implement scene randomizations using USD / Isaac Sim APIs:

- Randomize poses of assets in the scene

- Switch between different background environments

- Collect synthetic data at specific simulation events with Replicator

- Create and destroy render products on the fly to improve runtime performance

- Create and destroy Replicator capture graphs within the same simulation instance

### Prerequisites

- Familiarity with USD / Isaac Sim APIs for scene creation and manipulation.

- Familiarity with omni.replicator and its writers .

- Basic understanding of OmniGraph for the navigation implementation.

- Running simulations as Standalone Applications or via the Script Editor .

## Scenario
This tutorial uses the Nova Carter robot equipped with an OmniGraph navigation stack, notably without collision avoidance features. The navigation stack constantly drives the robot towards a designated Xform target (`<..>/targetXform`), positioned at the location of the randomized objects of interest. As the robot comes in the proximity of the object of interest, a synthetic data generation (SDG) pipeline is triggered to capture data from its two main camera sensors. After the data is captured the objects of interest are re-randomized and the simulation continues. After a certain number of frames (`env_interval`) the background environment is changed as well. After `num_frames` the application terminates.
The `use_temp_rp` flag is used to provide an option to use temporary render products to improve the runtime performance. This speeds up the simulation by only using the render products when capturing the data, thus avoiding the overhead of rendering the sensor views when not capturing data.
The scenario uses the left and right camera sensors of Nova Carter (`<..>/stereo_cam_<left/right>_sensor_frame/camera_sensor_<left/right>`) to collect LdrColor (rgb) annotator data using Replicator. By default, the data is written to `<working_dir>/_out_nav_sdg_demo` and runs for `num_frames=9` iterations.
Furthermore, it changes the background environment every `env_interval=3` captured frames. The `use_temp_rp` flag can be used to optimize performance by disabling the sensor render products during simulation and temporarily enabling them during data capture.
The following image provides an illustration of the resulting data from the various environments.
[image: ../_images/isaac_tutorial_replicator_amr_data.png]

## Implementation
The following section provides an overview and explanation of the implementation and examples on how to run the demo.
