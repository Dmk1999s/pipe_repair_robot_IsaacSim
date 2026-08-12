<!-- source: py/api/enum__mesh_8h_1a5cab9ae6eb6e9ad6bc1de40e6b5660e7.html | title: GymMeshNormalMode — Isaac Sim -->

# GymMeshNormalMode
enumGymMeshNormalMode

Defines how mesh normals should be computed or loaded.
Used when loading meshes to determine the strategy for handling surface normal vectors for lighting calculations.
Values:
enumeratoreFromAsset

Load normals from the mesh asset if available.

enumeratoreComputePerVertex

Compute smooth per-vertex normals.

enumeratoreComputePerFace

Compute flat per-face normals.
