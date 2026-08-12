<!-- source: py/api/structisaacsim_1_1sensors_1_1physics_1_1_is_reading.html | title: IsReading — Isaac Sim -->

# IsReading
Fully qualified name: `isaacsim::sensors::physics::IsReading`
structIsReading

IMU sensor reading data structure.
Public Members
floattime={0.0f}

Simulation timestamp for IMU sensor reading.

floatlinAccX={0.0f}

Accelerometer reading value x axis, in m/s^2.

floatlinAccY={0.0f}

Accelerometer reading value y axis, in m/s^2.

floatlinAccZ={0.0f}

Accelerometer reading value z axis, in m/s^2.

floatangVelX={0.0f}

Gyroscope reading value x axis, in rad/s.

floatangVelY={0.0f}

Gyroscope reading value y axis, in rad/s.

floatangVelZ={0.0f}

Gyroscope reading value z axis, in rad/s.

carb::Float4orientation={0.0f,0.0f,0.0f,0.0f}

Quaternion orientation of parent body (x, y, z, w).

boolisValid={false}

Validity of the data.
False for when the sensor is disabled, true for enabled.
