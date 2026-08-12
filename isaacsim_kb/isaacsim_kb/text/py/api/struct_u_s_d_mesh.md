<!-- source: py/api/struct_u_s_d_mesh.html | title: USDMesh — Isaac Sim -->

# USDMesh
structUSDMesh

USD-compatible mesh data structure.
Contains mesh geometry data formatted for USD (Universal Scene Description) with support for points, faces, normals, UVs, and colors.
Public Members
std ::stringname

Name identifier for the USD mesh.

pxr ::VtArray<pxr ::GfVec3f>points

Array of 3D vertex positions.

pxr ::VtArray<int>faceVertexCounts

Number of vertices per face (typically 3 for triangles).

pxr ::VtArray<int>faceVertexIndices

Vertex indices defining face connectivity.

pxr ::VtArray<pxr ::GfVec3f>normals

Face-varying normal vectors for lighting.

pxr ::VtArray<pxr ::VtArray<pxr ::GfVec2f>>uvs

Face-varying UV texture coordinates.

pxr ::VtArray<pxr ::VtArray<pxr ::GfVec3f>>colors

Face-varying vertex colors.
