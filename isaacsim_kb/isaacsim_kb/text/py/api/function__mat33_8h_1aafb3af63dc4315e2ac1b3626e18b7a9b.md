<!-- source: py/api/function__mat33_8h_1aafb3af63dc4315e2ac1b3626e18b7a9b.html | title: Inverse — Isaac Sim -->

# Inverse
inlineMatrix33 Inverse(constMatrix33 &a, bool&success)

Computes the inverse of a 3x3 matrix using single precision.
Uses cofactor method with single precision arithmetic
Parameters:

- a – [in] Matrix to invert

- success – [out] Set to true if inversion succeeded, false if matrix is singular

Returns:
Inverse matrix if successful, uninitialized matrix if failed
