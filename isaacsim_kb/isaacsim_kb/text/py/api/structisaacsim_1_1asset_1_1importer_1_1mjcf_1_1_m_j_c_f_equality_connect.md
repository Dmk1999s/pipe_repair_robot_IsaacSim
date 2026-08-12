<!-- source: py/api/structisaacsim_1_1asset_1_1importer_1_1mjcf_1_1_m_j_c_f_equality_connect.html | title: MJCFEqualityConnect — Isaac Sim -->

# MJCFEqualityConnect
Fully qualified name: `isaacsim::asset::importer::mjcf::MJCFEqualityConnect`
structMJCFEqualityConnect

Equality constraint that connects two bodies at a fixed relative position.
Represents an equality constraint in MJCF that constrains two bodies to maintain a fixed relative position and orientation. This is used to create rigid connections between bodies in the simulation.
Public Members
std ::stringbody1

Name of the first body in the constraint.

std ::stringbody2

Name of the second body in the constraint.

Vec3 anchor

Anchor point for the constraint connection.
