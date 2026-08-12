<!-- source: py/api/structisaacsim_1_1asset_1_1importer_1_1urdf_1_1_urdf.html | title: Urdf — Isaac Sim -->

# Urdf
Fully qualified name: `isaacsim::asset::importer::urdf::Urdf`
structUrdf

Interface for URDF parsing and import operations.
This structure defines the interface for URDF (Unified Robot Description Format) operations including parsing URDF files/strings and importing robots into the simulation environment.
Public Members
UrdfRobot (*parseUrdf)(conststd ::string&assetRoot,conststd ::string&assetName,ImportConfig &importConfig)

Parses a URDF file into a UrdfRobot data structure.
Param assetRoot:
[in] Root directory path for assets

Param assetName:
[in] Name of the URDF asset file

Param importConfig:
[inout] Configuration parameters for import

Return:
UrdfRobot data structure containing parsed robot information

UrdfRobot (*parseUrdfString)(conststd ::string&urdf_str,ImportConfig &importConfig)

Parses a URDF data string into a UrdfRobot data structure.
Param urdf_str:
[in] URDF content as string

Param importConfig:
[inout] Configuration parameters for import

Return:
UrdfRobot data structure containing parsed robot information

float(*computeJointNaturalStiffess)(constUrdfRobot &robot,std ::stringjoint,floatnaturalFrequency)

Computes natural stiffness for a joint.
Param robot:
[in] Robot data structure

Param joint:
[in] Name of the joint

Param naturalFrequency:
[in] Desired natural frequency in Hz

Return:
Computed natural stiffness value

std ::string(*importRobot)(conststd ::string&assetRoot,conststd ::string&assetName,constUrdfRobot &robot,ImportConfig &importConfig,conststd ::string&stage,constboolgetArticulationRoot)

Imports a UrdfRobot into the stage.
Param assetRoot:
[in] Root directory path for assets

Param assetName:
[in] Name of the asset

Param robot:
[in] Robot data structure to import

Param importConfig:
[inout] Configuration parameters for import

Param stage:
[in] Stage identifier where robot will be imported

Param getArticulationRoot:
[in] Whether to get the articulation root

Return:
Path to the imported robot in the stage

pybind11::dict(*getKinematicChain)(constUrdfRobot &robot)

Gets the kinematic chain of the robot.
Param robot:
[in] Robot data structure

Return:
Python dictionary containing kinematic chain information
