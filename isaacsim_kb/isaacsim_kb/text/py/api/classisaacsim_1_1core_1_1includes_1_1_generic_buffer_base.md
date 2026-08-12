<!-- source: py/api/classisaacsim_1_1core_1_1includes_1_1_generic_buffer_base.html | title: GenericBufferBase — Isaac Sim -->

# GenericBufferBase
Fully qualified name: `isaacsim::core::includes::GenericBufferBase`
template<typenameT>
classGenericBufferBase:publicisaacsim ::core ::includes ::Buffer <T >

Device-generic (CPU or CUDA device) memory buffer implementation.
Manages a buffer of memory allocated in host RAM (using std::vector) or on a CUDA device. Provides functionality for:

- Memory allocation and deallocation.

- Device selection and switching (with or without data transfer).

- Memory copying between host and device.

- Fill the buffer with a constant value.

- Generate a string representation of the buffer.

Note
Uses RAII principles for automatic resource management.
Warning
Requires proper CUDA environment setup and Unified Virtual Address (UVA) space.
Template Parameters:
T – The data type stored in the buffer.

Public Functions
inlineGenericBufferBase(constsize_t&size=0, constintdevice=-1)

Construct a new device-generic (CPU or CUDA device) buffer.
Parameters:

- size – [in] Initial size of the buffer in elements.

- device – [in] CUDA device ID (higher or equal to 0) to allocate on or -1 for CPU.

inlinevirtual~GenericBufferBase()

Destructor that ensures proper cleanup of allocated memory.

inlinevirtualT *data()const

Gets a pointer to the buffer’s data.
Returns:
Pointer to the buffer’s data.

inlinevirtualsize_tsize()const

Gets the current size of the buffer.
Returns:
Number of elements in the buffer.

inlinevirtualvoidclear()

Clear the buffer.
Clear the buffer by freeing the memory and resetting the size to 0.

inlinevirtualboolsetDevice(
constintdevice=-1,
boolkeepData=false,
)
Changes the device for this buffer.
If the device changes, existing memory is freed on the old device and reallocated on the new device.
Parameters:

- device – [in] New CUDA device ID (higher or equal to 0) or -1 for CPU.

- keepData – [in] If true, the data from the old device is kept on the new device.

Returns:
True if the device was changed, false otherwise.

inlinevirtualvoidresize(size_tsize)

Resizes the device buffer (synchronous version of resizeAsync ).
Reallocates memory if the new size is different from the current size. Handles deallocation of existing memory if necessary.
Parameters:
size – [in] New size in number of elements.

Returns:
True if the size was changed, false otherwise.

inlinevirtualvoidresizeAsync(
size_tsize,
cudaStream_tcudaStream=0,
)
Resizes the device buffer asynchronously (asynchronous version of resize ).
Reallocates memory if the new size is different from the current size. Handles deallocation of existing memory if necessary.
Parameters:

- size – [in] New size in number of elements.

- cudaStream – [in] CUDA stream to use for the operation.

Returns:
True if the size was changed, false otherwise.

inlinevirtualvoidcopyTo(void*dst, size_tsize)

Copies the buffer’s data to a destination memory (synchronous version of copyToAsync ).
Note
If the specified size is greater than the buffer size, only the first `. size()` elements are copied. A warning message is logged in this case.
Parameters:

- dst – [out] Destination pointer to copy to.

- size – [in] Number of elements to copy.

inlinevirtualvoidcopyToAsync(
void*dst,
size_tsize,
cudaStream_tcudaStream=0,
)
Copies the buffer’s data to a destination memory asynchronously (asynchronous version of copyTo ).
Note
If the specified size is greater than the buffer size, only the first `. size()` elements are copied. A warning message is logged in this case.
Parameters:

- dst – [out] Destination pointer to copy to.

- size – [in] Number of elements to copy.

- cudaStream – [in] CUDA stream to use for the operation.

inlinevirtualvoidcopyFrom(constvoid*src, size_tsize)

Copies the buffer’s data from a source memory (synchronous version of copyFromAsync ).
Note
If the specified size is greater than the buffer size, only the first `. size()` elements are copied. A warning message is logged in this case.
Parameters:

- src – [in] Source pointer to copy from.

- size – [in] Number of elements to copy.

inlinevirtualvoidcopyFromAsync(
constvoid*src,
size_tsize,
cudaStream_tcudaStream=0,
)
Copies the buffer’s data from a source memory asynchronously (asynchronous version of copyFrom ).
Note
If the specified size is greater than the buffer size, only the first `. size()` elements are copied. A warning message is logged in this case.
Parameters:

- src – [in] Source pointer to copy from.

- size – [in] Number of elements to copy.

- cudaStream – [in] CUDA stream to use for the operation.

inlinevirtualboolfill(constT &value)

Fills the buffer with a constant value (synchronous version of fillAsync ).
Warning
Only data types of size 1, 2, and 4 bytes are supported. Using other data type sizes will log a warning.
Parameters:
value – [in] Value to fill the buffer with.

Returns:
True if the fill was successful, false otherwise.

inlinevirtualboolfillAsync(
constT &value,
cudaStream_tcudaStream=0,
)
Fills the buffer with a constant value asynchronously (asynchronous version of fill ).
Warning
Only data types of size 1, 2, and 4 bytes are supported. Using other data type sizes will log a warning.
Parameters:

- value – [in] Value to fill the buffer with.

- cudaStream – [in] CUDA stream to use for the operation.

Returns:
True if the fill was successful, false otherwise.

inlinestd ::stringtoString()const

Generates a string representation of the buffer.
Returns:
String representation of the buffer.

inlinesize_tsizeofType()const

Gets the size of a single element in bytes.
Returns:
Size of type T in bytes

inlinesize_tsizeInBytes()const

Gets the total size of the buffer in bytes.
Returns:
Total size of the buffer in bytes

inlineMemoryType type()const

Gets the memory type of the buffer.
Returns:
Memory type (Host or Device)

Protected Attributes
MemoryType m_memoryType

Type of memory where the buffer resides.
