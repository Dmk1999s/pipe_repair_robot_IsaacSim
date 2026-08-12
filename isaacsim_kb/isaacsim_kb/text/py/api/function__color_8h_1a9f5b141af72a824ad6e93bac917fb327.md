<!-- source: py/api/function__color_8h_1a9f5b141af72a824ad6e93bac917fb327.html | title: distToRgba — Isaac Sim -->

# distToRgba
Fully qualified name: `isaacsim::core::includes::color::distToRgba`
staticinlinecarb::ColorRgbaisaacsim ::core ::includes ::color ::distToRgba(
doubleratio,
)
Converts a ratio value to a carb::ColorRgba struct.
Generates a color from the rainbow color spectrum (ROYGBIV) based on the input ratio. The ratio is mapped to six color regions, creating a smooth gradient transition between them. Similar to distToColor() but returns a different format.
Parameters:
ratio – [in] A value between 0.0 and 1.0 representing position in the color gradient

Returns:
carb::ColorRgba struct with values normalized to [0.0, 1.0] and alpha set to 1.0
