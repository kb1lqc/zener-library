<!-- GENERATED - do not edit. Run: python3 -m lib.readme -->

# ERA-3AEB

## Datasheet review

[![Human page-image review: 0/27 human](https://img.shields.io/badge/human%20review-0%2F27%20human-lightgrey)](../../../docs/spec/datasheet-review.md)

Human page-image review: 0/27; cross-model audits: 0; manufacturer-export stamps: 0; legacy/unclassified: 0. Text checks are not verification. `lib.check` validates stamp format, not that review occurred.

## Part

- **alternates**: []
- **manufacturer**: Panasonic
- **description**: 0603 (1608 metric) 0.1 W +/-0.1 % +/-25 ppm/degC thin film chip resistor, ERA-3AEB (47 to 330 k ohm, E24/E96)
- **category**: resistor_thin_film
- **package**: 0603 (1608 metric)
- **datasheet_url**: 
- **datasheet_file**: docs/datasheets/panasonic-fixed-resistors-catalog-2026-05.pdf
- **datasheet_rev**: Catalog 2026.5 (ERA A pages: footer 24-Apr-24, printed pp.19-21)
- **datasheet_date**: 2026-05
- **temp_grade**: -55 to 155 degC
- **kicad_symbol**: ERA-3AEB.kicad_sym
- **kicad_footprint**: ERA-3AEB.kicad_mod
- **step**: ERA-3AEB.step

## Series

- **Value range**: 47 ohm to 330 kohm (`res_range`)
- **E-series**: E24, E96 (408 values in range); E96 only from 100 ohm
- **Tolerance**: 0.1 % (`tol`), used by `Part.series_value`
- **MPN rule**: `calc.mpn(value)`; examples: 47 ohm -> `ERA3AEB470V`, 5.23 kohm -> `ERA3AEB5231V`, 330 kohm -> `ERA3AEB334V`
- **Rated voltage**: min(sqrt(P70 x R), Vlimit), P70 = 100 mW (`p85`), Vlimit = 75 V (`v_limit`)
- **Zener wrapper**: config `value`, optional `v_across` (the module's worst-case voltage across the part; replaces the net ranges in `rated_voltage` when set); checks `value_allowed` and `rated_voltage` (|V(P1) - V(P2)| <= derate x rated voltage). It uses the 70 degC power rating at every ambient, so above 70 degC it is optimistic: use `calc.rated_power` (curve-based) for hot designs
- **Worst-case resistance**: `wca(calc.resistance_worst, r0=<value>, tol=part.param('tol'), tcr=..., ...)` with the plain value as r0; `Part.series_value(value)` already includes the tolerance, so do not pass it as r0 together with tol (that counts the tolerance twice)

Rated voltage at decade values, computed from `p85`, `v_limit` and the formula above:

| Resistance | Rated voltage |
|---|---|
| 100 ohm | 3.162 V |
| 1 kohm | 10 V |
| 10 kohm | 31.62 V |
| 100 kohm | 75 V |

## Pins

| Pin | Name | Type | Function | Cite |
|---|---|---|---|---|
| 1 | 1 | passive | Resistor terminal | DS p.21, Construction (figure; no pin drawing or pin table in this catalog) |
| 2 | 2 | passive | Resistor terminal | DS p.21, Construction (figure; no pin drawing or pin table in this catalog) |

## Parameters: rec_op

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Power rating at 85 degC | P85 |  |  | 0.1 | W | Ambient 85 degC; use on the condition that the case temperature is below the upper category temperature (footnote *1) Note: Printed 0.1 W for this size (DS p.20). Printed with no MIN/TYP/MAX label: stored as max (Defaults table). Derated above 85 degC (derate_knee, derate_zero). | DS p.20, Ratings, Power rating (85 degC) (W), ERA3AEB row |  |
| Limiting element voltage | V limit |  |  | 75 | V | Note: Upper limit on RCWV (footnote *2): RCWV = sqrt(Power rating x Resistance value) or this limit, whichever is less. See rcwv_rule. | DS p.20, Ratings, Limiting element voltage (V), ERA3AEB row |  |
| Maximum overload voltage | V overload |  |  | 150 | V | Note: Upper limit on the overload test voltage (footnote *3): OTV = 2.5 x RCWV or this limit, whichever is less. The Performance table (p.21) prints the overload test as rated voltage x 2.5, 5 s. | DS p.20, Ratings, Maximum overload voltage (V), ERA3AEB row |  |
| Rated continuous working voltage, RCWV | RCWV |  | sqrt(Power rating x Resistance value), or limiting element voltage, whichever less |  | V | Note: Formula, not a number. calc.py rated_voltage implements it. | DS p.20, Ratings, footnote *2 |  |
| Category temperature range | T category | -55 |  | 155 | degC | Note: Read as ambient, the axis of the derating figure (DS p.20). Ratings are for the case temperature below this limit (footnote *1). | DS p.20, Ratings, Category temperature range (degC), all rows of the table (also DS p.19 Features) |  |
| Derating knee: full rated power up to | TA knee |  | 85 |  | degC | Note: Printed in the text, not read off the graph. Used by calc.rated_power. | DS p.20, Power derating curve (text: 'above 85 degC, power rating shall be derated') |  |
| Derating: 0 % rated power at | TA zero |  | 155 |  | degC | Note: Read off the graph (no printed number). Linear between knee and zero (graph shape). Curve-based estimate; reading uncertainty not quantified (open item). | DS p.20, Power derating curve (figure: the derating line reaches 0 % at the 155 degC label) (curve) |  |

## Parameters: electrical

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Resistance tolerance, code B | TOL | -0.1 |  | 0.1 | % | Resistance measured at 20 degC (DS p.21, Performance, Resistance row) Note: Printed +/-0.1 %. | DS p.20, Ratings, Resistance tolerance (%), ERA3AEB row; DS p.19, tolerance code B = +/-0.1 % |  |
| Resistance range (E24, E96) |  | 47 |  | 330000 | ohm | E24, E96 values (E192 on request, not in this format) Note: The printed range for this size's EB grade, as printed (the range differs by size). Printed in k and M: written out in ohm. Duplicate values follow the E24 part number (DS note *5). Values in E96 below 100 ohm have no printed code (calc.mpn raises). | DS p.20, Ratings, Resistance range (ohm), ERA3AEB row '47 to 330 k (E24,E96)' |  |
| Temperature coefficient of resistance, +/-25 ppm/degC | TCR | -25 |  | 25 | ppm/degC | T.C.R. test at +25 degC / +125 degC (DS p.21, Performance) Note: Printed +/-25 x10^-6/K for this size's range (one value for the printed resistance range). Stored as min = -25, max = 25. The DS does not state the reference temperature for the T.C.R.; the Performance test runs from +25 degC. | DS p.20, Ratings, T.C.R. (x10-6/K), ERA3AED, AEC, AEB group, +/-25 (the printed x10^-6/K unit is ppm/degC) |  |
| Resistance change, overload |  | -0.1 |  | 0.1 | % | Rated voltage x 2.5, 5 s Note: Printed +/-0.1 % (R>=47 ohm row). | DS p.21, Performance, Overload, R>=47 ohm: +/-0.1 % |  |
| Resistance change, resistance to soldering heat |  | -0.1 |  | 0.1 | % | 270 degC, 10 s Note: Printed +/-0.1 % (R>=47 ohm row). | DS p.21, Performance, Resistance to soldering heat, R>=47 ohm: +/-0.1 % |  |
| Resistance change, rapid change of temperature |  | -0.1 |  | 0.1 | % | ERA3A, 6A, 8A: -55 degC (30 min) / +155 degC (30 min), 1000 cycles Note: Printed +/-0.1 % (R>=47 ohm row). | DS p.21, Performance, Rapid change of temperature, R>=47 ohm: +/-0.1 % |  |
| Resistance change, high temperature exposure |  | -0.1 |  | 0.1 | % | +155 degC, 1000 h Note: Printed +/-0.1 % (R>=47 ohm row). | DS p.21, Performance, High temperature exposure, R>=47 ohm: +/-0.1 % |  |
| Resistance change, damp heat, steady state |  | -0.1 |  | 0.1 | % | 85 degC, 85 %RH, 1000 h Note: Printed +/-0.1 % (R>=47 ohm row). | DS p.21, Performance, Damp heat, steady state, R>=47 ohm: +/-0.1 % |  |
| Resistance change, load life in humidity |  | -0.1 |  | 0.1 | % | 85 degC, 85 %RH, 10 % rated power, 1.5 h ON / 0.5 h OFF, 1000 h; max test voltage 23.7 V (this size) Note: Printed +/-0.1 % (R>=47 ohm row). | DS p.21, Performance, Load life in humidity, R>=47 ohm: +/-0.1 % |  |
| Resistance change, endurance at 85 degC |  | -0.1 |  | 0.1 | % | 85 degC, rated voltage, 1.5 h ON / 0.5 h OFF, 1000 h Note: Printed +/-0.1 % (R>=47 ohm row). | DS p.21, Performance, Endurance at 85 degC, R>=47 ohm: +/-0.1 % |  |
| AEC-Q200 grade |  |  | Grade 0 |  |  | Note: Informational. DS p.19 Features: AEC-Q200 compliant. | DS p.20, Ratings, AEC-Q200 Grade column, ERA3AE row group |  |

## Parameters: mechanical

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Body length | L | 1.4 | 1.6 | 1.8 | mm | Note: Printed 1.60+/-0.20 mm (DS p.21). | DS p.21, Dimensions (mm) table, row ERA3A, column L |  |
| Body width | W | 0.6 | 0.8 | 1.0 | mm | Note: Printed 0.80+/-0.20 mm (DS p.21). | DS p.21, Dimensions (mm) table, row ERA3A, column W |  |
| Terminal width, a | a | 0.1 | 0.3 | 0.5 | mm | Note: Printed 0.30+/-0.20 mm (DS p.21). | DS p.21, Dimensions (mm) table, row ERA3A, column a |  |
| Terminal width, b | b | 0.1 | 0.3 | 0.5 | mm | Note: Printed 0.30+/-0.20 mm (DS p.21). | DS p.21, Dimensions (mm) table, row ERA3A, column b |  |
| Terminal thickness, T | T | 0.35 | 0.45 | 0.55 | mm | Note: Printed 0.45+/-0.10 mm (DS p.21). | DS p.21, Dimensions (mm) table, row ERA3A, column T |  |
| Mass (reference) |  |  | 2 |  | mg | Reference value, per part Note: 2 g per 1000 pcs = 2 mg per part (per-part value in mg keeps the printed digits). Reference only, not a bound. | DS p.21, Dimensions (mm) table, row ERA3A, Mass (Weight) (Reference) (g/1000 pcs) = 2 |  |
| Land pattern dimension a (DS land pattern table, rectangular type) | a | 0.7 |  | 0.9 | mm | Recommended land pattern (not a tolerance on the body) Note: Printed as a range. The land table is one table for the listed categories; the ERA key line is printed above it. The footprint uses the middle of the range (pads 0.65 x 0.9 mm at +/-0.725 mm). | DS PDF p.1, DMM0000COL17 (Panasonic land-pattern document), Recommended land pattern, 'High precision type (ERA, ERJPC/PB)' key, row 0603 (1608), column a |  |
| Land pattern dimension b (DS land pattern table, rectangular type) | b | 2.0 |  | 2.2 | mm | Recommended land pattern (not a tolerance on the body) Note: Printed as a range. The land table is one table for the listed categories; the ERA key line is printed above it. The footprint uses the middle of the range (pads 0.65 x 0.9 mm at +/-0.725 mm). | DS PDF p.1, DMM0000COL17 (Panasonic land-pattern document), Recommended land pattern, 'High precision type (ERA, ERJPC/PB)' key, row 0603 (1608), column b |  |
| Land pattern dimension c (DS land pattern table, rectangular type) | c | 0.8 |  | 1.0 | mm | Recommended land pattern (not a tolerance on the body) Note: Printed as a range. The land table is one table for the listed categories; the ERA key line is printed above it. The footprint uses the middle of the range (pads 0.65 x 0.9 mm at +/-0.725 mm). | DS PDF p.1, DMM0000COL17 (Panasonic land-pattern document), Recommended land pattern, 'High precision type (ERA, ERJPC/PB)' key, row 0603 (1608), column c |  |

## Limits of this data

Rows by scope: na 27 (25C rows hold only at 25 degC). Curve (graph) rows: 1. Text rows: 2.

## Zener checks

Generated wrapper: `ERA-3AEB.zen` (`python3 -m lib.zen`). abs_max and rec_op rows are errors (abs_max x derate); 25C and partial rows are waivable warnings; a checked net with no voltage is UNVERIFIED.

| Param | Name | Checked against | Not checked / reason |
|---|---|---|---|
| p85 | Power rating at 85 degC | UNCHECKED | series_power: used by the wrapper rated_voltage check (85 degC rating, optimistic above 85 degC ambient) |
| v_limit | Limiting element voltage | UNCHECKED | series_vlimit: used by the wrapper rated_voltage check |
| v_overload | Maximum overload voltage | UNCHECKED | overload test voltage (short-time test condition), not an operating limit; owner: module |
| rcwv_rule | Rated continuous working voltage, RCWV | UNCHECKED | formula rating; owner: module (calc.rated_voltage) |
| category_temp | Category temperature range | board ambient |  |
| derate_knee | Derating knee: full rated power up to | UNCHECKED | derating knee (printed in text, not a limit); used by calc.rated_power |
| derate_zero | Derating: 0 % rated power at | UNCHECKED | curve value; used by calc.rated_power |

## Equations

### `rated_voltage`

```
RCWV = min(sqrt(P x R), limiting element voltage). DS p.20, Ratings, footnote *2 (printed formula).
r: ohm. p85: W (power rating at 85 degC). v_limit: V. Returns: V.
```

Inputs:

- `p85` -> `p85.max` (max 0.1 W)
- `v_limit` -> `v_limit.max` (max 75 V)

### `rated_power`

```
Rated power in W at AMBIENT temperature ta_c (degC).
p85 is the printed 85 degC rating (DS p.20, Ratings). knee_c = 85 degC is printed in the derating text (DS p.20).
zero_c = 155 degC is read off the DS p.20 derating figure (curve = true).
Result: p85 up to knee_c, then a linear fall to 0 W at zero_c. Above knee_c the result is a CURVE-BASED ESTIMATE,
not a datasheet bound. ta_c at or above zero_c gives 0 W.
ta_c, knee_c, zero_c: degC. p85: W. Returns: W.
```

Inputs:

- `p85` -> `p85.max` (max 0.1 W)
- `knee_c` -> `derate_knee.typ` (typ 85 degC)
- `zero_c` -> `derate_zero.typ` (typ 155 degC)

### `resistance_worst`

```
Not a DS equation: combines tolerance (DS p.20) and T.C.R. (DS p.20) per the SPEC temperature recipe.
r0 is the plain nominal value (a float, e.g. from part.values()), NOT part.series_value(), which already carries
the tolerance: passing both would count the tolerance twice. The DS does not state a reference temperature for the
T.C.R.; the caller supplies t_ref_c (25 degC: the T.C.R. test starts at +25 degC, DS p.21).
R = R0 x (1 + tol) x (1 + tcr x (T - Tref)). Call with tol = -0.001 and +0.001 for the two worst corners.
The TCR term is valid only over the span the DS covers, which the DS does not state (open item).
r0: ohm. tol: fraction (0.001 = 0.1 %). tcr: 1/degC (25e-6 = 25 ppm/degC). t_c, t_ref_c: degC. Returns: ohm.
```

Inputs:

- `tol` -> `tol` (min -0.1 max 0.1 %)
- `tcr` -> `tcr_25` (min -25 max 25 ppm/degC)

### `mpn`

```
Not a DS equation: orderable part number from the catalog part-number rule (DS p.19, Explanation of part numbers,
E24 and E96 blocks): ERA3AEB + size/T.C.R./tolerance letters + resistance code + packaging code V.
E24 value (two significant figures): code = two figures + number of zeros, e.g. 47 ohm -> ERA3AEB470V, 1 kohm -> ERA3AEB102V.
A value that is also an E24 value follows the E24 number (DS note *5). Other E96 values use four figures
(three significant + zeros), e.g. 1.05 kohm -> ERA3AEB1051V.
An E96 value below 100 ohm that is not an E24 value has no printed code (the catalog has no decimal-point code):
raises ValueError (open item). Values outside 47 to 330 k ohm raise ValueError.
Returns: str.
```

Inputs:



## Examples

| Call | Computed | Expected | Rel. tol | Result | Cite |
|---|---|---|---|---|---|
| rated_voltage(r=1000, p85=0.1, v_limit=75) | 10 | 10 | 1e-09 | pass | DS p.20, Ratings, footnote *2: RCWV = sqrt(Power rating x R) (arithmetic on the printed formula; 1 kohm is below the limit) |
| rated_voltage(r=330000, p85=0.1, v_limit=75) | 75 | 75 | 1e-09 | pass | DS p.20, Ratings, Limiting element voltage 75 V: the limit applies at the top of the range |
| rated_power(ta_c=85, p85=0.1, knee_c=85, zero_c=155) | 0.1 | 0.1 | 1e-09 | pass | DS p.20, Ratings, Power rating (85 degC) 0.1 W |
| rated_power(ta_c=25, p85=0.1, knee_c=85, zero_c=155) | 0.1 | 0.1 | 1e-09 | pass | DS p.20, Power derating curve: full rated power below 85 degC |
| rated_power(ta_c=155, p85=0.1, knee_c=85, zero_c=155) | 0 | 0 | 1e-09 | pass | DS p.20, Power derating curve: 0 % at 155 degC (curve reading) |
| resistance_worst(r0=1000, tol=0.001, tcr=2.5e-05, t_c=125, t_ref_c=25) | 1003.5 | 1003.5 | 1e-09 | pass | Arithmetic check of the formula: 1 kohm x 1.001 x (1 + 25e-6 x 100); tol +/-0.1 % (DS p.20), TCR +/-25 ppm/degC (DS p.20) |
