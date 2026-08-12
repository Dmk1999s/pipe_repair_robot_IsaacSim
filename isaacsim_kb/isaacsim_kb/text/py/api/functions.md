<!-- source: py/api/functions.html | title: Functions — Isaac Sim -->

# Functions
floatACos (float theta)
Computes the arc cosine (inverse cosine) of a value.

floatASin (float theta)
Computes the arc sine (inverse sine) of a value.

floatATan (float theta)
Computes the arc tangent (inverse tangent) of a value.

floatATan2 (float x, float y)
Computes the arc tangent of y/x using the signs to determine quadrant.

floatAbs (float x)
Computes the absolute value of a float.

Matrix22Add (const Matrix22 &a, const Matrix22 &b)
Adds two 2x2 matrices element-wise.

Matrix33Add (const Matrix33 &a, const Matrix33 &b)
Adds two matrices element-wise.

XMatrix44< T >AffineInverse (const XMatrix44< T > &m)
RotationAlignToVector (const Vec3 &vector)
Vec2AngleToVector (float a)
voidBasisFromVector (const Vec3 &w, Vec3 *u, Vec3 *v)
ColourBourkeColorMap (float low, float high, float v)
TClamp (T a, T low, T high)
Clamps a value between a minimum and maximum range.

floatClosestPointBetweenLineSegmentAndTri (const Vec3 &p, const Vec3 &q, const Vec3 &a, const Vec3 &b, const Vec3 &c, float &outT, float &outV, float &outW)
voidClosestPointBetweenLineSegments (const Vec3 &p, const Vec3 &q, const Vec3 &r, const Vec3 &s, float &u, float &v)
Vec3ClosestPointOnFatTriangle (const Vec3 &a, const Vec3 &b, const Vec3 &c, const Vec3 &p, const float thickness, float &v, float &w)
Vec3ClosestPointOnTriangle (const Vec3 &a, const Vec3 &b, const Vec3 &c, const Vec3 &p, float &v, float &w)
Vec3ClosestPointToAABB (const Vec3 &p, const Vec3 &lower, const Vec3 &upper)
uint32_tColourToRGBA8 (const Colour &c)
floatCos (float theta)
Computes the cosine of an angle.

Vec3CosineSampleHemisphere ()
Mesh *CreateCapsule (int slices, int segments, float radius=1.0f, float halfHeight=1.0f)
Creates a capsule mesh primitive.

Mesh *CreateCubeMesh ()
Creates a cube mesh primitive.

Mesh *CreateCylinder (int slices, float radius, float halfHeight, bool cap=false)
Creates a cylinder mesh primitive.

Mesh *CreateDiscMesh (float radius, uint32_t segments)
Creates a circular disc mesh.

Mesh *CreateEllipsoid (int slices, int segments, Vec3 radiis)
Creates an ellipsoid mesh primitive.

Mesh *CreateQuadMesh (float sizex, float sizez, int gridx, int gridz)
Creates a subdivided quad mesh.

Mesh *CreateSphere (int slices, int segments, float radius=1.0f)
Creates a sphere mesh primitive.

Mesh *CreateTetrahedron (float ground=0.0f, float height=1.0f)
Creates a tetrahedron mesh primitive.

Mesh *CreateTriMesh (float size, float y=0.0f)
Creates a triangular mesh primitive.

TCross (const XVector2< T > &a, const XVector2< T > &b)
Computes the 2D cross product of two vectors.

Vec3Cross (const Vec3 &b, const Vec3 &c)
Computes the cross product of two 3D vectors.

TCube (T x)
Computes the cube of a value.

floatDegToRad (float t)
Converts degrees to radians.

floatDeterminant (const Matrix22 &m)
Calculates the determinant of a 2x2 matrix.

floatDeterminant (const Matrix33 &m)
Computes the determinant of a 3x3 matrix.

TDeterminant (const XMatrix< n, n, T > &A, XMatrix< n, n, T > &L, XMatrix< n, n, T > &U)
Matrix33Diagonalize (const Vec3 &v)
Creates a diagonal matrix from a 3D vector.

Vec3DifferentiateQuat (const Quat &q1, const Quat &q0, float invdt)
T::value_typeDistance (const T &v1, const T &v2)
Computes the distance between two vectors.

floatDot (const Plane &p, const Point3 &v)
floatDot (const Plane &p, const Vector3 &v)
floatDot (const Vector3 &v, const Plane &p)
TDot (const XVector4< T > &v1, const XVector4< T > &v2)
floatDot (const Quat &a, const Quat &b)
TDot (const XVector2< T > &v1, const XVector2< T > &v2)
Computes the dot product of two vectors.

TDot (const XVector3< T > &v1, const XVector3< T > &v2)
Computes the dot product of two 3D vectors.

T::value_typeDot3 (const T &v1, const T &v2)
Computes the dot product of two vectors with value_type return.

floatDot3 (const float *v1, const float *v2)
Computes the dot product of two float arrays representing 3D vectors.

voidEulerFromQuatZYX (const Quat &q, float &rotx, float &roty, float &rotz)
voidExportMeshToBin (const char *path, const Mesh *m)
Exports a mesh to binary format.

voidExtractFrustumPlanes (const Matrix44 &m, Plane *planes)
boolFileMove (const char *src, const char *dest)
boolFileScan (const char *pattern, std::vector< std::string > &files)
TFrobeniusNorm (const XMatrix< m, n, T > &A)
Vec3GetBasisVector0 (const Quat &q)
Vec3GetBasisVector1 (const Quat &q)
Vec3GetBasisVector2 (const Quat &q)
boolGetCmdLineArg (const char *arg, T &out, int argc, const char *const argv[])
std::stringGetExePath ()
std::stringGetFilePathByPlatform (const char *path)
QuatGetRotationQuat (const Vec3 &_u, const Vec3 &_v)
doubleGetSeconds ()
std::stringGetWorkingDirectory ()
PXR_NAMESPACE_OPEN_SCOPE boolGfIsClose(const pxr::GfQuatd &val1, const pxr::GfQuatd &val2, double tolerance)
ColourHSVToRGB (float h, float s, float v)
THermiteInterpolate (const T &a, const T &b, const T &t1, const T &t2, float t)
THermiteSecondDerivative (const T &a, const T &b, const T &t1, const T &t2, float t)
THermiteTangent (const T &a, const T &b, const T &t1, const T &t2, float t)
QuatIntegrateQuat (const Vec3 &omega, const Quat &q0, float dt)
boolIntersectLineSegmentPlane (const Vec3 &start, const Vec3 &end, const Plane &plane, Vec3 &out)
boolIntersectLineTri (const Vec3 &p, const Vec3 &q, const Vec3 &a, const Vec3 &b, const Vec3 &c)
boolIntersectPlaneAABB (const Vec4 &plane, const Vec3 &center, const Vec3 &extents)
boolIntersectRayAABB (const Vec3 &start, const Vector3 &dir, const Vector3 &min, const Vector3 &max, float &t, Vector3 *normal)
boolIntersectRayAABBFast (const Vec3 &pos, const Vector3 &rcp_dir, const Vector3 &min, const Vector3 &max, float &t)
boolIntersectRayFatTriangle (const Vec3 &p, const Vec3 &dir, const Vec3 &a, const Vec3 &b, const Vec3 &c, float thickness, float threshold, float maxT, float &t, float &u, float &v, float &w, Vec3 *normal)
boolIntersectRayPlane (const Point3 &p, const Vector3 &dir, const Plane &plane, float &t)
boolIntersectRaySphere (const Point3 &sphereOrigin, float sphereRadius, const Point3 &rayOrigin, const Vec3 &rayDir, float &t, Vec3 *hitNormal=nullptr)
boolIntersectRaySphere (const Point3 &sphereOrigin, float sphereRadius, const Point3 &rayOrigin, const Vector3 &rayDir, float &minT, float &maxT, Vec3 *hitNormal=nullptr)
boolIntersectRayTri (const Point3 &p, const Vec3 &dir, const Point3 &a, const Point3 &b, const Point3 &c, float &t, float &u, float &v, float &w, Vec3 *normal)
boolIntersectRayTriTwoSided (const Vec3 &p, const Vec3 &dir, const Vec3 &a, const Vec3 &b, const Vec3 &c, float &t, float &u, float &v, float &w, float &sign, Vec3 *normal)
boolIntersectSegmentTri (const Vec3 &p, const Vec3 &q, const Vec3 &a, const Vec3 &b, const Vec3 &c, float &t, float &u, float &v, float &w, Vec3 *normal)
BoundsIntersection (const Bounds &a, const Bounds &b)
floatInvSqrt (float x)
Computes the inverse square root of a value.

