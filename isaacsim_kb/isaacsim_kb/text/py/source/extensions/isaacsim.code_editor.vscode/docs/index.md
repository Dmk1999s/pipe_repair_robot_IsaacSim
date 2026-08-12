<!-- source: py/source/extensions/isaacsim.code_editor.vscode/docs/index.html | title: [isaacsim.code_editor.vscode] VS Code integration — Isaac Sim -->

# [isaacsim.code_editor.vscode] VS Code integration
Version: 1.1.0
VS Code version of Omniverse’s script editor

## Enable Extension
The extension can be enabled (if not already) in one of the following ways:

## Settings

### Extension Settings
The table list the extension-specific settings.

[TABLE]
Setting name | Description | Type | Default value
host | IP address where the extension server will listen for connections. | str | '127.0.0.1'
port | Port number where the extension server will listen for connections. | int | 8226
carb_logs | Whether to publish incoming carb logging messages.
Warning: enabling this feature may cause the application to freeze in certain circumstances. | bool | False
[/TABLE]
The extension-specific settings can be either specified (set) or retrieved (get) in one of the following ways:
