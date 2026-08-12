<!-- source: installation/install_python.html | title: Python Environment Installation — Isaac Sim Documentation -->

# Python Environment Installation
This section presents the following contents:

- Install Isaac Sim using PIP in a (virtual) Python environment

- Using the Isaac Sim Default Python Environment

# Install Isaac Sim using PIP
Note

- Isaac Sim requires Python 3.11. Visit the Python download page to get a suitable version.

- On Linux, GLIBC 2.35+ (`manylinux_2_35_x86_64`) version compatibility is required for pip to discover and install the Python packages. Check the GLIBC version using the command `ldd --version`.

- On Windows, it may be necessary to enable long path support to avoid installation errors due to OS limitations.

Isaac Sim provides several Python namespace packages that allow you to compose an Isaac Sim app by parts using a Python package manager (for example: pip ). The following tables list the available Isaac Sim - Python packages.

[TABLE]
Package | Description
isaacsim | A metapackage that defines optional dependencies for installing some or all of the other Python packages
|
isaacsim-kernel | Isaac Sim kernel
isaacsim-app | Isaac Sim components for application setup
isaacsim-asset | Isaac Sim components for asset import, creation and management
isaacsim-benchmark | Isaac Sim components for benchmarking
isaacsim-code-editor | Isaac Sim components for scripting and code edition
isaacsim-core | Isaac Sim core extensions and APIs
isaacsim-cortex | Isaac Sim components to enable the Cortex decision framework for intelligent robot behavior
isaacsim-example | Isaac Sim examples
isaacsim-gui | Isaac Sim components for the graphical user interface (GUI)
isaacsim-replicator | Isaac Sim components to enable the Replicator framework for synthetic data generation pipelines and services
isaacsim-rl | Isaac Sim components for reinforcement learning
isaacsim-robot | Isaac Sim’s robot models and APIs
isaacsim-robot-motion | Isaac Sim components for motion generation pipelines and algorithms
isaacsim-robot-setup | Isaac Sim components for robot setup
isaacsim-ros2 | Isaac Sim components for ROS 2 system integration
isaacsim-sensor | Isaac Sim components to simulate sensors
isaacsim-storage | Isaac Sim components for storage system
isaacsim-template | Isaac Sim templates
isaacsim-test | Isaac Sim components for testing
isaacsim-utils | Isaac Sim utilities
[/TABLE]

[TABLE]
Package | Description
isaacsim-extscache-kit | Kit extensions cache for Isaac Sim
isaacsim-extscache-kit-sdk | Kit-SDK extensions cache for Isaac Sim
isaacsim-extscache-physics | Physics extensions cache for Isaac Sim
[/TABLE]

## Installation Using PIP

- Create and activate the virtual environment (optional, but highly recommended):
Make sure pip is updated (`pip install --upgrade pip`) after activating the environment and before proceeding with installation.

- Install Isaac Sim - Python packages:
The installation path can be queried with the command `pip show isaacsim`.

## Running Isaac Sim
Note
You must agree and accept the Omniverse License Agreement (EULA) to use Isaac Sim. The EULA can be accepted in two ways, through system environment variables or by responding to a prompt:
Warning

- Some Python packages required by some Isaac Sim extensions or examples may not be included as dependencies. However, it is possible to install them using the command `pip install DEPENDENCY_NAME`.

- On DGX Spark / aarch64 architecture , it may be necessary to preload (`LD_PRELOAD`) the `libgomp` shared library for some modules to be loaded. When the `isaacsim` package is imported, a check will be performed, after which a message providing preload instructions may be displayed.

### Launching Isaac Sim Experiences
Hint
To launch the (standard) Isaac Sim app, run the `isaacsim` command in the terminal.
The installation registers a Python entry point (`isaacsim`) that allows launching experience (`.kit`) files. The experience file can be defined by its:

- absolute or relative file path

- file name, with/without `.kit` file extension (search paths: `isaacsim/apps`, `omni/apps`)

```
isaacsim path/to/experience_file.kit [arguments]
```

The following table lists the most common Isaac Sim - Python packages commands to launch experiences:

