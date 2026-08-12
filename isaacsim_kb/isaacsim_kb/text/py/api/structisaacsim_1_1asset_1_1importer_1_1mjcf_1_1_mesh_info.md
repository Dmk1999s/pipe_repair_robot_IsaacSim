<!-- source: py/api/structisaacsim_1_1asset_1_1importer_1_1mjcf_1_1_mesh_info.html | title: MeshInfo — Isaac Sim -->

# MeshInfo
Fully qualified name: `isaacsim::asset::importer::mjcf::MeshInfo`
structMeshInfo

Information about a mesh used in the MJCF model.
Contains pointers and handles to mesh data structures used for collision detection and rendering in the physics simulation.
Public Members
Mesh *mesh=nullptr

Pointer to the mesh data structure.

TriangleMeshHandle meshId=-1

Handle to the triangle mesh for collision detection.

GymMeshHandle meshHandle=-1

Handle to the mesh in the physics simulation.
