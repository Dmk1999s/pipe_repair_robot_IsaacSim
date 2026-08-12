<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_subscriber.html | title: Ros2Subscriber — Isaac Sim -->

# Ros2Subscriber
Fully qualified name: `isaacsim::ros2::bridge::Ros2Subscriber`
classRos2Subscriber

Base class for ROS 2 subscribers.
Provides the interface for subscribing to messages from ROS 2 topics. Subscribers receive data published by other ROS 2 nodes.
Subclassed by isaacsim::ros2::bridge::Ros2SubscriberImpl
Public Functions
virtualboolspin(void*msg)=0

Processes incoming messages from the topic.
Checks for and retrieves any available messages from the subscription queue. If a message is available, it is copied into the provided message structure.
Parameters:
msg – [out] Pointer to store the received message.

Returns:
True if a message was received, false otherwise.

Pre:
The msg pointer must point to a valid message structure of the correct type.

Pre:
The subscriber must be valid (check with isValid() ).

virtualboolisValid()=0

Checks whether the subscriber is valid.
Verifies if the object holds a properly initialized ROS 2 subscriber instance.
Note
A subscriber may become invalid if its associated node or context is destroyed.
Returns:
True if the subscriber is valid, false otherwise.
