<!-- source: py/api/structisaacsim_1_1asset_1_1importer_1_1urdf_1_1_urdf_geometry.html | title: UrdfGeometry — Isaac Sim -->

# UrdfGeometry
Fully qualified name: `isaacsim::asset::importer::urdf::UrdfGeometry`
structUrdfGeometry

Geometric shape definition for URDF visual and collision elements.
Represents various geometric primitives and mesh assets that can be used for visual rendering and collision detection. Supports boxes, cylinders, capsules, spheres, and mesh files with scaling parameters.
Public Members
UrdfGeometryType type

Type of geometric shape.

floatsize_x=0.0f

Box size in x-direction.

floatsize_y=0.0f

Box size in y-direction.

floatsize_z=0.0f

Box size in z-direction.

floatradius=0.0f

Radius for cylindrical and spherical shapes.

floatlength=0.0f

Length for cylindrical shapes.

floatscale_x=1.0f

Scale factor in x-direction for mesh geometry.

floatscale_y=1.0f

Scale factor in y-direction for mesh geometry.

floatscale_z=1.0f

Scale factor in z-direction for mesh geometry.

std ::stringmeshFilePath

File path to mesh asset.
