<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_math_8h_1abe8d732b98fef8d7e281916fc16b3a1c.html | title: roundNearest — Isaac Sim -->

# roundNearest
Fully qualified name: `isaacsim::core::includes::math::roundNearest`
inlinedoubleisaacsim ::core ::includes ::math ::roundNearest(
doubleinput,
doubleplace,
)
Rounds a number to the nearest multiple of a given value.
Rounds the input to the nearest multiple of the place value. For example, roundNearest(3.7, 0.5) returns 3.5.
Note
If place is 0, returns the input value unchanged
Parameters:

- input – [in] Value to round

- place – [in] Multiple to round to

Returns:
double The rounded value
