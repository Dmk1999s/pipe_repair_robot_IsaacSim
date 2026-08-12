<!-- source: core_api_tutorials/tutorial_advanced_data_logging.html | title: Data Logging — Isaac Sim Documentation -->

# Data Logging

## Learning Objectives
This tutorial shows how to record data using the DataLogger and play it back in NVIDIA Isaac Sim. After this tutorial, you can record and play back states and actions in your pipeline while using NVIDIA Isaac Sim.
10-15 Minute Tutorial

## Recording Data
Let’s begin by using the following target extension example to record data

- Open the Follow Target example by first activating Windows > Examples > Robotics Examples which will open the `Robotics Examples` window. Next enable the example from Robotics Examples > Manipulation > Follow Target Task.

- Click on LOAD under the World Controls to load Franka with a visual target cube.

- Choose the output directory of the JSON file to save the data under Data Logging in the Follow Target menu.

- Click on Follow Target under Task Controls.

- Click on START LOGGING

- Move the visual cube around so that Franka follows it using the RMPFlowController

- After a few seconds, click on SAVE DATA

- Click on File > New From Stage Template > Empty to create new stage.

- The data should be recorded under the chosen file shown in the Output Directory text field.

### Code Overview
Open the extension example code located at ISAAC_SIM_DIR/exts/isaacsim.examples.interactive/isaacsim/examples/interactive/follow_target/follow_target.py using the open-source code button located at the top of the menu.
First, let’s look at the logging function.

```
1def _on_logging_event(self, val):
2 world = self.get_world()
3 data_logger = world.get_data_logger() # a DataLogger object is defined in the World by default
4 if not world.get_data_logger().is_started():
5 robot_name = self._task_params["robot_name"]["value"]
6 target_name = self._task_params["target_name"]["value"]
7
8 # A data logging function is called at every time step index if the data logger is started already.
9 # We define the function here. The tasks and scene are passed to this function when called.
10
11 def frame_logging_func(tasks, scene):
12 return {
13 "joint_positions": scene.get_object(robot_name).get_joint_positions().tolist(),# save data as lists since its a JSON file.
14 "applied_joint_positions": scene.get_object(robot_name)
15 .get_applied_action()
16 .joint_positions.tolist(),
17 "target_position": scene.get_object(target_name).get_world_pose()[0].tolist(),
18 }
19
20 data_logger.add_data_frame_logging_func(frame_logging_func) # adds the function to be called at each physics time step.
21 if val:
22 data_logger.start() # starts the data logging
23 else:
24 data_logger.pause()
25 return
```

Now let’s look at how to save the data collected so far.

```
1def _on_save_data_event(self, log_path):
2 world = self.get_world()
3 data_logger = world.get_data_logger() # a DataLogger object is defined in the World by default
4 data_logger.save(log_path=log_path) # Saves the collected data to the json file specified.
5 data_logger.reset() # Resets the DataLogger internal state so that another set of data can be collected and saved separately.
6 return
```

### Inspect the Data
As shown below, the DataLogger takes care of logging the time in seconds and time step corresponding to each data frame.

```
1{"Isaac Sim Data": [{"current_time": 1.4833334106951952, "current_time_step": 89, "data": {"joint_positions": [0.07561380416154861, -1.2318825721740723, 0.11344202607870102, -2.4259397983551025, 0.0970514565706253, 1.6226640939712524, 0.8470714688301086, 4.0, 3.997776985168457], "applied_joint_positions": [0.07291083037853241, -1.2202218770980835, 0.1190749853849411, -2.39223575592041, 0.11230156570672989, 1.3975754976272583, 0.9029524326324463, 4.0, 4.0], "target_position": [0.0, 10.0, 70.0]}}, {"current_time": 1.5000000782310963, "current_time_step": 90, "data": {"joint_positions": [0.07484950870275497, -1.2287049293518066, 0.11509127914905548, -2.416816234588623, 0.09880664199590683, 1.603981614112854, 0.8490884304046631, 4.0, 3.997793197631836], "applied_joint_positions": [0.07221028953790665, -1.2172484397888184, 0.1205318346619606, -2.3833296298980713, 0.11395926028490067, 1.3804354667663574, 0.9063650369644165, 4.0, 4.0], "target_position": [0.0, 10.0, 70.0]}}, {"current_time": 1.5166667457669973, "current_time_step": 91, "data": {"joint_positions": [0.07410304993391037, -1.2255841493606567, 0.11668683588504791, -2.4077510833740234, 0.10055229812860489, 1.58543062210083, 0.8511277437210083, 4.0, 3.997816562652588], "applied_joint_positions": [0.07153353840112686, -1.2144113779067993, 0.1219213530421257, -2.3745198249816895, 0.11559101194143295, 1.363703727722168, 0.9096996784210205, 4.0, 4.0], "target_position": [0.0, 10.0, 70.0]}] }
```

## Replaying Back Data
Similarly, we will use another extension example provided under Robotics Examples to play back the recorded data.

- Open the Follow Target example by first activating Windows > Examples > Robotics Examples which will open the `Robotics Examples` window. Next enable the example from Robotics Examples > Manipulation > Replay Follow Target Task.

- Click on LOAD under the World Controls to load Franka with a visual target cube.

- Point to the JSON file saved in the last step in Recording Data section under Data File at the Data Replay section in the menu.

- Click on Replay Trajectory under Data Replay to replay the actions only and wait for the trajectory to finish replaying.

- Click on Reset

- Similarly, click on Replay Scene under Data Replay to replay the actions and the cube position.

- Click on File > New From Stage Template > Empty to create new stage.

### Code Overview
Open the extension example code using the open-source code button located at the top of the menu located at:
ISAAC_SIM_DIR/exts/isaacsim.examples.interactive/isaacsim/examples/interactive/replay_follow_target/replay_follow_target.py
First, let’s look at how to load the data and replay the trajectory.

```
1async def _on_replay_trajectory_event_async(self, data_file):
2 # Loads the data from the json file
3 self._data_logger.load(log_path=data_file)
4 world = self.get_world()
5 await world.play_async()
6 # Adds the physics callback to set the joint targets every frame
7 world.add_physics_callback("replay_trajectory", self._on_replay_trajectory_step)
8 return
9
10def _on_replay_trajectory_step(self, step_size):
11 if self._world.current_time_step_index < self._data_logger.get_num_of_data_frames():
12 # To sync time steps and get the data frame at the same time step
13 data_frame = self._data_logger.get_data_frame(data_frame_index=self._world.current_time_step_index)
14 # Applies the same recorded action to the articulation controller
15 self._articulation_controller.apply_action(
16 ArticulationAction(joint_positions=data_frame.data["applied_joint_positions"])
17 )
18 return
```

Now let’s look at how to replay the scene, including the goal cube position.

```
1def _on_replay_scene_step(self, step_size):
2 if self._world.current_time_step_index < self._data_logger.get_num_of_data_frames():
3 target_name = self._task_params["target_name"]["value"]
4 data_frame = self._data_logger.get_data_frame(data_frame_index=self._world.current_time_step_index)
5 self._articulation_controller.apply_action(
6 ArticulationAction(joint_positions=data_frame.data["applied_joint_positions"])
7 )
8 # Sets the world position of the goal cube to the same recorded position
9 self._world.scene.get_object(target_name).set_world_pose(
10 position=np.array(data_frame.data["target_position"])
11 )
12 return
```

## Summary
This tutorial covered the following topics:

- Using the DataLogger to save data.

- Using the DataLogger to replay data.
