<!-- source: py/api/class_structisaacsim_1_1sensors_1_1physx_1_1_light_beam_sensor_interface.html | title: LightBeamSensorInterface — Isaac Sim -->

# LightBeamSensorInterface
Fully qualified name: `isaacsim::sensors::physx::LightBeamSensorInterface`
classLightBeamSensorInterface

Interface for accessing light beam sensor functionality.
Provides methods to interact with light beam sensors that can detect intersections with objects in the scene.
Public Members
bool(*isLightBeamSensor)(constchar*usdPath)

Check is Prim a LightBeamSensorSchema.
Return True for is, False for is not an LightBeamSensorSchema
Param usdPath:
sensor prim path

Return:
true for is, false for is not an LightBeamSensorSchema

float*(*getLinearDepthData)(constchar*usdPath)

Gets the linear depth data buffer.
Param usdPath:
[in] Path to the sensor in the scene.

Return:
Pointer to the linear depth data buffer.

int(*getNumRays)(constchar*usdPath)

Gets the number of rays in the beam configuration.
Param usdPath:
[in] Path to the sensor in the scene.

Return:
Number of rays.

uint8_t*(*getBeamHitData)(constchar*usdPath)

Gets the beam hit data buffer.
Param usdPath:
[in] Path to the sensor in the scene.

Return:
Pointer to the beam hit data buffer.

carb::Float3*(*getHitPosData)(constchar*usdPath)

Gets the hit position data buffer.
Param usdPath:
[in] Path to the sensor in the scene.

Return:
Pointer to the hit position data buffer.

void(*getTransformData)(constchar*usdPath,omni ::math::linalg::matrix4d&matrixOutput)

Gets the transform data of the sensor.
Param usdPath:
[in] Path to the sensor in the scene.

Param matrixOutput:
[out]Transform matrix output.

carb::Float3*(*getBeamOrigins)(constchar*usdPath)

Gets the beam origin positions buffer.
Param usdPath:
[in] Path to the sensor in the scene.

Return:
Pointer to the beam origins buffer.

carb::Float3*(*getBeamEndPoints)(constchar*usdPath)

Gets the beam end points buffer.
Param usdPath:
[in] Path to the sensor in the scene.

Return:
Pointer to the beam end points buffer.
