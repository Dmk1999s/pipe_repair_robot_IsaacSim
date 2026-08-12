<!-- source: py/api/function__vec2_8h_1abe1d2e4c960e6739e5f856af8ebff1c3.html | title: PerpCCW — Isaac Sim -->

# PerpCCW
template<typenameT>
XVector2 <T >PerpCCW(constXVector2 <T >&v)

Returns the counter-clockwise perpendicular vector.
For a vector (x, y), returns (-y, x).
Template Parameters:
T – The component type of the vector.

Parameters:
v – [in] The input vector.

Returns:
A new XVector2 rotated 90 degrees counter-clockwise.
