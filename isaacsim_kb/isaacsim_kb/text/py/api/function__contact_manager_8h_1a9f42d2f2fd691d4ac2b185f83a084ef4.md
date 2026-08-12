<!-- source: py/api/function__contact_manager_8h_1a9f42d2f2fd691d4ac2b185f83a084ef4.html | title: asInt — Isaac Sim -->

# asInt
Fully qualified name: `isaacsim::sensors::physics::asInt`
inlineuint64_tisaacsim ::sensors ::physics ::asInt(
constpxr ::SdfPath&path,
)
Converts a USD path to an integer representation.
Uses the same logic as SdfPath::_AsInt() to ensure path equality comparisons. Assumes sizeof(pxr::SdfPath) == sizeof(uint64_t).
Parameters:
path – [in] USD path to convert.

Returns:
Integer representation of the path.
