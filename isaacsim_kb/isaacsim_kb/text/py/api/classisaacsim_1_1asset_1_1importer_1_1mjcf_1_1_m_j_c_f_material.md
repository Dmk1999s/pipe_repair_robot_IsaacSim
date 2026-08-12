<!-- source: py/api/classisaacsim_1_1asset_1_1importer_1_1mjcf_1_1_m_j_c_f_material.html | title: MJCFMaterial — Isaac Sim -->

# MJCFMaterial
Fully qualified name: `isaacsim::asset::importer::mjcf::MJCFMaterial`
classMJCFMaterial

Material definition for visual appearance.
Defines the visual appearance properties of surfaces including color, texture mapping, and lighting response characteristics. Materials can reference textures and define reflection and roughness properties.
Public Functions
inlineMJCFMaterial()

Public Members
std ::stringname

Name identifier for the material.

std ::stringtexture

Name of the texture applied to this material.

floatspecular

Specular reflection coefficient (0.0 to 1.0).

floatroughness

Surface roughness coefficient (0.0 to 1.0).

floatshininess

Shininess/metallic property (0.0 to 1.0).

Vec4 rgba

RGBA color values [red, green, blue, alpha].

boolproject_uvw

Whether to project UVW coordinates for texture mapping.
