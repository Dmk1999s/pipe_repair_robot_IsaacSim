<!-- source: py/api/classomni_1_1kit_1_1_run_loop_synchronizer.html | title: RunLoopSynchronizer — Isaac Sim -->

# RunLoopSynchronizer
Fully qualified name: `omni::kit::RunLoopSynchronizer`
classRunLoopSynchronizer

Class for synchronizing multiple run loops.
Provides functionality to synchronize multiple threads or run loops to a common timing source, typically the present/render thread. Supports frame rate control and timing adjustments.
Public Functions
RunLoopSynchronizer()

~RunLoopSynchronizer()

voidpresentPreNotify()

Saves the present time and duration.

voidpresentPostNotify()

Notifies the condition variable in `wait` that it has to wake up.
Saves the syncronization point.

voidwait(
floatalreadyPassedNs,
size_tslidingMaximumCount,
size_tslidingMaximumOutlierCount,
floatslidingMaximumToleranceFactor,
)
Waits for the present thread and syncs the calling thread to the present thread.
This function calculates how long it needs to wait using a Sliding Maximum of the already passed time. It uses a high resolution clock to wait until the desired frame duration is met. It starts by obtaining the current time, and calculates the sliding maximum of the already passed time, ignoring a specified number of outliers. The function then determines if waiting is necessary by comparing the current time with the computed time point it should wake up at.
Parameters:

- alreadyPassedNs – The duration in nanoseconds that has already passed.

- slidingMaximumCount – The number of recent durations to consider when finding the sliding maximum.

- slidingMaximumOutlierCount – The number of outlier durations to ignore when finding the sliding maximum.

- slidingMaximumToleranceFactor – A multiplier for the average duration. Durations exceeding this are considered outliers.

voidsetTargetFPS(doublefps)

Sets the target frames per second.
Parameters:
fps – [in] Desired frame rate in frames per second

boolisActive()const

Checks if the synchronizer is active.
Returns:
True if synchronization is active, false otherwise

voidsetActive(boolactive)

Enables or disables synchronization.
Parameters:
active – [in] True to enable synchronization, false to disable
