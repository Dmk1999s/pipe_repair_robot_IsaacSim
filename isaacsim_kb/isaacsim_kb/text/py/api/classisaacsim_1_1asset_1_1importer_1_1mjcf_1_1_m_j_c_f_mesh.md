<!-- source: py/api/classisaacsim_1_1asset_1_1importer_1_1mjcf_1_1_m_j_c_f_mesh.html | title: MJCFMesh — Isaac Sim -->

# MJCFMesh
Fully qualified name: `isaacsim::asset::importer::mjcf::MJCFMesh`
classMJCFMesh

Mesh asset definition for 3D geometry.
Defines a mesh asset that can be loaded from external files and used for collision detection or visualization. Contains the file path and scaling information for the mesh.
Public Functions
inlineMJCFMesh()

Public Members
std ::stringname

Name identifier for the mesh.

std ::stringfilename

File path to the mesh asset.

Vec3 scale

Scale factors [x, y, z] to apply to the mesh.
