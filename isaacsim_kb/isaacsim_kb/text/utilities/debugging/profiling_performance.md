<!-- source: utilities/debugging/profiling_performance.html | title: Profiling Performance Using Tracy — Isaac Sim Documentation -->

# Profiling Performance Using Tracy

## Learning Objectives
This tutorial shows how to get a high-level live CPU/GPU performance overview of NVIDIA Isaac Sim using the Tracy profiler.
After this tutorial, you will be able to gauge the performance of various components of the application, add profiling zones and understand the relative significance of each zone.
15-20 Minutes Tutorial

## Getting Started
Prerequisites

- Review the Core API Hello World and GUI Tutorial series Troubleshooting prior to beginning this tutorial.

- Have an understanding of various workflows. Refer to Workflows for details.

## Launching Tracy Profiler
The first step of profiling the application is to open the Tracy profiler. There are a few different ways to do this.

- It is recommended to use the Tracy binary that comes with NVIDIA Isaac Sim. To do this, you need to enable the `omni.kit.profiler.tracy` extension from the registry which contains the currently supported version of Tracy. To do this, navigate to Windows > Extensions, search for `omni.kit.profiler.tracy` extension and enable it. If you need the extension to be enabled by default, you can check the AUTOLOAD box as well. This will add a new Profiler menu item from where you can Launch the profiler or Launch and Connect an instance of the Tracy UI and stream the output of the NVIDIA Isaac Sim to it.

- Another convenient approach to open the Tracy applicaton is to use the binary that is used by the `omni.kit.profiler.tracy` extension manually. The binary is located inside the extension folder, e.g.

```
./extscache/omni.kit.profiler.tracy-1.2.0+lx64/bin/Tracy
```

Note
You can keep using the same instance of the profiler even if you close the NVIDIA Isaac Sim application. This is useful to keep Tracy profiler ready when you profile the Application in the standalone workflow.

## Using Tracy Profiler

### GUI Workflow

- Enable/Open Tracy based on the instructions above.

- Launch and Connect the Tracy profiler will open the profiler windows. Press Stop in the profiler window to stop the profiler. You can press Save trace from the “net icon” to save the trace file.

### Standalone Workflow
The easiest way to enable Tracy profiling with its default behavior is to launch your standalone script with `--enable omni.kit.profiler.tracy` as

```
python.sh PATH_TO_STANDALONE_EXAMPLE --enable omni.kit.profiler.tracy
```
Note that you need to change the `SimulationApp` parameters of your standalone script to include the necessary profiler_backend parameter as follows.

```
from isaacsim import SimulationApp
simulation_app = SimulationApp({"headless": False, "profiler_backend": ["tracy"]})
# Add your standalone script here
```
Once the application is running you can Launch and Connect the Tracy profiler to get the live performance data.
Note
If you are running in headless mode you can still use the Tracy profiler by clicking on Connect in the profiler window once the application runs. However, you should keep a Tracy window running with one of the previous methods to be able to do this.
For more fine-grained control, it is possible to customize the profiler output by adding additional command line arguments which works similarly for any kit-based app. For instance, you can run a standalone example with Tracy enabled as follows:

```
python.sh PATH_TO_STANDALONE_EXAMPLE --enable omni.kit.profiler.tracy \
--/profiler/enabled=true \
--/app/profilerBackend=tracy \
--/privacy/externalBuild=0 \
--/app/profileFromStart=true \
--/profiler/gpu=true \
--/profiler/gpu/tracyInject/enabled=true
--/profiler/gpu/tracyInject/msBetweenClockCalibration=0 \
--/app/profilerMask=1 \
--/profiler/channels/carb.tasking/enabled=false \
--/profiler/channels/carb.events/enabled=false \
--/plugins/carb.profiler-tracy.plugin/fibersAsThreads=false
```
Note
Above `--/profiler/enabled` and `--/app/profilerBackend` are the only necessary command line arguments, and the rest are optional parameters to customize the profiler output. `--/privacy/externalBuild=0` is necessary to capture traces with F5 key.
All these parameters (with the default values mentioned above) are already included in the first method described above.

## Adding Profiling Zones

### Python
To add profiler zones in your Python script, you can use the `@carb.profiler.profile` function decorator to add a zone for a specific function.

```
import carb
@carb.profiler.profile
def some_function():
# function code here
```
More fine-grained control can be achieved by encapsulating the required code in a pair of `carb.profiler.begin` and `carb.profiler.end` calls to manually start and stop a zone as follows:

```
import carb
def some_function():
# Some code that shouldn't be included in the profiler zone
carb.profiler.begin(1, "zone title")
# code to profile
carb.profiler.end(1)
```

### C++
To add profiler zones in your C++ code, you can use the `CARB_PROFILE_ZONE` macro to add a zone for a specific scope as follows:

```
#include <carb/logging/Log.h>
void some_function() {
CARB_PROFILE_ZONE("zone title");
{
// code to profile
}
}
```

## Summary
This tutorial covered the following topics:

- How to use the Tracy profiler in NVIDIA Isaac Sim in both GUI and standalone workflows.

- How to add new profiling zones to gauge the performance of your code Python and C++.
