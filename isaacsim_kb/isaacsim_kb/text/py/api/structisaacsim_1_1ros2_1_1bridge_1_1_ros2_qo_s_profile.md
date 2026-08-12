<!-- source: py/api/structisaacsim_1_1ros2_1_1bridge_1_1_ros2_qo_s_profile.html | title: Ros2QoSProfile — Isaac Sim -->

# Ros2QoSProfile
Fully qualified name: `isaacsim::ros2::bridge::Ros2QoSProfile`
structRos2QoSProfile

ROS 2 QoS Profile configuration.
Comprehensive structure for configuring all aspects of ROS 2 Quality of Service. Provides settings for history, reliability, durability, deadlines, lifespan, and liveliness policies.
Public Functions
inlineRos2QoSProfile()

Default constructor initializing system default values.
Initializes the QoS profile with ROS 2 default values from rmw_qos_profile_default:

- History: Keep last 10 messages

- Reliability: Reliable delivery

- Durability: Volatile

- Other timing parameters: 0

Public Members
Ros2QoSHistoryPolicy history

History policy setting.

size_tdepth

Size of the message queue.

Ros2QoSReliabilityPolicy reliability

Reliability policy setting.

Ros2QoSDurabilityPolicy durability

Durability policy setting.

Ros2QoSTime deadline

Period for expected message send/receive.

Ros2QoSTime lifespan

Maximum age for valid messages.

Ros2QoSLivelinessPolicy liveliness

Liveliness policy setting.

Ros2QoSTime livelinessLeaseDuration

Time window for liveliness assertion.

boolavoidRosNamespaceConventions

Flag to bypass ROS 2 namespace conventions.
