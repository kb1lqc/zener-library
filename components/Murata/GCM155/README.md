<!-- GENERATED - do not edit. Run: python3 -m lib.readme -->

# GCM155

## Datasheet review

[![Human page-image review: 0/70 human](https://img.shields.io/badge/human%20review-0%2F70%20human-lightgrey)](../../../docs/spec/datasheet-review.md)

Human page-image review: 0/70; cross-model audits: 0; manufacturer-export stamps: 0; legacy/unclassified: 0. Text checks are not verification. `lib.check` validates stamp format, not that review occurred.

## Part

- **manufacturer**: Murata
- **description**: Chip multilayer ceramic capacitors, X7R (R7) and C0G (5C), 1005M (0402), AEC-Q200 (GCM series)
- **category**: capacitor_mlcc
- **package**: 1005M (0402)
- **datasheet_url**: 
- **datasheet_file**: docs/datasheets/GCM155R71H104KE02-01A-EN.pdf
- **datasheet_rev**: 01A
- **datasheet_date**: 2026-04
- **kicad_symbol**: GCM155.kicad_sym
- **kicad_footprint**: GCM155.kicad_mod
- **step**: GCM155.step

## Series

- **Catalog**: `catalog.csv`, 697 orderable values, one row per value with its cite (a manufacturer export, not a datasheet table)
- **MPN rule**: catalog value + package letter; default `D`, alternates `W`, `J`, `V` (same part, other packaging); example: `GCM1555C1HR56BA16` -> `GCM1555C1HR56BA16D`
- **Selection**: `sel = part.select(capacitance, rated_voltage, dielectric, tolerance=None)` returns the MPN, `capacitance` / `rated_voltage` Params and `sel.part`, a Part holding the rows that apply (dielectric and part restrictions applied, plus `capacitance`, `tolerance`, `rated_v` and `tc`); an unlisted or ambiguous request raises ValueError
- **Zener wrapper**: configs `value`, `rated_v`, `dielectric`, optional `tolerance`; checks `part_orderable`, `rated_voltage` (|V(P1) - V(P2)| <= derate x rated voltage) and `ambient_range` (per dielectric)
- **Worst-case capacitance**: X7R (percent change): `wca(sel.part.calc.capacitance_worst_pct, **sel.part.inputs('capacitance_worst_pct'))`; C0G (ppm/degC): `wca(sel.part.calc.capacitance_worst_ppm, dt=Param(min=0, max=100), **sel.part.inputs('capacitance_worst_ppm'))` (dt required, 0 to 100 degC; below 25 degC use the printed drift rows). Both EXCLUDE DC-bias and aging loss

| Dielectric | Parts | Capacitance | Rated voltages | Tolerances | TC row |
|---|---|---|---|---|---|
| C0G | 556 | 100 fF to 1 nF | 50 V, 100 V | ±0.05pF, ±0.1pF, ±0.25pF, ±0.5pF, ±1%, ±2%, ±2.5%, ±20%, ±5% | `tc_c0g` |
| X7R | 141 | 220 pF to 1 uF | 4 V, 6.3 V, 10 V, 16 V, 25 V, 50 V, 100 V | ±10%, ±20% | `tc_x7r` |

## Pins

| Pin | Name | Type | Function | Cite |
|---|---|---|---|---|
| 1 | 1 | passive | Capacitor terminal (non-polarized) | DS p.2, Type & Dimension, image:Dimension |
| 2 | 2 | passive | Capacitor terminal (non-polarized) | DS p.2, Type & Dimension, image:Dimension |

## Parameters: rec_op

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Rated voltage (DC) |  | -50 (rel. 2) |  | 50 (rel. 2) | V | Voltage between pin 1 and pin 2 (non-polarized; either polarity) Applies to: parts GCM155R71H104KE02. Note: DS prints DC 50V with no MIN/MAX label. Stored symmetric (min -50, max 50) because the part is non-polarized: \|V(1)-V(2)\| <= 50 V. The wrapper checks the catalog rating (same value for this part), not this row. | DS p.2, Rated Value, Rated Voltage (DC 50V) |  |
| Operating temperature range |  | -55 |  | 125 | degC | Applies to: dielectric X7R. Note: Read from the reference sheet of the one part this directory has. lib.catalog refuses an export row whose Operating Temperature is not -55 to 125 degC, so every X7R catalog row uses it. | DS p.2, Rated Value, Operating Temp. Range (-55 to 125 degC) |  |
| Self-heating of the capacitor body (AC or pulse load) |  |  |  | 20 | degC | Measured at 25 degC ambient; rated voltage below 100 VDC Applies to: parts GCM155R71H104KE02. | DS p.14, Rating 4. Type of Applied Voltage and Self-heating Temperature |  |
| AC or pulse voltage: peak-to-peak (and zero-to-peak with DC) within the rated DC voltage |  |  | Vp-p <= rated DC voltage; AC superimposed on DC: zero-to-peak <= rated DC voltage |  |  | AC or pulse voltage applied Applies to: parts GCM155R71H104KE02. | DS p.13, Rating 3. Applied Voltage, 1-1 (1) |  |
| Operating temperature range |  | -55 |  | 125 | degC | Applies to: dielectric C0G. Note: Read from the C0G reference sheet of GCM1555C1H101FA16. lib.catalog refuses an export row whose Operating Temperature is not -55 to 125 degC, so every C0G catalog row uses it. | DS p.2 (GCM1555C1H101FA16-01A-EN.pdf), Rated Value, Operating Temp. Range (-55 to 125 degC) |  |
| Rated voltage (DC) |  | -50 (rel. 2) |  | 50 (rel. 2) | V | Voltage between pin 1 and pin 2 (non-polarized; either polarity) Applies to: parts GCM1555C1H101FA16. Note: DS prints DC 50V with no MIN/MAX label. Stored symmetric (min -50, max 50) because the part is non-polarized, as for the X7R row. | DS p.2 (GCM1555C1H101FA16-01A-EN.pdf), Rated Value, Rated Voltage (DC 50V) |  |

## Parameters: electrical

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Capacitance | C |  | 0.1 |  | uF | 25 degC, 1.0 +/-0.1 kHz, 1.0 +/-0.2 Vrms (DS p.6, No. 17) Applies to: parts GCM155R71H104KE02. | DS p.2, Rated Value, Capacitance (0.1uF) |  |
| Capacitance tolerance |  | -10 |  | 10 | % | Applies to: parts GCM155R71H104KE02. Note: Printed +/-10 % as a limit: min -10, max 10 (SPEC +/-X rule). | DS p.2, Rated Value, Capacitance Tolerance (+/-10 %) |  |
| Dissipation factor (DF), initial | DF |  |  | 0.1 |  | 25 degC, 1.0 +/-0.1 kHz, 1.0 +/-0.2 Vrms Applies to: parts GCM155R71H104KE02. | DS p.6, Specifications and Test Methods, No. 18 Q or Dissipation Factor (DF) |  |
| Insulation resistance (IR), 25 degC | IR |  | More than 50 ohm*F (printed 'More than 50 Ohm.F'), IR x C |  |  | 25 degC, rated voltage, charging time 1 min, charge/discharge current 50 mA max Applies to: parts GCM155R71H104KE02. | DS p.6, Specifications and Test Methods, No. 19 Insulation Resistance (IR), Room Temperature |  |
| Insulation resistance (IR), 125 degC | IR |  | More than 5 ohm*F (printed 'More than 5 Ohm.F'), IR x C |  |  | 125 degC, rated voltage, charging time 1 min, charge/discharge current 50 mA max Applies to: parts GCM155R71H104KE02. | DS p.6, Specifications and Test Methods, No. 20 Insulation Resistance (IR), High Temperature |  |
| Capacitance change, board flex | dC | -10 |  | 10 | % | Board flex: flexure 2 mm, holding time 60 s, reflow solder on test substrate; after test Applies to: parts GCM155R71H104KE02. | DS p.6, Specifications and Test Methods, No. 22 Board Flex, Capacitance Change |  |
| Capacitance change, high-temperature exposure (storage) | dC | -10 |  | 10 | % | 150 degC, 1000 h, no bias; after 24 h at room temperature Applies to: parts GCM155R71H104KE02. | DS p.3, Specifications and Test Methods, No. 3 High Temperature Exposure (Storage), Capacitance Change |  |
| Dissipation factor, high-temperature exposure | DF |  |  | 0.2 |  | 150 degC, 1000 h, no bias; after 24 h at room temperature Applies to: parts GCM155R71H104KE02. | DS p.3, Specifications and Test Methods, No. 3 High Temperature Exposure (Storage), Q or D.F. |  |
| Insulation resistance, high-temperature exposure | IR |  | More than 50 ohm*F (printed 'More than 50 Ohm.F'), IR x C |  |  | Room temperature, after 150 degC, 1000 h exposure Applies to: parts GCM155R71H104KE02. | DS p.3, Specifications and Test Methods, No. 3 High Temperature Exposure (Storage), I.R. (Room Temp.) |  |
| Capacitance change, temperature cycling | dC | -7.5 |  | 7.5 | % | 1000 cycles, min operating temp to max operating temp (30 min dwell each); after room-temperature sit Applies to: parts GCM155R71H104KE02. Note: DS prints Q/DF and IR as 'within the specified initial value' (no number), so only the capacitance limit is stored. | DS p.3, Specifications and Test Methods, No. 4 Temperature Cycling, Capacitance Change |  |
| Capacitance change, moisture resistance | dC | -10 |  | 10 | % | +25 degC to +65 degC, 80 to 98 %RH, 10 cycles of the 24 h profile Applies to: parts GCM155R71H104KE02. | DS p.4, Specifications and Test Methods, No. 6 Moisture Resistance, Capacitance Change |  |
| Dissipation factor, moisture resistance | DF |  |  | 0.2 |  | +25 degC to +65 degC, 80 to 98 %RH, 10 cycles of the 24 h profile Applies to: parts GCM155R71H104KE02. | DS p.4, Specifications and Test Methods, No. 6 Moisture Resistance, Q or D.F. |  |
| Insulation resistance, moisture resistance | IR |  | More than 25 ohm*F (printed 'More than 25 Ohm.F'), IR x C |  |  | Room temperature, after the moisture test Applies to: parts GCM155R71H104KE02. | DS p.4, Specifications and Test Methods, No. 6 Moisture Resistance, I.R. (Room Temp.) |  |
| Capacitance change, humidity bias | dC | -12.5 |  | 12.5 | % | 85 degC, 80 to 85 %RH, 1000 h; test voltage: rated voltage and 1.3 +0.2/-0 V DC (6.8 kohm series, as printed) Applies to: parts GCM155R71H104KE02. | DS p.4, Specifications and Test Methods, No. 7 Humidity Bias, Capacitance Change |  |
| Dissipation factor, humidity bias | DF |  |  | 0.2 |  | 85 degC, 80 to 85 %RH, 1000 h Applies to: parts GCM155R71H104KE02. | DS p.4, Specifications and Test Methods, No. 7 Humidity Bias, Q or D.F. |  |
| Insulation resistance, humidity bias | IR |  | More than 12.5 ohm*F (printed 'More than 12.5 Ohm.F'), IR x C |  |  | Room temperature, after the humidity bias test Applies to: parts GCM155R71H104KE02. | DS p.4, Specifications and Test Methods, No. 7 Humidity Bias, I.R. (Room Temp.) |  |
| Capacitance change, high-temperature operating life | dC | -12.5 |  | 12.5 | % | Max operating temp +/-3 degC (125 degC), 1000 h, 150 % of rated voltage Applies to: parts GCM155R71H104KE02. | DS p.4, Specifications and Test Methods, No. 8 High Temperature Operating Life, Capacitance Change |  |
| Dissipation factor, high-temperature operating life | DF |  |  | 0.2 |  | Max operating temp +/-3 degC, 1000 h, 150 % of rated voltage Applies to: parts GCM155R71H104KE02. | DS p.4, Specifications and Test Methods, No. 8 High Temperature Operating Life, Q or D.F. |  |
| Insulation resistance, high-temperature operating life | IR |  | More than 25 ohm*F (printed 'More than 25 Ohm.F'), IR x C |  |  | Room temperature, after the high-temperature operating life test Applies to: parts GCM155R71H104KE02. | DS p.4, Specifications and Test Methods, No. 8 High Temperature Operating Life, I.R. (Room Temp.) |  |
| Temperature characteristic, R7 (X7R) | TC | -15 |  | 15 | % | Ref. temp 25 degC; temp range -55 to 125 degC; capacitance change over temperature Applies to: dielectric X7R. Note: Public STD code X7R (EIA). Capacitance change over temperature, not a DC-bias or aging limit (see the open items above). Read from the reference sheet of the one part this directory has; used for every X7R catalog row because -15 to 15 % over -55 to 125 degC is the X7R class limit the sheet prints for code R7 (open item: confirm for each other X7R part). | DS p.2, Rated Value, Temp. coeff. or Cap. Change (-15 to 15 %) |  |
| Capacitance change with DC bias |  |  | Not specified: the sheet shows only an example curve |  |  | DC voltage applied Applies to: parts GCM155R71H104KE02. Note: X7R loses capacitance under DC bias; the DS example curve (sample R(R1), 0.1 uF, 50 VDC: a different temperature-characteristic code from this R7 part) shows a large loss approaching rated voltage; it is an example, not a rating for this part. capacitance_worst_pct/_ppm exclude it: do not use capacitance_worst_pct as an in-circuit minimum. The DS also requires the AC/pulse zero-to-peak voltage to stay within the rated DC voltage; the Zener check is DC steady state only. | DS p.14, Rating 5. DC Voltage and AC Voltage Characteristic (example figure) |  |
| Temperature characteristic, C0G (EIA) | TC | -30 |  | 30 | ppm/degC | Ref. temp 25 degC; temp range printed as 25 to 125 degC; coefficient 0 +/-30 ppm/degC Applies to: dielectric C0G. Note: Public STD code C0G (EIA). A temperature coefficient, not a percent-change class. The DS prints the range 25 to 125 degC only: no coefficient is printed below 25 degC. The -55 to -10 degC capacitance drift is in the Table A rows (capdrift_*_c0g); the -10 to 25 degC segment has no printed number (open item). capacitance_worst_ppm requires dt and refuses values outside 0 to 100 degC (docs/SPEC.md, Capacitor series). | DS p.2 (GCM1555C1H101FA16-01A-EN.pdf), Rated Value, Temp. coeff. or Cap. Change (0+/-30 ppm/degC), Temp. Range (25 to 125 degC) |  |
| Capacitance change at -55 degC vs 25 degC (Table A) | dC | -0.24 |  | 0.58 | % | Reference 25 degC, no bias; measured at -55 degC Applies to: dielectric C0G. Note: Printed Max 0.58, Min -0.24: stored as min -0.24, max 0.58 (printed columns). Covers only the -55 degC point. | DS p.7 (GCM1555C1H101FA16-01A-EN.pdf), Table A Capacitance Change between at Reference Temp. and at each Temp. (%), 5C, -55 degC |  |
| Capacitance change at -30 degC vs 25 degC (Table A) | dC | -0.17 |  | 0.4 | % | Reference 25 degC, no bias; measured at -30 degC Applies to: dielectric C0G. Note: Printed Max 0.4, Min -0.17: stored as min -0.17, max 0.4 (printed columns). Covers only the -30 degC point. | DS p.7 (GCM1555C1H101FA16-01A-EN.pdf), Table A Capacitance Change between at Reference Temp. and at each Temp. (%), 5C, -30 degC |  |
| Capacitance change at -10 degC vs 25 degC (Table A) | dC | -0.11 |  | 0.25 | % | Reference 25 degC, no bias; measured at -10 degC Applies to: dielectric C0G. Note: Printed Max 0.25, Min -0.11: stored as min -0.11, max 0.25 (printed columns). Covers only the -10 degC point. | DS p.7 (GCM1555C1H101FA16-01A-EN.pdf), Table A Capacitance Change between at Reference Temp. and at each Temp. (%), 5C, -10 degC |  |
| Capacitance drift limit (temperature characteristics test) | dC |  | Within +/-0.2 % or +/-0.05 pF, whichever is larger |  | % | Temperature characteristics test, 1.0 Vrms max; capacitance at steps 1, 3, 5 compared with step 3 Applies to: dielectric C0G. Note: Text row: the limit is the larger of a percentage and an absolute value. Not stored as numbers. | DS p.6 (GCM1555C1H101FA16-01A-EN.pdf), Specifications and Test Methods, No. 25 Temperature Characteristics, Capacitance Drift |  |
| Capacitance | C |  | 100 |  | pF | 25 degC, 1.0 +/-0.1 MHz, 0.5 to 5.0 Vrms (DS p.5, No. 17) Applies to: parts GCM1555C1H101FA16. | DS p.2 (GCM1555C1H101FA16-01A-EN.pdf), Rated Value, Capacitance (100pF) |  |
| Capacitance tolerance |  | -1 |  | 1 | % | Applies to: parts GCM1555C1H101FA16. Note: Printed +/-1 % as a limit: min -1, max 1 (SPEC +/-X rule). The catalog tolerance of this value (catalog.csv) is the export's own printed value. | DS p.2 (GCM1555C1H101FA16-01A-EN.pdf), Rated Value, Capacitance Tolerance (+/-1 %) |  |
| Q or dissipation factor (Q), initial | Q | 1000 |  |  |  | 25 degC, 1.0 +/-0.1 MHz, 0.5 to 5.0 Vrms Applies to: parts GCM1555C1H101FA16. Note: C0G is specified as Q (not DF): stored as a minimum, as printed. | DS p.5 (GCM1555C1H101FA16-01A-EN.pdf), Specifications and Test Methods, No. 18 Q or Dissipation Factor (DF): Q>=1000 |  |
| Insulation resistance (IR), 25 degC | IR |  | More than 100000 Mohm (printed 'More than 100000MΩ') |  |  | 25 degC, rated voltage, charging time 2 min, charge/discharge current 50 mA max Applies to: parts GCM1555C1H101FA16. | DS p.5 (GCM1555C1H101FA16-01A-EN.pdf), Specifications and Test Methods, No. 19 Insulation Resistance (IR), Room Temperature |  |
| Insulation resistance (IR), 125 degC | IR |  | More than 10000 Mohm (printed 'More than 10000MΩ') |  |  | 125 degC, rated voltage, charging time 2 min, charge/discharge current 50 mA max Applies to: parts GCM1555C1H101FA16. | DS p.5 (GCM1555C1H101FA16-01A-EN.pdf), Specifications and Test Methods, No. 20 Insulation Resistance (IR), High Temperature |  |
| Capacitance change, high-temperature exposure (storage) | dC | -2.5 |  | 2.5 | % | 150 degC, 1000 h, no bias; after 24 h at room temperature Applies to: parts GCM1555C1H101FA16. | DS p.3 (GCM1555C1H101FA16-01A-EN.pdf), Specifications and Test Methods, No. 3 High Temperature Exposure (Storage), Capacitance Change |  |
| Q, high-temperature exposure | Q | 1000 |  |  |  | 150 degC, 1000 h, no bias; after 24 h at room temperature Applies to: parts GCM1555C1H101FA16. | DS p.3 (GCM1555C1H101FA16-01A-EN.pdf), Specifications and Test Methods, No. 3 High Temperature Exposure (Storage), Q or D.F. |  |
| Insulation resistance, high-temperature exposure | IR |  | More than 10000 Mohm (printed 'More than 10000MΩ') |  |  | Room temperature, after 150 degC, 1000 h exposure Applies to: parts GCM1555C1H101FA16. | DS p.3 (GCM1555C1H101FA16-01A-EN.pdf), Specifications and Test Methods, No. 3 High Temperature Exposure (Storage), I.R. (Room Temp.) |  |
| Capacitance change, temperature cycling | dC | -2.5 |  | 2.5 | % | 1000 cycles, min operating temp to max operating temp (30 min dwell each); after room-temperature sit Applies to: parts GCM1555C1H101FA16. | DS p.3 (GCM1555C1H101FA16-01A-EN.pdf), Specifications and Test Methods, No. 4 Temperature Cycling, Capacitance Change |  |
| Q, temperature cycling | Q | 1000 |  |  |  | 1000 cycles; after room-temperature sit Applies to: parts GCM1555C1H101FA16. | DS p.3 (GCM1555C1H101FA16-01A-EN.pdf), Specifications and Test Methods, No. 4 Temperature Cycling, Q or D.F. |  |
| Insulation resistance, temperature cycling | IR |  | More than 10000 Mohm (printed 'More than 10000MΩ') |  |  | Room temperature, after 1000 cycles Applies to: parts GCM1555C1H101FA16. | DS p.3 (GCM1555C1H101FA16-01A-EN.pdf), Specifications and Test Methods, No. 4 Temperature Cycling, I.R. (Room Temp.) |  |
| Capacitance change, moisture resistance | dC | -3 |  | 3 | % | +25 degC to +65 degC, 80 to 98 %RH, 10 cycles of the 24 h profile Applies to: parts GCM1555C1H101FA16. | DS p.3 (GCM1555C1H101FA16-01A-EN.pdf), Specifications and Test Methods, No. 6 Moisture Resistance, Capacitance Change |  |
| Q, moisture resistance | Q | 350 |  |  |  | +25 degC to +65 degC, 80 to 98 %RH, 10 cycles of the 24 h profile Applies to: parts GCM1555C1H101FA16. | DS p.3 (GCM1555C1H101FA16-01A-EN.pdf), Specifications and Test Methods, No. 6 Moisture Resistance, Q or D.F. |  |
| Insulation resistance, moisture resistance | IR |  | More than 10000 Mohm (printed 'More than 10000MΩ') |  |  | Room temperature, after the moisture test Applies to: parts GCM1555C1H101FA16. | DS p.3 (GCM1555C1H101FA16-01A-EN.pdf), Specifications and Test Methods, No. 6 Moisture Resistance, I.R. (Room Temp.) |  |
| Capacitance change, humidity bias | dC | -3 |  | 3 | % | 85 degC, 80 to 85 %RH, 1000 h; test voltage: rated voltage and 1.3 +0.2/-0 V DC (6.8 kohm series, as printed) Applies to: parts GCM1555C1H101FA16. | DS p.4 (GCM1555C1H101FA16-01A-EN.pdf), Specifications and Test Methods, No. 7 Humidity Bias, Capacitance Change |  |
| Q, humidity bias | Q | 200 |  |  |  | 85 degC, 80 to 85 %RH, 1000 h Applies to: parts GCM1555C1H101FA16. | DS p.4 (GCM1555C1H101FA16-01A-EN.pdf), Specifications and Test Methods, No. 7 Humidity Bias, Q or D.F. |  |
| Insulation resistance, humidity bias | IR |  | More than 1000 Mohm (printed 'More than 1000MΩ') |  |  | Room temperature, after the humidity bias test Applies to: parts GCM1555C1H101FA16. | DS p.4 (GCM1555C1H101FA16-01A-EN.pdf), Specifications and Test Methods, No. 7 Humidity Bias, I.R. (Room Temp.) |  |
| Capacitance change, high-temperature operating life | dC | -3 |  | 3 | % | Max operating temp +/-3 degC (125 degC), 1000 h, 200 % of rated voltage Applies to: parts GCM1555C1H101FA16. | DS p.4 (GCM1555C1H101FA16-01A-EN.pdf), Specifications and Test Methods, No. 8 High Temperature Operating Life, Capacitance Change |  |
| Q, high-temperature operating life | Q | 350 |  |  |  | Max operating temp +/-3 degC, 1000 h, 200 % of rated voltage Applies to: parts GCM1555C1H101FA16. | DS p.4 (GCM1555C1H101FA16-01A-EN.pdf), Specifications and Test Methods, No. 8 High Temperature Operating Life, Q or D.F. |  |
| Insulation resistance, high-temperature operating life | IR |  | More than 1000 Mohm (printed 'More than 1000MΩ') |  |  | Room temperature, after the high-temperature operating life test Applies to: parts GCM1555C1H101FA16. | DS p.4 (GCM1555C1H101FA16-01A-EN.pdf), Specifications and Test Methods, No. 8 High Temperature Operating Life, I.R. (Room Temp.) |  |
| Capacitance change, board flex | dC | -5 |  | 5 | % | Flexure 3 mm, holding time 60 s, reflow solder on test substrate (0.8 mm glass epoxy); after test Applies to: parts GCM1555C1H101FA16. | DS p.5 (GCM1555C1H101FA16-01A-EN.pdf), Specifications and Test Methods, No. 22 Board Flex, Capacitance Change |  |

## Parameters: mechanical

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Land pattern dimension a (reflow) | a | 0.3 |  | 0.5 | mm | Reflow soldering, chip 1.0x0.5 (within +/-0.10), chip code 15 Note: Letter label only in the DS figure; neutral name. Inferred meaning: gap between lands (not printed). | DS p.28, 2. Land Dimensions, Table 2 Reflow Soldering Method, 1.0x0.5 (within +/-0.10), a |  |
| Land pattern dimension b (reflow) | b | 0.35 |  | 0.45 | mm | Reflow soldering, chip 1.0x0.5 (within +/-0.10), chip code 15 Note: Letter label only in the DS figure; neutral name. Inferred meaning: land length, outer side (not printed). | DS p.28, 2. Land Dimensions, Table 2 Reflow Soldering Method, 1.0x0.5 (within +/-0.10), b |  |
| Land pattern dimension c (reflow) | c | 0.4 |  | 0.6 | mm | Reflow soldering, chip 1.0x0.5 (within +/-0.10), chip code 15 Note: Letter label only in the DS figure; neutral name. Inferred meaning: land width across the chip (not printed). | DS p.28, 2. Land Dimensions, Table 2 Reflow Soldering Method, 1.0x0.5 (within +/-0.10), c |  |
| Thickness (T) | T | 0.45 | 0.5 | 0.55 | mm | Applies to: parts GCM155R71H104KE02. Note: min and max are the printed nominal 0.5 -/+ 0.05 (arithmetic). | DS p.2, Type & Dimension, T (0.5+/-0.05) |  |
| Terminal width (e) | e | 0.15 |  | 0.35 | mm | Applies to: parts GCM155R71H104KE02. | DS p.2, Type & Dimension, e (0.15 to 0.35) |  |
| Gap between terminals (g) | g | 0.3 |  |  | mm | Applies to: parts GCM155R71H104KE02. Note: Printed as a minimum only; no max stored. | DS p.2, Type & Dimension, g (0.3 min.) |  |
| Beam load test, destruction value |  |  | More than 8 N (destruction value) |  |  | Speed 0.5 mm/s; chip length 2.5 mm max. Applies to: parts GCM155R71H104KE02. | DS p.6, Specifications and Test Methods, No. 24 Beam Load Test |  |
| Length (L) | L | 0.95 | 1.0 | 1.05 | mm | Applies to: parts GCM155R71H104KE02. Note: min and max are the printed nominal 1.0 -/+ 0.05 (arithmetic); the DS prints 1.0+/-0.05. | DS p.2, Type & Dimension, L (1.0+/-0.05) |  |
| Width (W) | W | 0.45 | 0.5 | 0.55 | mm | Applies to: parts GCM155R71H104KE02. Note: min and max are the printed nominal 0.5 -/+ 0.05 (arithmetic); the DS prints 0.5+/-0.05. | DS p.2, Type & Dimension, W (0.5+/-0.05) |  |
| Solderability: terminations soldered evenly and continuously |  | 95 |  |  | % | Specifications and Test Methods No.16 (a) test conditions Applies to: parts GCM155R71H104KE02. Note: Assembly acceptance criterion, not a circuit limit. | DS p.5, Specifications and Test Methods, No.16 Solderability (a) |  |
| Thickness (T) | T | 0.45 | 0.5 | 0.55 | mm | Applies to: parts GCM1555C1H101FA16. Note: min and max are the printed nominal 0.5 -/+ 0.05 (arithmetic). | DS p.2 (GCM1555C1H101FA16-01A-EN.pdf), Type & Dimension, T (0.5+/-0.05) |  |
| Length (L) | L | 0.95 | 1.0 | 1.05 | mm | Applies to: parts GCM1555C1H101FA16. Note: min and max are the printed nominal 1.0 -/+ 0.05 (arithmetic). | DS p.2 (GCM1555C1H101FA16-01A-EN.pdf), Type & Dimension, L (1.0+/-0.05) |  |
| Width (W) | W | 0.45 | 0.5 | 0.55 | mm | Applies to: parts GCM1555C1H101FA16. Note: min and max are the printed nominal 0.5 -/+ 0.05 (arithmetic). | DS p.2 (GCM1555C1H101FA16-01A-EN.pdf), Type & Dimension, W (0.5+/-0.05) |  |
| Terminal width (e) | e | 0.15 |  | 0.35 | mm | Applies to: parts GCM1555C1H101FA16. | DS p.2 (GCM1555C1H101FA16-01A-EN.pdf), Type & Dimension, e (0.15 to 0.35) |  |
| Gap between terminals (g) | g | 0.3 |  |  | mm | Applies to: parts GCM1555C1H101FA16. Note: Printed as a minimum only; no max stored. | DS p.2 (GCM1555C1H101FA16-01A-EN.pdf), Type & Dimension, g (0.3 min.) |  |
| Beam load test, destruction value |  |  | More than 8 N (destruction value) |  |  | Speed 0.5 mm/s; chip length 2.5 mm max. Applies to: parts GCM1555C1H101FA16. | DS p.5 (GCM1555C1H101FA16-01A-EN.pdf), Specifications and Test Methods, No. 24 Beam Load Test |  |
| Solderability: terminations soldered evenly and continuously |  | 95 |  |  | % | Specifications and Test Methods No.16 (a) test conditions Applies to: parts GCM1555C1H101FA16. Note: Assembly acceptance criterion, not a circuit limit. | DS p.5 (GCM1555C1H101FA16-01A-EN.pdf), Specifications and Test Methods, No.16 Solderability (a) |  |

## Limits of this data

Rows by scope: 25C 6, full 1, na 59, partial 4 (25C rows hold only at 25 degC). Curve (graph) rows: 0. Text rows: 18.

## Zener checks

Generated wrapper: `GCM155.zen` (`python3 -m lib.zen`). abs_max and rec_op rows are errors (abs_max x derate); 25C and partial rows are waivable warnings; a checked net with no voltage is UNVERIFIED.

| Param | Name | Checked against | Not checked / reason |
|---|---|---|---|
| rated_v_ds | Rated voltage (DC) | UNCHECKED | the generated rated_voltage check applies the catalog rated voltage of the selected part; this per-part row duplicates it (owner: module) |
| op_temp_x7r | Operating temperature range | board ambient |  |
| self_heating | Self-heating of the capacitor body (AC or pulse load) | UNCHECKED | depends on AC/pulse current, not a DC net voltage; owner: module |
| ac_peak | AC or pulse voltage: peak-to-peak (and zero-to-peak with DC) within the rated DC voltage | UNCHECKED | AC/pulse waveform is not modelled by the DC net-voltage check; owner: module |
| op_temp_c0g | Operating temperature range | board ambient |  |
| rated_v_ds_c0g | Rated voltage (DC) | UNCHECKED | the generated rated_voltage check applies the catalog rated voltage of the selected part; this per-part row duplicates it (owner: module) |

## Equations

### `capacitance_worst_pct`

```
Not a DS equation: C = C0 * (1 + tol) * (1 + tc).  For percent-change dielectrics (X7R): tc is the capacitance
change over the whole range as a FRACTION (DS p.2, Rated Value, Temp. coeff. or Cap. Change, -15 to 15 % over -55
to 125 degC, ref 25 degC), so with the row's min/max the corners give the full-range worst case. For C0G use
capacitance_worst_ppm: passing its 1/degC coefficient here would treat 3e-5 as a fraction and badly understate
the spread, so |tc| below 1e-3 (other than 0) raises ValueError.
EXCLUDES DC-bias and aging capacitance loss, which the reference sheet does not quantify (DS p.14 section 5 figure;
DS p.15 section 6 figure). For X7R these can dominate. A worst-case stack of printed rows, not a guaranteed
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
| capacitance_worst_pct(c0=1e-07, tol=-0.1, tc=-0.15) | 7.65e-08 | 7.65e-08 | 1e-09 | pass | DS p.2, Rated Value |
| capacitance_worst_ppm(c0=1e-10, tol=-0.01, tc=-3e-05, dt=100) | 9.8703e-11 | 9.8703e-11 | 1e-09 | pass | DS p.2, Rated Value |
