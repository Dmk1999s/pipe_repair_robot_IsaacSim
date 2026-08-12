<!-- source: assets/usd_assets_nonvisual_sensors.html | title: Non-Visual Sensors — Isaac Sim Documentation -->

# Non-Visual Sensors
Isaac Sim models many types of non-visual sensors models, with digital twins found in the Content Browser under `Isaac Sim/Sensors`, organized into subfolders by manufacturer.
Some non-visual sensor types do not have digital twins. For more information about these sensors, including how to create them from the GUI, follow the links below:

- Contact sensors

- IMU sensors

- Lightbeam sensors

- PhysX Lidars

- RTX Radars

## RTX Lidars
RTX Lidars marked as “certified” have Lidar configurations verified by the sensor manufacturer and tested before release.
Some Lidar models feature multiple configurations or profiles, which are implemented as USD Variants . In those cases, the available variants and their characteristics will also be provided as tables in the appropriate section below.

### NVIDIA
There are several example Lidar configuration files that ship with Isaac Sim. Note none of these Lidars have a mesh, so only a prim will appear in the Stage window when they are created. To create them via the UI, select the appropriate option below from the menu: Create>Sensors>RTX Lidar>NVIDIA.

- Debug Rotary - a single emitter rotary Lidar configuration, used to debug simple rotary Lidar issues.

- Example Rotary 2D - a 10Hz rotary Lidar configuration with emitters in a single plane.

- Example Rotary - a 10Hz rotary Lidar configuration using a Gaussian beam ray type.

- Example Solid_State - a solid state Lidar configuration.

- Simple Example Solid State - a simple 12-emitter solid state Lidar configuration, used to debug solid state Lidar issues.

### HESAI

#### XT32 SD10
HESAI XT32 SD10 is a high precision, 32 Channels 360 degrees spinning mid range Lidar.
To create the sensor from the menu: Create>Sensors>RTX Lidar>HESAI>XT32 SD10
To create the sensor from the Content Browser: Isaac Sim>Sensors>HESAI>XT32_SD10>HESAI_XT32_SD10.usd
Features and Specification
[TABLE]
name | XT-32 10hz
type | lidar
scanRateBaseHz | 10.0
reportRateBaseHz | 20000
numberOfEmitters | 32
nearRangeM | 0.05
farRangeM | 120.0
rangeResolutionM | 0.004
rangeAccuracyM | 0.02
minDistBetweenEchos | 0.05
minReflectance | 0.1
minReflectanceRange | 80.0
wavelengthNm | 905.0
pulseTimeNs | 10
azimuthErrorMean | 0.0
azimuthErrorStd | 0.015
elevationErrorMean | 0.0
elevationErrorStd | 0.0
maxReturns | 2
[/TABLE]
Other Features

- Dimensions: 100 mm (Top Diameter) by 103 mm (Bottom Diameter) by 76.0 mm (Height)

Note
For the datasheet and full list of specifications, visit the XT32 SD10 product page.

### Ouster

#### OS0
Ouster OS0 is a high precision Lidar for autonomous vehicles, heavy machinery, robot, and mapping solutions. Isaac Sim has several pre-configured frequencies and resolutions that can be added to the stage easily.
To create the sensor from the menu: Create>Sensors>RTX Lidar>Ouster>OS0, then select the desired sensor configuration.
To create the sensor from the Content Browser: Isaac Sim>Sensors>Ouster>OS0>OS0.usd
Features and SpecificationOther Features

- Rotation Rate: 10 or 20 hz (configurable)

- Dimensions: 87 mm (Diameter) by 58.35 mm (Height). With thermal cap, height is 74.2 mm.

- IMU supported: InvenSense IAM-20680HT

Note
For the datasheet and full list of specifications, visit the OS0 product page.

#### OS1
Ouster OS1 is a high precision Lidar for autonomous vehicles, heavy machinery, robot, and mapping solutions. Isaac Sim has several pre-configured frequencies and resolutions that can be easily added to the stage.
To create the sensor from the menu: Create>Sensors>RTX Lidar>Ouster>OS1.
To create the sensor from the Content Browser: Isaac Sim>Sensors>Ouster>OS1>OS1.usd
Features and SpecificationOther Features

- Dimensions: 87 mm (Diameter) by 58.35 mm (Height). With thermal cap, height is 74.2 mm.

- IMU supported: InvenSense IAM-20680HT

Note
For the datasheet and full list of specifications, visit the OS1 product page.

#### OS2
Ouster OS2 is a high precision Lidar for autonomous vehicles, heavy machinery, robot, and mapping solutions. Isaac Sim has several pre-configured frequencies and resolutions that can be easily added to the stage.
To create the sensor from the menu: Create>Sensors>RTX Lidar>Ouster>OS2.
To create the sensor from the Content Browser: Isaac Sim>Sensors>Ouster>OS2>OS2.usd
Features and SpecificationOther Features

- Dimensions: 87 mm (Diameter) by 58.35 mm (Height). With thermal cap, height is 74.2 mm.

