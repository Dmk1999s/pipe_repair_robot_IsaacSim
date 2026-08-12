<!-- source: robot_simulation/ext_isaacsim_robot_surface_gripper.html | title: Surface Gripper Extension — Isaac Sim Documentation -->

# Surface Gripper Extension

## About
The Surface Gripper Extension Extension is used to create a suction-cup gripper behavior for an end-effector. It works by parsing the Surface Gripper properties on the USD Surface Gripper Schema, and managing a set of D6 Joints between the parent and child rigid bodies at the gripper points of contact.
The physical properties of the gripper are defined on the D6 Joints properties, such as joint limits across the different degrees of freedom, and the stiffness and damping of the joint. The Surface gripper Object then handles the activation of the constraints, and define which objects to be grasped based on the grip threshold.
This extension is enabled by default. If it is ever disabled, it can be re-enabled from the Extension Manager by searching for `isaacsim.robot.surface_gripper`.
To create a surface gripper through the GUI, Go to the menu `Create` > `Robots` > `Surface Gripper`. This will create a surface gripper prim in the stage.

## API Documentation
See the API Documentation for usage information.

## Setting up a Surface Gripper
The Surface Gripper Has the following properties:

[TABLE]
Property | Description
Attachment Points | The list of Joints that will be used to attach the gripper to the object
Status | (Read-Only) The current state of the gripper
Gripped Objects | (Read-Only) The list of objects that are currently grasped by the gripper
Max Grip Distance | Distance from the gripper point that will accept closing contact
Retry Interval | How long the gripper will remain attempting to close on an object
Shear Force Limit | The maximum lateral force that the gripper can apply to an object before it will break the constraint
Coaxial Force Limit | The maximum axial force that the gripper can apply to an object before it will break the constraint
[/TABLE]

### Attachment Joints
The joints that will be used to attach the gripper to the object are defined on the `Attachment Points` property. This is a list of paths to the D6 Joints that will be used to attach the gripper to the object. These joints must be defined on the USD file at the gripper points of contact, and must be of type `D6`. Any physical properties for the joint are defined on the D6 Joint Schema, but there are a few properties that are required to be set for the Joint:

- Joint must be enabled

- All joints Body 0 must be the same.

- Joint must have “Exclude from Articulation” set to True. If this is not set, the surface gripper manager will set it to True at runtime.

### Attachment Point API
The joints that are defined on the `Attachment Points` property are automatically assigned the `Attachment API`. This API is responsible for providing additional attributes to the joint, which are necessary for the Surface Gripper Manager to handle the gripper. In the attachment point API, the following attributes are available:

- ClearanceOffset: This registers the distance from the joint to the parent object’s surface. Since the surface gripper works by sending a raycast from the joint world position, this offset will be added to the raycast origin to avoid false positive hits with the parent object. If this offset is not defined, it will start at the joint’s world position, and whenever it clears the parent object collider, it will author the offset at runtime for future use.

- Forward Axis: This registers which joint axis will be used to attempt to close the gripper. The default value is `X`.

#### Adding Attachment Joint API
To add an attachment joint API, select the joint in the stage, and in the right panel under the Properties tab, check the + Add button, and select `Edit API Schema`. Search for AttachmentPointAPI and apply it to the joint.

## Tutorials & Examples
Activate the `Robotics Examples` content browser from Windows > Examples > Robotics Examples. Navigate to Manipulation, select the Surface Gripper Example, and click the load button in the information window on the right side of the Robotics Examples content browser. You may need to adjust the GUI to see the load button.

### Surface Gripper Example
This example shows a Surface gripper mounted to a gantry, and contains cubes that can be grasped by the gripper. This Surface gripper is Added by code, and also connected throug the surface gripper Omniverse OmniGraph node.
To run the Example:

- Press the Load button. The scene should begin playing.

- You can move the Gantry with the gamepad axis, or by manually editing the gantry joint target positions.

- Move the gantry near some cube or set of cubes, and click on the “Open/Close” Button - the button label reflects the current gripper state. The gripper can also be closed by the down face button on the gamepad (e.g X on playstation controllers, or A on Xbox controllers).

