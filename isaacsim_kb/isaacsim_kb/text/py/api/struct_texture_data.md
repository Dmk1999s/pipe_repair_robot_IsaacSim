<!-- source: py/api/struct_texture_data.html | title: TextureData — Isaac Sim -->

# TextureData
structTextureData

Container for texture image data and metadata.
This structure holds texture information including dimensions, pixel data, and format. Can represent both compressed and uncompressed texture data.
Public Members
intwidth

Width of texture in pixels.
If height is 0, width equals buffer size.

intheight

Height of texture in pixels.
If 0, buffer contains compressed image data.

std ::vector<uint8_t>buffer

Pixel data buffer.
R8G8B8A8 format if uncompressed.

std ::stringformat

Format string for compressed data (e.g., “png”, “jpg”, “bmp”).
