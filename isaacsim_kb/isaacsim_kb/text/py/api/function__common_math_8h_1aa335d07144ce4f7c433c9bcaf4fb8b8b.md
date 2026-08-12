<!-- source: py/api/function__common_math_8h_1aa335d07144ce4f7c433c9bcaf4fb8b8b.html | title: Normalize — Isaac Sim -->

# Normalize
template<typenameT>
T Normalize(constT &v)

Normalizes a vector to unit length.
Template Parameters:
T – Vector type that supports division by scalar and Length() function

Parameters:
v – [in] Vector to normalize

Returns:
Normalized vector with unit length

Pre:
Length(v) > 0
