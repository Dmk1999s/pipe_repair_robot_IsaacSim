<!-- source: py/source/extensions/isaacsim.replicator.writers/docs/index.html | title: [isaacsim.replicator.writers] Isaac Sim Replicator Writers — Isaac Sim -->

# [isaacsim.replicator.writers] Isaac Sim Replicator Writers
Version: 1.0.17
The extension provides various custom Replicator based writers for Synthetic Data Generation (SDG) workflows. The writers are registered with Replicator at extension startup.

## Enable Extension
The extension can be enabled (if not already) in one of the following ways:

## Pytorch Online Writer and Listener
The `PytorchWriter` and `PytorchListener` are APIs for using `omni.replicator`’s writer API to retrieve various data such as RGB from the specified cameras (supports multiple cameras) and provides them to the user in both default format (e.g.: PNG for RGB data) and batched pytorch tensors. The `PytorchListener` provides an API to directly retrieve data sent to the `PytorchWriter` without the need to access the stored by `omni.replicator`’s `BackendDispatch`.

## API

### Python API

[TABLE]
DataVisualizationWriter | Data Visualization Writer
DOPEWriter | Basic writer capable of writing built-in annotator groundtruth.
PoseWriter | Pose Writer
PytorchListener | A Observer/Listener that keeps track of updated data sent by the writer.
PytorchWriter | A custom writer that uses omni.replicator API to retrieve RGB data via render products
YCBVideoWriter | Writer capable of writing annotator groundtruth in the YCB Video Dataset format.
[/TABLE]

classDataVisualizationWriter(*args:Any, **kwargs:Any)
Bases: `Writer`
Data Visualization Writer
This writer can be used to visualize various annotator data.
Supported annotators: - bounding_box_2d_tight - bounding_box_2d_loose - bounding_box_3d
Supported backgrounds: - rgb - normals
Parameters:

- output_dir (str) – Output directory for the data visualization files forwarded to the backend writer.

- bounding_box_2d_tight (bool, optional) – If True, 2D tight bounding boxes will be drawn on the selected background (transparent by default). Defaults to False.

- bounding_box_2d_tight_params (dict, optional) – Parameters for the 2D tight bounding box annotator. Defaults to None.

- bounding_box_2d_loose (bool, optional) – If True, 2D loose bounding boxes will be drawn on the selected background (transparent by default). Defaults to False.

- bounding_box_2d_loose_params (dict, optional) – Parameters for the 2D loose bounding box annotator. Defaults to None.

- bounding_box_3d (bool, optional) – If True, 3D bounding boxes will be drawn on the selected background (transparent by default). Defaults to False.

- bounding_box_3d_params (dict, optional) – Parameters for the 3D bounding box annotator. Defaults to None.

- frame_padding (int, optional) – Number of digits used for the frame number in the file name. Defaults to 4.

detach()
write(data:dict)
BB_2D_LOOSE='bounding_box_2d_loose_fast'
BB_2D_TIGHT='bounding_box_2d_tight_fast'
BB_3D='bounding_box_3d_fast'
SUPPORTED_BACKGROUNDS=['rgb','normals']

classDOPEWriter(*args:Any, **kwargs:Any)
Bases: `Writer`
Basic writer capable of writing built-in annotator groundtruth.
output_dir
Output directory string that indicates the directory to save the results. If use_s3 == True, this will be the bucket name.

semantic_types
List of semantic types to consider when filtering annotator data. Default: [“class”]

image_output_format
String that indicates the format of saved RGB images. Default: “png”

use_s3
Boolean value that indicates whether output will be written to s3 bucket. Default: False

Example

```
>>> import omni.replicator.core as rep
>>> camera = rep.create.camera()
>>> render_product = rep.create.render_product(camera, (512, 512))
>>> writer = rep.WriterRegistry.get("DOPEWriter")
>>> import carb
>>> tmp_dir = carb.tokens.get_tokens_interface().resolve("${temp}/rgb")
>>> writer.initialize(output_dir=tmp_dir, class_name_to_index_map=class_name_to_index_map)
>>> writer.attach([render_product])
>>> rep.orchestrator.run()
```
is_last_frame_valid()→bool
Checks if the last frame was valid (training data was present).
Returns:
True if the last frame was valid, False otherwise.

Return type:
bool

register_pose_annotator()
setup_writer(writer_config:dict)
Initialize writer and attach render product :param config_data: A dictionary containing the general configurations for the script. :param writer_config: A dictionary containing writer-specific configurations.

write(data:dict)
Write function called from the OgnWriter node on every frame to process annotator output.
Parameters:
data – A dictionary containing the annotator data for the current frame.

classPoseWriter(*args:Any, **kwargs:Any)
Bases: `Writer`
Pose Writer
Parameters:

- output_dir – Output directory string that indicates the directory to save the results.

- use_subfolders – If True, the writer will create subfolders for each render product, otherwise all data is saved in the same folder.

- visibility_threshold – Objects with visibility below this threshold will be skipped. Default: `0.0` (fully occluded)

- skip_empty_frames – If True, the writer will skip frames that do not have visible objects.

- write_debug_images – If True, the writer will include rgb images overlaid with the projected 3d bounding boxes.

- frame_padding – Pad the frame number with leading zeroes. Default: `4`

- format – Specifies which format the data will be outputted as. Default: `None` (will write most of the available data)

detach()
get_current_frame_id()
write(data:dict)
BB3D_ANNOT_NAME='bounding_box_3d_fast'
CAM_PARAMS_ANNOT_NAME='camera_params'
CUBOID_EDGE_COLORS={'back':'blue','connecting':'green','front':'red'}
CUBOID_KEYPOINTS_ORDER_DEFAULT=['Center','LDB','LDF','LUB','LUF','RDB','RDF','RUB','RUF']
CUBOID_KEYPOINT_COLORS=['white','red','green','blue','yellow','cyan','magenta','orange','purple']
CUBOID_KEYPOINT_ORDER_DOPE=['LUF','RUF','RDF','LDF','LUB','RUB','RDB','LDB','Center']
RGB_ANNOT_NAME='rgb'
SUPPORTED_FORMATS={'centerpose','dope'}

classPytorchListener
Bases: `object`
A Observer/Listener that keeps track of updated data sent by the writer. Is passed in the initialization of a PytorchWriter at which point it is pinged by the writer after any data is passed to the writer.
get_rgb_data()→Tensor|None
Returns RGB data as a batched tensor from the current data stored.
Returns:
images in batched pytorch tensor form

Return type:
images (Optional[torch.Tensor])

write_data(data:dict)→None
Updates the existing data in the listener with the new data provided.
Parameters:
data (dict) – new data retrieved from writer.

classPytorchWriter(*args:Any, **kwargs:Any)
Bases: `Writer`
A custom writer that uses omni.replicator API to retrieve RGB data via render products
and formats them as tensor batches. The writer takes a PytorchListener which is able to retrieve pytorch tensors for the user directly after each writer call.

Parameters:

- listener (PytorchListener ) – A PytorchListener that is sent pytorch batch tensors at each write() call.

- output_dir (str) – directory in which rgb data will be saved in PNG format by the backend dispatch. If not specified, the writer will not write rgb data as png and only ping the listener with batched tensors.

- device (str) – device in which the pytorch tensor data will reside. Can be “cpu”, “cuda”, or any other format that pytorch supports for devices. Default is “cuda”.

write(data:dict)→None
Sends data captured by the attached render products to the PytorchListener and will write data to the output directory if specified during initialization.
Parameters:
data (dict) – Data to be pinged to the listener and written to the output directory if specified.

classYCBVideoWriter(*args:Any, **kwargs:Any)
Bases: `Writer`
Writer capable of writing annotator groundtruth in the YCB Video Dataset format.
output_dir
Output directory string that indicates the directory to save the results.

num_frames
Total number of frames to be generated.

semantic_types
List of semantic types to consider when filtering annotator data. Default: [“class”]

rgb
Boolean value that indicates whether the rgb annotator will be activated and the data will be written or not. Default: False.

bounding_box_2d_tight
Boolean value that indicates whether the bounding_box_2d_tight annotator will be activated and the data will be written or not. Default: False.

semantic_segmentation
Boolean value that indicates whether the semantic_segmentation annotator will be activated and the data will be written or not. Default: False.

distance_to_image_plane
Boolean value that indicates whether the distance_to_image_plane annotator will be activated and the data will be written or not. Default: False.

image_output_format
String that indicates the format of saved RGB images. Default: “png”

pose
Boolean value that indicates whether the pose annotator will be activated and the data will be written or not. Default: False.

class_name_to_index_map
Mapping between semantic label and index used in the YCB Video Dataset. This indices are used in the ‘cls_indexes’ field of the generated meta.mat file, in addition to being used to color the semantic segmentation (where pixels are colored according to the grayscale class index).

factor_depth
Depth scaling factor used in the YCB Video Dataset. Default: 10000.

intrinsic_matrix
Camera intrinsic matrix. shape is (3, 3).

is_last_frame_valid()→bool
Checks if the last frame was valid (training data was present).
Returns:
True if the last frame was valid, False otherwise.

Return type:
bool

register_pose_annotator()
Registers the annotators for the specific writer :param config_data: A dictionary containing the configuration data for the current writer.

save_mesh_vertices(
coord_prim:pxr.Usd.Prim,
model_name:str,
output_folder:str,
)Create points.xyz file representing vertices of the mesh_prim, defined in the frame of the coord_prim. The points.xyz file will be saved in the output_folder/data/models/model_name/ directory.
Parameters:

- mesh_prim (UsdGeom.Mesh) – mesh prim to get the vertice points.

- coord_prim (Usd.Prim) – prim’s coordinate used to define the vertices with respect to.

- model_name (str) – name of the part to get the vertices of. Note: This corresponds to the name used for the part in the YCB Video Dataset, and is unrelated to the name of the part in the scene.

- output_folder (str) – path of the base output directory.

setup_writer(writer_config:dict)
Initialize writer and attach render product :param config_data: A dictionary containing the general configurations for the script. :param writer_config: A dictionary containing writer-specific configurations.

write(data:dict)
Write function called from the OgnWriter node on every frame to process annotator output.
Parameters:
data – A dictionary containing the annotator data for the current frame.

## Omnigraph Nodes
The extension exposes the following Omnigraph nodes:
