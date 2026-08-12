<!-- source: py/api/classisaacsim_1_1asset_1_1importer_1_1mjcf_1_1_m_j_c_f_joint.html | title: MJCFJoint — Isaac Sim -->

# MJCFJoint
Fully qualified name: `isaacsim::asset::importer::mjcf::MJCFJoint`
classMJCFJoint

Represents a joint in the MJCF (MuJoCo XML Format) model.
Defines a kinematic joint that connects two bodies with specified degrees of freedom. Supports various joint types including hinge (revolute), slide (prismatic), ball (spherical), and free joints with configurable limits, dynamics, and control parameters.
Public Types
enumType

Enumeration of joint types supported in MJCF.
Values:
enumeratorHINGE

Revolute joint with rotation about a single axis.

enumeratorSLIDE

Prismatic joint with translation along a single axis.

enumeratorBALL

Ball joint with rotation about all three axes.

enumeratorFREE

Free joint with translation and rotation in all directions.

Public Functions
inlineMJCFJoint()

Public Members
std ::stringname

Name identifier for the joint.

Type type=HINGE

Type of the joint (hinge, slide, ball, or free).

boollimited

Whether the joint has motion limits.

floatarmature

Armature inertia for numerical stability.

floatstiffness

Stiffness coefficient for joint springs.

floatdamping

Damping coefficient for joint friction.

floatfriction

Dry friction force magnitude.

Vec3 axis

Axis of rotation or translation for the joint.

floatref

Reference angle or position for the joint.

Vec3 pos

Position offset for the joint in the parent body frame.

Vec2 range

Joint motion limits [lower, upper].

Vec2 forcerange={0.0f,0.0f}

Force limits [lower, upper] for the joint.

floatvelocityLimits[6]

Velocity limits for each degree of freedom.

floatinitVal

Initial value for the joint position or angle.
