<!-- source: py/api/namespace_isaacsim__sensors__physics.html | title: physics — Isaac Sim -->

# physics
Fully qualified name: `isaacsim::sensors::physics`
namespacephysics

## Classes
ContactManager
Manages contact events and data in the physics simulation.

ContactSensor
Component for simulating contact sensors in the physics environment.

ContactSensorInterface
Interface for contact sensor functionality.

ImuSensor
Implementation of an Inertial Measurement Unit (IMU) sensor component.

ImuSensorInterface
Interface for IMU (Inertial Measurement Unit) sensor functionality.

IsaacSensorComponentBase
Base class template for non-RTX Isaac sensors.

IsaacSensorManager
Manager class for handling Isaac physics-based sensors.

## Functions
uint64_tasInt (const pxr::SdfPath &path)
Converts a USD path to an integer representation.

floatlerp (const float &start, const float &end, const float t)
Linear interpolation between two values.

## Structs
ContactPair
Represents a pair of bodies in contact.

CsProperties
Properties configuration for a contact sensor.

CsRawData
Raw contact data from the physics simulation.

CsReading
Contact sensor reading data structure.

IsProperties
Properties configuration for an IMU sensor.

IsRawData
Raw IMU data from the physics simulation.

IsReading
IMU sensor reading data structure.

## Typedefs
IsaacBaseSensorComponent
Convenience typedef for IsaacSensorComponentBase with IsaacBaseSensor prim type.
