<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_publisher.html | title: Ros2Publisher — Isaac Sim -->

# Ros2Publisher
Fully qualified name: `isaacsim::ros2::bridge::Ros2Publisher`
classRos2Publisher

Base class for ROS 2 publishers.
Provides the interface for publishing messages to ROS 2 topics. Publishers are used to send data from the application to other ROS 2 nodes.
Subclassed by isaacsim::ros2::bridge::Ros2PublisherImpl
Public Functions
virtualvoidpublish(constvoid*msg)=0

Sends a message to the topic.
Publishes the provided message to the associated ROS 2 topic.
Parameters:
msg – [in] Pointer to the message to publish.

Pre:
The message must be of the correct type for this publisher.

Pre:
The publisher must be valid (check with isValid() ).

virtualsize_tgetSubscriptionCount()=0

Gets the number of existing subscriptions to the publisher topic.
Queries the ROS 2 middleware to determine how many subscribers are currently connected to this publisher’s topic.
Note
This count may change as nodes join or leave the ROS 2 network.
Returns:
Number of active subscriptions.

virtualboolisValid()=0

Checks whether the publisher is valid.
Verifies if the object holds a properly initialized ROS 2 publisher instance.
Note
A publisher may become invalid if its associated node or context is destroyed.
Returns:
True if the publisher is valid, false otherwise.
