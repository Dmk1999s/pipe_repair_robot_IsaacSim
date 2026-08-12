<!-- source: py/api/function__mat33_8h_1abd202588d8f9fcecb476eab22e554efe.html | title: Skew — Isaac Sim -->

# Skew
inlineMatrix33 Skew(constVec3 &v)

Creates a skew-symmetric matrix from a vector.
Useful for representing cross products as matrix operations
Parameters:
v – [in] Input vector

Returns:
Skew-symmetric matrix such that result * x = v × x for any vector x
