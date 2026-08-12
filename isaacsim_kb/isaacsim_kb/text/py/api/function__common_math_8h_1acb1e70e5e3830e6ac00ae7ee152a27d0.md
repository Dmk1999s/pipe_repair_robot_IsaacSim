<!-- source: py/api/function__common_math_8h_1acb1e70e5e3830e6ac00ae7ee152a27d0.html | title: SafeNormalize — Isaac Sim -->

# SafeNormalize
template<typenameT>
inlineT SafeNormalize(
constT &v,
constT &fallback=T (),
)
Safely normalizes a vector with fallback for zero-length vectors.
Template Parameters:
T – Vector type that supports LengthSq(), multiplication, and InvSqrt()

Parameters:

- v – [in] Vector to normalize

- fallback – [in] Fallback vector to return if v has zero length (default: default-constructed T)

Returns:
Normalized vector if length > 0, fallback vector otherwise
