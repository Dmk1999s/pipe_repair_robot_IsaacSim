<!-- source: py/source/extensions/isaacsim.core.version/docs/index.html | title: [isaacsim.core.version] Isaac Sim Version — Isaac Sim -->

# [isaacsim.core.version] Isaac Sim Version
Version: 2.0.6
Isaac Sim Version extension provides tools to query Isaac Sim version and build information.

## Enable Extension
The extension can be enabled (if not already) in one of the following ways:

## API

### Python API

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
