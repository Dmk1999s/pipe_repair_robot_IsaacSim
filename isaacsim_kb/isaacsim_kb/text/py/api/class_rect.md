<!-- source: py/api/class_rect.html | title: Rect — Isaac Sim -->

# Rect
classRect

2D rectangle representation using integer coordinates.
This class represents a 2D rectangle defined by left, right, top, and bottom boundaries using integer coordinates. It provides methods for computing dimensions, expanding the rectangle, and testing point containment.
The coordinate system assumes that left < right and top < bottom.
Public Functions
inlineRect()

Default constructor creating a zero-sized rectangle.
Creates a rectangle with all boundaries set to zero.

inlineRect(
uint32_tleft,
uint32_tright,
uint32_ttop,
uint32_tbottom,
)
Constructor with explicit boundary values.
Parameters:

- left – [in] Left boundary coordinate

- right – [in] Right boundary coordinate

- top – [in] Top boundary coordinate

- bottom – [in] Bottom boundary coordinate

Pre:
left <= right and top <= bottom

inlineuint32_tWidth()const

Computes the width of the rectangle.
Returns:
Width as the difference between right and left boundaries

inlineuint32_tHeight()const

Computes the height of the rectangle.
Returns:
Height as the difference between bottom and top boundaries

inlinevoidExpand(uint32_tx)

Expands the rectangle by a uniform amount in all directions.
Warning
This operation may cause underflow if x is larger than the boundaries.
Parameters:
x – [in] Amount to expand by in each direction

inlineuint32_tLeft()const

Gets the left boundary coordinate.
Returns:
Left boundary value

inlineuint32_tRight()const

Gets the right boundary coordinate.
Returns:
Right boundary value

inlineuint32_tTop()const

Gets the top boundary coordinate.
Returns:
Top boundary value

inlineuint32_tBottom()const

Gets the bottom boundary coordinate.
Returns:
Bottom boundary value

inlineboolContains(uint32_tx, uint32_ty)const

Tests if a point is contained within the rectangle.
Parameters:

- x – [in] X-coordinate of the point to test

- y – [in] Y-coordinate of the point to test

Returns:
True if the point is inside or on the boundary of the rectangle, false otherwise

Public Members
uint32_tm_left

Left boundary coordinate.

uint32_tm_right

Right boundary coordinate.

uint32_tm_top

Top boundary coordinate.

uint32_tm_bottom

Bottom boundary coordinate.
