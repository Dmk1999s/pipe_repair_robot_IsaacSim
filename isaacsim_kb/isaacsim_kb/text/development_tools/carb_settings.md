<!-- source: development_tools/carb_settings.html | title: Modify Carb Settings — Isaac Sim Documentation -->

# Modify Carb Settings
Carbonite (carb) settings are used to configure default behaviors of Omniverse and Isaac Sim. They can control a wide ranges of features, such as window properties, ROS versions, browser folders, and more. You may wish to change these settings to suit your needs. Here we show the four ways to change the Carb settings in Isaac Sim.
For this tutorial, we will set a parameter inside extension `isaacsim.my.extension` named `data.foo` to the value `True`. Replace these with your actual extension name, setting parameter, and value when you are working with your project.

## Script Editor Snippet
You can temporarily and quickly change the Carb settings in the Script Editor . This is useful for testing and debugging, and can be done while Isaac Sim is open. The changes made this way will not be saved after you close the application, and relaunching the simulator will reset the settings.

```
1import carb.settings
2import omni.kit
3
4## Set Carb Setting
5settings = carb.settings.get_settings()
6settings.set("/exts/isaacsim.my.extension/data/foo", True)
7
8## Restart Extension to Apply Changes
9omni.kit.app.get_app().get_extension_manager().set_extension_enabled_immediate("isaacsim.my.extension",False)
10omni.kit.app.get_app().get_extension_manager().set_extension_enabled_immediate("isaacsim.my.extension",True)
```

## Command-Line Argument
You can launch Isaac Sim with a command-line argument to change the Carb settings. The changes made this way will not be saved after you close the application, and relaunching the simulator without the arguments will reset the settings.
At the root of your Isaac Sim installation, run the following command:

## Edit .toml File
For more permanent changes, you can edit the extension’s .toml file. The changes made this way will persist after you close the application.

- Navigate to the extension’s folder. For example, if you are changing the settings for the isaacsim.my.extension, navigate to <isaac-sim-root_dir>/exts/isaacsim.my.extension/config.

- Open the .toml file with a text editor, and add the following line to the file:

```
[settings]
exts."isaacsim.my.extension".data.foo = true
```

- Launch Isaac Sim to see the changes.

## Customize .kit File
If you have multiple settings in multiple extensions that you want to change, you can edit the .kit file for your application. The changes made this way will persist after you close the application.

- From the root of your Isaac Sim installation, navigate to <isaac-sim-root_dir>/apps/. Locate the Kit experience app file you are using in this folder. By default, it is the isaacsim.exp.full.kit.

- Open the app file and add the following line to the file:

```
[settings]
exts."isaacsim.my.extension".data.foo = true
```

- Launch Isaac Sim to see the changes.
