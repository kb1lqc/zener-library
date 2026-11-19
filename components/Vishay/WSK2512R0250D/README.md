<!-- GENERATED - do not edit. Run: python3 -m lib.readme -->

# WSK2512R0250D

## Datasheet review

[![Human page-image review: 0/33 human](https://img.shields.io/badge/human%20review-0%2F33%20human-lightgrey)](../../../docs/spec/datasheet-review.md)

Human page-image review: 0/33; cross-model audits: 0; manufacturer-export stamps: 0; legacy/unclassified: 0. Text checks are not verification. `lib.check` validates stamp format, not that review occurred.

## Part

- **mpn**: WSK2512R0250DEA
- **alternates**: ['WSK2512R0250DEK', 'WSK2512R0250DEB']
- **manufacturer**: Vishay Dale
- **description**: 0.025 ohm +/-0.5 % 1 W 4-terminal (Kelvin) Power Metal Strip current-sense resistor, 2512
- **category**: current_sense_resistor
- **package**: 2512 (4-terminal Kelvin, Power Metal Strip)
- **datasheet_url**: https://www.vishay.com/doc?30108
- **datasheet_file**: docs/datasheets/wsk2512.pdf
- **datasheet_rev**: 11-Dec-2023 (Document 30108)
- **datasheet_date**: 2023-12-11
- **temp_grade**: -65 to +170 degC
- **kicad_symbol**: WSK2512R0250D.kicad_sym
- **kicad_footprint**: WSK2512R0250D.kicad_mod
- **step**: none

## Pins

| Pin | Name | Type | Function | Cite |
|---|---|---|---|---|
| 1 | I2 | passive | Current connection (I2) | DS p.3, ELECTRICAL CONNECTION, I2 (figure, left terminal outer end) and Notes ('I1 and I2: current connection') |
| 2 | E2 | passive | Voltage sense connection (E2), on the I2 terminal | DS p.3, ELECTRICAL CONNECTION, E2 (figure, left terminal notch) and Notes ('E1 and E2: voltage sense connections') |
| 3 | E1 | passive | Voltage sense connection (E1), on the I1 terminal | DS p.3, ELECTRICAL CONNECTION, E1 (figure, right terminal notch) and Notes ('E1 and E2: voltage sense connections') |
| 4 | I1 | passive | Current connection (I1) | DS p.3, ELECTRICAL CONNECTION, I1 (figure, right terminal outer end) and Notes ('I1 and I2: current connection') |

## Parameters: rec_op

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Power rating at 70 degC ambient | P70 degC |  |  | 1.0 | W | Ambient 70 degC; 0.025 ohm lies in the 0.01 to 0.2 ohm and 0.001 to 0.2 ohm ranges Note: Rating: a maximum, stored as max. No abs-max table. Rated against AMBIENT (DS p.3 DERATING axis); self-heating is not given. | DS p.1, Standard Electrical Specifications, POWER RATING P70 degC, W, 1.0 |  |
| Maximum working voltage |  |  | (P x R)^1/2 |  | V | Note: Formula, not a number. calc.py max_working_voltage implements it. | DS p.2, Technical Specifications, Maximum working voltage, (P x R)^1/2 |  |
| Operating temperature range |  | -65 |  | 170 | degC | Note: The DS does not say whether this is ambient or element temperature; read as ambient (DS p.3 DERATING axis). Only temperature rating in the DS (no storage or abs-max row). | DS p.2, Technical Specifications, Operating temperature range, -65 to +170 |  |
| Derating knee: 100 % rated power up to | TA knee |  | 70 |  | degC | Note: Read off the graph. Not a worst-case bound (curve). | DS p.3, Figure: DERATING graph (unnumbered; rated power vs ambient, 100 % line ends at 70 degC); coincides with DS p.1 P70 degC (curve) |  |
| Derating: 0 % rated power at | TA zero |  | 170 |  | degC | Note: Read off the graph (no printed number). Coincides with the top of the operating range (DS p.2). Linear between knee and zero (graph shape). | DS p.3, Figure: DERATING graph (unnumbered; rated power vs ambient, line reaches 0 % at 170 degC) (curve) |  |

## Parameters: electrical

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Resistance, nominal | R |  | 0.025 |  | ohm | Note: Value decoded from the part number by the printed decimal rule (R0100 = 0.01 ohm is the printed example); no table row prints 0.025 ohm. Stored as typ only. | DS p.1, Global Part Number Information, resistance code R0250 (R = decimal rule, example R0100 = 0.01 ohm) |  |
| Resistance tolerance, code D | TOL | -0.5 |  | 0.5 | % | Note: The DS does not state the reference temperature for the tolerance. | DS p.1, Standard Electrical Specifications, TOL. +/-0.5 % column; DS p.1, Global Part Number Information, tolerance code D = +/-0.5 % |  |
| Resistance value range, +/-0.5 % tolerance |  | 0.001 |  | 0.2 | ohm | Note: Confirms 0.025 ohm is in range for code D. The +/-0.1 % range (0.01 to 0.2 ohm) also covers 0.025 ohm; the +/-1.0 % range is 0.0005 to 0.2 ohm. | DS p.1, Standard Electrical Specifications, Resistance value range TOL. +/-0.5 % column, 0.001 to 0.2 row |  |
| Temperature coefficient of resistance | TCR | -35 |  | 35 | ppm/degC | Resistance range 0.005 ohm to 0.2 ohm (covers 0.025 ohm) Note: DS p.1 Features says 'low TCR (< 20 ppm/degC)'. Feature text is not a specification; the table value +/-35 is used (open item). The DS states neither the reference temperature nor the temperature span over which the TCR holds. | DS p.2, Technical Specifications, Temperature coefficient (RESISTOR CHARACTERISTICS), +/-35 for 0.005 ohm to 0.2 ohm |  |
| Performance test limit, additive term (all PERFORMANCE rows) |  | -0.0005 |  | 0.0005 | ohm | Added to the percent term of every PERFORMANCE row: total limit ±(X % of R + 0.0005 ohm) Note: Printed '± X % + 0.0005 Ω' with no brackets. Stored symmetric, ±(X % of R + 0.0005 ohm): the conservative worst-case reading (a one-sided +0.0005 would understate the low side). Open item: confirm the reading with Vishay. | DS p.3, PERFORMANCE, TEST LIMITS column, '+ 0.0005 ohm' (all rows) |  |
| Resistance change, thermal shock |  | -0.5 |  | 0.5 | % | -55 degC to +150 degC, 1000 cycles, 15 min at each extreme Note: Printed ± 0.5 %. Total limit ±(0.5 % of R + 0.0005 ohm); add perf_offset_ohm. | DS p.3, PERFORMANCE, Thermal shock, TEST LIMITS |  |
| Resistance change, short time overload |  | -0.5 |  | 0.5 | % | Overload level not printed; DS refers to external link www.vishay.com/en/resistors/power-metal-strip-calculator/ Note: Printed ± 0.5 %. Total limit ±(0.5 % of R + 0.0005 ohm); add perf_offset_ohm. Do not apply to any specific overload: the DS gives no level. Pulse capability has no numbers in the DS (online calculator only). | DS p.3, PERFORMANCE, Short time overload, TEST LIMITS |  |
| Resistance change, low temperature operation |  | -0.5 |  | 0.5 | % | -65 degC for 24 h Note: Printed ± 0.5 %. Total limit ±(0.5 % of R + 0.0005 ohm); add perf_offset_ohm. | DS p.3, PERFORMANCE, Low temperature operation, TEST LIMITS |  |
| Resistance change, high temperature exposure |  | -1.0 |  | 1.0 | % | 1000 h at +170 degC Note: Printed ± 1.0 % (not 0.5 %). Total limit ±(1.0 % of R + 0.0005 ohm); add perf_offset_ohm. | DS p.3, PERFORMANCE, High temperature exposure, TEST LIMITS |  |
| Resistance change, bias humidity |  | -0.5 |  | 0.5 | % | +85 degC, 85 % RH, 10 % bias, 1000 h Note: Printed ± 0.5 %. Total limit ±(0.5 % of R + 0.0005 ohm); add perf_offset_ohm. | DS p.3, PERFORMANCE, Bias humidity, TEST LIMITS |  |
| Resistance change, mechanical shock |  | -0.5 |  | 0.5 | % | 100 g for 6 ms, 5 pulses Note: Printed ± 0.5 %. Total limit ±(0.5 % of R + 0.0005 ohm); add perf_offset_ohm. | DS p.3, PERFORMANCE, Mechanical shock, TEST LIMITS |  |
| Resistance change, vibration |  | -0.5 |  | 0.5 | % | Frequency varied 10 Hz to 2000 Hz in 1 min, 3 directions, 12 h Note: Printed ± 0.5 %. Total limit ±(0.5 % of R + 0.0005 ohm); add perf_offset_ohm. | DS p.3, PERFORMANCE, Vibration, TEST LIMITS |  |
| Resistance change, load life |  | -1.0 |  | 1.0 | % | 1000 h at rated power, +70 degC, 1.5 h ON, 0.5 h OFF Note: Printed ± 1.0 % (not 0.5 %). Total limit ±(1.0 % of R + 0.0005 ohm); add perf_offset_ohm. | DS p.3, PERFORMANCE, Load life, TEST LIMITS |  |
| Resistance change, resistance to solder heat |  | -0.5 |  | 0.5 | % | +260 degC solder, 10 s to 12 s dwell, 25 mm/s emergence Note: Printed ± 0.5 %. Total limit ±(0.5 % of R + 0.0005 ohm); add perf_offset_ohm. | DS p.3, PERFORMANCE, Resistance to solder heat, TEST LIMITS |  |
| Resistance change, moisture resistance |  | -0.5 |  | 0.5 | % | MIL-STD-202, method 106, 0 % power, 7a and 7b not required Note: Printed ± 0.5 %. Total limit ±(0.5 % of R + 0.0005 ohm); add perf_offset_ohm. | DS p.3, PERFORMANCE, Moisture resistance, TEST LIMITS |  |

## Parameters: mechanical

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Body length | L | 6.096 | 6.35 | 6.604 | mm | Note: Printed 6.35 +/-0.254 mm (0.250 in). Same for all resistance rows. min/max = nominal ±0.254 mm (arithmetic on the printed tolerance). | DS p.2, DIMENSIONS table (mm in brackets), row 0.005 to 0.2 ohm, column L |  |
| Body width | W | 2.926 | 3.18 | 3.434 | mm | Note: Printed 3.18 +/-0.254 mm (0.125 in). Same for all resistance rows. min/max = nominal ±0.254 mm (arithmetic on the printed tolerance). | DS p.2, DIMENSIONS table (mm in brackets), row 0.005 to 0.2 ohm, column W |  |
| Body height | H | 0.381 | 0.635 | 0.889 | mm | Note: Printed 0.635 +/-0.254 mm (0.025 in). Same for all resistance rows. min/max = nominal ±0.254 mm (arithmetic on the printed tolerance). | DS p.2, DIMENSIONS table (mm in brackets), row 0.005 to 0.2 ohm, column H |  |
| Terminal length (T) | T | 0.936 | 1.19 | 1.444 | mm | Note: Printed 1.19 +/-0.254 mm (0.047 in) for 0.005 to 0.2 ohm; other rows differ. min/max = nominal ±0.254 mm (arithmetic on the printed tolerance). | DS p.2, DIMENSIONS table (mm in brackets), row 0.005 to 0.2 ohm, column T |  |
| Terminal width, A | A | 0.508 | 0.762 | 1.016 | mm | Note: Printed 0.762 +/-0.254 mm (0.030 in). Same for all resistance rows. min/max = nominal ±0.254 mm (arithmetic on the printed tolerance). | DS p.2, DIMENSIONS table (mm in brackets), row 0.005 to 0.2 ohm, column A |  |
| Terminal width, B | B | 0.254 | 0.508 | 0.762 | mm | Note: Printed 0.508 +/-0.254 mm (0.020 in). Same for all resistance rows. min/max = nominal ±0.254 mm (arithmetic on the printed tolerance). | DS p.2, DIMENSIONS table (mm in brackets), row 0.005 to 0.2 ohm, column B |  |
| Land pattern dimension a (DS p.2 diagram) | a |  | 2.29 |  | mm | Note: Printed 0.090 in (2.29 mm). INFERRED feature, not printed: the arrow a runs from the sense-pad end to the far current-pad edge, so it looks like an overall X dimension, not a single pad length. Feature unverified. | DS p.2, SOLDER PAD DIMENSIONS (mm in brackets), row 0.005 to 0.2 ohm, column a |  |
| Land pattern dimension b (DS p.2 diagram) | b |  | 3.3 |  | mm | Note: Printed 0.130 in (3.30 mm). INFERRED feature, not printed: overall Y span of the pattern (3.30 = footprint -1.651..+1.651 mm). Arrow b runs from the top of the upper current pad to the bottom of the sense pad. | DS p.2, SOLDER PAD DIMENSIONS (mm in brackets), row 0.005 to 0.2 ohm, column b |  |
| Land pattern dimension c (DS p.2 diagram) | c |  | 0.76 |  | mm | Note: Printed 0.030 in (0.76 mm). INFERRED feature, not printed: width of the sense pad (arrow c spans its short edge). | DS p.2, SOLDER PAD DIMENSIONS (mm in brackets), row 0.005 to 0.2 ohm, column c |  |
| Land pattern dimension d (DS p.2 diagram) | d |  | 0.51 |  | mm | Note: Printed 0.020 in (0.51 mm). INFERRED feature, not printed: gap between the current pad and the sense pad (arrow d). | DS p.2, SOLDER PAD DIMENSIONS (mm in brackets), row 0.005 to 0.2 ohm, column d |  |
| Land pattern dimension e (DS p.2 diagram) | e |  | 1.7 |  | mm | Note: Printed 0.067 in (1.70 mm). INFERRED feature, not printed: length of the sense pad (arrow e spans its long edge). | DS p.2, SOLDER PAD DIMENSIONS (mm in brackets), row 0.005 to 0.2 ohm, column e |  |
| Land pattern dimension l (DS p.2 diagram) | l |  | 3.68 |  | mm | Note: Printed 0.145 in (3.68 mm). INFERRED feature, not printed: a gap in the X direction (arrow l runs from the a-arrow end to the far pad edge). Not confirmed as the gap between current pads. | DS p.2, SOLDER PAD DIMENSIONS (mm in brackets), row 0.005 to 0.2 ohm, column l |  |
| Weight |  |  | 63.6 |  | mg | typical; DS prints 63.6 g per 1000 pieces Note: Per part: 63.6 g per 1000 pieces = 63.6 mg per part. Typical only. | DS p.1, Standard Electrical Specifications, WEIGHT (typical) g/1000 pieces, row WSK2512 |  |

## Limits of this data

Rows by scope: na 33 (25C rows hold only at 25 degC). Curve (graph) rows: 2. Text rows: 1.

## Zener checks

Generated wrapper: `WSK2512R0250D.zen` (`python3 -m lib.zen`). abs_max and rec_op rows are errors (abs_max x derate); 25C and partial rows are waivable warnings; a checked net with no voltage is UNVERIFIED.

| Param | Name | Checked against | Not checked / reason |
|---|---|---|---|
| p70 | Power rating at 70 degC ambient | UNCHECKED | dissipation depends on the load current; owner: module (calc.dissipation vs calc.rated_power) |
| max_working_voltage | Maximum working voltage | UNCHECKED | formula rating; owner: module (calc.max_working_voltage) |
| t_oper | Operating temperature range | board ambient |  |
| derate_knee | Derating knee: 100 % rated power up to | UNCHECKED | curve value; used by calc.rated_power |
| derate_zero | Derating: 0 % rated power at | UNCHECKED | curve value; used by calc.rated_power |

## Equations

### `resistance_worst`

```
Not a DS equation: combines tolerance (DS p.1), TCR (DS p.2) and, optionally, the aging test limit (DS p.3)
per the SPEC temperature recipe; DS states no reference temperature, caller supplies t_ref_c (25 degC is the
usual assumption).
R = R0 * (1 + tol) * (1 + tcr * (T - Tref)). Call with tol = -0.005 and +0.005 for the two worst corners.
The TCR term is only valid over the span the DS covers, which the DS does not state (open item).
Aging (end of life): aging is the percent test limit of a PERFORMANCE row as a fraction (perf_load_life,
1000 h at rated power, +/-1.0 % -> +/-0.01) and aging_abs its additive term in ohm (perf_offset_ohm, +/-0.0005 ohm,
DS p.3 'TEST LIMITS'): R_EOL = R * (1 + aging) + aging_abs. Both default to 0, which is beginning of life and
reproduces the result without aging exactly. Full form:
R = R0 * (1 + tol) * (1 + tcr * (T - Tref)) * (1 + aging) + aging_abs.
INPUTS maps aging and aging_abs, so wca(..., **part.inputs("resistance_worst")) gives END-OF-LIFE bounds; pass
aging=0, aging_abs=0 (or call without them) for beginning of life.
r0: ohm. tol: fraction (0.005 = 0.5 %). tcr: 1/degC (35e-6 = 35 ppm/degC). t_c, t_ref_c: degC.
aging: fraction. aging_abs: ohm. Returns: ohm.
```

Inputs:

- `r0` -> `r_nom.typ` (typ 0.025 ohm)
- `tol` -> `tol` (min -0.5 max 0.5 %)
- `tcr` -> `tcr` (min -35 max 35 ppm/degC)
- `aging` -> `perf_load_life` (min -1.0 max 1.0 %)
- `aging_abs` -> `perf_offset_ohm` (min -0.0005 max 0.0005 ohm)

### `sense_voltage`

```
Not a DS equation: Ohm's law, V = I x R, for the E1-to-E2 sense voltage (DS p.3 Notes: E1, E2 sense the
voltage of the current path). i: A (signed). r: ohm. Returns: V.
```

Inputs:

- `r` -> `r_nom.typ` (typ 0.025 ohm)

### `dissipation`

```
Not a DS equation: P = I^2 x R, the power in the resistor (DS p.1 and p.3 rate power only). Physical relation.
i: A (either sign). r: ohm. Returns: W.
```

Inputs:

- `r` -> `r_nom.typ` (typ 0.025 ohm)

### `rated_power`

```
Rated power in W at AMBIENT temperature ta_c (degC).
Only p70 is a printed rating: DS p.1, Standard Electrical Specifications, P70 degC = 1.0 W (a maximum).
The 70 degC knee (knee_c) and the 170 degC zero (zero_c) are read off the DS p.3 DERATING graph (curve = true).
Result: p70 up to knee_c, then a linear fall to 0 W at zero_c. Above knee_c the result is a CURVE-BASED ESTIMATE,
not a datasheet bound. ta_c at or above zero_c gives 0 W.
ta_c, knee_c, zero_c: degC. p70: W. Returns: W.
```

Inputs:

- `p70` -> `p70.max` (max 1.0 W)
- `knee_c` -> `derate_knee.typ` (typ 70 degC)
- `zero_c` -> `derate_zero.typ` (typ 170 degC)

### `max_current`

```
Not a DS equation: largest continuous current magnitude I = sqrt(P / R), derived from P = I^2 R. The DS gives no
current figure. p_w: W, from rated_power (above 70 degC this is a CURVE-BASED ESTIMATE, see rated_power). r: ohm,
pass the largest resistance (resistance_worst) for a conservative bound. Returns: A (magnitude).
```

Inputs:

- `r` -> `r_nom.typ` (typ 0.025 ohm)

### `max_working_voltage`

```
Maximum working voltage across the resistor in V: V = (P x R)^1/2.
DS p.2, Technical Specifications, Maximum working voltage, (P x R)^1/2 (printed formula).
p_w: W, from rated_power (above 70 degC a CURVE-BASED ESTIMATE). r: ohm. Returns: V.
```

Inputs:

- `r` -> `r_nom.typ` (typ 0.025 ohm)


## Examples

| Call | Computed | Expected | Rel. tol | Result | Cite |
|---|---|---|---|---|---|
| rated_power(ta_c=70, p70=1, knee_c=70, zero_c=170) | 1 | 1 | 1e-09 | pass | DS p.1, Standard Electrical Specifications, P70 degC = 1.0 W (100 % at 70 degC, DS p.3 DERATING) |
| rated_power(ta_c=25, p70=1, knee_c=70, zero_c=170) | 1 | 1 | 1e-09 | pass | DS p.3, DERATING graph: 100 % flat below 70 degC (curve reading) |
| rated_power(ta_c=170, p70=1, knee_c=70, zero_c=170) | 0 | 0 | 1e-09 | pass | DS p.3, DERATING graph: 0 % at 170 degC (curve reading) |
| resistance_worst(r0=0.025, tol=0.005, tcr=0, t_c=25, t_ref_c=25, aging=0.01, aging_abs=0.0005) | 0.0258762 | 0.0258762 | 1e-09 | pass | DS p.1 TOL. +/-0.5 % (D); DS p.3 PERFORMANCE, Load life +/-1.0 % + 0.0005 ohm: high corner at end of life |
