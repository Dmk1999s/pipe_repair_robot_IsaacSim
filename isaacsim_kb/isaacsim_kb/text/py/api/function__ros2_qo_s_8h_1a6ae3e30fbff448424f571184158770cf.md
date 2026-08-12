<!-- source: py/api/function__ros2_qo_s_8h_1a6ae3e30fbff448424f571184158770cf.html | title: jsonToRos2QoSProfile — Isaac Sim -->

# jsonToRos2QoSProfile
Fully qualified name: `isaacsim::ros2::bridge::jsonToRos2QoSProfile`
staticinlineconstboolisaacsim ::ros2 ::bridge ::jsonToRos2QoSProfile(
Ros2QoSProfile &qos,
conststd ::string&jsonString,
)
Converts a JSON string to a ROS 2 QoS profile.
Parses a JSON string containing QoS settings and converts it into a Ros2QoSProfile structure. The JSON must contain all required fields with appropriate types:

- history: string (matching Ros2QoSHistoryPolicy)

- depth: non-negative integer

- reliability: string (matching Ros2QoSReliabilityPolicy)

- durability: string (matching Ros2QoSDurabilityPolicy)

- deadline: non-negative float (seconds)

- lifespan: non-negative float (seconds)

- liveliness: string (matching Ros2QoSLivelinessPolicy)

- leaseDuration: non-negative float (seconds)

Note
The function performs extensive validation of the JSON input
Parameters:

- qos – [out] Reference to Ros2QoSProfile to store the converted settings

- jsonString – [in] JSON string containing QoS settings

Returns:
bool True if conversion successful, false otherwise
