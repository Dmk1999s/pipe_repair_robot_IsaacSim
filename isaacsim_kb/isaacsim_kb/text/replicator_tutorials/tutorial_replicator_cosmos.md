<!-- source: replicator_tutorials/tutorial_replicator_cosmos.html | title: Cosmos Synthetic Data Generation — Isaac Sim Documentation -->

# Cosmos Synthetic Data Generation
This tutorial demonstrates generating multi-modal synthetic data for NVIDIA Cosmos using the `CosmosWriter` in Isaac Sim. The writer captures synchronized RGB, depth, segmentation, and edge data from a robot navigating a warehouse environment.
The generated data serves as ground truth input for Cosmos Transfer , which transforms low-resolution control signals into high-quality visual simulations through its Multi-ControlNet architecture.
[image: Multi-modal data captured from robot perspective: RGB, depth, segmentation, shaded segmentation, and edge maps]

## Prerequisites

- Familiarity with the omni.replicator extension and its writers

- Basic understanding of Isaac Sim’s SDG Getting Started Scripts

- Running simulations as Standalone Applications or via the Script Editor .

## What the CosmosWriter Generates
The writer outputs five synchronized modalities from the robot’s camera:

- RGB - Color imagery (vis control)

- Depth - Distance-to-camera for spatial understanding

- Segmentation - Instance masks for object tracking

- Shaded Segmentation - Instance masks with realistic shading

- Edges - Canny edge detection for boundaries

These modalities correspond to Cosmos Transfer’s control branches:

- vis: Uses RGB imagery with bilateral blurring

- edge: Applies Canny edge detection (tunable thresholds)

- depth: Depth maps for 3D structure understanding

- seg: Segmentation masks for object identification

Each control branch can be weighted (0.0-1.0) to balance adherence vs. creative freedom in the generated output.

## Implementation
This example demonstrates a Carter Nova robot autonomously navigating through a warehouse environment. As the robot moves from its starting position to a target location, the `CosmosWriter` captures synchronized multi-modal data (RGB, depth, segmentation, shaded segmentation, and edges) from the robot’s front camera. The captured data is organized into clips, with each clip containing a sequence of frames that can be used as input for Cosmos Transfer.

## Output Structure
The `CosmosWriter` generates organized multi-modal data optimized for Cosmos Transfer. Each clip represents a continuous sequence of frames captured during robot navigation:

```
_out_cosmos_warehouse/
clip_0000/ # First clip sequence
rgb/ # Standard color images
rgb_0000.png, rgb_0001.png, ...
depth/ # Colorized depth visualization
depth_0000.png, depth_0001.png, ...
segmentation/ # Instance/semantic masks
segmentation_0000.png, segmentation_0001.png, ...
shaded_seg/ # Segmentation with realistic shading
shaded_seg_0000.png, shaded_seg_0001.png, ...
edges/ # Canny edge detection results
edges_0000.png, edges_0001.png, ...
rgb.mp4 # Combined RGB video
depth.mp4 # Combined depth video
segmentation.mp4 # Combined segmentation video
shaded_seg.mp4 # Combined shaded segmentation video
edges.mp4 # Combined edges video
clip_0001/ # Next clip sequence
```

## Advanced Usage
Custom Segmentation Colors:
Map specific semantic labels to custom colors when you need consistent class identification across datasets. Use this when training models that require specific object classes to maintain the same color/ID across all training data, ensuring Cosmos Transfer preserves class relationships.

```
segmentation_mapping = {
"floor": [255, 0, 0, 255], # Red
"wall": [0, 255, 0, 255], # Green
"rack": [0, 0, 255, 255] # Blue
}

# Note: This overrides instance ID mode and requires semantic annotations
cosmos_writer.initialize(
backend=backend,
segmentation_mapping=segmentation_mapping
)
```
Edge Detection Tuning:
Adjust Canny edge detection parameters for the hysteresis procedure when generating edge maps. The Canny algorithm uses two thresholds:

- Low threshold: Edges with gradient magnitude above this value are considered as potential edges

- High threshold: Edges with gradient magnitude above this value are definitely edges

Lower threshold values detect more edges (including noise), while higher values produce cleaner output with only strong edges. Values typically range from 10-200.

```
cosmos_writer.initialize(
backend=backend,
use_instance_id=True,
canny_threshold_low=10, # Low threshold for hysteresis
canny_threshold_high=100 # High threshold for hysteresis
)
```

## Using Data with Cosmos Transfer
The generated data can be used with Cosmos Transfer to create high-quality visual simulations. Here’s how the modalities map to Transfer’s control branches:
Basic Single Control Example:

```
{
"prompt": "A modern warehouse with autonomous robots...",
"input_video_path": "_out_cosmos_warehouse/clip_0000/rgb.mp4",
"edge": {
"control_weight": 1.0
}
}
```
Multi-Modal Control Example:

```
{
"prompt": "High-quality warehouse simulation...",
"input_video_path": "_out_cosmos_warehouse/clip_0000/rgb.mp4",
"vis": {"control_weight": 0.25},
"edge": {"control_weight": 0.25},
"depth": {
"input_control": "_out_cosmos_warehouse/clip_0000/depth.mp4",
"control_weight": 0.25
},
"seg": {
"input_control": "_out_cosmos_warehouse/clip_0000/segmentation.mp4",
"control_weight": 0.25
}
}
```
Key Considerations:

- Control Weights: Values 0.0-1.0 control adherence (higher = stricter following, lower = more creative freedom)

- Automatic Normalization: If total weights > 1.0, they’re normalized automatically

- Prompting: Focus on single scenes with rich descriptions; avoid camera control instructions

- Safety: Human faces are automatically blurred by Cosmos Guardrail

For advanced features like spatiotemporal control maps and prompt upsampling, refer to the Cosmos Transfer documentation .

## Summary
This tutorial demonstrated using the CosmosWriter to generate synchronized multi-modal data from a robot navigating a warehouse. The output provides ground truth for Cosmos Transfer to create high-quality visual simulations for physical AI applications.
