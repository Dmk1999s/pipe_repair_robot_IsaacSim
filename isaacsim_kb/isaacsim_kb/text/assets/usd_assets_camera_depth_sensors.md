<!-- source: assets/usd_assets_camera_depth_sensors.html | title: Camera and Depth Sensors — Isaac Sim Documentation -->

# Camera and Depth Sensors
Isaac Sim supports camera and depth sensors, with digital twins found in the Content Browser
under `Isaac Sim/Sensors`, organized into subfolders by manufacturer.

## Cameras
For more information about camera modeling in Isaac Sim, see here .

### Leopard Imaging

#### Hawk Stereo Camera
The Hawk Stereo Camera (LI-AR0234CS-STEREO-GMSL2-30 ) from Leopard Imaging consists of two OnSemi AR0234CS RGB image sensors and a 6-axis IMU, both are simulated in the NVIDIA Isaac Sim.
To create the camera from the menu: Create>Sensors>Camera and Depth Sensors>LeopardImaging>Hawk
To create the sensor from the Content Browser: Isaac Sim>Sensors>LeopardImaging>Hawk>hawk_v1.1_nominal.usd
Features and Specification
[TABLE]
name | camera_left | camera_right
focalLength | 2.8734347820281982 | 2.8779797554016113
focusDistance | 0.6000000238418579 | 0.6000000238418579
fStop | 240.0 | 240.0
projection | perspective | perspective
stereoRole | left | right
horizontalAperture | 5.760000228881836 | 5.760000228881836
verticalAperture | 3.5999999046325684 | 3.5999999046325684
clippingRange | (0.076, 100000) | (0.076, 100000)
cameraProjectionType | fisheyePolynomial | fisheyePolynomial
nominalWidth | 1920.0 | 1920.0
nominalHeight | 1200.0 | 1200.0
opticalCenterX | 957.85107421875 | 954.709228515625
opticalCenterY | 589.5376586914062 | 588.3735961914062
maxFOV | 150.0 | 150.0
polyK0 | 5.0055230531143025e-05 | 8.962746505858377e-05
polyK1 | 0.0010426010703667998 | 0.001039923052303493
polyK2 | 9.85131620723223e-09 | 1.502240820627776e-08
polyK3 | 1.6426542417957712e-11 | 5.982795422271314e-12
polyK4 | 2.9886398802796144e-14 | 3.6818906078281075e-14
polyK5 | 0.0 | 0.0
p0 | -0.00037 | -0.00037
p1 | -0.00074 | -0.00074
s0 | -0.00058 | -0.00058
s1 | -0.00022 | -0.00022
s2 | 0.00019 | 0.00019
s3 | -0.0002 | -0.0002
physicalDistortionCoefficients | [0.147811, -0.032313, -0.000194, -0.000035, 0.008823, 0.517913, -0.06708, 0.01695] | [6.815791, 5.172144, -0.000246, -0.000128, 0.353267, 7.180808, 7.640372, 1.596375]
physicalDistortionModel | rational_polynomial | rational_polynomial
[/TABLE]
Other Features

- Waterproof: IP65

- Dimensions: 180 mm (length) by 44.33 mm (depth) by 25.0 mm (height)

- Operating Temperature: -20C to 50C

IMU to Hawk sensor (left camera) transformation in Isaac Sim
[TABLE]
Transformation | x | y | z
Rotation (degrees) | 0.0 | 90 | 0.0
Translation (meters) | 0.0 | -0.0947 | 0.0061
[/TABLE]
Note
For the datasheet and full list of specifications, visit the Hawk stereo camera product page and purchase here .

#### Owl Fisheye camera
The Owl camera (LI-AR0234CS-GMSL2-OWL ) from Leopard Imaging consists of a 2.3MP OnSemi AR0234CS RGB image sensor, capable of producing crisp images in low-light and bright scenes.
To create the camera from the menu: Create>Sensors>Camera and Depth Sensors>LeopardImaging>Owl
To create the sensor from the Content Browser: Isaac Sim>Sensors>LeopardImaging>Owl>owl.usd
Features and Specification
[TABLE]
name | camera
focalLength | 1.3646053075790405
focusDistance | 0.6000000238418579
fStop | 180.0
projection | perspective
stereoRole | mono
horizontalAperture | 5.760000228881836
verticalAperture | 3.5999999046325684
clippingRange | (0.076, 100000)
cameraProjectionType | fisheyePolynomial
nominalWidth | 1920.0
nominalHeight | 1200.0
opticalCenterX | 943.99462890625
opticalCenterY | 602.3110961914062
maxFOV | 235.0
polyK0 | 0.0002725422091316432
polyK1 | 0.0021866457536816597
polyK2 | 1.2340817079348199e-07
polyK3 | -1.079574096785052e-09
polyK4 | 5.997452426180494e-13
polyK5 | 0.0
p0 | -0.00037
p1 | -0.00074
s0 | -0.00058
s1 | -0.00022
s2 | 0.00019
s3 | -0.0002
physicalDistortionCoefficients | [0.057225, 0.012671, -0.002978, -0.000472]
physicalDistortionModel | kannalaBrandt
[/TABLE]
Other Features

