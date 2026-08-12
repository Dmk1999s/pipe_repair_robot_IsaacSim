<!-- source: py/api/classisaacsim_1_1core_1_1includes_1_1_multi_library_loader.html | title: MultiLibraryLoader — Isaac Sim -->

# MultiLibraryLoader
Fully qualified name: `isaacsim::core::includes::MultiLibraryLoader`
classMultiLibraryLoader

Manager for multiple dynamic libraries.
Provides functionality to load and manage multiple dynamic libraries simultaneously. Handles cleanup of all loaded libraries on destruction.
Public Functions
inline~MultiLibraryLoader()

Destructor.
Cleans up all loaded libraries

inlinestd ::shared_ptr<LibraryLoader >loadLibrary(
conststd ::stringlibrary,
std ::stringprefix="",
)
Loads a new library.
Creates a new LibraryLoader instance for the specified library and adds it to the managed collection
Parameters:

- library – [in] Base name of the library to load

- prefix – [in] Optional prefix to add to the library name

Returns:
std::shared_ptr<LibraryLoader> Pointer to the created loader