Matrix22Inverse (const Matrix22 &m, float &det)
Computes the inverse of a 2x2 matrix.

Matrix33Inverse (const Matrix33 &a, bool &success)
Computes the inverse of a 3x3 matrix using single precision.

TransformInverse (const Transform &transform)
XMatrix< n, n, T >Inverse (const XMatrix< n, n, T > &A, T &det)
QuatInverse (const Quat &q)
Matrix33InverseDouble (const Matrix33 &a, bool &success)
Computes the inverse of a 3x3 matrix using double precision.

Vec3InverseTransformPoint (const Transform &t, const Vec3 &v)
Vec3InverseTransformVector (const Transform &t, const Vec3 &v)
ColourJetColorMap (float low, float high, float x)
floatL2_magnitude (const Matrix33 &matrix)
Computes the L2 magnitude (Frobenius norm) of a matrix.

XMatrix< n, n, T >LU (const XMatrix< n, n, T > &m, XMatrix< n, n, T > &L)
T::value_typeLength (const T &v)
Computes the length (magnitude) of a vector.

floatLength (const Quat &a)
T::value_typeLengthSq (const T v)
Computes the squared length of a vector.

VLerp (const V &start, const V &end, const T &t)
Performs linear interpolation between two values.

ColourLinearToSrgb (const Colour &c)
floatLog (float base, float x)
intLog2 (int x)
Mat44LookAtMatrix (const Point3 &viewer, const Point3 &target)
TMax (T a, T b)
Returns the maximum of two values.

Point3Max (const Point3 &a, const Point3 &b)
Computes the component-wise maximum of two points.

XVector2< T >Max (const XVector2< T > &a, const XVector2< T > &b)
Computes the component-wise maximum of two vectors.

XVector3< T >Max (const XVector3< T > &a, const XVector3< T > &b)
Component-wise maximum of two vectors.

TMin (T a, T b)
Returns the minimum of two values.

Point3Min (const Point3 &a, const Point3 &b)
Computes the component-wise minimum of two points.

XVector2< T >Min (const XVector2< T > &a, const XVector2< T > &b)
Computes the component-wise minimum of two vectors.

XVector3< T >Min (const XVector3< T > &a, const XVector3< T > &b)
Component-wise minimum of two vectors.

floatMod (float x, float y)
Computes the floating-point remainder of x/y.

Matrix22Multiply (const Matrix22 &a, const Matrix22 &b)
Multiplies two 2x2 matrices.

Matrix22Multiply (float s, const Matrix22 &m)
Multiplies a 2x2 matrix by a scalar value.

Vec2Multiply (const Matrix22 &a, const Vec2 &x)
Multiplies a 2x2 matrix by a 2D vector.

Vec3Multiply (const Matrix33 &a, const Vec3 &x)
Multiplies a matrix by a vector.

Matrix33Multiply (float s, const Matrix33 &m)
Multiplies a matrix by a scalar.

Matrix33Multiply (const Matrix33 &a, const Matrix33 &b)
Multiplies two matrices.

XVector3< T >Multiply (const XMatrix44< T > &mat, const XVector3< T > &v)
XVector4< T >Multiply (const XMatrix44< T > &mat, const XVector4< T > &v)
Point3Multiply (const XMatrix44< T > &mat, const Point3 &v)
XMatrix< m, o >Multiply (const XMatrix< m, n, T > &lhs, const XMatrix< n, o, T > &rhs)
TNormalize (const T &v)
Normalizes a vector to unit length.

QuatNormalize (const Quat &q)
Vec4NormalizePlane (const Vec4 &p)
Mat44OrthographicMatrix (float left, float right, float bottom, float top, float n, float f)
Matrix22Outer (const Vec2 &a, const Vec2 &b)
Computes the outer product of two 2D vectors.

Matrix33Outer (const Vec3 &a, const Vec3 &b)
Computes the outer product of two vectors.

XMatrix44< float >Outer (const Vec4 &a, const Vec4 &b)
XMatrix< n, n >Permutation (int i, int j)
XVector2< T >PerpCCW (const XVector2< T > &v)
Returns the counter-clockwise perpendicular vector.

XVector2< T >PerpCW (const XVector2< T > &v)
Returns the clockwise perpendicular vector.

Vec4PlaneFromPoints (const Vec3 &p, const Vec3 &q, const Vec3 &r)
boolPointInTriangle (Vec3 a, Vec3 b, Vec3 c, Vec3 p)
intPoissonSample3D (float radius, float separation, Vec3 *points, int maxPoints, int maxAttempts)
intPoissonSampleBox3D (Vec3 lower, Vec3 upper, float separation, Vec3 *points, int maxPoints, int maxAttempts)
Matrix22PolarDecomposition (const Matrix22 &m)
Performs polar decomposition of a 2x2 matrix.

floatPow (float b, float e)
Computes b raised to the power e.

voidPrintMatrix (const char *name, XMatrix< m, n > a)
Mat44ProjectionMatrix (float fov, float aspect, float znear, float zfar)
Matrix22QRDecomposition (const Matrix22 &m)
Performs QR decomposition of a 2x2 matrix.

QuatQuatFromAxisAngle(const Vec3 &axis, float angle)
XQuat< T >QuatFromAxisAngle(const Vec3 &axis, float angle)
QuatQuatFromEulerZYX (float rotx, float roty, float rotz)
floatRadToDeg (float t)
Converts radians to degrees.

uint32_tRand (uint32_t min, uint32_t max)
uint32_tRand ()
voidRandInit (uint32_t seed=315645664)
Vec3RandVec3 ()
Vec4Randf (const Vec4 &range)
floatRandf ()
floatRandf (float max)
floatRandf (float min, float max)
floatRandom (float lo, float hi)
voidRandomShuffle (T begin, T end)
floatRandomSignedUnit ()
floatRandomUnit ()
Vec3RandomUnitVector ()
TRangeMap (T value, T lower, T upper)
Vec3Rotate (const Quat &q, const Vec3 &x)
Vec3RotateInv (const Quat &q, const Vec3 &x)
Matrix22RotationMatrix (float theta)
Creates a 2D rotation matrix for the given angle.

Mat44RotationMatrix (float angle, const Vec3 &axis)
Mat44RotationMatrix (const Quat &q)
intRound (float f)
Rounds a float value to the nearest integer.

TSafeNormalize (const T &v, const T &fallback=T())
Safely normalizes a vector with fallback for zero-length vectors.

floatScalarTriple (const Vec3 &a, const Vec3 &b, const Vec3 &c)
Mat44ScaleMatrix (const Vector3 &s)
floatSgn (float x)
Computes the sign of a value.

floatSign (float x)
Computes the sign of a float value.

doubleSign (double x)
Computes the sign of a double value.

floatSin (float theta)
Computes the sine of an angle.

voidSinCos (float theta, float &s, float &c)
Computes both sine and cosine of an angle simultaneously.

Matrix33Skew (const Vec3 &v)
Creates a skew-symmetric matrix from a vector.

voidSleep (double seconds)
floatSmoothStep (float a, float b, float t)
XMatrix< m, 1, T >Solve (const XMatrix< m, m, T > &L, const XMatrix< m, m, T > &U, const XMatrix< m, 1, T > &b)
boolSolveQuadratic (T a, T b, T c, T &minT, T &maxT)
floatSpecularExponentToRoughness (float exponent, float maxExponent=2048.0f)
floatSpecularRoughnessToExponent (float roughness, float maxExponent=2048.0f)
Vec3SphericalToXYZ (float theta, float phi)
floatSqDistPointSegment (Vec3 a, Vec3 b, Vec3 c)
TSqr (T x)
Computes the square of a value.

doubleSqrt (double x)
Computes the square root of a double value.

