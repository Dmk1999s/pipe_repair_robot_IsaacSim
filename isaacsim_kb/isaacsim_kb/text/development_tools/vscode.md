<!-- source: development_tools/vscode.html | title: Visual Studio Code (VS Code) — Isaac Sim Documentation -->

# Visual Studio Code (VS Code)

## Isaac Sim VS Code Edition
Isaac Sim VS Code Edition is an extension for Visual Studio Code that provides development support for NVIDIA Omniverse in general and Isaac Sim in particular.
Key Features:

- Execute Python code, in the Python environment of a running application, locally or remotely from VS Code and show the output in the Isaac Sim VS Code Edition panel.

- Browse and insert snippets of code related to Isaac Sim, Omniverse Kit and Universal Scene Description (USD).

- Create templates for Omniverse/Isaac Sim extensions and other development approaches.

- Quick access to the most relevant Omniverse/Isaac Sim documentation sources and resources without leaving the editor.

Install it now to get started: Isaac Sim VS Code Edition
[image: ../_images/isaac_tutorial_advanced_code_editors_vscode.png]

## Interactive Scripting
The `isaacsim.code_editor.vscode` extension allows you to edit and execute Python code interactively from the VS Code editor. It can be enabled or disabled using the Extension Manager by searching for `isaacsim.code_editor.vscode`.
Note
This extension requires its Visual Studio Code pair extension: Isaac Sim VS Code Edition to be installed and enabled, in the VS Code editor, in order to execute Python scripts on a running Isaac Sim instance.

- To begin, enable this extension using the Extension Manager by searching for `isaacsim.code_editor.vscode`.

- Once the extension is enabled, go to the top menu bar and click on Window > VS Code to open the Isaac Sim folder in a VS Code application.

- Open a stored file or write the code you want to run in a VS Code editor tab.

- From the VS Code editor, click on the Isaac Sim VS Code Edition container in the Activity Bar (the one with the Isaac Sim logo) to open it. Then, click on Run (or Run selected text if you have selected code statements), in the Commands tree view, to execute it.

- Inspect the execution output, if any, in the Isaac Sim VS Code Edition output panel.

## VS Code Configuration Files
The Isaac Sim installation provides a `.vscode` workspace with a pre-configured environment under the following three files:

```
.vscode/launch.json
.vscode/settings.json
.vscode/tasks.json
```

### launch.json
This file provides three different configurations that can be executed using the `Run & Debug` section in VSCode.

- Python: Current File: Debug the currently open standalone Python file, should not be used with extension examples/code.

- Python: Attach: Attach to a running Isaac Sim application for debugging purposes, most useful when running an interactive GUI application. See Attaching the Debugger to a Running App for usage information.

- (Linux) isaac-sim Run the main Isaac Sim application with an attached debugger.

### settings.json
This file sets the default Python executable that comes with Isaac Sim:

```
"python.pythonPath": "${workspaceFolder}/kit/python/bin/python3",
```
As well as a configuration for `"python.analysis.extraPaths"` which by default includes all of the extensions that are provided by default. You can add additional paths here if needed.

### tasks.json
This is a helper file that contains a task used to automatically setup the Python environment when using the `Python: Current File` option in `Run & Debug`.

```
"tasks": [
{
"label": "setup_python_env",
"type": "shell",
"linux": {
"command": "source ${workspaceFolder}/setup_python_env.sh && printenv >${workspaceFolder}/.vscode/.standalone_examples.env"
}
}
]
```
Once executed, the task generates the `.standalone_examples.env` file used by VS Code to launch the Python debug process. Refer to Debugging With Visual Studio Code for more details.
