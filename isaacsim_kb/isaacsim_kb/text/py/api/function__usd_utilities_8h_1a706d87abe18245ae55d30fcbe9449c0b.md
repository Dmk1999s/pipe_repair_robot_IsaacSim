<!-- source: py/api/function__usd_utilities_8h_1a706d87abe18245ae55d30fcbe9449c0b.html | title: getCameraAttributeFromRenderProduct — Isaac Sim -->

# getCameraAttributeFromRenderProduct
Fully qualified name: `isaacsim::core::includes::getCameraAttributeFromRenderProduct`
inlinepxr ::UsdAttributeisaacsim ::core ::includes ::getCameraAttributeFromRenderProduct(
conststd ::string&attributeString,
conststd ::string&renderProductPathString,
)
Retrieves a specific attribute from a camera associated with a render product.
Combines camera prim lookup with attribute access in a single function. Process:

- Gets the camera prim from render product

- Validates the camera prim

- Retrieves the requested attribute

See also
getCameraPrimFromRenderProduct
Note
Returns invalid attribute if camera prim is invalid
Parameters:

- attributeString – [in] Name of the attribute to retrieve

- renderProductPathString – [in] Path to the render product

Returns:
pxr::UsdAttribute The requested attribute if found, invalid attribute otherwise
