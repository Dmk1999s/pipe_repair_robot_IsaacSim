<!-- source: importer_exporter/ext_omni_exporter_urdf.html | title: USD to URDF Exporter Extension — Isaac Sim Documentation -->

# USD to URDF Exporter Extension

## Overview
The USD to URDF Exporter is a tool to convert a USD stage or file to a URDF file. A user just needs to open a stage with the desired USD they want to export, and provide the path to directory where the new URDF file will be saved, or the path to the new URDF file directly.
To enable this extension, open the Extension Manager window by navigating to Window > Extensions, and enable `isaacsim.asset.exporter.urdf`.
Once enabled, the USD to Exporter is accessed by going to the top Menu Bar and clicking File > Export to URDF. Mesh files are saved by default to a meshes directory, which is placed in the same directory as the new URDF file. Additional options are available that allow customization of some parts of the conversion.

## Parameters
Output File/Directory
The file path for the new URDF file. The file path conventionally ends with the extension `.urdf`.
Or a directory path where new URDF file will be saved. The new URDF file will have the same name as the USD.
Mesh Directory Path
The directory where the meshes will be saved for the URDF (defaults to the same directory as the as where the URDF file is saved).
Mesh Path Prefix
A prefix to apply to each mesh filename. For example, to set the mesh file paths to valid URI with the file scheme, set the mesh path prefix to `file://`.
Root Prim Path
The root prim within the USD stage of the kinematic tree to be exported to URDF. The default is the default prim of the USD file.
Visualize Collisions
If set, the collision meshes are included as visual meshes in the resulting URDF.

## Notes

- URDF files do not support kinematic loops. If the USD file has a kinematic loop, the converter will fail. Try manually break the loop first.

- URDF files require a parent link and a child link when defining a joint, they do not allow having a joint with a single link. If there are such joints in the USD file, for example, an unattached end-effector, the converter will likely produce inconsistent joint transforms and fail.
