<!-- source: py/api/classisaacsim_1_1ros2_1_1tf__viewer_1_1_ros2_buffer_core.html | title: Ros2BufferCore — Isaac Sim -->

# Ros2BufferCore
Fully qualified name: `isaacsim::ros2::tf_viewer::Ros2BufferCore`
classRos2BufferCore

Class that partially implements a tf2 `BufferCore`.
This abstract class provides an interface for tf2 buffer operations such as setting transforms, retrieving transforms, and querying frame information. It serves as a compatibility layer for working with ROS 2 tf2 functionality.
Subclassed by isaacsim::ros2::tf_viewer::Ros2BufferCoreImpl
Public Functions
virtualboolsetTransform(
void*msg,
conststd ::string&authority,
boolisStatic,
)=0
Adds a transform information to the buffer.
This function takes a ROS TFMessage and stores the transform information in the buffer for later retrieval.
Parameters:

- msg – [in]`TFMessage` message pointer.

- authority – [in] The source of the information for the transform.

- isStatic – [in] Whether to record the transform as static (the transform will be good across all time).

Returns:
Whether the transform has been added successfully.

virtualboolgetTransform(
conststd ::string&targetFrame,
conststd ::string&sourceFrame,
doubletranslation[],
doublerotation[],
)=0
Gets the transform between two frames at the ROS zero time.
Calculates and retrieves the coordinate transformation between two frames in the tf tree at the ROS zero time.
Parameters:

- targetFrame – [in] Frame ID to which data should be transformed.

- sourceFrame – [in] Frame ID where the data originated.

- translation – [out] Buffer to store the Cartesian translation. Buffer length should be 3.

- rotation – [out] Buffer to store the rotation (as quaternion: xyzw). Buffer length should be 4.

Returns:
Whether the transform has been computed without exceptions.

virtualboolgetParentFrame(
conststd ::string&frame,
std ::string&parentFrame,
)=0
Gets the parent frame of the specified frame at the ROS zero time.
Retrieves the parent frame ID for a given frame in the tf tree.
Parameters:

- frame – [in] Frame ID to search for.

- parentFrame – [out] Reference in which the parent frame ID will be stored.

Returns:
True if a parent exists, false otherwise.

virtualstd ::vector<std ::string>getFrames()=0

Gets the available frame IDs.
Retrieves a list of all frame IDs currently available in the tf tree.
Returns:
A list of available frame IDs.

virtualvoidclear()=0

Clears all buffer data.
Removes all transformations and frames from the buffer.
