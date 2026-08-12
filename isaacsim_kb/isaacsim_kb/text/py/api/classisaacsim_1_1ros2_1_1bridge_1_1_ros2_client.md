<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_client.html | title: Ros2Client — Isaac Sim -->

# Ros2Client
Fully qualified name: `isaacsim::ros2::bridge::Ros2Client`
classRos2Client

Base class for ROS 2 service clients.
Provides the interface for implementing ROS 2 service clients. Service clients send requests and receive responses in a request-response pattern.
Subclassed by isaacsim::ros2::bridge::Ros2ClientImpl
Public Functions
virtualboolsendRequest(void*requestMsg)=0

Sends a request to a service.
Sends the provided request message to the associated service server.
Note
This method does not wait for a response. Use takeResponse() to retrieve the response.
Parameters:
requestMsg – [in] Pointer to the request message to send.

Returns:
True if the request was sent successfully, false otherwise.

Pre:
The requestMsg pointer must point to a valid request message structure of the correct type.

Pre:
The service client must be valid (check with isValid() ).

virtualbooltakeResponse(void*responseMsg)=0

Retrieves the response to a service request.
Checks for and retrieves the response to a previously sent request. If a response is available, it is copied into the provided message structure.
Parameters:
responseMsg – [out] Pointer to store the received response message.

Returns:
True if a response was received, false otherwise.

Pre:
The responseMsg pointer must point to a valid response message structure of the correct type.

Pre:
The service client must have previously sent a request via sendRequest() .

Pre:
The service client must be valid (check with isValid() ).

virtualboolisValid()=0

Checks whether the service client is valid.
Verifies if the object holds a properly initialized ROS 2 service client instance.
Note
A service client may become invalid if its associated node or context is destroyed.
Returns:
True if the service client is valid, false otherwise.
