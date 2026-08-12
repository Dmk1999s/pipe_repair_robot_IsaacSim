<!-- source: action_and_event_data_generation/tutorial_sensors_rtx_placement.html | title: RTX Sensors Placement and Calibration — Isaac Sim Documentation -->

# RTX Sensors Placement and Calibration
Optimizing camera placement is a crucial technique, particularly in indoor or enclosed spaces such as warehouses, retail stores, hospitals, and other similar environments, to ensure comprehensive coverage while minimizing camera deployment costs.
`isaacsim.sensors.rtx.placement` (ISP) enables you to automatically determine optimal camera locations based on scene layout and coverage requirements.
It also provides detailed camera metadata for generated cameras and generate the stage layout visualization with each camera’s FOV coverage.
Camera calibration data such as the camera’s direction, location, and FOV polygon information can also be captured and saved to a `.json` file.

## Enable isaacsim.sensors.rtx.placement
Follow the Omniverse Extension Manager guide to enable the `isaacsim.sensors.rtx.placement` extension.
This extension has two components that have been split into two separate UI windows.

- Camera Placement: Helps you automatically place cameras with optimized poses in your scene based on coverage requirements and scene layout constraints.

- Camera Calibration: Allows you to extract and manage camera calibration data, including position, orientation, and field of view information.
