<!-- source: overview/extensions_renaming.html | title: Renaming Extensions in Isaac Sim 4.5 — Isaac Sim Documentation -->

# Renaming Extensions in Isaac Sim 4.5

## Renamed Extensions
The following table specifies the new extension name(s) for deprecated Isaac Sim extensions.
Note
Several deprecated extensions (eg. `omni.isaac.sensor`) have been split into multiple new extensions, and some new extensions (eg. `isaacsim.sensors.physx`) contain APIs from multiple deprecated extensions. Deprecation warnings, as described above , will reflect these changes.
Note
Support for the deprecated extensions listed below will be removed in Isaac Sim 5.0 release.
Note
For more information about each extension’s functionality, please review the API Documentation .

[TABLE]
Isaac Sim 4.2 Extension(s) | Isaac Sim 4.5 Extension(s)
omni.exporter.urdf | isaacsim.asset.exporter.urdf
omni.importer.mjcf | isaacsim.asset.importer.mjcf
omni.importer.urdf | isaacsim.asset.importer.urdf
omni.isaac.app.selector | isaacsim.app.selector
omni.isaac.app.setup | isaacsim.app.setup
omni.isaac.articulation_inspector | omni.physx.inspector
omni.isaac.asset_browser omni.isaac.assets_check | isaacsim.asset.browser
omni.isaac.benchmark.services | isaacsim.benchmark.services
omni.isaac.benchmarks | isaacsim.benchmark.examples
omni.isaac.block_world | isaacsim.asset.importer.heightmap
omni.isaac.camera_inspector | isaacsim.util.camera_inspector
omni.isaac.cloner | isaacsim.core.cloner
omni.isaac.conveyor | isaacsim.asset.gen.conveyor
omni.isaac.conveyor.ui | isaacsim.asset.gen.conveyor.ui
omni.isaac.core_nodes | isaacsim.core.nodes
omni.isaac.core | isaacsim.core.api isaacsim.core.prims isaacsim.core.utils
omni.isaac.cortex | isaacsim.cortex.framework
omni.isaac.cortex.sample_behaviors | isaacsim.cortex.behaviors
omni.isaac.debug_draw | isaacsim.util.debug_draw
omni.isaac.diff_usd | isaacsim.util
omni.isaac.doctest | isaacsim.test.docstring
omni.isaac.examples | isaacsim.examples.interactive
omni.isaac.extension_templates | isaacsim.examples.extension
omni.isaac.franka | isaacsim.robot.manipulators.examples
omni.isaac.gain_tuner | isaacsim.robot_setup.gain_tuner
omni.isaac.grasp_editor | isaacsim.robot_setup.grasp_editor
omni.isaac.import_wizard | isaacsim.robot_setup.import_wizard
omni.isaac.jupyter_notebook | isaacsim.code_editor.jupyter
omni.isaac.kit | isaacsim.simulation_app
omni.isaac.lula_test_widget | isaacsim.robot_motion.lula_test_widget
omni.isaac.lula | isaacsim.robot_motion.lula
omni.isaac.manipulators | isaacsim.robot.manipulators
omni.isaac.manipulators.ui | isaacsim.robot.manipulators.ui
omni.isaac.menu | isaacsim.gui.menu
omni.isaac.merge_mesh | isaacsim.util.merge_mesh
omni.isaac.motion_generation | isaacsim.robot_motion.motion_generation
omni.isaac.nucleus | isaacsim.storage.native
omni.isaac.occupancy_map | isaacsim.asset.gen.omap
omni.isaac.occupancy_map.ui | isaacsim.asset.gen.omap.ui
omni.isaac.physics_utilities | isaacsim.util.physics
omni.isaac.proximity_sensor | isaacsim.sensors.physx
omni.isaac.quadruped | isaacsim.robot.policy.examples
omni.isaac.range_sensor | isaacsim.sensors.physx
omni.isaac.range_sensor.examples | isaacsim.sensors.physx.examples
omni.isaac.range_sensor.ui | isaacsim.sensors.physx.ui
omni.isaac.robot_assembler | isaacsim.robot_setup.assembler
omni.isaac.robot_description_editor | isaacsim.robot_setup.xrdf_editor isaacsim.robot_setup.lula_editor
omni.isaac.ros_bridge | isaacsim.ros1.bridge
omni.isaac.ros2_bridge | isaacsim.ros2.bridge
omni.isaac.ros2_bridge.robot_description | isaacsim.ros2.urdf
omni.isaac.scene_blox | isaacsim.replicator.scene_blox
omni.isaac.sensor | isaacsim.sensors.camera isaacsim.sensors.camera.ui isaacsim.sensors.physics isaacsim.sensors.physics.examples isaacsim.sensors.physics.ui isaacsim.sensors.physx isaacsim.sensors.rtx isaacsim.sensors.rtx.ui
omni.isaac.surface_gripper | isaacsim.robot.surface_gripper
omni.isaac.surface_gripper.ui | isaacsim.robot.surface_gripper.ui
omni.isaac.synthetic_recorder | isaacsim.replicator.synthetic_recorder
omni.isaac.tests | isaacsim.test.collection
omni.isaac.tf_viewer | isaacsim.ros2.tf_viewer
omni.isaac.throttling | isaacsim.core.throttling
omni.isaac.ui_template | isaacsim.examples.ui
omni.isaac.ui | isaacsim.gui.components
omni.isaac.unit_converter | omni.usd.metrics_assembler
omni.isaac.universal_robots | isaacsim.robot.manipulators.examples
omni.isaac.utils | isaacsim.core.utils
omni.isaac.version | isaacsim.core.version
omni.isaac.vscode | isaacsim.code_editor.vscode
omni.isaac.wheeled_robots | isaacsim.robot.wheeled_robots isaacsim.robot.wheeled_robots.examples
omni.isaac.wheeled_robots.ui | isaacsim.robot.wheeled_robots.ui
omni.isaac.window.about | isaacsim.app.about
omni.kit.property.isaac | isaacsim.gui.property
omni.replicator.agent.camera_calibration | isaacsim.replicator.agent.camera_calibration
omni.replicator.agent.core | isaacsim.replicator.agent.core
omni.replicator.agent.ui | isaacsim.replicator.agent.ui
omni.replicator.isaac | isaacsim.replicator.domain_randomization isaacsim.replicator.examples isaacsim.replicator.writers
[/TABLE]

