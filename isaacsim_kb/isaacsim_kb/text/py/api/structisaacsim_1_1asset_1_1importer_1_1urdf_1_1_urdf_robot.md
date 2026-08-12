<!-- source: py/api/structisaacsim_1_1asset_1_1importer_1_1urdf_1_1_urdf_robot.html | title: UrdfRobot — Isaac Sim -->

# UrdfRobot
Fully qualified name: `isaacsim::asset::importer::urdf::UrdfRobot`
structUrdfRobot

Complete URDF robot model definition.
Represents the entire robot model containing all links, joints, materials, and metadata. Serves as the root container for the robot description.
Public Members
std ::stringname

Name identifier for the robot.

std ::stringrootLink

Name of the root link in the kinematic tree.

std ::stringurdfPath

File path to the original URDF file.

std ::stringassetRoot

Root directory for resolving relative asset paths.

std ::map<std ::string,UrdfLink >links

Map of all links in the robot indexed by name.

std ::map<std ::string,UrdfJoint >joints

Map of all joints in the robot indexed by name.

std ::map<std ::string,UrdfLoopJoint >loopJoints

Map of all loop joints in the robot indexed by name.

std ::map<std ::string,UrdfMaterial >materials

Map of all materials in the robot indexed by name.