floatSqrt (float x)
Computes the square root of a float value.

ColourSrgbToLinear (const Colour &c)
floatSurfaceArea (const Bounds &b)
voidSwap (T &a, T &b)
Swaps two values.

floatTan (float theta)
Computes the tangent of an angle.

boolTestSphereAgainstFrustum (const Plane *planes, Vec3 center, float radius)
intTightPack3D (float radius, float separation, Vec3 *points, int maxPoints)
ColourToneMap (const Colour &s)
floatTrace (const Matrix22 &a)
Calculates the trace of a 2x2 matrix.

floatTrace (const Matrix33 &a)
Computes the trace (sum of diagonal elements) of a matrix.

voidTransformBounds (const Quat &q, Vec3 extents, Vec3 &newExtents)
voidTransformBounds (const Vec3 &localLower, const Vec3 &localUpper, const Vec3 &translation, const Quat &rotation, float scale, Vec3 &lower, Vec3 &upper)
Mat44TransformFromVector (const Vec3 &w, const Point3 &t=Point3(0.0f, 0.0f, 0.0f))
Mat44TransformMatrix (const Rotation &r, const Point3 &p)
Mat44TransformMatrix (const Transform &t)
Vec3TransformPoint (const Transform &t, const Vec3 &v)
Vec3TransformVector (const Transform &t, const Vec3 &v)
Mat44TranslationMatrix (const Point3 &t)
Matrix22Transpose (const Matrix22 &a)
Computes the transpose of a 2x2 matrix.

Matrix33Transpose (const Matrix33 &a)
Computes the transpose of a matrix.

XMatrix44< T >Transpose (const XMatrix44< T > &m)
XMatrix< n, m >Transpose (const XMatrix< m, n > &a)
Vec2UniformSampleDisc ()
Vec3UniformSampleHemisphere ()
Vec3UniformSampleSphere ()
Vec3UniformSampleSphereVolume ()
voidUniformSampleTriangle (float &u, float &v)
BoundsUnion (const Bounds &a, const Bounds &b)
BoundsUnion (const Bounds &a, const Vec3 &b)
floatVectorToAngle (const Vec2 &v)
Mat44ViewMatrix (const Point3 &pos)
ColourXYZToLinear (float x, float y, float z)
ColourYxyToXYZ (float Y, float x, float y)
std::unique_ptr< isaacsim::ros2::bridge::Ros2Factory >createFactory()
Factory creation function exported by the library.

isaacsim::ros2::tf_viewer::Tf2Factory *createFactory()
Factory creation function for non-Windows platforms.

isaacsim::ros2::bridge::Ros2Factory *createFactoryC ()
C wrapper for factory creation function for dynamic symbol loading.

Quateuler_xyz2quat (const float x_rot, const float y_rot, const float z_rot)
intgetClosestAxis (const Vec3 &vec)
voidgetEulerXYZ (const XQuat< float > &q, float &X, float &Y, float &Z)
Extracts Euler angles from a quaternion using XYZ rotation order.

