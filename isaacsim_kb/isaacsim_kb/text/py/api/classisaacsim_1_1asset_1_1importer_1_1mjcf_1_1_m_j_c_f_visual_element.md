<!-- source: py/api/classisaacsim_1_1asset_1_1importer_1_1mjcf_1_1_m_j_c_f_visual_element.html | title: MJCFVisualElement — Isaac Sim -->

# MJCFVisualElement
Fully qualified name: `isaacsim::asset::importer::mjcf::MJCFVisualElement`
classMJCFVisualElement

Base class for visual elements in MJCF models.
Represents a geometric shape that can be rendered visually in the simulation. Contains basic properties like name, material, color, size, and shape type that are common to all visual geometry elements.
Subclassed by isaacsim::asset::importer::mjcf::MJCFGeom , isaacsim::asset::importer::mjcf::MJCFSite
Public Types
enumType

Enumeration of geometric shape types for visual elements.
Values:
enumeratorCAPSULE

Capsule shape (cylinder with hemispherical caps).

enumeratorSPHERE

Sphere shape.

enumeratorELLIPSOID

Ellipsoid shape.

enumeratorCYLINDER

Cylinder shape.

enumeratorBOX

Box (rectangular cuboid) shape.

enumeratorMESH

Mesh shape loaded from file.

enumeratorPLANE

Infinite plane shape.

enumeratorOTHER

Other or unspecified shape type.

Public Members
std ::stringname

Name identifier for the visual element.

std ::stringmaterial

Name of the material applied to this element.

Vec4 rgba

RGBA color values [red, green, blue, alpha].

Vec3 size

Size dimensions of the geometric shape.

Type type

Type of geometric shape for this visual element.
