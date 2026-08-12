<!-- source: py/api/struct_mesh.html | title: Mesh — Isaac Sim -->

# Mesh
structMesh

Core mesh data structure with geometry and material information.
Contains vertex data, connectivity information, materials, and various utility functions for mesh manipulation and processing. Supports conversion to USD format and asset conversion operations.
Public Functions
voidAddMesh(constMesh &m)

Merges another mesh into this mesh.
Combines vertex data, indices, and materials from the source mesh into this mesh, effectively creating a single merged mesh.
Parameters:
m – [in] The mesh to merge into this mesh

inlineuint32_tGetNumVertices()const

Gets the total number of vertices in the mesh.
Returns:
Number of vertices as unsigned 32-bit integer

inlineuint32_tGetNumFaces()const

Gets the total number of faces (triangles) in the mesh.
Returns:
Number of faces as unsigned 32-bit integer

voidDuplicateVertex(uint32_ti)

Duplicates a vertex at the specified index.
Creates a copy of the vertex data at the given index, adding it to the end of the vertex arrays.
Parameters:
i – [in] Index of the vertex to duplicate

voidCalculateFaceNormals()

Calculates face normals by splitting vertices.
Computes faceted normals by duplicating vertices where needed, changing the mesh topology to create sharp edges between faces.

voidCalculateNormals()

Calculates smooth vertex normals.
Computes per-vertex normals by averaging adjacent face normals, creating smooth shading across the surface.

voidTransform(constMatrix44 &m)

Transforms the mesh by the given transformation matrix.
Applies the transformation matrix to all vertex positions and normal vectors in the mesh.
Parameters:
m – [in] 4x4 transformation matrix to apply

voidNormalize(floats=1.0f)

Normalizes the mesh to fit within specified bounds.
Scales the mesh so that its maximum dimension equals the specified size and moves it so the minimum bound is at origin.
Parameters:
s – [in] Target size for the largest dimension (default: 1.0)

voidFlip()

Flips the mesh by reversing face winding order.
Reverses the vertex order of all triangles, effectively flipping the surface normals and changing inside/outside orientation.

voidGetBounds(Vector3 &minExtents, Vector3 &maxExtents)const

Calculates the axis-aligned bounding box of the mesh.
Computes the minimum and maximum extents of the mesh along each coordinate axis.
Parameters:

- minExtents – [out] Minimum bounds of the mesh

- maxExtents – [out] Maximum bounds of the mesh

Public Members
std ::stringname

Optional name identifier for the mesh.

std ::vector<Point3 >m_positions

Array of vertex positions in 3D space.

std ::vector<Vector3 >m_normals

Array of vertex normal vectors.

std ::vector<Vector2 >m_texcoords

Array of 2D texture coordinates per vertex.

std ::vector<Colour >m_colours

Array of vertex colors.

std ::vector<uint32_t>m_indices

Array of vertex indices defining triangle connectivity.

std ::vector<Material >m_materials

Array of materials used by this mesh.

std ::vector<MaterialAssignment >m_materialAssignments

Array of material assignments to mesh regions.

std ::vector<USDMesh >m_usdMeshPrims

Array of USD-compatible mesh representations.

std ::stringm_convertedUsdMesh

Path to converted USD mesh file.

Vec3 scale={1.0f,1.0f,1.0f}

Scale factor applied to the mesh (X, Y, Z).

OmniConverterFuture*m_assetConvertStatus=nullptr

Pointer to asset conversion status tracker.
