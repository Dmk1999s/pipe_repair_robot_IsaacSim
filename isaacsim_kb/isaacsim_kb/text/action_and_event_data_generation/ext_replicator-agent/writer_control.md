<!-- source: action_and_event_data_generation/ext_replicator-agent/writer_control.html | title: Writer Control — Isaac Sim Documentation -->

# Writer Control
Writers determines what data to output and its format. Isaacsim.Replicator.Agent (IRA) provides built-in writers as well as the ability for you to create your own custom writers.
All the IRA built-in writers are derived from IRABasicWriter, which is derived from the Replicator BasicWriter . As a result, all the annotators from the Replicator BasicWriter are supported with the following exceptions:

- `bounding_box_2d_tight`, `bounding_box_2d_loose`, `bounding_box_3d` are overwritten by annotators with corresponding names starting with object_info_.

- `skeleton_data` is overwritten by `agent_info_skeleton_data`.

- S3 related parameters are disabled for now.

In addition, while data written is identical from Replicator, IRA built-in writers output each annotator data to separated folders for better readability. The annotators overwritten by the IRABasic writer are organized into one file called `object_detection.json`.

## Built-in Writers

### IRABasicWriter
IRABasicWriter is the base writer for all IRA built-in writers and it is derived from the Replicator BasicWriter .

#### Parameters
By default, all the following annotators are turned off. The output data is written to the `object_detection.json` file.

- `object_info_bounding_box_2d_tight`: outputs objects bounding box 2D tight data. The output data is written to the object section.

- `object_info_bounding_box_2d_loose`: outputs objects bounding box 2D loose data. The output data is written to the object section.

- `object_info_bounding_box_3d`: outputs objects bounding box 3D data. The output data is written to the object section.

- `agent_info_skeleton_data`: outputs agents skeleton data. The output data is written to agent section.

- More sections in the UI display the parameters inherited from BasicWriter. `rgb` and `camera_params` are on by default while other annotators follow the Replicator’s default setting. Refer to Replicator Annotators Information for details.

Note
`object_info` also includes the `agent_info`.

### TaoWriter
TaoWriter overwrites IRABasicWriter’s bounding box output by applying a configurable occlusion check.

#### Parameters

- `bbox`: outputs objects and agents bounding box 2D and 3D data based on the occlusion rule mentioned below. It overwrites `object_info_bounding_box_2d_tight`, `object_info_bounding_box_2d_loose` and `object_info_bounding_box_3d` from `IRABasicWriter`.

- `shoulder_height_ratio`: the ratio of head-to-shoulder distance to overall height.

- `valid_width_unoccluded_threshold`: the threshold for the ratio of visible character width to total width.

- `valid_height_unoccluded_threshold`: the threshold for the ratio of visible character height to total height.

- `agent_info_skeleton_data`: inherited from IRABasicWriter.

Note
`shoulder_height_ratio`, `valid_width_unoccluded_threshold`, and `valid_height_unoccluded_threshold` will be used to calculate the occlusion by the rule below. Occluded bounding box data will not be written to the output.

#### Occlusion Rule
To make sure characters are mostly visible, the following test is applied to select valid characters for data generation.
Two conditions are defined for whether a character must be labeled, visibility in height and visibility in width. Review the images for more details.

- Visibility Requirement in Height

- If more than `shoulder_height_ratio` of the character’s upper body is visible then this condition is met.

- If more than `valid_height_unoccluded_threshold` of the character’s body height is visible, then this condition is met.

Note
Only one of the above conditions is needed to satisfy the height requirement.

- Visibility Requirement in Width

- If more than `valid_width_unoccluded_threshold` of the character’s body width is visible, then this condition is met.

Note

- For occluded characters (characters that are blocked by an object within the camera frame), characters must satisfy both the visibility in height and width requirements.

- For truncated characters (characters that are cut off by the camera frame), characters must satisfy visibility in height or the visibility in width requirement.

- For characters that are both occluded and truncated, characters must satisfy the visibility in height or the visibility in width requirements.

### StereoWriter
StereoWriter writes the data for simulating stereo cameras to the `camera_params.json`, while applying the same occlusion check as the TaoWriter .

#### Parameters

- `customized_camera_params`: output additional camera parameter data compared to the standard `camera_params` annotator, such as the camera’s intrinsic data (`fx_fy_cx_cy`, `focallength`) and the stereo baseline (`stereo_baseline`).

- `customized_distance_to_image_plane`: output the `distance_to image_plane` data in `.pfm` file format.

- `depth_format`: specifies the data format for `distance_to_image_plane` as either `.png` or `.npm` if `customized_distance_to_image_plane` is not activated.

