<!-- source: development_tools/jupyter_notebook.html | title: Jupyter Notebook — Isaac Sim Documentation -->

# Jupyter Notebook

## Interactive Scripting
The `isaacsim.code_editor.jupyter` extension allows you to to open a JupyterLab (or Jupyter Notebook ) app in the current Isaac Sim application scope and edit and execute Python code interactively.

- To begin, enable this extension using the Extension Manager by searching for `isaacsim.code_editor.jupyter`.
Note
This may take several seconds (and Isaac Sim will freeze) if this is the first time the `isaacsim.code_editor.jupyter` is enabled. Several Python dependencies will be installed.

- Once the extension is enabled, go to the top menu bar and click on Window > Jupyter Notebook to open a Jupyter app in the default web browser.

- In the Jupyter app, click on the Omniverse (Python 3) kernel (the one with the Omniverse logo) to create a new Untitled notebook.

- Execute code by clicking the Run button at the top of the notebook. Try it yourself with the same code snippet from above!
Warning

- The Omniverse (Python 3) kernel is designed to run Python code, via the `isaacsim.code_editor.jupyter` extension, on a running Isaac Sim instance (where the Kit application has control over the update/simulation loop).

- The Isaac Sim Python 3 kernel is used to run standalone applications (see Running Standalone Isaac Sim from Jupyter Notebook for more details).

[image: ../_images/isaac_tutorial_advanced_code_editors_jupyter.png]

Warning
Execution of blocking code freezes Isaac Sim.
Hint

- Use the Tab key for code autocompletion.

- Use the Ctrl + I keys for code introspection (display docstring if available).

Note
The notebooks are saved, by default, in a folder within the extension itself: `exts/isaacsim.code_editor.jupyter/data/notebooks`. See the location for Isaac Sim packages/extensions in Location for Isaac Sim app .
Limitations

- IPython magic commands are not available.

- Matplotlib plotting is not available in the notebooks.

- Printing, inside callbacks, is not displayed in the notebooks but in the Omniverse terminal.

## Running Standalone Isaac Sim from Jupyter Notebook
Warning

- This workflow is only supported on Linux.

### Configuration Files
In order for Isaac Sim to work inside of a Jupyter Notebook we provide a custom Jupyter kernel that is installed the first time you run `./jupyter_notebook.sh`. The kernel.json itself is fairly simple:

```
{
"argv": ["AUTOMATICALLY_REPLACED", "-m", "ipykernel_launcher", "-f", "{connection_file}"],
"display_name": "Isaac Sim Python 3",
"language": "python",
"env": {
"ISAAC_JUPYTER_KERNEL": "1"
},
"metadata": {
"debugger": true
}
}
```
The important part is that `AUTOMATICALLY_REPLACED` gets replaced by `jupyter_notebook.sh` with the absolute path to the Python executable that is located in the kit/python directory at runtime. Once the variable is replaced, the kernel is installed and the notebook is started. There is an extra variable `ISAAC_JUPYTER_KERNEL` that is used inside of Isaac Sim to setup for notebook usage properly.
Because notebooks require asyncio support, and Isaac Sim itself uses asyncio internally, we automatically execute the following two lines when loading the `isaacsim` module (or the `isaacsim.simulation_app` extension) which provides the `SimulationApp` class:

```
import nest_asyncio
nest_asyncio.apply()
```
This ensures that asyncio calls can be nested inside of the Jupyter Notebook properly.
When writing code in notebooks, it is necessary to first instantiate the `SimulationApp` class (from `isaacsim` or `isaacsim.simulation_app`) after perform any Isaac Sim / Omniverse imports:

```
from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": True})
# perform any Isaac Sim / Omniverse imports after instantiating the class
```
Then, to run the notebook just execute the following commands and play the notebook cells:

```
./jupyter_notebook.sh PATH_TO_NOTEBOOK.ipynb
```
