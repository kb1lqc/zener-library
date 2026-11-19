<!-- GENERATED - do not edit. Run: python3 -m lib.readme -->

# ERJ-6ENF

## Datasheet review

[![Human page-image review: 0/27 human](https://img.shields.io/badge/human%20review-0%2F27%20human-lightgrey)](../../../docs/spec/datasheet-review.md)

Human page-image review: 0/27; cross-model audits: 0; manufacturer-export stamps: 0; legacy/unclassified: 0. Text checks are not verification. `lib.check` validates stamp format, not that review occurred.

## Part

- **alternates**: []
- **manufacturer**: Panasonic
- **description**: 0805 (2012 metric) 0.125 W +/-1 % thick film chip resistor, ERJ-6ENF series (10 ohm to 2.2 Mohm, E24/E96)
- **category**: resistor_thick_film
- **package**: 0805 (2012 metric)
- **datasheet_url**: 
- **datasheet_file**: docs/datasheets/panasonic-fixed-resistors-catalog-2026-05.pdf
- **datasheet_rev**: Products catalog 2026.5; page footers dated 29-May-25 (printed pp.8-11)
- **datasheet_date**: 2025-05-29
- **temp_grade**: -55 to 155 degC
- **kicad_symbol**: ERJ-6ENF.kicad_sym
- **kicad_footprint**: ERJ-6ENF.kicad_mod
- **step**: ERJ-6ENF.step

## Series

- **Value range**: 10 ohm to 2.2 Mohm (`res_range`)
- **E-series**: E24, E96 (607 values in range)
- **Tolerance**: 1 % (`tol`), used by `Part.series_value`
- **MPN rule**: `calc.mpn(value)`; examples: 10 ohm -> `ERJ6ENF10R0V`, 4.64 kohm -> `ERJ6ENF4641V`, 2.2 Mohm -> `ERJ6ENF2204V`
- **Rated voltage**: min(sqrt(P70 x R), Vlimit), P70 = 125 mW (`p70`), Vlimit = 150 V (`v_limit`)
- **Zener wrapper**: config `value`, optional `v_across` (the module's worst-case voltage across the part; replaces the net ranges in `rated_voltage` when set); checks `value_allowed` and `rated_voltage` (|V(P1) - V(P2)| <= derate x rated voltage). It uses the 70 degC power rating at every ambient, so above 70 degC it is optimistic: use `calc.rated_power` (curve-based) for hot designs
- **Worst-case resistance**: `wca(calc.resistance_worst, r0=<value>, tol=part.param('tol'), tcr=..., ...)` with the plain value as r0; `Part.series_value(value)` already includes the tolerance, so do not pass it as r0 together with tol (that counts the tolerance twice)

Rated voltage at decade values, computed from `p70`, `v_limit` and the formula above:

| Resistance | Rated voltage |
|---|---|
| 10 ohm | 1.118 V |
| 100 ohm | 3.536 V |
| 1 kohm | 11.18 V |
| 10 kohm | 35.36 V |
| 100 kohm | 111.8 V |
| 1 Mohm | 150 V |

## Pins

| Pin | Name | Type | Function | Cite |
|---|---|---|---|---|
| 1 | 1 | passive | Resistor terminal | DS p.10, Construction (figure; no pin drawing or pin table in this datasheet) |
| 2 | 2 | passive | Resistor terminal | DS p.10, Construction (figure; no pin drawing or pin table in this datasheet) |

## Parameters: rec_op

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Rated power at 70 degC | P70 |  |  | 0.125 | W | Ambient 70 degC; use with case temperature below the upper category temperature (footnote *1) Note: The catalog prints 0.125 W for ERJ6EN. Printed with no MIN/TYP/MAX label: stored as max (Defaults table). Derated above 70 degC (derate_knee, derate_zero). No abs-max table in this catalog. | DS p.10, Ratings <+/-1 %>, Power rating (70 degC) (W), ERJ6EN row |  |
| Limiting element voltage | V limit |  |  | 150 | V | Note: Upper limit on RCWV (footnote *2): RCWV = sqrt(Power rating x Resistance value) or this limit, whichever is less. See rcwv_rule. | DS p.10, Ratings <+/-1 %>, Limiting element voltage (V), ERJ6EN row |  |
| Maximum overload voltage | V overload |  |  | 200 | V | Note: Upper limit on the overload test voltage (footnote *3): OTV = specified magnification x RCWV or this limit, whichever is less. | DS p.10, Ratings <+/-1 %>, Maximum overload voltage (V), ERJ6EN row |  |
| Rated continuous working voltage, RCWV | RCWV |  | sqrt(Power rating x Resistance value), or limiting element voltage, whichever less |  | V | Note: Formula, not a number. calc.py rated_voltage implements it. | DS p.10, Ratings <+/-1 %>, footnote *2 |  |
| Category temperature range | T category | -55 |  | 155 | degC | Note: Read as ambient, the axis of the derating figure (DS p.10). Ratings are for the case temperature below this limit (footnote *1). | DS p.10, Ratings <+/-1 %>, Category temperature range (degC), ERJ6EN row (merged cell with ERJ2RK, ERJ3EK) |  |
| Derating knee: full rated power up to | TA knee |  | 70 |  | degC | Note: Printed in the text, not read off the graph. Used by calc.rated_power. | DS p.10, Power derating curve (text: 'above 70 degC, power rating shall be derated') |  |
| Derating: 0 % rated power at | TA zero |  | 155 |  | degC | Note: Read off the graph (no printed number). The 155 degC line is used because this part's category range is -55 to +155 degC; the steeper 125 degC line is labelled ERJXG,1G,1R. Linear between knee and zero (graph shape). Curve-based estimate; reading uncertainty not quantified (open item). | DS p.10, Power derating curve (figure: the 155 degC line reaches 0 %) (curve) |  |

## Parameters: electrical

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Resistance tolerance, code F | TOL | -1 |  | 1 | % | Resistance measured at 20 degC (catalog p.11, Performance <+/-1 %> (F), Resistance row) Note: Reference temperature 20 degC from the Performance table; the T.C.R. test runs from +25 degC (DS p.11). | DS p.10, Ratings <+/-1 %>, Resistance tolerance (%), ERJ6EN row; DS p.9, tolerance code F = +/-1 % |  |
| Resistance range |  | 10 |  | 2200000 | ohm | E24, E96 values Note: Printed '10 to 2.2 M' in the ohm column; 2.2 M is written out as 2200000 ohm. Values below 100 ohm use the R decimal code (DS p.9), see calc.mpn. | DS p.10, Ratings <+/-1 %>, Resistance range (ohm), ERJ6EN row '10 to 2.2 M' |  |
| Temperature coefficient of resistance, 10 ohm to 2.2 Mohm | TCR | -100 |  | 100 | ppm/degC | Resistance 10 ohm to 2.2 Mohm; T.C.R. test at +25 degC / +155 degC (DS p.11, Performance <+/-1 %> (F), T. C. R. row) Note: Printed +/-100 x10-6/K (= ppm/degC): stored as min = -100, max = 100. One TCR for the full +/-1 % range (the catalog's single +/-100 cell covers ERJ2RK, ERJ3EK and ERJ6EN). The catalog does not state the TCR reference temperature. Use this key for any value in 10 ohm to 2.2 Mohm. | DS p.10, Ratings <+/-1 %>, T.C.R. (x10-6/K), ERJ6EN row (+/-100, one value for the whole +/-1 % range) |  |
| Resistance change, overload |  | -2 |  | 2 | % | Rated voltage x 2.5, 5 s Note: Printed +/-2 %. | DS p.11, Performance, ERJ XGN, 1GN, 1GJ, 2RC, 2RK, 3EK, 6EN, 8EN, 14N, 12N, 12S, 1TN series: +/-1 % (F), Overload |  |
| Resistance change, resistance to soldering heat |  | -1 |  | 1 | % | 270 degC, 10 s Note: Printed +/-1 %. | DS p.11, Performance, +/-1 % (F) block, Resistance to soldering heat |  |
| Resistance change, rapid change of temperature |  | -1 |  | 1 | % | -55 degC (30 min) / +155 degC (30 min), 100 cycles Note: Printed +/-1 %. | DS p.11, Performance, +/-1 % (F) block, Rapid change of temperature |  |
| Resistance change, high temperature exposure |  | -1 |  | 1 | % | +155 degC, 1000 h Note: Printed +/-1 %. | DS p.11, Performance, +/-1 % (F) block, High temperature exposure |  |
| Resistance change, damp heat, steady state |  | -1 |  | 1 | % | 60 degC, 90 % to 95 %RH, 1000 h Note: Printed +/-1 %. | DS p.11, Performance, +/-1 % (F) block, Damp heat, Steady state |  |
| Resistance change, load life in humidity |  | -2 |  | 2 | % | 60 degC, 90 % to 95 %RH, rated voltage, 1.5 h ON / 0.5 h OFF cycle, 1000 h Note: Printed +/-2 % (the +/-3 % limit is for ERJXG, 1G only, not this part). | DS p.11, Performance, +/-1 % (F) block, Load life in humidity |  |
| Resistance change, endurance at 70 degC |  | -2 |  | 2 | % | 70 degC, rated voltage, 1.5 h ON / 0.5 h OFF cycle, 1000 h Note: Printed +/-2 % (the +/-3 % limit is for ERJXG, 1G only, not this part). | DS p.11, Performance, +/-1 % (F) block, Endurance at 70 degC |  |
| AEC-Q200 grade |  |  | Grade 0 |  |  | Note: Informational. Grade column of the Ratings table only; the AEC-Q200 claim is not restated elsewhere in the pages read. | DS p.10, Ratings <+/-1 %>, AEC-Q200 Grade, ERJ6EN row (merged cell with ERJ2RK, ERJ3EK) |  |

## Parameters: mechanical

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Body length | L | 1.8 | 2.0 | 2.2 | mm | Note: Printed 2.00+/-0.20. The ERJ6E row is shared with ERJ6R in the DS table. | DS p.11, Dimensions (mm) table, row ERJ6E (0805), column L |  |
| Body width | W | 1.15 | 1.25 | 1.35 | mm | Note: Printed 1.25+/-0.10. | DS p.11, Dimensions (mm) table, row ERJ6E (0805), column W |  |
| Terminal width, a | a | 0.2 | 0.4 | 0.6 | mm | Note: Printed 0.40+/-0.20. | DS p.11, Dimensions (mm) table, row ERJ6E (0805), column a |  |
| Terminal width, b | b | 0.2 | 0.4 | 0.6 | mm | Note: Printed 0.40+/-0.20. | DS p.11, Dimensions (mm) table, row ERJ6E (0805), column b |  |
| Terminal thickness, T | T | 0.5 | 0.6 | 0.7 | mm | Note: Printed 0.60+/-0.10. | DS p.11, Dimensions (mm) table, row ERJ6E (0805), column T |  |
| Mass (reference) |  |  | 4 |  | mg | Reference value, per part Note: 4 g per 1000 pcs = 4 mg per part (per-part value in mg keeps the printed digits). Reference only, not a bound. | DS p.11, Dimensions (mm) table, row ERJ6E (0805), Mass (Weight) (Reference) (g/1000 pcs) = 4 |  |
| Land pattern dimension a (DS land pattern table, rectangular type) | a | 1.0 |  | 1.4 | mm | Recommended land pattern (not a tolerance on the body) Note: Printed as a range. Inferred meaning: inner gap between lands (inferred; letter label only). The footprint uses the middle of the range. | DS PDF p.1, DMM0000COL17 (Panasonic land-pattern document), Recommended land pattern, 'General purpose type (ERJ)' key, row 0805 (2012), column a |  |
| Land pattern dimension b (DS land pattern table, rectangular type) | b | 3.2 |  | 3.8 | mm | Recommended land pattern (not a tolerance on the body) Note: Printed as a range. Inferred meaning: outer span of the two lands (inferred). The footprint uses the middle of the range. | DS PDF p.1, DMM0000COL17 (Panasonic land-pattern document), Recommended land pattern, 'General purpose type (ERJ)' key, row 0805 (2012), column b |  |
| Land pattern dimension c (DS land pattern table, rectangular type) | c | 0.9 |  | 1.4 | mm | Recommended land pattern (not a tolerance on the body) Note: Printed as a range. Inferred meaning: land width (inferred). The footprint uses the middle of the range. | DS PDF p.1, DMM0000COL17 (Panasonic land-pattern document), Recommended land pattern, 'General purpose type (ERJ)' key, row 0805 (2012), column c |  |

## Limits of this data

Rows by scope: na 27 (25C rows hold only at 25 degC). Curve (graph) rows: 1. Text rows: 2.

## Zener checks

Generated wrapper: `ERJ-6ENF.zen` (`python3 -m lib.zen`). abs_max and rec_op rows are errors (abs_max x derate); 25C and partial rows are waivable warnings; a checked net with no voltage is UNVERIFIED.

| Param | Name | Checked against | Not checked / reason |
|---|---|---|---|
| p70 | Rated power at 70 degC | UNCHECKED | series_power: used by the wrapper rated_voltage check (70 degC rating, optimistic above 70 degC ambient) |
| v_limit | Limiting element voltage | UNCHECKED | series_vlimit: used by the wrapper rated_voltage check |
| v_overload | Maximum overload voltage | UNCHECKED | overload test voltage (short-time test condition), not an operating limit; owner: module |
| rcwv_rule | Rated continuous working voltage, RCWV | UNCHECKED | formula rating; owner: module (calc.rated_voltage) |
| category_temp | Category temperature range | board ambient |  |
| derate_knee | Derating knee: full rated power up to | UNCHECKED | derating knee (printed in text, not a limit); used by calc.rated_power |
| derate_zero | Derating: 0 % rated power at | UNCHECKED | curve value; used by calc.rated_power |

## Equations

### `rated_voltage`

```
RCWV = min(sqrt(P x R), limiting element voltage). DS p.10, Ratings <+/-1 %>, footnote *2 (printed formula).
r: ohm. p70: W (rated power at 70 degC). v_limit: V. Returns: V.
```

Inputs:

- `p70` -> `p70.max` (max 0.125 W)
- `v_limit` -> `v_limit.max` (max 150 V)

### `rated_power`

```
Rated power in W at AMBIENT temperature ta_c (degC).
p70 is the printed 70 degC rating (DS p.10, Ratings <+/-1 %>). knee_c = 70 degC is printed in the derating text
(DS p.10). zero_c = 155 degC is read off the DS p.10 derating figure (155 degC line, curve = true).
Result: p70 up to knee_c, then a linear fall to 0 W at zero_c. Above knee_c the result is a CURVE-BASED ESTIMATE,
not a datasheet bound. ta_c at or above zero_c gives 0 W.
ta_c, knee_c, zero_c: degC. p70: W. Returns: W.
```

Inputs:

- `p70` -> `p70.max` (max 0.125 W)
- `knee_c` -> `derate_knee.typ` (typ 70 degC)
- `zero_c` -> `derate_zero.typ` (typ 155 degC)

### `resistance_worst`

```
Not a DS equation: combines tolerance (DS p.10) and TCR (DS p.10) per the SPEC temperature recipe.
r0 is the plain nominal value (a float, e.g. from part.values()), NOT part.series_value(), which already carries
the tolerance: passing both would count the tolerance twice. The DS
states no reference temperature for either; the caller supplies t_ref_c (25 degC is the usual assumption; the DS
T.C.R. test runs from +25 degC).
R = R0 x (1 + tol) x (1 + tcr x (T - Tref)). Call with tol = -0.01 and +0.01 for the two worst corners.
The TCR term is valid only over the span the DS covers, which the DS does not state (open item).
r0: ohm. tol: fraction (0.01 = 1 %). tcr: 1/degC (100e-6 = 100 ppm/degC). t_c, t_ref_c: degC. Returns: ohm.
```

Inputs:

- `tol` -> `tol` (min -1 max 1 %)
- `tcr` -> `tcr_10r_2m2` (min -100 max 100 ppm/degC)

### `mpn`

```
Not a DS equation: part-number string from the DS decode rule (DS p.9, Explanation of part numbers, +/-1 %
block): ERJ6EN + F (tolerance) + 4-digit code + V (packaging). Code = three significant digits then the number of
zeros: 1002 = 10 kohm. The DS prints the hyphen-less form (ERJ6EN), so the prefix is written without the hyphen.
Below 100 ohm the code is three significant digits with the decimal point written as "R" (DS p.9: "Decimal
point is expressed by 'R'"), e.g. 49.9 ohm -> 49R9, 10 ohm -> 10R0. Series range 10 ohm to 2.2 Mohm (DS p.10).
Returns: str.
```

Inputs:



## Examples

| Call | Computed | Expected | Rel. tol | Result | Cite |
|---|---|---|---|---|---|
| rated_voltage(r=2.2e+06, p70=0.125, v_limit=150) | 150 | 150 | 1e-09 | pass | DS p.10, Ratings <+/-1 %>, ERJ6EN limiting element voltage 150 V (sqrt(0.125 x 2.2 Mohm) = 524 V, so the limit applies) |
| rated_power(ta_c=70, p70=0.125, knee_c=70, zero_c=155) | 0.125 | 0.125 | 1e-09 | pass | DS p.10, Ratings <+/-1 %>, Power rating (70 degC) 0.125 W |
| rated_power(ta_c=25, p70=0.125, knee_c=70, zero_c=155) | 0.125 | 0.125 | 1e-09 | pass | DS p.10, Power derating curve: full rated power below 70 degC |
| rated_power(ta_c=155, p70=0.125, knee_c=70, zero_c=155) | 0 | 0 | 1e-09 | pass | DS p.10, Power derating curve: 0 % at 155 degC (curve reading) |
