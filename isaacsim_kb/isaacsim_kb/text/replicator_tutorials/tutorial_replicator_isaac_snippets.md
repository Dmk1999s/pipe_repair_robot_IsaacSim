<!-- source: replicator_tutorials/tutorial_replicator_isaac_snippets.html | title: Useful Snippets — Isaac Sim Documentation -->

# Useful Snippets
Various examples of Isaac Sim Replicator snippets that can be run as Standalone Applications or from the UI using the Script Editor .

## Annotator and Custom Writer Data from Multiple Cameras
Example on how to access data from multiple cameras in a scene using annotators or custom writers. The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```
./python.sh standalone_examples/api/isaacsim.replicator.examples/multi_camera.py
```

## Synthetic Data Access at Specific Simulation Timepoints
Example on how to access synthetic data (RGB, semantic segmentation) from multiple cameras in a simulation scene at specific events using annotators or writers. The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```
./python.sh standalone_examples/api/isaacsim.replicator.examples/simulation_get_data.py
```

## Custom Event Randomization and Writing
The following example showcases the use of custom events to trigger randomizations and data writing at various times throughout the simulation. The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```
./python.sh standalone_examples/api/isaacsim.replicator.examples/custom_event_and_write.py
```

## Motion Blur
This example demonstrates how to capture motion blur data using RTX Real-Time and RTX Interactive (Path Tracing) rendering modes. For the RTX - Real-Time mode, refer to motion blur parameters . For the RTX – Interactive (Path Tracing) mode, motion blur is achieved by rendering multiple subframes (`/omni/replicator/pathTracedMotionBlurSubSamples`) and combining them to create the effect.
The example uses animated and physics-enabled assets with synchronized motion. Keyframe animated assets can be advanced at any custom delta time due to their interpolated motion, whereas physics-enabled assets require a custom physics FPS to ensure motion samples at any custom delta time. The example showcases how to compute the target physics FPS, change it if needed, and restore the original physics FPS after capturing the motion blur.
The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```
./python.sh standalone_examples/api/isaacsim.replicator.examples/motion_blur.py
```

## Subscribers and Events at Custom FPS
Examples of subscribing to various events (such as stage, physics, and render/app), setting custom update rates, and adjusting various related settings. The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```
./python.sh standalone_examples/api/isaacsim.replicator.examples/subscribers_and_events.py
```

## Accessing Writer and Annotator Data at Custom FPS
Example of how to trigger a writer and access annotator data at a custom FPS, with product rendering disabled when the data is not needed. The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```
./python.sh standalone_examples/api/isaacsim.replicator.examples/custom_fps_writer_annotator.py
```
Note
It is currently not possible to change timeline (stage) FPS after the replicator graph creation as it causes a graph reset. This issue is being addressed. As a workaround make sure you are setting the timeline (stage) parameters before creating the replicator graph.

## Cosmos Writer Example
This example demonstrates the `CosmosWriter` for capturing multi-modal synthetic data compatible with NVIDIA Cosmos world foundation models. It creates a simple falling box scene and captures synchronized RGB, segmentation, depth, and edge data (images and videos) that can be used with Cosmos Transfer to generate photorealistic variations.
For a more detailed tutorial please see Cosmos Synthetic Data Generation .
The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```
./python.sh standalone_examples/api/isaacsim.replicator.examples/cosmos_writer_simple.py
```
