<!-- source: py/docs/source/standalone_examples_list.html | title: Standalone Examples Reference List — Isaac Sim -->

# Standalone Examples Reference List
This document lists all standalone examples available in Isaac Sim.

## standalone_examples/api

### isaacsim.asset.importer.mjcf

- `mjcf_import.py`

### isaacsim.asset.importer.urdf

- `urdf_import.py`

### isaacsim.core.api

- `add_cubes.py`

- `add_frankas.py`

- `cloth.py`

- `control_robot.py`

- `data_logging.py`

- `deformable.py`

- `detailed_contact_data.py`

- `omnigraph_triggers.py`

- `rigid_contact_view.py`

- `simulate_robot.py`

- `simulation_callbacks.py`

- `time_stepping.py`

- `visual_materials.py`

### isaacsim.core.cloner

- `clone_ants.py`

### isaacsim.core.experimental

- `control_robot_jax.py`

- `control_robot_numpy.py`

- `control_robot_torch.py`

- `control_robot_warp.py`

### isaacsim.cortex.framework

- `demo_ur10_conveyor_main.py`

- `example_command_api_main.py`

- `follow_example_main.py`

- `follow_example_modified_main.py`

- `franka_examples_main.py`

#### behaviors/franka

- `behaviors/franka/franka_behaviors.py`

### isaacsim.replicator.behavior

- `behaviors.py`

### isaacsim.replicator.domain_randomization

- `randomization_demo.py`

### isaacsim.replicator.examples

- `cosmos_writer_simple.py`

- `cosmos_writer_warehouse.py`

- `custom_event_and_write.py`

- `custom_fps_writer_annotator.py`

- `motion_blur.py`

- `multi_camera.py`

- `sdg_getting_started_01.py`

- `sdg_getting_started_02.py`

- `sdg_getting_started_03.py`

- `sdg_getting_started_04.py`

- `simready_assets_sdg.py`

- `simulation_get_data.py`

- `subscribers_and_events.py`

### isaacsim.replicator.grasping

- `grasping_workflow_sdg.py`

### isaacsim.robot.manipulators

- `franka_pick_up.py`

- `ur10_pick_up.py`

#### cobotta_900

- `cobotta_900/follow_target_example.py`

- `cobotta_900/gripper_control.py`

- `cobotta_900/pick_up_example.py`

#### cobotta_900/controllers

- `cobotta_900/controllers/pick_place.py`

- `cobotta_900/controllers/rmpflow.py`

#### cobotta_900/tasks

- `cobotta_900/tasks/follow_target.py`

- `cobotta_900/tasks/pick_place.py`

#### franka

- `franka/follow_target_with_ik.py`

- `franka/follow_target_with_rmpflow.py`

- `franka/franka_gripper.py`

- `franka/multiple_tasks.py`

- `franka/pick_place.py`

- `franka/stacking.py`

#### rmpflow_supported_robots

- `rmpflow_supported_robots/supported_robot_follow_target_example.py`

#### universal_robots

- `universal_robots/bin_filling.py`

- `universal_robots/follow_target_with_ik.py`

- `universal_robots/follow_target_with_ik_experimental.py`

- `universal_robots/follow_target_with_rmpflow.py`

- `universal_robots/multiple_tasks.py`

- `universal_robots/pick_place.py`

- `universal_robots/pick_place2.py`

- `universal_robots/stacking.py`

#### ur10e

- `ur10e/follow_target_example.py`

- `ur10e/follow_target_example_rmpflow.py`

- `ur10e/gripper_control.py`

- `ur10e/pick_up_example.py`

#### ur10e/controller

- `ur10e/controller/ik_solver.py`

- `ur10e/controller/pick_place.py`

- `ur10e/controller/rmpflow.py`

#### ur10e/tasks

- `ur10e/tasks/follow_target.py`

- `ur10e/tasks/pick_place.py`

### isaacsim.robot.policy.examples

- `anymal_standalone.py`

- `h1_standalone.py`

- `spot_standalone.py`

### isaacsim.robot.wheeled_robots.examples

- `jetbot_differential_move.py`

- `kaya_holonomic_move.py`

### isaacsim.ros2.bridge

- `camera_manual.py`

- `camera_noise.py`

- `camera_periodic.py`

- `carter_multiple_robot_navigation.py`

- `carter_stereo.py`

- `clock.py`

- `moveit.py`

- `rtx_lidar.py`

- `subscriber.py`

### isaacsim.sensors.camera

- `camera.py`

- `camera_add_depth_sensor.py`

- `camera_annotator_device.py`

- `camera_opencv_fisheye.py`

- `camera_opencv_pinhole.py`

- `camera_pre_isp_pipeline.py`

- `camera_ros.py`

- `camera_stereoscopic_depth.py`

- `camera_view.py`

### isaacsim.sensors.physics

- `contact_sensor.py`

- `effort_sensor.py`

- `imu_sensor.py`

### isaacsim.sensors.physx

