<!-- source: robot_setup/troubleshooting.html | title: Robot Setup Troubleshooting — Isaac Sim Documentation -->

# Robot Setup Troubleshooting
This page consolidates troubleshooting information for robot setup and simulation in Isaac Sim.

## Reparenting Assets
You can change how reparenting behaves under Edit > Preferences, and on the Stage Panel, scroll down to authoring. The checkbox Keep Prim world Transform when reparenting, lets you decide when reparenting if the objects remain in place or if they get moved to the parent’s frame of reference. You can use this to your advantage to apply offsets or change the parent’s origin without impacting the children elements.

## Robot Rigging Issues
If your robot “explodes” during simulation or after some movements, check if any of the collision meshes are colliding with each other.
Common rigging issues and their solutions:

- Colliding collision geometries - Ensure that collision geometries do not intersect or overlap, especially at joint pivot points

- Joint limit violations - Verify that joint limits are set appropriately and not being exceeded during simulation

- Incorrect joint ordering - Make sure that joint orderings in articulation chains are correct

- Physics instabilities - Adjust physics timestep or solver iteration counts if experiencing vibrations or instabilities

Physics Inspector “failed to find internal joint” errors for robots with mimic joints does not affect the functionality of the mimic joints and can be ignored:

```
[Error] [omni.physx.plugin] Usd Physics: failed to find internal joint object for PhysxMimicJointAPI at /Franka/panda_hand/panda_finger_joint2. Please ensure that the prim is a supported joint type and is part of an articulation.
```

## Robot Controller Issues

- Gains produced by the gain turner may not perfectly track the robot’s commanded movements (for example, as seen in the Cobotta Pro robot). Manual tuning of gains may be necessary for optimal performance.

- Some grippers with parallel mechanism (that is, Robotiq 2F-85 and 2F-C2) have links that do not move with rest of the gripper. This is a known issue and may require manual adjustment of the gripper joints.

- When working with differential drive robots, make sure that wheel friction is appropriate. Too little friction can result in wheel slippage, while too much friction can cause erratic movement.

## Robot Import Issues
USD to URDF Exporter issues:

- The Collider meshes may be improperly included in the visuals. They can be manually removed from the URDF file.

- The Body and Joints are authored in the URDF file in alphabetical order. They can be manually reordered in the URDF file.

- Depending on the robot structure, some body names may be overridden due to the merging of different frames. Review the output and verify that it’s accurate.

- The URDF exporter adds joint effort and velocity limits as inf when unbounded. This may make the URDF not import correctly if the URDF parser does not support inf values in Float.

When importing a URDF:

- If more than one asset in URDF contains the same material name, only one material is created regardless if the parameters in the material are different. For example, if two meshes have materials with the name “material”, one is blue and the other is red, both meshes will be either red or blue. This also applies for textured materials.

- MJCF importer does not show the built-in bookmark in the file picker dialog. The bookmark is still available in the content pane and can be copy-pasted into the file picker dialog.

## Closed Loop Structure Issues
For robots with closed-loop kinematic chains:

- Make sure that the constraints are properly defined and initialized

- Check that all joints in the closed loop have appropriate drive settings

- Consider simulating the closed loop as separate articulations with constraints rather than with a single complex closed-loop structure

- Adjust solver settings for better convergence if experiencing stability issues

## Robot Importing tips

- Sometimes the robot may have non-zero target positions. When the target position does not match the initial position, the robot will move to the target position on the first frame. To prevent this, either set the target position to zero or set the initial position to the target position.

- Max forces may be high or low in the URDF, set them to a more reasonable value in the USD.

- If the stiffness and damping values are too high, the robot may oscillate. If it’s too low, the robot may not move to the desired position. Use the gain tuner to test the stiffness and damping.

- If the robot have overlapping collision meshes, use a filtered pair to ignore collisions between specific meshes.
