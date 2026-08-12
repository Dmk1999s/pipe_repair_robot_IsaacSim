<!-- source: py/api/structisaacsim_1_1asset_1_1importer_1_1mjcf_1_1_mjcf.html | title: Mjcf — Isaac Sim -->

# Mjcf
Fully qualified name: `isaacsim::asset::importer::mjcf::Mjcf`
structMjcf

Interface for MJCF file import functionality.
This structure defines the plugin interface for importing MJCF (MuJoCo XML) files and converting them to USD format for use in Isaac Sim.
Public Members
void(*createAssetFromMJCF)(constchar*fileName,constchar*primName,ImportConfig &config,conststd ::string&stage_identifier)

Function pointer for creating assets from MJCF files.
This function loads an MJCF file and creates corresponding USD assets based on the provided configuration settings.
Param fileName:
[in] Path to the MJCF file to import

Param primName:
[in] Name for the created USD primitive

Param config:
[inout] Configuration settings for the import process

Param stage_identifier:
[in] Identifier for the target USD stage
