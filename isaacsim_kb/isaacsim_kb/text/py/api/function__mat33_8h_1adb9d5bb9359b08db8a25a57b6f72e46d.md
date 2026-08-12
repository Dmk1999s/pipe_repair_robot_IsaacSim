<!-- source: py/api/function__mat33_8h_1adb9d5bb9359b08db8a25a57b6f72e46d.html | title: Outer — Isaac Sim -->

# Outer
inlineMatrix33 Outer(constVec3 &a, constVec3 &b)

Computes the outer product of two vectors.
Parameters:

- a – [in] First vector (column vector)

- b – [in] Second vector (treated as row vector)

Returns:
Matrix where result(i,j) = a[i] * b[j]
