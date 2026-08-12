<!-- source: py/api/structisaacsim_1_1asset_1_1importer_1_1urdf_1_1_urdf_joint.html | title: UrdfJoint — Isaac Sim -->

# UrdfJoint
Fully qualified name: `isaacsim::asset::importer::urdf::UrdfJoint`
structUrdfJoint

Joint definition connecting two links in URDF robot model.
Represents a kinematic joint between parent and child links with motion constraints, dynamics properties, control parameters, and hierarchical relationships.
Public Members
std ::stringname

Name identifier for the joint.

UrdfJointType type

Type of joint (revolute, prismatic, fixed, etc.).

Transform origin

Transform from parent link to child link frame.
The joint is located at the origin of the child link.

std ::stringparentLinkName

Name of the parent link.

std ::stringchildLinkName

Name of the child link.

UrdfAxis axis

Axis of rotation or translation for the joint.

UrdfDynamics dynamics

Dynamics properties (damping, friction, stiffness).

UrdfLimit limit

Motion limits for the joint.

UrdfJointDrive drive

Drive configuration for joint actuation.

UrdfJointMimic mimic

Mimic configuration for coupled joint motion.

std ::map<std ::string,float>mimicChildren

Map of child joints that mimic this joint with their multipliers.

floatnaturalStiffness

Natural stiffness used for auto-configuring position control gains.

floatjointInertia

Joint inertia used for auto-configuring position control gains.

booldontCollapse=false

Custom attribute to prevent fixed joint merging.
Prevents the child link from being collapsed into the parent link when fixed joint merging is enabled. Useful for sensor or end-effector frames. This is a custom Isaac Gym extension, not part of standard URDF.

std ::stringparentJoint

Name of the parent joint in the kinematic tree.

std ::vector<std ::string>childrenJoints

Names of child joints in the kinematic tree.