voidgetEulerZYX (const Quat &q, float &yawZ, float &pitchY, float &rollX)
Vec3isaacsim::asset::importer::mjcf::Diagonalize (const Matrix33 &m, Quat &massFrame)
std::stringisaacsim::asset::importer::mjcf::GetAttr (const tinyxml2::XMLElement *c, const char *name)
voidisaacsim::asset::importer::mjcf::LoadActuator (tinyxml2::XMLElement *g, MJCFActuator &actuator, std::string className, MJCFActuator::Type type, const std::map< std::string, MJCFClass > &classesInput)
voidisaacsim::asset::importer::mjcf::LoadAssets (tinyxml2::XMLElement *a, const std::string &baseDirPath, MJCFCompiler &compiler, std::map< std::string, MeshInfo > &simulationMeshCache, std::map< std::string, MJCFMesh > &meshes, std::map< std::string, MJCFMaterial > &materials, std::map< std::string, MJCFTexture > &textures, const std::string &className, const std::map< std::string, MJCFClass > &classes, ImportConfig &config)
voidisaacsim::asset::importer::mjcf::LoadBody (tinyxml2::XMLElement *g, std::vector< MJCFBody * > &bodies, MJCFBody &body, std::string className, MJCFCompiler &compiler, std::map< std::string, MJCFClass > &classes, const std::string &baseDirPath)
voidisaacsim::asset::importer::mjcf::LoadCompiler (tinyxml2::XMLElement *c, MJCFCompiler &compiler)
voidisaacsim::asset::importer::mjcf::LoadContact (tinyxml2::XMLElement *g, MJCFContact &contact, MJCFContact::Type type, std::map< std::string, MJCFClass > &classes)
voidisaacsim::asset::importer::mjcf::LoadDefault (tinyxml2::XMLElement *e, const std::string &className, MJCFClass &cl, MJCFCompiler &compiler, std::map< std::string, MJCFClass > &classes)
tinyxml2::XMLElement *isaacsim::asset::importer::mjcf::LoadFile (tinyxml2::XMLDocument &doc, const std::string &filePath)
voidisaacsim::asset::importer::mjcf::LoadFreeJoint (tinyxml2::XMLElement *g, MJCFJoint &joint, std::string className, MJCFCompiler &compiler, const std::map< std::string, MJCFClass > &classesInput, bool isDefault)
voidisaacsim::asset::importer::mjcf::LoadGeom (tinyxml2::XMLElement *g, MJCFGeom &geom, std::string className, MJCFCompiler &compiler, const std::map< std::string, MJCFClass > &classesInput, bool isDefault)
voidisaacsim::asset::importer::mjcf::LoadGlobals (tinyxml2::XMLElement *root, std::string &defaultClassName, const std::string &baseDirPath, MJCFBody &worldBody, std::vector< MJCFBody * > &bodies, std::vector< MJCFActuator * > &actuators, std::vector< MJCFTendon * > &tendons, std::vector< MJCFContact * > &contacts, std::vector< MJCFEqualityConnect * > &equalityConnects, std::map< std::string, MeshInfo > &simulationMeshCache, std::map< std::string, MJCFMesh > &meshes, std::map< std::string, MJCFMaterial > &materials, std::map< std::string, MJCFTexture > &textures, MJCFCompiler &compiler, std::map< std::string, MJCFClass > &classes, std::map< std::string, int > &jointToActuatorIdx, ImportConfig &config)
tinyxml2::XMLElement *isaacsim::asset::importer::mjcf::LoadInclude (tinyxml2::XMLDocument &doc, const tinyxml2::XMLElement *c, const std::string &baseDirPath)
voidisaacsim::asset::importer::mjcf::LoadInertial (tinyxml2::XMLElement *i, MJCFInertial &inertial)
voidisaacsim::asset::importer::mjcf::LoadJoint (tinyxml2::XMLElement *g, MJCFJoint &joint, std::string className, const MJCFCompiler &compiler, const std::map< std::string, MJCFClass > &classesInput, bool isDefault)
voidisaacsim::asset::importer::mjcf::LoadMesh (tinyxml2::XMLElement *m, MJCFMesh &mesh, std::string className, MJCFCompiler &compiler, const std::map< std::string, MJCFClass > &classesInput)
voidisaacsim::asset::importer::mjcf::LoadSite (tinyxml2::XMLElement *s, MJCFSite &site, std::string className, MJCFCompiler &compiler, const std::map< std::string, MJCFClass > &classesInput, bool isDefault)
voidisaacsim::asset::importer::mjcf::LoadTendon (tinyxml2::XMLElement *t, MJCFTendon &tendon, std::string className, MJCFTendon::Type type, const std::map< std::string, MJCFClass > &classesInput)
std::stringisaacsim::asset::importer::mjcf::SanitizeUsdName (const std::string &src)
voidisaacsim::asset::importer::mjcf::applyArticulationAPI (std::unordered_map< std::string, pxr::UsdStageRefPtr > stages, pxr::UsdGeomXformable prim, const isaacsim::asset::importer::mjcf::ImportConfig config)
voidisaacsim::asset::importer::mjcf::applyCollisionGeom (pxr::UsdStageWeakPtr stage, pxr::UsdPrim prim, bool ConvexDecomposition)
voidisaacsim::asset::importer::mjcf::applyJointLimits (pxr::UsdPhysicsJoint jointPrim, const MJCFJoint *joint, const MJCFActuator *actuator, const int *axisMap, const int jointIdx, const int numJoints, const ImportConfig &config)
voidisaacsim::asset::importer::mjcf::applyPhysxJoint (pxr::UsdPhysicsJoint &jointPrim, const MJCFJoint *joint)
voidisaacsim::asset::importer::mjcf::applyRigidBody (std::unordered_map< std::string, pxr::UsdStageRefPtr > stages, pxr::UsdGeomXformable bodyPrim, const MJCFBody *body, const ImportConfig &config)
voidisaacsim::asset::importer::mjcf::createAndBindMaterial (pxr::UsdStageWeakPtr stage, pxr::UsdPrim prim, MJCFMaterial *material, MJCFTexture *texture, Vec4 &color, bool colorOnly, std::map< pxr::TfToken, pxr::SdfPath > &materialPaths)
pxr::UsdGeomXformableisaacsim::asset::importer::mjcf::createBody (pxr::UsdStageWeakPtr stage, const std::string &primPath, const Transform &trans, const ImportConfig &config)
pxr::UsdPhysicsJointisaacsim::asset::importer::mjcf::createD6Joint (pxr::UsdStageWeakPtr stage, const std::string &jointPath, const Transform &poseJointToParentBody, const Transform &poseJointToChildBody, const std::string &parentBodyPath, const std::string &bodyPath, const ImportConfig &config)
pxr::UsdPhysicsJointisaacsim::asset::importer::mjcf::createFixedJoint (pxr::UsdStageWeakPtr stage, const std::string &jointPath, const Transform &poseJointToParentBody, const Transform &poseJointToChildBody, const std::string &parentBodyPath, const std::string &bodyPath, const ImportConfig &config)
voidisaacsim::asset::importer::mjcf::createFixedRoot (std::unordered_map< std::string, pxr::UsdStageRefPtr > stages, const std::string &jointPath, const std::string &bodyPath)
voidisaacsim::asset::importer::mjcf::createJointDrives (pxr::UsdPhysicsJoint jointPrim, const MJCFJoint *joint, const MJCFActuator *actuator, const std::string &axis, const ImportConfig &config)
pxr::UsdGeomMeshisaacsim::asset::importer::mjcf::createMesh (pxr::UsdStageWeakPtr stage, const pxr::SdfPath path, const std::vector< pxr::GfVec3f > &points, const std::vector< pxr::GfVec3f > &normals, const std::vector< int > &indices, const std::vector< int > &vertexCounts)
pxr::UsdPrimisaacsim::asset::importer::mjcf::createPrimitiveGeom (pxr::UsdStageWeakPtr stage, const std::string &geomPath, const MJCFSite *site, const ImportConfig &config, bool importMaterials)
pxr::UsdPrimisaacsim::asset::importer::mjcf::createPrimitiveGeom (pxr::UsdStageWeakPtr stage, const std::string &geomPath, const MJCFGeom *geom, const std::map< std::string, MeshInfo > &simulationMeshCache, const ImportConfig &config, std::map< pxr::TfToken, pxr::SdfPath > &materialPaths, bool importMaterials, const std::string &rootPrimPath, bool collisionGeom)
voidisaacsim::asset::importer::mjcf::createRoot (std::unordered_map< std::string, pxr::UsdStageRefPtr > stages, Transform trans, const std::string &rootPrimPath, const isaacsim::asset::importer::mjcf::ImportConfig config)
pxr::UsdPrimisaacsim::asset::importer::mjcf::createUsdMesh (pxr::UsdStageWeakPtr stage, const pxr::SdfPath path, Mesh *mesh, float scale, bool importMaterials, bool instanceable)
voidisaacsim::asset::importer::mjcf::getAngleAxisIfExist (tinyxml2::XMLElement *e, const char *aname, Quat &q, bool angleInRad)
voidisaacsim::asset::importer::mjcf::getEulerIfExist (tinyxml2::XMLElement *e, const char *aname, Quat &q, std::string eulerseq, bool angleInRad)
voidisaacsim::asset::importer::mjcf::getIfExist (tinyxml2::XMLElement *e, const char *aname, Vec3 &p)
voidisaacsim::asset::importer::mjcf::getIfExist (tinyxml2::XMLElement *e, const char *aname, float &p)
voidisaacsim::asset::importer::mjcf::getIfExist (tinyxml2::XMLElement *e, const char *aname, Quat &q)
voidisaacsim::asset::importer::mjcf::getIfExist (tinyxml2::XMLElement *e, const char *aname, bool &p)
voidisaacsim::asset::importer::mjcf::getIfExist (tinyxml2::XMLElement *e, const char *aname, Vec4 &p)
voidisaacsim::asset::importer::mjcf::getIfExist (tinyxml2::XMLElement *e, const char *aname, Vec3 &from, Vec3 &to)
voidisaacsim::asset::importer::mjcf::getIfExist (tinyxml2::XMLElement *e, const char *aname, Vec2 &p)
voidisaacsim::asset::importer::mjcf::getIfExist (tinyxml2::XMLElement *e, const char *aname, int &p)
voidisaacsim::asset::importer::mjcf::getIfExist (tinyxml2::XMLElement *e, const char *aname, std::string &s)
pxr::SdfPathisaacsim::asset::importer::mjcf::getNextFreePath (pxr::UsdStageWeakPtr stage, const pxr::SdfPath &primPath)
voidisaacsim::asset::importer::mjcf::getZAxisIfExist (tinyxml2::XMLElement *e, const char *aname, Quat &q)
Quatisaacsim::asset::importer::mjcf::indexedRotation (int axis, float s, float c)
voidisaacsim::asset::importer::mjcf::initPhysicsJoint (pxr::UsdPhysicsJoint &jointPrim, const Transform &poseJointToParentBody, const Transform &poseJointToChildBody, const std::string &parentBodyPath, const std::string &bodyPath, const float &distanceScale)
voidisaacsim::asset::importer::mjcf::setStageMetadata (pxr::UsdStageWeakPtr stage, const isaacsim::asset::importer::mjcf::ImportConfig config)
Vec3isaacsim::asset::importer::urdf::Diagonalize (const Matrix33 &m, Quat &massFrame)
std::stringisaacsim::asset::importer::urdf::GetNewSdfPathString (pxr::UsdStageWeakPtr stage, std::string path, int nameClashNum=-1)
boolisaacsim::asset::importer::urdf::IsUsdFile (const std::string &filename)
pxr::SdfPathisaacsim::asset::importer::urdf::SimpleImport (pxr::UsdStageRefPtr usdStage, const std::string &path, const std::string &meshPath, std::map< pxr::TfToken, pxr::SdfPath > &meshList, std::map< pxr::TfToken, pxr::SdfPath > &materialList, const pxr::SdfPath &rootPath)
boolisaacsim::asset::importer::urdf::addVisualMeshToCollision (UrdfRobot &robot)
boolisaacsim::asset::importer::urdf::collapseFixedJoints (UrdfRobot &robot)
floatisaacsim::asset::importer::urdf::computeSimpleStiffness (const UrdfRobot &robot, std::string joint, float naturalFrequency)
boolisaacsim::asset::importer::urdf::findRootLink (const std::map< std::string, UrdfLink > &urdfLinks, const std::map< std::string, UrdfJoint > &urdfJoints, std::string &rootLinkName)
Quatisaacsim::asset::importer::urdf::indexedRotation (int axis, float s, float c)
voidisaacsim::asset::importer::urdf::inertiaToUrdf (const Matrix33 &inertia, UrdfInertia &urdfInertia)
voidisaacsim::asset::importer::urdf::mergeFixedChildLinks (const KinematicChain::Node &parentNode, UrdfRobot &robot)
boolisaacsim::asset::importer::urdf::parseAxis (const tinyxml2::XMLElement &element, UrdfAxis &axis)
boolisaacsim::asset::importer::urdf::parseDynamics (const tinyxml2::XMLElement &element, UrdfDynamics &dynamics)
boolisaacsim::asset::importer::urdf::parseFixedFrames (const tinyxml2::XMLElement &element, std::map< std::string, UrdfLink > &links)
boolisaacsim::asset::importer::urdf::parseGeometry (const tinyxml2::XMLElement &element, UrdfGeometry &geometry)
boolisaacsim::asset::importer::urdf::parseInertia (const tinyxml2::XMLElement &element, UrdfInertia &inertia)
boolisaacsim::asset::importer::urdf::parseInertial (const tinyxml2::XMLElement &element, UrdfInertial &inertial)
boolisaacsim::asset::importer::urdf::parseJointType (const std::string &str, UrdfJointType &type)
boolisaacsim::asset::importer::urdf::parseJoints (const tinyxml2::XMLElement &root, std::map< std::string, UrdfJoint > &urdfJoints)
boolisaacsim::asset::importer::urdf::parseLimit (const tinyxml2::XMLElement &element, UrdfLimit &limit)
boolisaacsim::asset::importer::urdf::parseLinks (const tinyxml2::XMLElement &root, std::map< std::string, UrdfLink > &urdfLinks)
boolisaacsim::asset::importer::urdf::parseLoopJoints (const tinyxml2::XMLElement &element, std::map< std::string, UrdfLoopJoint > &loopJoints)
boolisaacsim::asset::importer::urdf::parseMass (const tinyxml2::XMLElement &element, float &mass)
boolisaacsim::asset::importer::urdf::parseMaterial (const tinyxml2::XMLElement &element, UrdfMaterial &material)
boolisaacsim::asset::importer::urdf::parseMaterials (const tinyxml2::XMLElement &root, std::map< std::string, UrdfMaterial > &urdfMaterials)
boolisaacsim::asset::importer::urdf::parseOrigin (const tinyxml2::XMLElement &element, Transform &origin)
boolisaacsim::asset::importer::urdf::parseSensors (const tinyxml2::XMLElement &root, std::map< std::string, UrdfLink > &urdfLinks)
boolisaacsim::asset::importer::urdf::parseUrdf (const std::string &urdfPackagePath, const std::string &urdfFileRelativeToPackage, UrdfRobot &urdfRobot)
boolisaacsim::asset::importer::urdf::parseUrdfString (const std::string &urdf_str, UrdfRobot &urdfRobot)
std::stringisaacsim::asset::importer::urdf::resolveXrefPath (const std::string &assetRoot, const std::string &urdfPath, const std::string &xrefpath)
Vec3isaacsim::asset::importer::urdf::urdfAxisToVec (const UrdfAxis &axis)
voidisaacsim::asset::importer::urdf::urdfToInertia (const UrdfInertia &urdfInertia, Matrix33 &inertia)
boolisaacsim::core::cloner::fabricClone (long int stageId, const std::string &source_prim_path, const std::vector< std::string > &prim_paths)
Creates clones of a source prim at specified target paths in the USD stage.

