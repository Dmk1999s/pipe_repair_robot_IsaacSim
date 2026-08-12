<!-- source: py/api/classisaacsim_1_1asset_1_1importer_1_1urdf_1_1_urdf_importer.html | title: UrdfImporter — Isaac Sim -->

# UrdfImporter
Fully qualified name: `isaacsim::asset::importer::urdf::UrdfImporter`
classUrdfImporter

URDF (Unified Robot Description Format) importer for converting robot descriptions to USD format.
This class handles the import and conversion of URDF robot descriptions into USD (Universal Scene Description) format for use in Isaac Sim. It processes URDF files containing robot geometry, kinematics, dynamics, and material properties, creating equivalent USD representations suitable for physics simulation.
The importer supports:

- Link geometry conversion from meshes and primitives

- Joint definitions with proper kinematic constraints

- Material properties and textures

- Physics properties including mass, inertia, and collision shapes

- Loop closures for closed kinematic chains

Note
The importer requires a valid URDF file and asset root directory containing referenced mesh files.
Public Functions
inlineUrdfImporter(
conststd ::string&assetRoot,
conststd ::string&urdfPath,
constImportConfig &options,
)
Constructs a UrdfImporter with the specified configuration.
Initializes the URDF importer with paths to the robot description and import settings. The asset root should contain all mesh and texture files referenced by the URDF.
Parameters:

- assetRoot – [in] Root directory path containing robot assets (meshes, textures)

- urdfPath – [in] Full path to the URDF file to import

- options – [in] Import configuration settings controlling conversion behavior

Pre:
assetRoot must be a valid directory path accessible for reading

Pre:
urdfPath must be a valid URDF file path

UrdfRobot createAsset()

Creates and populates a robot asset from the URDF description.
Parses the URDF file and converts it into a UrdfRobot data structure containing all robot components including links, joints, materials, and kinematic chains. This method performs the core conversion logic from URDF to internal representation.
Throws:

- std ::runtime_error – If URDF file cannot be parsed or contains invalid data

- std ::invalid_argument – If required mesh files are not found in asset root

Returns:
UrdfRobot Complete robot data structure with parsed URDF content

Pre:
URDF file must be accessible and contain valid robot description

Post:
Returns fully populated robot structure ready for USD stage creation

std ::stringaddToStage(
std ::unordered_map<std ::string,pxr ::UsdStageRefPtr>stageMap,
constUrdfRobot &robot,
constboolgetArticulationRoot,
)
Adds the robot to USD stages for simulation.
Parameters:

- stageMap – [inout] Map of stage names to USD stage references

- robot – [in] Robot data structure to add to stages

- getArticulationRoot – [in] Whether to get the articulation root

Returns:
Path to the created robot in the USD stage
