<!-- source: py/api/classisaacsim_1_1asset_1_1importer_1_1mjcf_1_1_m_j_c_f_site.html | title: MJCFSite — Isaac Sim -->

# MJCFSite
Fully qualified name: `isaacsim::asset::importer::mjcf::MJCFSite`
classMJCFSite:publicisaacsim ::asset ::importer ::mjcf ::MJCFVisualElement

Site element for marking specific locations and orientations in the model.
Sites are special objects that mark locations and orientations but do not participate in collisions or dynamics. They are commonly used for sensors, cameras, or as attachment points for other elements.
Public Types
enumType

Enumeration of geometric shape types for site visualization.
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

Public Functions
inlineMJCFSite()

Public Members
intgroup

Group identifier for site organization.

Vec3 friction

Friction coefficients for the site.

Vec3 from

Start point for sites defined by two points.

Vec3 to

End point for sites defined by two points.

boolhasFromTo

Whether the site is defined by from-to points.

Vec3 pos

Position offset in the parent body frame.

Quat quat

Quaternion orientation relative to parent body.

Vec3 zaxis

Z-axis direction for orientation specification.

boolhasGeom

Whether the site has associated geometry for visualization.

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
