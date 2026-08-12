<!-- source: py/api/function__prim_utils_8h_1a5ad8bc9fdc7207dfaee41f1bc3256898.html | title: findMatchingPrimPaths — Isaac Sim -->

# findMatchingPrimPaths
Fully qualified name: `isaacsim::core::utils::findMatchingPrimPaths`
std ::vector<std ::string>isaacsim ::core ::utils ::findMatchingPrimPaths(
conststd ::string&pattern,
longintstageId,
conststd ::string&api=std ::string(""),
)
Finds USD prims matching a specified path pattern.
Searches for prims in a USD stage that match the provided path pattern. The pattern supports wildcard matching for path components. Optionally filters results by specified API schemas.
Note
The pattern supports standard glob-style wildcards for matching.
Parameters:

- pattern – [in] Path pattern to match against prim paths.

- stageId – [in] ID of the USD stage to search.

- api – [in] Optional API schema filter. When specified, only returns prims with the given API. Current supported values are “articulation” and “rigid_body”.

Throws:
std ::invalid_argument – If the stage ID is invalid or the API type is not supported.

Returns:
Vector of strings containing paths of matching prims.
