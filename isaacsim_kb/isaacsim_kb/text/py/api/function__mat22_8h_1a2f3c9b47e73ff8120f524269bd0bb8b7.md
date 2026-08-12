<!-- source: py/api/function__mat22_8h_1a2f3c9b47e73ff8120f524269bd0bb8b7.html | title: PolarDecomposition — Isaac Sim -->

# PolarDecomposition
inlineMatrix22 PolarDecomposition(constMatrix22 &m)

Performs polar decomposition of a 2x2 matrix.
Decomposes the matrix into an orthogonal (rotation) matrix using an optimized analytical method. The decomposition finds the closest orthogonal matrix to the input matrix.
Note
This implementation uses an analytical approach rather than the iterative method shown in comments
Parameters:
m – [in] Matrix to decompose

Returns:
Orthogonal matrix from the polar decomposition
