<!-- source: py/api/structisaacsim_1_1ros2_1_1bridge_1_1_dynamic_message_field.html | title: DynamicMessageField — Isaac Sim -->

# DynamicMessageField
Fully qualified name: `isaacsim::ros2::bridge::DynamicMessageField`
structDynamicMessageField

Structure that encapsulates a dynamic message field.
Provides a flexible container for ROS 2 message fields with support for both ROS and OmniGraph data types, including hierarchical field names.
Public Functions
inlinestd ::vector<std ::string>names(chardelimiter=':')

Splits the field name into hierarchical components.
Generates a list of field names by splitting the hierarchical name using the specified delimiter.
Note
The default delimiter is ‘:’ which matches how hierarchical fields are stored.
Parameters:
delimiter – [in] Character used to split the name.

Returns:
List of field names in hierarchical order.

Public Members
std ::stringname

Field name.
Hierarchical names (e.g.: MESSAGE fields are unrolled and concatenated by `:`).

uint8_trosType

ROS data type from rosidl_typesupport_introspection_c/field_types.h.

boolisArray

Whether the field is an array.

std ::stringognType

OmniGraph data type name from omni.graph.docs.

omni ::fabric::BaseDataTypedataType

Fabric data type.
