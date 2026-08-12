<!-- source: py/api/structisaacsim_1_1asset_1_1importer_1_1mjcf_1_1_contact_node.html | title: ContactNode — Isaac Sim -->

# ContactNode
Fully qualified name: `isaacsim::asset::importer::mjcf::ContactNode`
structContactNode

A node in the contact graph representing collision relationships.
Represents a body or geometry in the contact filtering graph, storing its name and connections to adjacent nodes for collision filtering purposes.
Public Members
std ::stringname

Name of the contact node (typically body or geometry name).

std ::set<int>adjacentNodes

Set of indices of adjacent nodes in the contact graph.
