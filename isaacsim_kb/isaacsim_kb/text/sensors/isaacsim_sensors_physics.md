<!-- source: sensors/isaacsim_sensors_physics.html | title: Physics-Based Sensors — Isaac Sim Documentation -->

# Physics-Based Sensors
Isaac Sim’s physics-based sensors are based on CPU physics simulations and are run after the rendering is finished. They have access to a prim’s physics properties, like mass and velocity.
These sensors output the exact measurements from the physics engine and the sensor readings can be augmented in post processing. By default, the highest rate that the sensors can output data is the physics rate and you must provide additional interpolation options to generate data beyond this rate. Furthermore, ground truth readings from the simulator might already have some noise; additional noise can be augmented to the sensor readings in post process to make them more realistic.
The physics-based sensors are organized in the isaacsim.sensors.physics extension.
Isaac Sim supports the following physics-based ground truth sensors:
