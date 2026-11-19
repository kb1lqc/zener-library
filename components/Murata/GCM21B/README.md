<!-- GENERATED - do not edit. Run: python3 -m lib.readme -->

# GCM21B

## Datasheet review

[![Human page-image review: 0/53 human](https://img.shields.io/badge/human%20review-0%2F53%20human-lightgrey)](../../../docs/spec/datasheet-review.md)

Human page-image review: 0/53; cross-model audits: 18; manufacturer-export stamps: 0; legacy/unclassified: 0. Text checks are not verification. `lib.check` validates stamp format, not that review occurred.

## Part

- **manufacturer**: Murata
- **description**: Chip multilayer ceramic capacitors, X7R (R7) and C0G (5C), 2012M (0805), thickness 1.25 mm (code B), AEC-Q200 (GCM series)
- **category**: capacitor_mlcc
- **package**: 2012M (0805)
- **datasheet_url**: 
- **datasheet_file**: docs/datasheets/GCM21BR72A104KA37-01A-EN.pdf
- **datasheet_rev**: 01A
- **datasheet_date**: 2026-04
- **kicad_symbol**: GCM21B.kicad_sym
- **kicad_footprint**: GCM21B.kicad_mod
- **step**: GCM21B.step

## Series

- **Catalog**: `catalog.csv`, 137 orderable values, one row per value with its cite (a manufacturer export, not a datasheet table)
- **MPN rule**: catalog value + package letter; default `L`, alternates `K` (same part, other packaging); example: `GCM21BR70J106ME22` -> `GCM21BR70J106ME22L`
- **Selection**: `sel = part.select(capacitance, rated_voltage, dielectric, tolerance=None)` returns the MPN, `capacitance` / `rated_voltage` Params and `sel.part`, a Part holding the rows that apply (dielectric and part restrictions applied, plus `capacitance`, `tolerance`, `rated_v` and `tc`); an unlisted or ambiguous request raises ValueError
- **Zener wrapper**: configs `value`, `rated_v`, `dielectric`, optional `tolerance`; checks `part_orderable`, `rated_voltage` (|V(P1) - V(P2)| <= derate x rated voltage) and `ambient_range` (per dielectric)
- **Worst-case capacitance**: X7R (percent change): `wca(sel.part.calc.capacitance_worst_pct, **sel.part.inputs('capacitance_worst_pct'))`; C0G (ppm/degC): `wca(sel.part.calc.capacitance_worst_ppm, dt=Param(min=0, max=100), **sel.part.inputs('capacitance_worst_ppm'))` (dt required, 0 to 100 degC; below 25 degC use the printed drift rows). Both EXCLUDE DC-bias and aging loss

| Dielectric | Parts | Capacitance | Rated voltages | Tolerances | TC row |
|---|---|---|---|---|---|
| C0G | 67 | 680 pF to 39 nF | 50 V, 80 V, 100 V, 250 V, 630 V | ±1%, ±2%, ±5% | `tc_c0g` |
| X7R | 70 | 10 nF to 10 uF | 6.3 V, 10 V, 16 V, 25 V, 35 V, 50 V, 100 V, 250 V | ±10%, ±20% | `tc_x7r` |

## Pins

| Pin | Name | Type | Function | Cite |
|---|---|---|---|---|
| 1 | 1 | passive | Capacitor terminal (non-polarized) | DS p.2, Type & Dimension, image:Dimension |
| 2 | 2 | passive | Capacitor terminal (non-polarized) | DS p.2, Type & Dimension, image:Dimension |

## Parameters: rec_op

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Rated voltage (DC) |  | -100 (rel. 2) |  | 100 (rel. 2) | V | Voltage between pin 1 and pin 2 (non-polarized; either polarity) Applies to: parts GCM21BR72A104KA37. Note: DS prints DC 100V with no MIN/MAX label. Stored symmetric (min -100, max 100) because the part is non-polarized: \|V(1)-V(2)\| <= 100 V. The wrapper checks the catalog rating (same value for this part), not this row. | DS p.2, Rated Value, Rated Voltage (DC 100V) |  |
| Operating temperature range |  | -55 |  | 125 | degC | Applies to: dielectric X7R. Note: Read from the X7R reference sheet of GCM21BR72A104KA37. lib.catalog refuses an export row whose Operating Temperature is not -55 to 125 degC, so every X7R catalog row uses it. | DS p.2, Rated Value, Operating Temp. Range (-55 to 125 degC) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Self-heating of the capacitor body (AC or pulse load) |  |  | Below 20 degC self-heating at 25 degC ambient, for rated voltages below 100 VDC only (no limit printed for 100 VDC) |  | degC | Measured at 25 degC ambient; applies to rated voltage below 100 VDC Applies to: parts GCM21BR72A104KA37. Note: The DS limit is printed for rated voltages below 100 VDC. This part is 100 VDC, so no self-heating limit is stored (open item). | DS p.13, Rating 4. Type of Applied Voltage and Self-heating Temperature, '< Applicable to Rated Voltage of less than 100VDC >' |  |
| AC or pulse voltage: peak-to-peak (and zero-to-peak with DC) within the rated DC voltage |  |  | Vp-p <= rated DC voltage; AC superimposed on DC: zero-to-peak <= rated DC voltage |  |  | AC or pulse voltage applied Applies to: parts GCM21BR72A104KA37. | DS p.12, Rating 3. Applied Voltage, 1-1 (1) |  |
| Operating temperature range |  | -55 |  | 125 | degC | Applies to: dielectric C0G. Note: Read from the C0G reference sheet of GCM21A5C2E101FX01. lib.catalog refuses an export row whose Operating Temperature is not -55 to 125 degC, so every C0G catalog row uses it. | DS p.2 (GCM21A5C2E101FX01-00B-EN.pdf), Rated Value, Operating Temp. Range (-55 to 125 degC) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |

## Parameters: electrical

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Capacitance | C |  | 0.1 |  | uF | 25 degC, 1.0 +/-0.1 kHz, 1.0 +/-0.2 Vrms (DS p.5, No. 17) Applies to: parts GCM21BR72A104KA37. | DS p.2, Rated Value, Capacitance (0.1uF) |  |
| Capacitance tolerance |  | -10 |  | 10 | % | Applies to: parts GCM21BR72A104KA37. Note: Printed +/-10 % as a limit: min -10, max 10 (SPEC +/-X rule). The catalog tolerance of this value (catalog.csv) is the export's own printed value. | DS p.2, Rated Value, Capacitance Tolerance (+/-10 %) |  |
| Dissipation factor (DF), initial | DF |  |  | 0.025 |  | 25 degC, 1.0 +/-0.1 kHz, 1.0 +/-0.2 Vrms Applies to: parts GCM21BR72A104KA37. | DS p.5, Specifications and Test Methods, No. 18 Q or Dissipation Factor (DF) |  |
| Insulation resistance (IR), 25 degC | IR |  | More than 500 ohm*F (printed 'More than 500 Ω・F'), IR x C |  |  | 25 degC, rated voltage, charging time 2 min, charge/discharge current 50 mA max Applies to: parts GCM21BR72A104KA37. | DS p.6, Specifications and Test Methods, No. 19 Insulation Resistance (IR), Room Temperature |  |
| Insulation resistance (IR), 125 degC | IR |  | More than 10 ohm*F (printed 'More than 10 Ω・F'), IR x C |  |  | 125 degC, rated voltage, charging time 2 min, charge/discharge current 50 mA max Applies to: parts GCM21BR72A104KA37. | DS p.6, Specifications and Test Methods, No. 20 Insulation Resistance (IR), High Temperature |  |
| Insulation resistance, after resistance to solvents | IR |  | More than 500 ohm*F (printed 'More than 500 Ω・F'), IR x C |  |  | Room temperature, after MIL-STD-202 Method 215 Applies to: parts GCM21BR72A104KA37. | DS p.5, Specifications and Test Methods, No. 11 Resistance to Solvents, I.R. (Room Temp.) |  |
| Insulation resistance, after mechanical shock | IR |  | More than 500 ohm*F (printed 'More than 500 Ω・F'), IR x C |  |  | Room temperature, after mechanical shock (1500 g, half-sine, 0.5 ms) Applies to: parts GCM21BR72A104KA37. | DS p.5, Specifications and Test Methods, No. 12 Mechanical Shock, I.R. (Room Temp.) |  |
| Insulation resistance, after vibration | IR |  | More than 500 ohm*F (printed 'More than 500 Ω・F'), IR x C |  |  | Room temperature, after vibration (10 Hz to 2000 Hz to 10 Hz, 1.5 mm total amplitude, 20 min) Applies to: parts GCM21BR72A104KA37. | DS p.5, Specifications and Test Methods, No. 13 Vibration, I.R. (Room Temp.) |  |
| Insulation resistance, after resistance to soldering heat | IR |  | More than 500 ohm*F (printed 'More than 500 Ω・F'), IR x C |  |  | Room temperature, after 260 degC solder bath, 10 s Applies to: parts GCM21BR72A104KA37. | DS p.5, Specifications and Test Methods, No. 14 Resistance to Soldering Heat, I.R. (Room Temp.) |  |
| Insulation resistance, after ESD | IR |  | More than 500 ohm*F (printed 'More than 500 Ω・F'), IR x C |  |  | Room temperature, after AEC-Q200-002 ESD Applies to: parts GCM21BR72A104KA37. | DS p.5, Specifications and Test Methods, No. 15 ESD, I.R. (Room Temp.) |  |
| Capacitance change, board flex | dC | -10 |  | 10 | % | Board flex: flexure 2 mm, holding time 60 s, reflow solder on test substrate; after test Applies to: parts GCM21BR72A104KA37. | DS p.6, Specifications and Test Methods, No. 22 Board Flex, Capacitance Change |  |
| Insulation resistance, board flex | IR |  | More than 500 ohm*F (printed 'More than 500 Ω・F'), IR x C |  |  | Room temperature, after board flex test Applies to: parts GCM21BR72A104KA37. | DS p.6, Specifications and Test Methods, No. 22 Board Flex, I.R. (Room Temp.) |  |
| Insulation resistance, after terminal strength | IR |  | More than 500 ohm*F (printed 'More than 500 Ω・F'), IR x C |  |  | Room temperature, after terminal strength test (18 N applied force, 60 s) Applies to: parts GCM21BR72A104KA37. | DS p.6, Specifications and Test Methods, No. 23 Terminal Strength, I.R. (Room Temp.) |  |
| Capacitance change, high-temperature exposure (storage) | dC | -10 |  | 10 | % | 150 degC, 1000 h, no bias; after 24 h at room temperature (pre-treatment: 150 degC 1 h heat treatment) Applies to: parts GCM21BR72A104KA37. | DS p.3, Specifications and Test Methods, No. 3 High Temperature Exposure (Storage), Capacitance Change |  |
| Dissipation factor, high-temperature exposure | DF |  |  | 0.03 |  | 150 degC, 1000 h, no bias; after 24 h at room temperature Applies to: parts GCM21BR72A104KA37. | DS p.3, Specifications and Test Methods, No. 3 High Temperature Exposure (Storage), Q or D.F. |  |
| Insulation resistance, high-temperature exposure | IR |  | More than 500 ohm*F (printed 'More than 500 Ω・F'), IR x C |  |  | Room temperature, after 150 degC, 1000 h exposure Applies to: parts GCM21BR72A104KA37. | DS p.3, Specifications and Test Methods, No. 3 High Temperature Exposure (Storage), I.R. (Room Temp.) |  |
| Capacitance change, temperature cycling | dC | -10 |  | 10 | % | 1000 cycles, min operating temp to max operating temp; after room-temperature sit Applies to: parts GCM21BR72A104KA37. | DS p.3, Specifications and Test Methods, No. 4 Temperature Cycling, Capacitance Change |  |
| Dissipation factor, temperature cycling | DF |  |  | 0.03 |  | 1000 cycles, min operating temp to max operating temp Applies to: parts GCM21BR72A104KA37. | DS p.3, Specifications and Test Methods, No. 4 Temperature Cycling, Q or D.F. |  |
| Insulation resistance, temperature cycling | IR |  | More than 500 ohm*F (printed 'More than 500 Ω・F'), IR x C |  |  | Room temperature, after 1000 temperature cycles Applies to: parts GCM21BR72A104KA37. | DS p.3, Specifications and Test Methods, No. 4 Temperature Cycling, I.R. (Room Temp.) |  |
| Capacitance change, moisture resistance | dC | -12.5 |  | 12.5 | % | +25 degC to +65 degC, 80 to 98 %RH, 10 cycles of the 24 h profile Applies to: parts GCM21BR72A104KA37. | DS p.4, Specifications and Test Methods, No. 6 Moisture Resistance, Capacitance Change |  |
| Dissipation factor, moisture resistance | DF |  |  | 0.03 |  | +25 degC to +65 degC, 80 to 98 %RH, 10 cycles of the 24 h profile Applies to: parts GCM21BR72A104KA37. | DS p.4, Specifications and Test Methods, No. 6 Moisture Resistance, Q or D.F. |  |
| Insulation resistance, moisture resistance | IR |  | More than 500 ohm*F (printed 'More than 500 Ω・F'), IR x C |  |  | Room temperature, after the moisture test Applies to: parts GCM21BR72A104KA37. | DS p.4, Specifications and Test Methods, No. 6 Moisture Resistance, I.R. (Room Temp.) |  |
| Capacitance change, humidity bias | dC | -12.5 |  | 12.5 | % | 85 degC, 80 to 85 %RH, 1000 h; test voltage: rated voltage and 1.3 +0.2/-0 V DC (6.8 kohm series, as printed) Applies to: parts GCM21BR72A104KA37. | DS p.4, Specifications and Test Methods, No. 7 Humidity Bias, Capacitance Change |  |
| Dissipation factor, humidity bias | DF |  |  | 0.035 |  | 85 degC, 80 to 85 %RH, 1000 h Applies to: parts GCM21BR72A104KA37. | DS p.4, Specifications and Test Methods, No. 7 Humidity Bias, Q or D.F. |  |
| Insulation resistance, humidity bias | IR |  | More than 50 ohm*F (printed 'More than 50 Ω・F'), IR x C |  |  | Room temperature, after the humidity bias test Applies to: parts GCM21BR72A104KA37. | DS p.4, Specifications and Test Methods, No. 7 Humidity Bias, I.R. (Room Temp.) |  |
| Capacitance change, high-temperature operating life | dC | -12.5 |  | 12.5 | % | Max operating temp +/-3 degC (125 degC), 1000 h, 200 % of rated voltage Applies to: parts GCM21BR72A104KA37. | DS p.4, Specifications and Test Methods, No. 8 High Temperature Operating Life, Capacitance Change |  |
| Dissipation factor, high-temperature operating life | DF |  |  | 0.035 |  | Max operating temp +/-3 degC, 1000 h, 200 % of rated voltage Applies to: parts GCM21BR72A104KA37. | DS p.4, Specifications and Test Methods, No. 8 High Temperature Operating Life, Q or D.F. |  |
| Insulation resistance, high-temperature operating life | IR |  | More than 50 ohm*F (printed 'More than 50 Ω・F'), IR x C |  |  | Room temperature, after the high-temperature operating life test Applies to: parts GCM21BR72A104KA37. | DS p.4, Specifications and Test Methods, No. 8 High Temperature Operating Life, I.R. (Room Temp.) |  |
| Temperature characteristic, R7 (X7R) | TC | -15 |  | 15 | % | Ref. temp 25 degC; temp range -55 to 125 degC; capacitance change over temperature Applies to: dielectric X7R. Note: Public STD code X7R (EIA). Capacitance change over temperature, not a DC-bias or aging limit. Read from the reference sheet of the one part this directory has; used for every X7R catalog row (open item: confirm for each other X7R part). | DS p.2, Rated Value, Temp. coeff. or Cap. Change (-15 to 15 %) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Capacitance change with DC bias |  |  | Not specified: the sheet shows only an example curve |  |  | DC voltage applied Applies to: parts GCM21BR72A104KA37. Note: X7R loses capacitance under DC bias; the DS example curve (0.1 uF, 50 VDC sample) shows a large loss approaching rated voltage; it is an example, not a rating for this part. capacitance_worst_pct/_ppm exclude it: do not use capacitance_worst_pct as an in-circuit minimum. The DS also requires the AC/pulse zero-to-peak voltage to stay within the rated DC voltage; the Zener check is DC steady state only. | DS p.13, Rating 5. DC Voltage and AC Voltage Characteristic (example figure) |  |
| Temperature characteristic, C0G (EIA) | TC | -30 |  | 30 | ppm/degC | Ref. temp 25 degC; temp range printed as 25 to 125 degC; coefficient 0 +/-30 ppm/degC Applies to: dielectric C0G. Note: Public STD code C0G (EIA). A temperature coefficient, not a percent-change class. The DS prints the range 25 to 125 degC only: no coefficient is printed below 25 degC. The -55 to -10 degC capacitance drift is in the Table A rows (capdrift_*_c0g); the -10 to 25 degC segment has no printed number (open item). capacitance_worst_ppm requires dt and refuses values outside 0 to 100 degC (docs/SPEC.md, Capacitor series). | DS p.2 (GCM21A5C2E101FX01-00B-EN.pdf), Rated Value, Temp. coeff. or Cap. Change (0+/-30 ppm/degC), Temp. Range (25 to 125 degC) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Capacitance change at -55 degC vs 25 degC (Table A) | dC | -0.24 |  | 0.58 | % | Reference 25 degC, no bias; measured at -55 degC Applies to: dielectric C0G. Note: Printed Max 0.58, Min -0.24: stored as min -0.24, max 0.58 (printed columns). Covers only the -55 degC point. | DS p.7 (GCM21A5C2E101FX01-00B-EN.pdf), Table A Capacitance Change between at Reference Temp. and at each Temp. (%), 5C, -55 degC |  |
| Capacitance change at -30 degC vs 25 degC (Table A) | dC | -0.17 |  | 0.4 | % | Reference 25 degC, no bias; measured at -30 degC Applies to: dielectric C0G. Note: Printed Max 0.4, Min -0.17: stored as min -0.17, max 0.4 (printed columns). Covers only the -30 degC point. | DS p.7 (GCM21A5C2E101FX01-00B-EN.pdf), Table A Capacitance Change between at Reference Temp. and at each Temp. (%), 5C, -30 degC |  |
| Capacitance change at -10 degC vs 25 degC (Table A) | dC | -0.11 |  | 0.25 | % | Reference 25 degC, no bias; measured at -10 degC Applies to: dielectric C0G. Note: Printed Max 0.25, Min -0.11: stored as min -0.11, max 0.25 (printed columns). Covers only the -10 degC point. | DS p.7 (GCM21A5C2E101FX01-00B-EN.pdf), Table A Capacitance Change between at Reference Temp. and at each Temp. (%), 5C, -10 degC | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Capacitance drift limit (temperature characteristics test) | dC |  | Within +/-0.2 % or +/-0.05 pF, whichever is larger |  | % | Temperature characteristics test, 1.0 Vrms max; capacitance at steps 1, 3, 5 compared with step 3 Applies to: dielectric C0G. Note: Text row: the limit is the larger of a percentage and an absolute value. Not stored as numbers. | DS p.6 (GCM21A5C2E101FX01-00B-EN.pdf), Specifications and Test Methods, No. 25 Temperature Characteristics, Capacitance Drift |  |

## Parameters: mechanical

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Land pattern dimension a (reflow) | a | 1.2 |  | 1.2 | mm | Reflow soldering, chip 2.0x1.25 (+/-0.15), code 21 Note: Letter label only in the DS figure; neutral name. Inferred meaning: gap between lands (not printed). Row for the +/-0.15 chip; the +/-0.20 row is land_a_020. | DS p.27 (GCM21BR72A104KA37-01A-EN.pdf), 2. Land Dimensions, Table 2 Reflow Soldering Method, 2.0x1.25 (+/-0.15), a | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Land pattern dimension b (reflow) | b | 0.6 |  | 0.8 | mm | Reflow soldering, chip 2.0x1.25 (+/-0.15), code 21 Note: Letter label only in the DS figure; neutral name. Inferred meaning: land length, outer side (not printed). | DS p.27 (GCM21BR72A104KA37-01A-EN.pdf), 2. Land Dimensions, Table 2 Reflow Soldering Method, 2.0x1.25 (+/-0.15), b | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Land pattern dimension c (reflow) | c | 1.2 |  | 1.4 | mm | Reflow soldering, chip 2.0x1.25 (+/-0.15), code 21 Note: Letter label only in the DS figure; neutral name. Inferred meaning: land width across the chip (not printed). | DS p.27 (GCM21BR72A104KA37-01A-EN.pdf), 2. Land Dimensions, Table 2 Reflow Soldering Method, 2.0x1.25 (+/-0.15), c | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Land pattern dimension a (reflow) | a | 1.0 |  | 1.4 | mm | Reflow soldering, chip 2.0x1.25 (+/-0.20), code 21 Note: Letter label only in the DS figure; neutral name. Inferred meaning: gap between lands (not printed). | DS p.27 (GCM21BR72A104KA37-01A-EN.pdf), 2. Land Dimensions, Table 2 Reflow Soldering Method, 2.0x1.25 (+/-0.20), a | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Land pattern dimension b (reflow) | b | 0.6 |  | 0.8 | mm | Reflow soldering, chip 2.0x1.25 (+/-0.20), code 21 Note: Letter label only in the DS figure; neutral name. Inferred meaning: land length, outer side (not printed). | DS p.27 (GCM21BR72A104KA37-01A-EN.pdf), 2. Land Dimensions, Table 2 Reflow Soldering Method, 2.0x1.25 (+/-0.20), b | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Land pattern dimension c (reflow) | c | 1.2 |  | 1.4 | mm | Reflow soldering, chip 2.0x1.25 (+/-0.20), code 21 Note: Letter label only in the DS figure; neutral name. Inferred meaning: land width across the chip (not printed). | DS p.27 (GCM21BR72A104KA37-01A-EN.pdf), 2. Land Dimensions, Table 2 Reflow Soldering Method, 2.0x1.25 (+/-0.20), c | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Length (L) | L | 1.85 | 2.0 | 2.15 | mm | Applies to: parts GCM21BR72A104KA37. Note: min and max are the printed nominal 2.0 -/+ 0.15 (arithmetic); the DS prints 2.0+/-0.15. | DS p.2, Type & Dimension, L (2.0+/-0.15) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Width (W) | W | 1.1 | 1.25 | 1.4 | mm | Applies to: parts GCM21BR72A104KA37. Note: min and max are the printed nominal 1.25 -/+ 0.15 (arithmetic); the DS prints 1.25+/-0.15. | DS p.2, Type & Dimension, W (1.25+/-0.15) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Thickness (T) | T | 1.1 | 1.25 | 1.4 | mm | Applies to: parts GCM21BR72A104KA37. Note: min and max are the printed nominal 1.25 -/+ 0.15 (arithmetic). Catalog thickness column: 1.25mm +/-0.15mm for 92 rows, 1.25mm +/-0.2mm for 45 rows (open item). | DS p.2, Type & Dimension, T (1.25+/-0.15) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Terminal width (e) | e | 0.2 |  | 0.7 | mm | Applies to: parts GCM21BR72A104KA37. | DS p.2, Type & Dimension, e (0.2 to 0.7) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Gap between terminals (g) | g | 0.7 |  |  | mm | Applies to: parts GCM21BR72A104KA37. Note: Printed as a minimum only; no max stored. | DS p.2, Type & Dimension, g (0.7 min.) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Beam load test, destruction value |  |  | More than 20 N (destruction value) |  |  | Speed 0.5 mm/s; placement diagram Applies to: parts GCM21BR72A104KA37. | DS p.6, Specifications and Test Methods, No. 24 Beam Load Test | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Solderability: terminations soldered evenly and continuously |  | 95 |  |  | % | Specifications and Test Methods No.16 (a) test conditions Applies to: parts GCM21BR72A104KA37. Note: Assembly acceptance criterion, not a circuit limit. | DS p.5, Specifications and Test Methods, No.16 Solderability (a) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |

## Limits of this data

Rows by scope: 25C 3, full 1, na 45, partial 4 (25C rows hold only at 25 degC). Curve (graph) rows: 0. Text rows: 19.

## Zener checks

Generated wrapper: `GCM21B.zen` (`python3 -m lib.zen`). abs_max and rec_op rows are errors (abs_max x derate); 25C and partial rows are waivable warnings; a checked net with no voltage is UNVERIFIED.

| Param | Name | Checked against | Not checked / reason |
|---|---|---|---|
| rated_v_ds | Rated voltage (DC) | UNCHECKED | the generated rated_voltage check applies the catalog rated voltage of the selected part; this per-part row duplicates it (owner: module) |
| op_temp_x7r | Operating temperature range | board ambient |  |
| self_heating | Self-heating of the capacitor body (AC or pulse load) | UNCHECKED | depends on AC/pulse current, not a DC net voltage; the printed limit does not apply to this 100 VDC part; owner: module |
| ac_peak | AC or pulse voltage: peak-to-peak (and zero-to-peak with DC) within the rated DC voltage | UNCHECKED | AC/pulse waveform is not modelled by the DC net-voltage check; owner: module |
| op_temp_c0g | Operating temperature range | board ambient |  |

## Equations

### `capacitance_worst_pct`

```
Not a DS equation: C = C0 * (1 + tol) * (1 + tc).  For percent-change dielectrics (X7R): tc is the capacitance
change over the whole range as a FRACTION (DS p.2 of the X7R sheet, Rated Value, Temp. coeff. or Cap. Change,
-15 to 15 % over -55 to 125 degC, ref 25 degC), so with the row's min/max the corners give the full-range worst case.
For C0G use capacitance_worst_ppm: passing its 1/degC coefficient here would treat 3e-5 as a fraction and badly
understate the spread, so |tc| below 1e-3 (other than 0) raises ValueError.
EXCLUDES DC-bias and aging capacitance loss, which the reference sheet does not quantify (DS p.13 section 5 figure;
DS p.14 section 6 text). For X7R these can dominate. A worst-case stack of printed rows, not a guaranteed
capacitance.
c0: nominal capacitance, F (catalog, 'capacitance.typ'). tol: capacitance tolerance, fraction (catalog letter).
tc: capacitance change over temperature, fraction (the dielectric's row, 'tc'). Returns: C, F.
```

Inputs:

- `c0` -> `capacitance.typ` (from the catalog part selection, `Part.select`)
- `tol` -> `tolerance` (from the catalog part selection, `Part.select`)
- `tc` -> `tc` (from the catalog part selection, `Part.select`)

### `capacitance_worst_ppm`

```
Not a DS equation: C = C0 * (1 + tol) * (1 + tc * dt).  For ppm/degC dielectrics (C0G): tc is the coefficient in
1/degC (0 +/-30 ppm/degC, the 'tc' row) and dt = T - 25 degC in degC, REQUIRED (no default). The coefficient is
printed only for 25 to 125 degC (tc_c0g, scope partial), so dt is valid from 0 to 100 and ValueError is raised
outside it. Below 25 degC the coefficient is not printed: use the Table A capacitance-drift rows (capdrift_m55_c0g,
capdrift_m30_c0g, capdrift_m10_c0g) for -55 to -10 degC; the -10 to 25 degC segment has no printed number.
For a percent-change dielectric (X7R) use capacitance_worst_pct: a fraction passed here (|tc| above 1e-3) raises
ValueError. EXCLUDES DC-bias and aging loss. A worst-case stack of printed rows, not a guaranteed capacitance.
c0: nominal capacitance, F. tol: capacitance tolerance, fraction. tc: coefficient, 1/degC.
dt: temperature minus 25 degC, degC, 0 to 100 (wca: dt=Param(min=0, max=100)). Returns: C, F.
```

Inputs:

- `c0` -> `capacitance.typ` (from the catalog part selection, `Part.select`)
- `tol` -> `tolerance` (from the catalog part selection, `Part.select`)
- `tc` -> `tc` (from the catalog part selection, `Part.select`)


## Examples

| Call | Computed | Expected | Rel. tol | Result | Cite |
|---|---|---|---|---|---|
| capacitance_worst_ppm(c0=1e-10, tol=-0.01, tc=-3e-05, dt=100) | 9.8703e-11 | 9.8703e-11 | 1e-09 | pass | DS p.2, Rated Value (C0G sheet) |
| capacitance_worst_pct(c0=1e-07, tol=-0.1, tc=-0.15) | 7.65e-08 | 7.65e-08 | 1e-09 | pass | DS p.2, Rated Value |
