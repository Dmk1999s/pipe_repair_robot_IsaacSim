<!-- source: robot_simulation/ext_isaacsim_robot_policy_example.html | title: Reinforcement Learning Policies Examples in Isaac Sim — Isaac Sim Documentation -->

# Reinforcement Learning Policies Examples in Isaac Sim

## About
The isaac_sim_policy_example Extension is a framework and has a set of helper functions to deploy Isaac Lab Reinforcement Learning Policies in Isaac Sim. For details for training and building the policy in Isaac Sim, visit deploying policy in Isaac Sim .
This Extension is enabled by default. If it is ever disabled, it can be re-enabled from the Extension Manager by searching for `isaacsim.robot.policy.example`. To run examples below activate Windows > Examples > Robotics Examples which will open the `Robotics Examples` tab.

### Unitree H1 Humanoid Example

- The Unitree H1 humanoid example can be accessed by creating a empty stage.

- Open the example menu using Robotics Examples > POLICY > Humanoid.

- Press LOAD to open the scene.

This example uses the H1 Flat Terrain Policy trained in Isaac Lab to control the humanoid’s locomotion.
Controls:

- Forward: UP ARROW / NUM 8

- Turn Left: LEFT ARROW / NUM 4

- Turn Right: RIGHT ARROW / NUM 6

### Boston Dynamics Spot Quadruped Example

- The Boston Dynamics Spot quadruped example can be accessed by creating a empty stage.

- Open the example menu using Robotics Examples > POLICY > Quadruped.

- Press LOAD to open the scene.

This example uses the Spot Flat Terrain Policy trained in Isaac Lab to control the quadruped’s locomotion.
Controls:

- Forward: UP ARROW / NUM 8

- Backward: BACK ARROW / NUM 2

- Move Left: LEFT ARROW / NUM 4

- Move Right: RIGHT ARROW / NUM 6

- Turn Left: N / NUM 7

- Turn Right: M / NUM 9

### Franka Panda Open Drawer Example

- The Franka Panda Open Drawer example can be accessed by creating a empty stage.

- Open the example menu using Robotics Examples > POLICY > Franka.

- Press LOAD to open the scene.

This example uses the Franka Open Drawer Policy trained in Isaac Lab to control the robot’s arm. The robot will open the drawer, hold it open until the would reset.

## Policies Files
The policies used in the examples are trained in Isaac Lab and are available here:

[TABLE]
Name | Policy | Parameters
H1 Flat Terrain Policy | H1 Flat Terrain Policy | H1 Flat Terrain Policy Environment Parameters H1 Flat Terrain Policy Network Parameters
Spot Flat Terrain Policy | Spot Flat Terrain Policy | Spot Flat Terrain Policy Environment Parameters Spot Flat Terrain Policy Network Parameters
ANYmal C Flat Terrain Policy | ANYmal C Flat Terrain Policy Anymal C Motor Policy | ANYmal C Flat Terrain Policy Environment Parameters ANYmal C Flat Terrain Policy Network Parameters
Franka Panda Open Drawer Policy | Franka Panda Open Drawer Policy | Franka Panda Open Drawer Policy Environment Parameters
[/TABLE]
Note
The policies can also be downloaded directly from the Content Browser by right clicking the policy and selecting `Download`.

## API Documentation
See the API documentation for complete usage information.

## Standalone Examples
h1_standalone.py

- This standalone example demonstrates a Unitree H1 controlled by a flat terrain policy, following a set of predetermined command sequences. It may be run via the following command:

```
./python.sh standalone_examples/api/isaacsim.robot.policy.examples/h1_standalone.py --num-robots <number of robot> --env-url </path/to/environment>
```
For example, this will spawn 5 robots on the flat grid scene below:

```
./python.sh standalone_examples/api/isaacsim.robot.policy.examples/h1_standalone.py --num-robots 5 --env-url /Isaac/Environments/Grid/default_environment.usd
```

spot_standalone.py

- This standalone example demonstrates a Boston Dynamics Spot controlled by a flat terrain policy, following a set of predetermined command sequences. It may be run via the following command:

```
./python.sh standalone_examples/api/isaacsim.robot.policy.examples/spot_standalone.py
```

anymal_standalone.py

- This standalone example demonstrates an ANYmal C robot that is controlled by a neural network policy. The rough terrain policy was trained in Isaac Lab and takes as input the state of the robot, the commanded base velocity, and the surrounding terrain and outputs joint position targets. The example may be run via the following command:

```
./python.sh standalone_examples/api/isaacsim.robot.policy.examples/anymal_standalone.py
```

Controls:

- Forward: UP ARROW / NUM 8

- Backward: BACK ARROW / NUM 2

- Move Left: LEFT ARROW / NUM 4

- Move Right: RIGHT ARROW / NUM 6

- Turn Left: N / NUM 7

- Turn Right: M / NUM 9
