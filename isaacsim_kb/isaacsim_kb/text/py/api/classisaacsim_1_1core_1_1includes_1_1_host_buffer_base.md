<!-- source: py/api/classisaacsim_1_1core_1_1includes_1_1_host_buffer_base.html | title: HostBufferBase — Isaac Sim -->

# HostBufferBase
Fully qualified name: `isaacsim::core::includes::HostBufferBase`
template<typenameT>
classHostBufferBase:publicisaacsim ::core ::includes ::Buffer <T >

Host (CPU) memory buffer implementation.
Manages a buffer of memory allocated in host RAM using std::vector. Provides a simple wrapper around std::vector with the Buffer interface.
Template Parameters:
T – The data type stored in the buffer

Public Functions
inlineHostBufferBase(size_tsize=0)

Constructs a new host buffer.
Parameters:
size – [in] Initial size of the buffer in elements (default: 0)

inlinevirtualvoidresize(size_tsize)

Resizes the host buffer.
Parameters:
size – [in] New size in number of elements

inlinevirtualvoidresize(size_tsize, constT &val)

Resizes the host buffer and initializes new elements.
Parameters:

- size – [in] New size in number of elements

- val – [in] Value to initialize new elements with

inlinevirtualT *data()const

Gets a pointer to the host memory.
Returns:
Raw pointer to the host memory

inlinevirtualsize_tsize()const

Gets the current size of the buffer.
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

Public Members
std ::vector<T >m_buffer

Underlying vector storing the data.

Protected Attributes
MemoryType m_memoryType

Type of memory where the buffer resides.
