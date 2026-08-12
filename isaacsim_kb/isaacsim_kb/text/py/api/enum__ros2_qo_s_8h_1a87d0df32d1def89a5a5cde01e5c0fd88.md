<!-- source: py/api/enum__ros2_qo_s_8h_1a87d0df32d1def89a5a5cde01e5c0fd88.html | title: Ros2QoSReliabilityPolicy — Isaac Sim -->

# Ros2QoSReliabilityPolicy
Fully qualified name: `isaacsim::ros2::bridge::Ros2QoSReliabilityPolicy`
enumclassisaacsim ::ros2 ::bridge ::Ros2QoSReliabilityPolicy

Enumerations of ROS 2 QoS Reliability policy.
Defines the reliability policy options for ROS 2 QoS settings, determining the guarantees about message delivery.
See also
ROS 2 QoS policies
Values:
enumeratoreSystemDefault

Use the system default reliability setting.

enumeratoreReliable

Guarantee message delivery with retries.

enumeratoreBestEffort

No delivery guarantee, may drop messages.

enumeratoreUnknown

Unknown or invalid reliability policy.
