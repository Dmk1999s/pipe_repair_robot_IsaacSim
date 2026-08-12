<!-- source: py/api/function__vec2_8h_1a63bbf54997a33a3a7de3f4c3dbf0bd9c.html | title: Cross — Isaac Sim -->

# Cross
template<typenameT>
T Cross(
constXVector2 <T >&a,
constXVector2 <T >&b,
)
Computes the 2D cross product of two vectors.
For vectors (a.x, a.y) and (b.x, b.y), returns (a.x * b.y - a.y * b.x).
Template Parameters:
T – The component type of the vectors.

Parameters:

- a – [in] The first vector.

- b – [in] The second vector.

Returns:
The magnitude of the z-component if the vectors were in the xy plane.
