<!-- source: overview/troubleshooting.html | title: Troubleshooting — Isaac Sim Documentation -->

# Troubleshooting
This page serves as a central hub for troubleshooting information across Isaac Sim components. For detailed troubleshooting guidance on specific components, follow the links below.

## Isaac Sim Issues

### Isaac Lab

### ROS 2 Troubleshooting

### Replicator

### Robot Setup

### Digital Twin

## Common Issues

### Installation Issues

#### Linux Driver Installation

- See Linux Troubleshooting to resolve driver installation issues on Linux.

- We recommend installing the Latest Production Branch Version drivers from the Unix Driver Archive using the `.run` installer on Linux, if you are on a new GPU or experiencing issues with current drivers.

- NVIDIA driver version 535.216.01 or later is recommended when upgrading to Ubuntu 22.04.5 kernel 6.8.0-48-generic or later.

### Performance Issues

#### Tracy Profiler
For performance troubleshooting, you can use the Tracy profiler to gauge the performance of various components of the application. See Profiling Performance Using Tracy for details on using Tracy for performance profiling.

#### Simulation Frame Rates
If you observe publish rates that differ from the target simulation frame rate, try:

- Running Isaac Sim with factory settings to clear any persistent simulation frame rate settings:

```
./isaac-sim.sh --reset-user
```

- Check your computer’s CPU usage to identify bottlenecks. If Isaac Sim is exhibiting incredibly high usage, try running with Fabric enabled.

#### Reducing Log Output
There can be many warnings and other messages when running Isaac Sim. You can reduce log output using command line arguments:

```
--/log/level=error --/log/fileLogLevel=error --/log/outputStreamLevel=error
```

### UI Issues
When the frame rate is low, the UI response may be sluggish. This can be resolved using “Ctrl + click” instead of the standard “click” to select objects.

### Windows-Specific Issues

#### Thread Cleanup
When running standalone examples in Windows, threads may not be properly cleaned up when the application is closed. This can usually be ignored because the application will still successfully close. As a workaround, add multiple `standalone_app.update()` calls before calling `standalone_app.close()`.

#### File Path Length
The `omni.kit.telemetry` extension startup error with code `(error = 206)` on Windows is caused by a file path exceeding the length limit. Verify that the file path of `omni.telemetry.transmitter.exe` does not exceed 260 characters.

#### GPU Overclocking
If you encounter the error message `Windows fatal exception: int divide by zero` once the app is started, it could be due to GPU overclocking software such as MSI Afterburner. Try disabling such software to resolve the issue.

### Python Issues
Python errors related to `tkinter` indicate the user is attempting to use `tkinter` with the Python distribution shipped with Isaac Sim. This is not supported.

## Additional Resources
For a comprehensive list of known issues and their workarounds, see Known Issues .