carb::ColorRgbaisaacsim::core::includes::color::distToRgba (double ratio)
Converts a ratio value to a carb::ColorRgba struct.

carb::Float3isaacsim::core::includes::conversions::asCarbFloat3 (const pxr::GfVec3d &v)
Converts pxr::GfVec3d to carb::Float3.

carb::Float3isaacsim::core::includes::conversions::asCarbFloat3 (const pxr::GfVec3f &v)
Converts pxr::GfVec3f to carb::Float3.

carb::Float4isaacsim::core::includes::conversions::asCarbFloat4 (const pxr::GfQuatf &v)
Converts pxr::GfQuatf to carb::Float4.

carb::Float4isaacsim::core::includes::conversions::asCarbFloat4 (const physx::PxQuat &q)
convert physx::PxQuat to carb::Float4

carb::Float4isaacsim::core::includes::conversions::asCarbFloat4 (const pxr::GfQuatd &v)
Converts pxr::GfQuatd to carb::Float4.

pxr::GfQuatdisaacsim::core::includes::conversions::asGfQuatd (const carb::Float4 &q)
Converts a carb::Float4 into a pxr::GfQuatd.

pxr::GfQuatfisaacsim::core::includes::conversions::asGfQuatf (const carb::Float4 &q)
Converts a carb::Float4 into a pxr::GfQuatf.

pxr::GfRotationisaacsim::core::includes::conversions::asGfRotation (const carb::Float4 &q)
Converts a carb::Float4 into a pxr::GfRotation.

pxr::GfTransformisaacsim::core::includes::conversions::asGfTransform (const carb::Float3 &p, const carb::Float4 &r)
Converts position and rotation into a pxr::GfTransform.

pxr::GfVec3disaacsim::core::includes::conversions::asGfVec3d (const carb::Float3 &v)
Converts a carb::Float3 into a pxr::GfVec3d.

pxr::GfVec3fisaacsim::core::includes::conversions::asGfVec3f (const carb::Float3 &v)
Converts a carb::Float3 into a pxr::GfVec3f.

inline ::physx::PxQuatisaacsim::core::includes::conversions::asPxQuat (const usdrt::GfQuatf &v)
Converts usdrt::GfQuatf into PhysX quaternion.

inline ::physx::PxQuatisaacsim::core::includes::conversions::asPxQuat (const pxr::GfQuatd &v)
Converts pxr::GfQuatd into PhysX quaternion.

inline ::physx::PxQuatisaacsim::core::includes::conversions::asPxQuat (const usdrt::GfQuatd &v)
Converts usdrt::GfQuatd into PhysX quaternion.

inline ::physx::PxQuatisaacsim::core::includes::conversions::asPxQuat (const pxr::GfQuatf &v)
Converts pxr::GfQuatf into PhysX quaternion.

inline ::physx::PxQuatisaacsim::core::includes::conversions::asPxQuat (const carb::Float4 &q)
Converts carb::Float4 into PhysX quaternion.

inline ::physx::PxTransformisaacsim::core::includes::conversions::asPxTransform (const pxr::GfTransform &trans)
Converts USD transform into PhysX transform.

inline ::physx::PxTransformisaacsim::core::includes::conversions::asPxTransform (const usdrt::GfVec3d &translation, const usdrt::GfQuatd &orientation)
Converts USD runtime translation and orientation into PhysX transform.

inline ::physx::PxTransformisaacsim::core::includes::conversions::asPxTransform (const usdrt::GfMatrix4d &mat)
Converts USD runtime matrix into PhysX transform.

inline ::physx::PxVec3isaacsim::core::includes::conversions::asPxVec3 (const pxr::GfVec3d &v)
Converts pxr::GfVec3d into PhysX vector.

inline ::physx::PxVec3isaacsim::core::includes::conversions::asPxVec3 (const carb::Float3 &v)
Converts carb::Float3 into PhysX vector.

inline ::physx::PxVec3isaacsim::core::includes::conversions::asPxVec3 (const usdrt::GfVec3d &v)
Converts usdrt::GfVec3d into PhysX vector.

inline ::physx::PxVec3isaacsim::core::includes::conversions::asPxVec3 (const pxr::GfVec3f &v)
Converts pxr::GfVec3f into PhysX vector.

inline ::physx::PxVec3isaacsim::core::includes::conversions::asPxVec3 (const usdrt::GfVec3f &v)
Converts usdrt::GfVec3f into PhysX vector.

voidisaacsim::core::includes::copyTimeSamplesFromWeakerLayer (pxr::UsdStage &stage, const pxr::UsdAttribute &attr)
Copy TimeSample From Waker Layer.

pxr::GfMatrix4disaacsim::core::includes::findInnerTransform (pxr::UsdPrim prim, const pxr::GfMatrix4d &mtx, bool &foundTransformOp, pxr::UsdTimeCode timecode=pxr::UsdTimeCode::Default(), bool skipEqualSetForTimeSample=false)
Given a target local transform matrix for a prim, determine what value to set just the transformOp when other xformOps are present.

const PXR_NS::TfTokenisaacsim::core::includes::g_kIsaacNameOveride("isaac:nameOverride")
Token for overriding prim names in Isaac Sim.

TimeSamplesOnLayerisaacsim::core::includes::getAttributeEffectiveTimeSampleLayerInfo (const pxr::UsdStage &stage, const pxr::UsdAttribute &attr, pxr::SdfLayerRefPtr *outLayer=nullptr)
check if attribute has efficient timesample and these data are on currentlayer/strongerlayer/weakerlayer

