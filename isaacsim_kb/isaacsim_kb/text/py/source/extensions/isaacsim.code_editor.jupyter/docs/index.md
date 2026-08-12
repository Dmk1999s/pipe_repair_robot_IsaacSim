<!-- source: py/source/extensions/isaacsim.code_editor.jupyter/docs/index.html | title: [isaacsim.code_editor.jupyter] Jupyter notebook integration — Isaac Sim -->

# [isaacsim.code_editor.jupyter] Jupyter notebook integration
Version: 1.1.1
Jupyter notebook version of Omniverse’s script editor

## Enable Extension
The extension can be enabled (if not already) in one of the following ways:

## Settings

### Extension Settings
The table list the extension-specific settings.

[TABLE]
Setting name | Description | Type | Default value
host | IP address where the extension server will listen for connections. | str | '127.0.0.1'
port | Port number where the extension server will listen for connections. | int | 8227
kill_processes_with_port_in_use | Whether to kill applications/processes that use the same ports before enabling the extension.
Disable this option if you want to launch multiple applications with this extension enabled. | bool | False
notebook_ip | IP address where the Jupyter server is being started. | str | '127.0.0.1'
notebook_port | Port number where the Jupyter server is being started. | int | 8228
notebook_token | Jupyter server token for token-based authentication. If empty, the server will start without authentication. | str | ''
notebook_dir | The directory to use for notebooks. If empty, the directory is data/notebooks within the extension tree. | str | ''
command_line_options | Jupyter server command line options other than --ip , --port , --token and --notebook-dir . | str | '--allow-root --no-browser --JupyterApp.answer_yes=True'
[/TABLE]
The extension-specific settings can be either specified (set) or retrieved (get) in one of the following ways:
