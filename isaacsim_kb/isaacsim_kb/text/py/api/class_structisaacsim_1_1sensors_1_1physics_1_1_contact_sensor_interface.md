<!-- source: py/api/class_structisaacsim_1_1sensors_1_1physics_1_1_contact_sensor_interface.html | title: ContactSensorInterface — Isaac Sim -->

# ContactSensorInterface
Fully qualified name: `isaacsim::sensors::physics::ContactSensorInterface`
classContactSensorInterface

Interface for contact sensor functionality.
Provides methods for accessing contact sensor data and raw physics engine data related to contact events between rigid bodies.
Public Members
CsRawData *(*getSensorRawData)(constchar*primPath,size_t&numContacts)

Gets contact raw data from physics engine.
Gets Contact raw data, for validation purposes and ground truth
Param primPath:
path of the sensor prim

Param numContacts:
size of contacts

Return:
Raw Data

CsReading (*getSensorReading)(constchar*primPath,constbool&getLatestValue)

Gets Sensor latest simulation.
Check is the prim path contact sensor
Param primPath:
path of the sensor prim

Param getLatestValue:
boolean flag for getting the latest sim value or the last sensor measured value

Return:
time-stamped sensor values

bool(*isContactSensor)(constchar*primPath)

Checks if a prim is a contact sensor.
Param primPath:
[in] Path of the prim to check.

Return:
True if the prim is a contact sensor, false otherwise.

constchar*(*decodeBodyName)(uint64_tbody)

Decodes a rigid body identifier into a human-readable name.
Param body:
[in] Unique identifier of the rigid body.

Return:
Human-readable name of the rigid body.

CsRawData *(*getBodyRawData)(constchar*primPath,size_t&numContacts)

Gets contact raw data of a rigid body with contact report API from physics engine.
Gets Contact raw data, for validation purposes and ground truth
Param primPath:
path of the rigid body prim

Param numContacts:
size of contacts

Return:
Raw Data
