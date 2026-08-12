<!-- source: py/api/namespace_isaacsim__asset__importer__mjcf.html | title: mjcf — Isaac Sim -->

# mjcf
Fully qualified name: `isaacsim::asset::importer::mjcf`
namespacemjcf

## Classes
MJCFActuator
Actuator component for applying forces/torques to joints.

MJCFBody
Represents a rigid body in the MJCF model hierarchy.

MJCFClass
Class definition for setting default values for MJCF elements.

MJCFCompiler
Compiler settings that affect how the MJCF model is processed.

MJCFContact
Contact definition for collision filtering and contact parameters.

MJCFGeom
Geometry element for collision detection and physics simulation.

MJCFImporter
Main importer class for loading and converting MJCF models to USD format.

MJCFInertial
Inertial properties of a body in the MJCF model.

MJCFJoint
Represents a joint in the MJCF (MuJoCo XML Format) model.

MJCFMaterial
Material definition for visual appearance.

MJCFMesh
Mesh asset definition for 3D geometry.

MJCFSite
Site element for marking specific locations and orientations in the model.

MJCFTendon
Tendon element for creating cable-like constraints between bodies.

MJCFTexture
Texture asset definition for materials.

MJCFVisualElement
Base class for visual elements in MJCF models.

## Enumerations
JointAxis

