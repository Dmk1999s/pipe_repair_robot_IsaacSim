<!-- source: py/api/function__usd_utilities_8h_1aad6451fee194fd772ab26ad442299959.html | title: getSdfPathFromUint64 — Isaac Sim -->

# getSdfPathFromUint64
Fully qualified name: `isaacsim::core::includes::getSdfPathFromUint64`
inlinepxr ::SdfPathisaacsim ::core ::includes ::getSdfPathFromUint64(
uint64_tpathToken,
)
Converts a uint64_t token to a USD path.
Performs a reinterpret cast from uint64_t to SdfPath with:

- Platform-specific warning suppression

- Safe type conversion

Warning
Uses reinterpret_cast, ensure token is a valid path representation
Parameters:
pathToken – [in] Path token as uint64_t

Returns:
pxr::SdfPath Converted USD path
