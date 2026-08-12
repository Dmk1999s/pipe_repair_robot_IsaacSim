<!-- source: utilities/extension_template_generator.html | title: Extension Template Generator — Isaac Sim Documentation -->

# Extension Template Generator
The Extension Template Generator populate a UI-based extensions on your local machine. The available extension templates give a useful starting point for many Isaac Sim applications and are structured to help you learn how to build a custom UI tool that meets your needs.

## Getting Started
To create and enable a new extension using the Extension Template Generator, follow these steps:

- Open the extension generator by going to Utilities > Generate Extension Templates in the menu bar.

- Select the types of templates to expand the corresponding window. Fill in the fields as follow:

- Extension Path: `<Extension_Host_Dir>/my.extension.name`

- Extension Name: `my.extension.name`

- Extension Description: `My Extension Description`

- Click Generate Extension.

- Navigate to Window > Extensions in the toolbar to open the Extensions Manager. Click the hamburger icon to the right of search bar, and then Settings in the sub-menu to open up the path table. If your selected `<Extension_Host_Dir>` is not already on the list, then scroll all the way down to the end in the “Extension Search Path”. Click on the “+” button in the last row in the “edit” column, and type in the full path to the `<Extension_Host_Dir>`.

- Search for your new extension.

- If your chosen `<Extension_Host_Dir>` was one of the default Extension Search Paths, you should find your extension under NVIDIA tab.

- If you added a new Extension Search Path, you should find your extension under the Third Party tab.

- Enable the extension. Verify that it appears in the menu bar on the top in Isaac Sim.

- Alternatively, you can enable extensions by command-line arguments when running Isaac Sim from the terminal: `./isaac-sim.sh --ext-folder {path_to_user_ext_folder} --enable {ext_directory_name}`. On Windows use `python.bat` instead of `python.sh`.

- Get familiar with the template code by reading the `README.md` file in the provided Python module.

[image: ../_images/isim_4.5_full_tut_gui_extension_template.webp]

## Template Options

- Load Scenario Template: The Loaded Scenario Template starts the user off with a simple UI that contains three buttons: Load, Reset, and Run. This is meant to provide as clear a pathway as possible for the user to start writing code to directly affect the USD stage without having to understand much about the internal workings of the underlying simulator.

- Scripting Template: The Scripting Template demonstrates the implementation of a more advanced framework for programming script-like behavior from a UI-based extension in NVIDIA Isaac Sim. This template uses the same mechanics for loading and resetting the robot position as the “Load Scenario Template”, but it implements the Run button as a script.

- Configuration Tooling Template: The Configuration Tooling Template templates provides fundamental tools for asset configuration, such as finding `Articulation` on the stage and dynamically creates a UI frame through which the user may control each joint in the selected `Articulation`.

- UI Component Library Template: The UI Component Library template demonstrate the usage of each `UIElementWrapper`, such as the type of arguments and return values required for each callback function that can be attached to each `UIElementWrapper`.

## More Resources
For more detailed explanation regarding the template generator and each template can be found in Extension Template Generator Explained .
