<!-- source: py/api/classes.html | title: Classes — Isaac Sim -->

# Classes
Colour
RGBA color representation with floating point components.

IPCBufferManager
Manages CUDA device memory buffers for inter-process communication (IPC).

Plane
3D plane representation in the form ax + by + cz + d = 0.

Point3
Represents a 3D point in space with floating-point coordinates.

Rect
2D rectangle representation using integer coordinates.

Rotation
Euler angle representation of 3D rotation.

XMatrix
Template class representing an m×n matrix with column-major storage.

XMatrix44
Template class representing a 4x4 matrix stored in column-major order.

XQuat
Template class representing a quaternion with x, y, z, and w components.

XVector2
A template class representing a 2D vector with templated component type.

XVector3
Template class representing a 3-dimensional vector with x, y, and z components.

XVector4
Template class representing a 4-dimensional vector with x, y, z, and w components.

isaacsim::asset::gen::omap::MapGenerator
Generator class for creating 2D and 3D occupancy maps from USD stages.

isaacsim::asset::importer::mjcf::MJCFActuator
Actuator component for applying forces/torques to joints.

isaacsim::asset::importer::mjcf::MJCFBody
Represents a rigid body in the MJCF model hierarchy.

isaacsim::asset::importer::mjcf::MJCFClass
Class definition for setting default values for MJCF elements.

isaacsim::asset::importer::mjcf::MJCFCompiler
Compiler settings that affect how the MJCF model is processed.

isaacsim::asset::importer::mjcf::MJCFContact
Contact definition for collision filtering and contact parameters.

isaacsim::asset::importer::mjcf::MJCFGeom
Geometry element for collision detection and physics simulation.

isaacsim::asset::importer::mjcf::MJCFImporter
Main importer class for loading and converting MJCF models to USD format.

isaacsim::asset::importer::mjcf::MJCFInertial
Inertial properties of a body in the MJCF model.

isaacsim::asset::importer::mjcf::MJCFJoint
Represents a joint in the MJCF (MuJoCo XML Format) model.

isaacsim::asset::importer::mjcf::MJCFMaterial
Material definition for visual appearance.

isaacsim::asset::importer::mjcf::MJCFMesh
Mesh asset definition for 3D geometry.

isaacsim::asset::importer::mjcf::MJCFSite
Site element for marking specific locations and orientations in the model.

isaacsim::asset::importer::mjcf::MJCFTendon
Tendon element for creating cable-like constraints between bodies.

isaacsim::asset::importer::mjcf::MJCFTexture
Texture asset definition for materials.

isaacsim::asset::importer::mjcf::MJCFVisualElement
Base class for visual elements in MJCF models.

isaacsim::asset::importer::urdf::KinematicChain
Represents the kinematic chain of a robot as a tree structure.

isaacsim::asset::importer::urdf::UrdfImporter
URDF (Unified Robot Description Format) importer for converting robot descriptions to USD format.

isaacsim::core::includes::BaseResetNode
Base class for nodes that automatically reset their state when simulation is stopped.

isaacsim::core::includes::Buffer
Abstract base class for memory buffer management.

isaacsim::core::includes::ComponentBase
Base class template for USD prim-attached components in an Application.

isaacsim::core::includes::ComponentManager
Base class for managing USD-based components in an application.

isaacsim::core::includes::DeviceBufferBase
CUDA device (GPU) memory buffer implementation.

isaacsim::core::includes::GenericBufferBase
Device-generic (CPU or CUDA device) memory buffer implementation.

isaacsim::core::includes::HostBufferBase
Host (CPU) memory buffer implementation.

isaacsim::core::includes::LibraryLoader
Single dynamic library loader.

isaacsim::core::includes::MultiLibraryLoader
Manager for multiple dynamic libraries.

isaacsim::core::includes::PrimManagerBase
Base template class for bridge applications managing USD-based components.

isaacsim::core::includes::PrimManagerUsdNoticeListener
Custom USD notice listener for handling object changes in the stage.

isaacsim::core::includes::ScopedCudaTextureObject
RAII wrapper for CUDA texture object management.

isaacsim::core::includes::ScopedDevice
RAII wrapper for CUDA device context management.

isaacsim::core::includes::ScopedTimer
RAII-style performance timer for code block measurement.

isaacsim::core::includes::UsdNoticeListener
Helper base class to subscribe to pxr::TfNotice.

isaacsim::core::includes::posetree::PoseTree
A utility class for managing and traversing hierarchical pose transformations in a scene.

isaacsim::core::nodes::CoreNodes
Minimal interface for core node functionality.

isaacsim::core::simulation_manager::UsdNoticeListener
Listener class for USD object change notifications.

isaacsim::robot::surface_gripper::SurfaceGripperComponent
Component class for managing Surface Gripper functionality.

