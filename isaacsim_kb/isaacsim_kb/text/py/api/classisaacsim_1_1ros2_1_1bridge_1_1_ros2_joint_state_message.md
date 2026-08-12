<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_joint_state_message.html | title: Ros2JointStateMessage — Isaac Sim -->

# Ros2JointStateMessage
Fully qualified name: `isaacsim::ros2::bridge::Ros2JointStateMessage`
classRos2JointStateMessage:publicisaacsim ::ros2 ::bridge ::Ros2Message

Class implementing a `sensor_msgs/msg/JointState` message.
Provides functionality to read and write ROS 2 JointState messages that contain joint positions, velocities, and efforts for articulated mechanisms.
Subclassed by isaacsim::ros2::bridge::Ros2JointStateMessageImpl
Public Functions
virtualvoidwriteData(
constdouble&timeStamp,
omni ::physics ::tensors ::IArticulationView*articulation,
pxr ::UsdStageWeakPtrstage,
std ::vector<float>&jointPositions,
std ::vector<float>&jointVelocities,
std ::vector<float>&jointEfforts,
std ::vector<uint8_t>&dofTypes,
constdouble&stageUnits,
)=0
Write the message field values from the given arguments.
Sets the joint names, positions, velocities, efforts, and timestamp in a ROS 2 JointState message.
Parameters:

- timeStamp – [in] Time (seconds).

- articulation – [in] Articulation handler.

- stage – [in] USD stage.

- jointPositions – [in] Joint positions.

- jointVelocities – [in] Joint velocities.

- jointEfforts – [in] Joint efforts.

- dofTypes – [in] Articulation DOF types.

- stageUnits – [in] Unit scale of the stage.

virtualvoidreadData(
std ::vector<char*>&jointNames,
double*jointPositions,
double*jointVelocities,
double*jointEfforts,
double&timeStamp,
)=0
Read the message field values.
Extracts joint names, positions, velocities, efforts, and timestamp from a ROS 2 JointState message.
The size of the arrays to store the joint positions, velocities, and efforts must be equal to the number of joints (see Ros2JointStateMessage::getNumJoints ) of the message before calling this method.
Parameters:

- jointNames – [out] Joint names.

- jointPositions – [out] Joint positions.

- jointVelocities – [out] Joint velocities.

- jointEfforts – [out] Joint efforts.

- timeStamp – [out] Time (seconds).

virtualsize_tgetNumJoints()=0

Get the number of joints in the message.
Returns the number of joints in the message, derived from the size of the `name` field array.
Returns:
Number of joints.

virtualboolcheckValid()=0

Check that the message field arrays have the same size.
Verifies that the joint names, positions, velocities, and efforts arrays all have the same size, indicating a valid message.
Returns:
Whether the message field arrays have the same size.

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
