<!-- source: py/api/class_i_p_c_buffer_manager.html | title: IPCBufferManager — Isaac Sim -->

# IPCBufferManager
classIPCBufferManager

Manages CUDA device memory buffers for inter-process communication (IPC).
This class creates and manages a pool of CUDA device memory buffers that can be shared between processes using POSIX file descriptors. It handles the allocation, mapping, and access control for these buffers, as well as cycling through them for use in communication scenarios.
Public Functions
IPCBufferManager()=default

inlineIPCBufferManager(size_tsize, size_tbufferStep)

Constructor that creates device memory buffers and exports them to file descriptors.
Allocates a specified number of CUDA device memory buffers and exports them as POSIX file descriptors for inter-process communication. The buffers are set up with read/write access permissions.
Parameters:

- size – [in] Number of buffers to create in the pool.

- bufferStep – [in] Size of each buffer in bytes.

Throws:
std ::runtime_error – If CUDA memory allocation granularity cannot be determined or is zero.

inline~IPCBufferManager()

Destructor.
Frees all allocated device memory and resources when the buffer manager is destroyed. This includes releasing all CUDA memory allocations and unmapping virtual address ranges.

inlinevoidnext()

Advances to the next available device memory buffer in the pool.
Increments the current buffer index, wrapping around to the beginning when the end of the buffer pool is reached. This implements a circular buffer pattern for cycling through available memory blocks.

inlineCUdeviceptrgetCurBufferPtr()

Retrieves the device pointer to the current memory buffer.
Returns the CUDA device pointer for the currently selected buffer in the pool, which can be used for CUDA operations.
Returns:
CUdeviceptr Device pointer to the current buffer.

inlinestd ::vector<int>&getCurIpcMemHandle()

Retrieves the IPC handle for the current memory buffer.
Returns a reference to the vector containing the process ID and file descriptor for the currently selected buffer, which can be used for inter-process communication.
Returns:
std::vector<int>& Reference to the vector containing the process ID and file descriptor.
