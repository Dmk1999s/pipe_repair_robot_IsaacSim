<!-- source: py/api/classisaacsim_1_1sensors_1_1rtx_1_1_lidar_config_helper.html | title: LidarConfigHelper — Isaac Sim -->

# LidarConfigHelper
Fully qualified name: `isaacsim::sensors::rtx::LidarConfigHelper`

## Structs
EmitterState
Configuration state for individual LiDAR emitters.

classLidarConfigHelper

Helper class for managing LiDAR sensor configuration.
Provides utilities for handling LiDAR profiles, scan types, and configuration parameters. Manages the storage and access of LiDAR-specific settings and profile data. Supports both rotary and solid-state LiDAR configurations with customizable parameters such as scan rates, resolution, and emitter configurations.
Public Types
enumclassLidarRotationDirection

Defines the rotation direction of the LiDAR scanner.
Specifies whether the LiDAR sensor rotates clockwise or counterclockwise during scanning. This affects the order in which points are collected during a scan.
Values:
enumeratorCW

Clockwise rotation direction.

enumeratorCCW

Counterclockwise rotation direction.

Public Functions
floatgetNearRange()const

Gets the minimum range of the LiDAR sensor.

floatgetFarRange()const

Gets the maximum range of the LiDAR sensor.

uint32_tgetNumChannels()const

Gets the number of vertical channels in the LiDAR.

uint32_tgetNumEchos()const

Gets the number of echoes per beam.

uint32_tgetReturnsPerScan()const

Gets the total number of returns per complete scan.

uint32_tgetTicksPerScan()const

Gets the number of ticks required for a complete scan.

boolupdateLidarConfig(constchar*renderProductPath)

Updates the LiDAR configuration from a render product path.
Parameters:
renderProductPath – [in] Path to the render product configuration

Throws:
std ::runtime_error – If the configuration file cannot be read or parsed

Returns:
True if update was successful, false otherwise

voidinit(constchar*json)

init document
Parameters:
json – [in] json file name with path

omni ::stringgetProfileJsonAtPaths(constchar*fileName)

Gets JSON content from given filename.
Searches for the JSON file in internal paths or at given paths
Parameters:
fileName – [in] JSON file name with path

Throws:
std ::runtime_error – If the file cannot be found or read

Returns:
String containing the JSON content from the file

Public Members
std ::stringconfig

Configuration string for the LiDAR sensor.

LidarScanType scanType={LidarScanType ::kUnknown }

Type of LiDAR scanning pattern.

floatnearRangeM={0.3f}

Minimum range of the LiDAR sensor in meters.

floatfarRangeM={200.0f}

Maximum range of the LiDAR sensor in meters.

floatazimuthStartDeg={0.0f}

Start azimuth angle of the LiDAR sensor in degrees.

floatazimuthEndDeg={360.0f}

End azimuth angle of the LiDAR sensor in degrees.

floathorizontalResolutionDeg={0.1f}

Horizontal resolution of the LiDAR sensor in degrees.

uint32_treportRateBaseHz={36000}

Report rate base frequency of the LiDAR sensor in Hz.

uint32_tscanRateBaseHz={10}

Rotation rate of the LiDAR sensor in Hz.

uint32_tnumberOfEmitters={128}

Number of emitters in the LiDAR sensor.

uint32_temitterStateCount={0}

Number of configured emitter states.
Count of valid entries in the emitterStates vector that define emitter configurations. This may be less than the total number of emitters if some are not configured.

uint32_tmaxReturns={2}

Maximum number of returns per laser beam.
Specifies the maximum number of echo returns that can be detected from a single laser pulse. Higher values allow for better detection of partially transparent or reflective surfaces.

std ::vector<uint32_t>numRaysPerLine

Number of rays per scan line.
Vector specifying the number of laser rays for each horizontal scan line in the LiDAR pattern. This determines the vertical resolution of the scan.

std ::vector<EmitterState >emitterStates

Configuration states for all emitters.
Vector containing EmitterState configurations that define the angular positioning of each emitter. Each entry specifies the elevation and azimuth angles for a specific emitter.

uint32_tnumLines={1}

Number of vertical scan lines.
Total number of horizontal scan lines that make up the complete LiDAR scan pattern. This determines the vertical field of view and resolution.

LidarRotationDirection rotationDirection={LidarRotationDirection ::CW }

Rotation direction of the LiDAR scanner.
Specifies whether the scanner rotates clockwise or counterclockwise during operation. This affects the order in which points are collected during a scan.

boolis2D={false}

Whether the LiDAR sensor is 2D (single line) or 3D (multiple lines)

std ::unique_ptr<rapidjson::Document>m_doc={nullptr}

JSON document for configuration parsing.
Smart pointer to rapidjson document used for parsing LiDAR configuration files. This is used to store and process the JSON configuration data.

Public Static Functions
staticstd ::stringReadWholeTextFile(conststd ::string&fullPath)

Reads the entire contents of a text file.
Utility function for reading complete text files into memory as a string. Used for loading configuration files and other text-based data.
Parameters:
fullPath – [in] Complete file path to the text file to read

Throws:
std ::runtime_error – If file cannot be opened or read

Returns:
String containing the complete file contents

structEmitterState

Configuration state for individual LiDAR emitters.
Contains the angular configuration for LiDAR emitters, defining their pointing directions in spherical coordinates. This structure stores elevation and azimuth angles that determine where each emitter points in 3D space.
Public Members
std ::vector<float>elevationDeg{-15.0f,-14.19f,-13.39f,-12.58f,-11.77f,-10.97f,-10.16f,-9.35f,-8.55f,-7.74f,-6.94f,-6.13f,-5.32f,-4.52f,-3.71f,-2.9f,-2.1f,-1.29f,-0.48f,0.32f,1.13f,1.94f,2.74f,3.55f,4.35f,5.16f,5.97f,6.77f,7.58f,8.39f,9.19f,10.0f,-15.0f,-14.19f,-13.39f,-12.58f,-11.77f,-10.97f,-10.16f,-9.35f,-8.55f,-7.74f,-6.94f,-6.13f,-5.32f,-4.52f,-3.71f,-2.9f,-2.1f,-1.29f,-0.48f,0.32f,1.13f,1.94f,2.74f,3.55f,4.35f,5.16f,5.97f,6.77f,7.58f,8.39f,9.19f,10.0f,-15.0f,-14.19f,-13.39f,-12.58f,-11.77f,-10.97f,-10.16f,-9.35f,-8.55f,-7.74f,-6.94f,-6.13f,-5.32f,-4.52f,-3.71f,-2.9f,-2.1f,-1.29f,-0.48f,0.32f,1.13f,1.94f,2.74f,3.55f,4.35f,5.16f,5.97f,6.77f,7.58f,8.39f,9.19f,10.0f,-15.0f,-14.19f,-13.39f,-12.58f,-11.77f,-10.97f,-10.16f,-9.35f,-8.55f,-7.74f,-6.94f,-6.13f,-5.32f,-4.52f,-3.71f,-2.9f,-2.1f,-1.29f,-0.48f,0.32f,1.13f,1.94f,2.74f,3.55f,4.35f,5.16f,5.97f,6.77f,7.58f,8.39f,9.19f,10.0f}

Elevation angles for each emitter in degrees.
Array of elevation angles (vertical angles) for LiDAR emitters, measured from horizontal plane. Negative values point downward, positive values point upward. Values typically range from -15.0 to 10.0 degrees.

std ::vector<float>azimuthDeg{-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-3.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,-1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,1.0f,3.0f,3.0f,3.0f,3.0f,3.0f,3.0f,3.0f,3.0f,3.0f,3.0f,3.0f,3.0f,3.0f,3.0f,3.0f,3.0f,3.0f,3.0f,3.0f,3.0f,3.0f,3.0f,3.0f,3.0f,3.0f,3.0f,3.0f,3.0f,3.0f,3.0f,3.0f,3.0f}

Azimuth angles for each emitter in degrees.
Array of azimuth angles (horizontal angles) for LiDAR emitters, measured from forward direction. Negative values point to the left, positive values point to the right. Values typically range from -3.0 to 3.0 degrees.
