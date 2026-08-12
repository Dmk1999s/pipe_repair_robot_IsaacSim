<!-- source: py/api/function__usd_utilities_8h_1a5026e6e02a457759235f58ffe0a449aa.html | title: safeGetAttribute — Isaac Sim -->

# safeGetAttribute
Fully qualified name: `isaacsim::core::includes::safeGetAttribute`
template<classT>
voidisaacsim ::core ::includes ::safeGetAttribute(
constpxr ::UsdAttribute&attr,
T &inputValue,
)
Safely retrieves a USD attribute value with error handling.
Provides a safe way to get attribute values with:

- Value existence checking

- Type-safe value retrieval

Note
Logs a warning if attribute exists but has no value
Warning
Input value remains unchanged if attribute has no value
Template Parameters:
T – Type of the attribute value to retrieve

Parameters:

- attr – [in] USD attribute to read

- inputValue – [out] Variable to store the attribute value
