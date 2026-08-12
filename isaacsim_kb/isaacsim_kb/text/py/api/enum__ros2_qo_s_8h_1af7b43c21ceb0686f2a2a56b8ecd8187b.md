<!-- source: py/api/enum__ros2_qo_s_8h_1af7b43c21ceb0686f2a2a56b8ecd8187b.html | title: Ros2QoSDurabilityPolicy — Isaac Sim -->

# Ros2QoSDurabilityPolicy
Fully qualified name: `isaacsim::ros2::bridge::Ros2QoSDurabilityPolicy`
enumclassisaacsim ::ros2 ::bridge ::Ros2QoSDurabilityPolicy

Enumerations of ROS 2 QoS Durability policy.
Defines the durability policy options for ROS 2 QoS settings, determining how messages are handled for late-joining subscribers.
See also
ROS 2 QoS policies
Values:
enumeratoreSystemDefault

Use the system default durability setting.

enumeratoreTransientLocal

Store messages locally for late joiners.

enumeratoreVolatile

No storage of messages for late joiners.

enumeratoreUnknown

Unknown or invalid durability policy.
