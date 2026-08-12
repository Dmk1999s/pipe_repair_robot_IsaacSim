<!-- source: py/api/classisaacsim_1_1core_1_1includes_1_1_scoped_cuda_texture_object.html | title: ScopedCudaTextureObject — Isaac Sim -->

# ScopedCudaTextureObject
Fully qualified name: `isaacsim::core::includes::ScopedCudaTextureObject`
classScopedCudaTextureObject

RAII wrapper for CUDA texture object management.
Manages the lifecycle of a CUDA texture object, including creation and cleanup. Automatically handles:

- Texture object creation from mipmapped arrays

- Resource and texture descriptor setup

- Automatic cleanup on destruction

Note
Uses RAII pattern to ensure texture resources are properly freed
Warning
Requires valid CUDA context when constructed
Public Functions
inlineScopedCudaTextureObject(
cudaMipmappedArray_tmmarr,
intmipLevel=0,
)
Constructs a texture object from a mipmapped array.
Creates a texture object with specified properties:

- Clamp address mode

- Point filtering

- Element-type read mode

- Normalized coordinates

Note
Fails gracefully if input array is invalid
Warning
Ensure mipmapped array remains valid during object lifetime
Parameters:

- mmarr – [in] CUDA mipmapped array handle

- mipLevel – [in] Mipmap level to use (default: 0)

inline~ScopedCudaTextureObject()

Destructor that cleans up the texture object.
Automatically destroys the texture object if it was successfully created.

inlineoperatorcudaTextureObject_t&()

Implicit conversion operator to texture object handle.
Returns:
Reference to the underlying CUDA texture object
