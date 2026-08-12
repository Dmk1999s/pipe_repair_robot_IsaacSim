<!-- source: omniverse_usd/intro_to_usd.html | title: Working with USD — Isaac Sim Documentation -->

# Working with USD

## Learning Objectives
This tutorial covers how to:

- save USD stages

- load and reference existing USD stages

- Organize stage tree hierarchy

## Saving Options

- Save: To save the current USD stage, go to the Menu Bar and click Files > Save or Files > Save As .. to save as a new file.

- Save Flattened As: Saves the current USD file while merging all components to one mesh.

- as .usda files: You have the option to save as `.usda` file instead of `.usd` file. `.usda` file is a human-readable text file format for the given USD stage.

- Collect Assets: If your current stage used many reference USD stages, materials, and textures from other folders and servers, you must Collect Assets to make sure all the external references that are used in your stage get collected in one folder. To do so, save the current USD locally, then find it in the Content tab, right-click on it, and select Collect Asset.

## Loading Options

- Open: To load a USD stage, go to Menu Bar and click Files > Open. This opens the USD stage for direct editing.

- Add Reference: Files > Add Reference adds a USD file as a reference. Or find the file in the Content Tab and drag it into the viewport. You can not edit the referenced USD.

### Set the Stage for a Reference
To demonstrate adding a file as reference, save the current stage with the cube and cylinders as a mock robot. First, you must rearrange the rigid bodies on the stage into a hierarchical structure with meaningful names. Put all the rigid body parts of the robot under a single Prim .

- Right click inside the Stage tab, select Create > Xform.

- Rename the newly added Xform to mock_robot. The Prim appears under the World prim.

- Drag and drop the Cube, both Cylinders, Physics Material, and Looks folder under mock_robot.

- Rename the Cube and Cylinders to the body, wheel_left, and wheel_right.

- Save the stage as an USD file.

- Open a new stage.

- Load the USD file as a reference, either Files > Add Reference or drag the file from Content on to the stage. It loads the referenced USD under a Prim withe the same name as the USD filename.

- Validate that it loaded everything under the original `World(defaultPrim)`, including `PhysicsScene`, `defaultLight`, and `GroundPlane`. This may not be optimal if you are loading multiple USD references that all have their own version of PhysicsScenes and defaultLights. You cannot delete them on the new stage because they are loaded by reference, but deleting them in the original USD would make it difficult to work within those USD stages.

To have the necessary environment set up in the USD stages but not export them when they are being referenced, you need to move non-referenced items out of the default Prim:

- Select the robot’s parent prim on stage, in this tutorial /mock_robot.

- Open the menu Edit while the prim is selected, and click on unparent.

- Validate that instead of being under World, mock_robot is parallel to World.

- Right-click on the robot prim again on stage, and Set as a Default Prim. Save.

- Open a new stage and load the same file again as a reference, verify that only the robot is imported.

## Summary
In this tutorial, you learned how to save and open USD files.

### Further Readings
More on File Menu , Collect Assets , and others in Composer .
