<!-- source: robot_simulation/mobile_robot_controllers.html | title: Mobile Robot Controllers — Isaac Sim Documentation -->

# Mobile Robot Controllers

## Differential controller
The differential controller uses the speed differential between the left and right wheels to control the robot’s linear and angular velocity. The differential robot enables the robot to turn in place and is used in the NVIDIA Nova Carter robot.

### The Math
\[ \begin{align}\begin{aligned}\omega_R &= \frac{1}{2r}(2V + \omega l_{tw})\\\omega_L &= \frac{1}{2r}(2V - \omega l_{tw})\end{aligned}\end{align} \]where \(\omega\) is the desired angular velocity, \(V\) is the desired linear velocity, \(r\) is the radius of the wheels, and \(l_{tw}\) is the distance between them. \(\omega_R\) is the desired right wheel angular velocity and \(\omega_L\) is the desired left wheel angular velocity.

### OmniGraph Node

[TABLE]
Input Commands | description
execIn | Input execution
wheelRadius | Radius of the wheels in meters
wheelDistance | Distance between the wheels in meters
dt | Delta time in seconds
maxAcceleration | Max linear acceleration for moving forward and reverse in m/s^2, 0.0 means not set
maxDeceleration | Max linear breaking of the robot in m/s^2, 0.0 means not set
maxAngularAcceleration | Max angular acceleration of the robot in rad/s^2, 0.0 means not set
maxLinearSpeed | Max linear speed allowed for the robot in m/s, 0.0 means not set
maxAngularSpeed | Max angular speed allowed for the robot in rad/s, 0.0 means not set
maxWheelSpeed | Max wheel speed in rad/s
Desired Linear Velocity | Desired linear velocity in m/s
Desired Angular Velocity | Desired angular velocity in rad/s
[/TABLE]

[TABLE]
Output Commands | description
VelocityCommand | Velocity command for the left and right wheel in m/s and rad/s
[/TABLE]

### Python
The code snippet below setups the differential controller for a NVIDIA Jetbot with a wheel radius of 3 cm and a base of 11.25cm, with a linear speed of 0.3m/s and angular speed of 1.0rad/s.

```
1import numpy as np
2import asyncio
3from isaacsim.core.api import World
4from isaacsim.robot.wheeled_robots.controllers.differential_controller import DifferentialController
5from isaacsim.robot.wheeled_robots.robots import WheeledRobot
6from isaacsim.storage.native import get_assets_root_path
7
8async def differential_controller_example():
9 if World.instance():
10 World.instance().clear_instance()
11 world = World()
12 await world.initialize_simulation_context_async()
13
14 world.scene.add_default_ground_plane()
15 assets_root_path = get_assets_root_path()
16 jetbot_asset_path = assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd"
17 my_jetbot = world.scene.add(
18 WheeledRobot(
19 prim_path="/World/Jetbot",
20 name="my_jetbot",
21 wheel_dof_names=["left_wheel_joint", "right_wheel_joint"],
22 create_robot=True,
23 usd_path=jetbot_asset_path,
24 position=np.array([-1.5, -1.5, 0]),
25 )
26 )
27 await world.reset_async()
28 await world.play_async()
29
30 wheel_radius = 0.03
31 wheel_base = 0.1125
32 controller = DifferentialController("test_controller", wheel_radius, wheel_base)
33 linear_speed = 0.3
34 angular_speed = 1.0
35
36 command = [linear_speed, angular_speed]
37 my_jetbot.apply_wheel_actions(controller.forward(command))
38
39 await asyncio.sleep(5.0) # Run for 5 seconds
40 world.pause()
41# Run the example
42asyncio.ensure_future(differential_controller_example())
```

## Holonomic Controller
The holonomic controller computes the joint drive commands required on omni-directional robots to produce the commanded forward, lateral, and yaw speeds of the robot. An example of a holonomic robot is the NVIDIA Kaya robot. The problem is framed as a quadratic program to minimize the residual “net force” acting on the center of mass.
Note
The wheel joints of the robot prim must have additional attributes to definine the roller angles and radii of the mecanum wheels.

