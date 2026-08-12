<!-- source: py/api/namespace_isaacsim__asset__importer__urdf.html | title: urdf — Isaac Sim -->

# urdf
Fully qualified name: `isaacsim::asset::importer::urdf`
namespaceurdf

## Classes
KinematicChain
Represents the kinematic chain of a robot as a tree structure.

UrdfImporter
URDF (Unified Robot Description Format) importer for converting robot descriptions to USD format.

## Enumerations
UrdfGeometryType
UrdfJointDriveType
UrdfJointTargetType
UrdfJointType
UrdfNormalSubdivisionScheme
UrdfSensorType

## Functions
Vec3Diagonalize (const Matrix33 &m, Quat &massFrame)
std::stringGetNewSdfPathString (pxr::UsdStageWeakPtr stage, std::string path, int nameClashNum=-1)
boolIsUsdFile (const std::string &filename)
pxr::SdfPathSimpleImport (pxr::UsdStageRefPtr usdStage, const std::string &path, const std::string &meshPath, std::map< pxr::TfToken, pxr::SdfPath > &meshList, std::map< pxr::TfToken, pxr::SdfPath > &materialList, const pxr::SdfPath &rootPath)
booladdVisualMeshToCollision (UrdfRobot &robot)
boolcollapseFixedJoints (UrdfRobot &robot)
floatcomputeSimpleStiffness (const UrdfRobot &robot, std::string joint, float naturalFrequency)
boolfindRootLink (const std::map< std::string, UrdfLink > &urdfLinks, const std::map< std::string, UrdfJoint > &urdfJoints, std::string &rootLinkName)
QuatindexedRotation (int axis, float s, float c)
voidinertiaToUrdf (const Matrix33 &inertia, UrdfInertia &urdfInertia)
voidmergeFixedChildLinks (const KinematicChain::Node &parentNode, UrdfRobot &robot)
boolparseAxis (const tinyxml2::XMLElement &element, UrdfAxis &axis)
boolparseDynamics (const tinyxml2::XMLElement &element, UrdfDynamics &dynamics)
boolparseFixedFrames (const tinyxml2::XMLElement &element, std::map< std::string, UrdfLink > &links)
boolparseGeometry (const tinyxml2::XMLElement &element, UrdfGeometry &geometry)
boolparseInertia (const tinyxml2::XMLElement &element, UrdfInertia &inertia)
boolparseInertial (const tinyxml2::XMLElement &element, UrdfInertial &inertial)
boolparseJointType (const std::string &str, UrdfJointType &type)
boolparseJoints (const tinyxml2::XMLElement &root, std::map< std::string, UrdfJoint > &urdfJoints)
boolparseLimit (const tinyxml2::XMLElement &element, UrdfLimit &limit)
boolparseLinks (const tinyxml2::XMLElement &root, std::map< std::string, UrdfLink > &urdfLinks)
boolparseLoopJoints (const tinyxml2::XMLElement &element, std::map< std::string, UrdfLoopJoint > &loopJoints)
boolparseMass (const tinyxml2::XMLElement &element, float &mass)
boolparseMaterial (const tinyxml2::XMLElement &element, UrdfMaterial &material)
boolparseMaterials (const tinyxml2::XMLElement &root, std::map< std::string, UrdfMaterial > &urdfMaterials)
boolparseOrigin (const tinyxml2::XMLElement &element, Transform &origin)
boolparseSensors (const tinyxml2::XMLElement &root, std::map< std::string, UrdfLink > &urdfLinks)
boolparseUrdf (const std::string &urdfPackagePath, const std::string &urdfFileRelativeToPackage, UrdfRobot &urdfRobot)
boolparseUrdfString (const std::string &urdf_str, UrdfRobot &urdfRobot)
std::stringresolveXrefPath (const std::string &assetRoot, const std::string &urdfPath, const std::string &xrefpath)
Vec3urdfAxisToVec (const UrdfAxis &axis)
voidurdfToInertia (const UrdfInertia &urdfInertia, Matrix33 &inertia)

## Structs
ImportConfig
Configuration parameters for URDF import operations.

Urdf
Interface for URDF parsing and import operations.

UrdfAxis
Joint axis definition for URDF joints.

UrdfCamera
Camera sensor configuration extending base sensor.

UrdfCollision
Collision element definition for URDF links.

UrdfColor
RGBA color specification for URDF materials.

UrdfContact
Contact sensor configuration.

UrdfDynamics
Joint dynamics properties for URDF joints.

UrdfForce
Force sensor configuration.

UrdfGeometry
Geometric shape definition for URDF visual and collision elements.

UrdfGps
GPS sensor configuration.

UrdfImu
Inertial measurement unit sensor configuration.

UrdfInertia
Inertia tensor components for a rigid body.

UrdfInertial
Inertial properties of a URDF link.

UrdfJoint
Joint definition connecting two links in URDF robot model.

UrdfJointDrive
Joint drive configuration for actuated joints.

UrdfJointMimic
Joint mimic configuration for coupled joint motion.

UrdfLimit
Joint motion limits for URDF joints.

UrdfLink
Link definition in URDF robot model.

UrdfLoopJoint
Loop joint definition for closed kinematic chains.

UrdfMagnetometer
Magnetometer sensor configuration.

UrdfMaterial
Material definition for URDF visual elements.

UrdfNoise
Noise characteristics for sensor measurements.

UrdfRay
Ray-based sensor configuration for lidar/laser scanners.

UrdfRayDim
Ray dimension configuration for lidar sensors.

UrdfRfid
RFID reader sensor configuration.

UrdfRfidTag
RFID tag sensor configuration.

UrdfRobot
Complete URDF robot model definition.

UrdfSensor
Base sensor definition for URDF sensors.

UrdfSonar
Sonar sensor configuration.

UrdfVisual
Visual element definition for URDF links.
