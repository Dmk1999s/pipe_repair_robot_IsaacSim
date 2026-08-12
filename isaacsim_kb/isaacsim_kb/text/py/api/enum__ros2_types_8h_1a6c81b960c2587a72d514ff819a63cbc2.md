<!-- source: py/api/enum__ros2_types_8h_1a6c81b960c2587a72d514ff819a63cbc2.html | title: BackendMessageType — Isaac Sim -->

# BackendMessageType
Fully qualified name: `isaacsim::ros2::bridge::BackendMessageType`
enumclassisaacsim ::ros2 ::bridge ::BackendMessageType:uint8_t

Enumerations of ROS 2 message types.
Defines the various types of messages that can be handled by the ROS 2 bridge, including topics, services, and actions with their respective components.
Values:
enumeratoreMessage

Topic message.

enumeratoreRequest

Service request (`_Request`).

enumeratoreResponse

Service response (`_Response`).

enumeratoreGoal

Action goal (`_Goal`).

enumeratoreResult

Action result (`_Result`).

enumeratoreFeedback

Action feedback (`_Feedback`).

enumeratoreSendGoalRequest

Action goal request (`_SendGoal_Request`).

enumeratoreSendGoalResponse

Action goal response (`_SendGoal_Response`).

enumeratoreFeedbackMessage

Action feedback (`_FeedbackMessage`).

enumeratoreGetResultRequest

Action result request (`_GetResult_Request`).

enumeratoreGetResultResponse

Action result response (`_GetResult_Response`).
