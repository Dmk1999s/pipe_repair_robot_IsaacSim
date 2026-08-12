<!-- source: replicator_tutorials/tutorial_replicator_recorder.html | title: Synthetic Data Recorder — Isaac Sim Documentation -->

# Synthetic Data Recorder
This tutorial introduces the Synthetic Data Recorder for Isaac Sim, which is a GUI extension for recording synthetic data with the possibility of using custom writers to record the data in various formats.
The Synthetic Data Recorder requires assets to be semantically labelled for all of the annotators to work correctly. The recorder uses the `BasicWriter` by default with access to most common annotators .

## Getting Started
The UI window can be opened from the main menu using Tools > Replicator > Synthetic Data Recorder.
This tutorial uses the following stage as an example:

```
https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/5.1
/Isaac/Samples/Replicator/Stage/full_warehouse_worker_and_anim_cameras.usd
```
The stage asset can be found in the Content Browser under Isaac Sim > Samples > Replicator > Stage > full_warehouse_worker_and_anim_cameras.usd, or can be loaded using by inserting the whole URL in the path field.
[image: Synthetic Data Recorder]The example stage comes preloaded with semantic annotations and multiple cameras. Some of the included cameras are animated to move around the scene when running the simulation. To create custom camera movement animations, review the Camera Animation Tutorial .

## Basic Usage
The recorder is split into two main parts:

- the Writer frame - containing sensor, data, and output parameters

- the Control frame - containing the recording functionalities such as start, stop, pause, and parameters such as the number of frames to execute

### Writer Frame
The Writer frame provides access to Render Products, Parameters, Output, and Config options.
The Render Products frame allows the creation of a list of render product entries using the Add New Render Product button. By default, a new entry is added to the list using the active viewport camera as its camera path (see left figure). If cameras are selected in the stage viewer, these are added to the render products list (see right figure). The render products list can include the same camera path multiple times, with each instance having a different resolution. All entry values, such as camera path or resolution, can be manually edited in the input fields.
[image: Synthetic Data Recorder Render Products]The Parameters frame offers a choice between the default built-in Replicator writer (`BasicWriter`) and a custom writer. Default writer parameters, primarily annotators, can be selected from the checkbox list. Parameters for custom writers, which are unknown beforehand, must be provided in the form of a JSON file containing all required parameters. The path to the JSON file is entered in the Parameters Path input field.
[image: Synthetic Data Recorder Parameters]The Output frame (left figure) specifies the working directory path where the data is saved, along with the folder name for the current recording. The output folder name is incremented in case of conflicts. The recorder also supports writing to S3 buckets by enabling Use S3, entering the required fields, and ensuring AWS credentials are properly configured.
Note
When writing to S3, the Increment folder naming feature is not supported and defaults to Timestamp.
The Config frame (right figure) allows loading and saving the GUI writer state as a JSON configuration file. By default, the extension loads the most recently used configuration state.
[image: Synthetic Data Recorder Output and Config]

### Control Frame
The Control frame contains the recording functionalities such as Start/Stop and Pause/Resume, and parameters such as the number of frames to record or the number of subframes to render for each recorded frame.

- The Start button creates a writer, given the selected parameters, and starts the recording.

- The Stop button stops the recording and clears the writer.

- The Pause button pauses the recording without clearing the writer.

- The Resume button resumes the recording.

- The Number of Frames input field sets the number of frames to record, after which the recorder is stopped and the writer cleared. If the value is set to `0`, the recording runs indefinitely or until the Stop button is pressed.

- The RTSubframes field sets the number of additional subframes to render for each per frame. This can be used if randomized materials are not loaded in time or if temporal rendering artifacts (such as ghosting) are present due to objects being teleported.

- The Control Timeline checkbox starts, stops, pauses, and resumes the timeline together with the recorder.

- The Verbose checkbox enables verbose logging for the recorder (events such as start, stop, pause, resume, and the number of frames recorded).

Note
To improve the rendering quality, or to avoid any rendering artifacts caused by low lighting conditions or fast-moving objects, increase the RTSubframes parameter. This renders multiple subframes for each frame, thereby improving the quality of recorded data at the expense of longer rendering times per frame. For more details, see the subframes documentation.

## Custom Writer Example
To support custom data formats, the custom writer can be registered and loaded from the GUI. In this example, a custom writer called `MyCustomWriter` is registered using the Script Editor for use with the recorder.
MyCustomWriter
```
1import numpy as np
2from omni.replicator.core import AnnotatorRegistry, BackendDispatch, Writer, WriterRegistry
3
4class MyCustomWriter(Writer):
5 def __init__(
6 self,
7 output_dir,
8 rgb = True,
9 normals = False,
10 ):
11 self.version = "0.0.1"
12 self.backend = BackendDispatch({"paths": {"out_dir": output_dir}})
13 self.annotators = []
14 if rgb:
15 self.annotators.append(AnnotatorRegistry.get_annotator("rgb"))
16 if normals:
17 self.annotators.append(AnnotatorRegistry.get_annotator("normals"))
18 self._frame_id = 0
19
20 def write(self, data: dict):
21 for annotator in data.keys():
22 # If there are multiple render products the data will be stored in subfolders
23 annotator_split = annotator.split("-")
24 render_product_path = ""
25 multi_render_prod = 0
26 if len(annotator_split) > 1:
27 multi_render_prod = 1
28 render_product_name = annotator_split[-1]
29 render_product_path = f"{render_product_name}/"
30
31 # rgb
32 if annotator.startswith("rgb"):
33 if multi_render_prod:
34 render_product_path += "rgb/"
35 filename = f"{render_product_path}rgb_{self._frame_id}.png"
36 print(f"[{self._frame_id}] Writing {self.backend.output_dir}/{filename} ..")
37 self.backend.write_image(filename, data[annotator])
38
39 # semantic_segmentation
40 if annotator.startswith("normals"):
41 if multi_render_prod:
42 render_product_path += "normals/"
43 filename = f"{render_product_path}normals_{self._frame_id}.png"
44 print(f"[{self._frame_id}] Writing {self.backend.output_dir}/{filename} ..")
45 colored_data = ((data[annotator] * 0.5 + 0.5) * 255).astype(np.uint8)
46 self.backend.write_image(filename, colored_data)
47
48 self._frame_id += 1
49
50 def on_final_frame(self):
51 self._frame_id = 0
52
53WriterRegistry.register(MyCustomWriter)
```
my_params.json
```
1{
2 "rgb": true,
3 "normals": true
4}
```
[image: Synthetic Data Recorder Custom Writer]

