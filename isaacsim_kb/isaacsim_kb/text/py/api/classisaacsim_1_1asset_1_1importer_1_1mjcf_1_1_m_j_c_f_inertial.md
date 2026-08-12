<!-- source: py/api/classisaacsim_1_1asset_1_1importer_1_1mjcf_1_1_m_j_c_f_inertial.html | title: MJCFInertial — Isaac Sim -->

# MJCFInertial
Fully qualified name: `isaacsim::asset::importer::mjcf::MJCFInertial`
classMJCFInertial

Inertial properties of a body in the MJCF model.
Defines the mass distribution and inertial properties of a rigid body. Contains mass, center of mass position, and moment of inertia tensor information needed for dynamics computation.
Public Functions
inlineMJCFInertial()

Public Members
floatmass

Total mass of the body.

Vec3 pos

Position of the center of mass relative to the body frame.

Vec3 diaginertia

Diagonal elements of the inertia tensor.

Quat principalAxes

Principal axes orientation as a quaternion.

boolhasFullInertia

Whether the full inertia tensor is specified.
