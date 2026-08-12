<!-- source: utilities/debugging/tutorial_advanced_python_debugging.html | title: Debugging With Visual Studio Code — Isaac Sim Documentation -->

# Debugging With Visual Studio Code

## Learning Objectives
In this tutorial, we will go over

- Debugging a standalone Python script

- Debugging Python Scripts Running in Docker .

- Attaching to the `omni.kit.debug.vscode_debugger` extension to debug a running instance of Isaac Sim

## Standalone Python Scripts
Note
Debugging standalone Python scripts is only supported on Linux currently

- From the Isaac Sim App Selector click the “Open in Terminal” button, then execute the following command: `code .` This launches a new VS Code window and opens the current folder. You can also launch VS Code and open the folder.

- Let’s try debugging a simple script, open `standalone_examples/api/isaacsim.simulation_app/hello_world.py` and place a breakpoint.

- Select the “Run” icon from the toolbar on the left, and ensure “Current File” is selected from the configuration dropdown menu.

- Click “Start Debugging” or press F5 to launch the debugger. Pressing F10 will step line by line. You can mouse over to examine variable values.
[image: ../../_images/isim_4.5_full_ref_external_vscode_standalone_debug.png]
- Stop the current debugging session and let’s try passing a command-line argument to our code in the “args” field of the .vscode/launch.json file. For example, here we change the default nucleus server

```
{
"name": "Python: Current File",
"type": "python",
"request": "launch",
"program": "${file}",
"console": "integratedTerminal",
"env": {
"EXP_PATH": "${workspaceFolder}/apps",
"RESOURCE_NAME": "IsaacSim"
},
"python": "${workspaceFolder}/kit/python/bin/python3",
"envFile": "${workspaceFolder}/.vscode/.standalone_examples.env",
"preLaunchTask": "setup_python_env",
"args": ["--/persistent/isaac/asset_root/default=\"omniverse://my_server\""]
}
```

- Add the following lines to `hello_world.py` and place a breakpoint on the `print(server_check)` line.

```
# The most basic usage for creating a simulation app
kit = SimulationApp()
import carb
server_check = carb.settings.get_settings().get_as_string("/persistent/isaac/asset_root/default")
print(server_check)
for i in range(100):
kit.update()
kit.close() # Cleanup application
```

- After modifying and saving the launch.json, press F5 to launch the debugger.

- Verify that the variable contains the server set in the `args` in `launch.json`
[image: ../../_images/isim_4.5_full_ref_external_vscode_standalone_inspect.png]

## Python Scripts Running in Docker
You can debug a Python script running headless in a docker container.

- Deploy the container and run it with an interactive Bash session.

- In the running container, install `debugpy`:

```
# ./python.sh -m pip install debugpy
```

- Create a new debugging configuration in VS Code with (“Run” menu > “Add Configuration…” > “Python Debugger” > “Remote Attach”, choose: host “localhost” and port “5678”).

- Make sure the pathMappings are correct with `/isaac-sim` in the container mapping to the folder where you have Isaac Sim installed locally. These paths should match the configuration in your vscode `launch.json`:

```
{
"name": "Python Debugger: Docker Attach",
"type": "debugpy",
"request": "attach",
"connect": {
"host": "localhost",
"port": 5678
},
"pathMappings": [
{
"localRoot": "${workspaceFolder}/_build/linux-x86_64/release",
"remoteRoot": "/isaac-sim"
}
]
},
```

- You must still use `./python.sh` to run Python scripts, but to debug them you have to add `-m debugpy --wait-for-client --listen 0.0.0.0:5678` after `./python.sh` and before the Python file.

- As an example, open `standalone_examples/api/isaacsim.core.api/time_stepping.py` in VS Code and set a breakpoint by clicking on the margin to the left of a line of code.

- Now start run `time_stepping.py` in the docker container with the complete debugging command:

```
# ./python.sh -m debugpy --wait-for-client --listen 0.0.0.0:5678 standalone_examples/api/isaacsim.core.api/time_stepping.py
```

- Because of the `--wait-for-client` flag, the script will not start right away. You must attach the debugger first by selecting it in VS Code’s debug window and pressing the Play button.

- The script should start in the docker window, and stop at the breakpoint inside VS Code.

Note
If the path mappings are incorrect you will not be able to set breakpoints or step through code.

## Attaching the Debugger to a Running App
To debug a script you are already running, use the VS Code Debugger extension.

- Launch Isaac Sim, and from the top toolbar, select Window > Extensions. Then search for “vscode” and click the Enable button for the `omni.kit.debug.vscode` extension. By default, the status will show “VS Code Debugger Unattached” in red text.
[image: ../../_images/isim_4.5_full_ref_external_vscode_debug_extension.png]
- Then launch VS Code, and select the “Run” icon from the toolbar on the left.

- From the configuration menu, select “Python: Attach (windows-x86_64/linux-x86_64) and click the green arrow to start debugging.

- Notice that the status in Isaac Sim changes to “VS Code Debugger Attached” in blue text.
[image: ../../_images/isim_4.5_full_ref_external_vscode_debug_attach.png]
- You can now return to your Python file in VS Code and add breakpoints to debug, as described above.

Note
To configure the host and port used for debugging, the following command-line arguments can be provided

```
--/exts/omni.kit.debug.python/host="127.0.0.1"
--/exts/omni.kit.debug.python/port=3000
```
These should match the configuration in your vscode `launch.json`

```
{
"name": "Python: Attach (windows-x86_64/linux-x86_64)",
"type": "python",
"request": "attach",
"port": 3000,
"host": "127.0.0.1"
},
```

## Summary
In this tutorial, we covered #. Debugging a standalone Python script #. Attaching the vscode debugger to a running instance of Isaac Sim

### Further Learning
For more details about how the vscode integration works, refer to Visual Studio Code (VS Code)
