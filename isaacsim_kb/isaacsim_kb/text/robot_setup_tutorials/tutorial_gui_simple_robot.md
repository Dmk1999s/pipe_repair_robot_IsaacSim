<!-- source: robot_setup_tutorials/tutorial_gui_simple_robot.html | title: Tutorial 3: Articulate a Basic Robot — Isaac Sim Documentation -->

# Tutorial 3: Articulate a Basic Robot
NVIDIA Isaac Sim’s GUI interface features are the same ones used in NVIDIA Omniverse™ USD Composer, an application dedicated to world-building. This tutorial focuses on the GUI functions that are most relevant to robotic uses. For more sophisticated general world creation, see Omniverse Composer .
You will rig a basic “robot” with three links and two revolute joints to introduce the concepts of joints and articulations. You take the objects that were added to the stage in Tutorial 2: Assemble a Simple Robot and turn them into a mock mobile robot with a rectangular body and two cylindrical wheels.
This is not needed for robots that are imported from Importing your Onshape Document or URDF Importer Extension , these are important concepts to understand for tuning your robots and assembling objects with articulations.

## Learning Objectives
This tutorial details how to rig a two-wheel mobile robot and covers how to:

- Organize stage tree hierarchy

- Add joints between two rigid bodies

- Add joint drives and joint properties

- Add articulations

- Move the robot via a Articulation Velocity Controller

## Prerequisites

- Complete Tutorial 2: Assemble a Simple Robot .

- Or load the checkpoint asset provided in the Content Browser at `Isaac Sim/Samples/Rigging/MockRobot/mock_robot_no_joints`. Do not load it as a reference because you must make permanent modifications to the file.

## Add Joints

- If you are continuing from the GUI Tutorials and have your own `mock_robot.usd` saved, open it using File > Open. Otherwise, load the asset provided in the Content Browser at `Isaac Sim/Samples/Rigging/MockRobot/mock_robot_no_joints`. Do not load it as a reference because you must make permanent modifications to the file.

- For organization, create a Scope to store the joints by right clicking Create > Scope, rename it to Joints.

- To add a joint between two bodies, you must first select them both. Begin by clicking on the body and wheel parent transforms in the context tree window. For our mock robot, select the the cube object `body`, then while holding `Ctrl`, select the cylinder object `wheel_left`.

- With both bodies highlighted, right-click and select Create > Physics > Joints > Revolute Joint. `RevoluteJoint` appears under `wheel_left` on the stage tree. Rename it to `wheel_joint_left`.

- Verify in the Property tab that body0 is `/mock_robot/body/body` (the cube) and body1 is `/mock_robot/wheel_left/wheel_left` (the cylinder).

- Set the X axis of the joint to Local Rotation 0 to `0.0` and Local Rotation 1 to `-90.0` to account for the transformation between the body and the cylinder. This is because the cylinder is rotated 90 degrees in the X axis compared to the body.

- Change the Axis of the joint to Y. Because there is no local rotation `0` for the robot, the joint is in the same pose as the body.

- For organization, drag the joint you just created into the Joints scope.

- Repeat the previous five steps with the right wheel joint.

Before the joints were added, the three rigid bodies fell to the ground separately after pressing Play. Now that there are joints attached, the bodies fall as if they are connected. To see that they move together like they are connected with revolute joints, you can drag the robot around by holding down the `Shift` key and clicking and dragging on any part of the robot in the viewport.

## Add a Joint Drive
Adding the joint adds the mechanical connection. To be able to control and drive the joints, you must add a joint drive API. Select both joints and click the `+ Add` button in the Property tab, and select Physics > Angular Drive to add drive to both joints simultaneously.

- Position Control: For position controlled joints, set a high stiffness and relatively low or zero damping.

- Velocity Control: For velocity controller joints, set a high damping and zero stiffness.

For joints on a wheel, it makes more sense to be velocity controlled, so set both wheels’ Damping to 1e4 and Target Velocity to 200rad/s. If you are working with joints with limited range, those can be set in the Property tab, under the Raw USD Properties > Lower (Upper) Limit. Press Play to see the mock mobile robot drive off.

## Add Articulation
Even though directly driving the joints can move the robot, it is not the most computationally efficient way. Making things into articulations can achieve higher simulation fidelity, fewer joint errors, and can handle larger mass ratios between the jointed bodies. For more information on the physics simulation behind it, see Physics Core: Articulation .
To turn a series of connected rigid bodies and joints into articulation, set an articulation root to anchor the articulation tree. According to instructions on defining articulation trees in Physics Core: Articulation :
For a fixed-base articulation, add the Articulation Root Component either to:

- the fixed joint that connects the articulation base to the world.

- an ancestor of the fixed joint in the USD hierarchy. This allows creating multiple articulations from a single root component added to the scene.

Each descendant fixed joint defines an articulation base link.
For a floating-base articulation, add the Articulation Root Component to either:

- the root rigid-body link

- an ancestor of the root link in the USD hierarchy

For this tutorial, add the articulation root to the robot:

- Select `mock_robot` on the tree.

- Open + Add in the Property tab.

- Add Physics > Articulation Root.

Validate that the resulting robot matches the asset that is provided in the Content Browser at `Isaac Sim/Samples/Rigging/MockRobot/mock_robot_rigged`.

## Add Controller
After the joints are part of an articulation, you can use tools to test the robot’s movement.

- Create another scope by right clicking Create > Scope, rename it to Graphs. This will be used to store the ActionGraphs.

- Drag the Graphs scope under the `mock_robot` Xform in the stage tree.

- Go to Tools > Robotics > Omnigraph Controllers > Joint Velocity to add a velocity controller graph to the stage. This graph will allow you to control the robot’s movement by setting the target velocity for each joint.

- Click the Add button for “Robot Prim” and select the prim with the Articulation Root API, in this case, it’s `/mock_robot`.

- For Graph Path, write `mock_robot/Graphs/Velocity_Controller` to place the ActionGraph in the Graphs scope above.

- Click OK to create the graph.

- To move the robot, press Play to start the simulation. If you have any default position or velocity targets set, the robot starts moving towards those targets immediately. To change the joint commands, select the `JointCommandArray` on the stage tree under /Graphs/velocity_controller, and change the parameters `input0` and `input1` in the properties window.

Note
The articulation controllers use radians, the default USD properties you find under Drive API when you select the individual joints on the stage tree are in degrees.
For this particular robot, it can also be controlled using a Differential Controller. For more information about Omnigraph Controller shortcuts, go to Commonly Used Omnigraph Shortcuts .

## Summary
In this tutorial, you learned to connect rigid bodies using joints, add a joint drive to control the joints, turn a chain of joints into an articulation, and control the robot using an Articulation Velocity Controller.
By the end of this tutorial, you have a robot with a body and two wheels, similar to the `mock_robot_rigged` asset, located in the `Samples/Rigging/MockRobot` folder.

### Next Steps

- Continue on to Tutorial 4: Add Camera and Sensors to a Robot to learn how to add a camera to the car.

### Further Reading
Physics Core for more details regarding joints and articulations.