```
1stage = omni.usd.get_context().get_stage()
2joint_prim = stage.GetPrimAtPath("/path/to/wheel_joint")
3joint_prim.CreateAttribute("isaacmecanumwheel:radius",Sdf.ValueTypeNames.Float).Set(0.12)
4joint_prim.CreateAttribute("isaacmecanumwheel:angle",Sdf.ValueTypeNames.Float).Set(10.3)
```
The `HolonomicRobotUsdSetup` class automates this process.

### The Math
The cost funciton is defined as the control input to the robot joints. By minimizing the control inputs, excess acceleration and be reduced.
\[J = min(X^T \cdot X)\]The equality constrains are set by the linear and angular target velocity Inputs:
\[ \begin{align}\begin{aligned}v_{input} &= V^T \cdot X\\w_{input} &= (V \times D_{wheel dist to COM}) \cdot X\end{aligned}\end{align} \]

### OmniGraph Node

[TABLE]
Input Commands | description
execIn | Input execution
wheelRadius | Array of wheel radius in meters
wheelPositions | Position of the wheel with respect to chassis’ center of mass in meters
wheelOrientations | Orientation of the wheel with respect to chassis’ center of mass frame
mecanumAngles | Angles of the mecanum wheels with respect to wheel’s rotation axis in radians
wheelAxis | The rotation axis of the wheels
upAxis | The up axis (default to z axis)
Velocity Commands for the vehicle | Velocity in x and y (m/s) and rotation (rad/s)
maxLinearSpeed | Maximum speed allowed for the vehicle in m/s
maxAngularSpeed | Maximum angular rotation speed allowed for the vehicles in rad/s
maxWheelSpeed | Maximum rotation speed allowed for the wheel joints in rad/s
linearGain | Gain for the linear velocity input
angularGain | Gain for the angular input
[/TABLE]

[TABLE]
Output Commands | description
jointVelocityCommand | Velocity command for the wheel joints in rad/s
[/TABLE]

### Python
The code snippet below computes the joint velocity output for a three wheeled NVIDIA Kaya holonomic robot with command velocity of [1.0, 1.0, 0.1]

```
1import numpy as np
2import asyncio
3from isaacsim.core.api import World
4from isaacsim.robot.wheeled_robots.controllers.holonomic_controller import HolonomicController
5from isaacsim.robot.wheeled_robots.robots import WheeledRobot
6from isaacsim.storage.native import get_assets_root_path
7
8async def holonomic_controller_example():
9 if World.instance():
10 World.instance().clear_instance()
11 world = World()
12 await world.initialize_simulation_context_async()
13
14 world.scene.add_default_ground_plane()
15 assets_root_path = get_assets_root_path()
16 kaya_asset_path = assets_root_path + "/Isaac/Robots/NVIDIA/Kaya/kaya.usd"
17 my_kaya = world.scene.add(
18 WheeledRobot(
19 prim_path="/World/Kaya",
20 name="my_kaya",
21 wheel_dof_names=["axle_0_joint", "axle_1_joint", "axle_2_joint"],
22 create_robot=True,
23 usd_path=kaya_asset_path,
24 position=np.array([-1, 0, 0]),
25 )
26 )
27 await world.reset_async()
28 await world.play_async()
29
30 wheel_radius = [0.04, 0.04, 0.04]
31 wheel_orientations = [[0, 0, 0, 1], [0.866, 0, 0, -0.5], [0.866, 0, 0, 0.5]]
32 wheel_positions = [
33 [-0.0980432, 0.000636773, -0.050501],
34 [0.0493475, -0.084525, -0.050501],
35 [0.0495291, 0.0856937, -0.050501],
36 ]
37 mecanum_angles = [90, 90, 90]
38 command = [1.0, 1.0, 0.1]
39
40 controller = HolonomicController(
41 name="holonomic_controller",
42 wheel_radius=wheel_radius,
43 wheel_positions=wheel_positions,
44 wheel_orientations=wheel_orientations,
45 mecanum_angles=mecanum_angles,
46 )
47 my_kaya.apply_wheel_actions(controller.forward(command))
48
49 await asyncio.sleep(5.0) # Run for 5 seconds
50 world.pause()
51# Run the example
52asyncio.ensure_future(holonomic_controller_example())
```

