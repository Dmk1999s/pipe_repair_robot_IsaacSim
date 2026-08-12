<!-- source: py/api/classisaacsim_1_1ros2_1_1tf__viewer_1_1_ros2_buffer_core_impl.html | title: Ros2BufferCoreImpl — Isaac Sim -->

# Ros2BufferCoreImpl
Fully qualified name: `isaacsim::ros2::tf_viewer::Ros2BufferCoreImpl`
classRos2BufferCoreImpl:publicisaacsim ::ros2 ::tf_viewer ::Ros2BufferCore

Implementation of ROS 2 Transform Buffer Core.
Manages a transform buffer that stores and maintains the transform tree, providing functionality to set and query transforms between different coordinate frames.
Public Functions
Ros2BufferCoreImpl()

Constructor for ROS 2 Buffer Core implementation.

virtual~Ros2BufferCoreImpl()

Virtual destructor.

virtualboolsetTransform(
void*msg,
conststd ::string&authority,
boolisStatic,
)
Sets a transform in the buffer.
Parameters:

- msg – [in] Pointer to the transform message.

- authority – [in] Name of the authority setting the transform.

- isStatic – [in] Whether the transform is static (unchanging).

Returns:
True if transform was successfully set.

virtualboolgetTransform(
conststd ::string&targetFrame,
conststd ::string&sourceFrame,
doubletranslation[],
doublerotation[],
)
Gets the transform between two frames.
Parameters:

- targetFrame – [in] Name of the target frame.

- sourceFrame – [in] Name of the source frame.

- translation – [out] Array to store the translation components [x, y, z].

- rotation – [out] Array to store the rotation components [x, y, z, w].

Returns:
True if transform was successfully retrieved.

virtualboolgetParentFrame(
conststd ::string&frame,
std ::string&parentFrame,
)
Gets the parent frame of a given frame.
Parameters:

- frame – [in] Name of the frame to query.

- parentFrame – [out] Name of the parent frame.

Returns:
True if parent frame was successfully retrieved.

virtualstd ::vector<std ::string>getFrames()

Gets a list of all frames in the buffer.
Returns:
Vector of frame names.

virtualvoidclear()

Clears all transforms from the buffer.
