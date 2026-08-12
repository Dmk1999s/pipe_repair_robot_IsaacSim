<!-- source: py/api/function__mat22_8h_1a45e012df3e6d57c82d32a2da9b1c6932.html | title: Inverse — Isaac Sim -->

# Inverse
inlineMatrix22 Inverse(constMatrix22 &m, float&det)

Computes the inverse of a 2x2 matrix.
Calculates the matrix inverse using the analytical formula for 2x2 matrices. If the determinant is close to zero (within FLT_EPSILON), the matrix is considered singular and the original matrix is returned with determinant set to 0.
Note
If the matrix is singular (determinant near zero), the function returns the original matrix and sets det to 0.0f
Parameters:

- m – [in] Matrix to invert

- det – [out] Determinant of the input matrix

Returns:
Inverse matrix if invertible, otherwise the original matrix
