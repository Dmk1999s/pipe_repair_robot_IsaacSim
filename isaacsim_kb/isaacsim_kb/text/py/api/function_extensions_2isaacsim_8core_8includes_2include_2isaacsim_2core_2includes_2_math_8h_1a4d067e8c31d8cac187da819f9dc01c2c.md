<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_math_8h_1a4d067e8c31d8cac187da819f9dc01c2c.html | title: transformInv — Isaac Sim -->

# transformInv
Fully qualified name: `isaacsim::core::includes::math::transformInv`
inlinepxr ::GfTransformisaacsim ::core ::includes ::math ::transformInv(
constpxr ::GfTransform&a,
constpxr ::GfTransform&b,
)
Computes the local transform of b relative to transform a.
Calculates the transform that represents b’s pose in a’s local coordinate frame. This is equivalent to inverse(a) * b.
Note
This is the Pixar USD transform version of transformInv()
Parameters:

- a – [in] Reference transform that defines the local coordinate frame

- b – [in] Target transform to be expressed in a’s frame

Returns:
pxr::GfTransform Transform representing b in a’s local frame
