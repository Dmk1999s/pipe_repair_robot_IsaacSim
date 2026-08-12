<!-- source: sensors/isaacsim_sensors_physics_effort.html | title: Effort Sensor — Isaac Sim Documentation -->

# Effort Sensor
The effort sensor in Isaac Sim tracks the torque or force applied to individual joints. Torque is measured for revolute joints and magnitude of force is measured for linear joints.
See the Isaac Sim Conventions documentation for a complete list of Isaac Sim conventions.

## GUI

### Scene Setup
Begin by adding a Simple Articulation to the scene, which can be accessed in the Content Browser.

- In the Content Browser, search for `simple_articulation` or navigate to `Isaac Sim/Robots/IsaacSim/SimpleArticulation/simple_articulation.usd`.

- Drag `simple_articulation` onto the World prim in the Stage UI window on the right hand side to add an instance into the environment.

- To drive the revolute joint, in the Stage window, select the RevoluteJoint prim at /World/simple_articulation/Arm/RevoluteJoint, and scroll down to Drive in the Property window. Set the target velocity to `90 deg/s`, and stiffness to `0`.

### Creating and Modifying the Effort Sensor
The following section describes how to create the effort sensor using the Script Editor, opened from Window > Script Editor. The effort sensor can be created using the `isaacsim.sensors.physics.EffortSensor` Python wrapper class. The benefit of using the wrapper class is that it comes with additional helper functions to set the effort sensor properties and retrieve sensor data.

```
1from isaacsim.sensors.physics.scripts.effort_sensor import EffortSensor
2import numpy as np
3
4sensor = EffortSensor(
5 prim_path="/World/simple_articulation/Arm/RevoluteJoint",
6 sensor_period=0.1,
7 use_latest_data=False,
8 enabled=True
9)
```
To modify sensor parameters, you can change class member variables like `sensor_period`, `use_latest_data`, and `enabled` directly, and for changing the `dof_name` and `buffer_size` for the readings, use the corresponding member functions `update_dof_name` and `change_buffer_size`.

### Reading Sensor Output with Python
get_sensor_reading(self, interpolation_function = None, use_latest_data = False)
The get sensor reading function takes in two parameters:

- an interpolation function (optional) to use in place of the default linear interpolation function

- a use latest data flag (optional) for retrieving the data point from the current physics step, if the sensor is running at a slower rate than physics rate

The function will return an `EsSensorReading` object which contains `is_valid`, `time`, and `value`.
After you created the effort sensor, press PLAY to start the simulation and call the function below to get the sensor reading for the current frame:

```
1from isaacsim.sensors.physics.scripts.effort_sensor import EffortSensor
2
3# get sensor reading
4reading = sensor.get_sensor_reading(use_latest_data = True)
```
Sample usage with custom interpolation function:

```
1from isaacsim.sensors.physics.scripts.effort_sensor import EffortSensor
2
3# Input Param: List of past EsSensorReading, time of the expected sensor reading
4def interpolation_function(data, time):
5 interpolated_reading = EsSensorReading()
6 # do interpolation
7 return interpolated_reading
8
9# get sensor readings
10reading = sensor.get_sensor_reading(interpolation_function)
```

### OmniGraph Workflow
To set up the OmniGraph to create the effort sensor and collect readings from it.

- Create the new action graph by navigating to Window > Graph Editors > Action Graph, and selecting New Action Graph in the new tab that opens.

- Add the following nodes to the graph:

- On Playback Tick: Executes the graph nodes every simulation timestep.

- Isaac Read Effort Node: Reads the effort sensor. In the Property tab, set Effort Prim to the exact joint of measurement. For example /World/simple_articulation/Arm/RevoluteJoint in `simple_articulation.usd`.

- To String: Converts the effort sensor readings to string format.

- Print Text: Prints the string readings to console. In the Property tab, set Log Level to Warning so that messages are visible in the terminal/console by default. Additionally, check To Screen to print directly to screen.

Connect the above nodes as follows to print out the effort sensor reading:
Note
Configure the joints to the correct axis to get the expected readings.

## API Documentation
See the API Documentation for complete usage information.
