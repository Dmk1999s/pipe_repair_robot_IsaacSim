<!-- source: py/api/function__prim_utils_8h_1a58fe1aa80e79ec62342e2d7d15ed062d.html | title: findMatchingChildren — Isaac Sim -->

# findMatchingChildren
Fully qualified name: `isaacsim::core::utils::findMatchingChildren`
voidisaacsim ::core ::utils ::findMatchingChildren(
pxr ::UsdPrimroot,
conststd ::string&pattern,
std ::vector<pxr ::UsdPrim>&primsRet,
)
Finds child prims matching a specified name pattern.
Searches immediate children of a root prim for names matching the specified pattern. Uses TfPatternMatcher for name comparison.
Note
If the root prim is invalid, the function returns without modifying primsRet.
Note
The pattern uses TfPatternMatcher syntax which supports glob-style wildcards.
Parameters:

- root – [in] The parent prim whose children will be searched.

- pattern – [in] The name pattern to match against child prim names.

- primsRet – [out] Vector that will be populated with matching child prims.
