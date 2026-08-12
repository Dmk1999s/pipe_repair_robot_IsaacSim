<!-- source: py/api/namespace_isaacsim__core__includes__utils__path.html | title: path — Isaac Sim -->

# path
Fully qualified name: `isaacsim::core::includes::utils::path`
namespacepath

## Enumerations
PathType

## Functions
std::stringMakeRelativePath (const std::string &filePath, const std::string &fileRelativePath)
boolcreateSymbolicLink (const std::string &target, const std::string &link)
std::stringgetParent (const std::string &filePath)
std::stringgetPathStem (const char *path)
boolhasExtension (const std::string &filename, const std::string &extension)
boolisAbsolutePath (const char *path)
boolisFile (const std::string &path)
std::stringnormalizeUrl (const char *url)
std::stringpathJoin (const std::string &path1, const std::string &path2)
std::stringresolve_absolute (std::string parent, std::string relative)
std::stringresolve_path (const std::string &path)
Calculates the final path by resolving the relative path and removing any unnecessary components.

std::stringresolve_relative (const std::string &base, const std::string &target)
Calculates the relative path of target relative to base.

std::vector< std::string >split_path (const std::string &path)
PathTypetestPath (const char *path)
std::stringtoLowercase (const std::string &str)