### Data Visualization Writer
The Data Visualization writer is a custom writer that can be used to visualize the annotation data on top of rendered images. The writer and its implementation details can be found in `/isaacsim.replicator.writers/python/scripts/writers/data_visualization_writer.py`, and can be imported using `from isaacsim.replicator.writers import DataVisualizationWriter`. The custom writer can be selected from the Parameters frame and its parameters can be loaded from a JSON file using the Parameters Path input field. Here is an example JSON file that can be used to parameterize the writer:
my_data_visualization_params.json
```
1{
2 "bounding_box_2d_tight": true,
3 "bounding_box_2d_tight_params": {
4 "background": "rgb",
5 "outline": "green",
6 "fill": null
7 },
8 "bounding_box_2d_loose": true,
9 "bounding_box_2d_loose_params": {
10 "background": "normals",
11 "outline": "red",
12 "fill": null
13 },
14 "bounding_box_3d": true,
15 "bounding_box_3d_params": {
16 "background": "rgb",
17 "fill": "blue",
18 "width": 2
19 }
20}
```
And the resulting data:
[image: Synthetic Data Recorder Visualization Writer]For more information on the supported parameters, see the class docstring:
DataVisualizationWriter class docstring
```
1"""Data Visualization Writer
2
3This writer can be used to visualize various annotator data.
4
5Supported annotators:
6- bounding_box_2d_tight
7- bounding_box_2d_loose
8- bounding_box_3d
9
10Supported backgrounds:
11- rgb
12- normals
13
14Args:
15 output_dir (str):
16 Output directory for the data visualization files forwarded to the backend writer.
17 bounding_box_2d_tight (bool, optional):
18 If True, 2D tight bounding boxes will be drawn on the selected background (transparent by default).
19 Defaults to False.
20 bounding_box_2d_tight_params (dict, optional):
21 Parameters for the 2D tight bounding box annotator. Defaults to None.
22 bounding_box_2d_loose (bool, optional):
23 If True, 2D loose bounding boxes will be drawn on the selected background (transparent by default).
24 Defaults to False.
25 bounding_box_2d_loose_params (dict, optional):
26 Parameters for the 2D loose bounding box annotator. Defaults to None.
27 bounding_box_3D (bool, optional):
28 If True, 3D bounding boxes will be drawn on the selected background (transparent by default). Defaults to False.
29 bounding_box_3d_params (dict, optional):
30 Parameters for the 3D bounding box annotator. Defaults to None.
31 frame_padding (int, optional):
32 Number of digits used for the frame number in the file name. Defaults to 4.
33
34"""
```

## Replicator Randomized Cameras
To take advantage of Replicator randomization techniques, randomized cameras can be loaded using the Script Editor before starting the recorder to run scene randomizations during recording. In this example a randomized camera is created using the Replicator API. This can be attached as a render product to the recorder and for each frame the camera is randomized with the given parameters.
Randomized Camera
```
1import omni.replicator.core as rep
2
3camera = rep.create.camera()
4with rep.trigger.on_frame():
5 with camera:
6 rep.modify.pose(
7 position=rep.distribution.uniform((-5, 5, 1), (-1, 15, 5)),
8 look_at="/Root/Warehouse/SM_CardBoxA_3",
9 )
```
[image: Synthetic Data Recorder Custom Writer]

## Recording Loop Overview
The Synthetic Data Recorder is a GUI extension for Isaac Sim that uses the `BasicWriter` or custom Replicator writers for capturing data. Its implementation is located in `/isaacsim.replicator.synthetic_recorder/isaacsim/replicator/synthetic_recorder/synthetic_recorder.py` and utilizes the `orchestrator.step(rt_subframes, pause_timeline, delta_time)` function to manage the recording process. This function ensures that recorded frames remain synchronized with the stage by waiting for any “frames in flight” from the renderer. For integration with the UI, the recorder uses the asynchronous version of this function: `step_async`.

```
while self._current_frame < num_frames:
timeline = omni.timeline.get_timeline_interface()

if self.control_timeline and not timeline.is_playing():
timeline.play()
timeline.commit()

await rep.orchestrator.step_async(rt_subframes=self.rt_subframes, delta_time=None, pause_timeline=False)

self._current_frame += 1
```

The recording loop offers flexibility for different use cases. It can advance the timeline for dynamic scenes, such as simulations or animations, or operate without advancing the timeline for static captures. This approach enables recording scenarios like randomizing views, adjusting lighting conditions, or repositioning objects.
