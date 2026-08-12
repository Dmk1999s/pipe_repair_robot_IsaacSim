<!-- source: py/api/classisaacsim_1_1core_1_1includes_1_1_buffer.html | title: Buffer — Isaac Sim -->

# Buffer
Fully qualified name: `isaacsim::core::includes::Buffer`
template<typenameT>
classBuffer

Abstract base class for memory buffer management.
Provides a common interface for managing memory buffers, whether they reside in host (CPU) or device (GPU) memory. This class defines the basic operations that all buffer implementations must support.
Note
All derived classes must implement resize() , data() , and size() functions
Template Parameters:
T – The data type stored in the buffer

Subclassed by isaacsim::core::includes::GenericBufferBase< float > , isaacsim::core::includes::DeviceBufferBase< T > , isaacsim::core::includes::GenericBufferBase< T > , isaacsim::core::includes::HostBufferBase< T >
Public Functions
virtual~Buffer()=default

Virtual destructor for proper cleanup of derived classes.

virtualvoidresize(size_tsize)=0

Resizes the buffer to hold the specified number of elements.
Parameters:
size – [in] The new size of the buffer in number of elements

virtualT *data()const=0

Gets a pointer to the buffer’s data.
Returns:
Pointer to the buffer’s data

virtualsize_tsize()const=0

Gets the number of elements in the buffer.
Returns:
Number of elements in the buffer

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
