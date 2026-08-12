<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_service.html | title: Ros2Service — Isaac Sim -->

# Ros2Service
Fully qualified name: `isaacsim::ros2::bridge::Ros2Service`
classRos2Service

Base class for ROS 2 service servers.
Provides the interface for implementing ROS 2 service servers. Service servers receive requests and send responses in a request-response pattern.
Subclassed by isaacsim::ros2::bridge::Ros2ServiceImpl
Public Functions
virtualbooltakeRequest(void*requestMsg)=0

Processes incoming service requests.
Checks for and retrieves any pending service requests. If a request is available, it is copied into the provided message structure.
Parameters:
requestMsg – [out] Pointer to store the received request message.

Returns:
True if a request was received, false otherwise.

Pre:
The requestMsg pointer must point to a valid request message structure of the correct type.

Pre:
The service server must be valid (check with isValid() ).

virtualboolsendResponse(void*responseMsg)=0

Sends a response to a service request.
Sends the provided response message back to the client that made the request.
Parameters:
responseMsg – [in] Pointer to the response message to send.

Returns:
True if the response was sent successfully, false otherwise.

Pre:
The responseMsg pointer must point to a valid response message structure of the correct type.

Pre:
The service server must have previously received a request via takeRequest() .

Pre:
The service server must be valid (check with isValid() ).

virtualboolisValid()=0

Checks whether the service server is valid.
Verifies if the object holds a properly initialized ROS 2 service server instance.
Note
A service server may become invalid if its associated node or context is destroyed.
Returns:
True if the service server is valid, false otherwise.
