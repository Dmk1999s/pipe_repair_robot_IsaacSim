<!-- source: py/api/namespace_isaacsim__ros2__bridge.html | title: bridge — Isaac Sim -->

# bridge
Fully qualified name: `isaacsim::ros2::bridge`
namespacebridge

## Classes
Ros2AckermannDriveStampedMessage
Class implementing a `ackermann_msgs/msg/AckermannDriveStamped` .

Ros2AckermannDriveStampedMessageImpl
Implementation of ROS 2 Ackermann Drive Stamped message.

Ros2BoundingBox2DMessage
Class implementing a `vision_msgs/msg/Detection2DArray` message.

Ros2BoundingBox2DMessageImpl
Implementation of ROS 2 2D Bounding Box message.

Ros2BoundingBox3DMessage
Class implementing a `vision_msgs/msg/Detection3DArray` message.

Ros2BoundingBox3DMessageImpl
Implementation of ROS 2 3D Bounding Box message.

Ros2Bridge
Main interface class for the ROS 2 bridge functionality.

Ros2CameraInfoMessage
Class implementing a `sensor_msgs/msg/CameraInfo` message.

Ros2CameraInfoMessageImpl
Implementation of ROS 2 Camera Info message.

Ros2Client
Base class for ROS 2 service clients.

Ros2ClientImpl
Implementation of ROS 2 Service Client.

Ros2ClockMessage
Class implementing a `rosgraph_msgs/msg/Clock` message.

Ros2ClockMessageImpl
Implementation of ROS 2 Clock message.

Ros2ContextHandle
Encapsulates a ROS 2 context for initialization and cleanup.

Ros2ContextHandleImpl
Implementation of ROS 2 Context Handle.

Ros2DynamicMessage
Class implementing dynamic ROS 2 messages.

Ros2DynamicMessageImpl
Implementation of ROS 2 Dynamic Message.

Ros2Factory
Base class for creating ROS 2 related functions/objects according to the sourced ROS 2 distribution.

Ros2FactoryImpl
Concrete implementation of the ROS 2 factory interface.

Ros2ImageMessage
Class implementing a `sensor_msgs/msg/Image` message.

Ros2ImageMessageImpl
Implementation of ROS 2 Image message.

Ros2ImuMessage
Class implementing a `sensor_msgs/msg/Imu` message.

Ros2ImuMessageImpl
Implementation of ROS 2 IMU message.

Ros2JointStateMessage
Class implementing a `sensor_msgs/msg/JointState` message.

Ros2JointStateMessageImpl
Implementation of ROS 2 Joint State message.

Ros2LaserScanMessage
Class implementing a `sensor_msgs/msg/LaserScan` message.

Ros2LaserScanMessageImpl
Implementation of ROS 2 Laser Scan message.

Ros2Message
Base class for all ROS 2 message encapsulations.

Ros2MessageInterface
Base class for ROS 2 message definition/generation via ROS Interface Definition Language (IDL).

Ros2MessageInterfaceImpl
Implementation of the ROS 2 message interface.

Ros2NitrosBridgeImageMessage
Class implementing a `isaac_ros_nitros_bridge_interfaces/msg/NitrosBridgeImage` message.

Ros2NitrosBridgeImageMessageImpl
Implementation of NITROS Bridge Image message.

Ros2Node
Base class for ROS 2 bridge nodes.

Ros2NodeHandle
Base class that encapsulates a ROS 2 node ( `rcl_node_t` ) instance.

Ros2NodeHandleImpl
Implementation of ROS 2 Node Handle.

Ros2OdometryMessage
Class implementing a `nav_msgs/msg/Odometry` message.

Ros2OdometryMessageImpl
Implementation of ROS 2 Odometry message.

Ros2PointCloudMessage
Class implementing a `sensor_msgs/msg/PointCloud2` message.

Ros2PointCloudMessageImpl
Implementation of ROS 2 Point Cloud message.

Ros2Publisher
Base class for ROS 2 publishers.

Ros2PublisherImpl
Implementation of ROS 2 Publisher.

Ros2QoSProfileConverter
Utility class for converting QoS profiles between formats.

Ros2RawTfTreeMessage
Class implementing a `tf2_msgs/msg/TFMessage` message with only one transform.

Ros2RawTfTreeMessageImpl
Implementation of ROS 2 Raw Transform Tree message.

Ros2SemanticLabelMessage
Class implementing a `std_msgs/msg/String` message for semantic label.

Ros2SemanticLabelMessageImpl
Implementation of ROS 2 Semantic Label message.

Ros2Service
Base class for ROS 2 service servers.

Ros2ServiceImpl
Implementation of ROS 2 Service Server.

Ros2Subscriber
Base class for ROS 2 subscribers.

Ros2SubscriberImpl
Implementation of ROS 2 Subscriber.

Ros2TfTreeMessage
Class implementing a `tf2_msgs/msg/TFMessage` message.

Ros2TfTreeMessageImpl
Implementation of ROS 2 Transform Tree message.

Ros2TwistMessage
Class implementing a `geometry_msgs/msg/Twist` .

Ros2TwistMessageImpl
Implementation of ROS 2 Twist message.

## Enumerations
uint8_tBackendMessageType
Enumerations of ROS 2 message types.

Ros2Distro
Enumeration of supported ROS 2 distributions.

Ros2QoSDurabilityPolicy
Enumerations of ROS 2 QoS Durability policy.

Ros2QoSHistoryPolicy
Enumerations of ROS 2 QoS History policy.

Ros2QoSLivelinessPolicy
Enumerations of ROS 2 QoS Liveliness policy.

Ros2QoSReliabilityPolicy
Enumerations of ROS 2 QoS Reliability policy.

## Functions
boolisRos2DistroSupported (const std::string &distro)
Checks if a ROS 2 distribution is supported.

const booljsonToRos2QoSProfile (Ros2QoSProfile &qos, const std::string &jsonString)
Converts a JSON string to a ROS 2 QoS profile.

## Namespaces
@69
@76

## Structs
DynamicMessageField
Structure that encapsulates a dynamic message field.

Ros2QoSProfile
ROS 2 QoS Profile configuration.

Ros2QoSTime
ROS 2 QoS time representation.

TfTransformStamped
Structure that encapsulates geometry_msgs/msg/TransformStamped data.
