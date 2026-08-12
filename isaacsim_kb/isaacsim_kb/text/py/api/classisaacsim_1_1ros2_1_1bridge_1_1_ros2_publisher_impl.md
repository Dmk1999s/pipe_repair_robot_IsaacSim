<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_publisher_impl.html | title: Ros2PublisherImpl — Isaac Sim -->

# Ros2PublisherImpl
Fully qualified name: `isaacsim::ros2::bridge::Ros2PublisherImpl`
classRos2PublisherImpl:publicisaacsim ::ros2 ::bridge ::Ros2Publisher

Implementation of ROS 2 Publisher.
Manages a ROS 2 publisher instance, providing functionality for publishing messages and monitoring subscriber count.
Public Functions
Ros2PublisherImpl(
Ros2NodeHandle *nodeHandle,
constchar*topicName,
constvoid*typeSupport,
constRos2QoSProfile &qos,
)
Constructor for ROS 2 Publisher implementation.
Parameters:

- nodeHandle – [in] Pointer to the ROS 2 node handle.

- topicName – [in] Name of the topic to publish on.

- typeSupport – [in] Type support handle for the message type.

- qos – [in] Quality of Service settings for the publisher.

virtual~Ros2PublisherImpl()

virtualvoidpublish(constvoid*msg)

Sends a message to the topic.
Publishes the provided message to the associated ROS 2 topic.
Parameters:
msg – [in] Pointer to the message to publish.

Pre:
The message must be of the correct type for this publisher.

Pre:
The publisher must be valid (check with isValid() ).

virtualsize_tgetSubscriptionCount()

Gets the number of existing subscriptions to the publisher topic.
Queries the ROS 2 middleware to determine how many subscribers are currently connected to this publisher’s topic.
Note
This count may change as nodes join or leave the ROS 2 network.
Returns:
Number of active subscriptions.

inlinevirtualboolisValid()

Checks whether the publisher is valid.
Verifies if the object holds a properly initialized ROS 2 publisher instance.
Note
A publisher may become invalid if its associated node or context is destroyed.
Returns:
True if the publisher is valid, false otherwise.
