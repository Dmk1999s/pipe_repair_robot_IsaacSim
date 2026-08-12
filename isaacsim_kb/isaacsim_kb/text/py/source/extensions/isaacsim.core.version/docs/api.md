<!-- source: py/source/extensions/isaacsim.core.version/docs/api.html | title: API — Isaac Sim -->

# API

## Python API

[TABLE]
[/TABLE]
classVersion
Bases: `object`

get_version()→Tuple[str,str,str,str,str,str,str,str]
Retrieve version from the App VERSION file
Returns:
[Core version, Pre-release tag and build number, Major version, Minor version, Patch version, Pre-release tag, Build number, Build tag]

Return type:
Tuple[str, str, str, str, str, str, str, str]

parse_version(
full_version:str,
)→Version Parse a version string into a version object
Parameters:
full_version (str) – full version string read from a VERSION file

Returns:
Parsed version object

Return type:
Version