- `bbox`, `shoulder_height_ratio`, `valid_height_unoccluded_threshold`, `valid_width_unoccluded_threshold`, and `agent_info_skeleton_data` are the same as the TaoWriter .

Note

- Stereo cameras must be pairs with names like `Camera_01` pairing with `Camera_01_R`, where `Camera_01` is the left camera and `Camera_01_R` is the right camera.

- IRA does not spawn stereo cameras. To create stereo cameras, you can run the following script. `DIST` is the distance between the paired cameras, and `CAMERA_PATH` is the path to the camera that you want to make into a stereo camera. The script will treat the input camera as the left camera and generate the right camera for it.

```
DIST = 1
CAMERA_PATH = "/World/Cameras/Camera_01"
import omni.usd
import omni.kit.commands
from pxr import Gf, UsdGeom

camera_prim = omni.usd.get_context().get_stage().GetPrimAtPath(CAMERA_PATH)
new_translate = UsdGeom.Camera(camera_prim).GetCamera().transform.Transform(Gf.Vec3d(DIST,0,0))
omni.kit.commands.execute("CopyPrim", path_from=CAMERA_PATH, path_to=CAMERA_PATH+"_R")
stage.GetPrimAtPath(CAMERA_PATH + "_R").GetAttribute("xformOp:translate").Set(new_translate)
```

### RTSPWriter
RTSPWriter is a custom writer that streams annotated render products to an RTSP server. Each render product is registered as an RTSPCamera, and its RTSP URL is constructed using the camera’s prim path and the annotator name. It supports publishing multiple annotated video streams to a server in real time.

#### Parameters
RTSPWriter supports the following parameters, which control what data is streamed:

- `rtsp_stream_url`: The prefix of the RTSP stream URL.

- `rtsp_rgb`: Stream standard RGB (LDR color) image output.

- `rtsp_semantic_segmentation`: Stream semantic segmentation data.

- `rtsp_instance_id_segmentation`: Stream instance ID segmentation output.

- `rtsp_instance_segmentation`: Stream colored instance segmentation masks.

- `rtsp_normals`: Stream normal vectors of the scene geometry.

- `rtsp_distance_to_image_plane`: Stream the linearized distance from each pixel to the image plane.

- `rtsp_distance_to_camera`: Stream the linearized distance from each pixel to the camera.

Each of these parameters is represented as a boolean toggle in the UI. Enabling any of them will include that data type in the RTSP output stream.
Note
Before streaming from Isaac Sim using RTSPWriter, you need to install FFmpeg.
Run the following command on Linux to install FFmpeg:

```
sudo apt update && sudo apt install -y ffmpeg
```
Run the following command on Windows 10/11 to install FFmpeg:

```
winget install ffmpeg
```
If the data format of the annotator supports NVENC, the RTSPWriter will perform GPU-based encoding. Multiple GPUs are automatically distributed across the available render products.

#### RTSP Stream URL Format
Each RTSP stream URL is constructed using the following format:

```
[rtsp_stream_url]/RTSPWriter[camera_prim_path_with_underscores]_[annotator_name]
```
Where:

- `rtsp_stream_url`: The base RTSP server URL (e.g., `rtsp://localhost:8554/RTSPWriter`)

- `camera_prim_path_with_underscores`: The camera’s prim path with forward slashes `/` replaced by underscores `_`

- `annotator_name`: The original name of the specific annotator (e.g., `rgb`, `semantic_segmentation`)

Examples:
if the stream URL is `rtsp://localhost:8554/RTSPWriter`
For a camera with prim path `/World/Cameras/Camera_01` with annotator name `rtsp_rgb`:

- RGB stream: `rtsp://localhost:8554/RTSPWriter_World_Cameras_Camera_01_rgb`

For a camera with prim path `/World/Cameras/Camera` and annotator name `rtsp_distance_to_camera`:

- Distance to camera stream: `rtsp://localhost:8554/RTSPWriter_World_Cameras_Camera_distance_to_camera`

Note
A warning message will be posted in the console to show the match between annotator name and the RTSP stream URL.
Initializing RTSP streaming may take a while.
During RTSP stream initialization, the first few frames may exhibit visual artifacts or corruption. This is expected behavior that resolves automatically after the stream is fully established.

## Custom Writers
IRA supports using custom writers created by you, through the UI or config file directly.

- To enable it from UI, select Custom from the dropdown of the Replicator Setting panel, enter the writer’s name and its input parameters in the text boxes.

- To enable it from config file, put the writer’s name and parameters in the `replicator` section.

IRA obtains the writer using the writer’s name from the Replicator extension, so writers are expected to be registered in the Replicator beforehand. For writers mentioned above (provided by IRA), they are registered when IRA is loaded. Other custom writers must be registered by you.Follow the Custom Writer documentation to create and register custom writers.