- The gripper will attempt to close on the cubes, and if successful, the cubes will be grasped by the gripper.

- Lift the gantry, and the cubes will remain grasped by the gripper, or forces may be excessive and break the gripper constraint.

[image: ../_images/isim_5.0_base_ref_gui_surface_gripper_example.png]

## Omniverse OmniGraph Node
The Surface Gripper extension provides a implementation through Omniverse OmniGraph. To use it, Add a surface gripper node to the desired graph, and select the Surface gripper prim it will control.

## Creating a Surface Gripper fully on code
This section describes how to implement a surface gripper completely from code. These are snippets from the Surface Gripper Example code, and is not complete.

### Defining the Surface Gripper Properties

```
1 # Relevant Imports
2 import isaacsim.robot.surface_gripper._surface_gripper as surface_gripper
3 import usd.schema.isaac.robot_schema as robot_schema
4
5 # [...]
6
7 self.gripper_prim_path = "/World/SurfaceGripper"
8 self.gripper_interface = surface_gripper.acquire_surface_gripper_interface()
9
10 # Create the Surface Gripper Prim
11 # Once it is created it can be saved and this doesn't need to be redone
12 robot_schema.CreateSurfaceGripper(self._stage, self.gripper_prim_path)
13 gripper_prim = self._stage.GetPrimAtPath(self.gripper_prim_path)
14 attachment_points_rel = gripper_prim.GetRelationship(robot_schema.Relations.ATTACHMENT_POINTS.name)
15
16 # Select the joints to the gripper
17 # The joints should be D6 joints defined in the usd file.
18 # All joint attributes can be defined as desired, except for:
19 # Joint Should be enabled
20 # Joint Type should be D6
21 # All Joint Parents should be the same Rigid body
22 # Exclude from Articulation must be checked
23 # No Break force/Torque should be set
24 # Joint drives can be used to derive the desired joint bounce/stretch behavior
25 # Enable/Disable the joint DoFs and limits as desired.
26
27 gripper_joints = [
28 p.GetPath() for p in self._stage.GetPrimAtPath("/World/Surface_Gripper_Joints").GetChildren()
29 ]
30 attachment_points_rel.SetTargets(gripper_joints)
31
32 # Define the distance the joint can grasp, and at what distance from the origin of the joints it will settle
33 gripper_prim.GetAttribute(robot_schema.Attributes.MAX_GRIP_DISTANCE.name).Set(0.011)
34 # Define the Override Break limits
35 gripper_prim.GetAttribute(robot_schema.Attributes.COAXIAL_FORCE_LIMIT.name).Set(0.005)
36 gripper_prim.GetAttribute(robot_schema.Attributes.SHEAR_FORCE_LIMIT.name).Set(5)
37
38 # How long the gripper will try to close if it is open
39 gripper_prim.GetAttribute(robot_schema.Attributes.RETRY_INTERVAL.name).Set(1.0)
40
41 # [...]
```

### Get Gripper State
The Surface Gripper is updated on every simulation step, and the state can be retrieved at any time through the interface:

```
1 self.gripper_interface = surface_gripper.acquire_surface_gripper_interface()
2 status = self.gripper_interface.get_gripper_status(self.gripper_prim_path)
3 print(status) # Open, Closed, or Closing
```

### Controlling the Gripper
The Gripper State is controlled through the `open` and `close` methods of the interface. Alternativel, there’s also the `set_gripper_action`, which receives a numeric value between -1 and 1, where `< -0.3` will open the gripper, `> 0.3` will close it, and anything in between will be ignored.

```
1self.gripper_interface.close_gripper(gripper_prim_path)
2
3self.gripper_interface.open_gripper(gripper_prim_path)
4
5self.gripper_interface.set_gripper_action(gripper_prim_path, 0.5) # Closes the gripper
6self.gripper_interface.set_gripper_action(gripper_prim_path, -0.5) # Opens the gripper
```
