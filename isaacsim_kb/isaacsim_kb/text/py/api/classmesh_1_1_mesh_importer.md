<!-- source: py/api/classmesh_1_1_mesh_importer.html | title: MeshImporter — Isaac Sim -->

# MeshImporter
Fully qualified name: `mesh::MeshImporter`
classMeshImporter

Utility class for importing and converting mesh assets to USD format.
Handles the import pipeline for various mesh formats, converting them to USD geometry with materials and textures. Manages asset conversion using the Omni Converter and handles material binding and mesh optimization.
Public Functions
inlineMeshImporter()

Default constructor for MeshImporter .

inlinestd ::stringresolveMeshPath(conststd ::string&filePath)

Resolves a mesh file path to its absolute location.
Parameters:
filePath – [in] Relative or absolute path to mesh file

Returns:
Resolved absolute path to mesh file

inlinepxr ::TfTokengetMaterialToken(
pxr ::UsdStageWeakPtrstage,
constpxr ::SdfPath&materialPath,
)
Gets a unique token for a material based on its properties.
Parameters:

- stage – [in] USD stage containing the material

- materialPath – [in] Path to the material primitive

Returns:
Unique token identifying the material properties

inlinevoidmoveAndBindMaterial(
constpxr ::UsdStageRefPtr&sourceStage,
constpxr ::UsdStageRefPtr&dstStage,
constpxr ::SdfPath&rootPath,
constpxr ::SdfPath&sourcePath,
constpxr ::SdfPath&dstPath,
std ::map<pxr ::TfToken,pxr ::SdfPath>&materialPaths,
)
Moves and binds a material from source stage to destination stage.
Parameters:

- sourceStage – [in] Source USD stage containing the material

- dstStage – [in] Destination USD stage to move material to

- rootPath – [in] Root path in destination stage

- sourcePath – [in] Path to source primitive with material binding

- dstPath – [in] Path to destination primitive for material binding

- materialPaths – [inout] Map tracking material paths to avoid duplicates

inlinevoidmoveMeshAndMaterials(
constpxr ::UsdStageRefPtr&sourceStage,
constpxr ::UsdStageRefPtr&dstStage,
constpxr ::SdfPath&rootPath,
constpxr ::SdfPath&meshPath,
constpxr ::SdfPath&targetPrimPath,
std ::map<pxr ::TfToken,pxr ::SdfPath>&materialPaths,
)
Moves mesh geometry and associated materials between USD stages.
Parameters:

- sourceStage – [in] Source USD stage containing the mesh

- dstStage – [in] Destination USD stage to move mesh to

- rootPath – [in] Root path in destination stage

- meshPath – [in] Path to source mesh primitive

- targetPrimPath – [in] Path where new mesh should be created

- materialPaths – [inout] Map tracking material paths to avoid duplicates

inlinepxr ::SdfPathwaitForConverter(
OmniConverterFuture*future,
pxr ::UsdStageRefPtrusdStage,
conststd ::string&mesh_usd_path,
conststd ::string&meshStagePath,
constpxr ::SdfPath&rootPath,
std ::map<pxr ::TfToken,pxr ::SdfPath>&materialPaths,
)
Waits for asset conversion to complete and processes the results.
Parameters:

- future – [in] Future object tracking conversion progress

- usdStage – [in] USD stage to add converted mesh to

- mesh_usd_path – [in] Path to converted USD mesh file

- meshStagePath – [in] Path in stage where mesh should be placed

- rootPath – [in] Root path for organizing assets

- materialPaths – [inout] Map tracking material paths to avoid duplicates

Returns:
Path to the imported mesh primitive in the stage

inlinevoidimportMesh(
Mesh *mesh,
std ::stringrelativeMeshPath,
constVec3 &scale,
boolflip=false,
)
Imports a mesh from file using the Omni Converter.
Parameters:

- mesh – [inout]Mesh object to store conversion results

- relativeMeshPath – [in] Relative path to source mesh file

- scale – [in] Scale factors to apply during conversion

- flip – [in] Whether to flip normals during conversion (default: false)
