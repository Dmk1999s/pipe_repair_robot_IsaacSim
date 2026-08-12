<!-- source: py/api/classisaacsim_1_1core_1_1includes_1_1_library_loader.html | title: LibraryLoader — Isaac Sim -->

# LibraryLoader
Fully qualified name: `isaacsim::core::includes::LibraryLoader`
classLibraryLoader

Single dynamic library loader.
Handles loading, symbol resolution, and unloading of a single dynamic library. Provides platform-independent interface for library operations with automatic cleanup on destruction.
Public Functions
inlineLibraryLoader(
std ::stringlibrary,
std ::stringprefix="",
booltest=false,
)
Constructor for LibraryLoader .
Attempts to load the specified library with platform-specific naming conventions. On Windows, appends .dll, on other platforms prepends lib and appends .so
Parameters:

- library – [in] Base name of the library to load

- prefix – [in] Optional prefix to add to the library name

- test – [in] If true, suppresses error messages on load failure

inline~LibraryLoader()

Destructor.
Ensures proper cleanup by unloading the library if it was loaded

template<typenameT>
inlineT getSymbol(std ::stringsymbol)

Gets a symbol from the loaded library.
Template function to retrieve a symbol of any type from the library
Template Parameters:
T – Type of the symbol to retrieve

Parameters:
symbol – [in] Name of the symbol to retrieve

Returns:
T The retrieved symbol cast to type T

template<typenameT>
inlineT callSymbol(std ::stringsymbol)

Calls a symbol function with no arguments.
Template function to call a function symbol that takes no arguments
Template Parameters:
T – Return type of the function

Parameters:
symbol – [in] Name of the function to call

Returns:
T The return value from the function call, or nullptr if symbol not found

template<typenameT,typename...Arguments>
inlineT callSymbolWithArg(
std ::stringsymbol,
Arguments ...args,
)
Calls a symbol function with arguments.
Template function to call a function symbol with variable number of arguments
Template Parameters:

- T – Return type of the function

- Arguments – Types of the function arguments

Parameters:

- symbol – [in] Name of the function to call

- args – [in] Arguments to pass to the function

Returns:
T The return value from the function call

inlineboolisValid()

Checks if the library is loaded.
Returns:
bool True if the library was loaded successfully

Public Members
std ::stringloadedLibraryFile

Path to the loaded library file.

carb::extras::LibraryHandleloadedLibrary=carb::extras::kInvalidLibraryHandle

Handle to the loaded library.
