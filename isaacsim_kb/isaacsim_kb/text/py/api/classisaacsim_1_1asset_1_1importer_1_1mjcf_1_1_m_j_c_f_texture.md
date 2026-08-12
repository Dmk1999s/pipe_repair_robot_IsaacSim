<!-- source: py/api/classisaacsim_1_1asset_1_1importer_1_1mjcf_1_1_m_j_c_f_texture.html | title: MJCFTexture — Isaac Sim -->

# MJCFTexture
Fully qualified name: `isaacsim::asset::importer::mjcf::MJCFTexture`
classMJCFTexture

Texture asset definition for materials.
Defines a texture that can be applied to materials for visual rendering. Supports various texture types including file-based textures and procedurally generated grid patterns.
Public Functions
inlineMJCFTexture()

Public Members
std ::stringname

Name identifier for the texture.

std ::stringfilename

File path to the texture image.

std ::stringgridsize

Grid size specification for procedural textures.

std ::stringgridlayout

Grid layout pattern for procedural textures.

std ::stringtype

Type of texture (e.g., “cube”, “sphere”, “cylinder”).