- IMU supported: InvenSense IAM-20680HT

Note
For the datasheet and full list of specifications, visit the OS2 product page.

#### VLS 128
Ouster VLS 128 is a long range, ultra high resolution 3D Lidar for autonomous vehicles.
To create the sensor from the menu: Create>Sensors>RTX Lidar>Ouster>VLS 128
To create the sensor from the Content Browser: Isaac Sim>Sensors>Ouster>VLS_128>Ouster_VLS_128.usd
Features and Specification
[TABLE]
name | Velodyne VLS-128
type | lidar
scanRateBaseHz | 10.0
reportRateBaseHz | 18761
numberOfEmitters | 128
nearRangeM | 1.0
farRangeM | 200.0
rangeResolutionM | 0.004
rangeAccuracyM | 0.02
minReflectance | 0.1
minReflectanceRange | 120.0
wavelengthNm | 903.0
pulseTimeNs | 6
maxReturns | 2
[/TABLE]
Other Features

- Dimensions: 165.5 mm (Diameter) by 141.3 mm (Height)

- Operating Temperature: -20C to 60C

Note
VLS 128 product page.

### SICK

#### microScan3 (Certified)
The SICK microScan3 safety laser scanner stands for the protection of very different applications: from stationary to mobile, from simple to complex and delivers high-precision measurement data.

##### Features and Specification

[TABLE]
Profile | Protective field range | Scan frequency
Profile_1 | 4.0 m | 33.3 Hz
Profile_2 | 4.0 m | 25.0 Hz
Profile_3 | 5.5 m | 33.3 Hz
Profile_4 | 5.5 m | 25.0 Hz
Profile_5 | 9.0 m | 25.0 Hz
Profile_6 | 9.0 m | 20.0 Hz
[/TABLE]
ℹ️ Note For the datasheet and full list of specifications, visit the microScan3 product page .

To create the sensor from the menu: Create>Sensors>RTX Lidar>SICK>microScan3
To create the sensor from the Content Browser: Isaac Sim>Sensors>SICK>microScan3>SICK_microScan3.usd

#### multiScan136 (Certified)
The SICK multiScan136 of the multiScan100 family is a 3D LiDAR sensor for mobile and stationary applications and reliably detects drop-off edges and obstacles ahead.
ℹ️ Note For the datasheet and full list of specifications, visit the multiScan136 product page .

To create the sensor from the menu: Create>Sensors>RTX Lidar>SICK>multiScan136
To create the sensor from the Content Browser: Isaac Sim>Sensors>SICK>multiScan136>SICK_multiScan136.usd

#### multiScan165 (Certified)
The SICK multiScan165 of the multiScan100 family is a 3D LiDAR sensor for mobile and stationary applications and reliably detects drop-off edges and obstacles ahead.
ℹ️ Note For the datasheet and full list of specifications, visit the multiScan165 product page .

To create the sensor from the menu: Create>Sensors>RTX Lidar>SICK>multiScan165
To create the sensor from the Content Browser: Isaac Sim>Sensors>SICK>multiScan165>SICK_multiScan165.usd

#### nanoScan3 (Certified)
The SICK nanoScan3 is the smallest safety laser scanner, which is well suited for the protection and localization of mobile platforms.

##### Features and Specification
ℹ️ Note For the datasheet and full list of specifications, visit the nanoScan3 product page .

To create the sensor from the menu: Create>Sensors>RTX Lidar>SICK>nanoScan3
To create the sensor from the Content Browser: Isaac Sim>Sensors>SICK>nanoScan3>SICK_nanoScan3.usd

#### picoScan150 (Certified)
The SICK picoScan150 of the picoScan100 family is a 2D LiDAR sensor for solving demanding industrial applications such as collision avoidance or measurement and monitoring in indoor and outdoor areas.

##### Features and Specification

[TABLE]
Profile | Scan frequency | Angular resolution
Profile_1 | 15 Hz | 0.5°
Profile_2 | 15 Hz | 0.33°
Profile_3 | 20 Hz | 0.1°
Profile_4 | 20 Hz | 0.25°
Profile_5 | 25 Hz | 0.25°
Profile_6 | 30 Hz | 0.1°
Profile_7 | 40 Hz | 0.25°
Profile_8 | 50 Hz | 0.25°
Profile_9 | 15 Hz | 0.05°
Profile_10 | 40 Hz | 0.125°
Profile_11 | 15 Hz | 1.0°
[/TABLE]
ℹ️ Note For the datasheet and full list of specifications, visit the picoScan150 product page .

To create the sensor from the menu: Create>Sensors>RTX Lidar>SICK>picoScan150
To create the sensor from the Content Browser: Isaac Sim>Sensors>SICK>picoScan150>SICK_picoScan150.usd

#### TiM781 (Certified)
The SICK TiM781 of the TiM family is a 2D LiDAR sensor for collision protection for mobile applications, object measurement or monitoring of objects.
ℹ️ Note For the datasheet and full list of specifications, visit the TiM781 product page .

