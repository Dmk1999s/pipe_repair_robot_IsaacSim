<!-- source: py/api/namespace_isaacsim__ros2__omnigraph__utils.html | title: omnigraph_utils — Isaac Sim -->

# omnigraph_utils
Fully qualified name: `isaacsim::ros2::omnigraph_utils`
namespaceomnigraph_utils

## Functions
boolcheckCondition (const void *ptr, std::string message)
Verifies that a pointer is not null and logs an error message if it is.

boolcreateOgAttributesForFields (OgnROS2DatabaseDerivedType &db, const NodeObj &nodeObj, std::vector< DynamicMessageField > messageFields, const std::string prependStr, std::string messageType)
Creates OmniGraph attributes for message fields.

boolcreateOgAttributesForMessage (OgnROS2DatabaseDerivedType &db, const NodeObj &nodeObj, const std::string &messagePackage, const std::string &messageSubfolder, const std::string &messageName, std::shared_ptr< Ros2Message > message, const std::string prependStr)
Creates OmniGraph attributes for a ROS 2 message.

boolfindMatchingAttribute (OgnROS2DatabaseDerivedType &db, const NodeObj &nodeObj, std::vector< DynamicMessageField > messageFields, const std::string prependStr)
Checks if node attributes match message fields.

T const *getAttributeReadableArrayData (const NodeObj &nodeObj, const std::string &attrName, size_t &newCount)
Gets read-only data for an array attribute.

T const *getAttributeReadableData (const NodeObj &nodeObj, const std::string &attrName)
Gets read-only data for a simple attribute.

T *getAttributeWritableArrayData (const NodeObj &nodeObj, const std::string &attrName, size_t newCount)
Gets writable data for an array attribute with resizing.

T *getAttributeWritableData (const NodeObj &nodeObj, const std::string &attrName)
Gets writable data for a simple attribute.

std::stringinputOutput (bool isOutput)
Returns the OmniGraph attribute prefix based on direction.

boolremoveDynamicAttributes (const NodeObj &nodeObj)
Removes dynamic attributes from a node.

boolwriteMessageDataFromNode (OmniGraphDatabase &db, std::shared_ptr< Ros2Message > message, std::string prependStr, bool isOutput)
Reads attribute data from an OmniGraph node and writes it to a ROS 2 message.

boolwriteNodeAttributeFromMessage (OmniGraphDatabase &db, std::shared_ptr< Ros2Message > message, std::string prependStr, bool isOutput)
Reads data from a ROS 2 message and writes it to OmniGraph node attributes.
