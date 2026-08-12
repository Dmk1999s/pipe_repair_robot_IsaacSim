<!-- source: py/source/extensions/isaacsim.asset.gen.omap/docs/index.html | title: [isaacsim.asset.gen.omap] Isaac Sim Occupancy Map — Isaac Sim -->

# [isaacsim.asset.gen.omap] Isaac Sim Occupancy Map
Version: 2.0.29
The Isaac Sim Occupancy Map extension provides tools to generate occupancy maps for a Scene
[image: Preview]

## Enable Extension
The extension can be enabled (if not already) in one of the following ways:

## API

### Python API

[TABLE]
Generator | Generator for creating occupancy maps from USD stages.
[/TABLE]

classGenerator
Bases: `pybind11_object`
Generator for creating occupancy maps from USD stages.
This class is used to generate an occupancy map for a USD stage. Assuming the stage has collision geometry information, it can produce 2D or 3D representations of the environment’s occupied and free space.
None
Example

```
>>> import omni
>>> from isaacsim.asset.gen.omap.bindings import _omap
>>>
>>> physx = omni.physx.get_physx_interface()
>>> stage_id = omni.usd.get_context().get_stage_id()
>>>
>>> generator = _omap.Generator(physx, stage_id)
>>> # 0.05m cell size, output buffer will have 4 for occupied cells,
>>> # 5 for unoccupied, and 6 for cells that cannot be seen
>>> # this assumes your usd stage units are in m, and not cm
>>> generator.update_settings(.05, 4, 5, 6)
>>> # Set location to map from and the min and max bounds to map to
>>> generator.set_transform((0, 0, 0), (-2, -2, 0), (2, 2, 0))
>>> generator.generate2d()
>>> # Get locations of the occupied cells in the stage
>>> points = generator.get_occupied_positions()
>>> # Get computed 2d occupancy buffer
>>> buffer = generator.get_buffer()
>>> # Get dimensions for 2d buffer
>>> dims = generator.get_dimensions()
```
__init__(
self:isaacsim.asset.gen.omap.bindings._omap.Generator,
arg0:omni::physx::IPhysx,
arg1:int,
)→None Initialize a new Generator instance.
Parameters:

- physx_ptr – Pointer to PhysX interface used for collision detection.

- stage_id – Stage ID for the USD stage to map.

Returns:
A new Generator instance.

generate2d(
self:isaacsim.asset.gen.omap.bindings._omap.Generator ,
)→None Generate a 2D occupancy map.
Generates a map based on the settings and transform set. Assumes that a 2D map is generated and flattens the computed data.
Parameters:
None

Returns:
None

generate3d(
self:isaacsim.asset.gen.omap.bindings._omap.Generator ,
)→None Generate a 3D occupancy map.
Generates a map based on the settings and transform set. Creates a full 3D volumetric representation of the scene’s occupancy.
Parameters:
None

Returns:
None

get_buffer(
self:isaacsim.asset.gen.omap.bindings._omap.Generator ,
)→List[float]Get the raw occupancy buffer.
Returns:
2D array containing values for each cell in the occupancy map.
Values correspond to the occupancy state of each cell (occupied, unoccupied, or unknown) as configured in update_settings().

Return type:
list

get_colored_byte_buffer(
self:isaacsim.asset.gen.omap.bindings._omap.Generator,
arg0:carb::Int4,
arg1:carb::Int4,
arg2:carb::Int4,
)→List[str]Generate a colored visualization buffer.
Creates an RGBA buffer for visualization purposes, where each cell is colored according to its occupancy state.
Parameters:

- occupied_color (tuple) – RGBA Value used to denote an occupied cell.

- unoccupied_color (tuple) – RGBA Value used to denote an unoccupied cell.

- unknown_color (tuple) – RGBA Value used to denote unknown areas that could not be reached.

Returns:
Flattened buffer containing list of RGBA values for each pixel.
Can be used to render as image directly.

Return type:
list

get_dimensions(
self:isaacsim.asset.gen.omap.bindings._omap.Generator ,
)→carb::Int3Get the dimensions of the map in cell units.
Returns:
Dimensions for output buffer (width, height, depth).

Return type:
tuple

get_free_positions(
self:isaacsim.asset.gen.omap.bindings._omap.Generator ,
)→List[carb::Float3]Get positions of all free (unoccupied) cells.
Returns:
List of 3D points in stage coordinates from the generated map,
containing free locations.

Return type:
list

get_max_bound(
self:isaacsim.asset.gen.omap.bindings._omap.Generator ,
)→carb::Float3Get the maximum boundary point of the map.
Returns:
Maximum bound for generated occupancy map in stage coordinates.

Return type:
tuple

get_min_bound(
self:isaacsim.asset.gen.omap.bindings._omap.Generator ,
)→carb::Float3Get the minimum boundary point of the map.
Returns:
Minimum bound for generated occupancy map in stage coordinates.

Return type:
tuple

get_occupied_positions(
self:isaacsim.asset.gen.omap.bindings._omap.Generator ,
)→List[carb::Float3]Get positions of all occupied cells.
Returns:
List of 3D points in stage coordinates from the generated map,
containing occupied locations.

Return type:
list

set_transform(
self:isaacsim.asset.gen.omap.bindings._omap.Generator,
arg0:carb::Float3,
arg1:carb::Float3,
arg2:carb::Float3,
)→None Set origin and bounds for mapping.
Parameters:

- origin (tuple of float) – Origin in stage to start mapping from, must be in unoccupied space.

- min_bound (tuple of float) – Minimum bound to map up to.

- max_bound (tuple of float) – Maximum bound to map up to.

Returns:
None

update_settings(
self:isaacsim.asset.gen.omap.bindings._omap.Generator ,
arg0:float,
arg1:float,
arg2:float,
arg3:float,
)→None Update the settings used for generating the occupancy map.
Parameters:

- cell_size (float) – Size of the cell in stage units, resolution of the grid.

- occupied_value (float) – Value used to denote an occupied cell.

- unoccupied_value (float) – Value used to denote an unoccupied cell.

- unknown_value (float) – Value used to denote unknown areas that could not be reached from the starting location.

Returns:
None
