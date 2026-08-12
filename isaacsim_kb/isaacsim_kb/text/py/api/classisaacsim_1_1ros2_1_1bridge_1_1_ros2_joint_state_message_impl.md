<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_joint_state_message_impl.html | title: Ros2JointStateMessageImpl — Isaac Sim -->

# Ros2JointStateMessageImpl
Fully qualified name: `isaacsim::ros2::bridge::Ros2JointStateMessageImpl`
classRos2JointStateMessageImpl:publicisaacsim ::ros2 ::bridge ::Ros2JointStateMessage ,privateisaacsim ::ros2 ::bridge ::Ros2MessageInterfaceImpl

Implementation of ROS 2 Joint State message.
Handles the creation and manipulation of sensor_msgs/msg/JointState messages, which contain robot joint positions, velocities, and efforts.
Public Functions
Ros2JointStateMessageImpl()

virtual~Ros2JointStateMessageImpl()

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
omni ::physics ::tensors ::IArticulationView*articulation,
pxr ::UsdStageWeakPtrstage,
std ::vector<float>&jointPositions,
std ::vector<float>&jointVelocities,
std ::vector<float>&jointEfforts,
std ::vector<uint8_t>&dofTypes,
constdouble&stageUnits,
)
Sets the joint state data.
Parameters:

- timeStamp – [in] Time in seconds

- articulation – [in] Pointer to articulation view

- stage – [in] USD stage pointer

- jointPositions – [in] Vector of joint positions

- jointVelocities – [in] Vector of joint velocities

- jointEfforts – [in] Vector of joint efforts

- dofTypes – [in] Vector of DOF types

- stageUnits – [in] Stage unit scale factor

virtualvoidreadData(
std ::vector<char*>&jointNames,
double*jointPositions,
double*jointVelocities,
double*jointEfforts,
double&timeStamp,
)
Reads the joint state data.
Parameters:

- jointNames – [out] Vector of joint names

- jointPositions – [out] Array of joint positions

- jointVelocities – [out] Array of joint velocities

- jointEfforts – [out] Array of joint efforts

- timeStamp – [out] Time in seconds

virtualsize_tgetNumJoints()

Gets the number of joints in the message.
Returns:
size_t Number of joints

virtualboolcheckValid()

Validates the joint state message.
Returns:
bool True if the message is valid

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
