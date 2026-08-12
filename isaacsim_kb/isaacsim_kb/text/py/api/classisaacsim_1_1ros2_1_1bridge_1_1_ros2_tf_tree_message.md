<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_tf_tree_message.html | title: Ros2TfTreeMessage — Isaac Sim -->

# Ros2TfTreeMessage
Fully qualified name: `isaacsim::ros2::bridge::Ros2TfTreeMessage`
classRos2TfTreeMessage:publicisaacsim ::ros2 ::bridge ::Ros2Message

Class implementing a `tf2_msgs/msg/TFMessage` message.
Provides functionality to read and write ROS 2 TFMessage messages that contain multiple transforms between coordinate frames.
Subclassed by isaacsim::ros2::bridge::Ros2TfTreeMessageImpl
Public Functions
virtualvoidwriteData(
constdouble&timeStamp,
std ::vector<TfTransformStamped >&transforms,
)=0
Write the message field values from the given arguments.
Sets the transforms in a ROS 2 TFMessage message with multiple transforms.
Parameters:

- timeStamp – [in] Time (seconds).

- transforms – [in] Transforms.

virtualvoidreadData(
std ::vector<TfTransformStamped >&transforms,
)=0
Read the message field values.
Extracts transform data from a ROS 2 TFMessage message.
Parameters:
transforms – [out] Transforms.

inlinevoid*getPtr()

Retrieves the message pointer.
Returns the pointer to the underlying ROS 2 message if it has been properly created and initialized.
Note
This method does not perform type checking - the caller is responsible for proper casting to the appropriate message type.
Returns:
Pointer to the message or nullptr if not initialized.

virtualconstvoid*getTypeSupportHandle()=0

Gets the type support handle for the message.
Returns a pointer to the ROS IDL message type support data structure. The actual type depends on the message category:

- Topic: rosidl_message_type_support_t

- Service: rosidl_service_type_support_t

- Action: rosidl_action_type_support_t

Returns:
Pointer to the type support structure or nullptr.

Protected Attributes
void*m_msg=nullptr

Message pointer.