## Ackermann Controller
The ackeramnn controller is commonly used for robots with steerable wheels, an example of steerable robot is the NVIDIA leatherback robot. The ackeramnn controller in Isaac Sim will assume the desired steering angle and linear velocity is provided, and based on the robot geometry

### The Math
Compute the steering angle offset between the left and right steering wheels:
\[ \begin{align}\begin{aligned}R_{icr} &= \frac{l_{wb}}{tan(\theta_{steer})}\\\theta_L &= \arctan[\frac{l_{wb}}{R_{icr} - 0.5 * l_{tw}}]\\\theta_R &= \arctan[\frac{l_{wb}}{R_{icr} + 0.5 * l_{tw}}]\end{aligned}\end{align} \]where \(R_{icr}\) is the radius to the instantaneous center of rotation, \(\theta_{steer}\) is the desired steering angle, \(l_{wb}\) is the distance between rear and front axles (wheel base), \(l_{tw}\) is the track width
Compute the individual wheel velocities (Forward steering case):
First step is to find the distance between the wheels and the instantaneous center of rotation.
\[ \begin{align}\begin{aligned}D_{front} &= \sqrt{ (R_{icr} \pm 0.5 l_{tw})^2 + (l_{wb})^2 }\\D_{rear} &= R_{icr} \pm 0.5 l_{tw}\end{aligned}\end{align} \]Note
for \(\pm\), use \(-\) for the wheel closer to the \(R_{icr}\) and \(+\) for the wheel further to the \(R_{icr}\)
Then desired wheel velocity can be computed
\[ \begin{align}\begin{aligned}\omega_{front} &= \frac{V_{desired}}{R_{icr}} \cdot \frac{D_{front}}{r_{front}}\\\omega_{rear} &= \frac{V_{desired}}{R_{icr}} \cdot \frac{D_{rear}}{r_{rear}}\end{aligned}\end{align} \]Where \(V_{desired}\) is the desired linear velocity, \(r_{front}\) is the desired front wheel radius, and \(r_{rear}\) is the desired rear wheel radius.

### OmniGraph Node

[TABLE]
Input Commands | description
execIn | Input execution
acceleration | Desired forward acceleration for the robot in m/s^2
speed | Desired forward speed in m/s
steeringAngle | Desired steering angle in radians, by default it is positive for turning left for a front wheel drive
currentLinearVelocity | Current linear velocity of the robot in m/s
wheelBase | Distance between the front and rear axles of the robot in meters
trackWidth | Distance between the left and right rear wheels of the robot in meters
turningWheelRadius | Radius of the front wheels of the robot in meters
maxWheelVelocity | Maximum angular velocity of the robot wheel in rad/s
invertSteeringAngle | Flips the sign of the steering angle, Set to true for rear wheel steering
useAcceleration | Use acceleration as an input, Set to false to use speed as input instead
maxWheelRotation | Maximum angle of rotation for the front wheels in radians
dt | Delta time for the simulation step
[/TABLE]

[TABLE]
Output Commands | description
execOut | Output execution
leftWheelAngle | Angle for the left turning wheel in radians
rightWheelAngle | Angle for the right turning wheel in radians
wheelRotationVelocity | Angular velocity for the turning wheels in rad/s
[/TABLE]

### Python
The python snippet below creates an ackerrmann controller for a NVIDIA Leatherback robot with a wheel base of 1.65m, trackwidth of 1.25m, and wheel radius of 0.25m, sending it a desired forward velocity of 1.1 rad/s and steering angle of 0.1rad.

