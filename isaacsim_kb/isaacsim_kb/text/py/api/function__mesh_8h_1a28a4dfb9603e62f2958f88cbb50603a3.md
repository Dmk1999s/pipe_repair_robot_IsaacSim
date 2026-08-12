<!-- source: py/api/function__mesh_8h_1a28a4dfb9603e62f2958f88cbb50603a3.html | title: CreateQuadMesh — Isaac Sim -->

# CreateQuadMesh
Mesh *CreateQuadMesh(floatsizex, floatsizez, intgridx, intgridz)

Creates a subdivided quad mesh.
Generates a rectangular mesh divided into a grid of smaller quads.
Parameters:

- sizex – [in] Width of the quad in the X direction

- sizez – [in] Height of the quad in the Z direction

- gridx – [in] Number of subdivisions along X axis

- gridz – [in] Number of subdivisions along Z axis

Returns:
Pointer to the created quad mesh