isaacsim::robot::surface_gripper::SurfaceGripperManager
Manager class for handling surface grippers in a scene.

isaacsim::ros2::bridge::Ros2AckermannDriveStampedMessage
Class implementing a `ackermann_msgs/msg/AckermannDriveStamped` .

isaacsim::ros2::bridge::Ros2AckermannDriveStampedMessageImpl
Implementation of ROS 2 Ackermann Drive Stamped message.

isaacsim::ros2::bridge::Ros2BoundingBox2DMessage
Class implementing a `vision_msgs/msg/Detection2DArray` message.

isaacsim::ros2::bridge::Ros2BoundingBox2DMessageImpl
Implementation of ROS 2 2D Bounding Box message.

isaacsim::ros2::bridge::Ros2BoundingBox3DMessage
Class implementing a `vision_msgs/msg/Detection3DArray` message.

isaacsim::ros2::bridge::Ros2BoundingBox3DMessageImpl
Implementation of ROS 2 3D Bounding Box message.

isaacsim::ros2::bridge::Ros2Bridge
Main interface class for the ROS 2 bridge functionality.

isaacsim::ros2::bridge::Ros2CameraInfoMessage
Class implementing a `sensor_msgs/msg/CameraInfo` message.

isaacsim::ros2::bridge::Ros2CameraInfoMessageImpl
Implementation of ROS 2 Camera Info message.

isaacsim::ros2::bridge::Ros2Client
Base class for ROS 2 service clients.

isaacsim::ros2::bridge::Ros2ClientImpl
Implementation of ROS 2 Service Client.

isaacsim::ros2::bridge::Ros2ClockMessage
Class implementing a `rosgraph_msgs/msg/Clock` message.

isaacsim::ros2::bridge::Ros2ClockMessageImpl
Implementation of ROS 2 Clock message.

isaacsim::ros2::bridge::Ros2ContextHandle
Encapsulates a ROS 2 context for initialization and cleanup.

isaacsim::ros2::bridge::Ros2ContextHandleImpl
Implementation of ROS 2 Context Handle.

isaacsim::ros2::bridge::Ros2DynamicMessage
Class implementing dynamic ROS 2 messages.

isaacsim::ros2::bridge::Ros2DynamicMessageImpl
Implementation of ROS 2 Dynamic Message.

isaacsim::ros2::bridge::Ros2Factory
Base class for creating ROS 2 related functions/objects according to the sourced ROS 2 distribution.

isaacsim::ros2::bridge::Ros2FactoryImpl
Concrete implementation of the ROS 2 factory interface.

isaacsim::ros2::bridge::Ros2ImageMessage
Class implementing a `sensor_msgs/msg/Image` message.

isaacsim::ros2::bridge::Ros2ImageMessageImpl
Implementation of ROS 2 Image message.

isaacsim::ros2::bridge::Ros2ImuMessage
Class implementing a `sensor_msgs/msg/Imu` message.

isaacsim::ros2::bridge::Ros2ImuMessageImpl
Implementation of ROS 2 IMU message.

isaacsim::ros2::bridge::Ros2JointStateMessage
Class implementing a `sensor_msgs/msg/JointState` message.

isaacsim::ros2::bridge::Ros2JointStateMessageImpl
Implementation of ROS 2 Joint State message.

isaacsim::ros2::bridge::Ros2LaserScanMessage
Class implementing a `sensor_msgs/msg/LaserScan` message.

isaacsim::ros2::bridge::Ros2LaserScanMessageImpl
Implementation of ROS 2 Laser Scan message.

isaacsim::ros2::bridge::Ros2Message
Base class for all ROS 2 message encapsulations.

isaacsim::ros2::bridge::Ros2MessageInterface
Base class for ROS 2 message definition/generation via ROS Interface Definition Language (IDL).

isaacsim::ros2::bridge::Ros2MessageInterfaceImpl
Implementation of the ROS 2 message interface.

isaacsim::ros2::bridge::Ros2NitrosBridgeImageMessage
Class implementing a `isaac_ros_nitros_bridge_interfaces/msg/NitrosBridgeImage` message.

isaacsim::ros2::bridge::Ros2NitrosBridgeImageMessageImpl
Implementation of NITROS Bridge Image message.

isaacsim::ros2::bridge::Ros2Node
Base class for ROS 2 bridge nodes.

isaacsim::ros2::bridge::Ros2NodeHandle
Base class that encapsulates a ROS 2 node ( `rcl_node_t` ) instance.

isaacsim::ros2::bridge::Ros2NodeHandleImpl
Implementation of ROS 2 Node Handle.

isaacsim::ros2::bridge::Ros2OdometryMessage
Class implementing a `nav_msgs/msg/Odometry` message.

isaacsim::ros2::bridge::Ros2OdometryMessageImpl
Implementation of ROS 2 Odometry message.

