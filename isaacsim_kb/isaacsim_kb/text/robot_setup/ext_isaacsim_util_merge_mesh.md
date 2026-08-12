<!-- source: robot_setup/ext_isaacsim_util_merge_mesh.html | title: Merge Mesh Utility — Isaac Sim Documentation -->

# Merge Mesh Utility

## About
The Merge Mesh Utility Extension is used to merge multiple prims into a single mesh. Geometry subsets are used when there are multiple materials on the set of meshes being merged.
To access this Extension, go to the top menu bar and click Tools> Robotics > Asset Editors > Mesh Merge Tool. This extension is enabled by default. If it is ever disabled, it can be re-enabled from the Extension Manager by searching for `isaacsim.util.merge_mesh`.

## User Interface
[image: Merge Mesh UI]

### Configuration Options
Under the input section you will observe:

- Source Prim: This text box shows the prims selected to be merged. TThis gets automatically populated by the selection in the scene. The first item selected will be used as base and origin for the merged asset.

- Submeshes: The number of meshes the selected prim contains.

- Geometry Subsets: The number of subsets the selected prim contains.

- Materials: The number of unique materials used by the selected prim.

Note
To change the mesh origin, you can first select an empty Xform at the desired origin pose, then select all meshes you want to merge afterwards.
Under the output section you will observe:

- Destination Prim: The auto-generated output path for the merged mesh.

- Geometry Subsets: The number of geometry subsets created after merge. Each unique material will generate a subset on the final merged mesh.

The options when merging are:

- Clear Parent Transform: When selected, the merged mesh transform will be at world origin, otherwise it will be the same as the source prim.

- Deactivate source assets: When selected, the prims that were selected for merging will be set to “inactive” (effectively deleted, but can be reactivated later).

- Combine Materials: When selected, provide the Prim for the Looks folder, it will combine all meshes that use the same material (checked by material name) into a single geomsubset, and move that material to the provided Looks Folder. This is useful for Onshape and Cad imported assets, that contain internal Looks Scopes that are sublayers to the a materials USD layer.

## Tutorials and Examples
The following example showcases how to best use this extension:
