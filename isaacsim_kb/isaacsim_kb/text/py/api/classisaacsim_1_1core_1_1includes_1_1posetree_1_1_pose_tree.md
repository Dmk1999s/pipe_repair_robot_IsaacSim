<!-- source: py/api/classisaacsim_1_1core_1_1includes_1_1posetree_1_1_pose_tree.html | title: PoseTree — Isaac Sim -->

# PoseTree
Fully qualified name: `isaacsim::core::includes::posetree::PoseTree`
classPoseTree

A utility class for managing and traversing hierarchical pose transformations in a scene.
PoseTree provides functionality to manage and process pose transformations between different frames in a hierarchical scene structure. It handles both rigid bodies and articulated objects, computing relative transforms between parent and child frames.
The class supports:

- Parent-child relationships between prims

- Rigid body transformations

- Articulation hierarchies

- Camera-specific transformations

Note
This class requires a valid USD stage and DynamicControl instance to function properly.
Warning
Frame names must be unique within the tree. Duplicate names will be automatically renamed with their full path.
Public Functions
inlinePoseTree(
constuint64_t&stageId,
ISimulationView*simulationView,
)
Constructs a new PoseTree instance.
Initializes the PoseTree with USD stage and dynamic control references.
Parameters:

- stageId – [in] The unique identifier for the USD stage

- simulationView – [in] Pointer to the simulation view instance for physics interactions

Pre:
stageId must be valid and correspond to an existing USD stage

Pre:
simulationView must be a valid pointer to a simulation view instance

inline~PoseTree()

Destructor that cleans up cached physics views.

inlinevoidsetParentPrimPath(
constpxr ::SdfPath&parentPath,
conststd ::string&parentFrame,
)
Sets the parent prim path and frame name for the pose tree.
Establishes the root reference frame for subsequent pose calculations.
Note
The parent frame serves as the root reference for all child transformations
Parameters:

- parentPath – [in] SDF path for the parent prim in the USD stage

- parentFrame – [in] Name identifier for the parent frame

inlinevoidsetTargetPrimPaths(constpxr ::SdfPathVector&targets)

Sets the target prim paths to be processed in the pose tree.
Defines the set of prims whose poses will be computed relative to the parent frame.
Parameters:
targets – [in] Vector of SDF paths representing the target prims

inlinevoidprocessAllFrames(
std ::function<void(conststd ::string&,conststd ::string&,const::physx ::PxTransform&)>&processTransform,
)
Traverses the complete pose tree and processes each transform.
Performs a depth-first traversal of the pose tree, computing transforms between parent and child frames. Handles different types of prims including:

- Articulations and their bodies

- Rigid bodies

- Regular transforms

- Special cases like cameras

Note
The callback function receives:

- Parent frame name (string)

- Child frame name (string)

- Relative transform between frames (PxTransform)

Warning
For cameras without RTXLidar API, an additional 180-degree rotation about the x-axis is applied
Parameters:
processTransform – [in] Callback function to handle each computed transform

inline::physx ::PxTransformgetRigidBodyPose(IRigidBodyView*rb)

Retrieves the physics-based pose of a rigid body.
Queries the DynamicControl system for the current pose of a rigid body prim.
Parameters:
rb – [in] Pointer to the rigid body view interface

Returns:
PxTransform representing the world-space pose of the rigid body

Pre:
The rigid body view must be valid or nullptr (returns identity transform)

inline::physx ::PxTransformgetXformPose(constpxr ::SdfPath&path)

Gets the pose of a prim using fabric or USD.
Computes the world-space transform of a prim, prioritizing fabric data if available.
Parameters:
path – [in] SDF path to the target prim

Returns:
PxTransform representing the world-space pose of the prim

inlinestd ::stringgetUniqueFrameName(
conststd ::string&frame,
conststd ::string&path,
)
Generates a unique frame name for a given prim.
Ensures unique frame names by:

- Using the provided frame name if unique

- Using a cached renamed version if previously processed

- Creating a new unique name based on the full path if needed

Note
If a name collision occurs, the full path is used with ‘/’ replaced by ‘_’
Warning
Logs a warning when name collisions occur, suggesting the use of isaac:nameOverride
Parameters:

- frame – [in] Desired frame name

- path – [in] Full USD path of the prim

Returns:
std::string Unique frame name

inline::physx ::PxTransformgetFrameWorldPose(
conststd ::string&frame,
boolgetParent=false,
)
Retrieves the world pose of a frame.
Computes the world-space transform of a frame, prioritizing fabric data if available.
Parameters:

- frame – [in] Frame name

- getParent – [in] If true, retrieves the pose of the parent frame

Returns:
PxTransform representing the world-space pose of the frame