- Dimensions: 50 mm (length) by 37.63 mm (depth) by 25.0 mm (height)

- Operating Temperature: -20C to 50C

Note
For full list of specifications, visit the product page ,and the owl cameras can be purchased here .

### Sensing

#### SG2-AR0233C-5200-G2A-H100F1A Camera (Certified by Sensing)
SG2-AR0233C-5200-G2A-H100F1A from the SG2-AR0233C-5200-G2A-Hxxx Series is a megapixel high performance automotive camera module, primarily used for ADAS, HDR imaging functionalities.
To create the camera from the menu: Create>Sensors>Camera and Depth Sensors>Sensing>Sensing SG2-AR0233C-5200-G2A-H100F1A
To create the sensor from the Content Browser: Isaac Sim>Sensors>Sensing>SG2>H100F1A>SG2-AR0233C-5200-G2A-H100F1A.usd
Features and Specification
[TABLE]
name | SG2_AR0233C_5200_G2A_H100F1A_01
focalLength | 3.549999952316284
focusDistance | 270.0
fStop | 1.600000023841858
projection | perspective
stereoRole | mono
horizontalAperture | 5.760000228881836
verticalAperture | 3.240000009536743
clippingRange | (1, 1000000)
cameraProjectionType | fisheyeOrthographic
nominalWidth | 1920.0
nominalHeight | 1080.0
opticalCenterX | 998.0842895507812
opticalCenterY | 520.5062866210938
maxFOV | 100.0
polyK0 | 0.9293811321258545
polyK1 | 0.15743136405944824
polyK2 | 0.008131147362291813
polyK3 | 1.358112096786499
polyK4 | 0.4388065040111542
polyK5 | 0.035474397242069244
p0 | -1.8616799934534356e-05
p1 | -0.000114203299744986
s0 | 0.0
s1 | 0.0
s2 | 0.0
s3 | 0.0
physicalDistortionCoefficients | Not Applicable
physicalDistortionModel | Not Applicable
[/TABLE]
Other Features

- Waterproof: IP67

- Dimensions: 30 mm (length) by 22.5 mm (depth) by 30 mm (height)

- Operating Temperature: -40C to 85C

Note
For the datasheet and full list of specifications, visit the SG2-AR0233C-5200-G2A-Hxxx series product page.

#### SG2-OX03CC-5200-GMSL2-H60YA Series Camera (Certified by Sensing)
SG2-OX03CC-5200-GMSL2-H60YA from the SG2-OX03CC-5200-GMSL2-Hxxx Series is a megapixel high performance automotive camera module, primarily used for ADAS, HDR imaging functionalities.
To create the camera from the menu: Create>Sensors>Camera and Depth Sensors>Sensing>Sensing SG2-OX03CC-5200-GMSL2-H60YA
To create the sensor from the Content Browser: Isaac Sim>Sensors>Sensing>SG2>H60YA>Camera_SG2_OX03CC_5200_GMSL2_H60YA.usd
Features and Specification
[TABLE]
name | Camera_SG2_OX03CC_5200_GMSL2_H60YA
focalLength | 5.75
focusDistance | 700.0
fStop | 1.600000023841858
projection | perspective
stereoRole | mono
horizontalAperture | 5.760000228881836
verticalAperture | 3.240000009536743
clippingRange | (0.1, 1000000)
cameraProjectionType | fisheyeOrthographic
nominalWidth | 1920.0
nominalHeight | 1080.0
opticalCenterX | 959.595947265625
opticalCenterY | 647.6140747070312
maxFOV | 60.0
polyK0 | 0.7182272672653198
polyK1 | 60.113136291503906
polyK2 | 2.598527431488037
polyK3 | 1.1977670192718506
polyK4 | 60.394771575927734
polyK5 | 31.610383987426758
p0 | 0.0004008802934549749
p1 | -0.0013344850158318877
s0 | 0.0
s1 | 0.0
s2 | 0.0
s3 | 0.0
physicalDistortionCoefficients | Not Applicable
physicalDistortionModel | Not Applicable
[/TABLE]
Other Features

- Waterproof: IP67

- Dimensions: 30 mm (length) by 22.5 mm (depth) by 30 mm (height)

- Operating Temperature: -40C to 85C

Note
For the datasheet and full list of specifications, visit the SG2-OX03CC-5200-GMSL2F-Hxxx series product page.

