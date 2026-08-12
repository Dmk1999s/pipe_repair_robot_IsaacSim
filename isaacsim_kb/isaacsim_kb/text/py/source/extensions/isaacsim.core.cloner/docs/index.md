<!-- source: py/source/extensions/isaacsim.core.cloner/docs/index.html | title: [isaacsim.core.cloner] Isaac Sim Cloner — Isaac Sim -->

# [isaacsim.core.cloner] Isaac Sim Cloner
Version: 1.4.10
The Cloner extension provides a set of APIs to clone prims and environments in an efficient way as well as filtering the collisions across the clones if needed.

## Enable Extension
The extension can be enabled (if not already) in one of the following ways:

## API

### Python API

[TABLE]
Cloner | This class provides a set of simple APIs to make duplication of objects simple.
GridCloner | This is a specialized Cloner class that will automatically generate clones in a grid fashion.
[/TABLE]

classCloner(stage:pxr.Usd.Stage=None)
Bases: `object`
This class provides a set of simple APIs to make duplication of objects simple. Objects can be cloned using this class to create copies of the same object, placed at user-specified locations in the scene.
Note that the cloning process is performed in a for-loop, so performance should be expected to follow linear scaling with an increase of clones.
clone(
source_prim_path:str,
prim_paths:List[str],
positions:ndarray|Tensor=None,
orientations:ndarray|Tensor=None,
replicate_physics:bool=False,
base_env_path:str=None,
root_path:str=None,
copy_from_source:bool=False,
unregister_physics_replication:bool=False,
enable_env_ids:bool=False,
clone_in_fabric:bool=False,
)Clones a source prim at user-specified destination paths.
Clones will be placed at user-specified positions and orientations.

Parameters:

- source_prim_path (str) – Path of source object.

- prim_paths (List[str]) – List of destination paths.

- positions (Union[np.ndarray, torch.Tensor]) – An array containing target positions of clones. Dimension must equal length of prim_paths. Defaults to None. Clones will be placed at (0, 0, 0) if not specified.

- orientations (Union[np.ndarray, torch.Tensor]) – An array containing target orientations of clones. Dimension must equal length of prim_paths. Defaults to None. Clones will have identity orientation (1, 0, 0, 0) if not specified.

- replicate_physics (bool) – Uses omni.physics replication. This will replicate physics properties directly for paths beginning with root_path and skip physics parsing for anything under the base_env_path.

- base_env_path (str) – Path to namespace for all environments. Required if replicate_physics=True and define_base_env() not called.

- root_path (str) – Prefix path for each environment. Required if replicate_physics=True and generate_paths() not called.

- copy_from_source – (bool): Setting this to False will inherit all clones from the source prim; any changes made to the source prim will be reflected in the clones. Setting this to True will make copies of the source prim when creating new clones; changes to the source prim will not be reflected in clones. Defaults to False. Note that setting this to True will take longer to execute.

- unregister_physics_replication (bool) – Setting this to True will unregister the physics replicator on the current stage.

- enable_env_ids (bool) – Setting this enables co-location of clones in physics with automatic filtering of collisions between clones.

Raises:
Exception – Raises exception if source prim path is not valid.

define_base_env(base_env_path:str)
Creates a USD Scope at base_env_path. This is designed to be the parent that holds all clones.
Parameters:
base_env_path (str) – Path to create the USD Scope at.

disable_change_listener()
enable_change_listener()
filter_collisions(
physicsscene_path:str,
collision_root_path:str,
prim_paths:List[str],
global_paths:List[str]=[],
)Filters collisions between clones. Clones will not collide with each other, but can collide with objects specified in global_paths.
Parameters:

- physicsscene_path (str) – Path to PhysicsScene object in stage.

- collision_root_path (str) – Path to place collision groups under.

- prim_paths (List[str]) – Paths of objects to filter out collision.

- global_paths (List[str]) – Paths of objects to generate collision (e.g. ground plane).

generate_paths(root_path:str, num_paths:int)
Generates a list of paths under the root path specified.
Parameters:

- root_path (str) – Base path where new paths will be created under.

- num_paths (int) – Number of paths to generate.

Returns:
A list of paths

Return type:
paths (List[str])

replicate_physics(
source_prim_path:str,
prim_paths:list,
base_env_path:str,
root_path:str,
enable_env_ids:bool=False,
clone_in_fabric:bool=False,
)Replicates physics properties directly in omni.physics to avoid performance bottlenecks when parsing physics.
Parameters:

- source_prim_path (str) – Path of source object.

- prim_paths (List[str]) – List of destination paths.

