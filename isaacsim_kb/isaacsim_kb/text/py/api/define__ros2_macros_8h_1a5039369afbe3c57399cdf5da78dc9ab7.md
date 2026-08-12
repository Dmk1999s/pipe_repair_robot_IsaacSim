<!-- source: py/api/define__ros2_macros_8h_1a5039369afbe3c57399cdf5da78dc9ab7.html | title: RCL_WARN_MSG — Isaac Sim -->

# RCL_WARN_MSG
RCL_WARN_MSG(caller, called)

Macro for printing RCL warnings with context.
Prints the current RCL error string as a WARNING level message, including information about where the warning occurred. After printing, it resets the RCL error state to prevent warning propagation.
Usage example:

```
if (rcl_operation_suspicious) {
RCL_WARN_MSG(MyClass::MyMethod, rcl_operation);
// continue execution
}
```
Parameters:

- caller – The context where the warning occurred (e.g., class, method, function)

- called – The RCL operation that triggered the warning
