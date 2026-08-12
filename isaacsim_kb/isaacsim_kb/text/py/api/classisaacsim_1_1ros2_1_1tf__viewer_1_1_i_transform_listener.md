<!-- source: py/api/classisaacsim_1_1ros2_1_1tf__viewer_1_1_i_transform_listener.html | title: ITransformListener — Isaac Sim -->

# ITransformListener
Fully qualified name: `isaacsim::ros2::tf_viewer::ITransformListener`
classITransformListener

ROS 2 transform listener interface.
Interface for a listener that subscribes to ROS 2 transform messages (tf) and provides methods to retrieve and manipulate transformation data. This interface allows for integration with the ROS 2 tf2 system.
Public Functions
virtualboolinitialize(conststd ::string&rosDistro)=0

Initializes the transform listener by loading the adequate ROS 2 plugin and creating the tf2 buffer.
This method loads the appropriate ROS 2 plugin based on the specified distribution and sets up the necessary tf2 buffer for transform handling.
Parameters:
rosDistro – [in] The ROS 2 distribution name to use for initialization.

Returns:
Whether the transform listener was initialized successfully.

virtualvoidfinalize()=0

Finalizes subscriptions to the tf (if any) and resets ROS 2 node.
Cleans up resources and disconnects from the ROS 2 system.

virtualboolspin()=0

Processes transform listener to record incoming tf transforms.
This method should be called regularly to process incoming transform messages and update the internal buffer.
Returns:
True if the tf messages have been processed without error, false otherwise.

virtualvoidreset()=0

Resets the internal buffer by clearing its data.
Removes all stored transforms from the internal buffer.

virtualvoidcomputeTransforms(conststd ::string&rootFrame)=0

Computes all transforms with respect to the specified (root) frame.
Calculates the transformation data for all available frames relative to the specified root frame. This data can then be retrieved using other methods.
Parameters:
rootFrame – [in] Frame ID on which to compute transforms.

virtualconststd ::vector<std ::string>&getFrames()=0

Gets the available frame IDs.
Retrieves the list of all available frame IDs in the tf tree. It is necessary to call the computeTransforms method first before invoking this one to obtain updated data.
Returns:
A list of available frame IDs.

virtualconststd ::vector<std ::tuple<std ::string,std ::string>>&getRelations(
)=0
Gets the relations between available frame IDs.
Retrieves the parent-child relationships between frames in the tf tree. It is necessary to call the computeTransforms method first before invoking this one to obtain updated data.
Returns:
A list of relation-pairs between frame IDs (parent-child tuples).

virtualconststd ::unordered_map<std ::string,std ::tuple<std ::tuple<double,double,double>,std ::tuple<double,double,double,double>>>&getTransforms(
)=0
Gets the transforms of the available frame IDs with respect to the specified (root) frame.
Retrieves the transformation data (translation and rotation) for each frame relative to the root frame specified in the last call to computeTransforms. It is necessary to call the computeTransforms method first before invoking this one to obtain updated data.
Returns:
A map of transforms (translation: xyz, rotation: xyzw) for each frame ID.
