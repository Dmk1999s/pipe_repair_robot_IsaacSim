<!-- source: assets/usd_assets_nurec.html | title: Neural Volume Rendering — Isaac Sim Documentation -->

# Neural Volume Rendering
NuRec (Neural Reconstruction) enables scene rendering in Omniverse using neural volumes derived from real-world images. These scenes, based on 3D Gaussian models, can be loaded into Isaac Sim as standard USD assets for visualization and simulation.
For more details on how NuRec works in Omniverse, including data preparation, rendering settings, and known limitations, see the NuRec documentation . To generate compatible scenes, you can use the open-source project 3DGruT which provides tools for training 3D Gaussian models from image collections and exporting them in a USDZ-based format suitable for use in Omniverse applications.

## Example
[image: NuRec Carter NavigationScene]The following example demonstrates how to load a NuRec scene into Isaac Sim and run a simulation. The snippet iterates over the provided examples and starts by loading the provided stage, it then loads the carter navigation asset and sets the start location. It then checks if a collision ground plane needs to be created at the spawn location, and if so, creates a plane prim with a collision API applied. It then sets the carter navigation target prim location and runs the simulation for the given number of steps. During the simulation the wheeled robot will navigate towards the target location.
The example script can be run directly from the Script Editor or as a Standalone Application .

### Prerequisites

- Download the NVIDIA NuRec Dataset from Hugging Face .

- Update the `USER_PATH` variable in the script: `USER_PATH = "/home/user/PhysicalAI-Robotics-NuRec"`
