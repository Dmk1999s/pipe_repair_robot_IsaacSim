<!-- source: py/api/structisaacsim_1_1asset_1_1importer_1_1urdf_1_1_urdf_loop_joint.html | title: UrdfLoopJoint — Isaac Sim -->

# UrdfLoopJoint
Fully qualified name: `isaacsim::asset::importer::urdf::UrdfLoopJoint`
structUrdfLoopJoint

Loop joint definition for closed kinematic chains.
Represents a joint that creates a closed loop in the kinematic structure by connecting two links that are already connected through other joints.
Public Members
std ::stringname

Name identifier for the loop joint.

UrdfJointType type

Type of joint creating the loop closure.

std ::stringlinkName[2]

Names of the two links connected by the loop joint.

Transform linkPose[2]

Poses of the connection points on each link.
