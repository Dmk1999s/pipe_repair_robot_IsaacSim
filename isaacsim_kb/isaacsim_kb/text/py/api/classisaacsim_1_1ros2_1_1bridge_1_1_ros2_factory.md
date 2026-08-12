<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_factory.html | title: Ros2Factory — Isaac Sim -->

# Ros2Factory
Fully qualified name: `isaacsim::ros2::bridge::Ros2Factory`
classRos2Factory

Base class for creating ROS 2 related functions/objects according to the sourced ROS 2 distribution.
This abstract factory class provides an interface for creating various ROS 2 entities such as nodes, publishers, subscribers, and different message types. It serves as a bridge between Isaac Sim and ROS 2, allowing simulation components to communicate with ROS 2 ecosystem.
Implementations of this class handle the specific ROS 2 distribution being used (e.g., Foxy, Humble) while providing a consistent interface for the simulation.
Subclassed by isaacsim::ros2::bridge::Ros2FactoryImpl
Public Functions
virtual~Ros2Factory()=default

Virtual destructor.
Ensures proper cleanup of derived classes when destroyed through a base class pointer.

virtualstd ::shared_ptr<Ros2ContextHandle >createContextHandle()=0

Create a ROS 2 context handler.
Creates and initializes a ROS 2 context which is required for any ROS 2 communication. The context maintains the ROS 2 initialization state and global configuration.
Returns:
Shared pointer to the created context handler.

virtualstd ::shared_ptr<Ros2NodeHandle >createNodeHandle(
constchar*name,
constchar*namespaceName,
Ros2ContextHandle *contextHandle,
)=0
Create a ROS 2 node handler.
Creates a ROS 2 node with the specified name and namespace within the given context. The node is the primary entry point for communication with the ROS 2 graph.
Parameters:

- name – [in] Name of the node.

- namespaceName – [in] Namespace of the node.

- contextHandle – [in] Context handler within which to create the node.

Returns:
Shared pointer to the created node handler.

virtualstd ::shared_ptr<Ros2Publisher >createPublisher(
Ros2NodeHandle *nodeHandle,
constchar*topicName,
constvoid*typeSupport,
constRos2QoSProfile &qos,
)=0
Create a ROS 2 publisher.
Creates a publisher that can send messages of the specified type on the given topic with the specified quality of service settings.
Parameters:

- nodeHandle – [in] Node handler to which the publisher will be attached.

- topicName – [in] Name of the topic to publish on.

- typeSupport – [in] Message type support structure that provides serialization capabilities.

- qos – [in] Quality of service profile that defines communication properties.

Returns:
Shared pointer to the created publisher.

virtualstd ::shared_ptr<Ros2Subscriber >createSubscriber(
Ros2NodeHandle *nodeHandle,
constchar*topicName,
constvoid*typeSupport,
constRos2QoSProfile &qos,
)=0
Create a ROS 2 subscriber.
Creates a subscriber that can receive messages of the specified type from the given topic with the specified quality of service settings.
Parameters:

- nodeHandle – [in] Node handler to which the subscriber will be attached.

- topicName – [in] Name of the topic to subscribe to.

- typeSupport – [in] Message type support structure that provides deserialization capabilities.

- qos – [in] Quality of Service profile that defines communication properties.

Returns:
Shared pointer to the created subscriber.

virtualstd ::shared_ptr<Ros2Service >createService(
Ros2NodeHandle *nodeHandle,
constchar*serviceName,
constvoid*typeSupport,
constRos2QoSProfile &qos,
)=0
Create a ROS 2 service server.
Creates a service server that can receive service requests and provide responses of the specified type on the given service name with the specified quality of service settings.
Parameters:

- nodeHandle – [in] Node handler to which the service server will be attached.

- serviceName – [in] Name of the service.

- typeSupport – [in] Service type support structure that provides serialization/deserialization capabilities.

- qos – [in] Quality of Service profile that defines communication properties.

Returns:
Shared pointer to the created service server.

virtualstd ::shared_ptr<Ros2Client >createClient(
Ros2NodeHandle *nodeHandle,
constchar*serviceName,
constvoid*typeSupport,
constRos2QoSProfile &qos,
)=0
Create a ROS 2 service client.
Creates a service client that can send service requests and receive responses of the specified type to the given service name with the specified quality of service settings.
Parameters:

- nodeHandle – [in] Node handler to which the service client will be attached.

- serviceName – [in] Name of the service.

- typeSupport – [in] Service type support structure that provides serialization/deserialization capabilities.

- qos – [in] Quality of Service profile that defines communication properties.

Returns:
Shared pointer to the created service client.

virtualstd ::shared_ptr<Ros2ClockMessage >createClockMessage()=0

Create a ROS 2 `rosgraph_msgs/msg/Clock` message.
Creates a message that can be used to publish simulation time to ROS 2 clock topics.
Returns:
Shared pointer to the created clock message.

virtualstd ::shared_ptr<Ros2ImuMessage >createImuMessage()=0

Create a ROS 2 `sensor_msgs/msg/Imu` message.
Creates a message that can be used to publish inertial measurement unit data.
Returns:
Shared pointer to the created IMU message.

virtualstd ::shared_ptr<Ros2CameraInfoMessage >createCameraInfoMessage(
)=0
Create a ROS 2 `sensor_msgs/msg/CameraInfo` message.
Creates a message that can be used to publish camera calibration and metadata.
Returns:
Shared pointer to the created camera info message.

virtualstd ::shared_ptr<Ros2ImageMessage >createImageMessage()=0

