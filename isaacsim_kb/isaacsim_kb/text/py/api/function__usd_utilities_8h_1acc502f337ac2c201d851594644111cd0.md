<!-- source: py/api/function__usd_utilities_8h_1acc502f337ac2c201d851594644111cd0.html | title: setAttribute — Isaac Sim -->

# setAttribute
Fully qualified name: `isaacsim::core::includes::setAttribute`
template<classValueType>
inlineboolisaacsim ::core ::includes ::setAttribute(
constpxr ::UsdAttribute&attribute,
constValueType &val,
pxr ::UsdTimeCodetimeCode=pxr ::UsdTimeCode::Default(),
boolskipEqualSetForTimeSample=false,
boolautoTargetSessionLayer=true,
)
Sets attribute value with optional time sampling and session layer targeting.
Provides functionality to set USD attribute values with advanced features:

- Automatic session layer targeting for better edit workflow

- Time sample management and optimization

- Value comparison to avoid redundant writes

Note
For time-sampled attributes, will copy time samples from weaker layers if needed
Warning
Requires valid USD context and stage
Template Parameters:
ValueType – The data type of the attribute value

Parameters:

- attribute – [in] The USD attribute to set value on

- val – [in] The value to set

- timeCode – [in] Time code for time-sampled attributes (default: UsdTimeCode::Default())

- skipEqualSetForTimeSample – [in] Whether to skip setting if value is equal for time samples

- autoTargetSessionLayer – [in] Whether the edit target should auto switch to session layer

Returns:
True if the value was successfully set, false otherwise
