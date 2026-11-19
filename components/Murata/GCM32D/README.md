<!-- GENERATED - do not edit. Run: python3 -m lib.readme -->

# GCM32D

## Datasheet review

[![Human page-image review: 0/73 human](https://img.shields.io/badge/human%20review-0%2F73%20human-lightgrey)](../../../docs/spec/datasheet-review.md)

Human page-image review: 0/73; cross-model audits: 0; manufacturer-export stamps: 0; legacy/unclassified: 0. Text checks are not verification. `lib.check` validates stamp format, not that review occurred.

## Part

- **manufacturer**: Murata
- **description**: Chip multilayer ceramic capacitors, X7R (R7) and C0G (5C), 3225M (1210), thickness 2.0 mm (code D), AEC-Q200 (GCM series)
- **category**: capacitor_mlcc
- **package**: 3225M (1210)
- **datasheet_url**: 
- **datasheet_file**: docs/datasheets/GCM32D5C3A682GX01-00B-EN.pdf
- **datasheet_rev**: 00B
- **datasheet_date**: 2026-04
- **kicad_symbol**: GCM32D.kicad_sym
- **kicad_footprint**: GCM32D.kicad_mod
- **step**: GCM32D.step

## Series

- **Catalog**: `catalog.csv`, 41 orderable values, one row per value with its cite (a manufacturer export, not a datasheet table)
- **MPN rule**: catalog value + package letter; default `L`, alternates `K` (same part, other packaging); example: `GCM32D5C3A822JX01` -> `GCM32D5C3A822JX01L`
- **Selection**: `sel = part.select(capacitance, rated_voltage, dielectric, tolerance=None)` returns the MPN, `capacitance` / `rated_voltage` Params and `sel.part`, a Part holding the rows that apply (dielectric and part restrictions applied, plus `capacitance`, `tolerance`, `rated_v` and `tc`); an unlisted or ambiguous request raises ValueError
- **Zener wrapper**: configs `value`, `rated_v`, `dielectric`, optional `tolerance`; checks `part_orderable`, `rated_voltage` (|V(P1) - V(P2)| <= derate x rated voltage) and `ambient_range` (per dielectric)
- **Worst-case capacitance**: X7R (percent change): `wca(sel.part.calc.capacitance_worst_pct, **sel.part.inputs('capacitance_worst_pct'))`; C0G (ppm/degC): `wca(sel.part.calc.capacitance_worst_ppm, dt=Param(min=0, max=100), **sel.part.inputs('capacitance_worst_ppm'))` (dt required, 0 to 100 degC; below 25 degC use the printed drift rows). Both EXCLUDE DC-bias and aging loss

| Dielectric | Parts | Capacitance | Rated voltages | Tolerances | TC row |
|---|---|---|---|---|---|
| C0G | 33 | 4.7 nF to 18 nF | 630 V, 1 kV, 1.25 kV | ±1%, ±2%, ±5% | `tc_c0g` |
| X7R | 8 | 15 nF to 220 nF | 250 V, 630 V | ±10% | `tc_x7r` |

## Pins

| Pin | Name | Type | Function | Cite |
|---|---|---|---|---|
| 1 | 1 | passive | Capacitor terminal (non-polarized) | DS p.2, Type & Dimension, image:Dimension |
| 2 | 2 | passive | Capacitor terminal (non-polarized) | DS p.2, Type & Dimension, image:Dimension |

## Parameters: rec_op

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Rated voltage (DC) |  | -1000 (rel. 2) |  | 1000 (rel. 2) | V | Voltage between pin 1 and pin 2 (non-polarized; either polarity) Applies to: parts GCM32D5C3A682GX01. Note: DS prints DC 1000V with no MIN/MAX label. Stored symmetric (min -1000, max 1000) because the part is non-polarized: \|V(1)-V(2)\| <= 1000 V. The wrapper checks the catalog rating (same value for this part), not this row. | DS p.2, Rated Value, Rated Voltage (DC 1000V) |  |
| Rated voltage (DC) |  | -630 (rel. 2) |  | 630 (rel. 2) | V | Voltage between pin 1 and pin 2 (non-polarized; either polarity) Applies to: parts GCM32D5C2J123FX01. Note: DS prints DC 630V with no MIN/MAX label. Stored symmetric (min -630, max 630) because the part is non-polarized. The wrapper checks the catalog rating, not this row. | DS p.2 (GCM32D5C2J123FX01-00B-EN.pdf), Rated Value, Rated Voltage (DC 630V) |  |
| Operating temperature range |  | -55 |  | 125 | degC | Applies to: dielectric C0G. Note: Read from the C0G reference sheet of GCM32D5C3A682GX01 (the 123 sheet prints the same). lib.catalog refuses an export row whose Operating Temperature is not -55 to 125 degC, so every C0G catalog row uses it. | DS p.2 (GCM32D5C3A682GX01-00B-EN.pdf), Rated Value, Operating Temp. Range (-55 to 125 degC) |  |
| Operating temperature range |  | -55 |  | 125 | degC | Applies to: dielectric X7R. Note: Read from the 1210 X7R sheet GCM32ER71C226ME19-01A. lib.catalog refuses an export row whose Operating Temperature is not -55 to 125 degC, so every X7R catalog row uses it. | DS p.2 (GCM32ER71C226ME19-01A-EN.pdf), Rated Value, Operating Temp. Range (-55 to 125 degC) |  |

## Parameters: electrical

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Capacitance | C |  | 6800 |  | pF | 25 degC, 1.0 +/-0.1 kHz, 1.0 +/-0.2 Vrms (DS p.5, No. 17) Applies to: parts GCM32D5C3A682GX01. | DS p.2, Rated Value, Capacitance (6800pF) |  |
| Capacitance tolerance |  | -2 |  | 2 | % | Applies to: parts GCM32D5C3A682GX01. Note: Printed +/-2 % as a limit: min -2, max 2 (SPEC +/-X rule). The catalog tolerance of this value (catalog.csv) is the export's own printed value. | DS p.2, Rated Value, Capacitance Tolerance (+/-2 %) |  |
| Q or dissipation factor (Q), initial | Q | 1000 |  |  |  | 25 degC, 1.0 +/-0.1 kHz, 1.0 +/-0.2 Vrms Applies to: parts GCM32D5C3A682GX01. Note: C0G is specified as Q (not DF): stored as a minimum, as printed. | DS p.5, Specifications and Test Methods, No. 18 Q or Dissipation Factor (DF): Q>=1000 |  |
| Insulation resistance (IR), 25 degC | IR |  | More than 100000 MΩ (printed 'More than 100000MΩ') |  |  | 25 degC, DC 500 V +/-50 V, charging time 1 min, charge/discharge current 50 mA max Applies to: parts GCM32D5C3A682GX01. | DS p.5, Specifications and Test Methods, No. 19 Insulation Resistance (IR), Room Temperature |  |
| Insulation resistance (IR), 125 degC | IR |  | More than 1000 MΩ (printed 'More than 1000MΩ') |  |  | 125 degC, DC 500 V +/-50 V, charging time 1 min, charge/discharge current 50 mA max Applies to: parts GCM32D5C3A682GX01. | DS p.5, Specifications and Test Methods, No. 20 Insulation Resistance (IR), High Temperature |  |
| Capacitance change, high-temperature exposure (storage) | dC | -2 |  | 2 | % | 150 degC, 1000 h, no bias; after 24 h at room temperature Applies to: parts GCM32D5C3A682GX01. | DS p.3, Specifications and Test Methods, No. 3 High Temperature Exposure (Storage), Capacitance Change |  |
| Q, high-temperature exposure | Q |  | Within the specified initial value |  |  | 150 degC, 1000 h, no bias; after 24 h at room temperature Applies to: parts GCM32D5C3A682GX01. | DS p.3, Specifications and Test Methods, No. 3 High Temperature Exposure (Storage), Q or D.F. |  |
| Insulation resistance, high-temperature exposure | IR |  | More than 10000 MΩ (printed 'More than 10000MΩ') |  |  | Room temperature, after 150 degC, 1000 h exposure Applies to: parts GCM32D5C3A682GX01. | DS p.3, Specifications and Test Methods, No. 3 High Temperature Exposure (Storage), I.R. (Room Temp.) |  |
| Capacitance change, temperature cycling | dC | -2 |  | 2 | % | 1000 cycles, min operating temp to max operating temp (15 min dwell each); after room-temperature sit Applies to: parts GCM32D5C3A682GX01. | DS p.3, Specifications and Test Methods, No. 4 Temperature Cycling, Capacitance Change |  |
| Q, temperature cycling | Q |  | Within the specified initial value |  |  | 1000 cycles; after room-temperature sit Applies to: parts GCM32D5C3A682GX01. | DS p.3, Specifications and Test Methods, No. 4 Temperature Cycling, Q or D.F. |  |
| Insulation resistance, temperature cycling | IR |  | More than 10000 MΩ (printed 'More than 10000MΩ') |  |  | Room temperature, after 1000 cycles Applies to: parts GCM32D5C3A682GX01. | DS p.3, Specifications and Test Methods, No. 4 Temperature Cycling, I.R. (Room Temp.) |  |
| Capacitance change, resistance to soldering heat | dC | -5 |  | 5 | % | Solder bath method, Sn-3.0Ag-0.5Cu, 260 +/-5 degC, 10 +/-1 s; after 24 h at room temperature Applies to: parts GCM32D5C3A682GX01. | DS p.4, Specifications and Test Methods, No. 14 Resistance to Soldering Heat, Capacitance Change |  |
| Capacitance change, moisture resistance | dC | -2 |  | 2 | % | +25 degC to +65 degC, 80 to 98 %RH, 10 cycles of the 24 h profile Applies to: parts GCM32D5C3A682GX01. | DS p.3, Specifications and Test Methods, No. 6 Moisture Resistance, Capacitance Change |  |
| Q, moisture resistance | Q | 350 |  |  |  | +25 degC to +65 degC, 80 to 98 %RH, 10 cycles of the 24 h profile Applies to: parts GCM32D5C3A682GX01. | DS p.3, Specifications and Test Methods, No. 6 Moisture Resistance, Q or D.F. |  |
| Insulation resistance, moisture resistance | IR |  | More than 10000 MΩ (printed 'More than 10000MΩ') |  |  | Room temperature, after the moisture test Applies to: parts GCM32D5C3A682GX01. | DS p.3, Specifications and Test Methods, No. 6 Moisture Resistance, I.R. (Room Temp.) |  |
| Capacitance change, humidity bias | dC | -3 |  | 3 | % | 85 degC, 80 to 85 %RH, 1000 h; test voltage: rated voltage and 1.3 +0.2/-0 V DC (6.8 kohm series, as printed) Applies to: parts GCM32D5C3A682GX01. | DS p.4, Specifications and Test Methods, No. 7 Humidity Bias, Capacitance Change |  |
| Q, humidity bias | Q | 200 |  |  |  | 85 degC, 80 to 85 %RH, 1000 h Applies to: parts GCM32D5C3A682GX01. | DS p.4, Specifications and Test Methods, No. 7 Humidity Bias, Q or D.F. |  |
| Insulation resistance, humidity bias | IR |  | More than 1000 MΩ (printed 'More than 1000MΩ') |  |  | Room temperature, after the humidity bias test Applies to: parts GCM32D5C3A682GX01. | DS p.4, Specifications and Test Methods, No. 7 Humidity Bias, I.R. (Room Temp.) |  |
| Capacitance change, high-temperature operating life | dC | -3 |  | 3 | % | Max operating temp +/-3 degC (125 degC), 1000 h, 100 % of rated voltage Applies to: parts GCM32D5C3A682GX01. | DS p.4, Specifications and Test Methods, No. 8 High Temperature Operating Life, Capacitance Change |  |
| Q, high-temperature operating life | Q | 350 |  |  |  | Max operating temp +/-3 degC, 1000 h, 100 % of rated voltage Applies to: parts GCM32D5C3A682GX01. | DS p.4, Specifications and Test Methods, No. 8 High Temperature Operating Life, Q or D.F. |  |
| Insulation resistance, high-temperature operating life | IR |  | More than 1000 MΩ (printed 'More than 1000MΩ') |  |  | Room temperature, after the high-temperature operating life test Applies to: parts GCM32D5C3A682GX01. | DS p.4, Specifications and Test Methods, No. 8 High Temperature Operating Life, I.R. (Room Temp.) |  |
| Capacitance change, board flex | dC | -5 |  | 5 | % | Flexure 3 mm, holding time 60 s, reflow solder on test substrate (1.6 mm glass epoxy); after test Applies to: parts GCM32D5C3A682GX01. | DS p.5, Specifications and Test Methods, No. 22 Board Flex, Capacitance Change |  |
| Voltage proof |  |  | No defects or abnormalities at 120 % of the rated voltage, applied 1 s to 5 s |  |  | Test voltage 120 % of the rated voltage; charge/discharge current 50 mA max Applies to: parts GCM32D5C3A682GX01. | DS p.5, Specifications and Test Methods, No. 21 Voltage proof |  |
| Capacitance | C |  | 12000 |  | pF | 25 degC, 1.0 +/-0.1 kHz, 1.0 +/-0.2 Vrms (DS p.5, No. 17) Applies to: parts GCM32D5C2J123FX01. | DS p.2 (GCM32D5C2J123FX01-00B-EN.pdf), Rated Value, Capacitance (12000pF) |  |
| Capacitance tolerance |  | -1 |  | 1 | % | Applies to: parts GCM32D5C2J123FX01. Note: Printed +/-1 % as a limit: min -1, max 1 (SPEC +/-X rule). The catalog tolerance of this value (catalog.csv) is the export's own printed value. | DS p.2 (GCM32D5C2J123FX01-00B-EN.pdf), Rated Value, Capacitance Tolerance (+/-1 %) |  |
| Q or dissipation factor (Q), initial | Q | 1000 |  |  |  | 25 degC, 1.0 +/-0.1 kHz, 1.0 +/-0.2 Vrms Applies to: parts GCM32D5C2J123FX01. Note: C0G is specified as Q (not DF): stored as a minimum, as printed. | DS p.5 (GCM32D5C2J123FX01-00B-EN.pdf), Specifications and Test Methods, No. 18 Q or Dissipation Factor (DF): Q>=1000 |  |
| Insulation resistance (IR), 25 degC | IR |  | More than 1000 MΩ·µF (printed 'More than 1000MΩ·µF') |  |  | 25 degC, DC 500 V +/-50 V, charging time 1 min, charge/discharge current 50 mA max Applies to: parts GCM32D5C2J123FX01. | DS p.5 (GCM32D5C2J123FX01-00B-EN.pdf), Specifications and Test Methods, No. 19 Insulation Resistance (IR), Room Temperature |  |
| Insulation resistance (IR), 125 degC | IR |  | More than 10 MΩ·µF (printed 'More than 10MΩ·µF') |  |  | 125 degC, DC 500 V +/-50 V, charging time 1 min, charge/discharge current 50 mA max Applies to: parts GCM32D5C2J123FX01. | DS p.5 (GCM32D5C2J123FX01-00B-EN.pdf), Specifications and Test Methods, No. 20 Insulation Resistance (IR), High Temperature |  |
| Capacitance change, high-temperature exposure (storage) | dC | -2 |  | 2 | % | 150 degC, 1000 h, no bias; after 24 h at room temperature Applies to: parts GCM32D5C2J123FX01. | DS p.3 (GCM32D5C2J123FX01-00B-EN.pdf), Specifications and Test Methods, No. 3 High Temperature Exposure (Storage), Capacitance Change |  |
| Q, high-temperature exposure | Q |  | Within the specified initial value |  |  | 150 degC, 1000 h, no bias; after 24 h at room temperature Applies to: parts GCM32D5C2J123FX01. | DS p.3 (GCM32D5C2J123FX01-00B-EN.pdf), Specifications and Test Methods, No. 3 High Temperature Exposure (Storage), Q or D.F. |  |
| Insulation resistance, high-temperature exposure | IR |  | More than 100 MΩ·µF (printed 'More than 100MΩ·µF') |  |  | Room temperature, after 150 degC, 1000 h exposure Applies to: parts GCM32D5C2J123FX01. | DS p.3 (GCM32D5C2J123FX01-00B-EN.pdf), Specifications and Test Methods, No. 3 High Temperature Exposure (Storage), I.R. (Room Temp.) |  |
| Capacitance change, temperature cycling | dC | -2 |  | 2 | % | 1000 cycles, min operating temp to max operating temp (15 min dwell each); after room-temperature sit Applies to: parts GCM32D5C2J123FX01. | DS p.3 (GCM32D5C2J123FX01-00B-EN.pdf), Specifications and Test Methods, No. 4 Temperature Cycling, Capacitance Change |  |
| Q, temperature cycling | Q |  | Within the specified initial value |  |  | 1000 cycles; after room-temperature sit Applies to: parts GCM32D5C2J123FX01. | DS p.3 (GCM32D5C2J123FX01-00B-EN.pdf), Specifications and Test Methods, No. 4 Temperature Cycling, Q or D.F. |  |
| Insulation resistance, temperature cycling | IR |  | More than 100 MΩ·µF (printed 'More than 100MΩ·µF') |  |  | Room temperature, after 1000 cycles Applies to: parts GCM32D5C2J123FX01. | DS p.3 (GCM32D5C2J123FX01-00B-EN.pdf), Specifications and Test Methods, No. 4 Temperature Cycling, I.R. (Room Temp.) |  |
| Capacitance change, resistance to soldering heat | dC | -5 |  | 5 | % | Solder bath method, Sn-3.0Ag-0.5Cu, 260 +/-5 degC, 10 +/-1 s; after 24 h at room temperature Applies to: parts GCM32D5C2J123FX01. | DS p.4 (GCM32D5C2J123FX01-00B-EN.pdf), Specifications and Test Methods, No. 14 Resistance to Soldering Heat, Capacitance Change |  |
| Capacitance change, moisture resistance | dC | -2 |  | 2 | % | +25 degC to +65 degC, 80 to 98 %RH, 10 cycles of the 24 h profile Applies to: parts GCM32D5C2J123FX01. | DS p.3 (GCM32D5C2J123FX01-00B-EN.pdf), Specifications and Test Methods, No. 6 Moisture Resistance, Capacitance Change |  |
| Q, moisture resistance | Q | 350 |  |  |  | +25 degC to +65 degC, 80 to 98 %RH, 10 cycles of the 24 h profile Applies to: parts GCM32D5C2J123FX01. | DS p.3 (GCM32D5C2J123FX01-00B-EN.pdf), Specifications and Test Methods, No. 6 Moisture Resistance, Q or D.F. |  |
| Insulation resistance, moisture resistance | IR |  | More than 100 MΩ·µF (printed 'More than 100MΩ·µF') |  |  | Room temperature, after the moisture test Applies to: parts GCM32D5C2J123FX01. | DS p.3 (GCM32D5C2J123FX01-00B-EN.pdf), Specifications and Test Methods, No. 6 Moisture Resistance, I.R. (Room Temp.) |  |
| Capacitance change, humidity bias | dC | -3 |  | 3 | % | 85 degC, 80 to 85 %RH, 1000 h; test voltage: rated voltage and 1.3 +0.2/-0 V DC (6.8 kohm series, as printed) Applies to: parts GCM32D5C2J123FX01. | DS p.4 (GCM32D5C2J123FX01-00B-EN.pdf), Specifications and Test Methods, No. 7 Humidity Bias, Capacitance Change |  |
| Q, humidity bias | Q | 200 |  |  |  | 85 degC, 80 to 85 %RH, 1000 h Applies to: parts GCM32D5C2J123FX01. | DS p.4 (GCM32D5C2J123FX01-00B-EN.pdf), Specifications and Test Methods, No. 7 Humidity Bias, Q or D.F. |  |
| Insulation resistance, humidity bias | IR |  | More than 1000 MΩ (printed 'More than 1000MΩ') |  |  | Room temperature, after the humidity bias test Applies to: parts GCM32D5C2J123FX01. | DS p.4 (GCM32D5C2J123FX01-00B-EN.pdf), Specifications and Test Methods, No. 7 Humidity Bias, I.R. (Room Temp.) |  |
| Capacitance change, high-temperature operating life | dC | -3 |  | 3 | % | Max operating temp +/-3 degC (125 degC), 1000 h, 120 % of rated voltage Applies to: parts GCM32D5C2J123FX01. | DS p.4 (GCM32D5C2J123FX01-00B-EN.pdf), Specifications and Test Methods, No. 8 High Temperature Operating Life, Capacitance Change |  |
| Q, high-temperature operating life | Q | 350 |  |  |  | Max operating temp +/-3 degC, 1000 h, 120 % of rated voltage Applies to: parts GCM32D5C2J123FX01. | DS p.4 (GCM32D5C2J123FX01-00B-EN.pdf), Specifications and Test Methods, No. 8 High Temperature Operating Life, Q or D.F. |  |
| Insulation resistance, high-temperature operating life | IR |  | More than 1000 MΩ (printed 'More than 1000MΩ') |  |  | Room temperature, after the high-temperature operating life test Applies to: parts GCM32D5C2J123FX01. | DS p.4 (GCM32D5C2J123FX01-00B-EN.pdf), Specifications and Test Methods, No. 8 High Temperature Operating Life, I.R. (Room Temp.) |  |
| Capacitance change, board flex | dC | -5 |  | 5 | % | Flexure 3 mm, holding time 60 s, reflow solder on test substrate (1.6 mm glass epoxy); after test Applies to: parts GCM32D5C2J123FX01. | DS p.5 (GCM32D5C2J123FX01-00B-EN.pdf), Specifications and Test Methods, No. 22 Board Flex, Capacitance Change |  |
| Voltage proof |  |  | No defects or abnormalities at 150 % of the rated voltage, applied 1 s to 5 s |  |  | Test voltage 150 % of the rated voltage; charge/discharge current 50 mA max Applies to: parts GCM32D5C2J123FX01. | DS p.5 (GCM32D5C2J123FX01-00B-EN.pdf), Specifications and Test Methods, No. 21 Voltage proof |  |
| Temperature characteristic, C0G (EIA) | TC | -30 |  | 30 | ppm/degC | Ref. temp 25 degC; temp range printed as 25 to 125 degC; coefficient 0 +/-30 ppm/degC Applies to: dielectric C0G. Note: Public STD code C0G (EIA). A temperature coefficient, not a percent-change class. The DS prints the range 25 to 125 degC only: no coefficient is printed below 25 degC. The -55 to -10 degC capacitance drift is in the Table A rows (capdrift_*_c0g); the -10 to 25 degC segment has no printed number (open item). capacitance_worst_ppm requires dt and refuses values outside 0 to 100 degC (docs/SPEC.md, Capacitor series). | DS p.2 (GCM32D5C3A682GX01-00B-EN.pdf), Rated Value, Temp. coeff. or Cap. Change (0+/-30 ppm/degC), Temp. Range (25 to 125 degC) |  |
| Capacitance change at -55 degC vs 25 degC (Table A) | dC | -0.24 |  | 0.58 | % | Reference 25 degC, no bias; measured at -55 degC Applies to: dielectric C0G. Note: Printed Max 0.58, Min -0.24: stored as min -0.24, max 0.58 (printed columns). Covers only the -55 degC point. | DS p.7, Table A Capacitance Change between at Reference Temp. and at each Temp. (%), 5C, -55 degC |  |
| Capacitance change at -30 degC vs 25 degC (Table A) | dC | -0.17 |  | 0.4 | % | Reference 25 degC, no bias; measured at -30 degC Applies to: dielectric C0G. Note: Printed Max 0.4, Min -0.17: stored as min -0.17, max 0.4 (printed columns). Covers only the -30 degC point. | DS p.7, Table A Capacitance Change between at Reference Temp. and at each Temp. (%), 5C, -30 degC |  |
| Capacitance change at -10 degC vs 25 degC (Table A) | dC | -0.11 |  | 0.25 | % | Reference 25 degC, no bias; measured at -10 degC Applies to: dielectric C0G. Note: Printed Max 0.25, Min -0.11: stored as min -0.11, max 0.25 (printed columns). Covers only the -10 degC point. | DS p.7, Table A Capacitance Change between at Reference Temp. and at each Temp. (%), 5C, -10 degC |  |
| Capacitance drift limit (temperature characteristics test) | dC |  | Within +/-0.2 % or +/-0.05 pF, whichever is larger |  | % | Temperature characteristics test, 1.0 Vrms max; capacitance at steps 1, 3, 5 compared with step 3 Applies to: dielectric C0G. Note: Text row: the limit is the larger of a percentage and an absolute value. Not stored as numbers. | DS p.6, Specifications and Test Methods, No. 25 Temperature Characteristics, Capacitance Drift |  |
| Temperature characteristic, R7 (X7R) | TC | -15 |  | 15 | % | Ref. temp 25 degC; temp range -55 to 125 degC; capacitance change over temperature Applies to: dielectric X7R. Note: Public STD code X7R (EIA). Capacitance change over temperature, not a DC-bias or aging limit. Read from the 1210 X7R sheet (thickness code E); used for every X7R catalog row of this directory (open item: no X7R sheet for thickness code D). | DS p.2 (GCM32ER71C226ME19-01A-EN.pdf), Rated Value, Temp. coeff. or Cap. Change (-15 to 15 %) |  |

## Parameters: mechanical

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Land pattern dimension a (reflow) | a | 2.0 |  | 2.4 | mm | Reflow soldering, chip 3.2x2.5, code 32 Note: Letter label only in the DS figure; neutral name. Inferred meaning: gap between lands (not printed). | DS p.28 (GCM32ER71C226ME19-01A-EN.pdf), 2. Land Dimensions, Table 2 Reflow Soldering Method, 3.2x2.5, a |  |
| Land pattern dimension b (reflow) | b | 1.0 |  | 1.2 | mm | Reflow soldering, chip 3.2x2.5, code 32 Note: Letter label only in the DS figure; neutral name. Inferred meaning: land length, outer side (not printed). | DS p.28 (GCM32ER71C226ME19-01A-EN.pdf), 2. Land Dimensions, Table 2 Reflow Soldering Method, 3.2x2.5, b |  |
| Land pattern dimension c (reflow) | c | 1.8 |  | 2.3 | mm | Reflow soldering, chip 3.2x2.5, code 32 Note: Letter label only in the DS figure; neutral name. Inferred meaning: land width across the chip (not printed). | DS p.28 (GCM32ER71C226ME19-01A-EN.pdf), 2. Land Dimensions, Table 2 Reflow Soldering Method, 3.2x2.5, c |  |
| Length (L) | L | 3.05 | 3.2 | 3.35 | mm | Applies to: parts GCM32D5C3A682GX01. Note: min and max are the printed nominal 3.2 -/+ 0.15 (arithmetic); the DS prints 3.2+/-0.15. | DS p.2, Type & Dimension, L (3.2+/-0.15) |  |
| Width (W) | W | 2.35 | 2.5 | 2.65 | mm | Applies to: parts GCM32D5C3A682GX01. Note: min and max are the printed nominal 2.5 -/+ 0.15 (arithmetic); the DS prints 2.5+/-0.15. | DS p.2, Type & Dimension, W (2.5+/-0.15) |  |
| Thickness (T) | T | 1.75 | 2.0 | 2.0 | mm | Applies to: parts GCM32D5C3A682GX01. Note: Printed 2.0 +0/-0.25: min 1.75, typ 2.0, max 2.0. Catalog thickness column: 2mm +0mm/-0.25mm (export, agrees). | DS p.2, Type & Dimension, T (2.0+0/-0.25) |  |
| Terminal width (e) | e | 0.3 |  |  | mm | Applies to: parts GCM32D5C3A682GX01. Note: Printed as a minimum only; no max stored. | DS p.2, Type & Dimension, e (0.3 min.) |  |
| Gap between terminals (g) | g | 1.5 |  |  | mm | Applies to: parts GCM32D5C3A682GX01. Note: Printed as a minimum only; no max stored. | DS p.2, Type & Dimension, g (1.5 min.) |  |
| Beam load test, destruction value |  |  | More than 54.5 N (destruction value) |  |  | Speed 2.5 mm/s; placement diagram Applies to: parts GCM32D5C3A682GX01. | DS p.5, Specifications and Test Methods, No. 24 Beam Load Test |  |
| Solderability: terminations soldered evenly and continuously |  | 95 |  |  | % | Specifications and Test Methods No.16 (a) test conditions Applies to: parts GCM32D5C3A682GX01. Note: Assembly acceptance criterion, not a circuit limit. | DS p.5, Specifications and Test Methods, No.16 Solderability (a) |  |
| Length (L) | L | 3.05 | 3.2 | 3.35 | mm | Applies to: parts GCM32D5C2J123FX01. Note: min and max are the printed nominal 3.2 -/+ 0.15 (arithmetic). | DS p.2 (GCM32D5C2J123FX01-00B-EN.pdf), Type & Dimension, L (3.2+/-0.15) |  |
| Width (W) | W | 2.35 | 2.5 | 2.65 | mm | Applies to: parts GCM32D5C2J123FX01. Note: min and max are the printed nominal 2.5 -/+ 0.15 (arithmetic). | DS p.2 (GCM32D5C2J123FX01-00B-EN.pdf), Type & Dimension, W (2.5+/-0.15) |  |
| Thickness (T) | T | 1.75 | 2.0 | 2.0 | mm | Applies to: parts GCM32D5C2J123FX01. Note: Printed 2.0 +0/-0.25: min 1.75, typ 2.0, max 2.0. | DS p.2 (GCM32D5C2J123FX01-00B-EN.pdf), Type & Dimension, T (2.0+0/-0.25) |  |
| Terminal width (e) | e | 0.3 |  |  | mm | Applies to: parts GCM32D5C2J123FX01. Note: Printed as a minimum only; no max stored. | DS p.2 (GCM32D5C2J123FX01-00B-EN.pdf), Type & Dimension, e (0.3 min.) |  |
| Gap between terminals (g) | g | 1.5 |  |  | mm | Applies to: parts GCM32D5C2J123FX01. Note: Printed as a minimum only; no max stored. | DS p.2 (GCM32D5C2J123FX01-00B-EN.pdf), Type & Dimension, g (1.5 min.) |  |
| Beam load test, destruction value |  |  | More than 54.5 N (destruction value) |  |  | Speed 2.5 mm/s; placement diagram Applies to: parts GCM32D5C2J123FX01. | DS p.5 (GCM32D5C2J123FX01-00B-EN.pdf), Specifications and Test Methods, No. 24 Beam Load Test |  |
| Solderability: terminations soldered evenly and continuously |  | 95 |  |  | % | Specifications and Test Methods No.16 (a) test conditions Applies to: parts GCM32D5C2J123FX01. Note: Assembly acceptance criterion, not a circuit limit. | DS p.5 (GCM32D5C2J123FX01-00B-EN.pdf), Specifications and Test Methods, No.16 Solderability (a) |  |

## Limits of this data

Rows by scope: 25C 6, full 1, na 62, partial 4 (25C rows hold only at 25 degC). Curve (graph) rows: 0. Text rows: 23.

## Zener checks

Generated wrapper: `GCM32D.zen` (`python3 -m lib.zen`). abs_max and rec_op rows are errors (abs_max x derate); 25C and partial rows are waivable warnings; a checked net with no voltage is UNVERIFIED.

| Param | Name | Checked against | Not checked / reason |
|---|---|---|---|
| rated_v_ds_682_c0g | Rated voltage (DC) | UNCHECKED | the generated rated_voltage check applies the catalog rated voltage of the selected part; this per-part row duplicates it (owner: module) |
| rated_v_ds_123_c0g | Rated voltage (DC) | UNCHECKED | the generated rated_voltage check applies the catalog rated voltage of the selected part; this per-part row duplicates it (owner: module) |
| op_temp_c0g | Operating temperature range | board ambient |  |
| op_temp_x7r | Operating temperature range | board ambient |  |

## Equations

### `capacitance_worst_pct`

```
Not a DS equation: C = C0 * (1 + tol) * (1 + tc).  For percent-change dielectrics (X7R): tc is the capacitance
change over the whole range as a FRACTION (DS p.2 of the 1210 X7R sheet, Rated Value, Temp. coeff. or Cap. Change,
-15 to 15 % over -55 to 125 degC, ref 25 degC), so with the row's min/max the corners give the full-range worst case.
For C0G use capacitance_worst_ppm: passing its 1/degC coefficient here would treat 3e-5 as a fraction and badly
understate the spread, so |tc| below 1e-3 (other than 0) raises ValueError.
EXCLUDES DC-bias and aging capacitance loss, which the reference sheet does not quantify (DS p.14 section 5 figure;
DS p.15 section 6 text). For X7R these can dominate. A worst-case stack of printed rows, not a guaranteed
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
| capacitance_worst_ppm(c0=6.8e-09, tol=-0.02, tc=-3e-05, dt=100) | 6.64401e-09 | 6.64401e-09 | 1e-12 | pass | DS p.2, Rated Value |
| capacitance_worst_pct(c0=2.2e-05, tol=-0.2, tc=-0.15) | 1.496e-05 | 1.496e-05 | 1e-12 | pass | DS p.2, Rated Value (X7R 1210 sheet) |