#### SG3-ISX031C-GMSL2F-H190XA (Certified by Sensing)
SG3-ISX031C-GMSL2F-H190XA is a 3 megapixels automotive camera for automotive surround view.
To create the camera from the menu: Create>Sensors>Camera and Depth Sensors>Sensing>Sensing SG3-ISX031C-GMSL2F-H190XA
To create the sensor from the Content Browser: Isaac Sim>Sensors>Sensing>SG3>H190XA>SG3S-ISX031C-GMSL2F-H190XA.usd
Features and Specification
[TABLE]
name | SG3S_ISX031C_GMSL2F_H190XA_01
focalLength | 1.5099999904632568
focusDistance | 39.0
fStop | 2.0
projection | perspective
stereoRole | mono
horizontalAperture | 5.760000228881836
verticalAperture | 4.607999801635742
clippingRange | (1, 1000000)
cameraProjectionType | fisheyeEquidistant
nominalWidth | 1920.0
nominalHeight | 1536.0
opticalCenterX | 960.6082153320312
opticalCenterY | 768.0
maxFOV | 190.0
polyK0 | 0.13215887546539307
polyK1 | -0.031036589294672012
polyK2 | -0.004391151946038008
polyK3 | 0.0018116832943633199
polyK4 | 0.0
polyK5 | 0.0
p0 | 0.0
p1 | 0.0
s0 | 0.0
s1 | 0.0
s2 | 0.0
s3 | 0.0
physicalDistortionCoefficients | Not Applicable
physicalDistortionModel | Not Applicable
[/TABLE]
Other Features

- Waterproof: IP67

- Dimensions: 30 mm (length) by 22.5 mm (depth) by 30 mm (height)

- Operating Temperature: -40C to 85C

Note
For the datasheet and full list of specifications, visit the SG3-ISX031C-GMSL2F-Hxxx series product page.

#### SG5-IMX490C-5300-GMSL2-H110SA (Certified by Sensing)
SG5-IMX490C-5300-GMSL2-H110SA is a 5 megapixels automotive camera for automotive surround view, ADAS and viewing fusion.
To create the camera from the menu: Create>Sensors>Camera and Depth Sensors>Sensing>Sensing SG5-IMX490C-5300-GMSL2-H110SA
To create the sensor from the Content Browser: Isaac Sim>Sensors>Sensing>SG5>H100SA>SG5-IMX490C-5300-GMSL2-H110SA.usd
Features and Specification
[TABLE]
name | Camera_SG5_IMX490C_5300_GMSL2_H110SA
focalLength | 4.260000228881836
focusDistance | 220.0
fStop | 2.799999952316284
projection | perspective
stereoRole | mono
horizontalAperture | 8.640000343322754
verticalAperture | 5.579999923706055
clippingRange | (1, 1000000)
cameraProjectionType | fisheyeOrthographic
nominalWidth | 2880.0
nominalHeight | 1860.0
opticalCenterX | 1442.3316650390625
opticalCenterY | 926.6644287109375
maxFOV | 110.0
polyK0 | 0.6106576919555664
polyK1 | -0.11334560066461563
polyK2 | -0.014692608267068863
polyK3 | 0.9237731099128723
polyK4 | -0.011052233166992664
polyK5 | -0.051484767347574234
p0 | 2.2259799152379856e-05
p1 | -7.929380080895498e-05
s0 | 0.0
s1 | 0.0
s2 | 0.0
s3 | 0.0
physicalDistortionCoefficients | Not Applicable
physicalDistortionModel | Not Applicable
[/TABLE]
Other Features

- Waterproof: IP67

- Dimensions: 30 mm (length) by 22.5 mm (depth) by 30 mm (height)

- Operating Temperature: -40C to 85C

- Multi camera synchronization support

Note
For the datasheet and full list of specifications, visit the SG5-IMX490C-5300-GMSL2-Hxxx series product page.

#### SG8S-AR0820C-5300-G2A-H30YA Camera (Certified by Sensing)
SG8S-AR0820C-5300-G2A-H30YA is a 4k high performance automotive grade camera that supports advanced on sensor HDR and multi-camera synchronization.
To create the camera from the menu: Create>Sensors>Camera and Depth Sensors>Sensing>Sensing SG8S-AR0820C-5300-G2A-H30YA
To create the sensor from the Content Browser: Isaac Sim>Sensors>Sensing>SG8>H30YA>SG8S-AR0820C-5300-G2A-H30YA.usd
Features and Specification
[TABLE]
name | SG8S_AR0820C_5300_G2A_H30YA_01
focalLength | 15.300000190734863
focusDistance | 7070.0
fStop | 1.600000023841858
projection | perspective
stereoRole | mono
horizontalAperture | 8.064000129699707
verticalAperture | 4.535999774932861
clippingRange | (1, 1000000)
cameraProjectionType | pinhole
nominalWidth | 3840.0
nominalHeight | 2160.0
opticalCenterX | 1864.240478515625
opticalCenterY | 986.3945922851562
maxFOV | 30.0
polyK0 | -0.6564998626708984
polyK1 | -4.156541347503662
polyK2 | 245.6761932373047
polyK3 | -0.43839189410209656
polyK4 | -4.5701212882995605
polyK5 | 251.74969482421875
p0 | -0.000658363220281899
p1 | 8.901000114747148e-07
s0 | 0.0
s1 | 0.0
s2 | 0.0
s3 | 0.0
physicalDistortionCoefficients | Not Applicable
physicalDistortionModel | Not Applicable
[/TABLE]
Other Features

- Dimensions: 40 mm (length) by 23 mm (depth) by 40 mm (height)

- Operating Temperature: -40C to 85C

Note
For the datasheet and full list of specifications, visit the SG8-AR820C-5300-G2A-Hxxx series cameras product page.

#### SG8S-AR0820C-5300-G2A-H60SA Camera (Certified by Sensing)
SG8S-AR0820C-5300-G2A-H60SA is a 4k high performance automotive grade camera that supports advanced on sensor HDR and multi-camera synchronization.
To create the camera from the menu: Create>Sensors>Camera and Depth Sensors>Sensing>Sensing SG8S-AR0820C-5300-G2A-H60SA
To create the sensor from the Content Browser: Isaac Sim>Sensors>Sensing>SG8>H60SA>SG8S-AR0820C-5300-G2A-H60SA.usd
Features and Specification
[TABLE]
name | SG8S_AR0820C_5300_G2A_H60SA_01
focalLength | 7.869999885559082
focusDistance | 1670.0
fStop | 1.7999999523162842
projection | perspective
stereoRole | mono
horizontalAperture | 8.064000129699707
verticalAperture | 4.535999774932861
clippingRange | (1, 1000000)
cameraProjectionType | fisheyeEquidistant
nominalWidth | 3840.0
nominalHeight | 2160.0
opticalCenterX | 1919.1090087890625
opticalCenterY | 1087.7274169921875
maxFOV | 60.0
polyK0 | 0.8600332140922546
polyK1 | -0.30780455470085144
polyK2 | -0.05103735625743866
polyK3 | 1.5231009721755981
polyK4 | 0.0005489090108312666
polyK5 | -0.25151902437210083
p0 | 6.143400241853669e-05
p1 | -4.332419848651625e-05
s0 | 0.0
s1 | 0.0
s2 | 0.0
s3 | 0.0
physicalDistortionCoefficients | Not Applicable
physicalDistortionModel | Not Applicable
[/TABLE]
Other Features

- Dimensions: 40 mm (length) by 23 mm (depth) by 40 mm (height)

- Operating Temperature: -40C to 85C

Note
For the datasheet and full list of specifications, visit the SG8-AR820C-5300-G2A-Hxxx series cameras product page.

#### SG8S-AR0820C-5300-G2A-H120YA Camera (Certified by Sensing)
SG8S-AR0820C-5300-G2A-H120YA is a 4k high performance automotive grade camera that supports advanced on sensor HDR and multi-camera synchronization.
To create the camera from the menu: Create>Sensors>Camera and Depth Sensors>Sensing>Sensing SG8S-AR0820C-5300-G2A-H120YA
To create the sensor from the Content Browser: Isaac Sim>Sensors>Sensing>SG8>H120YA>SG8S-AR0820C-5300-G2A-H120YA.usd
Features and Specification
[TABLE]
name | SG8S_AR0820C_5300_G2A_H120YA_01
focalLength | 4.010000228881836
focusDistance | 480.0
fStop | 1.600000023841858
projection | perspective
stereoRole | mono
horizontalAperture | 8.064000129699707
verticalAperture | 4.535999774932861
clippingRange | (1, 1000000)
cameraProjectionType | fisheyeEquidistant
nominalWidth | 3840.0
nominalHeight | 2160.0
opticalCenterX | 1919.1090087890625
opticalCenterY | 1087.7274169921875
maxFOV | 120.0
polyK0 | 0.8600332140922546
polyK1 | -0.30780455470085144
polyK2 | -0.05103735625743866
polyK3 | 1.5231009721755981
polyK4 | 0.0005489090108312666
polyK5 | -0.25151902437210083
p0 | 6.143400241853669e-05
p1 | -4.332419848651625e-05
s0 | 0.0
s1 | 0.0
s2 | 0.0
s3 | 0.0
physicalDistortionCoefficients | Not Applicable
physicalDistortionModel | Not Applicable
[/TABLE]
Other Features

- Dimensions: 40 mm (length) by 23 mm (depth) by 40 mm (height)

- Operating Temperature: -40C to 85C

Note
For the datasheet and full list of specifications, visit the SG8-AR820C-5300-G2A-Hxxx series cameras product page.

### SICK

#### Inspector83x (Certified by SICK)

##### Inspector83x (Certified)
The SICK Inspector83x is a 2D camera, which helps to rapidly solve vision applications such as quality assurance, defect detection, and sorting.