pxr::UsdAttributeisaacsim::core::includes::getCameraAttributeFromRenderProduct (const std::string &attributeString, const std::string &renderProductPathString)
Retrieves a specific attribute from a camera associated with a render product.

pxr::UsdPrimisaacsim::core::includes::getCameraPrimFromRenderProduct (const std::string &renderProductPathString)
Retrieves the camera prim associated with a render product.

PXR_NS::SdfLayerRefPtrisaacsim::core::includes::getLayerIfDefOnSessionOrItsSublayers (PXR_NS::UsdStageRefPtr stage, const PXR_NS::SdfPath &path)
Finds if the given prim path has a "def" primSpec on session layer or its sublayers.

PXR_NS::SdfLayerRefPtrisaacsim::core::includes::getLayerIfSpecOnSessionOrItsSublayers (PXR_NS::UsdStageRefPtr stage, const PXR_NS::SdfPath &path, const std::function< bool(PXR_NS::SdfSpecHandle)> &predicate=nullptr)
Finds if the given path has a spec on session layer or its sublayers.

pxr::GfMatrix4disaacsim::core::includes::getLocalTransformMatrix (const pxr::UsdPrim &prim, pxr::UsdTimeCode time=pxr::UsdTimeCode::Default())
Gets local transform matrix of a prim.

std::stringisaacsim::core::includes::getName (const pxr::UsdPrim &prim)
Retrieves the name of a USD prim, with support for custom overrides.

pxr::SdfPathisaacsim::core::includes::getSdfPathFromUint64 (uint64_t pathToken)
Converts a uint64_t token to a USD path.

pxr::GfMatrix4disaacsim::core::includes::getWorldTransformMatrix (const pxr::UsdPrim &prim, pxr::UsdTimeCode time=pxr::UsdTimeCode::Default())
Gets world transform matrix of a prim.

boolisaacsim::core::includes::hasTimeSample (const pxr::UsdAttribute &attribute, pxr::UsdTimeCode timeCode)
Checks if a UsdAttribute instance has time sample on key timeCode.

boolisaacsim::core::includes::isTimeSampled (const pxr::UsdAttribute &attribute)
Checks if a UsdAttribute instance is time sampled.

carb::Float3isaacsim::core::includes::math::cross (const carb::Float3 &b, const carb::Float3 &c)
Computes the cross product of two 3D vectors.

floatisaacsim::core::includes::math::dot (const carb::Float4 &v1, const carb::Float4 &v2)
Computes the dot product of two 4D vectors.

floatisaacsim::core::includes::math::dot (const carb::Float3 &v1, const carb::Float3 &v2)
Computes the dot product of two 3D vectors.

carb::Float3isaacsim::core::includes::math::getBasisVectorX (const carb::Float4 &q)
Gets the X basis vector from a rotation quaternion.

carb::Float3isaacsim::core::includes::math::getBasisVectorY (const carb::Float4 &q)
Gets the Y basis vector from a rotation quaternion.

carb::Float3isaacsim::core::includes::math::getBasisVectorZ (const carb::Float4 &q)
Gets the Z basis vector from a rotation quaternion.

carb::Float4isaacsim::core::includes::math::inverse (const carb::Float4 &q)
Computes the inverse of a quaternion.

carb::Float3isaacsim::core::includes::math::lerp (const carb::Float3 &start, const carb::Float3 &end, const float t)
Linearly interpolates between two 3D vectors.

carb::Float4isaacsim::core::includes::math::lerp (const carb::Float4 &start, const carb::Float4 &end, const float t)
Linearly interpolates between two quaternions.

pxr::GfQuatfisaacsim::core::includes::math::lookAt (const pxr::GfVec3f &camera, const pxr::GfVec3f &target, const pxr::GfVec3f &up)
Computes a look-at quaternion rotation.

carb::Float3isaacsim::core::includes::math::normalize (const carb::Float3 &q)
Normalizes a 3D vector to unit length.

carb::Float4isaacsim::core::includes::math::normalize (const carb::Float4 &q)
Normalizes a quaternion to unit length.

carb::Float4isaacsim::core::includes::math::operator* (const carb::Float4 &a, const carb::Float4 &b)
Performs quaternion multiplication.

carb::Float4isaacsim::core::includes::math::operator* (const carb::Float4 &a, const float x)
Scales a 4D vector/quaternion by a scalar value.

carb::Float3isaacsim::core::includes::math::operator* (const carb::Float3 &a, const float x)
Scales a 3D vector by a scalar value.

carb::Float4isaacsim::core::includes::math::operator+ (const carb::Float4 &a, const carb::Float4 &b)
Adds two 4D vectors/quaternions.

carb::Float3isaacsim::core::includes::math::operator+ (const carb::Float3 &a, const carb::Float3 &b)
Adds two 3D vectors.

carb::Float3isaacsim::core::includes::math::operator- (const carb::Float3 &a, const carb::Float3 &b)
Subtracts two 3D vectors.

carb::Float4isaacsim::core::includes::math::operator- (const carb::Float4 &a, const carb::Float4 &b)
Subtracts two 4D vectors/quaternions.

carb::Float3isaacsim::core::includes::math::rotate (const carb::Float4 &q, const carb::Float3 x)
Rotates a vector by a quaternion.

doubleisaacsim::core::includes::math::roundNearest (double input, double place)
Rounds a number to the nearest multiple of a given value.

carb::Float4isaacsim::core::includes::math::slerp (const carb::Float4 &start, const carb::Float4 &end, const float t)
Performs spherical linear interpolation between quaternions.

pxr::GfTransformisaacsim::core::includes::math::transformInv (const pxr::GfTransform &a, const pxr::GfTransform &b)
Computes the local transform of b relative to transform a.

usdrt::GfMatrix4disaacsim::core::includes::pose::computeWorldXformNoCache (pxr::UsdStageRefPtr usdStage, usdrt::UsdStageRefPtr usdrtStage, const pxr::SdfPath &path, pxr::UsdTimeCode timecode=pxr::UsdTimeCode::Default(), bool useFabricHierarchy=true, bool logWarningOnFallback=false)
Computes the world transform of a prim.

usdrt::GfMatrix4disaacsim::core::includes::pose::getRelativeTransform (pxr::UsdStageRefPtr usdStage, usdrt::UsdStageRefPtr usdrtStage, const pxr::SdfPath &sourcePrim, const pxr::SdfPath &targetPrim)
Computes the relative transform matrix between two prims.

voidisaacsim::core::includes::posetree::createTensorDesc (TensorDesc &tensorDesc, void *dataPtr, int numXforms, TensorDataType type, int device)
voidisaacsim::core::includes::safeGetAttribute (const pxr::UsdAttribute &attr, T &inputValue)
Safely retrieves a USD attribute value with error handling.

boolisaacsim::core::includes::setAttribute (const pxr::UsdAttribute &attribute, const ValueType &val, pxr::UsdTimeCode timeCode=pxr::UsdTimeCode::Default(), bool skipEqualSetForTimeSample=false, bool autoTargetSessionLayer=true)
Sets attribute value with optional time sampling and session layer targeting.

boolisaacsim::core::includes::setLocalTransformMatrix (pxr::UsdPrim prim, const pxr::GfMatrix4d &mtxIn, pxr::UsdTimeCode timecode=pxr::UsdTimeCode::Default(), bool skipEqualSetForTimeSample=false, std::unique_ptr< PXR_NS::SdfChangeBlock > *parentChangeBlock=nullptr)
Sets local transform matrix of a prim.

boolisaacsim::core::includes::setValueWithPrecision (pxr::UsdGeomXformOp &xformOp, const ValueType &value, pxr::UsdTimeCode timeCode=pxr::UsdTimeCode::Default(), bool skipEqualSetForTimeSample=false)
Set value with precision based on the UsdGeomXformOp precision type.

voidisaacsim::core::includes::transforms::createTensorDesc (TensorDesc &tensorDesc, void *dataPtr, int numElements, TensorDataType type)
voidisaacsim::core::includes::transforms::setScale (pxr::UsdPrim &prim, pxr::GfVec3f pxBodyScale)
Sets the scale of a USD prim.