## Deprecated Extensions
The following table specifies extensions deprecated, but not renamed, in Isaac Sim 4.5.
Note
Support for the deprecated extensions listed below will be removed in Isaac Sim 5.0 release.

[TABLE]
Deprecated Extensions
omni.isaac.dynamic_control
omni.isaac.examples_nodes
omni.isaac.repl
[/TABLE]

## Removed Extensions
The following table specifies extensions removed from Isaac Sim 4.5.

[TABLE]
Removed Extensions | Notes
omni.isaac.benchmark_environments | Deprecated since Isaac Sim 4.0.
omni.isaac.cortex_sync | Deprecated since Isaac Sim 4.0.
omni.isaac.dofbot | dofbot example no longer supported as of Isaac Sim 4.5
omni.isaac.partition | Partition tool no longer supported as of Isaac Sim 4.5
omni.isaac.physics_inspector | Deprecated since Isaac Sim 4.0. Replaced by Omniverse Physics Inspector .
omni.isaac.robot_benchmark | Deprecated since Isaac Sim 4.0.
omni.isaac.ocs2 | No longer supported as of Isaac Sim 4.5
[/TABLE]

# FAQ

## Why were extensions renamed in Isaac Sim 4.5?
We chose to rename and split extensions for Isaac Sim 4.5 to support ongoing brand standardization, and improve modularity for end-users who may choose to build custom apps using Isaac Sim extensions, including Isaac Lab.

## How will renamed extensions affect my Isaac Sim workflows?
Extension renaming will affect your workflows in three primary ways:

- Setting names referencing specific extensions have changed (eg. `/exts/omni.isaac.ros2_bridge/ros_distro` has become `/exts/isaacsim.ros2.bridge/ros_distro`).

- OmniGraph node names referencing specific extensions have changed (eg. `omni.isaac.core_nodes.IsaacReadSimulationTime` has become `isaacsim.core.nodes.IsaacReadSimulationTime`).

- Extension APIs have been renamed and/or moved (eg. `omni.isaac.sensor.LidarRtx` has become `isaacsim.sensors.rtx.LidarRtx`).

## How should I update my existing Isaac Sim workflows for Isaac Sim 4.5?
Isaac Sim 4.5 has introduced the `isaacsim.core.deprecation_manager` extension to support backwards compatibility with existing end-user workflows for Isaac Sim 4.5. While we cannot guarantee perfect compatibility, this section will explain how the new extension can simplify updating your workflows, and what steps you should take to fully transition to Isaac Sim 4.5.
Note
In addition to renaming extensions, to improve startup time compared to Isaac Sim 4.2, several extensions were removed from the Isaac Sim 4.5 base Kit app. If after trying the solutions below you are still encountering errors related to missing or renamed extensions, consider manually enabling the extension via the `isaacsim.core.utils.extensions.enable_extension` API.

### Renaming settings
The `isaacsim.core.deprecation_manager` extension will automatically copy values of settings associated with a deprecated Isaac Sim extension to its corresponding new extension’s settings. For example, if you execute the following:

```
./isaac-sim.sh --/exts/omni.isaac.ros2_bridge/ros_distro=humble
```
the `isaacsim.core.deprecation_manager` extension will automatically set the value of `/exts/isaacsim.ros2.bridge/ros_distro` to `humble`.
If your workflow relies on custom values for Isaac Sim extension settings, rename the settings by referencing the table below .

### Renaming OmniGraph nodes
The `isaacsim.core.deprecation_manager` extension will automatically update the prim type of any OmniGraph node belonging to a deprecated Isaac Sim extension when a scene opens, and print the changes to the console along with a message in the UI. The scene must be saved to retain the changes.
Note
If the OmniGraph node is part of a reference or payload asset in the scene, the name change will be registered as a delta to the reference in the opened scene. `isaacsim.core.deprecation_manager`will not recursively updated USD files. To ensure the referenced USD is properly updated, you will need to manually open the referenced USD on its own and then save it with the updated OmniGraph nodes.
Any USD asset shipped with Isaac Sim 4.5 that includes OmniGraph nodes will already be updated to use the new extensions’s OmniGraph nodes.

### Renaming extension APIs
All deprecated extensions have been included in Isaac Sim 4.5. When loaded from a kit app, they will print deprecation warning(s) indicating to which new extension(s) APIs have been moved.
To remove those deprecation warnings when running your own workflows, migrate your workflows to the new extensions by updating Python import statements to use the new extensions, eg.

```
from omni.isaac.sensor import LidarRtx
```
would become

```
from isaacsim.sensors.rtx import LidarRtx
```
