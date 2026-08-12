<!-- source: py/api/function__common_math_8h_1a6efee2e3c659d9493b4c4045acec79d2.html | title: Lerp — Isaac Sim -->

# Lerp
template<typenameV,typenameT>
inlineV Lerp(
constV &start,
constV &end,
constT &t,
)
Performs linear interpolation between two values.
Template Parameters:

- V – Type of the values to interpolate

- T – Type of the interpolation parameter

Parameters:

- start – [in] Starting value (when t = 0)

- end – [in] Ending value (when t = 1)

- t – [in] Interpolation parameter

Returns:
Interpolated value: start + (end - start) * t
