<!-- source: py/api/struct_transform.html | title: Transform — Isaac Sim -->

# Transform
structTransform

3D transformation represented by position and rotation.
This structure represents a 3D transformation consisting of a position (translation) and rotation (quaternion). It provides composition operations through multiplication and is commonly used for object positioning and coordinate space transformations.
Public Functions
inlineTransform()

Default constructor creating identity transform.
Creates a transform with zero translation and identity rotation (no rotation).

inlineTransform(constVec3 &v, constQuat &q=Quat ())

Constructor with position and optional rotation.
Parameters:

- v – [in] Position vector

- q – [in]Rotation quaternion (default: identity rotation)

inlineTransform operator*(constTransform &rhs)const

Transform composition operator.
Composes two transforms such that the result represents applying this transform followed by the rhs transform.
Parameters:
rhs – [in] The transform to compose with this transform

Returns:
The composed transform

Public Members
Vec3 p

Position (translation) component.

Quat q

Rotation component as a quaternion.
