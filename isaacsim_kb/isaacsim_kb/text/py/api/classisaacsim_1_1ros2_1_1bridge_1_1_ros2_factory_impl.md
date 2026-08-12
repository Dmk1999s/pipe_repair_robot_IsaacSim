<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_factory_impl.html | title: Ros2FactoryImpl — Isaac Sim -->

# Ros2FactoryImpl
Fully qualified name: `isaacsim::ros2::bridge::Ros2FactoryImpl`
classRos2FactoryImpl:publicisaacsim ::ros2 ::bridge ::Ros2Factory

Concrete implementation of the ROS 2 factory interface.
Implements the Ros2Factory interface to provide creation methods for all ROS 2 entities used in the Isaac Sim bridge. This includes context handlers, node handlers, communication primitives, and various message types.
Public Functions
virtualstd ::shared_ptr<Ros2ContextHandle >createContextHandle()

Creates a new ROS 2 context handle.
Returns:
std::shared_ptr<Ros2ContextHandle> Pointer to the created context handle

virtualstd ::shared_ptr<Ros2NodeHandle >createNodeHandle(
constchar*name,
constchar*namespaceName,
Ros2ContextHandle *contextHandle,
)
Creates a new ROS 2 node handle.
Parameters:

- name – [in] Name of the node

- namespaceName – [in] Namespace for the node

- contextHandle – [in] Pointer to the context handle for this node

Returns:
std::shared_ptr<Ros2NodeHandle> Pointer to the created node handle

virtualstd ::shared_ptr<Ros2Publisher >createPublisher(
Ros2NodeHandle *nodeHandle,
constchar*topicName,
constvoid*typeSupport,
constRos2QoSProfile &qos,
)
Creates a new ROS 2 publisher.
Parameters:

- nodeHandle – [in] Pointer to the node handle that will own this publisher

- topicName – [in] Name of the topic to publish to

- typeSupport – [in] Type support handle for the message type

- qos – [in] Quality of Service settings for the publisher

Returns:
std::shared_ptr<Ros2Publisher> Pointer to the created publisher

virtualstd ::shared_ptr<Ros2Subscriber >createSubscriber(
Ros2NodeHandle *nodeHandle,
constchar*topicName,
constvoid*typeSupport,
constRos2QoSProfile &qos,
)
Creates a new ROS 2 subscriber.
Parameters:

- nodeHandle – [in] Pointer to the node handle that will own this subscriber

- topicName – [in] Name of the topic to subscribe to

- typeSupport – [in] Type support handle for the message type

- qos – [in] Quality of Service settings for the subscriber

Returns:
std::shared_ptr<Ros2Subscriber> Pointer to the created subscriber

virtualstd ::shared_ptr<Ros2Service >createService(
Ros2NodeHandle *nodeHandle,
constchar*serviceName,
constvoid*typeSupport,
constRos2QoSProfile &qos,
)
Creates a new ROS 2 service server.
Parameters:

- nodeHandle – [in] Pointer to the node handle that will own this service

- serviceName – [in] Name of the service

- typeSupport – [in] Type support handle for the service type

- qos – [in] Quality of Service settings for the service

Returns:
std::shared_ptr<Ros2Service> Pointer to the created service server

virtualstd ::shared_ptr<Ros2Client >createClient(
Ros2NodeHandle *nodeHandle,
constchar*serviceName,
constvoid*typeSupport,
constRos2QoSProfile &qos,
)
Creates a new ROS 2 service client.
Parameters:

- nodeHandle – [in] Pointer to the node handle that will own this client

- serviceName – [in] Name of the service to connect to

- typeSupport – [in] Type support handle for the service type

- qos – [in] Quality of Service settings for the client

Returns:
std::shared_ptr<Ros2Client> Pointer to the created service client

virtualstd ::shared_ptr<Ros2ClockMessage >createClockMessage()

Creates a Clock message.

virtualstd ::shared_ptr<Ros2ImuMessage >createImuMessage()

Creates an IMU message.

virtualstd ::shared_ptr<Ros2CameraInfoMessage >createCameraInfoMessage(
)
Creates a Camera Info message.

virtualstd ::shared_ptr<Ros2ImageMessage >createImageMessage()

Creates an Image message.

virtualstd ::shared_ptr<Ros2NitrosBridgeImageMessage >createNitrosBridgeImageMessage(
)
Creates a Nitros Bridge Image message.

virtualstd ::shared_ptr<Ros2BoundingBox2DMessage >createBoundingBox2DMessage(
)
Creates a 2D Bounding Box message.

virtualstd ::shared_ptr<Ros2BoundingBox3DMessage >createBoundingBox3DMessage(
)
Creates a 3D Bounding Box message.

virtualstd ::shared_ptr<Ros2OdometryMessage >createOdometryMessage(
)
Creates an Odometry message.

virtualstd ::shared_ptr<Ros2RawTfTreeMessage >createRawTfTreeMessage(
)
Creates a Raw Transform Tree message.

virtualstd ::shared_ptr<Ros2SemanticLabelMessage >createSemanticLabelMessage(
)
Creates a Semantic Label message.

virtualstd ::shared_ptr<Ros2JointStateMessage >createJointStateMessage(
)
Creates a Joint State message.

virtualstd ::shared_ptr<Ros2PointCloudMessage >createPointCloudMessage(
)
Creates a Point Cloud message.

virtualstd ::shared_ptr<Ros2LaserScanMessage >createLaserScanMessage(
)
Creates a Laser Scan message.

virtualstd ::shared_ptr<Ros2TfTreeMessage >createTfTreeMessage()

Creates a Transform Tree message.

virtualstd ::shared_ptr<Ros2TwistMessage >createTwistMessage()

Creates a Twist message.

virtualstd ::shared_ptr<Ros2AckermannDriveStampedMessage >createAckermannDriveStampedMessage(
)
Creates an Ackermann Drive Stamped message.

virtualstd ::shared_ptr<Ros2Message >createDynamicMessage(
conststd ::string&pkgName,
conststd ::string&msgSubfolder,
conststd ::string&msgName,
BackendMessageType messageType=BackendMessageType ::eMessage ,
)
Creates a dynamic message type at runtime.
Parameters:

- pkgName – [in] Name of the ROS 2 package containing the message definition

- msgSubfolder – [in] Subfolder containing the message definition (msg, srv, action)

- msgName – [in] Name of the message type

- messageType – [in] Type of the message (topic, service, action component)

Returns:
std::shared_ptr<Ros2Message> Pointer to the created dynamic message

virtualboolvalidateTopicName(conststd ::string&topicName)

Validates a ROS 2 topic name.
Parameters:
topicName – [in] Name to validate

Returns:
bool True if the topic name is valid

virtualboolvalidateNamespaceName(conststd ::string&namespaceName)

Validates a ROS 2 namespace name.
Parameters:
namespaceName – [in] Name to validate

Returns:
bool True if the namespace name is valid

virtualboolvalidateNodeName(conststd ::string&nodeName)

Validates a ROS 2 node name.
Parameters:
nodeName – [in] Name to validate

Returns:
bool True if the node name is valid
