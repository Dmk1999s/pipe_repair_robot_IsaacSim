<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_service_impl.html | title: Ros2ServiceImpl — Isaac Sim -->

# Ros2ServiceImpl
Fully qualified name: `isaacsim::ros2::bridge::Ros2ServiceImpl`
classRos2ServiceImpl:publicisaacsim ::ros2 ::bridge ::Ros2Service

Implementation of ROS 2 Service Server.
Manages a ROS 2 service server instance, providing functionality for handling service requests and sending responses.
Public Functions
Ros2ServiceImpl(
Ros2NodeHandle *nodeHandle,
constchar*serviceName,
constvoid*typeSupport,
constRos2QoSProfile &qos,
)
Constructor for ROS 2 Service Server implementation.
Parameters:

- nodeHandle – [in] Pointer to the ROS 2 node handle.

- serviceName – [in] Name of the service.

- typeSupport – [in] Type support handle for the service type.

- qos – [in] Quality of Service settings for the service.

virtual~Ros2ServiceImpl()

virtualbooltakeRequest(void*requestMsg)

Takes a pending service request.
Parameters:
requestMsg – [out] Pointer to store the request message

Returns:
bool True if a request was received

virtualboolsendResponse(void*responseMsg)

Sends a service response.
Parameters:
responseMsg – [in] Pointer to the response message

Returns:
bool True if the response was sent successfully

inlinevirtualboolisValid()

Checks if the service server is valid.
Returns:
bool True if the service server is properly initialized
