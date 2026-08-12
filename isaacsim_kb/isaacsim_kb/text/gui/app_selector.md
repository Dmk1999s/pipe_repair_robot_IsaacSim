<!-- source: gui/app_selector.html | title: Isaac Sim App Selector — Isaac Sim Documentation -->

# Isaac Sim App Selector
The Isaac Sim App Selector allows users to quickly start different Isaac Sim modes and locate file paths.
Note

- The Isaac Sim App Selector is not supported on DGX Spark or aarch64 platforms.

- The Isaac Sim App Selector is deprecated as of Isaac Sim 5.1 and will be removed in a future release.

This table outlines the UI elements of the Isaac Sim App Selector.

[TABLE]
Ref # | Option | Result
1 | Isaac Sim Full | Selects the main Isaac Sim Application.
2 | Isaac Sim
Full Streaming | Selects a headless Isaac Sim with livestreaming via Isaac Sim WebRTC Streaming Client .
3 | Package Utilities | Package Path: Open package directory in the file browser or terminal, or copy the package path. Open In Terminal: This is useful if you want to run the Python Environment or directly execute the launch scripts to run Isaac Sim. Clear Caches: Run script to clear the texture, shader and kit caches. Follow the prompts to clear a specific cache.
4 | Additional Arguments | Starts the selected app with the added command line flags. Some useful commands below: -v for verbose logging in the terminal --reset-user reset user config --reset-user --/app/window/width=1920 set the application window width --reset-user --/app/window/height=1080 set the application window height --reset-user --/app/renderer/resolution/width=1920 set the renderer resolution width --reset-user --/app/renderer/resolution/height=1080 set the renderer resolution height --/renderer/activeGpu=0 to set the GPU used by Isaac Sim to the specified number Note: Run Isaac Sim with the --help flag to see additional command line flags.
5 | ROS Options | ROS Bridge Extension - Select whether to run the ROS 2 Bridge. Leave blank to disable the ROS 2 Bridge. Use Internal ROS 2 Internal Libraries - Select the ROS 2 distro internal library to run Isaac Sim with. Applicable when no local installation is available.
6 | Settings | Other settings. Set selection as new default app - This is useful when use with the next option “Automatically start default app”. - Select the a mode (#1-#4) above then click the checkbox. Click START or CLOSE to save this setting. Automatically start default app - This option will skip running the Isaac Sim App Selector and run the selected default app directly. Keep App Selector window opened - When selected, the Isaac Sim App Selector window will not close when the START button is pressed. Show startup console - When selected, Isaac Sim runs in a terminal window then the START button is pressed.
7 | Start | Press the START button to run the selected mode of Isaac Sim
[/TABLE]
Note
The configuration file for the Isaac Sim App Selector is located at `~/.local/share/ov/data/Kit/Isaac-Sim_App_Selector/<version>/user.config.json`
Here is the default config file:

```
"persistent": {
"ext": {
"isaacsim.app.selector": {
"default_app": "omni.isaac.sim",
"auto_start": false,
"persistent_selector": false,
"show_console": true,
"extra_args": "",
"ros_bridge_extension": 0,
"ros_internal_libs": 0
}
}
}
```
