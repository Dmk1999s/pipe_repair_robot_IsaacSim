<!-- source: replicator_tutorials/tutorial_replicator_custom_og_randomizer.html | title: Custom Replicator Randomization Nodes — Isaac Sim Documentation -->

# Custom Replicator Randomization Nodes
This tutorial provides an example of how to create custom randomization nodes for the omni.replicator extension.

## Learning Objectives
The goal of this tutorial is to demonstrate how to create custom OmniGraph randomization nodes. These nodes can then be further integrated into the Synthetic Data Generation (SDG) pipeline graph of Replicator .
This tutorial will showcase how to:

- Create custom scene randomization Python scripts.

- Wrap the scripts as OmniGraph nodes and manually add them to an existing SDG pipeline graph.

- Encapsulate the OmniGraph nodes as ReplicatorItems to be automatically added to the SDG pipeline graph using Replicator’s API.

## Prerequisites

- Familiarity with USD / Isaac Sim APIs for creating custom scene randomizers. See Randomization Snippets for more details.

- Familiarity with omni.replicator and its randomization API replicator randomizers .

- Basic knowledge of OmniGraph and how to create OmniGraph Nodes .

- Experience running simulations via the Script Editor .

## Implementation
This tutorial will showcase how to create custom scene randomization Python scripts. These scripts will create prims in a new stage and randomize their rotation and locations: in a sphere, on a sphere, and between two spheres.
The following image shows the result after running the randomization in the Script Editor:
As a next step, custom OmniGraph Nodes are created for the randomization functions. The node descriptions and implementations can be found in the following code snippets:
After this step, the randomizers will be available as nodes in the graph editor. For this tutorial the nodes are already added to the built-in `isaacsim.replicator.examples` extension and are available by default. Other custom nodes created through the OmniGraph tutorial will be accessible through the `omni.new.extension` extension (if the default tutorial-provided extension name was used). An example of accessing the nodes in an action graph is depicted below:
Note
If the custom nodes are not available, the newly created extension needs to be enabled. This can be done by navigating to Window > Extensions > THIRD PARTY > ``omni.new.extension`` > ENABLED:
After the OmniGraph randomization nodes are created, they can be manually added to a pre-existing SDG pipeline graph. To create a basic SDG graph, the following snippet can be used in the Script Editor to randomize the rotations of the created cubes every frame.
Basic SDG Pipeline
```
import omni.replicator.core as rep

cube = rep.create.cube(count=50, scale=0.1)
with rep.trigger.on_frame():
with cube:
rep.randomizer.rotation()
```
After the snippet is executed in the Script Editor, the generated graph can be opened at `/Replicator/SDGPipeline` and the custom nodes can be added to the graph. The following image shows the result after the custom nodes are added to the SDG pipeline graph together with the resulting randomization (from the UI using `Tools` > `Replicator` > `Preview` or `Step`):
To avoid manually adding the custom nodes to the SDG pipeline graph, the Replicator API can be used to automatically insert the nodes into the graph. For this purpose, the nodes need to be encapsulated as ReplicatorItems using the `@ReplicatorWrapper` decorator. The following code snippet demonstrates how ReplicatorItems can be created for the custom nodes:
ReplicatorWrapper
```
import omni.replicator.core as rep
from omni.replicator.core.scripts.utils import (
ReplicatorItem,
ReplicatorWrapper,
create_node,
set_target_prims,
)

@ReplicatorWrapper
def on_sphere(
radius: float = 1.0,
input_prims: ReplicatorItem | list[str] | None = None,
) -> ReplicatorItem:

node = create_node("isaacsim.replicator.examples.OgnSampleOnSphere", radius=radius)
if input_prims:
set_target_prims(node, "inputs:prims", input_prims)
return node

@ReplicatorWrapper
def in_sphere(
radius: float = 1.0,
input_prims: ReplicatorItem | list[str] | None = None,
) -> ReplicatorItem:

node = create_node("isaacsim.replicator.examples.OgnSampleInSphere", radius=radius)
if input_prims:
set_target_prims(node, "inputs:prims", input_prims)
return node

@ReplicatorWrapper
def between_spheres(
radius1: float = 0.5,
radius2: float = 1.0,
input_prims: ReplicatorItem | list[str] | None = None,
) -> ReplicatorItem:

node = create_node("isaacsim.replicator.examples.OgnSampleBetweenSpheres", radius1=radius1, radius2=radius2)
if input_prims:
set_target_prims(node, "inputs:prims", input_prims)
return node

prim_count = 50
prim_scale = 0.1
rad_in = 0.5
rad_on = 1.5
rad_bet1 = 2.5
rad_bet2 = 3.5

# Create the default prims
sphere = rep.create.sphere(count=prim_count, scale=prim_scale)
cube = rep.create.cube(count=prim_count, scale=prim_scale)
cylinder = rep.create.cylinder(count=prim_count, scale=prim_scale)

# Create the randomization graph
with rep.trigger.on_frame():
with sphere:
rep.randomizer.rotation()
in_sphere(rad_in)

with cube:
rep.randomizer.rotation()
on_sphere(rad_on)

with cylinder:
rep.randomizer.rotation()
between_spheres(rad_bet1, rad_bet2)
```
Note
For this tutorial the `create_node` function uses `"isaacsim.replicator.examples.OgnSampleInSphere"` as the node path, this path needs to be replaced in case the custom nodes are not part of the built-in `isaacsim.replicator.examples` extension.
After the snippet is executed in the Script Editor, the custom nodes will be automatically added to the SDG pipeline graph. To trigger the randomization, `Tools` > `Replicator` > `Preview` (or `Step`) can be called from the UI. The following image shows the generated graph and the resulting randomization:
