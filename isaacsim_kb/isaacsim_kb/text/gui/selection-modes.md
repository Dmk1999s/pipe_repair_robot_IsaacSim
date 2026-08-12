<!-- source: gui/selection-modes.html | title: Selection Modes — Isaac Sim Documentation -->

# Selection Modes
There are two selection modes in Omniverse: Selection by type and selection by model kind. Selection by type selects as deep in the tree possible and Selection by model kind starts at the clicked mesh and searches up the stage tree until it finds a prim of the currently specified model kind. A prim’s type is set when the prim is created and a prim’s kind is a property that can be set by the user in the properties window.

## Changing Selection Mode
To toggle between type and model kind selection, click on the top-most icon in the toolbar immediately to the right of the viewport as shown below:
Click on the selection mode button to toggle between type and model kind selection.
Note
Press T Hot-Key to quickly toggle between selection modes. Press Q Hot-Key to switch to select from a transform mode.
In addition, right clicking the selection mode button displays the selection rollout, which has specific type and kind options. These options will be explained in the respective type and model kind subsections.
Right click on the selection mode button to display type and model kind selection mode options.

### Type Selection
The selection toggle button will appear as two grey boxes and one orange box as shown below to indicate type selection mode.
Two grey boxes and one orange box will display in the selection mode toggle button if type selection is active.
While in this mode, clicking on an item in the viewport will select the lowest corresponding item in the stage tree. This will typically be a mesh, but could also be a light or a camera.
After right clicking the selection mode toggle button there are four filtering options for this selection mode: All Prim Types, Meshes, Lights and Cameras. All Prim Types is selected by default and does not filter the selection. Meshes, Lights and Cameras will filter the selection by the specified type.
The prim type is set when a prim is created and cannot be edited; it is inherent to the prim.
Note
When in prim mode, you can select a parent group by selecting the containment outline (bounding box).

### Model Kind Selection
The selection toggle button will appear as a single grey box as shown below to indicate model kind selection mode.
A single grey box will display in the selection mode toggle button if model kind selection is active.
While in this mode, clicking on an item in the viewport will start with the deepest item in the stage tree (what type mode would have selected) and then search up the tree for the first prim of the corresponding kind. The Kind is an attribute which can be set in the properties pane for any prim.
After right clicking the selection mode toggle button there are five filtering options for this selection mode: All Model Kinds, Assembly, Group, Component and Subcomponent. All Model Kinds is selected by default and will simply select the first prim with any Kind set. Assembly, Group, Component and Subcomponent will each navigate up the tree until encountering a prim of the specified kind.
So, a user can allow for sophisticated hierarchical group selection by purposefully choosing Model Kind selection filters and setting the kind attribute throughout their stage structure.