Create a ROS 2 `sensor_msgs/msg/Image` message.
Creates a message that can be used to publish image data.
Returns:
Shared pointer to the created image message.

virtualstd ::shared_ptr<Ros2NitrosBridgeImageMessage >createNitrosBridgeImageMessage(
)=0
Create a ROS 2 `isaac_ros_nitros_bridge_interfaces/msg/NitrosBridgeImage` message.
Creates a message that can be used for transferring images between NITROS and ROS 2.
Returns:
Shared pointer to the created NITROS bridge image message.

virtualstd ::shared_ptr<Ros2BoundingBox2DMessage >createBoundingBox2DMessage(
)=0
Create a ROS 2 `vision_msgs/msg/Detection2DArray` message.
Creates a message that can be used to publish 2D bounding box detection results.
Returns:
Shared pointer to the created 2D bounding box message.

virtualstd ::shared_ptr<Ros2BoundingBox3DMessage >createBoundingBox3DMessage(
)=0
Create a ROS 2 `vision_msgs/msg/Detection3DArray` message.
Creates a message that can be used to publish 3D bounding box detection results.
Returns:
Shared pointer to the created 3D bounding box message.

virtualstd ::shared_ptr<Ros2OdometryMessage >createOdometryMessage(
)=0
Create a ROS 2 `nav_msgs/msg/Odometry` message.
Creates a message that can be used to publish position and velocity in a global coordinate frame.
Returns:
Shared pointer to the created odometry message.

virtualstd ::shared_ptr<Ros2RawTfTreeMessage >createRawTfTreeMessage(
)=0
Create a ROS 2 `tf2_msgs/msg/TFMessage` message.
Creates a raw transform message that can be used to publish coordinate frame transformations.
Returns:
Shared pointer to the created raw transform tree message.

virtualstd ::shared_ptr<Ros2SemanticLabelMessage >createSemanticLabelMessage(
)=0
Create a ROS 2 `std_msgs/msg/String` message as semantic label.
Creates a message that can be used to publish semantic labels for objects.
Returns:
Shared pointer to the created semantic label message.

virtualstd ::shared_ptr<Ros2JointStateMessage >createJointStateMessage(
)=0
Create a ROS 2 `sensor_msgs/msg/JointState` message.
Creates a message that can be used to publish joint states including position, velocity, and effort.
Returns:
Shared pointer to the created joint state message.

virtualstd ::shared_ptr<Ros2PointCloudMessage >createPointCloudMessage(
)=0
Create a ROS 2 `sensor_msgs/msg/PointCloud2` message.
Creates a message that can be used to publish point cloud data.
Returns:
Shared pointer to the created point cloud message.

virtualstd ::shared_ptr<Ros2LaserScanMessage >createLaserScanMessage(
)=0
Create a ROS 2 `sensor_msgs/msg/LaserScan` message.
Creates a message that can be used to publish laser scan data.
Returns:
Shared pointer to the created laser scan message.

virtualstd ::shared_ptr<Ros2TfTreeMessage >createTfTreeMessage()=0

Create a ROS 2 `tf2_msgs/msg/TFMessage` message.
Creates a transform message that can be used to publish coordinate frame transformations.
Returns:
Shared pointer to the created transform tree message.

virtualstd ::shared_ptr<Ros2TwistMessage >createTwistMessage()=0

Create a ROS 2 `geometry_msgs/msg/Twist` message.
Creates a message that can be used to represent velocity in free space with linear and angular components.
Returns:
Shared pointer to the created twist message.

virtualstd ::shared_ptr<Ros2AckermannDriveStampedMessage >createAckermannDriveStampedMessage(
)=0
Create a ROS 2 `ackermann_msgs/msg/AckermannDriveStamped` message.
Creates a message that can be used to represent an Ackermann steering command with timestamp.
Returns:
Shared pointer to the created Ackermann drive stamped message.

virtualstd ::shared_ptr<Ros2Message >createDynamicMessage(
conststd ::string&pkgName,
conststd ::string&msgSubfolder,
conststd ::string&msgName,
BackendMessageType messageType=BackendMessageType ::eMessage ,
)=0
Create a ROS 2 dynamic message.
Creates a message based on dynamically loaded type information, allowing for handling of message types that may not be known at compile time. This is useful for creating message instances for custom or third-party message types.
Parameters:

- pkgName – [in] Message package name (e.g.: `"std_msgs"` for `std_msgs/msg/Int32`).

- msgSubfolder – [in] Message subfolder name (e.g.: `"msg"` for `std_msgs/msg/Int32`).

- msgName – [in] Message name (e.g.: `"Int32"` for `std_msgs/msg/Int32`).

- messageType – [in] Message type, defaults to eMessage.

Returns:
Shared pointer to the created dynamic message.

virtualboolvalidateTopicName(conststd ::string&topicName)=0

Determine if the given topic name is valid.
Validates a topic name according to ROS 2 naming conventions.
Parameters:
topicName – [in] Topic name to validate.

Returns:
True if the topic name is valid, false otherwise.

virtualboolvalidateNamespaceName(
conststd ::string&namespaceName,
)=0
Determine if the given node namespace name is valid.
Validates a node namespace name according to ROS 2 naming conventions.
Parameters:
namespaceName – [in] Namespace name to validate.

Returns:
True if the node namespace name is valid, false otherwise.

virtualboolvalidateNodeName(conststd ::string&nodeName)=0

Determine if the given node name is valid.
Validates a node name according to ROS 2 naming conventions.
Parameters:
nodeName – [in] Node name to validate.

Returns:
True if the node name is valid, false otherwise.
