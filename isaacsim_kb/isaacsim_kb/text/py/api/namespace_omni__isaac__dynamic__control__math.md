<!-- source: py/api/namespace_omni__isaac__dynamic__control__math.html | title: math — Isaac Sim -->

# math
Fully qualified name: `omni::isaac::dynamic_control::math`
namespacemath

## Functions
omni::isaac::dynamic_control::DcTransforminverse (const omni::isaac::dynamic_control::DcTransform &transform)
Computes the inverse of a transform.

omni::isaac::dynamic_control::DcTransformlerp (const omni::isaac::dynamic_control::DcTransform &a, const omni::isaac::dynamic_control::DcTransform &b, const float t)
Linearly interpolates between two transforms.

omni::isaac::dynamic_control::DcTransformoperator* (const omni::isaac::dynamic_control::DcTransform &self, const omni::isaac::dynamic_control::DcTransform &other)
Multiplies two transforms to compose them.

omni::isaac::dynamic_control::DcTransformslerp (const omni::isaac::dynamic_control::DcTransform &a, const omni::isaac::dynamic_control::DcTransform &b, const float t)
Performs spherical linear interpolation between transforms.

omni::isaac::dynamic_control::DcTransformtransformInv (const omni::isaac::dynamic_control::DcTransform &a, const omni::isaac::dynamic_control::DcTransform &b)
Computes the relative transform from a to b.