- base_env_path (str) – Path to namespace for all environments.

- root_path (str) – Prefix path for each environment.

- useEnvIds (bool) – Whether to use envIDs functionality in physics to enable co-location of clones. Clones will be filtered automatically.

Raises:
Exception – Raises exception if base_env_path is None or root_path is None.

classGridCloner(
spacing:float,
num_per_row:int=-1,
stage:pxr.Usd.Stage=None,
)Bases: Cloner
This is a specialized Cloner class that will automatically generate clones in a grid fashion.
clone(
source_prim_path:str,
prim_paths:List[str],
position_offsets:ndarray=None,
orientation_offsets:ndarray=None,
replicate_physics:bool=False,
base_env_path:str=None,
root_path:str=None,
copy_from_source:bool=False,
enable_env_ids:bool=False,
clone_in_fabric:bool=False,
)Creates clones in a grid fashion. Positions of clones are computed automatically.
Parameters:

- source_prim_path (str) – Path of source object.

- prim_paths (List[str]) – List of destination paths.

- position_offsets (np.ndarray) – Positions to be applied as local translations on top of computed clone position. Defaults to None, no offset will be applied.

- orientation_offsets (np.ndarray) – Orientations to be applied as local rotations for each clone. Defaults to None, no offset will be applied.

- replicate_physics (bool) – Uses omni.physics replication. This will replicate physics properties directly for paths beginning with root_path and skip physics parsing for anything under the base_env_path.

- base_env_path (str) – Path to namespace for all environments. Required if replicate_physics=True and define_base_env() not called.

- root_path (str) – Prefix path for each environment. Required if replicate_physics=True and generate_paths() not called.

- copy_from_source – (bool): Setting this to False will inherit all clones from the source prim; any changes made to the source prim will be reflected in the clones. Setting this to True will make copies of the source prim when creating new clones; changes to the source prim will not be reflected in clones. Defaults to False. Note that setting this to True will take longer to execute.

- enable_env_ids (bool) – Setting this enables co-location of clones in physics with automatic filtering of collisions between clones.

Returns:
Computed positions of all clones.

Return type:
positions (List)

define_base_env(base_env_path:str)
Creates a USD Scope at base_env_path. This is designed to be the parent that holds all clones.
Parameters:
base_env_path (str) – Path to create the USD Scope at.

disable_change_listener()
enable_change_listener()
filter_collisions(
physicsscene_path:str,
collision_root_path:str,
prim_paths:List[str],
global_paths:List[str]=[],
)Filters collisions between clones. Clones will not collide with each other, but can collide with objects specified in global_paths.
Parameters:

- physicsscene_path (str) – Path to PhysicsScene object in stage.

- collision_root_path (str) – Path to place collision groups under.

- prim_paths (List[str]) – Paths of objects to filter out collision.

- global_paths (List[str]) – Paths of objects to generate collision (e.g. ground plane).

generate_paths(root_path:str, num_paths:int)
Generates a list of paths under the root path specified.
Parameters:

- root_path (str) – Base path where new paths will be created under.

- num_paths (int) – Number of paths to generate.

Returns:
A list of paths

Return type:
paths (List[str])

get_clone_transforms(
num_clones:int,
position_offsets:ndarray=None,
orientation_offsets:ndarray=None,
)Computes the positions and orientations of clones in a grid.
Parameters:

- num_clones (int) – Number of clones.

- position_offsets (np.ndarray | torch.Tensor) – Positions to be applied as local translations on top of computed clone position.

- position_offsets – Positions to be applied as local translations on top of computed clone position. Defaults to None, no offset will be applied.

- orientation_offsets (np.ndarray | torch.Tensor) – Orientations to be applied as local rotations for each clone. Defaults to None, no offset will be applied.

Returns:
Computed positions of all clones. orientations (List): Computed orientations of all clones.

Return type:
positions (List)

replicate_physics(
source_prim_path:str,
prim_paths:list,
base_env_path:str,
root_path:str,
enable_env_ids:bool=False,
clone_in_fabric:bool=False,
)Replicates physics properties directly in omni.physics to avoid performance bottlenecks when parsing physics.
Parameters:

- source_prim_path (str) – Path of source object.

- prim_paths (List[str]) – List of destination paths.

- base_env_path (str) – Path to namespace for all environments.

- root_path (str) – Prefix path for each environment.

- useEnvIds (bool) – Whether to use envIDs functionality in physics to enable co-location of clones. Clones will be filtered automatically.

Raises:
Exception – Raises exception if base_env_path is None or root_path is None.