###### Features and Specification
ℹ️ Note For the datasheet and full list of specifications, visit the Inspector83x product page .

To create the camera from the menu: Create>Sensors>Camera and Depth Sensors>SICK>Inspector83x
To create the sensor from the Content Browser: Isaac Sim>Sensors>SICK>Inspector83x>SICK_Inspector83x.usd

## Depth Sensors
For more information about depth sensor modeling in Isaac Sim, see here .

### Intel

#### Intel Realsense D455
The Intel Realsense Depth Camera D455 consists of multiple RGB and depth image sensors and a 6-axis IMU, simulated in NVIDIA Isaac Sim.
To create the camera from the menu: Create>Sensors>Camera and Depth Sensors>Intel>Intel Realsense D455
To create the sensor from the Content Browser: Isaac Sim>Sensors>intel>RealSense>rsd455.usd
Features and Specification
[TABLE]
name | Camera_Pseudo_Depth | Camera_OmniVision_OV9782_Color | Camera_OmniVision_OV9782_Left | Camera_OmniVision_OV9782_Right
focalLength | 1.9299999475479126 | 1.9299999475479126 | 1.9299999475479126 | 1.9299999475479126
focusDistance | 0.6000000238418579 | 0.5 | 0.5 | 0.5
fStop | 2.0 | 2.0 | 2.0 | 2.0
projection | perspective | perspective | perspective | perspective
stereoRole | mono | mono | left | right
horizontalAperture | 3.8959999084472656 | 3.8959999084472656 | 3.8959999084472656 | 3.8959999084472656
verticalAperture | 2.453000068664551 | 2.453000068664551 | 2.453000068664551 | 2.453000068664551
clippingRange | (0.01, 1000000) | (0.01, 1000000) | (0.01, 1000000) | (0.01, 1000000)
cameraProjectionType | fisheyeEquidistant | fisheyeEquidistant | fisheyeEquidistant | fisheyeEquidistant
nominalWidth | 1936.0 | 1936.0 | 1936.0 | 1936.0
nominalHeight | 1216.0 | 1216.0 | 1216.0 | 1216.0
opticalCenterX | 970.94244 | 970.94244 | 970.94244 | 970.94244
opticalCenterY | 600.37482 | 600.37482 | 600.37482 | 600.37482
maxFOV | 100.5999984741211 | 98.0 | 98.0 | 98.0
polyK0 | 0.0 | 0.0 | 0.0 | 0.0
polyK1 | 0.00245 | 0.00245 | 0.00245 | 0.00245
polyK2 | 0.0 | 0.0 | 0.0 | 0.0
polyK3 | 0.0 | 0.0 | 0.0 | 0.0
polyK4 | 0.0 | 0.0 | 0.0 | 0.0
polyK5 | 0.0 | 0.0 | 0.0 | 0.0
p0 | -0.00037 | -0.00037 | -0.00037 | -0.00037
p1 | -0.00074 | -0.00074 | -0.00074 | -0.00074
s0 | -0.00058 | -0.00058 | -0.00058 | -0.00058
s1 | -0.00022 | -0.00022 | -0.00022 | -0.00022
s2 | 0.00019 | 0.00019 | 0.00019 | 0.00019
s3 | -0.0002 | -0.0002 | -0.0002 | -0.0002
physicalDistortionCoefficients | Not Applicable | Not Applicable | Not Applicable | Not Applicable
physicalDistortionModel | Not Applicable | Not Applicable | Not Applicable | Not Applicable
[/TABLE]
Other Features

- Dimensions: 124 mm (length) by 25 mm (depth) by 29 mm (height)

- IMU: Bosch BM1055

- Ideal Range: 0.6m to 6m

- Minimum Depth Distance at Max resolution: 52cm

- Depth accuracy: under 2% at 4m

IMU to RealSense transformation in Isaac Sim
[TABLE]
Transformation | x | y | z
Rotation (degrees) | 0.0 | 0.0 | 0.0
Translation (meters) | 0.016 | -0.01728 | 0.0074
[/TABLE]
Note
For the datasheet and full list of specifications, visit the D455 product page.

### Orbbec

