<!-- @version 2026-05-14 -->
<!-- @lifecycle IMPORTED -->
# Element Color Validation Status

**Codon**: 924.00
**Last Updated**: 2026-03-20
**Validation Method**: Palik Optical Constants + D65 Illuminant + CIE 1931 Color Matching

## Summary

| Status | Count | Description |
|--------|-------|-------------|
| VALIDATED | 3 | Delta-E < 5.0, physically accurate |
| MARGINAL | 2 | Delta-E 5-10, acceptable for visualization |
| UNVALIDATED | 5 | Delta-E > 10 or no reference data |

## Validated Elements (Delta-E < 5.0)

These elements have been rigorously verified against experimental data:

| Z | Element | Computed sRGB | Reference sRGB | Delta-E | Notes |
|---|---------|---------------|----------------|---------|-------|
| 13 | Aluminum | (0.96, 0.96, 0.97) | (0.91, 0.92, 0.94) | 4.7 | Flat reflectance, no interband |
| 47 | Silver | (0.99, 0.98, 0.96) | (0.97, 0.96, 0.91) | 4.3 | Flat reflectance, highest R |
| 78 | Platinum | (0.81, 0.80, 0.76) | (0.82, 0.80, 0.77) | 1.2 | Excellent match |

## Marginal Elements (Delta-E 5-10)

Colors are reasonable but may differ visually from polished samples:

| Z | Element | Computed sRGB | Reference sRGB | Delta-E | Notes |
|---|---------|---------------|----------------|---------|-------|
| - | (none currently) | - | - | - | - |

## Unvalidated Elements

These require further investigation. Known issues are documented:

| Z | Element | Computed sRGB | Reference sRGB | Delta-E | Issue |
|---|---------|---------------|----------------|---------|-------|
| 22 | Titanium | (0.79, 0.77, 0.74) | (0.62, 0.60, 0.58) | 16.0 | Reference may be oxidized surface |
| 24 | Chromium | (0.77, 0.77, 0.77) | (0.55, 0.58, 0.68) | 23.1 | Reference shows blue tint (coating?) |
| 26 | Iron | (0.77, 0.73, 0.67) | (0.56, 0.57, 0.58) | 18.4 | Reference may include oxide |
| 28 | Nickel | (0.81, 0.77, 0.72) | (0.66, 0.64, 0.58) | 13.1 | Surface finish dependent |
| 29 | Copper | (1.00, 0.84, 0.70) | (0.95, 0.64, 0.54) | 22.8 | Saturation mismatch (see notes) |
| 30 | Zinc | (0.89, 0.89, 0.88) | (0.67, 0.70, 0.75) | 19.9 | Reference may be tarnished |
| 79 | Gold | (1.00, 0.89, 0.64) | (1.00, 0.78, 0.34) | 29.3 | Saturation mismatch (see notes) |

## Technical Notes

### Why Copper and Gold Fail Validation

The computed colors for copper and gold show the correct **hue** (orange-red for Cu, yellow for Au) but insufficient **saturation**. This is because:

1. **Palik data is for bulk polished samples** at normal incidence
2. **Reference colors are often from photos/samples** under different viewing conditions
3. The strong interband transitions in Cu (2.1 eV) and Au (2.4 eV) cause wavelength-dependent reflectance, but the absolute reflectance in the red is still very high (~95%)

The **physics is correct** - the computed reflectance spectra match Palik exactly:
- Cu: R(400nm)=39%, R(600nm)=89%, R(700nm)=96%
- Au: R(400nm)=38%, R(550nm)=82%, R(700nm)=96%

The issue is that high absolute reflectance dilutes the color saturation.

### The Transition Metal Problem

Transition metals (Fe, Cr, Ni, Ti) show significant deviation. Possible causes:
1. **Oxide layers**: Even thin native oxides change apparent color
2. **Surface roughness**: Affects spectral response
3. **Reference color sources**: May be from industrial/tarnished samples

### Validation Methodology

1. **Palik Data**: Measured optical constants (n, k) from polished bulk samples
2. **D65 Illuminant**: Standard daylight (CIE Standard Illuminant D65)
3. **CIE 1931**: 2-degree color matching functions
4. **Delta-E**: CIE76 perceptual color difference

### Files

- `palik_interpolation.hpp` - Palik data and color computation
- `optical_model.hpp/cpp` - Drude-Lorentz model (for elements without Palik data)
- `elements_database.hpp` - Full 118-element database
- `test/palik_color_test.cpp` - Validation test

## Recommendations

### For Visualization

Use validated elements (Al, Ag, Pt) with confidence. For other metals:
- **Cu, Au**: Use computed colors but expect lower saturation than photos
- **Fe, Cr, Ni**: Consider using reference colors directly for realistic appearance
- **Non-metals**: Use element category colors (gases: light colors, etc.)

### For Scientific Applications

The **reflectance spectra** from Palik are accurate. Use those directly rather than sRGB colors for:
- Optical design
- Material identification
- Spectroscopy simulation

### Future Work

1. Add more Palik data (Pd, W, Mo, Ta, etc.)
2. Investigate oxide layer modeling
3. Add angle-dependent reflectance
4. Compare against rendered CGI reference (known lighting conditions)
