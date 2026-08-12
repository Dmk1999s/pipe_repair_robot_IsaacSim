<!-- source: py/api/struct_u_v_info.html | title: UVInfo — Isaac Sim -->

# UVInfo
structUVInfo

UV texture coordinate information for mesh surfaces.
Contains UV mapping data with support for multiple UV sets and corresponding index arrays for texture coordinate assignment.
Public Members
std ::vector<std ::vector<Vector2 >>uvs

UV coordinate arrays for multiple texture sets.

std ::vector<unsignedint>uvStartIndices

Starting indices for UV coordinate arrays.