voidisaacsim::core::includes::transforms::setTransform (pxr::UsdPrim &prim, pxr::GfVec3f bodyTranslation, pxr::GfQuatf bodyRotation)
Sets the transform (position and rotation) of a USD prim.

std::stringisaacsim::core::includes::utils::path::MakeRelativePath (const std::string &filePath, const std::string &fileRelativePath)
boolisaacsim::core::includes::utils::path::createSymbolicLink (const std::string &target, const std::string &link)
std::stringisaacsim::core::includes::utils::path::getParent (const std::string &filePath)
std::stringisaacsim::core::includes::utils::path::getPathStem (const char *path)
boolisaacsim::core::includes::utils::path::hasExtension (const std::string &filename, const std::string &extension)
boolisaacsim::core::includes::utils::path::isAbsolutePath (const char *path)
boolisaacsim::core::includes::utils::path::isFile (const std::string &path)
std::stringisaacsim::core::includes::utils::path::normalizeUrl (const char *url)
std::stringisaacsim::core::includes::utils::path::pathJoin (const std::string &path1, const std::string &path2)
std::stringisaacsim::core::includes::utils::path::resolve_absolute (std::string parent, std::string relative)
std::stringisaacsim::core::includes::utils::path::resolve_path (const std::string &path)
Calculates the final path by resolving the relative path and removing any unnecessary components.

std::stringisaacsim::core::includes::utils::path::resolve_relative (const std::string &base, const std::string &target)
Calculates the relative path of target relative to base.

std::vector< std::string >isaacsim::core::includes::utils::path::split_path (const std::string &path)
PathTypeisaacsim::core::includes::utils::path::testPath (const char *path)
std::stringisaacsim::core::includes::utils::path::toLowercase (const std::string &str)
pxr::GfMatrix4disaacsim::core::includes::utils::usd::GetGlobalTransform (const pxr::UsdPrim &prim)
std::stringisaacsim::core::includes::utils::usd::GetNewSdfPathString (pxr::UsdStageWeakPtr stage, std::string path, int nameClashNum=0)
std::stringisaacsim::core::includes::utils::usd::makeValidUSDIdentifier (const std::string &name)
boolisaacsim::core::includes::utils::usd::setAuthoringLayer (pxr::UsdStageRefPtr stage, const std::string &layerIdentifier)
Select a existing layer as edit target.

voidisaacsim::core::utils::findMatchingChildren (pxr::UsdPrim root, const std::string &pattern, std::vector< pxr::UsdPrim > &primsRet)
Finds child prims matching a specified name pattern.

std::vector< std::string >isaacsim::core::utils::findMatchingPrimPaths (const std::string &pattern, long int stageId, const std::string &api=std::string(""))
Finds USD prims matching a specified path pattern.

voidisaacsim::robot::schema::ApplyAttachmentPointAPI (pxr::UsdPrim &prim)
voidisaacsim::robot::schema::ApplyJointAPI (pxr::UsdPrim &prim)
voidisaacsim::robot::schema::ApplyLinkAPI (pxr::UsdPrim &prim)
voidisaacsim::robot::schema::ApplyReferencePointAPI (pxr::UsdPrim &prim)
voidisaacsim::robot::schema::ApplyRobotAPI (pxr::UsdPrim &prim)
pxr::UsdPrimisaacsim::robot::schema::CreateSurfaceGripper (pxr::UsdStagePtr stage, const std::string &primPath)
const std::stringisaacsim::robot::schema::_attrPrefix("isaac")
const pxr::TfTokenisaacsim::robot::schema::className (Classes name)
pxr::TfTokenisaacsim::robot::schema::getAttributeName (Attributes attr)
GripperStatusisaacsim::robot::surface_gripper::GripperStatusFromToken (const pxr::TfToken &token)
std::stringisaacsim::robot::surface_gripper::GripperStatusToString (GripperStatus status)
pxr::TfTokenisaacsim::robot::surface_gripper::GripperStatusToToken (GripperStatus status)
boolisaacsim::ros2::bridge::isRos2DistroSupported (const std::string &distro)
Checks if a ROS 2 distribution is supported.

const boolisaacsim::ros2::bridge::jsonToRos2QoSProfile (Ros2QoSProfile &qos, const std::string &jsonString)
Converts a JSON string to a ROS 2 QoS profile.

boolisaacsim::ros2::omnigraph_utils::checkCondition (const void *ptr, std::string message)
Verifies that a pointer is not null and logs an error message if it is.

boolisaacsim::ros2::omnigraph_utils::createOgAttributesForFields (OgnROS2DatabaseDerivedType &db, const NodeObj &nodeObj, std::vector< DynamicMessageField > messageFields, const std::string prependStr, std::string messageType)
Creates OmniGraph attributes for message fields.

boolisaacsim::ros2::omnigraph_utils::createOgAttributesForMessage (OgnROS2DatabaseDerivedType &db, const NodeObj &nodeObj, const std::string &messagePackage, const std::string &messageSubfolder, const std::string &messageName, std::shared_ptr< Ros2Message > message, const std::string prependStr)
Creates OmniGraph attributes for a ROS 2 message.

boolisaacsim::ros2::omnigraph_utils::findMatchingAttribute (OgnROS2DatabaseDerivedType &db, const NodeObj &nodeObj, std::vector< DynamicMessageField > messageFields, const std::string prependStr)
Checks if node attributes match message fields.

T const *isaacsim::ros2::omnigraph_utils::getAttributeReadableArrayData (const NodeObj &nodeObj, const std::string &attrName, size_t &newCount)
Gets read-only data for an array attribute.

T const *isaacsim::ros2::omnigraph_utils::getAttributeReadableData (const NodeObj &nodeObj, const std::string &attrName)
Gets read-only data for a simple attribute.

T *isaacsim::ros2::omnigraph_utils::getAttributeWritableArrayData (const NodeObj &nodeObj, const std::string &attrName, size_t newCount)
Gets writable data for an array attribute with resizing.

T *isaacsim::ros2::omnigraph_utils::getAttributeWritableData (const NodeObj &nodeObj, const std::string &attrName)
Gets writable data for a simple attribute.

std::stringisaacsim::ros2::omnigraph_utils::inputOutput (bool isOutput)
Returns the OmniGraph attribute prefix based on direction.

boolisaacsim::ros2::omnigraph_utils::removeDynamicAttributes (const NodeObj &nodeObj)
Removes dynamic attributes from a node.

boolisaacsim::ros2::omnigraph_utils::writeMessageDataFromNode (OmniGraphDatabase &db, std::shared_ptr< Ros2Message > message, std::string prependStr, bool isOutput)
Reads attribute data from an OmniGraph node and writes it to a ROS 2 message.

boolisaacsim::ros2::omnigraph_utils::writeNodeAttributeFromMessage (OmniGraphDatabase &db, std::shared_ptr< Ros2Message > message, std::string prependStr, bool isOutput)
Reads data from a ROS 2 message and writes it to OmniGraph node attributes.

uint64_tisaacsim::sensors::physics::asInt (const pxr::SdfPath &path)
Converts a USD path to an integer representation.

floatisaacsim::sensors::physics::lerp (const float &start, const float &end, const float t)
Linear interpolation between two values.

voidisaacsim::sensors::rtx::getTransformFromSensorPose (const omni::sensors::FrameAtTime &inPose, omni::math::linalg::matrix4d &matrixOutput)
Converts a sensor pose to a 4x4 transformation matrix.

floatmaxf (const float a, const float b)
std::stringmesh::StatusToString (OmniConverterStatus status)
floatminf (const float a, const float b)
omni::isaac::dynamic_control::DcTransformomni::isaac::dynamic_control::conversions::asDcTransform (const pxr::GfVec3f &p, const pxr::GfQuatf &q)
Converts USD position and orientation into Dynamic Control transform.

omni::isaac::dynamic_control::DcTransformomni::isaac::dynamic_control::conversions::asDcTransform (const pxr::GfVec3d &p, const pxr::GfQuatd &q)
Converts USD double precision position and orientation into Dynamic Control transform.

pxr::GfMatrix4domni::isaac::dynamic_control::conversions::asGfMatrix4d (const omni::isaac::dynamic_control::DcTransform &input)
Converts a DcTransform to a GfMatrix4d.

