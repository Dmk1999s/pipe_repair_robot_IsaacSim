<!-- source: py/api/structisaacsim_1_1asset_1_1importer_1_1urdf_1_1_urdf_color.html | title: UrdfColor — Isaac Sim -->

# UrdfColor
Fully qualified name: `isaacsim::asset::importer::urdf::UrdfColor`
structUrdfColor

RGBA color specification for URDF materials.
Represents color values for visual elements. By default, a UrdfColor struct has invalid color values (negative red component) unless it was explicitly defined in the XML.
Public Members
floatr=-1.0f

Red color component (0.0 to 1.0, or -1.0 if undefined).

floatg=-1.0f

Green color component (0.0 to 1.0, or -1.0 if undefined).

floatb=-1.0f

Blue color component (0.0 to 1.0, or -1.0 if undefined).

floata=1.0f

Alpha (transparency) component (0.0 to 1.0).
