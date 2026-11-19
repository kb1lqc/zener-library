<!-- GENERATED - do not edit. Run: python3 -m lib.readme -->

# WSK2512-LOW

## Datasheet review

[![Human page-image review: 0/41 human](https://img.shields.io/badge/human%20review-0%2F41%20human-lightgrey)](../../../docs/spec/datasheet-review.md)

Human page-image review: 0/41; cross-model audits: 27; manufacturer-export stamps: 0; legacy/unclassified: 0. Text checks are not verification. `lib.check` validates stamp format, not that review occurred.

## Part

- **alternates**: []
- **manufacturer**: Vishay Dale
- **description**: 0.0005 to 0.0049 ohm (decade values) +/-0.5 % / +/-1.0 % 1 W 4-terminal (Kelvin) Power Metal Strip current-sense resistor series, 2512
- **category**: current_sense_resistor
- **package**: 2512 (4-terminal Kelvin, Power Metal Strip)
- **datasheet_url**: https://www.vishay.com/doc?30108
- **datasheet_file**: docs/datasheets/wsk2512.pdf
- **datasheet_rev**: 11-Dec-2023 (Document 30108)
- **datasheet_date**: 2023-12-11
- **temp_grade**: -65 to +170 degC
- **kicad_symbol**: WSK2512-LOW.kicad_sym
- **kicad_footprint**: WSK2512-LOW.kicad_mod
- **step**: none

## Series

- **Value range**: 1 mohm to 4.9 mohm (`res_range`)
- **E-series**: VISHAY-DECADE (40 values in range); VISHAY-DECADE only from 1 mohm
- **Tolerance options** (code, tolerance, range clipped to the series range, values; `Part.tolerance`, wrapper config `tolerance`):
  - `D`: +/-0.5 % (`tol_d`), 1 mohm to 4.9 mohm, 40 values (`r_range_d`)
  - `F`: +/-1 % (`tol_f`), 1 mohm to 4.9 mohm, 40 values (`r_range_f`)
- **MPN rule**: `calc.mpn(value, tol_code)`; examples: 1 mohm D -> `WSK25121L000DEA`, 3 mohm D -> `WSK25123L000DEA`, 4.9 mohm F -> `WSK25124L900FEA`
- **TCR by value** (`Part.tcr(value)` returns the row whose range holds the value): `tcr_500u_990u` for 500 uohm to 990 uohm, `tcr_1m_2m9` for 1 mohm to 2.9 mohm, `tcr_3m_4m9` for 3 mohm to 4.9 mohm
- **Rated voltage**: sqrt(P70 x R), P70 = 1 W (`p70`); the datasheet prints no limiting element voltage
- **Zener wrapper**: config `value` and `tolerance` (a code), optional `v_across` (the module's worst-case voltage across the part; replaces the net ranges in `rated_voltage` when set); checks `value_allowed` and `rated_voltage` (|V(I1) - V(I2)| <= derate x rated voltage). It uses the 70 degC power rating at every ambient, so above 70 degC it is optimistic: use `calc.rated_power` (curve-based) for hot designs
- **Worst-case resistance**: `wca(calc.resistance_worst, r0=<value>, tol=part.tolerance(<code>), tcr=part.tcr(<value>), ...)` with the plain value as r0; `Part.series_value(value)` already includes the tolerance, so do not pass it as r0 together with tol (that counts the tolerance twice)

Rated voltage at decade values, computed from `p70` and the formula above:

| Resistance | Rated voltage |
|---|---|
| 1 mohm | 31.62 mV |

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
| Power rating at 70 degC ambient | P70 degC |  |  | 1.0 | W | Ambient 70 degC; one rating for every value of the WSK2512 model Note: Rating: a maximum, stored as max. No abs-max table. Rated against AMBIENT (DS p.3 DERATING axis); self-heating is not given. | DS p.1, Standard Electrical Specifications, POWER RATING P70 degC, W, 1.0 | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Maximum working voltage |  |  | (P x R)^1/2 |  | V | Note: Formula, not a number. calc.py max_working_voltage implements it. The DS prints no limiting element voltage, so the series has no series_vlimit. | DS p.2, Technical Specifications, Maximum working voltage, (P x R)^1/2 | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Operating temperature range |  | -65 |  | 170 | degC | Note: The DS does not say whether this is ambient or element temperature; read as ambient (DS p.3 DERATING axis). Only temperature rating in the DS (no storage or abs-max row). | DS p.2, Technical Specifications, Operating temperature range, -65 to +170 | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Derating knee: 100 % rated power up to | TA knee |  | 70 |  | degC | Note: Read off the graph. Not a worst-case bound (curve). | DS p.3, Figure: DERATING graph (unnumbered; rated power vs ambient, 100 % line ends at 70 degC); coincides with DS p.1 P70 degC (curve) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Derating: 0 % rated power at | TA zero |  | 170 |  | degC | Note: Read off the graph (no printed number). Coincides with the top of the operating range (DS p.2). Linear between knee and zero (graph shape). | DS p.3, Figure: DERATING graph (unnumbered; rated power vs ambient, line reaches 0 % at 170 degC) (curve) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |

## Parameters: electrical

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Series resistance range (this directory) |  | 0.0005 |  | 0.0049 | ohm | Note: Directory range: the low-value half of the WSK2512 model, split where the DS pad dimensions (a, l) change (0.005 ohm). Each tolerance range is clipped to it. The +/-0.1 % option (code B, 0.01 to 0.2 ohm) has no value here and is not listed. | DS p.2, SOLDER PAD DIMENSIONS table, resistance range 0.0005 to 0.0049 row (also DS p.2, DIMENSIONS table, rows 0.0005 to 0.00099 and 0.001 to 0.0049) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Resistance value range, +/-0.5 % tolerance (code D) |  | 0.001 |  | 0.2 | ohm | Note: As printed for the whole WSK2512 model; the series clips it to res_range. | DS p.1, Standard Electrical Specifications, Resistance value range TOL. +/-0.5 % column, 0.001 to 0.2 row |  |
| Resistance value range, +/-1.0 % tolerance (code F) |  | 0.0005 |  | 0.2 | ohm | Note: As printed for the whole WSK2512 model; the series clips it to res_range. | DS p.1, Standard Electrical Specifications, Resistance value range TOL. +/-1.0 % column, 0.0005 to 0.2 row |  |
| Resistance tolerance, code D | TOL | -0.5 |  | 0.5 | % | Note: The DS does not state the reference temperature for the tolerance. | DS p.1, Standard Electrical Specifications, TOL. +/-0.5 % column; DS p.1, Global Part Number Information, tolerance code D = +/-0.5 % | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Resistance tolerance, code F | TOL | -1.0 |  | 1.0 | % | Note: The DS does not state the reference temperature for the tolerance. | DS p.1, Standard Electrical Specifications, TOL. +/-1.0 % column; DS p.1, Global Part Number Information, tolerance code F = +/-1.0 % |  |
| Temperature coefficient of resistance, 0.5 mohm to 0.99 mohm | TCR | -350 |  | 350 | ppm/degC | Resistance range 0.5 mohm to 0.99 mohm Note: DS p.1 Features says 'low TCR (< 20 ppm/degC)'. Feature text is not a specification; the table value +/-350 is used (open item). The DS states neither the reference temperature nor the temperature span over which the TCR holds. Selected per value by Part.tcr(value) through [part] series_tcr (its range row is tcr_500u_990u_range). | DS p.2, Technical Specifications, Temperature coefficient (RESISTOR CHARACTERISTICS), +/-350 for 0.5 mohm to 0.99 mohm |  |
| TCR range: 0.5 mohm to 0.99 mohm |  | 0.0005 |  | 0.00099 | ohm | Note: Range for which the TCR row of the same name applies, as printed. | DS p.2, Technical Specifications, Temperature coefficient, range 0.5 mohm to 0.99 mohm | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Temperature coefficient of resistance, 0.001 ohm to 0.0029 ohm | TCR | -250 |  | 250 | ppm/degC | Resistance range 0.001 ohm to 0.0029 ohm Note: DS p.1 Features says 'low TCR (< 20 ppm/degC)'. Feature text is not a specification; the table value +/-250 is used (open item). The DS states neither the reference temperature nor the temperature span over which the TCR holds. Selected per value by Part.tcr(value) through [part] series_tcr (its range row is tcr_1m_2m9_range). | DS p.2, Technical Specifications, Temperature coefficient (RESISTOR CHARACTERISTICS), +/-250 for 0.001 ohm to 0.0029 ohm |  |
| TCR range: 0.001 ohm to 0.0029 ohm |  | 0.001 |  | 0.0029 | ohm | Note: Range for which the TCR row of the same name applies, as printed. | DS p.2, Technical Specifications, Temperature coefficient, range 0.001 ohm to 0.0029 ohm | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Temperature coefficient of resistance, 0.003 ohm to 0.0049 ohm | TCR | -75 |  | 75 | ppm/degC | Resistance range 0.003 ohm to 0.0049 ohm Note: DS p.1 Features says 'low TCR (< 20 ppm/degC)'. Feature text is not a specification; the table value +/-75 is used (open item). The DS states neither the reference temperature nor the temperature span over which the TCR holds. Selected per value by Part.tcr(value) through [part] series_tcr (its range row is tcr_3m_4m9_range). | DS p.2, Technical Specifications, Temperature coefficient (RESISTOR CHARACTERISTICS), +/-75 for 0.003 ohm to 0.0049 ohm | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| TCR range: 0.003 ohm to 0.0049 ohm |  | 0.003 |  | 0.0049 | ohm | Note: Range for which the TCR row of the same name applies, as printed. | DS p.2, Technical Specifications, Temperature coefficient, range 0.003 ohm to 0.0049 ohm | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Performance test limit, additive term (all PERFORMANCE rows) |  | -0.0005 |  | 0.0005 | ohm | Added to the percent term of every PERFORMANCE row: total limit ±(X % of R + 0.0005 ohm) Note: Printed '± X % + 0.0005 Ω' with no brackets. Stored symmetric, ±(X % of R + 0.0005 ohm): the conservative worst-case reading (a one-sided +0.0005 would understate the low side). Open item: confirm the reading with Vishay. | DS p.3, PERFORMANCE, TEST LIMITS column, '+ 0.0005 ohm' (all rows) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md); symmetric reading approved by the designer (audit R1) |
| Resistance change, thermal shock |  | -0.5 |  | 0.5 | % | -55 degC to +150 degC, 1000 cycles, 15 min at each extreme Note: Printed ± 0.5 %. Total limit ±(0.5 % of R + 0.0005 ohm); add perf_offset_ohm. | DS p.3, PERFORMANCE, Thermal shock, TEST LIMITS |  |
| Resistance change, short time overload |  | -0.5 |  | 0.5 | % | Overload level not printed; DS refers to external link www.vishay.com/en/resistors/power-metal-strip-calculator/ Note: Printed ± 0.5 %. Total limit ±(0.5 % of R + 0.0005 ohm); add perf_offset_ohm. Do not apply to any specific overload: the DS gives no level. Pulse capability has no numbers in the DS (online calculator only). | DS p.3, PERFORMANCE, Short time overload, TEST LIMITS |  |
| Resistance change, low temperature operation |  | -0.5 |  | 0.5 | % | -65 degC for 24 h Note: Printed ± 0.5 %. Total limit ±(0.5 % of R + 0.0005 ohm); add perf_offset_ohm. | DS p.3, PERFORMANCE, Low temperature operation, TEST LIMITS |  |
| Resistance change, high temperature exposure |  | -1.0 |  | 1.0 | % | 1000 h at +170 degC Note: Printed ± 1.0 % (not 0.5 %). Total limit ±(1.0 % of R + 0.0005 ohm); add perf_offset_ohm. | DS p.3, PERFORMANCE, High temperature exposure, TEST LIMITS |  |
| Resistance change, bias humidity |  | -0.5 |  | 0.5 | % | +85 degC, 85 % RH, 10 % bias, 1000 h Note: Printed ± 0.5 %. Total limit ±(0.5 % of R + 0.0005 ohm); add perf_offset_ohm. | DS p.3, PERFORMANCE, Bias humidity, TEST LIMITS |  |
| Resistance change, mechanical shock |  | -0.5 |  | 0.5 | % | 100 g for 6 ms, 5 pulses Note: Printed ± 0.5 %. Total limit ±(0.5 % of R + 0.0005 ohm); add perf_offset_ohm. | DS p.3, PERFORMANCE, Mechanical shock, TEST LIMITS |  |
| Resistance change, vibration |  | -0.5 |  | 0.5 | % | Frequency varied 10 Hz to 2000 Hz in 1 min, 3 directions, 12 h Note: Printed ± 0.5 %. Total limit ±(0.5 % of R + 0.0005 ohm); add perf_offset_ohm. | DS p.3, PERFORMANCE, Vibration, TEST LIMITS |  |
| Resistance change, load life |  | -1.0 |  | 1.0 | % | 1000 h at rated power, +70 degC, 1.5 h ON, 0.5 h OFF Note: Printed ± 1.0 % (not 0.5 %). Total limit ±(1.0 % of R + 0.0005 ohm); add perf_offset_ohm. | DS p.3, PERFORMANCE, Load life, TEST LIMITS |  |
| Resistance change, resistance to solder heat |  | -0.5 |  | 0.5 | % | +260 degC solder, 10 s to 12 s dwell, 25 mm/s emergence Note: Printed ± 0.5 %. Total limit ±(0.5 % of R + 0.0005 ohm); add perf_offset_ohm. | DS p.3, PERFORMANCE, Resistance to solder heat, TEST LIMITS | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Resistance change, moisture resistance |  | -0.5 |  | 0.5 | % | MIL-STD-202, method 106, 0 % power, 7a and 7b not required Note: Printed ± 0.5 %. Total limit ±(0.5 % of R + 0.0005 ohm); add perf_offset_ohm. | DS p.3, PERFORMANCE, Moisture resistance, TEST LIMITS |  |

## Parameters: mechanical

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Body length | L | 6.096 | 6.35 | 6.604 | mm | Note: Printed 6.35 +/-0.254 mm (0.250 in). Same for all resistance rows. min/max = nominal ±0.254 mm (arithmetic on the printed tolerance). | DS p.2, DIMENSIONS table (mm in brackets), row 0.0005 to 0.0049, column L | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Body width | W | 2.926 | 3.18 | 3.434 | mm | Note: Printed 3.18 +/-0.254 mm (0.125 in). Same for all resistance rows. min/max = nominal ±0.254 mm (arithmetic on the printed tolerance). | DS p.2, DIMENSIONS table (mm in brackets), row 0.0005 to 0.0049, column W | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Body height | H | 0.381 | 0.635 | 0.889 | mm | Note: Printed 0.635 +/-0.254 mm (0.025 in). Same for all resistance rows (DS p.2 prints one H cell for every row). min/max = nominal ±0.254 mm (arithmetic on the printed tolerance). | DS p.2, DIMENSIONS table (mm in brackets), row 0.0005 to 0.0049, column H | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Terminal length (T), 0.0005 to 0.00099 ohm | T | 2.406 | 2.66 | 2.914 | mm | Note: Printed 2.66 +/-0.254 mm (0.105 in). min/max = nominal +/-0.254 mm (arithmetic on the printed tolerance). T differs between the DS resistance rows. | DS p.2, DIMENSIONS table (mm in brackets), row 0.0005 to 0.00099, column T | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Terminal length (T), 0.001 to 0.0049 ohm | T | 1.956 | 2.21 | 2.464 | mm | Note: Printed 2.21 +/-0.254 mm (0.087 in). min/max = nominal +/-0.254 mm (arithmetic on the printed tolerance). T differs between the DS resistance rows. | DS p.2, DIMENSIONS table (mm in brackets), row 0.001 to 0.0049, column T | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Terminal width, A | A | 0.508 | 0.762 | 1.016 | mm | Note: Printed 0.762 +/-0.254 mm (0.030 in). Same for all resistance rows. min/max = nominal ±0.254 mm (arithmetic on the printed tolerance). | DS p.2, DIMENSIONS table (mm in brackets), row 0.0005 to 0.0049, column A | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Terminal width, B | B | 0.254 | 0.508 | 0.762 | mm | Note: Printed 0.508 +/-0.254 mm (0.020 in). Same for all resistance rows. min/max = nominal ±0.254 mm (arithmetic on the printed tolerance). | DS p.2, DIMENSIONS table (mm in brackets), row 0.0005 to 0.0049, column B | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Land pattern dimension a (DS p.2 diagram) | a |  | 3.3 |  | mm | Note: Printed 0.130 in (3.30 mm). INFERRED feature, not printed: the arrow a runs from the sense-pad end to the far current-pad edge, same inferred feature as in the 0.005 to 0.2 ohm series, a different value here. Feature unverified. | DS p.2, SOLDER PAD DIMENSIONS (mm in brackets), row 0.0005 to 0.0049, column a | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Land pattern dimension b (DS p.2 diagram) | b |  | 3.3 |  | mm | Note: Printed 0.130 in (3.30 mm). INFERRED feature, not printed: overall Y span of the pattern (3.30 = footprint -1.651..+1.651 mm). Arrow b runs from the top of the upper current pad to the bottom of the sense pad. | DS p.2, SOLDER PAD DIMENSIONS (mm in brackets), row 0.0005 to 0.0049, column b | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Land pattern dimension c (DS p.2 diagram) | c |  | 0.76 |  | mm | Note: Printed 0.030 in (0.76 mm). INFERRED feature, not printed: width of the sense pad (arrow c spans its short edge). | DS p.2, SOLDER PAD DIMENSIONS (mm in brackets), row 0.0005 to 0.0049, column c | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Land pattern dimension d (DS p.2 diagram) | d |  | 0.51 |  | mm | Note: Printed 0.020 in (0.51 mm). INFERRED feature, not printed: gap between the current pad and the sense pad (arrow d). | DS p.2, SOLDER PAD DIMENSIONS (mm in brackets), row 0.0005 to 0.0049, column d | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Land pattern dimension e (DS p.2 diagram) | e |  | 1.7 |  | mm | Note: Printed 0.067 in (1.70 mm). INFERRED feature, not printed: length of the sense pad (arrow e spans its long edge). | DS p.2, SOLDER PAD DIMENSIONS (mm in brackets), row 0.0005 to 0.0049, column e | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Land pattern dimension l (DS p.2 diagram) | l |  | 1.65 |  | mm | Note: Printed 0.065 in (1.65 mm). INFERRED, supported by footprint and figure: l = gap between the two current pads. | DS p.2, SOLDER PAD DIMENSIONS (mm in brackets), row 0.0005 to 0.0049, column l | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Weight |  |  | 63.6 |  | mg | typical; DS prints 63.6 g per 1000 pieces Note: Per part: 63.6 g per 1000 pieces = 63.6 mg per part. Typical only. | DS p.1, Standard Electrical Specifications, WEIGHT (typical) g/1000 pieces, row WSK2512 | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |

## Limits of this data

Rows by scope: na 41 (25C rows hold only at 25 degC). Curve (graph) rows: 2. Text rows: 1.

## Zener checks

Generated wrapper: `WSK2512-LOW.zen` (`python3 -m lib.zen`). abs_max and rec_op rows are errors (abs_max x derate); 25C and partial rows are waivable warnings; a checked net with no voltage is UNVERIFIED.

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
R = R0 * (1 + tol) * (1 + tcr * (T - Tref)). Call with tol = the tolerance row of the part's code (Part.tolerance(code),
+/-0.1 %, +/-0.5 % or +/-1.0 %) and tcr = Part.tcr(value), the TCR row whose resistance range holds the value.
The TCR term is only valid over the span the DS covers, which the DS does not state (open item).
Aging (end of life): aging is the percent test limit of a PERFORMANCE row as a fraction (perf_load_life,
1000 h at rated power, +/-1.0 % -> +/-0.01) and aging_abs its additive term in ohm (perf_offset_ohm, +/-0.0005 ohm,
DS p.3 'TEST LIMITS'): R_EOL = R * (1 + aging) + aging_abs. Both default to 0, which is beginning of life and
reproduces the result without aging exactly. Full form:
R = R0 * (1 + tol) * (1 + tcr * (T - Tref)) * (1 + aging) + aging_abs.
INPUTS maps aging and aging_abs, so wca(..., **part.inputs("resistance_worst")) gives END-OF-LIFE bounds; pass
aging=0, aging_abs=0 (or call without them) for beginning of life.
r0: ohm, the plain nominal value (not Part.series_value, which already carries the tolerance). tol: fraction (0.005 = 0.5 %). tcr: 1/degC (35e-6 = 35 ppm/degC). t_c, t_ref_c: degC.
aging: fraction. aging_abs: ohm. Returns: ohm.
```

Inputs:

- `aging` -> `perf_load_life` (min -1.0 max 1.0 %)
- `aging_abs` -> `perf_offset_ohm` (min -0.0005 max 0.0005 ohm)

### `sense_voltage`

```
Not a DS equation: Ohm's law, V = I x R, for the E1-to-E2 sense voltage (DS p.3 Notes: E1, E2 sense the
voltage of the current path). i: A (signed). r: ohm. Returns: V.
```

Inputs:


### `dissipation`

```
Not a DS equation: P = I^2 x R, the power in the resistor (DS p.1 and p.3 rate power only). Physical relation.
i: A (either sign). r: ohm. Returns: W.
```

Inputs:


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


### `max_working_voltage`

```
Maximum working voltage across the resistor in V: V = (P x R)^1/2.
DS p.2, Technical Specifications, Maximum working voltage, (P x R)^1/2 (printed formula).
p_w: W, from rated_power (above 70 degC a CURVE-BASED ESTIMATE). r: ohm. Returns: V.
```

Inputs:


### `mpn`

```
Not a DS equation: part number from the DS decode rule (DS p.1, Global Part Number Information):
WSK2512 + resistance value (5 characters) + tolerance code + EA (lead (Pb)-free, tape / reel) + no dash number.
Value code: "L" = mohm for values below 0.01 ohm ("Use L for resistance values < 0.01 ohm", 5L000 = 0.005 ohm),
"R" = decimal point in ohm (R0100 = 0.01 ohm). Four digits follow or surround the letter:
  - 0.01 ohm and above: "R" + the value in ohm to four decimals: 0.025 -> R0250, 0.2 -> R2000.
  - 0.001 to 0.00999 ohm: the whole mohm digit, "L", three decimals of mohm: 0.005 -> 5L000, 0.0011 -> 1L100.
  - below 0.001 ohm: "L" + the mohm value to four decimals (the L stands for the decimal point):
    0.0005 -> L5000. INFERRED: the DS prints no sub-1 mohm example (open item).
