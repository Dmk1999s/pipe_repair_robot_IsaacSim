<!-- source: py/source/extensions/isaacsim.asset.browser/docs/index.html | title: [isaacsim.asset.browser] Isaac Sim Asset Browser — Isaac Sim -->

# [isaacsim.asset.browser] Isaac Sim Asset Browser
Version: 1.3.23
The Isaac Sim Asset Browser extension provides an user interface for loading isaac sim assets and files.
[image: Preview]

## Enable Extension
The extension can be enabled (if not already) in one of the following ways:

### Actions in isaacsim.asset.browser

[TABLE]
ID | Display Name | Description
open_isaac_sim_asset_browser | | Open Isaac Sim Asset Browser
[/TABLE]

## Settings

### Extension Settings
The table list the extension-specific settings.

[TABLE]
Setting name | Description | Type | Default value
folders | Root folder URLs to list and monitor. | list | ['https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/5.1/Isaac/Robots', 'https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/5.1/Isaac/Environments', 'https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/5.1/Isaac/IsaacLab', 'https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/5.1/Isaac/Materials', 'https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/5.1/Isaac/People', 'https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/5.1/Isaac/Props', 'https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/5.1/Isaac/Samples', 'https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/5.1/Isaac/Sensors']
instanceable | List of asset categories that can be dragged from the browser to the viewport window. | list | []
data.timeout | Number of seconds to wait for the folder to be listed/read from. | int | 10
data.filter_file_suffixes | Filter for USD Types only | list | ['.usd', '.usda', '.usdc', '.usdz']
data.hide_file_without_thumbnails | Use only assets with thumbnail | bool | True
visible_after_startup | Whether the browser window is visible when the extension starts up. | bool | False
[/TABLE]
The extension-specific settings can be either specified (set) or retrieved (get) in one of the following ways:
