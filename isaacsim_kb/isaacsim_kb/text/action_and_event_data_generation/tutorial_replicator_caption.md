<!-- source: action_and_event_data_generation/tutorial_replicator_caption.html | title: VLM Scene Captioning — Isaac Sim Documentation -->

# VLM Scene Captioning
Vision-language models (VLMs) rely on paired image-caption datasets to learn the complex relationships between visual content and textual descriptions. Captions provide the semantic grounding necessary for models to understand objects, actions, and contexts within images. High-quality captions are essential for training VLMs capable of nuanced scene understanding and reasoning.
Leveraging 3D ground truth from NVIDIA Omniverse transforms the captioning process by enabling detailed, accurate, and scalable annotations. These captions include overall scene descriptions, object relationships, and spatial reasoning, such as relative positions and interactions between elements in a camera view. With 3D metadata, captions can describe not just what is visible but how elements are arranged and interact, offering richer contextual understanding.
This approach ensures more consistent and diverse datasets, allowing VLMs to excel in complex tasks like spatial reasoning and scene analysis, ultimately bridging the gap between visual and linguistic comprehension.
`Isaacsim.Replicator.Caption.Core` (IRC) has the following features:

- Generate image-caption pairs for loaded scenes in Omniverse.

- Plug in to other `Isaacsim.Replicator` modules, including `Isaacsim.replicator.object (IRO)` and `Isaacsim.replicator.agent (IRA)` to generate captions for each frame at their runtime.

- Export scene graphs alongside caption outputs for customized postprocessing and caption preparation.

[image: ../_images/isim_5.0_full_ext-isaacsim.replicator.caption-5.0.0_gui_IRC_demo.png]

## Workflow
`Isaacsim.Replicator.Caption.Core` uses the following workflow to generate captions:
[image: ../_images/isim_5.0_full_ext-isaacsim.replicator.caption-5.0.0_gui_IRC_workflow.png]

### Scene Graph
A scene graph is an intermediate output for caption generation. It is a structured representation of a visual scene, where nodes represent objects and edges denote spatial relationships between them. It captures how elements are arranged in space, such as relative positions and orientations. For example, in an image of a person sitting on a bench under a tree, the graph would include nodes for “person,” “bench,” and “tree,” with edges like “sitting on” and “under.” This spatial focus makes scene graphs valuable for tasks requiring detailed spatial reasoning and scene analysis.
You can export scene graphs alongside caption outputs to enable flexible and customizable management of scene graph data for your specific requirements.

## Enable Isaacsim.Replicator.Caption.Core Extension

- Follow the Omniverse Extension Manager guide to enable the `isaacsim.replicator.caption.core` extension.

- The extension fetches sample assets from Isaac Sim Assets during start. Refer to Isaac Sim Assets if you encounter issues for loading assets.

- If loading the UI appears to be hanging, try starting Isaac Sim with the flag `--/persistent/isaac/asset_root/timeout=1.0`.

- The IRC UI panel is accessible by Tools > Action and Event Data Generation > VLM Scene Captioning and it opens on the right side of the screen.

[image: ../_images/isim_5.0_full_ext-isaacsim.replicator.caption-5.0.0_gui_IRC_start_1.png]IRC can be invoked using the following methods:

- Using the UI panel

- Using the IRA extension

- Using the IRO extension

### Using the UI Panel
To launch scene caption generation with the UI panel:

- After enabling, the extension will appear in the UI panel:
[image: ../_images/isim_5.0_full_ext-isaacsim.replicator.caption-5.0.0_gui_IRC_start_1.png]
- To load the stage USD file, open up the `Caption Settings` panel, and then click on the file selector icon.
[image: ../_images/isim_5.0_full_ext-isaacsim.replicator.caption-5.0.0_gui_IRC_start_2.png]
- Select the USD file you want to caption. There is a default USD file for demonstration.
Note
We include an example USD. You can find it in `[Isaac Sim Assets Path]/Samples/Replicator/Captioning/test_caption.usda`.
`[Isaac Sim Assets Path]` is the path to Isaac Sim Assets Refer to Isaac Sim Assets Check for how to verify the assets access and how to retrieve the asset path.[image: ../_images/isim_5.0_full_ext-isaacsim.replicator.caption-5.0.0_gui_IRC_start_3.png]
- Click on the Load Scene button to load the scene.
[image: ../_images/isim_5.0_full_ext-isaacsim.replicator.caption-5.0.0_gui_IRC_start_4.png]The stage will be loaded in the stage view. If prompted to enable script execution, click Yes.
[image: ../_images/isim_5.0_full_ext-isaacsim.replicator.caption-5.0.0_gui_IRC_start_5.png]
- Enter the LLM model credentials in the API key field of the Model Settings panel; click Accept to continue.
[image: ../_images/isim_5.0_full_ext-isaacsim.replicator.caption-5.0.0_gui_IRC_start_6.png]
- Under the Caption Settings panel, enter the desired caption level – Brief Caption for short and Full Caption for a more elaborate description. Enter the camera prim path in the Input Camera Prim Path field. Input the Output Path to specify where to save the generated captions, the associated scene graphs, and metadata. Ensure the output path is a valid directory. Click Generate Scene Graph.
[image: ../_images/isim_5.0_full_ext-isaacsim.replicator.caption-5.0.0_gui_IRC_start_7.png]Note
The default service URL and model name are provided as a convenience. The services are hosted by NVIDIA and provided free of charge on a trial basis. If the service associated with the default model is not reachable, a different model can be selected. Examples include:

- `meta/llama3-8b-instruct`

- `meta/llama3-70b-instruct`

- `meta/llama-3.1-405b-instruct`

It’s also possible to obtain the NVIDIA NIMs listed on the LLM API reference page and host them locally. Visit NVIDIA’s NIM page for more details.

- The scene graph, the caption, and the corresponding images are generated and saved in the output directory.
[image: ../_images/isim_5.0_full_ext-isaacsim.replicator.caption-5.0.0_gui_IRC_start_8.png]

### Using the IRA Extension
To launch scene caption generation with IRA, load the a YAML configuration file. Or use the default configuration file that comes with the extension and follow the steps below to prepare some environment variables.
The anatomy of an IRC configuration file, used to run the extension under IRA and IRO, is explained.

- Prepare the NIM API key for the extension to use.
The extension requires NIM AI to generate captions. The credentials must be stored in the environment or in the bash shell script. For example, in `~/.bashrc` or `~/.bash_profile`.

```
export NIM_API_KEY=<API_KEY>
```
Note

- The NIM API key has a limited lifetime. The number of free credits is limited and is accessible through the account associated with the API key. After the credits are exhausted, you can apply for more credits through the developer portal. Refer to the developer forum for more details.

- If you only need to generate scene graphs without captions, the AI credentials are not required.

## Example Isaacsim.Replicator.Caption.Core Configuration File
For example, a configuration file is similar to the following:

```
isaacsim.replicator.caption.core:
version: 0.0.9
camera_prim_path: /World/Cameras/Camera
scene_path: USD_FILE
caption_configs:
save_full_scene_graph: true
save_pruned_scene_graph: true
attach_label_to_usd: false
use_ai_label: false
visualize_caption: true
max_object_capacity: 100
export_edges: true
global_caption: true
qa_caption: false
brief_caption: true
pruning_ratio: 1.0
verbose: true
random_seed: 0
caption_only: false
export_world: true
output_path: OUTPUT_PATH
```

### Global Properties
versionThe version of IRC extension. If version does not match, the extension will not work.
camera_prim_pathThe path to the camera prim in the scene. If not provided, the extension uses the default camera path defined in the `default_config.yaml` file. However, if there is no camera in the scene, the extension will not work. You must guarantee that the camera is available in the scene.
scene_pathThe path to the scene USD file. The extension can load the scene from this path. However, if the `scene_path` is not provided, the extension uses whatever scene is loaded in the app. If no scene is loaded, the extension will not work.
output_pathThe path to the output directory where the generated captions will be saved. If not provided, the extension will use the default output path.

### Caption Configurations
save_full_scene_graphIf True, it will save the full scene graph in the output directory.
The file will be saved as `<output_path>/<Camera Prim Name>/Captions/full_scene_graph.json`.
save_pruned_scene_graphIf True, it will save the pruned scene graph in the output directory. The full scene graph includes the edges between any two objects at the same level in the Support Tree.
The file will be saved as `<output_path>/<Camera Prim Name>/Captions/pruned_scene_graph.json`.
Note
Support Tree: A tree that represents the spatial relationships between objects in the scene. The root of the tree is the floor (0th level). The direct children of the root are the objects on the floor, which is considered the 1st level. The objects on the 2nd level are the objects supported by the objects on the 1st level, and so on.
pruning_ratioThe ratio of the scene graph to be pruned. The scene graph will be pruned to a Minimum Spanning Tree (MST). The pruning ratio determines the percentage of the MST edges to be kept. For example, if `pruning_ratio` is set to `0.5`, the scene graph is pruned to 50% of the MST edges.
By default, `pruning_ratio` is set to `1.0`, which means the scene graph will not be further pruned after the MST is generated.
random_seedAn integer for the random process. When `pruning_ratio` is less than `1.0`, the edges will be randomly removed from the MST. The random seed is used to control the randomness of this process.
attach_label_to_usdIf True, it will attach the automatically generated semantic labels to all prims with an USD address in the scene, if the prim does not have a semantic label pre-attached. The automatic semantic label is based on the prim path basename. For example, if the prim path is `/World/Objects/Chair`, the semantic label will be `Chair`.
With semantic label attached, Omniverse annotators are able to capture the prim for the annotation defined. This is critical for captioning tasks, because prims not captured by annotators cannot be included in the scene graph and therefore will not be captioned.
use_ai_labelIf True, it will use the AI-generated labels for the prims with semantic labels in the scene. The AI-generated labels are preprocessed and stored in the database, and they will be pulled from the database at runtime. This function can be combined with `attach_label_to_usd: true` to handle the case when target prims does not have semantic labels pre-stored in the scene file.
visualize_captionIf True, it will visualize the scene graph on the output images. The visualization will be saved as <output_path>/<Camera Prim Name>/Captions/vis_camera_scene_graph.jpg.
max_object_capacityThe maximum number of objects that the scene graph can contain. The objects are selected by their 2D bounding box sizes in the camera view in a reverse order.
export_edgesIf True, the edges of the scene graph will be exported to scene graph files. The edges represent the spatial relationships between objects.
export_worldIf True, the extension will export 3D World locations of the prims in the scene graph, and save them in the scene graph files. The 3D World locations are the 3D coordinates of the prims in the world space. If not mentioned, all other locations are in the camera space.
global_captionIf True, the extension will generate a global caption for the scene. The global caption describes the overall scene content and context. This will be saved in the output file `<output_path>/<Camera Prim Name>/Captions/scene_graph_caption.json`.
qa_captionIf True, the extension will generate QA captions for the scene. The QA captions are questions and answers that test the model’s understanding of the scene.
This will be saved in the output file `<output_path>/<Camera Prim Name>/Captions/scene_graph_caption.json`.
brief_captionIf True, the extension will generate brief captions for the scene. The brief captions are the short version of the global caption. This will be saved in the output file `<output_path>/<Camera Prim Name>/Captions/scene_graph_caption.json`.
verboseIf True, the extension will print the detailed information of the scene graph generation process, such as the `support tree`, and the number of nodes and edges in the scene graph.
caption_onlyIf True, only the prims whose corresponding USD files have their object caption preprocessed and stored in the database will be included in the scene graph and following caption generation process.

## Use IRC in Isaacsim.Replicator.Agent
Isaacsim.replicator.agent (IRA) is a module that generates synthetic data on human characters and robots across a variety of 3D environments. With the IRC extension enabled in IRA, you can generate captions for each frame at the same time.
To use IRC in IRA:

- In the IRA configuration file, use IRC’s `SceneGraphWriter` to write the captions to the output directory.
Example:

```
isaacsim.replicator.agent:
version: 0.0.9
agent_configs:
...
replicator:
writer: SceneGraphWriter
parameters:
output_dir: OUTPUT_PATH
caption_config:
pruning_ratio: 1.0
global_caption: true
qa_caption: false
brief_caption: true
export_edges: true
visualize_caption: true
max_object_capacity: 100
save_full_scene_graph: false
save_pruned_scene_graph: true
export_world: false
attach_label_to_usd: false
caption_only: false
use_ai_label: false
verbose: true
random_seed: 0
caption_interval: 1000
scene_graph_interval: 1
skip_frames: 0
writer_interval: 1
export_point_cloud: false
export_depth: false
```
The `caption_config` field is the same as the one in the IRC configuration file. The caption output will be stored in the output directory as:

- pruned scene graph: `<output_dir>/<Camera Prim Name>/caption_pruned_json/scene_graph_pruned_<frame id>.json`

- full scene graph: `<output_dir>/<Camera Prim Name>/caption_full_json/scene_graph_full_<frame id>.json`

- visualized scene graph: `<output_dir>/<Camera Prim Name>/caption_rgb/rgb_<frame id>.jpg`

- captions: `<output_dir>/<Camera Prim Name>/caption/caption_<frame id>.json`

Below are the other parameters in the `SceneGraphWriter`:
output_dirThe path to the output directory where the generated captions as well as IRA outputs will be saved. If not provided, the extension will use the default output path.
caption_intervalThe interval of the caption generation process. The caption will be generated every `caption_interval` frames. By default, `caption_interval` is set to `1000`.
scene_graph_intervalThe interval of the scene graph generation process. The scene graph will be generated every `scene_graph_interval` frames. By default, `scene_graph_interval` is set to `1`.
skip_framesThe number of frames to skip before starting the caption generation process. By default, `skip_frames` is set to `0`.
writer_intervalThe interval of the writer process. The writer will write the IRA outputs to the output directory every `writer_interval` frames. By default, `writer_interval` is set to `1`.
export_point_cloudIf True, the extension will export the point cloud of the frame. The point cloud will be saved in the output directory because `<output_dir>/<Camera Prim Name>/pointcloud/pointcloud_<frame id>.npy`. By default, `export_point_cloud` is set to False.
export_depthIf True, the extension will export the depth map of the frame. The depth map will be saved in the output directory as `<output_dir>/<Camera Prim Name>/depth/depth_<frame id>.npy`. By default, `export_depth` is set to False.

- Follow the steps in the Isaacsim.replicator.agent tutorial to start the data generation process.

## Use IRC in Isaacsim.Replicator.Object
Isaacsim.replicator.object (IRO) is a module that composes scenes that are uniquely domain randomized. With the IRC extension enabled in IRC, you can generate captions for each frame at the same time.
To enable IRC in IRO:

- In the IRO configuration file, use IRC’s `CombinedIROSceneGraphWriter` to write the IRO output together with captions to the output directory.
Example:

```
isaacsim.replicator.object:
version: 0.4.x
camera_parameters: ...
caption_configs:
save_full_scene_graph: true
save_pruned_scene_graph: true
attach_label_to_usd: false
use_ai_label: false
visualize_caption: true
max_object_capacity: 100
export_edges: true
caption_only: false
global_caption: true
qa_caption: true
brief_caption: true
pruning_ratio: 1.0
verbose: true
random_seed: 0
caption_writer: CombinedIROSceneGraphWriter
output_switches:
caption: True
...
```
In the `caption_configs` field, the configurations are the same as in the IRC configuration file, with one additional field `caption_writer`.
caption_writerThe writer to write the captions to the output directory. The available writers are:

- `CombinedIROSceneGraphWriter`: This writer combines the IRO outputs with the captions.

- `IROSceneGraphWriter`: This writer only writes the captions to the output directory while suppressing other
IRO outputs, such as `labels` (The 2D detection labels). However, it can generate `images`, `distance_to_image_plane` and `pointcloud`.

The caption output will be stored in the output directory as:

- pruned scene graph: `<output_dir>/caption/caption_pruned_json/<seed>_<camera_name>.json`

- full scene graph: `<output_dir>/caption/caption_full_json/<seed>_<camera_name>.json`

- visualized scene graph: `<output_dir>/caption_rgb/<seed>_<camera_name>.jpg`

- captions: `<output_dir>/<Camera Prim Name>/caption_dict/<seed>_<camera_name>.json`

- Follow the steps in the Isaacsim.replicator.object tutorial to start the data generation process.
