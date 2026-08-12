<!-- source: sensors/isaacsim_sensors_physx_lightbeam.html | title: PhysX SDK Lightbeam Sensor — Isaac Sim Documentation -->

# PhysX SDK Lightbeam Sensor
The PhysX SDK Lightbeam sensor in Isaac Sim uses PhysX SDK raycasts to determine if an object has intersected a light beam. You can specify the number of rays and height to create a safety light “curtain” of lightbeam sensors.
See the Isaac Sim Conventions documentation for a complete list of Isaac Sim conventions.

## Examples

- PhysX SDK Lightbeam Sensor example: Robotics Examples > Sensors > Lightbeam

To run the example:

- Activate Robotics Examples tab from Windows > Examples > Robotics Examples.

- Click Robotics Examples > Sensors > Lightbeam.

- Verify that you have a window containing empty data for each lightbeam, which will be populated with data after you press play. It will show if each beam was hit, the linear depth of the hit, and the exact hit position in `xyz`.

- Press the PLAY button to begin simulating.

- Press `SHIFT + LEFT_CLICK` to drag the cube or sensor around and see changes in the readings.
