<!-- source: py/api/classisaacsim_1_1asset_1_1importer_1_1urdf_1_1_kinematic_chain.html | title: KinematicChain — Isaac Sim -->

# KinematicChain
Fully qualified name: `isaacsim::asset::importer::urdf::KinematicChain`

## Structs
Node
Represents a single node in the kinematic tree.

classKinematicChain

Represents the kinematic chain of a robot as a tree structure.
This class builds and manages a tree representation of a robot’s kinematic structure, where each node represents a link connected by joints. The tree structure allows for efficient traversal and analysis of the robot’s kinematic relationships.
Public Functions
KinematicChain()=default

Default constructor creates an empty kinematic chain.

~KinematicChain()

Destructor cleans up the kinematic tree.

boolcomputeKinematicChain(constUrdfRobot &urdfRobot)

Computes the kinematic chain for a URDF robot description.
Parameters:
urdfRobot – [in] URDF robot data structure to build chain from

Returns:
True if kinematic chain was successfully computed, false otherwise

Public Members
std ::unique_ptr<Node >baseNode

Root node of the kinematic tree (base link)

structNode

Represents a single node in the kinematic tree.
Each node represents a link in the robot with its associated parent joint and child nodes (links). This forms a tree structure representing the complete kinematic chain of the robot.
Public Functions
inlineNode(std ::stringlinkName, std ::stringparentJointName)

Constructs a new node with specified link and parent joint names.
Parameters:

- linkName – [in] Name of the link for this node

- parentJointName – [in] Name of the parent joint connecting this link

Public Members
std ::stringlinkName_

Name of the link represented by this node.

std ::stringparentJointName_

Name of the parent joint connecting this link.

std ::vector<std ::unique_ptr<Node >>childNodes_

Collection of child nodes (links) connected to this node.
