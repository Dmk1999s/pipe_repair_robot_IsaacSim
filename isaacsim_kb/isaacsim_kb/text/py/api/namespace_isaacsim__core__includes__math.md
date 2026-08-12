<!-- source: py/api/namespace_isaacsim__core__includes__math.html | title: math — Isaac Sim -->

# math
Fully qualified name: `isaacsim::core::includes::math`
namespacemath

## Functions
carb::Float3cross (const carb::Float3 &b, const carb::Float3 &c)
Computes the cross product of two 3D vectors.

floatdot (const carb::Float4 &v1, const carb::Float4 &v2)
Computes the dot product of two 4D vectors.

floatdot (const carb::Float3 &v1, const carb::Float3 &v2)
Computes the dot product of two 3D vectors.

carb::Float3getBasisVectorX (const carb::Float4 &q)
Gets the X basis vector from a rotation quaternion.

carb::Float3getBasisVectorY (const carb::Float4 &q)
Gets the Y basis vector from a rotation quaternion.

carb::Float3getBasisVectorZ (const carb::Float4 &q)
Gets the Z basis vector from a rotation quaternion.

carb::Float4inverse (const carb::Float4 &q)
Computes the inverse of a quaternion.

carb::Float3lerp (const carb::Float3 &start, const carb::Float3 &end, const float t)
Linearly interpolates between two 3D vectors.

carb::Float4lerp (const carb::Float4 &start, const carb::Float4 &end, const float t)
Linearly interpolates between two quaternions.

pxr::GfQuatflookAt (const pxr::GfVec3f &camera, const pxr::GfVec3f &target, const pxr::GfVec3f &up)
Computes a look-at quaternion rotation.

carb::Float3normalize (const carb::Float3 &q)
Normalizes a 3D vector to unit length.

carb::Float4normalize (const carb::Float4 &q)
Normalizes a quaternion to unit length.

carb::Float4operator* (const carb::Float4 &a, const carb::Float4 &b)
Performs quaternion multiplication.

carb::Float4operator* (const carb::Float4 &a, const float x)
Scales a 4D vector/quaternion by a scalar value.

carb::Float3operator* (const carb::Float3 &a, const float x)
Scales a 3D vector by a scalar value.

carb::Float4operator+ (const carb::Float4 &a, const carb::Float4 &b)
Adds two 4D vectors/quaternions.

carb::Float3operator+ (const carb::Float3 &a, const carb::Float3 &b)
Adds two 3D vectors.

carb::Float3operator- (const carb::Float3 &a, const carb::Float3 &b)
Subtracts two 3D vectors.

carb::Float4operator- (const carb::Float4 &a, const carb::Float4 &b)
Subtracts two 4D vectors/quaternions.

carb::Float3rotate (const carb::Float4 &q, const carb::Float3 x)
Rotates a vector by a quaternion.

doubleroundNearest (double input, double place)
Rounds a number to the nearest multiple of a given value.

carb::Float4slerp (const carb::Float4 &start, const carb::Float4 &end, const float t)
Performs spherical linear interpolation between quaternions.

pxr::GfTransformtransformInv (const pxr::GfTransform &a, const pxr::GfTransform &b)
Computes the local transform of b relative to transform a.