[TABLE]
Command | Description
isaacsim isaacsim.exp.compatibility_check | Compatibility check app: a lightweight application that programmatically checks for Isaac Sim requirements.
isaacsim isaacsim.exp.full | Standard Isaac Sim app, as it is executed from binary. It is the default experience if no experience file is specified (for example: isaacsim ).
isaacsim isaacsim.exp.full.streaming --no-window | Headless livestreaming Isaac Sim (WebRTC protocol). See Isaac Sim WebRTC Streaming Client for more details. Warning Unsupported on DGX Spark / aarch64 architecture .
[/TABLE]

### Running Python Scripts
Run the following command to execute a Python script in the (virtual) environment:

```
python path/to/script.py
```

### Running in Interactive Interpreter or Notebooks
When running in interactive interpreter or Notebooks (for example: Jupyter, Colab), you must import the `isaacsim` package to access the SimulationApp class. For convenience, the `isaacsim` package exposes that class (implemented in the `isaacsim.simulation_app` extension).
Note
Calling the `SimulationApp.close` method on Notebooks causes a kernel interruption and termination.

## Generating VS Code Settings
Because of the structure resulting from the installation, VS Code IntelliSense (code completion, parameter info, and member lists) will not work by default. To set it up (define the search paths for import resolution, the path to the default Python interpreter, and other settings), for a given workspace folder, run the following command:

```
python -m isaacsim --generate-vscode-settings
```
Note
The command will generate a `.vscode/settings.json` file in the workspace folder. If the file already exists, it will be overwritten (a confirmation prompt will be shown first).

# Default Python Environment
It is possible to run Isaac Sim natively from Python rather than as a standalone executable. This provides more low-level control over how to initialize, setup, and manage an Omniverse application. Isaac Sim provides a built-in Python 3.11 environment that packages can use, similar to a system-level Python install. We recommend using this Python environment when running the Python scripts.
Run the following from the Isaac Sim root folder to start a Python script in this environment:

```
./python.sh path/to/script.py
```

Note

- You can open a terminal directly at the Isaac Sim root folder from the Isaac Sim App Selector .

- On Windows use `python.bat` instead of `python.sh`.

- If you need to install additional packages using pip, run the following:

```
./python.sh -m pip install name_of_package_here
```

See the Python Environment manual for more details about `python.sh`.

## Jupyter Notebook Setup
Jupyter Notebook is supported on Linux only.
Jupyter Notebooks that use Isaac Sim can be executed as follows:

```
./jupyter_notebook.sh path/to/notebook.ipynb
```

The first time you run `jupyter_notebook.sh`, it installs the Jupyter Notebook package into the Isaac Sim Python environment, this can take several minutes.
See the Jupyter Notebook documentation for more details.

## Visual Studio Code Support
Using Visual Studio Code for tutorials and examples is recommended.
The Isaac Sim package provides a `.vscode` workspace with a pre-configured environment that provides the following:

- Launch configurations for running in standalone Python mode or the interactive GUI

- An environment for Python auto-complete

You can open this workspace by opening the main Isaac Sim package folder in Visual Studio Code (VS Code).
See the Visual Studio Code (VS Code) documentation for details about the VS Code workspace.

## Advanced: Running in Docker
Start the Docker container following the instructions in Container Deployment up to step 7.
After the Isaac Sim container is running, you can run a Python script or Jupyter Notebook from the sections above.
Note

- You can install additional packages using pip:

```
./python.sh -m pip install name_of_package_here
```

- See Save Docker Image for committing the image and making the Python setup installation persistent.

## Advanced: Running with Anaconda
Warning
This setup (prior to Isaac Sim - Python packages installation) is deprecated and will be removed in the next release. To install/use Isaac Sim on a Conda (or any other Python environment), see Install Isaac Sim using PIP instead.

- Create a new environment with the following command:

```
conda env create -f environment.yml
conda activate isaac-sim
```

- If you have an existing Conda environment, ensure that the packages in `environment.yml` are installed. Alternatively, you can delete and re-create your Conda environment as follows:

```
conda remove --name isaac-sim --all
conda env create -f environment.yml
conda activate isaac-sim
```

- You must set up environment variables so that Isaac Sim Python packages are located correctly. On Linux, you can do this as follows:

```
source setup_conda_env.sh
```

- Run samples as follows in the `isaac-sim` Conda env:

```
python path/to/script.py
```

Note
If you are using the `isaac-sim` Anaconda environment, use `python` instead of `python.sh` to run the samples.
