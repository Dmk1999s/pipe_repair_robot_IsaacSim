<!-- source: py/api/classisaacsim_1_1core_1_1includes_1_1_scoped_timer.html | title: ScopedTimer — Isaac Sim -->

# ScopedTimer
Fully qualified name: `isaacsim::core::includes::ScopedTimer`
classScopedTimer

RAII-style performance timer for code block measurement.
Provides automatic timing of code blocks using RAII principles. Measures elapsed time between construction and destruction, automatically printing the results with a custom message.
Features:

- High-resolution timing using std::chrono::steady_clock

- Automatic measurement of scoped blocks

- Custom message support for timing identification

- Millisecond precision output

Example usage:

```
{
ScopedTimer timer("Operation X");
// Code to measure...
} // Timer automatically prints duration when scope ends
```
Note
Uses steady_clock for most reliable timing measurements
Warning
Output is sent to std::cout, which may affect timing of very short operations
Public Functions
inlineScopedTimer(conststd ::string&message)

Constructs a timer with an identifying message.
Starts the timer immediately upon construction and stores the message for later output when the timer is destroyed.
Note
The message will be printed with the elapsed time when the timer is destroyed
Parameters:
message – [in] Descriptive message to identify this timing measurement

inline~ScopedTimer()

Destructor that prints the elapsed time.
Automatically calculates and prints the elapsed time since construction. Output format: “<message> : <elapsed_time_ms>”
Note
Time is reported in milliseconds with floating-point precision
