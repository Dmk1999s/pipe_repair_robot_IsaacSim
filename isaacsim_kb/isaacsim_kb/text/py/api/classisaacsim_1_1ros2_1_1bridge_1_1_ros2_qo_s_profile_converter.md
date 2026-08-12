<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_qo_s_profile_converter.html | title: Ros2QoSProfileConverter — Isaac Sim -->

# Ros2QoSProfileConverter
Fully qualified name: `isaacsim::ros2::bridge::Ros2QoSProfileConverter`
classRos2QoSProfileConverter

Utility class for converting QoS profiles between formats.
Provides functionality to convert between different Quality of Service (QoS) profile representations used in ROS 2 communication. This class helps ensure proper QoS settings are maintained across different parts of the system.
Public Static Functions
staticrmw_qos_profile_tconvert(constRos2QoSProfile &qos)

Converts a QoS profile to RMW format.
Converts a ROS 2 QoS profile from the bridge’s internal representation to the ROS Middleware (RMW) format used by the ROS 2 implementation.
Parameters:
qos – [in] The QoS profile to convert

Returns:
rmw_qos_profile_t The converted QoS profile in RMW format
