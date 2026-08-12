<!-- source: installation/install_workstation.html | title: Workstation Installation — Isaac Sim Documentation -->

# Workstation Installation
The workstation installation is recommended if you want to run Isaac Sim as a GUI application on Windows or Linux with a GPU.
See also

- Differences Between Workstation And Docker

- Local Assets Packs

- Isaac Sim Launch Scripts for additional scripts like the warmup script to pre-warm the shader cache before running Isaac Sim.

Note

- Omniverse Launcher, Nucleus Workstation, and Nucleus Cache will be deprecated and will no longer be available starting October 1, 2025.

- For those who want to use Nucleus and Live Sync after October 1, 2025, please use Enterprise Nucleus Server .

- Nucleus Cache is replaced by Hub Workstation Cache .

- If you have issues installing Hub Workstation Cache in Windows, run:

```
mklink /d %APPDATA%\ov %LOCALAPPDATA%\ov
```

## Isaac Sim Compatibility Checker
The Isaac Sim Compatibility Checker is a lightweight application that programmatically checks the above requirements and indicates which of them are valid, or not, for running NVIDIA Isaac Sim on the machine.
The application can be run either from a binary installation (Workstation, Container or Open-Source repository) or from Python packages (pip install), as follows:

- From binary installation (Workstation or Open-Source repository setup):

- Install/build Isaac Sim according to the target setup workflow.

- Run the `isaac-sim.compatibility_check.sh` script on Linux, or the `isaac-sim.compatibility_check.bat` script on Windows.

- From Python packages (pip install):

- Follow the instructions to install Isaac Sim from Python packages .
Hint
You can use `pip install isaacsim[compatibility-check]` to install a minimal setup for the Compatibility Checker app instead of installing the full version.

- Run the `isaacsim isaacsim.exp.compatibility_check` command.

- From Container :

- Run headless:

```
$ docker run --entrypoint bash -it --gpus all --rm --network=host \
nvcr.io/nvidia/isaac-sim:5.1.0 ./isaac-sim.compatibility_check.sh --/app/quitAfter=10 --no-window
```

- Run as GUI:

```
$ xhost +local:
$ docker run --entrypoint bash -it --gpus all --rm --network=host \
-e "PRIVACY_CONSENT=Y" \
-v $HOME/.Xauthority:/isaac-sim/.Xauthority \
-e DISPLAY \
nvcr.io/nvidia/isaac-sim:5.1.0 ./isaac-sim.compatibility_check.sh
```

### Verifying Compatibility
The application highlights, in color, the following states:

- green excellent

- light-green good

- orange enough, more is recommended

- red not enough/unsupported

The application checks:

- NVIDIA GPU: Driver version, RTX-capable GPU, GPU VRAM

- CPU, RAM and Storage: CPU processor, Number of CPU cores, RAM, Available storage space

- Others: Operating system, Display

The Test Kit button, launches a minimal Kit application (in headless mode) and checks if its execution was successful or not, reporting the result on the panel next to it.

## Workstation Setup

- Review the requirements. See Isaac Sim Requirements .

- Optionally, for the full development install, make sure you have Visual Studio Code to view and debug source code.

## Isaac Sim Install and Launch
The Isaac Sim app can be run directly from the command line with `isaac-sim.bat` or `./isaac-sim.sh`.
The first run of the Isaac Sim app takes some time to warm up the shader cache.
To run Isaac Sim with a fresh config, use the `--reset-user` flag. This flag can be entered in the Extra Args section of the Isaac Sim App Selector or when running Isaac Sim in command line.
Nucleus, Cache, and Hub are not needed to run Isaac Sim.

- Download the Latest Release of Isaac Sim for your platform to the `Downloads` folder.

- Create a folder named `isaacsim` at `c:/` or at the root of your Linux environment.

- Unzip the package to that folder.

- Navigate to that folder.

- To create a symlink to the extension_examples for the tutorials, run the `post_install` script. The script can be run at this stage or after installation.

- On Linux, run `./post_install.sh`.

- On Windows, double click `post_install.bat`.

- Use one of the following methods to run the Isaac Sim App Selector:

- On Linux, run `./isaac-sim.selector.sh`.

- On Windows, double click `isaac-sim.selector.bat`.

- In the popup window choose Isaac Sim Full.

- Click START to run the Isaac Sim main app.
A command window opens and runs scripts.
You may need to login to Omniverse.
The command window continues running scripts.
Then the Isaac Sim GUI window opens with nothing displayed in it. It can take 5-10 minutes to complete.

- Proceed to Quick Tutorials to begin the first Basic Tutorial.

Note
There may be situations in which an internal conflict causes failures within the cache and configuration systems of Isaac Sim (for example, if there is a version mismatch between a source installation and a python package installation). If this occurs, the following may prove useful:

- The `--reset-user` flag can be used to reset the user configuration to its default state.

- The `clear_caches.sh` and `.bat` scripts can be used to clear the cache in Linux and Windows respectively.

## Example Installation
For example, from the command line, execute the following commands:
Final load message example:
