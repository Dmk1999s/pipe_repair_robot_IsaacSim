<!-- source: py/api/function__cloner_8h_1a4cac6d06e2a1a30f22c0cd5fa08d7cad.html | title: fabricClone — Isaac Sim -->

# fabricClone
Fully qualified name: `isaacsim::core::cloner::fabricClone`
boolisaacsim ::core ::cloner ::fabricClone(
longintstageId,
conststd ::string&source_prim_path,
conststd ::vector<std ::string>&prim_paths,
)
Creates clones of a source prim at specified target paths in the USD stage.
This function performs a fabric clone operation, creating copies of a source prim at multiple target locations within the same stage.
Warning
The source prim must exist at the specified path
Parameters:

- stageId – [in] The unique identifier of the USD stage where cloning will occur

- source_prim_path – [in] The path to the source prim that will be cloned, this prim should be a valid USD prim

- prim_paths – [in] Vector of target paths where clones will be created, these prims will be created in Fabric stage not in USD stage

Returns:
true if cloning was successful, false otherwise
