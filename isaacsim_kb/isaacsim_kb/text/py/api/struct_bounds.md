<!-- source: py/api/struct_bounds.html | title: Bounds — Isaac Sim -->

# Bounds
structBounds

Axis-aligned bounding box representation using lower and upper corner points.
This structure represents a 3D axis-aligned bounding box (AABB) defined by two corner points: lower and upper. It provides methods for computing geometric properties, expanding the bounds, and testing for overlaps with points and other bounds.
The bounds can be in an empty state where lower > upper, which is useful for initialization and union operations.
Public Functions
inlineBounds()

Default constructor creating empty bounds.
Initializes the bounds to an empty state where lower is set to positive infinity and upper is set to negative infinity. This allows subsequent union operations to work correctly.

inlineBounds(constVec3 &lower, constVec3 &upper)

Constructor creating bounds from lower and upper corner points.
Parameters:

- lower – [in] The lower corner point of the bounds

- upper – [in] The upper corner point of the bounds

inlineVec3 GetCenter()const

Computes the center point of the bounds.
Returns:
The center point as a Vec3

inlineVec3 GetEdges()const

Computes the dimensions (extents) of the bounds.
Returns:
The dimensions as a Vec3 representing width, height, and depth

inlinevoidExpand(floatr)

Expands the bounds by a uniform amount in all directions.
Parameters:
r – [in] The amount to expand by in all directions

inlinevoidExpand(constVec3 &r)

Expands the bounds by different amounts in each direction.
Parameters:
r – [in] The amounts to expand by in each direction (x, y, z)

inlineboolEmpty()const

Checks if the bounds are empty.
Returns:
True if the bounds are empty (lower >= upper in any dimension), false otherwise

inlineboolOverlaps(constVec3 &p)const

Tests if a point overlaps with the bounds.
Parameters:
p – [in] The point to test

Returns:
True if the point is inside or on the boundary of the bounds, false otherwise

inlineboolOverlaps(constBounds &b)const

Tests if another bounds overlaps with this bounds.
Parameters:
b – [in] The other bounds to test against

Returns:
True if the bounds overlap or touch, false otherwise

Public Members
Vec3 lower

The lower corner point of the bounds.

Vec3 upper

The upper corner point of the bounds.
