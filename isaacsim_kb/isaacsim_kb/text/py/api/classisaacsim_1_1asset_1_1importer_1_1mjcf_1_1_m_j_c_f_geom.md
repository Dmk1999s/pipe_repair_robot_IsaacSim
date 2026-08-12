<!-- source: py/api/classisaacsim_1_1asset_1_1importer_1_1mjcf_1_1_m_j_c_f_geom.html | title: MJCFGeom — Isaac Sim -->

# MJCFGeom
Fully qualified name: `isaacsim::asset::importer::mjcf::MJCFGeom`
classMJCFGeom:publicisaacsim ::asset ::importer ::mjcf ::MJCFVisualElement

Geometry element for collision detection and physics simulation.
Extends MJCFVisualElement with physical properties needed for collision detection and contact dynamics. Contains material properties, contact parameters, friction coefficients, and spatial positioning information.
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

Public Functions
inlineMJCFGeom()

Public Members
floatdensity

Mass density of the geometry material.

intconaffinity

Contact affinity bitmask for collision filtering.

intcondim

Number of contact dimensions (1-6).

intcontype

Contact type bitmask for collision filtering.

floatmargin

Contact margin for collision detection.

Vec3 friction

Friction coefficients [sliding, torsional, rolling].

Vec3 solimp

Constraint solver impedance parameters.

Vec2 solref

Constraint solver reference parameters.

Vec3 from

Start point for geometry shapes defined by two points.

Vec3 to

End point for geometry shapes defined by two points.

Vec3 pos

Position offset in the parent body frame.

Quat quat

Quaternion orientation relative to parent body.

Vec4 axisangle

Axis-angle representation of orientation.

Vec3 zaxis

Z-axis direction for orientation specification.

std ::stringmesh

Name of the mesh file for mesh geometry types.

boolhasFromTo

Whether the geometry is defined by from-to points.

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
