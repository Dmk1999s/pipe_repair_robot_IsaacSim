<!-- source: py/source/extensions/isaacsim.robot_setup.assembler/docs/api.html | title: API — Isaac Sim -->

# API

## Python API

[TABLE]
RobotAssembler | RobotAssembler is a class to assemble robots from a base robot and an attachment robot.
AssembledRobot |
AssembledBodies | Class representing two assembled rigid bodies connected by a fixed joint.
[/TABLE]

classRobotAssembler
Bases: `object`
RobotAssembler is a class to assemble robots from a base robot and an attachment robot. It will create a new USD stage with the assembly and configure a variant selection to enable the attachment robot to be selected. If the variant set already exists in the source asset, it creates a new entry to it, otherwise it creates a new variant set.
assemble()
Composes the attachment robot onto the base robot, so that the attachment robot is a child of the base robot, and ready to simulate

assemble_rigid_bodies(
base_path:str,
attach_path:str,
base_mount_frame:str,
attach_mount_frame:str,
mask_all_collisions:bool=True,
refresh_asset_paths:bool=False,
)→AssembledBodies Assemble two rigid bodies into one physical structure
Parameters:

- base_robot_path (str) – Path to base robot.

- attach_robot_path (str) – Path to attach robot. The attach robot will be unrooted from the stage and attached only to the base robot

- base_robot_mount_frame (str) – Relative path to frame in base robot where there is the desired attach point.

- attach_robot_mount_frame (str) – Relative path to frame in the attach robot where there is the desired attach point.

- mask_all_collisions (bool, optional) – Mask all collisions between attach robot and base robot. This is necessary when setting single_robot=False to prevent Physics constraint violations from the new fixed joint. Advanced users may set this flag to False and use the mask_collisions() function separately for more customizable behavior. Defaults to True.

Returns:
An object representing the assembled bodies. This object can detach the composed robots and edit the fixed joint transform.

Return type:
AssembledBodies

begin_assembly(
stage,
base_prim_path,
base_mount_path,
attachment_prim_path,
attachment_mount_path,
variant_set,
variant_name,
)Start the robot assembly process.
Places the attachment robot relative to the base robot but does not compose them yet.
Parameters:

- stage (Usd.Stage) – USD stage for assembly

- base_prim_path (str) – Path to base robot prim

- base_mount_path (str) – Path to mount frame on base robot

- attachment_prim_path (str) – Path to attachment robot prim

- attachment_mount_path (str) – Path to mount frame on attachment robot

- variant_set (str) – Name of variant set to create/modify

- variant_name (str) – Name of variant to create

cancel_assembly()
Cancel the current assembly operation and reset state.

create_fixed_joint(
prim_path:str,
target0:str=None,
target1:str=None,
)→pxr.UsdPhysics.FixedJointCreate a fixed joint between two bodies
Parameters:

- prim_path (str) – Prim path at which to place new fixed joint.

- target0 (str, optional) – Prim path of frame at which to attach fixed joint. Defaults to None.

- target1 (str, optional) – Prim path of frame at which to attach fixed joint. Defaults to None.

Returns:
A USD fixed joint

Return type:
UsdPhysics.FixedJoint

finish_assemble()
is_root_joint(prim)→bool
Check if a prim is a root joint (has no body0 or body1 target).
Parameters:
prim (Usd.Prim) – Prim to check

Returns:
True if prim is a root joint, False otherwise

Return type:
bool

mask_collisions(
prim_path_a:str,
prim_path_b:str,
)→pxr.Usd.RelationshipMask collisions between two prims. All nested prims will also be included.
Parameters:

- prim_path_a (str) – Path to a prim

- prim_path_b (str) – Path to a prim

Returns:
A relationship filtering collisions between prim_path_a and prim_path_b

Return type:
Usd.Relationship

reset()

classAssembledRobot(
assembled_robots:AssembledBodies ,
)Bases: `object`
propertyattach_path:str
Prim path of the floating (attach) body
Returns:
Prim path of the floating (attach) body

Return type:
str

propertybase_path:str
Prim path of the base body
Returns:
Prim path of the base body

Return type:
str

propertycollision_mask:pxr.Usd.Relationship
A Usd Relationship masking collisions between the two assembled robots
Returns:
A Usd Relationship masking collisions between the two assembled robots

Return type:
Usd.Relationship

propertyfixed_joint:pxr.UsdPhysics.FixedJoint
USD fixed joint linking base and floating body together
Returns:
USD fixed joint linking base and floating body together

Return type:
UsdPhysics.FixedJoint

propertyroot_joints:List[pxr.UsdPhysics.Joint]
Root joints that tie the floating body to the USD stage. These are disabled in an assembled body, and will be re-enabled by the disassemble() function.
Returns:
Root joints that tie the floating body to the USD stage.

Return type:
List[UsdPhysics.Joint]

classAssembledBodies(
base_path:str,
attach_path:str,
fixed_joint:pxr.UsdPhysics.FixedJoint,
root_joints:List[pxr.UsdPhysics.Joint],
attach_body_articulation_root:pxr.Usd.Prim,
collision_mask=None,
)Bases: `object`
Class representing two assembled rigid bodies connected by a fixed joint.
This class maintains references to the base and attach bodies, the fixed joint connecting them, and provides methods to manipulate their relative transform.
propertyattach_body_articulation_root:pxr.Usd.Prim
USD articulation root of the floating body
Returns:
USD articulation root of the floating body

Return type:
Usd.Prim

propertyattach_path:str
Prim path of the floating (attach) body
Returns:
Prim path of the floating (attach) body

Return type:
str

propertybase_path:str
Prim path of the base body
Returns:
Prim path of the base body

Return type:
str

propertycollision_mask:pxr.Usd.Relationship
A Usd Relationship masking collisions between the two assembled bodies
Returns:
A Usd Relationship masking collisions between the two assembled bodies

Return type:
Usd.Relationship

propertyfixed_joint:pxr.UsdPhysics.FixedJoint
USD fixed joint linking base and floating body together
Returns:
USD fixed joint linking base and floating body together

Return type:
UsdPhysics.FixedJoint

propertyroot_joints:List[pxr.UsdPhysics.Joint]
Root joints that tie the floating body to the USD stage. These are disabled in an assembled body, and will be re-enabled by the disassemble() function.
Returns:
Root joints that tie the floating body to the USD stage.

Return type:
List[UsdPhysics.Joint]