#### Orbbec Gemini 2 (Certified by Orbbec)
The Orbbec Gemini 2 is a depth camera based on Active Stereo IR technology.
To create the camera from the menu: Create>Sensors>Camera and Depth Sensors>Orbbec>Orbbec Gemini 2
To create the sensor from the Content Browser: Isaac Sim>Sensors>Orbbec>Gemini 2>orbbec_gemini2_V1.0.usd
Features and Specification
[TABLE]
name | Stream_rgb | Stream_depth | Stream_ir_left | Stream_ir_right
focalLength | 2.9700000286102295 | 1.809999942779541 | 1.809999942779541 | 1.809999942779541
focusDistance | 80.0 | 45.0 | 45.0 | 45.0
fStop | 0.0 | 0.0 | 0.0 | 0.0
projection | perspective | perspective | perspective | perspective
stereoRole | mono | mono | left | right
horizontalAperture | 5.539000034332275 | 3.619999885559082 | 3.880000114440918 | 3.880000114440918
verticalAperture | 3.0920000076293945 | 2.440000057220459 | 2.440000057220459 | 2.440000057220459
clippingRange | (0.005, 1000) | (0.005, 1000) | (0.005, 1000) | (0.005, 1000)
cameraProjectionType | pinhole | pinhole | pinhole | pinhole
nominalWidth | 1936.0 | 1936.0 | 1936.0 | 1936.0
nominalHeight | 1216.0 | 1216.0 | 1216.0 | 1216.0
opticalCenterX | 970.94244 | 970.94244 | 970.94244 | 970.94244
opticalCenterY | 600.37482 | 600.37482 | 600.37482 | 600.37482
maxFOV | 200.0 | 200.0 | 200.0 | 200.0
polyK0 | 0.0 | 0.0 | 0.0 | 0.0
polyK1 | 0.00245 | 0.00245 | 0.00245 | 0.00245
polyK2 | 0.0 | 0.0 | 0.0 | 0.0
polyK3 | 0.0 | 0.0 | 0.0 | 0.0
polyK4 | 0.0 | 0.0 | 0.0 | 0.0
polyK5 | 0.0 | 0.0 | 0.0 | 0.0
p0 | -0.00037 | -0.00037 | -0.00037 | -0.00037
p1 | -0.00074 | -0.00074 | -0.00074 | -0.00074
s0 | -0.00058 | -0.00058 | -0.00058 | -0.00058
s1 | -0.00022 | -0.00022 | -0.00022 | -0.00022
s2 | 0.00019 | 0.00019 | 0.00019 | 0.00019
s3 | -0.0002 | -0.0002 | -0.0002 | -0.0002
physicalDistortionCoefficients | Not Applicable | Not Applicable | Not Applicable | Not Applicable
physicalDistortionModel | Not Applicable | Not Applicable | Not Applicable | Not Applicable
[/TABLE]
Other Features

- Dimensions: 90 mm (length) by 25 mm (depth) by 30 mm (height)

- IMU supported with multi camera synchronization

- Ideal Range: 0.15m to 10m

- Depth accuracy: under 2% at 2m

Note
For the datasheet and full list of specifications, visit the Gemini 2 product page.

#### Orbbec Femto Mega (Certified by Orbbec)
The Orbbec Femto Mega is a programmable multi-mode Depth and RGB camera.
To create the camera from the menu: Create>Sensors>Camera and Depth Sensors>Orbbec>Orbbec FemtoMega
To create the sensor from the Content Browser: Isaac Sim>Sensors>Orbbec>FemtoMega>orbbec_femtomega_v1.0.usd
Features and Specification
[TABLE]
name | camera_rgb | camera_tof_nfov | camera_tof_wfov
focalLength | 3.25 | 1.690000057220459 | 1.690000057220459
focusDistance | 150.0 | 44.0 | 44.0
fStop | 0.0 | 0.0 | 0.0
projection | perspective | perspective | perspective
stereoRole | mono | mono | mono
horizontalAperture | 5.449999809265137 | 2.5899999141693115 | 5.849999904632568
verticalAperture | 3.0999999046325684 | 2.1500000953674316 | 5.849999904632568
clippingRange | (0.01, 1000000) | (0.01, 1000) | (0.01, 1000)
cameraProjectionType | pinhole | pinhole | pinhole
nominalWidth | 1936.0 | 1936.0 | 1936.0
nominalHeight | 1216.0 | 1216.0 | 1216.0
opticalCenterX | 970.94244 | 970.94244 | 970.94244
opticalCenterY | 600.37482 | 600.37482 | 600.37482
maxFOV | 200.0 | 200.0 | 200.0
polyK0 | 0.0 | 0.0 | 0.0
polyK1 | 0.00245 | 0.00245 | 0.00245
polyK2 | 0.0 | 0.0 | 0.0
polyK3 | 0.0 | 0.0 | 0.0
polyK4 | 0.0 | 0.0 | 0.0
polyK5 | 0.0 | 0.0 | 0.0
p0 | -0.00037 | -0.00037 | -0.00037
p1 | -0.00074 | -0.00074 | -0.00074
s0 | -0.00058 | -0.00058 | -0.00058
s1 | -0.00022 | -0.00022 | -0.00022
s2 | 0.00019 | 0.00019 | 0.00019
s3 | -0.0002 | -0.0002 | -0.0002
physicalDistortionCoefficients | Not Applicable | Not Applicable | Not Applicable
physicalDistortionModel | Not Applicable | Not Applicable | Not Applicable
[/TABLE]
Other Features

