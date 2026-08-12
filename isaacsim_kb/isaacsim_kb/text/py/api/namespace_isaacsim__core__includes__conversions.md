<!-- source: py/api/namespace_isaacsim__core__includes__conversions.html | title: conversions — Isaac Sim -->

# conversions
Fully qualified name: `isaacsim::core::includes::conversions`
namespaceconversions

## Functions
carb::Float3asCarbFloat3 (const pxr::GfVec3d &v)
Converts pxr::GfVec3d to carb::Float3.

carb::Float3asCarbFloat3 (const pxr::GfVec3f &v)
Converts pxr::GfVec3f to carb::Float3.

carb::Float4asCarbFloat4 (const pxr::GfQuatf &v)
Converts pxr::GfQuatf to carb::Float4.

carb::Float4asCarbFloat4 (const physx::PxQuat &q)
convert physx::PxQuat to carb::Float4

carb::Float4asCarbFloat4 (const pxr::GfQuatd &v)
Converts pxr::GfQuatd to carb::Float4.

pxr::GfQuatdasGfQuatd (const carb::Float4 &q)
Converts a carb::Float4 into a pxr::GfQuatd.

pxr::GfQuatfasGfQuatf (const carb::Float4 &q)
Converts a carb::Float4 into a pxr::GfQuatf.

pxr::GfRotationasGfRotation (const carb::Float4 &q)
Converts a carb::Float4 into a pxr::GfRotation.

pxr::GfTransformasGfTransform (const carb::Float3 &p, const carb::Float4 &r)
Converts position and rotation into a pxr::GfTransform.

pxr::GfVec3dasGfVec3d (const carb::Float3 &v)
Converts a carb::Float3 into a pxr::GfVec3d.

pxr::GfVec3fasGfVec3f (const carb::Float3 &v)
Converts a carb::Float3 into a pxr::GfVec3f.

inline ::physx::PxQuatasPxQuat (const usdrt::GfQuatf &v)
Converts usdrt::GfQuatf into PhysX quaternion.

inline ::physx::PxQuatasPxQuat (const pxr::GfQuatd &v)
Converts pxr::GfQuatd into PhysX quaternion.

inline ::physx::PxQuatasPxQuat (const usdrt::GfQuatd &v)
Converts usdrt::GfQuatd into PhysX quaternion.

inline ::physx::PxQuatasPxQuat (const pxr::GfQuatf &v)
Converts pxr::GfQuatf into PhysX quaternion.

inline ::physx::PxQuatasPxQuat (const carb::Float4 &q)
Converts carb::Float4 into PhysX quaternion.

inline ::physx::PxTransformasPxTransform (const pxr::GfTransform &trans)
Converts USD transform into PhysX transform.

inline ::physx::PxTransformasPxTransform (const usdrt::GfVec3d &translation, const usdrt::GfQuatd &orientation)
Converts USD runtime translation and orientation into PhysX transform.

inline ::physx::PxTransformasPxTransform (const usdrt::GfMatrix4d &mat)
Converts USD runtime matrix into PhysX transform.

inline ::physx::PxVec3asPxVec3 (const pxr::GfVec3d &v)
Converts pxr::GfVec3d into PhysX vector.

inline ::physx::PxVec3asPxVec3 (const carb::Float3 &v)
Converts carb::Float3 into PhysX vector.

inline ::physx::PxVec3asPxVec3 (const usdrt::GfVec3d &v)
Converts usdrt::GfVec3d into PhysX vector.

inline ::physx::PxVec3asPxVec3 (const pxr::GfVec3f &v)
Converts pxr::GfVec3f into PhysX vector.

inline ::physx::PxVec3asPxVec3 (const usdrt::GfVec3f &v)
Converts usdrt::GfVec3f into PhysX vector.
