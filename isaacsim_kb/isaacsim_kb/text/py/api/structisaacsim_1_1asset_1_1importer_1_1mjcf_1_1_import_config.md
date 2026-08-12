<!-- source: py/api/structisaacsim_1_1asset_1_1importer_1_1mjcf_1_1_import_config.html | title: ImportConfig — Isaac Sim -->

# ImportConfig
Fully qualified name: `isaacsim::asset::importer::mjcf::ImportConfig`
structImportConfig

Configuration settings for importing MJCF files.
This structure contains various options and parameters that control how MJCF files are imported and converted into USD format. It includes physics settings, visual options, and optimization flags.
Public Members
boolmergeFixedJoints=false

Whether to merge fixed joints during import.

boolconvexDecomp=false

Whether to perform convex decomposition on meshes.

boolimportInertiaTensor=false

Whether to import inertia tensor information.

boolfixBase=true

Whether to fix the base of the imported model.

boolselfCollision=false

Whether to enable self-collision detection.

floatdensity=1000

Default density used for objects without mass/inertia in kg/m³.

floatdefaultDriveStrength=100000

Default drive strength value for joints.

floatdistanceScale=1.0f

Scaling factor for distances in the imported model.

boolcreatePhysicsScene=true

Whether to create a physics scene during import.

boolmakeDefaultPrim=true

Whether to make the imported model the default prim.

boolcreateBodyForFixedJoint=true

Whether to create bodies for fixed joints.

booloverrideCoM=false

Whether to override center of mass calculations.

booloverrideInertia=false

Whether to override inertia calculations.

boolvisualizeCollisionGeoms=false

Whether to visualize collision geometries.

boolimportSites=true

Whether to import MJCF site elements.

boolmakeInstanceable=false

Whether to make meshes instanceable for optimization.

std ::stringinstanceableMeshUsdPath="./instanceable_meshes.usd"

USD file path for instanceable meshes.
