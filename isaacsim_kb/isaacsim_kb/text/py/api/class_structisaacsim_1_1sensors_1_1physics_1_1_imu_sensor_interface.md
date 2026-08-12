<!-- source: py/api/class_structisaacsim_1_1sensors_1_1physics_1_1_imu_sensor_interface.html | title: ImuSensorInterface — Isaac Sim -->

# ImuSensorInterface
Fully qualified name: `isaacsim::sensors::physics::ImuSensorInterface`
classImuSensorInterface

Interface for IMU (Inertial Measurement Unit) sensor functionality.
Provides methods for accessing IMU sensor data including acceleration, angular velocity, and orientation measurements.
Public Members
IsReading (*getSensorReading)(constchar*usdPath,conststd ::function<isaacsim ::sensors ::physics ::IsReading (std ::vector<isaacsim ::sensors ::physics ::IsReading >,float)>&interpolateFunction,constbool&getLatestValue,constbool&readGravity)

Gets Sensor last reading.
Gets the sensor last reading on its latest sensor period
Param usdPath:
sensor prim path

Param interpolationFunction:
interpolation functional pointer

Param getLatestValue:
flag for getting the latest sim value or the last sensor measured value

Param readGravity:
flag indicating whether to include gravity in the measurements

Return:
time-stamped sensor values.

bool(*isImuSensor)(constchar*usdPath)

Check is Prim an ImuSensorSchema.
Return True for is, False for is not an ImuSensorSchema
Param usdPath:
sensor prim path

Return:
true for is, false for is not an ImuSensorSchema
