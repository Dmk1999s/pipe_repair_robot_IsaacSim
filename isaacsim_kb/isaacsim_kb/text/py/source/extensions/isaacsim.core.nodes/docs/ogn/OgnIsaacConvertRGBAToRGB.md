<!-- source: py/source/extensions/isaacsim.core.nodes/docs/ogn/OgnIsaacConvertRGBAToRGB.html | title: Isaac RGBA to RGB — Isaac Sim -->

# Isaac RGBA to RGB
Converts a RGBA image buffer into RGB

## Installation
To use this node enable isaacsim.core.nodes in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Buffer Size ( inputs:bufferSize ) | uint | Size (in bytes) of the buffer (0 if the input is a texture) | 0
Cuda Device Index ( inputs:cudaDeviceIndex ) | int | Index of the device where the data lives (-1 for host data) | -1
Data Ptr ( inputs:dataPtr ) | uint64 | Pointer to the raw rgba array data | 0
Encoding ( inputs:encoding ) | token | Encoding as a token | rgba8
Exec In ( inputs:execIn ) | execution | The input execution port | None
Format ( inputs:format ) | uint64 | Format | 0
Height ( inputs:height ) | uint | Buffer array height | 0
Width ( inputs:width ) | uint | Buffer array width | 0
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Buffer Size ( outputs:bufferSize ) | uint | Size (in bytes) of the buffer (0 if the input is a texture) | None
Cuda Device Index ( outputs:cudaDeviceIndex ) | int | Index of the device where the data lives (-1 for host data) | -1
Data Ptr ( outputs:dataPtr ) | uint64 | Pointer to the rgb buffer data | 0
Encoding ( outputs:encoding ) | token | Encoding as a token | None
Exec Out ( outputs:execOut ) | execution | Output execution triggers when conversion complete | None
Height ( outputs:height ) | uint | Buffer array height, same as input | None
Width ( outputs:width ) | uint | Buffer array width, same as input | None
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.core.nodes.IsaacConvertRGBAToRGB
Version | 1
Extension | isaacsim.core.nodes
Icon | ogn/icons/isaacsim.core.nodes.IsaacConvertRGBAToRGB.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Isaac RGBA to RGB
Categories | isaacCore
Generated Class Name | OgnIsaacConvertRGBAToRGBDatabase
Python Module | isaacsim.core.nodes
[/TABLE]
