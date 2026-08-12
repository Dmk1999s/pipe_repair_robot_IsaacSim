<!-- source: py/api/classisaacsim_1_1asset_1_1importer_1_1mjcf_1_1_m_j_c_f_importer.html | title: MJCFImporter — Isaac Sim -->

# MJCFImporter
Fully qualified name: `isaacsim::asset::importer::mjcf::MJCFImporter`
classMJCFImporter

Main importer class for loading and converting MJCF models to USD format.
This class handles the complete import pipeline for MJCF (MuJoCo XML Format) models, including parsing, validation, and conversion to USD format with physics properties. It manages all model components including bodies, joints, geometries, actuators, tendons, materials, and contact definitions.
Public Functions
MJCFImporter(conststd ::stringfullPath, ImportConfig &config)

Constructor that loads and parses an MJCF file.
Parameters:

- fullPath – [in] Full path to the MJCF file

- config – [in] Import configuration settings

~MJCFImporter()

Destructor that cleans up allocated resources.

voidpopulateBodyLookup(MJCFBody *body)

Populates the body lookup maps for fast access.
Parameters:
body – [in] Body to add to lookup maps

boolAddPhysicsEntities(
std ::unordered_map<std ::string,pxr ::UsdStageRefPtr>stages,
constTransform trans,
conststd ::string&rootPrimPath,
constImportConfig &config,
)
Adds physics entities to the USD stages.
Parameters:

- stages – [in] Map of USD stages by name

- trans – [in] Root transformation

- rootPrimPath – [in] Root primitive path in USD

- config – [in] Import configuration settings

Returns:
True if successful, false otherwise

voidCreatePhysicsBodyAndJoint(
std ::unordered_map<std ::string,pxr ::UsdStageRefPtr>stages,
MJCFBody *body,
conststd ::string&rootPath,
conststd ::string&rootPrimPath,
constTransform &trans,
constboolisRoot,
conststd ::string&parentBodyPath,
constImportConfig &config,
conststd ::string&instanceableUsdPath,
pxr ::UsdPrim&robotPrim,
)
Creates physics body and joint USD primitives.
Parameters:

- stages – [in] Map of USD stages by name

- body – [in] MJCF body to convert

- rootPath – [in] Root path for USD primitives

- rootPrimPath – [in] Root primitive path

- trans – [in] Transformation to apply

- isRoot – [in] Whether this is the root body

- parentBodyPath – [in] Path to parent body

- config – [in] Import configuration settings

- instanceableUsdPath – [in] Path for instanceable USD assets

- robotPrim – [inout] Robot primitive in USD

voidaddJoints(
std ::unordered_map<std ::string,pxr ::UsdStageRefPtr>stages,
conststd ::string&rootPath,
conststd ::string&parentBodyPath,
conststd ::string&bodyPath,
MJCFBody *body,
constImportConfig &config,
constTransform &trans0,
constTransform &trans1,
constboolisRoot,
constintnumJoints,
pxr ::UsdPrim&robotPrim,
)
Adds joint USD primitives for a body.
Parameters:

- stages – [in] Map of USD stages by name

- rootPath – [in] Root path for USD primitives

- parentBodyPath – [in] Path to parent body

- bodyPath – [in] Path to current body

- body – [in] MJCF body containing joints

- config – [in] Import configuration settings

- trans0 – [in] Parent body transformation

- trans1 – [in] Current body transformation

- isRoot – [in] Whether this is the root body

- numJoints – [in] Number of joints to process

- robotPrim – [inout] Robot primitive in USD

voidcomputeJointFrame(
Transform &origin,
int*axisMap,
constMJCFBody *body,
)
Computes joint frame transformations.
Parameters:

- origin – [out] Computed joint origin transformation

- axisMap – [out] Axis mapping for joint

- body – [in] Body containing the joint

boolcontactBodyExclusion(MJCFBody *body1, MJCFBody *body2)

Checks if contact should be excluded between two bodies.
Parameters:

- body1 – [in] First body to check

- body2 – [in] Second body to check

Returns:
True if contact should be excluded, false otherwise

boolcreateContactGraph()

Creates the contact graph for collision filtering.
Returns:
True if successful, false otherwise

voidcomputeKinematicHierarchy()

Computes the kinematic hierarchy for the model.

voidaddWorldGeomsAndSites(
std ::unordered_map<std ::string,pxr ::UsdStageRefPtr>stages,
std ::stringrootPath,
constImportConfig &config,
conststd ::stringinstanceableUsdPath,
)
Adds world-level geometries and sites to USD.
Parameters:

- stages – [in] Map of USD stages by name

- rootPath – [in] Root path for USD primitives

- config – [in] Import configuration settings

- instanceableUsdPath – [in] Path for instanceable USD assets

booladdVisualGeom(
pxr ::UsdStageWeakPtrstage,
pxr ::UsdPrimbodyPrim,
MJCFBody *body,
std ::stringbodyPath,
constImportConfig &config,
boolcreateGeoms,
conststd ::stringrootPrimPath,
)
Adds visual geometry primitives to USD.
Parameters:

