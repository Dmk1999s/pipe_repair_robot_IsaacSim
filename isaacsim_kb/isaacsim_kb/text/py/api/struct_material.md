<!-- source: py/api/struct_material.html | title: Material — Isaac Sim -->

# Material
structMaterial

OBJ-style material definition with PBR properties.
Direct representation of .obj style material with ambient, diffuse, specular components and modern PBR extensions for metallic workflow.
Public Members
std ::stringname

Name identifier for the material.

Vec3 Ka

Ambient color component (RGB).

Vec3 Kd

Diffuse color component (RGB).

Vec3 Ks

Specular color component (RGB).

Vec3 emissive

Emissive color component (RGB).

floatNs=50.0f

Specular exponent for shininess calculation.

floatmetallic=0.0f

Metallic factor for PBR rendering (0.0 = dielectric, 1.0 = metallic).

floatspecular=0.0f

Specular reflectance factor.

std ::stringmapKd=""

Diffuse texture map file path.

std ::stringmapKs=""

Specular/shininess texture map file path.

std ::stringmapBump=""

Normal/bump texture map file path.

std ::stringmapEnv=""

Environment/emissive texture map file path.

std ::stringmapMetallic=""

Metallic texture map file path.

boolhasDiffuse=false

Whether the material has a diffuse texture.

boolhasSpecular=false

Whether the material has a specular texture.

boolhasMetallic=false

Whether the material has a metallic texture.

boolhasEmissive=false

Whether the material has an emissive texture.

boolhasShininess=false

Whether the material has a shininess texture.