```
1import numpy as np
2import asyncio
3from isaacsim.core.api import World
4from isaacsim.robot.wheeled_robots.controllers.ackermann_controller import AckermannController
5from isaacsim.core.api.robots import Robot
6from isaacsim.core.utils.types import ArticulationAction
7from isaacsim.storage.native import get_assets_root_path
8import isaacsim.core.utils.stage as stage_utils
9
10async def ackermann_controller_example():
11 if World.instance():
12 World.instance().clear_instance()
13 world = World()
14 await world.initialize_simulation_context_async()
15 world.scene.add_default_ground_plane()
16
17 assets_root_path = get_assets_root_path()
18 leatherback_asset_path = assets_root_path + "/Isaac/Robots/NVIDIA/Leatherback/leatherback.usd"
19 leatherback_prim_path = "/World/Leatherback"
20 stage_utils.add_reference_to_stage(leatherback_asset_path, leatherback_prim_path)
21 my_leatherback = world.scene.add(
22 Robot(
23 prim_path=leatherback_prim_path,
24 name="my_leatherback"
25 )
26 )
27 await world.reset_async()
28 await world.play_async()
29
30 # Steering joints (position control)
31 steering_joint_names = [
32 "Knuckle__Upright__Front_Left",
33 "Knuckle__Upright__Front_Right",
34 ]
35 # Wheel joints (velocity control)
36 wheel_joint_names = [
37 "Wheel__Knuckle__Front_Left",
38 "Wheel__Knuckle__Front_Right",
39 "Wheel__Upright__Rear_Left",
40 "Wheel__Upright__Rear_Right",
41 ]
42
43 steering_joint_indices = [my_leatherback.get_dof_index(name) for name in steering_joint_names]
44 wheel_joint_indices = [my_leatherback.get_dof_index(name) for name in wheel_joint_names]
45
46 wheel_base = 1.65
47 track_width = 1.25
48 wheel_radius = 0.25
49 desired_forward_vel = 1.1 # rad/s
50 desired_steering_angle = 0.1 # rad
51 # Setting acceleration, steering velocity, and dt to 0 to instantly reach the target steering and velocity
52 acceleration = 0.0 # m/s^2
53 steering_velocity = 0.0 # rad/s
54 dt = 0.0 # secs
55
56 controller = AckermannController(
57 "test_controller", wheel_base=wheel_base, track_width=track_width, front_wheel_radius=wheel_radius, back_wheel_radius=wheel_radius
58 )
59 actions = controller.forward([
60 desired_steering_angle,
61 steering_velocity,
62 desired_forward_vel,
63 acceleration,
64 dt
65 ])
66
67 full_joint_positions = np.zeros(my_leatherback.num_dof)
68 full_joint_positions[steering_joint_indices[0]] = actions.joint_positions[0] # Left steering
69 full_joint_positions[steering_joint_indices[1]] = actions.joint_positions[1] # Right steering
70 # Create full joint velocity array (for wheels)
71 full_joint_velocities = np.zeros(my_leatherback.num_dof)
72 full_joint_velocities[wheel_joint_indices[0]] = actions.joint_velocities[0] # FL wheel
73 full_joint_velocities[wheel_joint_indices[1]] = actions.joint_velocities[1] # FR wheel
74 full_joint_velocities[wheel_joint_indices[2]] = actions.joint_velocities[2] # BL wheel
75 full_joint_velocities[wheel_joint_indices[3]] = actions.joint_velocities[3] # BR wheel
76
77 # Apply combined action
78 combined_action = ArticulationAction(
79 joint_positions=full_joint_positions,
80 joint_velocities=full_joint_velocities
81 )
82 my_leatherback.apply_action(combined_action)
83
84 await asyncio.sleep(5.0) # Run for 5 seconds
85 world.pause()
86# Run the example
87asyncio.ensure_future(ackermann_controller_example())
```
