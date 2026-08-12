<!-- source: importer_exporter/formats.html | title: Formats — Isaac Sim Documentation -->

# Formats
The standard format used in Omniverse is USD for scenes and MDL for materials. You need to convert your content to be usable in Omniverse, if coming from external applications. Omniverse offers several ways to manage such content.

## Asset Converter
Apps in Omniverse are loaded with the Asset Converter extension. With it, you can convert models into USD using the Asset Converter service. Below is a list of formats it can convert to USD.

[TABLE]
Format | Name | Description
.fbx | Autodesk FBX Interchange File | Common 3D model saved in the Autodesk Filmbox format
.obj | Object File Format | Common 3D Model format
.gltf | GL Transmission Format File | Common 3D Scene Description
[/TABLE]

## Materials
NVIDIA has developed a custom schema in USD to represent material assignments and specify material parameters. In Omniverse, these specialized USD’s get an extension change to `.MDL` signifying that it is represented in NVIDIA’s open-source MDL (Material Definition Language).
