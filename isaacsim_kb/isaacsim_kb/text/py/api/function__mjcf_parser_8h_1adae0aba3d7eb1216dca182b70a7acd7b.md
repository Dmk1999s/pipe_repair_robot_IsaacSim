<!-- source: py/api/function__mjcf_parser_8h_1adae0aba3d7eb1216dca182b70a7acd7b.html | title: LoadGlobals — Isaac Sim -->

# LoadGlobals
Fully qualified name: `isaacsim::asset::importer::mjcf::LoadGlobals`
voidisaacsim ::asset ::importer ::mjcf ::LoadGlobals(
tinyxml2::XMLElement*root,
std ::string&defaultClassName,
conststd ::string&baseDirPath,
MJCFBody &worldBody,
std ::vector<MJCFBody *>&bodies,
std ::vector<MJCFActuator *>&actuators,
std ::vector<MJCFTendon *>&tendons,
std ::vector<MJCFContact *>&contacts,
std ::vector<MJCFEqualityConnect *>&equalityConnects,
std ::map<std ::string,MeshInfo >&simulationMeshCache,
std ::map<std ::string,MJCFMesh >&meshes,
std ::map<std ::string,MJCFMaterial >&materials,
std ::map<std ::string,MJCFTexture >&textures,
MJCFCompiler &compiler,
std ::map<std ::string,MJCFClass >&classes,
std ::map<std ::string,int>&jointToActuatorIdx,
ImportConfig &config,
)
