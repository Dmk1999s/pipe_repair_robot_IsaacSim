<!-- source: py/api/classisaacsim_1_1core_1_1includes_1_1_scoped_device.html | title: ScopedDevice — Isaac Sim -->

# ScopedDevice
Fully qualified name: `isaacsim::core::includes::ScopedDevice`
classScopedDevice

RAII wrapper for CUDA device context management.
Provides automatic CUDA device context switching and restoration. When constructed, switches to the specified device (if different from current). When destroyed, restores the previous device context.
Key features:

- Automatic device context management

- Exception-safe device restoration

- Support for CPU-only mode (-1 device)

- Thread-safe device switching

Note
Uses RAII pattern to ensure device context is always properly restored
Warning
CUDA API calls must be error-checked for proper device management
Public Functions
inlineScopedDevice(constintdevice=-1)

Constructs a scoped device context manager.
Saves the current device and switches to the specified device if different. If device is -1 or CUDA is unavailable, operates in CPU-only mode.
Note
Device -1 indicates CPU-only mode
Warning
Ensure CUDA runtime is initialized before using this class
Parameters:
device – [in] CUDA device ID to switch to (-1 for CPU mode)

inline~ScopedDevice()

Destructor that restores the previous device context.
Automatically switches back to the original device if a switch was performed. Ensures device context is restored even if exceptions occur.
