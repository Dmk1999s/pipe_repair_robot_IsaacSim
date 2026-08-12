<!-- source: action_and_event_data_generation/ext_replicator-object/geometry.html | title: Geometry — Isaac Sim Documentation -->

# Geometry
If a mutable has attribute `type` of `geometry`, it’s a geometry. A geometry is a substance in space.
Available attributes of `geometry`:

[TABLE]
Name | Type | Description
subtype | string | refer to Basic shapes, Deformed shape, and Mesh loaded from USD
physics | string | collision or rigidbody
[/TABLE]
If `physics` is set to `rigidbody`, the object is a dynamic object that responds to physics. If it’s set to `collision`, the object is a static object that dynamic objects interact with. For example, a wall can have `collision` and a ping-pong ball bouncing off of it has `rigidbody`.
Basic shapes
If `subtype` is one of `cone`, `cube`, `cylinder`, `disk`, `torus`, `plane`, or `sphere` it defines the corresponding basic geometry.
Deformed shape
Physics simulation for bottles is not supported.
If `subtype` is `bottle`, it defines a bottle shape, which is a parameterized deformed geometry controlled by the following parameters:

[TABLE]
Name | Type | Description
base_effector | string | vertical position of the base effector
neck_effector | string | vertical position of the neck effector
horizontal_effector | string | horizontal position of the body effector
vertical_effector | string | vertical position of the body effector
[/TABLE]
This image illustrates how the shape of the bottle is controlled by these four effectors.
Note
We currently don’t yet have collision detection for deformed shapes; they don’t have physics.
Mesh loaded from USD
If `subtype` is `mesh`, it defines a mesh loaded from USD.
Additional attribute of mesh:

[TABLE]
Name | Type | Description
usd_path | string | The path to the USD in disk
[/TABLE]