## Functions
Vec3Diagonalize (const Matrix33 &m, Quat &massFrame)
std::stringGetAttr (const tinyxml2::XMLElement *c, const char *name)
voidLoadActuator (tinyxml2::XMLElement *g, MJCFActuator &actuator, std::string className, MJCFActuator::Type type, const std::map< std::string, MJCFClass > &classesInput)
voidLoadAssets (tinyxml2::XMLElement *a, const std::string &baseDirPath, MJCFCompiler &compiler, std::map< std::string, MeshInfo > &simulationMeshCache, std::map< std::string, MJCFMesh > &meshes, std::map< std::string, MJCFMaterial > &materials, std::map< std::string, MJCFTexture > &textures, const std::string &className, const std::map< std::string, MJCFClass > &classes, ImportConfig &config)
voidLoadBody (tinyxml2::XMLElement *g, std::vector< MJCFBody * > &bodies, MJCFBody &body, std::string className, MJCFCompiler &compiler, std::map< std::string, MJCFClass > &classes, const std::string &baseDirPath)
voidLoadCompiler (tinyxml2::XMLElement *c, MJCFCompiler &compiler)
voidLoadContact (tinyxml2::XMLElement *g, MJCFContact &contact, MJCFContact::Type type, std::map< std::string, MJCFClass > &classes)
voidLoadDefault (tinyxml2::XMLElement *e, const std::string &className, MJCFClass &cl, MJCFCompiler &compiler, std::map< std::string, MJCFClass > &classes)
tinyxml2::XMLElement *LoadFile (tinyxml2::XMLDocument &doc, const std::string &filePath)
voidLoadFreeJoint (tinyxml2::XMLElement *g, MJCFJoint &joint, std::string className, MJCFCompiler &compiler, const std::map< std::string, MJCFClass > &classesInput, bool isDefault)
voidLoadGeom (tinyxml2::XMLElement *g, MJCFGeom &geom, std::string className, MJCFCompiler &compiler, const std::map< std::string, MJCFClass > &classesInput, bool isDefault)
voidLoadGlobals (tinyxml2::XMLElement *root, std::string &defaultClassName, const std::string &baseDirPath, MJCFBody &worldBody, std::vector< MJCFBody * > &bodies, std::vector< MJCFActuator * > &actuators, std::vector< MJCFTendon * > &tendons, std::vector< MJCFContact * > &contacts, std::vector< MJCFEqualityConnect * > &equalityConnects, std::map< std::string, MeshInfo > &simulationMeshCache, std::map< std::string, MJCFMesh > &meshes, std::map< std::string, MJCFMaterial > &materials, std::map< std::string, MJCFTexture > &textures, MJCFCompiler &compiler, std::map< std::string, MJCFClass > &classes, std::map< std::string, int > &jointToActuatorIdx, ImportConfig &config)
tinyxml2::XMLElement *LoadInclude (tinyxml2::XMLDocument &doc, const tinyxml2::XMLElement *c, const std::string &baseDirPath)
voidLoadInertial (tinyxml2::XMLElement *i, MJCFInertial &inertial)
voidLoadJoint (tinyxml2::XMLElement *g, MJCFJoint &joint, std::string className, const MJCFCompiler &compiler, const std::map< std::string, MJCFClass > &classesInput, bool isDefault)
voidLoadMesh (tinyxml2::XMLElement *m, MJCFMesh &mesh, std::string className, MJCFCompiler &compiler, const std::map< std::string, MJCFClass > &classesInput)
voidLoadSite (tinyxml2::XMLElement *s, MJCFSite &site, std::string className, MJCFCompiler &compiler, const std::map< std::string, MJCFClass > &classesInput, bool isDefault)
voidLoadTendon (tinyxml2::XMLElement *t, MJCFTendon &tendon, std::string className, MJCFTendon::Type type, const std::map< std::string, MJCFClass > &classesInput)
std::stringSanitizeUsdName (const std::string &src)
voidapplyArticulationAPI (std::unordered_map< std::string, pxr::UsdStageRefPtr > stages, pxr::UsdGeomXformable prim, const isaacsim::asset::importer::mjcf::ImportConfig config)
voidapplyCollisionGeom (pxr::UsdStageWeakPtr stage, pxr::UsdPrim prim, bool ConvexDecomposition)
voidapplyJointLimits (pxr::UsdPhysicsJoint jointPrim, const MJCFJoint *joint, const MJCFActuator *actuator, const int *axisMap, const int jointIdx, const int numJoints, const ImportConfig &config)
voidapplyPhysxJoint (pxr::UsdPhysicsJoint &jointPrim, const MJCFJoint *joint)
voidapplyRigidBody (std::unordered_map< std::string, pxr::UsdStageRefPtr > stages, pxr::UsdGeomXformable bodyPrim, const MJCFBody *body, const ImportConfig &config)
voidcreateAndBindMaterial (pxr::UsdStageWeakPtr stage, pxr::UsdPrim prim, MJCFMaterial *material, MJCFTexture *texture, Vec4 &color, bool colorOnly, std::map< pxr::TfToken, pxr::SdfPath > &materialPaths)
pxr::UsdGeomXformablecreateBody (pxr::UsdStageWeakPtr stage, const std::string &primPath, const Transform &trans, const ImportConfig &config)
pxr::UsdPhysicsJointcreateD6Joint (pxr::UsdStageWeakPtr stage, const std::string &jointPath, const Transform &poseJointToParentBody, const Transform &poseJointToChildBody, const std::string &parentBodyPath, const std::string &bodyPath, const ImportConfig &config)
pxr::UsdPhysicsJointcreateFixedJoint (pxr::UsdStageWeakPtr stage, const std::string &jointPath, const Transform &poseJointToParentBody, const Transform &poseJointToChildBody, const std::string &parentBodyPath, const std::string &bodyPath, const ImportConfig &config)
voidcreateFixedRoot (std::unordered_map< std::string, pxr::UsdStageRefPtr > stages, const std::string &jointPath, const std::string &bodyPath)
voidcreateJointDrives (pxr::UsdPhysicsJoint jointPrim, const MJCFJoint *joint, const MJCFActuator *actuator, const std::string &axis, const ImportConfig &config)
pxr::UsdGeomMeshcreateMesh (pxr::UsdStageWeakPtr stage, const pxr::SdfPath path, const std::vector< pxr::GfVec3f > &points, const std::vector< pxr::GfVec3f > &normals, const std::vector< int > &indices, const std::vector< int > &vertexCounts)
pxr::UsdPrimcreatePrimitiveGeom (pxr::UsdStageWeakPtr stage, const std::string &geomPath, const MJCFSite *site, const ImportConfig &config, bool importMaterials)
pxr::UsdPrimcreatePrimitiveGeom (pxr::UsdStageWeakPtr stage, const std::string &geomPath, const MJCFGeom *geom, const std::map< std::string, MeshInfo > &simulationMeshCache, const ImportConfig &config, std::map< pxr::TfToken, pxr::SdfPath > &materialPaths, bool importMaterials, const std::string &rootPrimPath, bool collisionGeom)
voidcreateRoot (std::unordered_map< std::string, pxr::UsdStageRefPtr > stages, Transform trans, const std::string &rootPrimPath, const isaacsim::asset::importer::mjcf::ImportConfig config)
pxr::UsdPrimcreateUsdMesh (pxr::UsdStageWeakPtr stage, const pxr::SdfPath path, Mesh *mesh, float scale, bool importMaterials, bool instanceable)
voidgetAngleAxisIfExist (tinyxml2::XMLElement *e, const char *aname, Quat &q, bool angleInRad)
voidgetEulerIfExist (tinyxml2::XMLElement *e, const char *aname, Quat &q, std::string eulerseq, bool angleInRad)
voidgetIfExist (tinyxml2::XMLElement *e, const char *aname, Vec3 &p)
voidgetIfExist (tinyxml2::XMLElement *e, const char *aname, float &p)
voidgetIfExist (tinyxml2::XMLElement *e, const char *aname, Quat &q)
voidgetIfExist (tinyxml2::XMLElement *e, const char *aname, bool &p)
voidgetIfExist (tinyxml2::XMLElement *e, const char *aname, Vec4 &p)
voidgetIfExist (tinyxml2::XMLElement *e, const char *aname, Vec3 &from, Vec3 &to)
voidgetIfExist (tinyxml2::XMLElement *e, const char *aname, Vec2 &p)
voidgetIfExist (tinyxml2::XMLElement *e, const char *aname, int &p)
voidgetIfExist (tinyxml2::XMLElement *e, const char *aname, std::string &s)
pxr::SdfPathgetNextFreePath (pxr::UsdStageWeakPtr stage, const pxr::SdfPath &primPath)
voidgetZAxisIfExist (tinyxml2::XMLElement *e, const char *aname, Quat &q)
QuatindexedRotation (int axis, float s, float c)
voidinitPhysicsJoint (pxr::UsdPhysicsJoint &jointPrim, const Transform &poseJointToParentBody, const Transform &poseJointToChildBody, const std::string &parentBodyPath, const std::string &bodyPath, const float &distanceScale)
voidsetStageMetadata (pxr::UsdStageWeakPtr stage, const isaacsim::asset::importer::mjcf::ImportConfig config)

## Structs
ContactNode
A node in the contact graph representing collision relationships.

ImportConfig
Configuration settings for importing MJCF files.

MJCFEqualityConnect
Equality constraint that connects two bodies at a fixed relative position.

MeshInfo
Information about a mesh used in the MJCF model.

Mjcf
Interface for MJCF file import functionality.

## Typedefs
GymMeshHandle
TriangleMeshHandle
