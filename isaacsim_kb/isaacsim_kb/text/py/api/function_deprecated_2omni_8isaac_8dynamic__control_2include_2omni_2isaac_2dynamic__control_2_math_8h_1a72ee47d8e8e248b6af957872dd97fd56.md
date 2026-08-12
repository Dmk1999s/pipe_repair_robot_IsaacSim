<!-- source: py/api/function_deprecated_2omni_8isaac_8dynamic__control_2include_2omni_2isaac_2dynamic__control_2_math_8h_1a72ee47d8e8e248b6af957872dd97fd56.html | title: operator* — Isaac Sim -->

# operator*
Fully qualified name: `omni::isaac::dynamic_control::math::operator*`
inlineomni ::isaac ::dynamic_control ::DcTransform omni ::isaac ::dynamic_control ::math ::operator*(
constomni ::isaac ::dynamic_control ::DcTransform &self,
constomni ::isaac ::dynamic_control ::DcTransform &other,
)
Multiplies two transforms to compose them.
Combines two transforms by applying them in sequence. The order of multiplication matters (non-commutative).
Note
The resulting transform applies other first, then self
Parameters:

- self – [in] First transform (applied second)

- other – [in] Second transform (applied first)

Returns:
DcTransform The composed transform
