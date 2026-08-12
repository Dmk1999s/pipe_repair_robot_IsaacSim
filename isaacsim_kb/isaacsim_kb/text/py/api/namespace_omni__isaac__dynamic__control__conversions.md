<!-- source: py/api/namespace_omni__isaac__dynamic__control__conversions.html | title: conversions — Isaac Sim -->

# conversions
Fully qualified name: `omni::isaac::dynamic_control::conversions`
namespaceconversions

## Functions
omni::isaac::dynamic_control::DcTransformasDcTransform (const pxr::GfVec3f &p, const pxr::GfQuatf &q)
Converts USD position and orientation into Dynamic Control transform.

omni::isaac::dynamic_control::DcTransformasDcTransform (const pxr::GfVec3d &p, const pxr::GfQuatd &q)
Converts USD double precision position and orientation into Dynamic Control transform.

pxr::GfMatrix4dasGfMatrix4d (const omni::isaac::dynamic_control::DcTransform &input)
Converts a DcTransform to a GfMatrix4d.

pxr::GfMatrix4fasGfMatrix4f (const omni::isaac::dynamic_control::DcTransform &input)
Converts a DcTransform to a GfMatrix4f.

pxr::GfMatrix4fasGfMatrix4fT (const omni::isaac::dynamic_control::DcTransform &input)
Converts a DcTransform to a transposed GfMatrix4f.

pxr::GfQuatdasGfQuatd (const carb::Float4 &q)
Converts a carb::Float4 into a pxr::GfQuatd.

pxr::GfQuatfasGfQuatf (const carb::Float4 &q)
Converts a carb::Float4 into a pxr::GfQuatf.

pxr::GfRotationasGfRotation (const carb::Float4 &q)
Converts a carb::Float4 into a pxr::GfRotation.

pxr::GfTransformasGfTransform (const omni::isaac::dynamic_control::DcTransform &pose)
Converts a DcTransform into a pxr::GfTransform.

pxr::GfVec3dasGfVec3d (const carb::Float3 &v)
Converts a carb::Float3 into a pxr::GfVec3d.

pxr::GfVec3fasGfVec3f (const carb::Float3 &v)
Converts a carb::Float3 into a pxr::GfVec3f.

inline ::physx::PxTransformasPxTransform (const omni::isaac::dynamic_control::DcTransform &pose)
Converts DcTransform into PhysX transform.
