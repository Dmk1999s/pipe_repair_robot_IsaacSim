<!-- source: py/api/structisaacsim_1_1asset_1_1importer_1_1urdf_1_1_urdf_inertial.html | title: UrdfInertial — Isaac Sim -->

# UrdfInertial
Fully qualified name: `isaacsim::asset::importer::urdf::UrdfInertial`
structUrdfInertial

Inertial properties of a URDF link.
Contains the mass, center of mass location, and inertia tensor for a link. The origin represents the pose of the inertial reference frame relative to the link reference frame, with the origin at the center of gravity.
Public Members
Transform origin

Pose of the inertial reference frame relative to link frame.
The origin must be at the center of gravity.

floatmass=0.0f

Mass of the link in kilograms.

UrdfInertia inertia

Inertia tensor components for the link.

boolhasOrigin=false

Whether the origin was explicitly defined in the URDF.

boolhasMass=false

Whether the mass was explicitly defined in the URDF.

boolhasInertia=false

Whether the inertia was explicitly defined in the URDF.
