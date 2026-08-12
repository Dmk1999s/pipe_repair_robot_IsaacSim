<!-- source: py/source/extensions/isaacsim.storage.native/docs/index.html | title: [isaacsim.storage.native] Isaac Sim Native Storage — Isaac Sim -->

# [isaacsim.storage.native] Isaac Sim Native Storage
Version: 1.5.1
Isaac Sim Native Storage

## Enable Extension
The extension can be enabled (if not already) in one of the following ways:

## API

### Python API

[TABLE]
[/TABLE]
classVersion(s)
Bases: Version

build_server_list()→List
Return list with all known servers to check
Returns:
List of servers found

Return type:
all_servers (List)

check_server(server:str, path:str, timeout:float=10.0)→bool
Check a specific server for a path
Parameters:

- server (str) – Name of Nucleus server

- path (str) – Path to search

- timeout (float) – Default value: 10 seconds

Returns:
True if folder is found

Return type:
bool

asynccheck_server_async(
server:str,
path:str,
timeout:float=10.0,
)→boolCheck a specific server for a path (asynchronous version).
Parameters:

- server (str) – Name of Nucleus server

- path (str) – Path to search

- timeout (float) – Default value: 10 seconds

Returns:
True if folder is found

Return type:
bool

create_folder(server:str, path:str)→bool
Create a folder on server
Parameters:

- server (str) – Name of Nucleus server

- path (str) – Path to folder

Returns:
True if folder is created successfully

Return type:
bool

delete_folder(server:str, path:str)→bool
Remove folder and all of its contents
Parameters:

- server (str) – Name of Nucleus server

- path (str) – Path to folder

Returns:
True if folder is deleted successfully

Return type:
bool

asyncdownload_assets_async(
src:str,
dst:str,
progress_callback,
concurrency:int=10,
copy_behaviour:omni.client.CopyBehavior=omni.client.CopyBehavior.OVERWRITE,
copy_after_delete:bool=True,
timeout:float=300.0,
)→omni.client.ResultDownload assets from S3 bucket
Parameters:

- src (str) – URL of S3 bucket as source

- dst (str) – URL of Nucleus server to copy assets to

- progress_callback – Callback function to keep track of progress of copy

- concurrency (int) – Number of concurrent copy operations. Default value: 3

- copy_behaviour (omni.client.CopyBehavior) – Behavior if the destination exists. Default value: OVERWRITE

- copy_after_delete (bool) – True if destination needs to be deleted before a copy. Default value: True

- timeout (float) – Default value: 300 seconds

Returns:
Result of copy

Return type:
Result (omni.client.Result)

find_nucleus_server(suffix:str)→Tuple[bool,str]
Attempts to determine best Nucleus server to use based on existing mountedDrives setting and the default server specified in json config at “/persistent/isaac/asset_root/”. Call is blocking
Parameters:
suffix (str) – Path to folder to search for. Default value: /Isaac

Returns:
True if Nucleus server with suffix is found url (str): URL of found Nucleus

Return type:
bool

get_assets_root_path(*, skip_check:bool=False)→str
Tries to find the root path to the Isaac Sim assets on a Nucleus server
Parameters:
skip_check (bool) – If True, skip the checking step to verify that the resolved path exists.

Raises:

- RuntimeError – if the root path setting is not set.

- RuntimeError – if the root path is not found.

Returns:
URL of Nucleus server with root path to assets folder.

Return type:
url (str)

asyncget_assets_root_path_async(*, skip_check:bool=False)→str
Tries to find the root path to the Isaac Sim assets on a Nucleus server (asynchronous version).
Parameters:
skip_check (bool) – If True, skip the checking step to verify that the resolved path exists.

Raises:

- RuntimeError – if the root path setting is not set.

- RuntimeError – if the root path is not found.

Returns:
URL of Nucleus server with root path to assets folder.

Return type:
url (str)

get_assets_server()→str|None
Tries to find a server with the Isaac Sim assets
Returns:
URL of Nucleus server with the Isaac Sim assets
Returns None if Nucleus server not found.

Return type:
url (str)

get_full_asset_path(path:str)→str|None
Tries to find the full asset path on connected servers
Parameters:
path (str) – Path of asset from root to verify

Raises:
RuntimeError – if the root path is not found.

Returns:
URL or full path to assets. Returns None if assets not found.

Return type:
url (str)

asyncget_full_asset_path_async(path:str)→str|None
Tries to find the full asset path on connected servers (asynchronous version).
Parameters:
path (str) – Path of asset from root to verify

Raises:
RuntimeError – if the root path is not found.

Returns:
URL or full path to assets. Returns None if assets not found.

Return type:
url (str)

get_isaac_asset_root_path()→str|None
get_nvidia_asset_root_path()→str|None
get_server_path(suffix:str='')→str|None
Tries to find a Nucleus server with specific path.
Parameters:
suffix (str) – Path to folder to search for.

Raises:
RuntimeError – if the root path is not found.

Returns:
URL of Nucleus server with path to folder. Returns None if Nucleus server not found.

Return type:
url (str)

asyncget_server_path_async(suffix:str='')→str|None
Tries to find a Nucleus server with specific path (asynchronous version).
Parameters:
suffix (str) – Path to folder to search for.

Raises:
RuntimeError – if the root path is not found.

Returns:
URL of Nucleus server with path to folder. Returns None if Nucleus server not found.

Return type:
url (str)

get_url_root(url:str)→str
Get root from URL or path. :param url: full http or omniverse path :type url: str
Raises:
RuntimeError – if the root path is not found.

Returns:
Root path or URL or Nucleus server

Return type:
str

is_dir(path:str)→bool
Check if path is a folder
Parameters:
path (str) – Path to folder

Returns:
True if path is a folder

Return type:
bool

asyncis_dir_async(path:str)→bool
Check if path is a folder
Parameters:
path (str) – Path to folder

Returns:
True if path is a folder

Return type:
bool

is_file(path:str)→bool
Check if path is a file
Parameters:
path (str) – Path to file

Returns:
True if path is a file

Return type:
bool

asyncis_file_async(path:str)→bool
Check if path is a file
Parameters:
path (str) – Path to file

Returns:
True if path is a file

Return type:
bool

asynclist_folder(path:str)→Tuple[List,List]
List files and sub-folders from root path
Parameters:
path (str) – Path to root folder

Raises:
Exception – When unable to find files under the path.

Returns:
List of path to each file dirs (typing.List): List of path to each sub-folder

Return type:
files (List)

asyncrecursive_list_folder(path:str)→List
Recursively list all files
Parameters:
path (str) – Path to folder

Returns:
List of path to each file

Return type:
paths (List)

verify_asset_root_path(
path:str,
)→Tuple[omni.client.Result,str]Attempts to determine Isaac assets version and check if there are updates. (asynchronous version)
Parameters:
path (str) – URL or path of asset root to verify

Returns:
OK if Assets verified ver (str): Version of Isaac Sim assets

Return type:
omni.client.Result

## Settings

### Other Settings
The extension changes some settings of the application or other extensions, which are listed in the table below.

[TABLE]
Application/extension setting | Description | Value
persistent.isaac.asset_root.default | Default asset root path for Isaac Sim | 'https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/5.1'
persistent.isaac.asset_root.timeout | Timeout in seconds for asset root path to be resolved | 5.0
[/TABLE]
