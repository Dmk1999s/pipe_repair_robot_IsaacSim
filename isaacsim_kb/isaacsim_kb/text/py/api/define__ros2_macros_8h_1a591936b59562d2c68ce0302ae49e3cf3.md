<!-- source: py/api/define__ros2_macros_8h_1a591936b59562d2c68ce0302ae49e3cf3.html | title: RCL_ERROR_MSG — Isaac Sim -->

# RCL_ERROR_MSG
RCL_ERROR_MSG(caller, called)

Macro for printing RCL errors with context.
Prints the current RCL error string as an ERROR level message, including information about where the error occurred. After printing, it resets the RCL error state to prevent error propagation.
Usage example:

```
if (rcl_operation_failed) {
RCL_ERROR_MSG(MyClass::MyMethod, rcl_operation);
return false;
}
```
Parameters:

- caller – The context where the error occurred (e.g., class, method, function)

- called – The RCL operation that failed
