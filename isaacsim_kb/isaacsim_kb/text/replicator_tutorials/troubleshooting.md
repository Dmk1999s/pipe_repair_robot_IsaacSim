<!-- source: replicator_tutorials/troubleshooting.html | title: Replicator Troubleshooting — Isaac Sim Documentation -->

# Replicator Troubleshooting
This page consolidates troubleshooting information for Replicator components in Isaac Sim.

## Replicator Rendering Issues
If there is unwanted noise in simulated depth images, disable anti-aliasing under the Render Settings > Ray Tracing > Anti-Aliasing tab by setting the `Algorithm` to `None`.
If randomized materials are not loaded on time for synthetic data generation, the rt_subframes must be set to be at least `2`.
The replicator Scatter3D OmniGraph node breaks physics when called on a stage using world. Avoid using these together or use alternative methods for object placement.
If ghosting artifacts are observed in the captured data, especially for scenes with moving objects or significant changes in lighting conditions, increase the `rt_subframes` value when capturing the data to a value until the renderer is able to remove the artifacts. For more information see RT Subframes Parameter and subframes examples .
If the captured images are written as black, try starting Isaac Sim once with the `--reset-user` to clear any previous user settings.

## Async Rendering and Frame Skipping
When using Replicator, frames may be skipped due to the `isaacsim.core.throttling` extension toggling `/app/asyncRendering=True` by default when the timeline is stopped. Since Replicator remains in STARTED mode, it does not re-initialize and toggle the setting back to False, leading to frames being skipped during capture.
Solution: Launch Isaac Sim with the following flag to disable async rendering toggling from the throttling extension:

```
--/exts/isaacsim.core.throttling/enable_async=false
```
This occurs because when the timeline is stopped, the throttling extension enables async rendering for performance. However, when Replicator schedules frames for capture before the timeline starts playing again, those frames may be skipped due to async rendering being enabled. The flag above prevents the throttling extension from toggling async rendering, ensuring all scheduled frames are captured properly.

## Replicator Data Storage Issues
Using Replicator to write to S3 buckets with the built-in backend in Windows may require setting the credentials in the environment variables instead of the AWS config files. This is because of a possible path parsing error in Boto3 on Windows.
When working with large datasets or high-resolution images, you may experience storage bottlenecks. Consider: 1. Using a faster storage device 2. Reducing the image resolution or compression level 3. Using batch processing with smaller batches

## Replicator Layers and Randomization
Using replicator ’s `rep.new_layer()` functionality, which creates a new layer in which to place and randomize assets, may lead to issues in simulation scenarios where these assets are used. In such cases the use of `rep.new_layer()` can be omitted.
When using multiple randomizers, be aware that they may conflict with each other. Test your randomization settings carefully to ensure they produce the expected results.

## Replicator Performance Issues
For complex scenes with many objects and randomizers, you may experience performance issues. Consider: 1. Reducing the number of objects in the scene 2. Simplifying the randomization parameters 3. Using fewer sensors or lower resolution sensors 4. Running with headless mode for improved performance during data generation

## Replicator API Changes
If you are encountering any issues regarding the dependencies on `omni.replicator.character` or `omni.replicator.agent`, the extension is now renamed to `isaacsim.replicator.agent`. Revise your code accordingly.

## Getting Started Scripts Issues
Common issues and solutions for the Getting Started Scripts:

- Data not being captured - Ensure the capture-on-play flag is properly set - Check if the render products are correctly attached to writers - Verify the output directory has write permissions

- Rendering artifacts - Try increasing RTSubframes value - Check if materials are fully loaded before capture - Ensure proper lighting setup

- Performance issues - Reduce resolution or number of cameras - Use headless mode for faster processing - Optimize scene complexity

- Memory issues - Reduce batch size - Clear unused resources with `destroy()` - Monitor GPU memory usage
