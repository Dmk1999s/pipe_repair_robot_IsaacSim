<!-- source: py/api/classisaacsim_1_1asset_1_1gen_1_1omap_1_1_map_generator.html | title: MapGenerator — Isaac Sim -->

# MapGenerator
Fully qualified name: `isaacsim::asset::gen::omap::MapGenerator`
classMapGenerator

Generator class for creating 2D and 3D occupancy maps from USD stages.
The MapGenerator class provides functionality to generate occupancy maps from USD stage data. It supports both 2D and 3D map generation with configurable cell sizes and occupancy values. The generator uses PhysX for collision detection and octomap for spatial representation.
Occupancy maps are useful for robotic applications like motion planning, navigation, and spatial reasoning about environments. The maps represent space as either occupied, free, or unknown, which allows algorithms to make decisions about valid paths and actions.
Note
This class requires valid PhysX and USD stage pointers to function properly
Warning
Memory usage increases with smaller cell sizes and larger map volumes
Public Functions
MapGenerator(omni ::physx ::IPhysx*physx, pxr ::UsdStageWeakPtrstage)

Constructs a new MapGenerator instance.
Initializes the generator with PhysX interface and USD stage references. The PhysX interface is used for collision detection, and the USD stage provides the geometry of the environment to be mapped.
Parameters:

- physx – [in] Pointer to the PhysX interface for collision detection

- stage – [in] Pointer to the USD stage containing the scene geometry

Throws:
std ::runtime_error – If the PhysX scene cannot be created or accessed

Pre:
physx pointer must be valid and initialized

Pre:
stage must be a valid USD stage

~MapGenerator()

Destructor for MapGenerator .
Cleans up resources used by the generator, including the octomap tree.

voidupdateSettings(
floatcellSize,
floatoccupiedValue,
floatunoccupiedValue,
floatunknownValue,
)
Updates the generator’s occupancy map settings.
Configures the cell size and values used for different occupancy states. These values determine the map resolution and how different cell states are represented numerically in the occupancy buffer.
Note
Smaller cell sizes provide higher resolution but require more memory and computation time
Parameters:

- cellSize – [in] Size of each occupancy grid cell in meters

- occupiedValue – [in] Numerical value assigned to occupied cells (default: 1.0)

- unoccupiedValue – [in] Numerical value assigned to unoccupied cells (default: 0.0)

- unknownValue – [in] Numerical value assigned to cells with unknown occupancy (default: 0.5)

Pre:
cellSize must be positive

voidsetTransform(
carb::Float3inputOrigin,
carb::Float3minPoint,
carb::Float3maxPoint,
)
Sets the transformation parameters for map generation.
Defines the origin and bounds of the area to be mapped. The occupancy map will be generated within the volume defined by these parameters.
Note
The volume defined should encompass the relevant parts of the scene to be mapped
Parameters:

- inputOrigin – [in] Origin point in world coordinates

- minPoint – [in] Minimum bounds relative to origin, defining the lower corner of the map volume

- maxPoint – [in] Maximum bounds relative to origin, defining the upper corner of the map volume

Pre:
minPoint components must be less than maxPoint components

voidgenerate2d()

Generates a 2D occupancy map.
Creates a 2D projection of the scene’s occupancy by collapsing the 3D space onto a horizontal plane. This is useful for applications like 2D navigation or floor plan generation.
Note
This method is more efficient than generate3d() but provides less spatial information
Post:
The internal occupancy data structures will be populated with 2D occupancy information

voidgenerate3d()

Generates a 3D occupancy map.
Creates a full 3D volumetric representation of the scene’s occupancy. This provides complete spatial information about the environment, useful for 3D path planning and spatial reasoning.
Note
This method requires more memory and computation than generate2d()
Post:
The internal occupancy data structures will be populated with 3D occupancy information

std ::vector<carb::Float3>getOccupiedPositions()

Retrieves positions of all occupied cells.
Gets the world coordinates of all cells that are marked as occupied in the current occupancy map.
Note
The returned positions are in world coordinates
Returns:
Vector of 3D positions representing the centers of occupied cells

std ::vector<carb::Float3>getFreePositions()

Retrieves positions of all free (unoccupied) cells.
Gets the world coordinates of all cells that are marked as free (unoccupied) in the current occupancy map.
Note
The returned positions are in world coordinates
Warning
For large maps with small cell sizes, this vector can be very large
Returns:
Vector of 3D positions representing the centers of free cells

carb::Float3getMinBound()

Gets the minimum boundary point of the map.
Retrieves the minimum coordinate values of the occupancy map’s bounding box in world coordinates.
Returns:
Minimum boundary coordinates as Float3

carb::Float3getMaxBound()

Gets the maximum boundary point of the map.
Retrieves the maximum coordinate values of the occupancy map’s bounding box in world coordinates.
Returns:
Maximum boundary coordinates as Float3

carb::Int3getDimensions()

Gets the dimensions of the map in cell units.
Retrieves the number of cells along each axis of the occupancy map. This represents the resolution of the map in each dimension.
Returns:
Number of cells in each dimension as Int3

std ::vector<float>getBuffer()

Retrieves the raw occupancy buffer.
Gets the raw occupancy values for all cells in the map. The values correspond to the occupancy state of each cell, as configured in updateSettings() .
Note
The buffer is stored in row-major order (x, then y, then z)
Returns:
Vector of occupancy values for all cells

std ::vector<char>getColoredByteBuffer(
constcarb::Int4&occupied,
constcarb::Int4&unoccupied,
constcarb::Int4&unknown,
)
Generates a colored visualization buffer.
Creates an RGBA buffer for visualization purposes, where each cell is colored according to its occupancy state (occupied, unoccupied, or unknown).
Note
The buffer is stored in row-major order (x, then y, then z) with 4 bytes per cell (RGBA)
Parameters:

- occupied – [in] Color for occupied cells (RGBA)

- unoccupied – [in] Color for unoccupied cells (RGBA)

- unknown – [in] Color for unknown cells (RGBA)

Returns:
Vector of bytes representing RGBA values for each cell