- stage – [in] USD stage to add to

- bodyPrim – [in] Parent body primitive

- body – [in] MJCF body containing geometry

- bodyPath – [in] Path to the body

- config – [in] Import configuration settings

- createGeoms – [in] Whether to create geometry primitives

- rootPrimPath – [in] Root primitive path

Returns:
True if successful, false otherwise

voidaddVisualSites(
pxr ::UsdStageWeakPtrstage,
pxr ::UsdPrimbodyPrim,
MJCFBody *body,
std ::stringbodyPath,
constImportConfig &config,
)
Adds site primitives to USD.
Parameters:

- stage – [in] USD stage to add to

- bodyPrim – [in] Parent body primitive

- body – [in] MJCF body containing sites

- bodyPath – [in] Path to the body

- config – [in] Import configuration settings

voidAddContactFilters(pxr ::UsdStageWeakPtrstage)

Adds contact filter primitives to USD.
Parameters:
stage – [in] USD stage to add to

voidAddTendons(pxr ::UsdStageWeakPtrstage, std ::stringrootPath)

Adds tendon primitives to USD.
Parameters:

- stage – [in] USD stage to add to

- rootPath – [in] Root path for USD primitives

pxr ::GfVec3fGetLocalPos(MJCFTendon ::SpatialAttachment attachment)

Gets local position for a spatial attachment.
Parameters:
attachment – [in] Spatial attachment to compute position for

Returns:
Local position as 3D vector

voidapplyMaterial(
pxr ::UsdStageWeakPtrstage,
pxr ::UsdPrim&prim,
MJCFVisualElement *element,
)
Applies material properties to a USD primitive.
Parameters:

- stage – [in] USD stage containing the primitive

- prim – [inout] USD primitive to apply material to

- element – [in] Visual element containing material information

Public Members
std ::stringbaseDirPath

Base directory path for resolving relative file paths.

std ::stringdefaultClassName

Name of the default class for element configurations.

std ::map<std ::string,MJCFClass >classes

Map of class definitions by name.

MJCFCompiler compiler

Compiler settings for model processing.

std ::vector<MJCFBody *>bodies

Collection of all bodies in the model.

std ::vector<MJCFGeom *>collisionGeoms

Collection of collision geometry elements.

std ::vector<MJCFActuator *>actuators

Collection of actuators in the model.

std ::vector<MJCFTendon *>tendons

Collection of tendons in the model.

std ::vector<MJCFContact *>contacts

Collection of contact definitions.

std ::vector<MJCFEqualityConnect *>equalityConnects

Collection of equality constraints.

MJCFBody worldBody

World body containing global elements.

std ::map<std ::string,pxr ::UsdPhysicsRevoluteJoint>revoluteJointsMap

Map of USD revolute joints by name.

std ::map<std ::string,pxr ::UsdPhysicsPrismaticJoint>prismaticJointsMap

Map of USD prismatic joints by name.

std ::map<std ::string,pxr ::UsdPhysicsJoint>d6JointsMap

Map of USD D6 (6-DOF) joints by name.

std ::map<std ::string,pxr ::UsdPrim>geomPrimMap

Map of USD geometry primitives by name.

std ::map<std ::string,pxr ::UsdPrim>sitePrimMap

Map of USD site primitives by name.

std ::map<std ::string,pxr ::UsdPrim>siteToBodyPrim

Map from site names to their parent body primitives.

std ::map<std ::string,pxr ::UsdPrim>geomToBodyPrim

Map from geometry names to their parent body primitives.

std ::map<std ::string,pxr ::UsdPrim>bodyNameToPrim

Map from body names to their USD primitives.

std ::queue<MJCFBody *>bodyQueue

Queue for processing bodies during import.

std ::map<std ::string,int>jointToKinematicHierarchy

Map from joint names to kinematic hierarchy indices.

std ::map<std ::string,int>jointToActuatorIdx

Map from joint names to actuator indices.

std ::map<std ::string,MeshInfo >simulationMeshCache

Cache of mesh information for simulation.

std ::map<std ::string,MJCFMesh >meshes

Map of mesh definitions by name.

std ::map<std ::string,MJCFMaterial >materials

Map of material definitions by name.

std ::map<pxr ::TfToken,pxr ::SdfPath>materialPaths

Map from material tokens to USD paths.

std ::map<std ::string,pxr ::SdfPath>convertedMeshes

Map of converted mesh USD paths.

std ::map<std ::string,MJCFTexture >textures

Map of texture definitions by name.

std ::vector<ContactNode *>contactGraph

Contact graph for collision filtering.

std ::map<std ::string,MJCFBody *>nameToBody

Map from body names to body objects.

std ::map<std ::string,int>geomNameToIdx

Map from geometry names to indices.

std ::map<std ::string,std ::string>nameToUsdCollisionPrim

Map from names to USD collision primitive paths.

boolcreateBodyForFixedJoint

Whether to create separate bodies for fixed joints.

boolisLoaded=false

Whether the model has been successfully loaded.
