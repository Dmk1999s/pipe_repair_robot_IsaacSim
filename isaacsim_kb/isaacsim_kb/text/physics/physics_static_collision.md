<!-- source: physics/physics_static_collision.html | title: Physics Static Collision Extension — Isaac Sim Documentation -->

# Physics Static Collision Extension
The Physics Static Collision Extension Extension is used to visualize collision meshes. Use this Utility extension to add static collision APIs to an entire Stage . The extension can also be used to remove all physics related APIs for testing purposes.
This extension is enabled by default. If it is ever disabled, it can be re-enabled from the Extension Manager by searching for `isaacsim.utils.physics`.
To access this Extension, go to the top menu bar and click Tools > Physics API Editor.
Note
Dynamic objects are currently not supported.

## User Interface
The User Interface provides options to add or clear static collision on selected static objects.

### Configuration Options

- Apply to children: Recursively create collision on all selected children; otherwise, create collision for just the selected object.

- Visible only: Ensure the prim is visible before creating collision. (Ignores hidden prims)

- Collision Type: Type of collision approximation to use

- Apply Static: Applies collision to the current selection.

- Remove Collision API: Clears the collision from the current selection.

- Remove All Physics APIs: Remove all Physics-related APIs (including collision) from the current selection.

### Enable Visualization
To visualize collision in any viewport:

- Select: the eye icon.

- Select: Show by type.

- Select: Physics Mesh.

- Check: All.

Note
Enable visualization after collision APIs have been applied or removed. Otherwise there will be a loss in performance while the extension traverses the desired subtree.
