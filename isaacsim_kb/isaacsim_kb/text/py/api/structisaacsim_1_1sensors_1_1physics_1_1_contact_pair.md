<!-- source: py/api/structisaacsim_1_1sensors_1_1physics_1_1_contact_pair.html | title: ContactPair — Isaac Sim -->

# ContactPair
Fully qualified name: `isaacsim::sensors::physics::ContactPair`
structContactPair

Represents a pair of bodies in contact.
Stores and manages the identifiers of two bodies involved in a contact. Ensures consistent ordering by keeping the smaller ID in body0.
Public Functions
inlineContactPair(uint64_tb0, uint64_tb1)

Constructor from two body IDs.
Parameters:

- b0 – [in] First body ID.

- b1 – [in] Second body ID.

inlineContactPair(pxr ::SdfPathb0, pxr ::SdfPathb1)

Constructor from two USD paths.
Parameters:

- b0 – [in] First body’s USD path.

- b1 – [in] Second body’s USD path.

inlineContactPair(CsRawData d)

Constructor from raw contact data.
Parameters:
d – [in] Raw contact data containing body IDs.

inlinebooloperator==(ContactPair rhs)const

Equality comparison operator.
Parameters:
rhs – [in] Right-hand side contact pair to compare with.

Returns:
True if both pairs represent the same contact.

Public Members
uint64_tbody0

First body in the contact pair (always has the smaller ID).

uint64_tbody1

Second body in the contact pair.
