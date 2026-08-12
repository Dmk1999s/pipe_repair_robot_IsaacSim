<!-- source: py/api/structisaacsim_1_1asset_1_1gen_1_1omap_1_1_occupancy_map.html | title: OccupancyMap — Isaac Sim -->

# OccupancyMap
Fully qualified name: `isaacsim::asset::gen::omap::OccupancyMap`
structOccupancyMap

Interface for occupancy map generation.
This interface provides functionality for generating and managing occupancy maps. Occupancy maps represent spatial information about the environment as a grid of cells, where each cell indicates whether the corresponding space is occupied, free, or unknown.
Note
The interface is designed to work with both 2D and 3D occupancy maps
Public Members
void(*generateMap)()

Generates the occupancy map.
Initializes and creates an occupancy map based on the current scene. This should be called after setting the transform and cell size parameters.
Pre:
Transform and cell size must be set before calling this function

Post:
A new occupancy map will be generated and stored in memory

void(*update)()

Updates the visualization.
Refreshes the visual representation of the occupancy map. This includes drawing the bounding box, grid, and coordinate axes.
Note
This should be called whenever the map or visualization settings change

void(*setTransform)(carb::Float3inputOrigin,carb::Float3minPoint,carb::Float3maxPoint)

Sets the transform for map generation.
Defines the origin and boundaries for the occupancy map in world coordinates.
Param inputOrigin:
[in] Origin point in world coordinates, serves as the reference point

Param minPoint:
[in] Minimum bounds relative to origin, defines the lower corner of the map volume

Param maxPoint:
[in] Maximum bounds relative to origin, defines the upper corner of the map volume

Pre:
minPoint components should be less than maxPoint components

void(*setCellSize)(floatcellSize)

Sets the cell size for the map.
Configures the resolution of the occupancy map by setting the size of each cell.
Note
Smaller cell sizes will result in higher resolution maps but require more memory
Param cellSize:
[in] Size of each cell in meters

Pre:
cellSize must be positive

std ::vector<carb::Float3>(*getOccupiedPositions)()

Gets positions of occupied cells.
Retrieves the world positions of all cells that are marked as occupied.
Return:
Vector of 3D positions representing the centers of occupied cells

std ::vector<carb::Float3>(*getFreePositions)()

Gets positions of free cells.
Retrieves the world positions of all cells that are marked as free (unoccupied).
Return:
Vector of 3D positions representing the centers of free cells

carb::Float3(*getMinBound)()

Gets minimum bounds of the map.
Retrieves the minimum coordinate values of the occupancy map’s bounding box.
Return:
Minimum bounds as Float3 in world coordinates

carb::Float3(*getMaxBound)()

Gets maximum bounds of the map.
Retrieves the maximum coordinate values of the occupancy map’s bounding box.
Return:
Maximum bounds as Float3 in world coordinates

carb::Int3(*getDimensions)()

Gets dimensions of the map in cells.
Retrieves the number of cells along each axis of the occupancy map.
Return:
Dimensions as Int3, where each component represents the number of cells along that axis

std ::vector<float>(*getBuffer)()

Gets the occupancy buffer.
Retrieves the raw occupancy values for all cells in the map.
Return:
Vector of cell values, where each value indicates the occupancy state (typically 1.0 for occupied, 0.0 for free, and 0.5 for unknown)

std ::vector<char>(*getColoredByteBuffer)(constcarb::Int4&occupied,constcarb::Int4&unoccupied,constcarb::Int4&unknown)

Gets colored byte buffer for visualization.
Generates a buffer of RGBA color values for visualization purposes. Each cell in the occupancy map is assigned a color based on its state.
Param occupied:
[in] Color for occupied cells as RGBA integers (0-255)

Param unoccupied:
[in] Color for unoccupied cells as RGBA integers (0-255)

Param unknown:
[in] Color for unknown cells as RGBA integers (0-255)

Return:
Vector of char values representing RGBA colors for each cell in the map
