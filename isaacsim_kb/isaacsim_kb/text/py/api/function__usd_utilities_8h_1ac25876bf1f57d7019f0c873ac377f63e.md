<!-- source: py/api/function__usd_utilities_8h_1ac25876bf1f57d7019f0c873ac377f63e.html | title: getName — Isaac Sim -->

# getName
Fully qualified name: `isaacsim::core::includes::getName`
inlinestd ::stringisaacsim ::core ::includes ::getName(
constpxr ::UsdPrim&prim,
)
Retrieves the name of a USD prim, with support for custom overrides.
Determines the name of a prim by:

- Using the default prim name from USD

- Checking for “isaac:nameOverride” attribute to allow custom naming

- Using the override value if present and not empty

See also
g_kIsaacNameOveride
See also
safeGetAttribute
Parameters:
prim – [in] USD prim whose name to retrieve

Returns:
std::string Name of the prim, potentially from override attribute
