<!-- source: py/api/struct_material_assignment.html | title: MaterialAssignment — Isaac Sim -->

# MaterialAssignment
structMaterialAssignment

Defines which triangles and indices use a specific material.
This structure maps ranges of triangles and vertex indices to a specific material, allowing meshes to have multiple materials across different regions.
Public Members
intstartTri

Starting triangle index for this material assignment.

intendTri

Ending triangle index for this material assignment.

intstartIndices

Starting vertex index for this material assignment.

intendIndices

Ending vertex index for this material assignment.

intmaterial

Index of the material to use for this range.