To create the sensor from the menu: Create>Sensors>RTX Lidar>SICK>TiM781
To create the sensor from the Content Browser: Isaac Sim>Sensors>SICK>tim781.usd

### SLAMTEC

#### RPLIDAR S2E
SLAMTEC RPLIDAR S2E is a low cost 360 degrees 2D laser scanner Lidar from SLAMTEC.
To create the sensor from the menu: Create>Sensors>RTX Lidar>Slamtec>RPLIDAR S2E
To create the sensor from the Content Browser: Isaac Sim>Sensors>Slamtec>RPLIDAR_S2E.usd
Features and Specification
[TABLE]
name | RPLIDAR S2E
type | lidar
scanRateBaseHz | 10.0
reportRateBaseHz | 32000
numberOfEmitters | 1
nearRangeM | 0.05
farRangeM | 30.0
rangeResolutionM | 0.013
rangeAccuracyM | 0.03
minDistBetweenEchos | 0.05
minReflectance | 0.1
minReflectanceRange | 10.0
wavelengthNm | 905.0
pulseTimeNs | 5
azimuthErrorMean | 0.0
azimuthErrorStd | 0.0
elevationErrorMean | 0.0
elevationErrorStd | 0.0
maxReturns | 1
[/TABLE]
Note
For the datasheet and full list of specifications, vist the RPLIDAR S2 product page.

### ZVISION

#### ML-30s+ (Certified)
ZVISION ML-30s+ is a short range automotive grade solid state Lidar. Note there is no mesh for this lidar, so when it is created via the UI, only a prim will appear in the Stage window.
Features and Specification
[TABLE]
name | ML-30s+
type | lidar
scanRateBaseHz | 10.0
reportRateBaseHz | 10
numberOfEmitters | 51200
numberOfChannels | 51200
nearRangeM | 0.2
farRangeM | 45.0
effectiveApertureSize | 0.01
focusDistM | 0.12
rangeResolutionM | 0.03
rangeAccuracyM | 0.03
minDistBetweenEchos | 0.2
minReflectance | 0.1
minReflectanceRange | 270.0
wavelengthNm | 905.0
pulseTimeNs | 6
azimuthErrorMean | 0.0
azimuthErrorStd | 0.025
elevationErrorMean | 0.0
elevationErrorStd | 0.025
maxReturns | 2
[/TABLE]
To create the sensor from the menu: Create>Sensors>RTX Lidar>ZVISION>ML30S+
To create the sensor from the Content Browser: Isaac Sim>Sensors>ZVISION>ZVISION_ML30S.usda
Note
For the datasheet and full list of specifications, visit the ML-30s+ product page.

#### ML-Xs (Certified)
ZVISION ML-Xs is a long range automotive high performance grade solid state Lidar. Note there is no mesh for this lidar, so when it is created via the UI, only a prim will appear in the Stage window.
Features and Specification
[TABLE]
name | ML-Xs
type | lidar
scanRateBaseHz | 10.0
reportRateBaseHz | 10
numberOfEmitters | 108000
numberOfChannels | 108000
nearRangeM | 0.5
farRangeM | 250
effectiveApertureSize | 0.01
focusDistM | 0.12
rangeResolutionM | 0.03
rangeAccuracyM | 0.05
minReflectance | 0.1
minReflectanceRange | 270.0
wavelengthNm | 1550.0
pulseTimeNs | 6
azimuthErrorMean | 0.0
azimuthErrorStd | 0.025
elevationErrorMean | 0.0
elevationErrorStd | 0.025
maxReturns | 2
[/TABLE]
To create the Lidar prim: Create>Sensors>RTX Lidar>ZVISION>MLXS
To create the sensor from the Content Browser: Isaac Sim>Sensors>ZVISION>ZVISION_MLXS.usda
Note
For the datasheet and full list of specifications, visit the ML-Xs product page.

## Tactile Sensors

### Tashan Technology

#### Universal Tactile Sensor TS-F-A (Certified)
Tashan Technology Universal Tactile Sensor TS-F-A is a tactile simulation model based on real products to advance research and innovation in robotic tactile perception technology and promote the development of embodied intelligent robots.
Features and SpecificationOutputs 11 dimensional feature channels:

- Proximity sensing [1]

- Tactile sensing [2-4]: Normal force, tangential force, tangential force direction

- Raw capacitance values [5-11]: 7-channel raw capacitance data

To create the sensor from the Content Browser: Isaac Sim>Sensors>Tashan>TS-F-A>TS-F-A.usd
Note
For usage in Isaac Sim, visit the Tashan Technology Tactile Simulation Platform User Manual.

## Sensor Gizmo in Viewport
In Isaac Sim, the sensor functions are decoupled from physical meshes, and you can have sensors on stage without any mesh associated with the sensor. We use sensor gizmo to track the location of the actual sensing functions regardless of mesh. The gizmos are not visible by default, but you can toggle them on or off in the viewport.
To toggle the sensor gizmos, go to Viewport Menu > > Show By Type > Sensors.
