<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_client_impl.html | title: Ros2ClientImpl — Isaac Sim -->

# Ros2ClientImpl
Fully qualified name: `isaacsim::ros2::bridge::Ros2ClientImpl`
classRos2ClientImpl:publicisaacsim ::ros2 ::bridge ::Ros2Client

Implementation of ROS 2 Service Client.
Manages a ROS 2 service client instance, providing functionality for sending service requests and receiving responses.
Public Functions
Ros2ClientImpl(
Ros2NodeHandle *nodeHandle,
constchar*serviceName,
constvoid*typeSupport,
constRos2QoSProfile &qos,
)
Constructor for ROS 2 Service Client implementation.
Parameters:

- nodeHandle – [in] Pointer to the ROS 2 node handle.

- serviceName – [in] Name of the service.

- typeSupport – [in] Type support handle for the service type.

- qos – [in] Quality of Service settings for the client.

virtual~Ros2ClientImpl()

virtualboolsendRequest(void*requestMsg)

Sends a service request.
Parameters:
requestMsg – [in] Pointer to the request message

Returns:
bool True if the request was sent successfully

virtualbooltakeResponse(void*responseMsg)

Takes a service response.
Parameters:
responseMsg – [out] Pointer to store the response message

Returns:
bool True if a response was received

inlinevirtualboolisValid()

Checks if the service client is valid.
Returns:
bool True if the service client is properly initialized
