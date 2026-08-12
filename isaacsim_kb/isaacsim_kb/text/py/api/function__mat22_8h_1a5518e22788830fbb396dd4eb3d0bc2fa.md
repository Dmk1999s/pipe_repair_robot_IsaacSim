<!-- source: py/api/function__mat22_8h_1a5518e22788830fbb396dd4eb3d0bc2fa.html | title: QRDecomposition — Isaac Sim -->

# QRDecomposition
inlineMatrix22 QRDecomposition(constMatrix22 &m)

Performs QR decomposition of a 2x2 matrix.
Decomposes the matrix into an orthogonal matrix Q. This implementation normalizes the first column and creates an orthogonal matrix using the perpendicular vector.
Note
This function only returns the Q component of the QR decomposition
Parameters:
m – [in] Matrix to decompose

Returns:
Orthogonal matrix Q from the QR decomposition
