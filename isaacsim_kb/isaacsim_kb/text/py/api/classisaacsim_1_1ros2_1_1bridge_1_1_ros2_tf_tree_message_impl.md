<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_tf_tree_message_impl.html | title: Ros2TfTreeMessageImpl — Isaac Sim -->

# Ros2TfTreeMessageImpl
Fully qualified name: `isaacsim::ros2::bridge::Ros2TfTreeMessageImpl`
classRos2TfTreeMessageImpl:publicisaacsim ::ros2 ::bridge ::Ros2TfTreeMessage ,privateisaacsim ::ros2 ::bridge ::Ros2MessageInterfaceImpl

Implementation of ROS 2 Transform Tree message.
Handles the creation and manipulation of tf2_msgs/msg/TFMessage messages, which contain multiple coordinate frame transforms.
Public Functions
Ros2TfTreeMessageImpl()

virtual~Ros2TfTreeMessageImpl()

virtualconstvoid*getTypeSupportHandle()

Gets the type support handle for the message.
Returns a pointer to the ROS IDL message type support data structure. The actual type depends on the message category:

- Topic: rosidl_message_type_support_t

- Service: rosidl_service_type_support_t

- Action: rosidl_action_type_support_t

Returns:
Pointer to the type support structure or nullptr.

virtualvoidwriteData(
constdouble&timeStamp,
std ::vector<TfTransformStamped >&transforms,
)
Sets the transform tree data.
Parameters:

- timeStamp – [in] Time in seconds

- transforms – [in] Vector of transform data

virtualvoidreadData(std ::vector<TfTransformStamped >&transforms)

Reads the transform tree data.
Parameters:
transforms – [out] Vector to store transform data

inlinevoid*getPtr()

Retrieves the message pointer.
Returns the pointer to the underlying ROS 2 message if it has been properly created and initialized.
Note
This method does not perform type checking - the caller is responsible for proper casting to the appropriate message type.
Returns:
Pointer to the message or nullptr if not initialized.

Protected Attributes
void*m_msg=nullptr

Message pointer.
