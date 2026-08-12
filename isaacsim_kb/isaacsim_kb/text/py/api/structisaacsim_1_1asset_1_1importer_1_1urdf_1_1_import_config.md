<!-- source: py/api/structisaacsim_1_1asset_1_1importer_1_1urdf_1_1_import_config.html | title: ImportConfig — Isaac Sim -->

# ImportConfig
Fully qualified name: `isaacsim::asset::importer::urdf::ImportConfig`
structImportConfig

Configuration parameters for URDF import operations.
This structure contains various options and settings that control how URDF files are parsed and imported into the simulation environment. It allows customization of joint merging, physics properties, scaling, and other import behaviors.
Public Members
boolmergeFixedJoints=true

Whether to merge fixed joints during import.

boolreplaceCylindersWithCapsules=false

Whether to replace cylinder geometries with capsule geometries.

boolconvexDecomp=false

Whether to perform convex decomposition on meshes.

boolimportInertiaTensor=true

Whether to import inertia tensor information.

boolfixBase=true

Whether to fix the base of the robot (make it static)

boolselfCollision=false

Whether to enable self-collision detection.

floatdensity=0.0f

Default density for objects without mass/inertia (0 to auto-compute)

UrdfJointTargetType defaultDriveType=UrdfJointTargetType ::POSITION

Default drive type for joints.

floatdefaultDriveStrength=1e3f

Default drive strength for joint actuators.

floatdefaultPositionDriveDamping=1e2f

Default damping for position-driven joints.

floatdistanceScale=1.0f

Scale factor for all distance measurements.

UrdfAxis upVector={0.0f,0.0f,1.0f}

Up vector direction for the coordinate system.

boolcreatePhysicsScene=false

Whether to create a physics scene during import.

boolmakeDefaultPrim=false

Whether to make the imported model the default prim.

UrdfNormalSubdivisionScheme subdivisionScheme=UrdfNormalSubdivisionScheme ::BILINEAR

Subdivision scheme for normal computation.

boolcollisionFromVisuals=false

Whether to create collision geometry from visual geometry when missing.

boolparseMimic=true

Whether to parse mimic joint relationships.

booloverrideJointDynamics=false

Whether to override joint dynamics parameters.