- `rotating_lidar_physX.py`

### isaacsim.sensors.rtx

- `inspect_lidar_metadata.py`

- `inspect_radar_metadata.py`

- `resolve_object_ids_from_gmo.py`

- `rotating_lidar_rtx.py`

- `specify_non_visual_materials.py`

### isaacsim.simulation_app

- `async_call.py`

- `change_resolution.py`

- `constant_fps.py`

- `hello_world.py`

- `livestream.py`

- `load_stage.py`

### isaacsim.util.debug_draw

- `rtx_lidar.py`

- `rtx_radar.py`

### isaacsim.xr.openxr

#### hand_tracking

- `hand_tracking/hand_tracking_sample.py`

### omni.isaac.dynamic_control

- `franka_articulation.py`

### omni.kit.app

- `app_framework.py`

### omni.kit.asset_converter

- `asset_usd_converter.py`

## standalone_examples/benchmarks

- `benchmark_camera.py`

- `benchmark_core_world.py`

- `benchmark_nucleus_kpis.py`

- `benchmark_physx_lidar.py`

- `benchmark_robots_evobot.py`

- `benchmark_robots_humanoid.py`

- `benchmark_robots_nova_carter.py`

- `benchmark_robots_nova_carter_ros2.py`

- `benchmark_robots_o3dyn.py`

- `benchmark_robots_ur10.py`

- `benchmark_rtx_lidar.py`

- `benchmark_rtx_radar.py`

- `benchmark_scene_loading.py`

- `benchmark_sdg.py`

- `benchmark_single_view_depth_sensor.py`

### validation

- `benchmark_robots_nova_carter_ros2_validation.py`

- `benchmark_sdg_validation.py`

## standalone_examples/replicator

- `amr_navigation.py`

- `cosmos_writer_warehouse.py`

### augmentation

- `annotator_augmentation.py`

- `writer_augmentation.py`

### infinigen

- `infinigen_sdg.py`

- `infinigen_sdg_utils.py`

### mobility_gen

- `replay_directory.py`

### object_based_sdg

- `object_based_sdg.py`

- `object_based_sdg_utils.py`

### online_generation

- `generate_shapenet.py`

- `shapenet_utils.py`

- `train_shapenet.py`

- `usd_convertor.py`

### pose_generation

- `__init__.py`

- `pose_generation.py`

#### flying_distractors

- `flying_distractors/__init__.py`

- `flying_distractors/collision_box.py`

- `flying_distractors/dynamic_asset_set.py`

- `flying_distractors/dynamic_object.py`

- `flying_distractors/dynamic_object_set.py`

- `flying_distractors/dynamic_shape_set.py`

- `flying_distractors/flying_distractors.py`

#### pose_tests

- `pose_tests/test_utils.py`

### scene_based_sdg

- `scene_based_sdg.py`

- `scene_based_sdg_utils.py`

## standalone_examples/testing

### isaacsim.benchmark.services

- `test_no_rendering.py`

### isaacsim.core.api

- `articulation.py`

- `hello_world.py`

- `rigid_prim_view.py`

- `tensor_api_handles.py`

- `test_articulation_determinism.py`

- `test_articulation_root.py`

- `test_delete_in_contact.py`

- `test_rendering.py`

- `test_save_stage.py`

- `test_time_stepping.py`

- `xform_prim_view.py`

### isaacsim.cortex.framework

- `cortex_bringup_test.py`

### isaacsim.replicator.examples

- `ar_capture_pipeline.py`

- `motion_blur_short.py`

### isaacsim.robot.manipulators.examples.franka

- `torque_control.py`

### isaacsim.ros2.bridge

- `enable_extension.py`

- `test_camera_tf_delay.py`

- `test_carter_camera_multi_robot_nav.py`

- `test_people_sim.py`

- `test_publish_camera_data.py`

### isaacsim.sensors.physics

- `contact_sensor_test.py`

### isaacsim.simulation_app

- `test_createstage_config.py`

- `test_extension_count.py`

- `test_external.py`

- `test_extra_args.py`

- `test_fabric_frame_delay.py`

- `test_fetch_results.py`

- `test_frame_delay.py`

- `test_headless_no_rendering.py`

- `test_multiprocess.py`

- `test_ogn.py`

- `test_ovd.py`

- `test_syntheticdata.py`

- `test_unsaved_on_exit.py`

- `test_viewport_ready.py`

### isaacsim.test.docstring

- `standalone_doctest.py`

### omni.isaac.dynamic_control

- `test_zero_step.py`

### omni.replicator.agent

- `test_scripting.py`

### omni.syntheticdata

- `test_basic.py`

### python_sh

- `import_scipy.py`

- `import_sys.py`

- `import_torch.py`

- `path_length.py`

### validation

- `test_assets.py`

- `test_deprecated.py`

- `test_standalone.py`

## standalone_examples/tutorials

- `getting_started.py`

- `getting_started_robot.py`
