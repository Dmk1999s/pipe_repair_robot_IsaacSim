<!-- source: py/api/function__mesh_8h_1a7ed263d39e94e4638b37bca1ae9bb95f.html | title: CreateCapsule — Isaac Sim -->

# CreateCapsule
Mesh *CreateCapsule(
intslices,
intsegments,
floatradius=1.0f,
floathalfHeight=1.0f,
)
Creates a capsule mesh primitive.
Generates a capsule (cylinder with hemispherical end caps) mesh.
Parameters:

- slices – [in] Number of circumferential slices

- segments – [in] Number of segments along the length

- radius – [in] Radius of the capsule (default: 1.0)

- halfHeight – [in] Half-height of the cylindrical portion (default: 1.0)

Returns:
Pointer to the created capsule mesh
