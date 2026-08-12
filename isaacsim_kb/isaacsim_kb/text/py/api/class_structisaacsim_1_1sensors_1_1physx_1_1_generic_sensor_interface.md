<!-- source: py/api/class_structisaacsim_1_1sensors_1_1physx_1_1_generic_sensor_interface.html | title: GenericSensorInterface — Isaac Sim -->

# GenericSensorInterface
Fully qualified name: `isaacsim::sensors::physx::GenericSensorInterface`
classGenericSensorInterface

Interface for accessing generic range sensor functionality.
Provides methods to interact with configurable range sensors that can be customized for different scanning patterns and behaviors.
Public Members
bool(*isGenericSensor)(constchar*sensorPath)

Checks if a given path refers to a generic sensor.
Param sensorPath:
[in] Path to check.

Return:
True if path refers to a generic sensor, false otherwise.

int(*getNumSamplesTicked)(constchar*sensorPath)

Gets the number of samples processed in the current tick.
Param sensorPath:
[in] Path to the sensor in the scene.

Return:
Number of samples processed.

uint16_t*(*getDepthData)(constchar*sensorPath)

Gets the depth data buffer.
Param sensorPath:
[in] Path to the sensor in the scene.

Return:
Pointer to the depth data buffer.

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

carb::Float3*(*getOffsetData)(constchar*sensorPath)

Gets the offset data buffer.
Param sensorPath:
[in] Path to the sensor in the scene.

Return:
Pointer to the offset data buffer.

bool(*sendNextBatch)(constchar*sensorPath)

Sends the next batch of ray configurations to be processed.
Param sensorPath:
[in] Path to the sensor in the scene.

Return:
True if batch was sent successfully, false otherwise.

void(*setNextBatchRays)(constchar*sensorPath,constfloat*azimuthAngles,constfloat*zenithAngles,constintsampleLength)

Sets the ray configuration for the next batch.
Param sensorPath:
[in] Path to the sensor in the scene.

Param azimuth_angles:
[in] Array of azimuth angles for each ray.

Param zenith_angles:
[in] Array of zenith angles for each ray.

Param sample_length:
[in] Number of rays in the batch.

void(*setNextBatchOffsets)(constchar*sensorPath,constfloat*originOffsets,constintsampleLength)

Sets the origin offsets for the next batch of rays.
Param sensorPath:
[in] Path to the sensor in the scene.

Param origin_offsets:
[in] Array of origin offsets for each ray.

Param sample_length:
[in] Number of rays in the batch.
