<!-- source: py/api/classisaacsim_1_1asset_1_1importer_1_1mjcf_1_1_m_j_c_f_compiler.html | title: MJCFCompiler — Isaac Sim -->

# MJCFCompiler
Fully qualified name: `isaacsim::asset::importer::mjcf::MJCFCompiler`
classMJCFCompiler

Compiler settings that affect how the MJCF model is processed.
Contains flags and settings that control various aspects of model compilation including angle units, coordinate systems, automatic limit generation, and file path specifications for assets.
Public Functions
inlineMJCFCompiler()

Public Members
boolangleInRad

Whether angles are specified in radians (true) or degrees (false).

boolinertiafromgeom

Whether to automatically compute inertia from geometry.

boolcoordinateInLocal

Whether coordinates are in local frame (true) or global frame (false).

boolautolimits

Whether to automatically generate joint limits.

std ::stringeulerseq

Euler angle sequence for rotations (e.g., “xyz”, “zyx”).

std ::stringmeshDir

Directory path for mesh files.

std ::stringtextureDir

Directory path for texture files.