- Dimensions: 115mm (length) by 145 mm (depth) by 40mm (height)

- IMU supported

- Ideal Range: 0.25m to 5.46m

- Depth accuracy: under 11mm + 0.1% distance

Note
For the datasheet and full list of specifications, visit the Femto Mega product page.

#### Orbbec Gemini 335 (Certified by Orbbec)
To create the camera from the menu: Create>Sensors>Camera and Depth Sensors>Orbbec>Orbbec Gemini 335
To create the sensor from the Content Browser: Isaac Sim>Sensors>Orbbec>Gemini335>orbbec_gemini_335.usd
Features and Specification
[TABLE]
name | Stream_rgb | Stream_ir_left | Stream_ir_right
focalLength | 2.9700000286102295 | 1.809999942779541 | 1.809999942779541
focusDistance | 80.0 | 45.0 | 45.0
fStop | 0.0 | 0.0 | 0.0
projection | perspective | perspective | perspective
stereoRole | mono | right | left
horizontalAperture | 5.539000034332275 | 3.880000114440918 | 3.880000114440918
verticalAperture | 3.0920000076293945 | 2.440000057220459 | 2.440000057220459
clippingRange | (0.005, 1000) | (0.005, 1000) | (0.005, 1000)
cameraProjectionType | pinhole | pinhole | pinhole
nominalWidth | 1936.0 | 1936.0 | 1936.0
nominalHeight | 1216.0 | 1216.0 | 1216.0
opticalCenterX | 970.94244 | 970.94244 | 970.94244
opticalCenterY | 600.37482 | 600.37482 | 600.37482
maxFOV | 200.0 | 200.0 | 200.0
polyK0 | 0.0 | 0.0 | 0.0
polyK1 | 0.00245 | 0.00245 | 0.00245
polyK2 | 0.0 | 0.0 | 0.0
polyK3 | 0.0 | 0.0 | 0.0
polyK4 | 0.0 | 0.0 | 0.0
polyK5 | 0.0 | 0.0 | 0.0
p0 | -0.00037 | -0.00037 | -0.00037
p1 | -0.00074 | -0.00074 | -0.00074
s0 | -0.00058 | -0.00058 | -0.00058
s1 | -0.00022 | -0.00022 | -0.00022
s2 | 0.00019 | 0.00019 | 0.00019
s3 | -0.0002 | -0.0002 | -0.0002
physicalDistortionCoefficients | Not Applicable | Not Applicable | Not Applicable
physicalDistortionModel | Not Applicable | Not Applicable | Not Applicable
[/TABLE]

#### Orbbec Gemini 335L (Certified by Orbbec)
To create the camera from the menu: Create>Sensors>Camera and Depth Sensors>Orbbec>Orbbec Gemini 335L
To create the sensor from the Content Browser: Isaac Sim>Sensors>Orbbec>Gemini335L>orbbec_gemini_335L.usd
Features and Specification
[TABLE]
name | Camera_ir_left | Camera_ir_right | Camera_rgb
focalLength | 1.809999942779541 | 1.809999942779541 | 1.809999942779541
focusDistance | 45.0 | 45.0 | 0.44999998807907104
fStop | 0.0 | 0.0 | 0.0
projection | perspective | perspective | perspective
stereoRole | mono | mono | mono
horizontalAperture | 3.8399999141693115 | 3.8399999141693115 | 3.8399999141693115
verticalAperture | 2.4000000953674316 | 2.4000000953674316 | 2.4000000953674316
clippingRange | (0.005, 100000) | (0.005, 100000) | (0.005, 100000)
cameraProjectionType | pinhole | pinhole | pinhole
nominalWidth | 1936.0 | 1936.0 | 1936.0
nominalHeight | 1216.0 | 1216.0 | 1216.0
opticalCenterX | 970.94244 | 970.94244 | 970.94244
opticalCenterY | 600.37482 | 600.37482 | 600.37482
maxFOV | 200.0 | 200.0 | 200.0
polyK0 | 0.0 | 0.0 | 0.0
polyK1 | 0.00245 | 0.00245 | 0.00245
polyK2 | 0.0 | 0.0 | 0.0
polyK3 | 0.0 | 0.0 | 0.0
polyK4 | 0.0 | 0.0 | 0.0
polyK5 | 0.0 | 0.0 | 0.0
p0 | -0.00037 | -0.00037 | -0.00037
p1 | -0.00074 | -0.00074 | -0.00074
s0 | -0.00058 | -0.00058 | -0.00058
s1 | -0.00022 | -0.00022 | -0.00022
s2 | 0.00019 | 0.00019 | 0.00019
s3 | -0.0002 | -0.0002 | -0.0002
physicalDistortionCoefficients | Not Applicable | Not Applicable | Not Applicable
physicalDistortionModel | Not Applicable | Not Applicable | Not Applicable
[/TABLE]

