<!-- source: py/source/extensions/isaacsim.benchmark.services/docs/api.html | title: API — Isaac Sim -->

# API

## Python API

[TABLE]
BaseIsaacBenchmarkAsync |
BaseIsaacBenchmark | Front-end for benchmarking standalone scripts and other non-async snippets.
[/TABLE]

classBaseIsaacBenchmarkAsync(*args:Any, **kwargs:Any)
Bases: `AsyncTestCase`
asyncfully_load_stage(usd_path)
Await this function to open a stage and then wait for it to fully load
Parameters:
usd_path (str) – Path to USD stage.

asyncsetUp(backend_type:str='JSONFileMetrics')
Must be awaited by derived benchmarks to properly set up the benchmark

set_phase(
phase:str,
start_recording_frametime:bool=True,
start_recording_runtime:bool=True,
)→None Sets benchmarking phase. Turns on frametime and runtime collection.
Parameters:

- phase (str) – Name of phase, used in output.

- start_recording_frametime (bool) – False to not start recording frametime at start of phase. Default True.

- start_recording_runtime (bool) – False to not start recording runtime at start of phase. Default True.

asyncstore_custom_measurement(
phase_name:str,
custom_measurement:<module'isaacsim.benchmark.services.metrics.measurements'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.benchmark.services/isaacsim/benchmark/services/metrics/measurements.py'>,
)→None Stores the custom measurement specificed in the benchmark.
Parameters:

- phase (str) – The phase name to which the measurement belongs.

- measurement (Measurement) – The measurement object to store.

asyncstore_measurements(
stop_recording_time:bool=True,
)→None Stores measurements, metadata, and artifacts collected by all recorders during the previous phase. Optionally, ends frametime and runtime collection.
Parameters:
stop_recording_time (bool) – False to not stop recording runtime and frametime at end of phase. Default True.

asynctearDown()
Must be awaited by derived benchmarks to properly tear down the benchmark

classBaseIsaacBenchmark(
benchmark_name:str='BaseIsaacBenchmark',
backend_type:str='OmniPerfKPIFile',
report_generation:bool=True,
workflow_metadata:dict={},
gpu_frametime:bool=False,
)Bases: `object`
Front-end for benchmarking standalone scripts and other non-async snippets.
By default this class will collect hardware performance data (see recorders), broken up by “phase”. Typical structure looks like:

```
benchmark = BaseIsaacBenchmark(benchmark_name=..., workflow_metadata=...)
benchmark.set_phase("loading")
# load stage, configure sim, etc.
benchmark.store_measurements()
benchmark.set_phase("benchmark")
# Actual code being benchmarked (running the sim for N frames, cloning an object, etc.)
benchmark.store_measurements()
benchmark.stop() # Shuts down benchmark, writes metrics to file
```
You can set any number of phases.
fully_load_stage(usd_path:str)→None
Loads provided USD stage, blocking execution until it is fully loaded.
Parameters:
usd_path (str) – Path to USD stage.

set_phase(
phase:str,
start_recording_frametime:bool=True,
start_recording_runtime:bool=True,
)→None Sets benchmarking phase. Turns on frametime and runtime collection.
Parameters:

- phase (str) – Name of phase, used in output.

- start_recording_frametime (bool) – False to not start recording frametime at start of phase. Default True.

- start_recording_runtime (bool) – False to not start recording runtime at start of phase. Default True.

stop()
Stop benchmarking and write accumulated metrics to file.

store_custom_measurement(
phase_name:str,
custom_measurement:<module'isaacsim.benchmark.services.metrics.measurements'from'/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.benchmark.services/isaacsim/benchmark/services/metrics/measurements.py'>,
)→None Stores the custom measurement specificed in the benchmark.
Parameters:

- phase (str) – The phase name to which the measurement belongs.

- measurement (Measurement) – The measurement object to store.

store_measurements(
stop_recording_time:bool=True,
)→None Stores measurements, metadata, and artifacts collected by all recorders during the previous phase. Optionally, ends frametime and runtime collection.
Parameters:
stop_recording_time (bool) – False to not stop recording runtime and frametime at end of phase. Default True.
