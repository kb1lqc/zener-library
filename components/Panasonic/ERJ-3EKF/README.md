<!-- GENERATED - do not edit. Run: python3 -m lib.readme -->

# ERJ-3EKF

## Datasheet review

[![Human page-image review: 0/24 human](https://img.shields.io/badge/human%20review-0%2F24%20human-lightgrey)](../../../docs/spec/datasheet-review.md)

Human page-image review: 0/24; cross-model audits: 15; manufacturer-export stamps: 0; legacy/unclassified: 0. Text checks are not verification. `lib.check` validates stamp format, not that review occurred.

## Part

- **alternates**: []
- **manufacturer**: Panasonic
- **description**: 0603 (1608 metric) 0.1 W +/-1 % thick film chip resistor, ERJ-3EKF series (10 ohm to 1 Mohm, E24/E96)
- **category**: resistor_thick_film
- **package**: 0603 (1608 metric)
- **datasheet_url**: https://industrial.panasonic.com/cdbs/www-data/pdf/RDA0000/AOA0000C304.pdf
- **datasheet_file**: docs/datasheets/AOA0000C304.pdf
- **datasheet_rev**: 29-May-25 (page footers, pp.1-4)
- **datasheet_date**: 2025-05-29
- **temp_grade**: -55 to 155 degC
- **kicad_symbol**: ERJ-3EKF.kicad_sym
- **kicad_footprint**: ERJ-3EKF.kicad_mod
- **step**: ERJ-3EKF.step

## Series

- **Value range**: 10 ohm to 1 Mohm (`res_range`)
- **E-series**: E24, E96 (571 values in range)
- **Tolerance**: 1 % (`tol`), used by `Part.series_value`
- **MPN rule**: `calc.mpn(value)`; examples: 10 ohm -> `ERJ3EKF10R0V`, 3.3 kohm -> `ERJ3EKF3301V`, 1 Mohm -> `ERJ3EKF1004V`
- **Rated voltage**: min(sqrt(P70 x R), Vlimit), P70 = 100 mW (`p70`), Vlimit = 75 V (`v_limit`)
- **Zener wrapper**: config `value`, optional `v_across` (the module's worst-case voltage across the part; replaces the net ranges in `rated_voltage` when set); checks `value_allowed` and `rated_voltage` (|V(P1) - V(P2)| <= derate x rated voltage). It uses the 70 degC power rating at every ambient, so above 70 degC it is optimistic: use `calc.rated_power` (curve-based) for hot designs
- **Worst-case resistance**: `wca(calc.resistance_worst, r0=<value>, tol=part.param('tol'), tcr=..., ...)` with the plain value as r0; `Part.series_value(value)` already includes the tolerance, so do not pass it as r0 together with tol (that counts the tolerance twice)

Rated voltage at decade values, computed from `p70`, `v_limit` and the formula above:

| Resistance | Rated voltage |
|---|---|
| 10 ohm | 1 V |
| 100 ohm | 3.162 V |
| 1 kohm | 10 V |
| 10 kohm | 31.62 V |
| 100 kohm | 75 V |
| 1 Mohm | 75 V |

## Pins

| Pin | Name | Type | Function | Cite |
|---|---|---|---|---|
| 1 | 1 | passive | Resistor terminal | DS PDF p.3, Construction (figure; no pin drawing or pin table in this datasheet) |
| 2 | 2 | passive | Resistor terminal | DS PDF p.3, Construction (figure; no pin drawing or pin table in this datasheet) |

## Parameters: rec_op

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Rated power at 70 degC | P70 |  |  | 0.1 | W | Ambient 70 degC; use with case temperature below the upper category temperature (footnote *1) Note: The DS prints 0.1 W for ERJ3EK (same for 0402 and 0603 in this series). Printed with no MIN/TYP/MAX label: stored as max (Defaults table). Derated above 70 degC (derate_knee, derate_zero). No abs-max table in this DS. | DS PDF p.3, Ratings <+/-1 %>, Power rating (70 degC) (W), ERJ3EK row | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Limiting element voltage | V limit |  |  | 75 | V | Note: Upper limit on RCWV (footnote *2): RCWV = sqrt(Power rating x Resistance value) or this limit, whichever is less. See rcwv_rule. | DS PDF p.3, Ratings <+/-1 %>, Limiting element voltage (V), ERJ3EK row | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Maximum overload voltage | V overload |  |  | 150 | V | Note: Upper limit on the overload test voltage (footnote *3): OTV = specified magnification x RCWV or this limit, whichever is less. | DS PDF p.3, Ratings <+/-1 %>, Maximum overload voltage (V), ERJ3EK row |  |
| Rated continuous working voltage, RCWV | RCWV |  | sqrt(Power rating x Resistance value), or limiting element voltage, whichever less |  | V | Note: Formula, not a number. calc.py rated_voltage implements it. | DS PDF p.3, Ratings <+/-1 %>, footnote *2 |  |
| Category temperature range | T category | -55 |  | 155 | degC | Note: Read as ambient, the axis of the derating figure (DS PDF p.3). Ratings are for the case temperature below this limit (footnote *1). | DS PDF p.3, Ratings <+/-1 %>, Category temperature range (degC), ERJ3EK row (shared with ERJ2RK and ERJ6EN) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Derating knee: full rated power up to | TA knee |  | 70 |  | degC | Note: Printed in the text, not read off the graph. Used by calc.rated_power. | DS PDF p.3, Power derating curve (text: 'above 70 degC, power rating shall be derated') | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Derating: 0 % rated power at | TA zero |  | 155 |  | degC | Note: Read off the graph (no printed number). The 155 degC line is used because this part's category range is -55 to +155 degC; the steeper 125 degC line is labelled ERJXG,1G,1R. Linear between knee and zero (graph shape). Curve-based estimate; reading uncertainty not quantified (open item). | DS PDF p.3, Power derating curve (figure: the 155 degC line reaches 0 %) (curve) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |

## Parameters: electrical

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Resistance tolerance, code F | TOL | -1 |  | 1 | % | Resistance measured at 20 degC (DS PDF p.4, Performance <+/-1 %>, Resistance row) Note: Reference temperature 20 degC from the Performance table; the T.C.R. test runs from +25 degC (DS p.4). | DS PDF p.3, Ratings <+/-1 %>, Resistance tolerance (%), ERJ3EK row; DS PDF p.2, tolerance code F = +/-1 % | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Resistance range |  | 10 |  | 1000000 | ohm | E24, E96 values Note: Printed '10 to 1 M' in the ohm column; 1 M is written out as 1000000 ohm. Values below 100 ohm use the R decimal code (DS p.2), see calc.mpn. | DS PDF p.3, Ratings <+/-1 %>, Resistance range (ohm), ERJ3EK row '10 to 1 M' | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Temperature coefficient of resistance, 10 ohm to 1 Mohm | TCR | -100 |  | 100 | ppm/degC | Resistance 10 ohm to 1 Mohm; T.C.R. test at +25 degC / +155 degC (DS PDF p.4) Note: Printed +/-100 x10-6/K (= ppm/degC): stored as min = -100, max = 100. One TCR for the full +/-1 % range. The DS does not state the TCR reference temperature. Use this key for any value in 10 ohm to 1 Mohm. | DS PDF p.3, Ratings <+/-1 %>, T.C.R. (x10-6/K), ERJ3EK row (+/-100, one value for the whole 10 to 1 M range) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Resistance change, overload |  | -2 |  | 2 | % | Rated voltage x 2.5, 5 s Note: Printed +/-2 %. | DS PDF p.4, Performance, ERJ XGN...2RK...3EK...series +/-1 % (F), Overload |  |
| Resistance change, resistance to soldering heat |  | -1 |  | 1 | % | 270 degC, 10 s Note: Printed +/-1 %. | DS PDF p.4, Performance, ERJ XGN...3EK...series +/-1 % (F), Resistance to soldering heat | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Resistance change, rapid change of temperature |  | -1 |  | 1 | % | -55 degC (30 min) / +155 degC (30 min), 100 cycles Note: Printed +/-1 %. | DS PDF p.4, Performance, ERJ XGN...3EK...series +/-1 % (F), Rapid change of temperature |  |
| Resistance change, high temperature exposure |  | -1 |  | 1 | % | +155 degC, 1000 h Note: Printed +/-1 %. | DS PDF p.4, Performance, ERJ XGN...3EK...series +/-1 % (F), High temperature exposure |  |
| Resistance change, damp heat, steady state |  | -1 |  | 1 | % | 60 degC, 90 % to 95 %RH, 1000 h Note: Printed +/-1 %. | DS PDF p.4, Performance, ERJ XGN...3EK...series +/-1 % (F), Damp heat, Steady state |  |
| Resistance change, load life in humidity |  | -2 |  | 2 | % | 60 degC, 90 % to 95 %RH, rated voltage, 1.5 h ON / 0.5 h OFF cycle, 1000 h Note: Printed +/-2 % (the +/-3 % limit is for ERJXG, 1G only, not this part). | DS PDF p.4, Performance, ERJ XGN...3EK...series +/-1 % (F), Load life in humidity |  |
| Resistance change, endurance at 70 degC |  | -2 |  | 2 | % | 70 degC, rated voltage, 1.5 h ON / 0.5 h OFF cycle, 1000 h Note: Printed +/-2 % (the +/-3 % limit is for ERJXG, 1G only, not this part). | DS PDF p.4, Performance, ERJ XGN...3EK...series +/-1 % (F), Endurance at 70 degC |  |
| AEC-Q200 grade |  |  | Grade 0 |  |  | Note: Informational. DS PDF p.1 Features: AEC-Q200 compliant (except ERJ1R, ERJXG, ERJ1GN). | DS PDF p.3, Ratings <+/-1 %>, AEC-Q200 Grade, ERJ3EK row |  |

## Parameters: mechanical

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Body length | L | 1.45 | 1.6 | 1.75 | mm | Note: Printed 1.60+/-0.15. The ERJ3E row is shared with ERJ3R in the DS table. | DS PDF p.4, Dimensions (mm) table, row ERJ3E (0603), column L | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Body width | W | 0.75 | 0.8 | 0.95 | mm | Note: Printed 0.80 +0.15/-0.05 (asymmetric): min = 0.75, max = 0.95 (arithmetic on the printed tolerance). | DS PDF p.4, Dimensions (mm) table, row ERJ3E (0603), column W | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Terminal width, a | a | 0.1 | 0.3 | 0.5 | mm | Note: Printed 0.30+/-0.20. | DS PDF p.4, Dimensions (mm) table, row ERJ3E (0603), column a | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Terminal width, b | b | 0.15 | 0.3 | 0.45 | mm | Note: Printed 0.30+/-0.15. | DS PDF p.4, Dimensions (mm) table, row ERJ3E (0603), column b | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Terminal thickness, T | T | 0.35 | 0.45 | 0.55 | mm | Note: Printed 0.45+/-0.10. | DS PDF p.4, Dimensions (mm) table, row ERJ3E (0603), column T | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Mass (reference) |  |  | 2 |  | mg | Reference value, per part Note: 2 g per 1000 pcs = 2 mg per part (per-part value in mg keeps the printed digits). Reference only, not a bound. | DS PDF p.4, Dimensions (mm) table, row ERJ3E (0603), Mass (Weight) (Reference) (g/1000 pcs) = 2 | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |

## Limits of this data

Rows by scope: na 24 (25C rows hold only at 25 degC). Curve (graph) rows: 1. Text rows: 2.

## Zener checks

Generated wrapper: `ERJ-3EKF.zen` (`python3 -m lib.zen`). abs_max and rec_op rows are errors (abs_max x derate); 25C and partial rows are waivable warnings; a checked net with no voltage is UNVERIFIED.

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
RCWV = min(sqrt(P x R), limiting element voltage). DS PDF p.3, Ratings <+/-1 %>, footnote *2 (printed formula).
r: ohm. p70: W (rated power at 70 degC). v_limit: V. Returns: V.
```

Inputs:

- `p70` -> `p70.max` (max 0.1 W)
- `v_limit` -> `v_limit.max` (max 75 V)

### `rated_power`

```
Rated power in W at AMBIENT temperature ta_c (degC).
p70 is the printed 70 degC rating (DS PDF p.3, Ratings <+/-1 %>). knee_c = 70 degC is printed in the derating text
(DS PDF p.3). zero_c = 155 degC is read off the DS PDF p.3 derating figure (155 degC line, curve = true).
Result: p70 up to knee_c, then a linear fall to 0 W at zero_c. Above knee_c the result is a CURVE-BASED ESTIMATE,
not a datasheet bound. ta_c at or above zero_c gives 0 W.
ta_c, knee_c, zero_c: degC. p70: W. Returns: W.
```

Inputs:

- `p70` -> `p70.max` (max 0.1 W)
- `knee_c` -> `derate_knee.typ` (typ 70 degC)
- `zero_c` -> `derate_zero.typ` (typ 155 degC)

### `resistance_worst`

```
Not a DS equation: combines tolerance (DS PDF p.3) and TCR (DS PDF p.3) per the SPEC temperature recipe.
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
- `tcr` -> `tcr_10r_1m` (min -100 max 100 ppm/degC)

### `mpn`

```
Not a DS equation: part-number string from the DS decode rule (DS PDF p.2, Explanation of part numbers, +/-1 %
block): ERJ3EK + F (tolerance) + 4-digit code + V (packaging). Code = three significant digits then the number of
zeros: 1002 = 10 kohm. The DS prints the hyphen-less form (ERJ3EK), so the prefix is written without the hyphen.
Below 100 ohm the code is three significant digits with the decimal point written as "R" (DS PDF p.2: "Decimal
point is expressed by 'R'"), e.g. 49.9 ohm -> 49R9, 10 ohm -> 10R0. Series range 10 ohm to 1 Mohm (DS PDF p.3).
Returns: str.
```

Inputs:



## Examples

| Call | Computed | Expected | Rel. tol | Result | Cite |
|---|---|---|---|---|---|
| rated_voltage(r=1e+06, p70=0.1, v_limit=75) | 75 | 75 | 1e-09 | pass | DS PDF p.3, Ratings <+/-1 %>, ERJ3EK limiting element voltage 75 V (sqrt(0.1 x 1 Mohm) = 316 V, so the limit applies) |
| rated_power(ta_c=70, p70=0.1, knee_c=70, zero_c=155) | 0.1 | 0.1 | 1e-09 | pass | DS PDF p.3, Ratings <+/-1 %>, Power rating (70 degC) 0.1 W |
| rated_power(ta_c=25, p70=0.1, knee_c=70, zero_c=155) | 0.1 | 0.1 | 1e-09 | pass | DS PDF p.3, Power derating curve: full rated power below 70 degC |
| rated_power(ta_c=155, p70=0.1, knee_c=70, zero_c=155) | 0 | 0 | 1e-09 | pass | DS PDF p.3, Power derating curve: 0 % at 155 degC (curve reading) |