### Stereolabs

#### ZED X (Certified by Stereolabs)
The ZED X Stereo Camera from Stereolabs consists of two 1200p 60fps RGB image sensors and a 6-axis IMU, all simulated in the NVIDIA Isaac Sim.
To create the camera from the menu: Create>Sensors>Camera and Depth Sensors>Stereolabs>ZED_X
To create the sensor from the Content Browser: Isaac Sim>Sensors>Stereolabs>ZED_X>ZED_X.usd
Features and Specification
[TABLE]
name | CameraLeft | CameraRight
focalLength | 2.2079999446868896 | 2.2079999446868896
focusDistance | 28.0 | 28.0
fStop | 0.0 | 0.0
projection | perspective | perspective
stereoRole | left | right
horizontalAperture | 5.760000228881836 | 5.760000228881836
verticalAperture | 3.240000009536743 | 3.240000009536743
clippingRange | (0.01, 100000) | (0.01, 100000)
cameraProjectionType | pinhole | pinhole
nominalWidth | 1936.0 | 1936.0
nominalHeight | 1216.0 | 1216.0
opticalCenterX | 970.94244 | 970.94244
opticalCenterY | 600.37482 | 600.37482
maxFOV | 200.0 | 200.0
polyK0 | 0.0 | 0.0
polyK1 | 0.00245 | 0.00245
polyK2 | 0.0 | 0.0
polyK3 | 0.0 | 0.0
polyK4 | 0.0 | 0.0
polyK5 | 0.0 | 0.0
p0 | -0.00037 | -0.00037
p1 | -0.00074 | -0.00074
s0 | -0.00058 | -0.00058
s1 | -0.00022 | -0.00022
s2 | 0.00019 | 0.00019
s3 | -0.0002 | -0.0002
physicalDistortionCoefficients | Not Applicable | Not Applicable
physicalDistortionModel | Not Applicable | Not Applicable
[/TABLE]
Other Features

- Dimensions: 163.4 mm (length) by 31.8 mm (depth) by 36.7 mm (height)

- Operating Temperature: -20C to 55C

IMU to ZED X transformation in Isaac Sim
[TABLE]
Transformation | x | y | z
Rotation (degrees) | -90.0 | 0.0 | 0.0
Translation (meters) | 0.06 | -0.0 | 0.00185
[/TABLE]
Note
For the datasheet and full list of specifications, visit the ZED X datasheet , for usage in Isaac Sim, see Stereolabs Documentation .

#### ZED X Mini (Certified by Stereolabs)
The ZED X Mini Stereo Camera from Stereolabs consists of two 1200p 60fps RGB image sensors and a 6-axis IMU, all simulated in the NVIDIA Isaac Sim.
To create the sensor from the Content Browser: Isaac Sim>Sensors>Stereolabs>ZED_X_mini>ZED_X_Mini.usd
Features and Specification
[TABLE]
name | CameraRight | CameraLeft
focalLength | 2.2079999446868896 | 2.2079999446868896
focusDistance | 28.0 | 28.0
fStop | 0.0 | 0.0
projection | perspective | perspective
stereoRole | right | left
horizontalAperture | 5.760000228881836 | 5.760000228881836
verticalAperture | 3.240000009536743 | 3.240000009536743
clippingRange | (0.01 100000) | (0.01 100000)
cameraProjectionType | pinhole | pinhole
nominalWidth | 1936.0 | 1936.0
nominalHeight | 1216.0 | 1216.0
opticalCenterX | 970.94244 | 970.94244
opticalCenterY | 600.37482 | 600.37482
maxFOV | 200.0 | 200.0
polyK0 | 0.0 | 0.0
polyK1 | 0.00245 | 0.00245
polyK2 | 0.0 | 0.0
polyK3 | 0.0 | 0.0
polyK4 | 0.0 | 0.0
polyK5 | 0.0 | 0.0
p0 | -0.00037 | -0.00037
p1 | -0.00074 | -0.00074
s0 | -0.00058 | -0.00058
s1 | -0.00022 | -0.00022
s2 | 0.00019 | 0.00019
s3 | -0.0002 | -0.0002
physicalDistortionCoefficients | Not Applicable | Not Applicable
physicalDistortionModel | Not Applicable | Not Applicable
[/TABLE]
Other Features

- Dimensions: 93.6 mm (length) by 31.8 mm (depth) by 36.7 mm (height)

- Operating Temperature: -20C to 55C

IMU to ZED X Mini transformation in Isaac Sim
[TABLE]
Transformation | x | y | z
Rotation (degrees) | -90.0 | 0.0 | 0.0
Translation (meters) | 0.06 | -0.0 | 0.00185
[/TABLE]
Note
For the datasheet and full list of specifications, visit the ZED X Mini datasheet , for usage in Isaac Sim, see Stereolabs Documentation .
