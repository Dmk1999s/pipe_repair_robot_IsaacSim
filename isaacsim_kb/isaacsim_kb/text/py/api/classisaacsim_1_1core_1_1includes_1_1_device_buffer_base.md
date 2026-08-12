<!-- source: py/api/classisaacsim_1_1core_1_1includes_1_1_device_buffer_base.html | title: DeviceBufferBase — Isaac Sim -->

# DeviceBufferBase
Fully qualified name: `isaacsim::core::includes::DeviceBufferBase`
template<typenameT>
classDeviceBufferBase:publicisaacsim ::core ::includes ::Buffer <T >

CUDA device (GPU) memory buffer implementation.
Manages a buffer of memory allocated on a CUDA device. Provides functionality for:

- Memory allocation and deallocation

- Device selection and switching

- Memory copying between host and device

- Debug printing of buffer contents

Note
Uses RAII principles for automatic resource management
Warning
Requires proper CUDA environment setup
Template Parameters:
T – The data type stored in the buffer

Public Functions
inlineDeviceBufferBase(constsize_t&size=0, constintdevice=-1)

Constructs a new device buffer.
Parameters:

- size – [in] Initial size of the buffer in elements (default: 0)

- device – [in] CUDA device ID to allocate on (default: -1 for CPU)

inlinevirtual~DeviceBufferBase()

Destructor that ensures proper cleanup of device memory.

inlinevirtualvoidsetDevice(constintdevice=-1)

Changes the CUDA device for this buffer.
If the device changes, existing memory is freed on the old device and reallocated on the new device.
Parameters:
device – [in] New CUDA device ID (-1 for CPU)

inlinevirtualvoidresize(size_tsize)

Resizes the device buffer.
Reallocates memory if the new size is different from the current size. Handles deallocation of existing memory if necessary.
Parameters:
size – [in] New size in number of elements

inlinevirtualvoidresizeAsync(
size_tsize,
cudaStream_tcudaStream=0,
)
Asynchronously resizes the device buffer.
Reallocates memory if the new size is different from the current size. Handles deallocation of existing memory if necessary.
Parameters:

- size – [in] New size in number of elements

- cudaStream – [in] CUDA stream to use for asynchronous operation

inlinevirtualT *data()const

Gets a pointer to the device memory.
Returns:
Raw pointer to the device memory

inlinevirtualsize_tsize()const

Gets the current size of the buffer.
Returns:
Number of elements in the buffer

inlinevirtualvoidcopy(
constvoid*src,
size_tsize,
enumcudaMemcpyKindkind=cudaMemcpyDeviceToHost,
)
Synchronously copies data to the device buffer.
Parameters:

- src – [in] Source pointer to copy from

- size – [in] Number of elements to copy

- kind – [in] Type of memory copy operation

inlinevirtualvoidcopyAsync(
constvoid*src,
size_tsize,
enumcudaMemcpyKindkind=cudaMemcpyDeviceToHost,
cudaStream_tcudaStream=0,
)
Asynchronously copies data to the device buffer.
Parameters:

- src – [in] Source pointer to copy from

- size – [in] Number of elements to copy

- kind – [in] Type of memory copy operation

- cudaStream – [in] CUDA stream to use for the copy operation

inlinevoiddebugPrint(
conststd ::string&start,
conststd ::string&end,
)
Prints the buffer contents for debugging.
Parameters:

- start – [in] String to print before the buffer contents

- end – [in] String to print after the buffer contents

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