pxr::GfMatrix4fomni::isaac::dynamic_control::conversions::asGfMatrix4f (const omni::isaac::dynamic_control::DcTransform &input)
Converts a DcTransform to a GfMatrix4f.

pxr::GfMatrix4fomni::isaac::dynamic_control::conversions::asGfMatrix4fT (const omni::isaac::dynamic_control::DcTransform &input)
Converts a DcTransform to a transposed GfMatrix4f.

pxr::GfQuatdomni::isaac::dynamic_control::conversions::asGfQuatd (const carb::Float4 &q)
Converts a carb::Float4 into a pxr::GfQuatd.

pxr::GfQuatfomni::isaac::dynamic_control::conversions::asGfQuatf (const carb::Float4 &q)
Converts a carb::Float4 into a pxr::GfQuatf.

pxr::GfRotationomni::isaac::dynamic_control::conversions::asGfRotation (const carb::Float4 &q)
Converts a carb::Float4 into a pxr::GfRotation.

pxr::GfTransformomni::isaac::dynamic_control::conversions::asGfTransform (const omni::isaac::dynamic_control::DcTransform &pose)
Converts a DcTransform into a pxr::GfTransform.

pxr::GfVec3domni::isaac::dynamic_control::conversions::asGfVec3d (const carb::Float3 &v)
Converts a carb::Float3 into a pxr::GfVec3d.

pxr::GfVec3fomni::isaac::dynamic_control::conversions::asGfVec3f (const carb::Float3 &v)
Converts a carb::Float3 into a pxr::GfVec3f.

inline ::physx::PxTransformomni::isaac::dynamic_control::conversions::asPxTransform (const omni::isaac::dynamic_control::DcTransform &pose)
Converts DcTransform into PhysX transform.

constexpr uint32_tomni::isaac::dynamic_control::getHandleContextId (DcHandle h)
constexpr uint32_tomni::isaac::dynamic_control::getHandleObjectId (DcHandle h)
constexpr uint32_tomni::isaac::dynamic_control::getHandleTypeId (DcHandle h)
constexpr DcHandleomni::isaac::dynamic_control::makeHandle (uint64_t objectId, uint64_t typeId, uint64_t contextId)
omni::isaac::dynamic_control::DcTransformomni::isaac::dynamic_control::math::inverse (const omni::isaac::dynamic_control::DcTransform &transform)
Computes the inverse of a transform.

omni::isaac::dynamic_control::DcTransformomni::isaac::dynamic_control::math::lerp (const omni::isaac::dynamic_control::DcTransform &a, const omni::isaac::dynamic_control::DcTransform &b, const float t)
Linearly interpolates between two transforms.

omni::isaac::dynamic_control::DcTransformomni::isaac::dynamic_control::math::operator* (const omni::isaac::dynamic_control::DcTransform &self, const omni::isaac::dynamic_control::DcTransform &other)
Multiplies two transforms to compose them.

omni::isaac::dynamic_control::DcTransformomni::isaac::dynamic_control::math::slerp (const omni::isaac::dynamic_control::DcTransform &a, const omni::isaac::dynamic_control::DcTransform &b, const float t)
Performs spherical linear interpolation between transforms.

omni::isaac::dynamic_control::DcTransformomni::isaac::dynamic_control::math::transformInv (const omni::isaac::dynamic_control::DcTransform &a, const omni::isaac::dynamic_control::DcTransform &b)
Computes the relative transform from a to b.

booloperator!= (const Colour &lhs, const Colour &rhs)
Vec2operator* (const Matrix22 &a, const Vec2 &x)
Matrix-vector multiplication operator.

Matrix22operator* (const Matrix22 &a, const Matrix22 &b)
Matrix-matrix multiplication operator.

Matrix22operator* (float s, const Matrix22 &a)
Scalar-matrix multiplication operator (scalar on left).

Matrix22operator* (const Matrix22 &a, float s)
Matrix-scalar multiplication operator (scalar on right).

Matrix33operator* (const Matrix33 &a, float s)
Matrix-scalar multiplication operator (scalar on right)

Vec3operator* (const Matrix33 &a, const Vec3 &x)
Matrix-vector multiplication operator.

Matrix33operator* (const Matrix33 &a, const Matrix33 &b)
Matrix multiplication operator.

Matrix33operator* (float s, const Matrix33 &a)
Scalar-matrix multiplication operator (scalar on left)

XVector4< T >operator* (const XMatrix44< T > &mat, const XVector4< T > &v)
XVector3< T >operator* (const XMatrix44< T > &mat, const XVector3< T > &v)
Point3operator* (const XMatrix44< T > &mat, const Point3 &v)
Colouroperator* (float lhs, const Colour &rhs)
Point3operator* (float lhs, const Point3 &rhs)
Scales a point by a scalar value (left-hand side scalar).

Vec3operator* (const Quat &q, const Vec3 &v)
XQuat< T >operator* (T lhs, const XQuat< T > &rhs)
XVector2< T >operator* (T lhs, const XVector2< T > &rhs)
Scales a vector by a scalar value (left-hand side scalar).

XVector2< T >operator* (const XVector2< T > &lhs, const XVector2< T > &rhs)
Multiplies two vectors component-wise.

XVector3< T >operator* (T lhs, const XVector3< T > &rhs)
Scalar multiplication operator (left-hand side)

XVector4< T >operator* (T lhs, const XVector4< T > &rhs)
Matrix22 &operator*= (Matrix22 &a, float s)
Scalar multiplication assignment operator.

Matrix33 &operator*= (Matrix33 &a, float s)
Scalar multiplication assignment operator.

Matrix22operator+ (const Matrix22 &a, const Matrix22 &b)
Matrix addition operator.

Matrix33operator+ (const Matrix33 &a, const Matrix33 &b)
Matrix addition operator.

XMatrix< m, n, T >operator+ (const XMatrix< m, n, T > &lhs, const XMatrix< m, n, T > &rhs)
Point3operator+ (const Point3 &lhs, const Point3 &rhs)
Adds two points component-wise.

Matrix22 &operator+= (Matrix22 &a, const Matrix22 &b)
Matrix addition assignment operator.

Matrix33 &operator+= (Matrix33 &a, const Matrix33 &b)
Matrix addition assignment operator.

Matrix22operator- (const Matrix22 &a, const Matrix22 &b)
Matrix subtraction operator.

Matrix33operator- (const Matrix33 &a, const Matrix33 &b)
Matrix subtraction operator.

XMatrix< m, n, T >operator- (const XMatrix< m, n, T > &lhs, const XMatrix< m, n, T > &rhs)
Vec3operator- (const Point3 &lhs, const Point3 &rhs)
Computes the vector from one point to another.

Matrix22 &operator-= (Matrix22 &a, const Matrix22 &b)
Matrix subtraction assignment operator.

Matrix33 &operator-= (Matrix33 &a, const Matrix33 &b)
Matrix subtraction assignment operator.

booloperator== (const Colour &lhs, const Colour &rhs)
booloperator== (const Point3 &lhs, const Point3 &rhs)
Tests for equality between two points.

booloperator== (const XQuat< T > &lhs, const XQuat< T > &rhs)
booloperator== (const XVector2< T > &lhs, const XVector2< T > &rhs)
Tests for equality between two vectors.

booloperator== (const XVector3< T > &lhs, const XVector3< T > &rhs)
Equality comparison operator for vectors.

booloperator== (const XVector4< T > &lhs, const XVector4< T > &rhs)
voidquat2Mat (const XQuat< float > &q, Matrix33 &m)
Converts a quaternion to a 3x3 rotation matrix.

voidquat2rpy (const Quat &q1, float &bank, float &attitude, float &heading)
QuatquaternionFromVectors (const Vec3 &vec1, const Vec3 &vec2)
Vec3rotate (const Vec3 &q, float w, const Vec3 &x)
Vec3rotateInv (const Vec3 &q, float w, const Vec3 &x)
Quatrpy2quat (const float roll, const float pitch, const float yaw)
floatsign (float x)
voidzUpQuat2rpy (const Quat &q1, float &roll, float &pitch, float &yaw)
