<!-- source: ros2_tutorials/tutorial_ros2_camera_noise.html | title: Add Noise to Camera — Isaac Sim Documentation -->

# Add Noise to Camera

## Learning Objectives
In this example, we will:

- Have a brief introduction regarding adding an augmentation to sensor images

- Publish image data with noise added

## Getting Started
Prerequisites

- Completed the ROS 2 Cameras tutorial.

- ROS 2 bridge is enabled.

- Familiarity with omni.replicator concepts.

- Set the environment variables needed to enable ROS2 messaging in standalone workflow by completing the steps in Using Terminal .

## Running the Example

- In one terminal source your ROS 2 workspace.

- In another terminal with your ROS 2 environment sourced, run the sample script:

```
./python.sh standalone_examples/api/isaacsim.ros2.bridge/camera_noise.py
```
After the scene finishes loading, verify that you observe the viewport scanning a warehouse scene counterclockwise.

- In a new terminal with your ROS environment sourced, open an empty RViz window by running `rviz2` on the command line.

- Add a Image window by clicking on “Add” on the bottom left. In the pop-up window, under the “By display type” tab, select “Image” and click “OK”.

- A new image window will appear somewhere on your RViz screen, along with a menu item labeled “Image” in the Display window. Dock the image window somewhere convenient.

- Expand the Image in the Display menu and change the “Image Topic” to `/rgb_augmented`. Verify that a slightly noisy version of the image in Isaac Sim is now showing in the RViz image window.
[image: ../_images/isim_5.0_ros_tut_gui_ros2_camera_noise.gif]

## Code Explained
The first step is to set the camera on the render product we want to use for capturing data. There are APIs to set the camera on the viewport, but there are also lower level APIs that use the render product prim directly. Both achieve the same. Because we are already working with the render product path, we use `set_camera_prim_path` for illustrative purposes.

```
# grab our render product and directly set the camera prim
render_product_path = get_active_viewport().get_render_product_path()
set_camera_prim_path(render_product_path, CAMERA_STAGE_PATH)
```
There are several methods for defining an augmentation within a sensor pipeline:

- C++ OmniGraph node

- Python OmniGraph node

- omni.warp kernel

- numpy kernel

The numpy and omni.warp kernel options are demonstrated below to define a basic noise function. For brevity there are no out of bounds checks for the color values.

```
# GPU Noise Kernel for illustrative purposes, input is rgba, outputs rgb
@wp.kernel
def image_gaussian_noise_warp(
data_in: wp.array3d(dtype=wp.uint8), data_out: wp.array3d(dtype=wp.uint8), seed: int, sigma: float = 0.5
):
i, j = wp.tid()
dim_i = data_out.shape[0]
dim_j = data_out.shape[1]
pixel_id = i * dim_i + j
state_r = wp.rand_init(seed, pixel_id + (dim_i * dim_j * 0))
state_g = wp.rand_init(seed, pixel_id + (dim_i * dim_j * 1))
state_b = wp.rand_init(seed, pixel_id + (dim_i * dim_j * 2))

data_out[i, j, 0] = wp.uint8(float(data_in[i, j, 0]) + (255.0 * sigma * wp.randn(state_r)))
data_out[i, j, 1] = wp.uint8(float(data_in[i, j, 1]) + (255.0 * sigma * wp.randn(state_g)))
data_out[i, j, 2] = wp.uint8(float(data_in[i, j, 2]) + (255.0 * sigma * wp.randn(state_b)))
```

```
# CPU noise kernel
def image_gaussian_noise_np(data_in: np.ndarray, seed: int, sigma: float = 25.0):
np.random.seed(seed)
return data_in + sigma * np.random.randn(*data_in.shape)
```
Either of the two functions can be used with `rep.Augmentation.from_function()` to define an augmentation.

```
# register new augmented annotator that adds noise to rgba and then outputs to rgb to the ROS publisher can publish
# the image_gaussian_noise_warp variable can be replaced with image_gaussian_noise_np to use the cpu version. Ensure to update device to "cpu" if using the cpu version.
rep.annotators.register(
name="rgb_gaussian_noise",
annotator=rep.annotators.augment_compose(
source_annotator=rep.annotators.get("rgb", device="cuda"),
augmentations=[
rep.annotators.Augmentation.from_function(
image_gaussian_noise_warp, sigma=0.1, seed=1234, data_out_shape=(-1, -1, 3)
),
],
),
)
```
Note
`seed` is an optional predefined Replicator Augmentation argument that can be used with both Python and warp functions. If set to None or < 0, it will use Replicator’s global seed together with the node identifier to produce a repeatable unique seed. When used with warp kernels, the seed is used to initialize a random number generator that produces a new integer seed value for each warp kernel call.
Next, a new writer is created with the new rgb_gaussian_noise annotator and registered.

```
# Create a new writer with the augmented image
rep.writers.register_node_writer(
name=f"CustomROS2PublishImage",
node_type_id="isaacsim.ros2.bridge.ROS2PublishImage",
annotators=[
"rgb_gaussian_noise",
omni.syntheticdata.SyntheticData.NodeConnectionTemplate(
"IsaacReadSimulationTime", attributes_mapping={"outputs:simulationTime": "inputs:timeStamp"}
),
],
category="custom",
)

# Register writer for Replicator telemetry tracking
(
rep.WriterRegistry._default_writers.append("CustomROS2PublishImage")
if "CustomROS2PublishImage" not in rep.WriterRegistry._default_writers
else None
)
```
The `CustomROS2PublishImage` writer, which uses our new augmented `rgb_gaussian_noise` annotator, is registered. We can attach the render product to our replicator writer after initializing. This will begin capturing and publishing data to ROS.

```
# Create the new writer and attach to our render product
writer = rep.writers.get(f"CustomROS2PublishImage")
writer.initialize(topicName="rgb_augmented", frameId="sim_camera")
writer.attach([render_product_path])
```

## Summary
This tutorial covered the basics of adding an augmentation to the ROS sensor pipeline and adding noise to the RGB sensor output.

### Next Steps
Continue on to the next tutorial in our ROS Tutorials series, Publishing Camera’s Data .
