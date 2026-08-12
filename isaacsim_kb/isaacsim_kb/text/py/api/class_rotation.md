<!-- source: py/api/class_rotation.html | title: Rotation — Isaac Sim -->

# Rotation
classRotation

Euler angle representation of 3D rotation.
This class encapsulates a 3D orientation using Euler angles (yaw, pitch, roll). While not as robust as quaternions for rotations, it provides an intuitive interface for manipulating object orientations, especially from scripting contexts.
All angles are stored in degrees for convenience in editing and visualization.
Note
Euler angles can suffer from gimbal lock and are order-dependent.
Warning
Be careful with angle accumulation to avoid numerical drift.
Public Functions
inlineRotation()

Default constructor creating zero rotation.
Creates a rotation with all angles set to zero (identity rotation).

inlineRotation(floatinYaw, floatinPitch, floatinRoll)

Constructor with explicit angle values.
Parameters:

- inYaw – [in] Yaw angle in degrees (rotation around Y-axis)

- inPitch – [in] Pitch angle in degrees (rotation around Z-axis)

- inRoll – [in] Roll angle in degrees (rotation around X-axis)

inlineRotation &operator+=(constRotation &rhs)

In-place addition operator.
Parameters:
rhs – [in]Rotation to add

Returns:
Reference to this rotation after addition

inlineRotation &operator-=(constRotation &rhs)

In-place subtraction operator.
Parameters:
rhs – [in]Rotation to subtract

Returns:
Reference to this rotation after subtraction

inlineRotation operator+(constRotation &rhs)const

Addition operator.
Parameters:
rhs – [in]Rotation to add

Returns:
New rotation with added angles

inlineRotation operator-(constRotation &rhs)const

Subtraction operator.
Parameters:
rhs – [in]Rotation to subtract

Returns:
New rotation with subtracted angles

Public Members
floatyaw

Yaw angle in degrees (rotation around Y-axis).

floatpitch

Pitch angle in degrees (rotation around Z-axis).

floatroll

Roll angle in degrees (rotation around X-axis).
