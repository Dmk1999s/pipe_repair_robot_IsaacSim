<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_subscriber_impl.html | title: Ros2SubscriberImpl — Isaac Sim -->

# Ros2SubscriberImpl
Fully qualified name: `isaacsim::ros2::bridge::Ros2SubscriberImpl`
classRos2SubscriberImpl:publicisaacsim ::ros2 ::bridge ::Ros2Subscriber

Implementation of ROS 2 Subscriber.
Manages a ROS 2 subscriber instance, providing functionality for receiving and processing messages.
Public Functions
Ros2SubscriberImpl(
Ros2NodeHandle *nodeHandle,
constchar*topicName,
constvoid*typeSupport,
constRos2QoSProfile &qos,
)
Constructor for ROS 2 Subscriber implementation.
Parameters:

- nodeHandle – [in] Pointer to the ROS 2 node handle.

- topicName – [in] Name of the topic to subscribe to.

- typeSupport – [in] Type support handle for the message type.

- qos – [in] Quality of Service settings for the subscriber.

virtual~Ros2SubscriberImpl()

virtualboolspin(void*msg)

Processes incoming messages.
Parameters:
msg – [out] Pointer to store the received message

Returns:
bool True if a message was received and processed

inlinevirtualboolisValid()

Checks if the subscriber is valid.
Returns:
bool True if the subscriber is properly initialized
