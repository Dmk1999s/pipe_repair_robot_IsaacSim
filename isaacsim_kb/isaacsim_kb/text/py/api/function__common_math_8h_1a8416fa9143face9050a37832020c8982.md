<!-- source: py/api/function__common_math_8h_1a8416fa9143face9050a37832020c8982.html | title: Clamp — Isaac Sim -->

# Clamp
template<typenameT>
inlineT Clamp(T a, T low, T high)

Clamps a value between a minimum and maximum range.
If low > high, the values are swapped before clamping
Template Parameters:
T – Type of the values

Parameters:

- a – [in] Value to clamp

- low – [in] Minimum allowed value

- high – [in] Maximum allowed value

Returns:
Clamped value in the range [low, high]
