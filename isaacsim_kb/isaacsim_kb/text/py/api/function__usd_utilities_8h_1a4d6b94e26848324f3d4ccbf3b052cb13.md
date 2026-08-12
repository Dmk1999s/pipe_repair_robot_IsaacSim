<!-- source: py/api/function__usd_utilities_8h_1a4d6b94e26848324f3d4ccbf3b052cb13.html | title: getCameraPrimFromRenderProduct — Isaac Sim -->

# getCameraPrimFromRenderProduct
Fully qualified name: `isaacsim::core::includes::getCameraPrimFromRenderProduct`
inlinepxr ::UsdPrimisaacsim ::core ::includes ::getCameraPrimFromRenderProduct(
conststd ::string&renderProductPathString,
)
Retrieves the camera prim associated with a render product.
Looks up the camera prim referenced by a render product in the current USD stage. The function performs several validation steps:

- Checks for valid stage and interfaces

- Creates render product prim handle

- Extracts camera path and retrieves corresponding prim

Note
Returns invalid prim if any required component is missing
Warning
Requires valid USD context and stage
Parameters:
renderProductPathString – [in] Path to the render product as a string

Returns:
pxr::UsdPrim Camera prim if found, invalid prim otherwise