isaacsim::ros2::bridge::Ros2PointCloudMessage
Class implementing a `sensor_msgs/msg/PointCloud2` message.

isaacsim::ros2::bridge::Ros2PointCloudMessageImpl
Implementation of ROS 2 Point Cloud message.

isaacsim::ros2::bridge::Ros2Publisher
Base class for ROS 2 publishers.

isaacsim::ros2::bridge::Ros2PublisherImpl
Implementation of ROS 2 Publisher.

isaacsim::ros2::bridge::Ros2QoSProfileConverter
Utility class for converting QoS profiles between formats.

isaacsim::ros2::bridge::Ros2RawTfTreeMessage
Class implementing a `tf2_msgs/msg/TFMessage` message with only one transform.

isaacsim::ros2::bridge::Ros2RawTfTreeMessageImpl
Implementation of ROS 2 Raw Transform Tree message.

isaacsim::ros2::bridge::Ros2SemanticLabelMessage
Class implementing a `std_msgs/msg/String` message for semantic label.

isaacsim::ros2::bridge::Ros2SemanticLabelMessageImpl
Implementation of ROS 2 Semantic Label message.

isaacsim::ros2::bridge::Ros2Service
Base class for ROS 2 service servers.

isaacsim::ros2::bridge::Ros2ServiceImpl
Implementation of ROS 2 Service Server.

isaacsim::ros2::bridge::Ros2Subscriber
Base class for ROS 2 subscribers.

isaacsim::ros2::bridge::Ros2SubscriberImpl
Implementation of ROS 2 Subscriber.

isaacsim::ros2::bridge::Ros2TfTreeMessage
Class implementing a `tf2_msgs/msg/TFMessage` message.

isaacsim::ros2::bridge::Ros2TfTreeMessageImpl
Implementation of ROS 2 Transform Tree message.

isaacsim::ros2::bridge::Ros2TwistMessage
Class implementing a `geometry_msgs/msg/Twist` .

isaacsim::ros2::bridge::Ros2TwistMessageImpl
Implementation of ROS 2 Twist message.

isaacsim::ros2::tf_viewer::ITransformListener
ROS 2 transform listener interface.

isaacsim::ros2::tf_viewer::Ros2BufferCore
Class that partially implements a tf2 `BufferCore` .

isaacsim::ros2::tf_viewer::Ros2BufferCoreImpl
Implementation of ROS 2 Transform Buffer Core.

isaacsim::ros2::tf_viewer::Tf2Factory
Base class for creating ROS 2 tf2 related functions/objects according to the sourced ROS 2 distribution.

isaacsim::ros2::tf_viewer::Tf2FactoryImpl
Factory implementation for creating TF2 components.

isaacsim::sensors::physics::ContactManager
Manages contact events and data in the physics simulation.

isaacsim::sensors::physics::ContactSensor
Component for simulating contact sensors in the physics environment.

isaacsim::sensors::physics::ContactSensorInterface
Interface for contact sensor functionality.

isaacsim::sensors::physics::ImuSensor
Implementation of an Inertial Measurement Unit (IMU) sensor component.

isaacsim::sensors::physics::ImuSensorInterface
Interface for IMU (Inertial Measurement Unit) sensor functionality.

isaacsim::sensors::physics::IsaacSensorComponentBase
Base class template for non-RTX Isaac sensors.

isaacsim::sensors::physics::IsaacSensorManager
Manager class for handling Isaac physics-based sensors.

isaacsim::sensors::physx::GenericSensor
A generic range sensor implementation that supports customizable scanning patterns.

isaacsim::sensors::physx::GenericSensorInterface
Interface for accessing generic range sensor functionality.

isaacsim::sensors::physx::LidarSensor
A LiDAR (Light Detection and Ranging) sensor implementation.

isaacsim::sensors::physx::LidarSensorInterface
Interface for accessing LIDAR sensor data and properties.

isaacsim::sensors::physx::LightBeamSensor
A sensor that simulates a curtain of light beams for range detection.

isaacsim::sensors::physx::LightBeamSensorInterface
Interface for accessing light beam sensor functionality.

isaacsim::sensors::physx::RadarSensorInterface
Interface for accessing radar sensor functionality.

isaacsim::sensors::physx::RangeSensorComponentBase
Base class which simulates a range sensor.

isaacsim::sensors::physx::RangeSensorManager
Manager class for handling multiple range sensor components in the simulation.

isaacsim::sensors::rtx::LidarConfigHelper
Helper class for managing LiDAR sensor configuration.

mesh::MeshImporter
Utility class for importing and converting mesh assets to USD format.

omni::isaac::dynamic_control::Bucket
A container for managing objects with unique IDs.

omni::isaac::dynamic_control::DcContext
Context for managing dynamic control objects in a physics scene.

omni::kit::RunLoopSynchronizer
Class for synchronizing multiple run loops.
