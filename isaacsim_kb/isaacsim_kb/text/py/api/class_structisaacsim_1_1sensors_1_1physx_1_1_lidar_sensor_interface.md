<!-- source: py/api/class_structisaacsim_1_1sensors_1_1physx_1_1_lidar_sensor_interface.html | title: LidarSensorInterface — Isaac Sim -->

# LidarSensorInterface
Fully qualified name: `isaacsim::sensors::physx::LidarSensorInterface`
classLidarSensorInterface

Interface for accessing LIDAR sensor data and properties.
Provides methods to access various aspects of LIDAR sensor data including depth measurements, beam timing, point clouds, and sensor configuration.
Public Members
int(*getNumCols)(constchar*sensorPath)

Gets the number of columns in the LIDAR scan pattern.
Param sensorPath:
[in] Path to the sensor in the scene.

Return:
Number of columns in the scan pattern.

int(*getNumRows)(constchar*sensorPath)

Gets the number of rows in the LIDAR scan pattern.
Param sensorPath:
[in] Path to the sensor in the scene.

Return:
Number of rows in the scan pattern.

int(*getNumColsTicked)(constchar*sensorPath)

Gets the number of columns processed in the current tick.
Param sensorPath:
[in] Path to the sensor in the scene.

Return:
Number of columns processed.

uint16_t*(*getDepthData)(constchar*sensorPath)

Gets the raw depth data buffer.
Param sensorPath:
[in] Path to the sensor in the scene.

Return:
Pointer to the depth data buffer.

float*(*getBeamTimeData)(constchar*sensorPath)

Gets the beam timing data buffer.
Param sensorPath:
[in] Path to the sensor in the scene.

Return:
Pointer to the beam time data buffer.

float*(*getLinearDepthData)(constchar*sensorPath)

Gets the linear depth data buffer.
Param sensorPath:
[in] Path to the sensor in the scene.

Return:
Pointer to the linear depth data buffer.

uint8_t*(*getIntensityData)(constchar*sensorPath)

Gets the intensity data buffer.
Param sensorPath:
[in] Path to the sensor in the scene.

Return:
Pointer to the intensity data buffer.

float*(*getZenithData)(constchar*sensorPath)

Gets the zenith angle data buffer.
Param sensorPath:
[in] Path to the sensor in the scene.

Return:
Pointer to the zenith angle data buffer.

float*(*getAzimuthData)(constchar*sensorPath)

Gets the azimuth angle data buffer.
Param sensorPath:
[in] Path to the sensor in the scene.

Return:
Pointer to the azimuth angle data buffer.

carb::Float3*(*getPointCloud)(constchar*sensorPath)

Gets the point cloud data buffer.
Param sensorPath:
[in] Path to the sensor in the scene.

Return:
Pointer to the point cloud data buffer.

std ::vector<std ::string>(*getPrimData)(constchar*sensorPath)

Gets the primitive data for hit objects.
Param sensorPath:
[in] Path to the sensor in the scene.

Return:
Vector of primitive paths that were hit.

bool(*isLidarSensor)(constchar*sensorPath)

Checks if a given path refers to a LIDAR sensor.
Param sensorPath:
[in] Path to check.

Return:
True if path refers to a LIDAR sensor, false otherwise.

uint64_t(*getSequenceNumber)(constchar*sensorPath)

Gets the sequence number of the current scan.
Param sensorPath:
[in] Path to the sensor in the scene.

Return:
Current sequence number.

carb::Float2(*getAzimuthRange)(constchar*sensorPath)

Gets the azimuth angle range of the sensor.
Param sensorPath:
[in] Path to the sensor in the scene.

Return:
Azimuth range as (min, max) angles.

carb::Float2(*getZenithRange)(constchar*sensorPath)

Gets the zenith angle range of the sensor.
Param sensorPath:
[in] Path to the sensor in the scene.

Return:
Zenith range as (min, max) angles.
