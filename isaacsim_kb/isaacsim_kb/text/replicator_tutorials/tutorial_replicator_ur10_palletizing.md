<!-- source: replicator_tutorials/tutorial_replicator_ur10_palletizing.html | title: Randomization in Simulation – UR10 Palletizing — Isaac Sim Documentation -->

# Randomization in Simulation – UR10 Palletizing
Example of using Isaac Sim and Replicator to capture synthetic data from simulated environments (UR10 palletizing).

## Learning Objectives
The goal of this tutorial is to provide an example on how to extend an existing Isaac Sim simulation to trigger a synthetic data generation (SDG) pipeline to randomize the environment and collect synthetic data at specific simulation events using the omni.replicator extension.
Note
The tutorial makes sure that the SDG pipeline does not change the outcome of the running simulation and cleans up its changes after each capture.
This tutorial teaches you to:

- Collect synthetic data at specific simulation events with Replicator:

- Using annotators to collect the data and manually write it to disk

- Using writers to implicitly write the data to disk

- Setup various Replicator randomization graphs to:

- Randomize lights around the object of interest

- Randomize materials and textures of objects of interest running at different rates

- Create and destroy Replicator randomization and capture graphs within the same simulation instance

- Switch between different rendering modes on the fly

- Create and destroy render products on the fly to improve runtime performance

## Prerequisites

- Familiarity with the omni.replicator extension and its annotators and writers .

- Familiarity with Replicator randomizers and OmniGraph for a better understanding of the randomization pipeline.

- Executing code from the Script Editor .

## Scenario
For this tutorial, you build on top of the UR10 palletizing demo scene, which is programmatically loaded and started by the provided script.
The demo scene depicts a simple palletizing scenario where the UR10 robot picks up bins from a conveyor belt and places them on a pallet.
For bins that are flipped, the robot flips them right side up with a helper object before placing them on the pallet.
In the above images, data collected from the actions in the left side image belong to the bin flip scenario.
In the above images, data collected from the right side image belongs to the bin on pallet scenario.
For each frame in this scenario, the camera pose is iterated through in a predefined sequence, while the custom lights’ parameters are randomized. Data is generated for each manipulated bin in the palletizing demo scene.
The events for which synthetic data are collected are:

- When the bin is placed on the flipping helper object

- When the bin is placed on the pallet (or on another bin that is already on the pallet)

Below, in each captured frame the bin colors are randomized. At a lower randomization rate, the camera poses and pallet textures are also randomized.
[image: ../_images/isaac_tutorial_replicator_palletizing_data.png]The annotator data collected by the scenario includes the LdrColor (rgb) and instance segmentation.
The data is directly accessed from the annotators and saved to disk using custom helper functions.
The data is written to disk using a built-in Replicator writer (`BasicWriter`).

## Implementation
