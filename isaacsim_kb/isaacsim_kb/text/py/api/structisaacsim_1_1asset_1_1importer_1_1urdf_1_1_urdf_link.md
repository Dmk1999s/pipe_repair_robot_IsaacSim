<!-- source: py/api/structisaacsim_1_1asset_1_1importer_1_1urdf_1_1_urdf_link.html | title: UrdfLink — Isaac Sim -->

# UrdfLink
Fully qualified name: `isaacsim::asset::importer::urdf::UrdfLink`
structUrdfLink

Link definition in URDF robot model.
Represents a rigid body in the robot with inertial properties, visual elements, collision geometry, sensors, and hierarchical relationships to other links.
Public Members
std ::stringname

Name identifier for the link.

UrdfInertial inertial

Inertial properties of the link.

std ::vector<UrdfVisual >visuals

Visual elements for rendering the link.

std ::vector<UrdfCollision >collisions

Collision elements for physics simulation.

std ::map<std ::string,Transform >mergedChildren

Transforms of merged child links (for fixed joint optimization).

std ::vector<UrdfCamera >cameras

Camera sensors attached to this link.

std ::vector<UrdfRay >lidars

Lidar sensors attached to this link.

std ::stringparentLink

Name of the parent link in the kinematic tree.

std ::vector<std ::string>childrenLinks

Names of child links in the kinematic tree.
