<!-- source: py/api/class_colour.html | title: Colour — Isaac Sim -->

# Colour
classColour

RGBA color representation with floating point components.
This class represents a color using red, green, blue, and alpha components as floating point values. It provides various constructors for different color representations and arithmetic operators for color manipulation.
Color components are typically in the range [0.0, 1.0], though values outside this range are supported for HDR operations.
Public Types
enumPreset

Predefined color presets.
Enumeration of common colors for convenience.
Values:
enumeratorkRed

Pure red color (1.0, 0.0, 0.0, 1.0).

enumeratorkGreen

Pure green color (0.0, 1.0, 0.0, 1.0).

enumeratorkBlue

Pure blue color (0.0, 0.0, 1.0, 1.0).

enumeratorkWhite

Pure white color (1.0, 1.0, 1.0, 1.0).

enumeratorkBlack

Pure black color (0.0, 0.0, 0.0, 1.0).

Public Functions
inlineColour(
floatr_=0.0f,
floatg_=0.0f,
floatb_=0.0f,
floata_=1.0f,
)
Default constructor with optional RGBA values.
Parameters:

- r_ – [in] Red component (default: 0.0)

- g_ – [in] Green component (default: 0.0)

- b_ – [in] Blue component (default: 0.0)

- a_ – [in] Alpha component (default: 1.0)

inlineColour(float*p)

Constructor from float array.
Parameters:
p – [in] Array of 4 floats representing RGBA values

inlineColour(uint32_trgba)

Constructor from packed 32-bit RGBA value.
Parameters:
rgba – [in] Packed RGBA value in format 0xRRGGBBAA

inlineColour(Preset p)

Constructor from color preset.
Parameters:
p – [in] Predefined color preset

inlineoperatorconstfloat*()const

Conversion operator to const float pointer.
Returns:
Pointer to the first color component

inlineoperatorfloat*()

Conversion operator to float pointer.
Returns:
Pointer to the first color component

inlineColour operator*(floatscale)const

Scalar multiplication operator.
Parameters:
scale – [in] Scalar value to multiply all components by

Returns:
New color with scaled components

inlineColour operator/(floatscale)const

Scalar division operator.
Parameters:
scale – [in] Scalar value to divide all components by

Returns:
New color with divided components

inlineColour operator+(constColour &v)const

Color addition operator.
Parameters:
v – [in] Color to add

Returns:
New color with added components

inlineColour operator-(constColour &v)const

Color subtraction operator.
Parameters:
v – [in] Color to subtract

Returns:
New color with subtracted components

inlineColour operator*(constColour &scale)const

Component-wise color multiplication operator.
Parameters:
scale – [in] Color to multiply with component-wise

Returns:
New color with multiplied components

inlineColour &operator*=(floatscale)

In-place scalar multiplication operator.
Parameters:
scale – [in] Scalar value to multiply all components by

Returns:
Reference to this color after multiplication

inlineColour &operator/=(floatscale)

In-place scalar division operator.
Parameters:
scale – [in] Scalar value to divide all components by

Returns:
Reference to this color after division

inlineColour &operator+=(constColour &v)

In-place color addition operator.
Parameters:
v – [in] Color to add

Returns:
Reference to this color after addition

inlineColour &operator-=(constColour &v)

In-place color subtraction operator.
Parameters:
v – [in] Color to subtract

Returns:
Reference to this color after subtraction

inlineColour &operator*=(constColour &v)

In-place component-wise color multiplication operator.
Parameters:
v – [in] Color to multiply with component-wise

Returns:
Reference to this color after multiplication

Public Members
floatr

Red color component.

floatg

Green color component.

floatb

Blue color component.

floata

Alpha (transparency) component.
