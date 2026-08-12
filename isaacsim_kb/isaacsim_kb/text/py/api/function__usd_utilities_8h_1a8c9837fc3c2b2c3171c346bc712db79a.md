<!-- source: py/api/function__usd_utilities_8h_1a8c9837fc3c2b2c3171c346bc712db79a.html | title: getAttributeEffectiveTimeSampleLayerInfo — Isaac Sim -->

# getAttributeEffectiveTimeSampleLayerInfo
Fully qualified name: `isaacsim::core::includes::getAttributeEffectiveTimeSampleLayerInfo`
inlineTimeSamplesOnLayer isaacsim ::core ::includes ::getAttributeEffectiveTimeSampleLayerInfo(
constpxr ::UsdStage&stage,
constpxr ::UsdAttribute&attr,
pxr ::SdfLayerRefPtr*outLayer=nullptr,
)
check if attribute has efficient timesample and these data are on currentlayer/strongerlayer/weakerlayer
Parameters:

- stage – [in] Current Working Stage.

- attr – [in] The attribute to check.

- outLayer – [out] Optional pointer to receive the layer containing time samples

Returns:
TimeSamplesOnLayer enum indicating where time samples are located