Tolerance code B = +/-0.1 %, D = +/-0.5 %, F = +/-1.0 % (DS p.1). EA is the only packaging written; EK (bulk) is the
same part (alternate). The value must have at most the digits above (decade values do) or ValueError is raised.
Only this directory's range 0.0005 to 0.0049 ohm and the codes D, F are checked here (B, +/-0.1 %, starts at 0.01 ohm: not in this directory); the range each code covers
(DS p.1, Standard Electrical Specifications) lives in component.toml and is enforced by Part.values / Part.mpn.
r_ohm: ohm. tol_code: "D" or "F". Returns: str.
```

Inputs:



## Examples

| Call | Computed | Expected | Rel. tol | Result | Cite |
|---|---|---|---|---|---|
| rated_power(ta_c=70, p70=1, knee_c=70, zero_c=170) | 1 | 1 | 1e-09 | pass | DS p.1, Standard Electrical Specifications, P70 degC = 1.0 W (100 % at 70 degC, DS p.3 DERATING) |
| rated_power(ta_c=170, p70=1, knee_c=70, zero_c=170) | 0 | 0 | 1e-09 | pass | DS p.3, DERATING graph: 0 % at 170 degC (curve reading) |
| rated_power(ta_c=25, p70=1, knee_c=70, zero_c=170) | 1 | 1 | 1e-09 | pass | DS p.3, DERATING graph: 100 % flat below 70 degC (curve reading) |
| resistance_worst(r0=0.003, tol=0.005, tcr=0, t_c=25, t_ref_c=25, aging=0.01, aging_abs=0.0005) | 0.00354515 | 0.00354515 | 1e-09 | pass | DS p.1 TOL. +/-0.5 % (D); DS p.3 PERFORMANCE, Load life +/-1.0 % + 0.0005 ohm: high corner at end of life |
