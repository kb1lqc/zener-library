<!-- GENERATED - do not edit. Run: python3 -m lib.readme -->

# ISC750P10LM

## Datasheet review

[![Human page-image review: 0/44 human](https://img.shields.io/badge/human%20review-0%2F44%20human-lightgrey)](../../../docs/spec/datasheet-review.md)

Human page-image review: 0/44; cross-model audits: 0; manufacturer-export stamps: 0; legacy/unclassified: 0. Text checks are not verification. `lib.check` validates stamp format, not that review occurred.

## Part

- **mpn**: ISC750P10LM
- **manufacturer**: Infineon Technologies
- **description**: -100 V P-channel OptiMOS Power-Transistor, logic level, -32 A, 75 mohm max at VGS = -10 V, PG-TDSON-8 (SuperSO8)
- **category**: mosfet
- **package**: PG-TDSON-8 (SuperSO8)
- **datasheet_url**: https://www.infineon.com
- **datasheet_file**: docs/datasheets/infineon/infineon-isc750p10lm-datasheet-en.pdf
- **datasheet_rev**: Rev.2.0
- **datasheet_date**: 2022-10-13
- **temp_grade**: -55 to 175 degC
- **kicad_symbol**: ISC750P10LM.kicad_sym
- **kicad_footprint**: ISC750P10LM.kicad_mod
- **step**: none

## Pins

| Pin | Name | Type | Function | Cite |
|---|---|---|---|---|
| 1 | S | passive | Source, discrete MOSFET terminal; pins 1 to 3 are one source node (DS p.1 pin diagram 'Source Pin 1-3') | DS p.1, pin diagram (SuperSO8), Source Pin 1-3 |
| 2 | S | passive | Source, discrete MOSFET terminal; same source node as pin 1 | DS p.1, pin diagram (SuperSO8), Source Pin 1-3 |
| 3 | S | passive | Source, discrete MOSFET terminal; same source node as pin 1 | DS p.1, pin diagram (SuperSO8), Source Pin 1-3 |
| 4 | G | passive | Gate, discrete MOSFET terminal (DS p.1 pin diagram 'Gate Pin 4') | DS p.1, pin diagram (SuperSO8), Gate Pin 4 |
| 5 | D | passive | Drain, discrete MOSFET terminal; pins 5 to 8 are one drain node (DS p.1 pin diagram 'Drain Pin 5-8'). The drain tab (exposed pad) has no DS number and is not a separate pin: the footprint makes it pad 5 (a real pad on the drain net), overlapping the drain lead pads 5-8. | DS p.1, pin diagram (SuperSO8), Drain Pin 5-8 |
| 6 | D | passive | Drain, discrete MOSFET terminal; same drain node as pin 5 | DS p.1, pin diagram (SuperSO8), Drain Pin 5-8 |
| 7 | D | passive | Drain, discrete MOSFET terminal; same drain node as pin 5 | DS p.1, pin diagram (SuperSO8), Drain Pin 5-8 |
| 8 | D | passive | Drain, discrete MOSFET terminal; same drain node as pin 5 | DS p.1, pin diagram (SuperSO8), Drain Pin 5-8 |

## Parameters: abs_max

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Continuous drain current, TC = 25 degC | ID |  |  | -32 | A | VGS = -10 V, TC = 25 degC Note: Printed in the Max column with a minus sign (P-channel sign convention, stored as printed). Footnote 1: derate for other case temperatures (Diagram 2). | DS p.3, Table 2 Maximum ratings, Continuous drain current ID (row 1) |  |
| Continuous drain current, TC = 100 degC | ID |  |  | -28 | A | VGS = -10 V, TC = 100 degC | DS p.3, Table 2 Maximum ratings, Continuous drain current ID (row 2) |  |
| Continuous drain current, PCB-limited | ID |  |  | -3.8 | A | VGS = -4.5 V, TA = 25 degC, RthJA = 50 degC/W Note: Footnote 2: 40 x 40 x 1.5 mm FR4 PCB with 6 cm2 drain copper, vertical in still air. | DS p.3, Table 2 Maximum ratings, Continuous drain current ID (row 3), footnote 2 |  |
| Pulsed drain current | ID,pulse |  |  | -129 | A | TA = 25 degC Note: The SOA (Diagram 3) is not extracted (open item). The DS prints TA = 25 degC on this row. | DS p.3, Table 2 Maximum ratings, Pulsed drain current ID,pulse (footnote 3: Diagram 3) |  |
| Gate-source voltage | VGS | -20 (rel. S) |  | 20 (rel. S) | V | Note: No reference pin printed; applied as gate to source (pin-pair row, S is the reference). | DS p.3, Table 2 Maximum ratings, Gate source voltage VGS |  |
| Power dissipation, TA = 25 degC (as printed) | Ptot |  |  | 188 | W | TA = 25 degC Note: Stored as printed. The DS prints TA = 25 degC on this 188 W row. Printed TA = 25 degC (render confirmed on both Ptot rows); the value is consistent with a TC rating (Diagram 1 is Ptot = f(TC)). DS ambiguity, open item: not corrected. | DS p.3, Table 2 Maximum ratings, Power dissipation Ptot (row 1) |  |
| Power dissipation, PCB-limited | Ptot |  |  | 3 | W | TA = 25 degC, RthJA = 50 degC/W | DS p.3, Table 2 Maximum ratings, Power dissipation Ptot (row 2), footnote 2 |  |
| Operating and storage temperature Tj, Tstg | Tj,Tstg | -55 |  | 175 | degC | Note: Junction range (Tj); the storage part of the row is assembly-owned (see the unchecked reason). | DS p.3, Table 2 Maximum ratings, Operating and storage temperature Tj, Tstg |  |
| IEC climatic category |  |  | 55/175/56 |  |  | DIN IEC 68-1 Note: Classification printed as text; no number. | DS p.3, Table 2 Maximum ratings, Operating and storage temperature, IEC climatic category (note column) |  |
| Avalanche energy, single pulse | EAS |  |  | 710 | mJ | ID = -25 A, RGS = 25 ohm | DS p.3, Table 2 Maximum ratings, Avalanche energy, single pulse EAS (footnote 4: Diagram 13) |  |

## Parameters: rec_op

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Drain-source voltage rating | VDS | -100 (rel. S) |  |  | V | Note: Not a row of the Maximum ratings table (DS p.3). P-channel: the limit is on the negative side, so it is stored as min = -100 (numeric order), not max. The DS gives no temperature for it. The guaranteed breakdown is V(BR)DSS = -100 V at 25 degC (vbr_dss, DS p.4 Table 4), the same value. | DS p.1, Table 1 Key Performance Parameters, VDS |  |

## Parameters: electrical

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Drain-source breakdown voltage | V(BR)DSS | -100 |  |  | V | VGS = 0 V, ID = -250 uA | DS p.4, Table 4 Static characteristics, Drain-source breakdown voltage V(BR)DSS |  |
| Gate threshold voltage | VGS(th) | -2 | -1.6 | -1 | V | VDS = VGS, ID = -2304 uA Note: Printed MIN -1, TYP -1.6, MAX -2. Stored in numeric order: min = printed MAX (-2), max = printed MIN (-1). | DS p.4, Table 4 Static characteristics, Gate threshold voltage VGS(th) |  |
| Zero gate voltage drain current, Tj = 25 degC | IDSS | -1 | -0.1 |  | uA | VDS = -100 V, VGS = 0 V, Tj = 25 degC Note: Printed MIN '-', TYP -0.1, MAX -1 (the bound is the printed MAX). Stored as min = -1 (numeric order, the bound), no max. | DS p.4, Table 4 Static characteristics, Zero gate voltage drain current IDSS (row 1) |  |
| Zero gate voltage drain current, Tj = 125 degC | IDSS | -100 | -10 |  | uA | VDS = -100 V, VGS = 0 V, Tj = 125 degC Note: Printed MIN '-', TYP -10, MAX -100. Stored as min = -100 (numeric order). Single stated temperature (125 degC). | DS p.4, Table 4 Static characteristics, Zero gate voltage drain current IDSS (row 2) |  |
| Gate-source leakage current | IGSS | -100 | -10 |  | nA | VGS = -20 V, VDS = 0 V Note: Printed MIN '-', TYP -10, MAX -100. Stored as min = -100 (numeric order). | DS p.4, Table 4 Static characteristics, Gate-source leakage current IGSS |  |
| Drain-source on-state resistance, VGS = -10 V | RDS(on) |  | 61 | 75 | mohm | VGS = -10 V, ID = -25 A Note: Table 1 prints RDS(on),max 75 mohm (DS p.1), same value. Tj = 25 degC only (open item, see calc.py). | DS p.4, Table 4 Static characteristics, Drain-source on-state resistance RDS(on) (row 1) |  |
| Drain-source on-state resistance, VGS = -4.5 V | RDS(on) |  | 63 | 86 | mohm | VGS = -4.5 V, ID = -20 A Note: Tj = 25 degC only (open item, see calc.py). | DS p.4, Table 4 Static characteristics, Drain-source on-state resistance RDS(on) (row 2) |  |
| Normalized drain-source on-state resistance at Tj = 100 degC (curve) | RDS(on)/RDS(on)25C |  | 1.6 |  |  | ID = -25 A, VGS = -10 V, normalized to 25 degC, Tj = 100 degC Note: Read by eye, +/-0.05. The figure has one unlabelled line: read as the typical curve (no typ or max line printed). Not a bound. | DS p.8, Diagram 9 figure Normalized drain-source on resistance, RDS(on)=f(Tj), ID = -25 A, VGS = -10 V, read at Tj = 100 degC (curve) |  |
| Normalized drain-source on-state resistance at Tj = 150 degC (curve) | RDS(on)/RDS(on)25C |  | 2.1 |  |  | ID = -25 A, VGS = -10 V, normalized to 25 degC, Tj = 150 degC Note: Read by eye, +/-0.05. Unlabelled single line: typical curve, not a bound. 150 degC is the printed Tj max. | DS p.8, Diagram 9 figure Normalized drain-source on resistance, RDS(on)=f(Tj), ID = -25 A, VGS = -10 V, read at Tj = 150 degC (curve) |  |
| Gate resistance | RG |  | 5.2 |  | ohm | Note: Typical only. | DS p.4, Table 4 Static characteristics, Gate resistance RG |  |
| Transconductance | gfs |  | 51 |  | A/V | \|VDS\| >= 2\|ID\| RDS(on)max, ID = -25 A Note: Printed unit S; S = A/V, stored as A/V (loader has no S unit). Typical only. | DS p.4, Table 4 Static characteristics, Transconductance gfs |  |
| Input capacitance | Ciss |  | 3600 | 4700 | pF | VGS = 0 V, VDS = -50 V, f = 1 MHz Note: Defined by design. Not subject to production test (footnote 1). | DS p.4, Table 5 Dynamic characteristics, Input capacitance Ciss |  |
| Output capacitance | Coss |  | 230 | 300 | pF | VGS = 0 V, VDS = -50 V, f = 1 MHz Note: Defined by design. Not subject to production test (footnote 1). | DS p.4, Table 5 Dynamic characteristics, Output capacitance Coss |  |
| Reverse transfer capacitance | Crss |  | 50 | 88 | pF | VGS = 0 V, VDS = -50 V, f = 1 MHz Note: Defined by design. Not subject to production test (footnote 1). | DS p.4, Table 5 Dynamic characteristics, Reverse transfer capacitance Crss |  |
| Turn-on delay time | td(on) |  | 35.6 |  | ns | VDD = -50 V, VGS = -4.5 V, ID = -25 A, RG,ext = 1.6 ohm Note: Typical only. | DS p.4, Table 5 Dynamic characteristics, Turn-on delay time td(on) |  |
| Rise time | tr |  | 47.2 |  | ns | VDD = -50 V, VGS = -4.5 V, ID = -25 A, RG,ext = 1.6 ohm Note: Typical only. | DS p.4, Table 5 Dynamic characteristics, Rise time tr |  |
| Turn-off delay time | td(off) |  | 100 |  | ns | VDD = -50 V, VGS = -4.5 V, ID = -25 A, RG,ext = 1.6 ohm Note: Typical only. | DS p.4, Table 5 Dynamic characteristics, Turn-off delay time td(off) |  |
| Fall time | tf |  | 24.8 |  | ns | VDD = -50 V, VGS = -4.5 V, ID = -25 A, RG,ext = 1.6 ohm Note: Typical only. | DS p.4, Table 5 Dynamic characteristics, Fall time tf |  |
| Gate plateau voltage | Vplateau |  | -3.1 |  | V | VDD = -50 V, ID = -25 A, VGS = 0 to -4.5 V Note: Typical only. | DS p.4, Table 6 Gate charge characteristics, Gate plateau voltage Vplateau |  |
| Diode continuous forward current | IS |  |  | -32 | A | TC = 25 degC Note: Printed in the Max column with a minus sign. Single stated temperature (TC = 25 degC). | DS p.5, Table 7 Reverse diode, Diode continuous forward current IS |  |
| Diode pulse current | IS,pulse |  |  | -129 | A | TC = 25 degC Note: Printed in the Max column with a minus sign. Single stated temperature (TC = 25 degC). | DS p.5, Table 7 Reverse diode, Diode pulse current IS,pulse |  |
| Diode forward voltage | VSD | -1 | -0.84 |  | V | VGS = 0 V, IF = -25 A, Tj = 25 degC Note: Printed MIN '-', TYP -0.84, MAX -1 (the bound is the printed MAX). Stored as min = -1 (numeric order). | DS p.5, Table 7 Reverse diode, Diode forward voltage VSD |  |
| Reverse recovery time | trr |  | 86 | 172 | ns | VR = -50 V, IF = -25 A, diF/dt = -100 A/us Note: Defined by design. Not subject to production test (footnote 1). | DS p.5, Table 7 Reverse diode, Reverse recovery time trr |  |
| Gate to source charge | Qgs |  | -11 |  | nC | VDD = -50 V, ID = -25 A, VGS = 0 to -4.5 V | DS p.4, Table 6 Gate charge characteristics, Gate to source charge Qgs |  |
| Gate charge at threshold | Qg(th) |  | -5.7 |  | nC | VDD = -50 V, ID = -25 A, VGS = 0 to -4.5 V | DS p.4, Table 6 Gate charge characteristics, Gate charge at threshold Qg(th) |  |
| Gate to drain charge | Qgd | -35 | -23 |  | nC | VDD = -50 V, ID = -25 A, VGS = 0 to -4.5 V Note: Printed MIN '-', TYP -23, MAX -35. Stored as min = -35 (numeric order). Defined by design (footnote 1). | DS p.4, Table 6 Gate charge characteristics, Gate to drain charge Qgd (footnote 1) |  |
| Switching charge | Qsw |  | -29 |  | nC | VDD = -50 V, ID = -25 A, VGS = 0 to -4.5 V | DS p.4, Table 6 Gate charge characteristics, Switching charge Qsw |  |
| Gate charge total, VGS = -4.5 V | Qg | -58 | -46 |  | nC | VDD = -50 V, ID = -25 A, VGS = 0 to -4.5 V Note: Printed MIN '-', TYP -46, MAX -58. Stored as min = -58 (numeric order). Defined by design (footnote 1). | DS p.4, Table 6 Gate charge characteristics, Gate charge total Qg (row 1, footnote 1) |  |
| Gate charge total, VGS = -10 V | Qg | -122 | -92 |  | nC | VDD = -50 V, ID = -25 A, VGS = 0 to -10 V Note: Printed MIN '-', TYP -92, MAX -122. Stored as min = -122 (numeric order). Defined by design (footnote 1). | DS p.4, Table 6 Gate charge characteristics, Gate charge total Qg (row 2, footnote 1) |  |
| Output charge | Qoss | -38 | -28.3 |  | nC | VDS = -50 V, VGS = 0 V Note: Printed MIN '-', TYP -28.3, MAX -38. Stored as min = -38 (numeric order). Defined by design (footnote 1). | DS p.4, Table 6 Gate charge characteristics, Output charge Qoss (footnote 1) |  |
| Reverse recovery charge | Qrr | -580 | -290 |  | nC | VR = -50 V, IF = -25 A, diF/dt = -100 A/us Note: DS ambiguity (open item): typ printed -290, max printed 580 with no minus sign (render DS p.5 checked). Stored as min = -580: the sign is inferred from typ -290 and the P-channel magnitude-order convention (printed Max -> min); the printed 580 carries no minus sign. Defined by design (footnote 1). | DS p.5, Table 7 Reverse diode, Reverse recovery charge Qrr (footnote 1) |  |

## Parameters: thermal

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Thermal resistance, junction to case | RthJC |  |  | 0.8 | degC/W | Note: No bottom or top qualifier in the DS (only one RthJC row); the drain-pad side is not stated. | DS p.3, Table 3 Thermal characteristics, Thermal resistance junction-case |  |
| Thermal resistance, junction to ambient, 6 cm2 PCB | RthJA |  |  | 50 | degC/W | Device on PCB, 6 cm2 cooling area Note: Valid only for the DS PCB (footnote 2). | DS p.3, Table 3 Thermal characteristics, Device on PCB 6 cm2 cooling area (RthJA), footnote 2 |  |

## Limits of this data

Rows by scope: 25C 26, na 18 (25C rows hold only at 25 degC). Curve (graph) rows: 2. Text rows: 1. Temperatures are junction (TJ): analyse with TJ = TA + P x RthJA; no ambient range is printed.

## Zener checks

Generated wrapper: `ISC750P10LM.zen` (`python3 -m lib.zen`). abs_max and rec_op rows are errors (abs_max x derate); 25C and partial rows are waivable warnings; a checked net with no voltage is UNVERIFIED.

| Param | Name | Checked against | Not checked / reason |
|---|---|---|---|
| vds_rating | Drain-source voltage rating | pins D |  |
| id_tc25 | Continuous drain current, TC = 25 degC | UNCHECKED | not a voltage; owner: module |
| id_tc100 | Continuous drain current, TC = 100 degC | UNCHECKED | not a voltage; owner: module |
| id_pcb | Continuous drain current, PCB-limited | UNCHECKED | not a voltage; owner: module |
| id_pulse | Pulsed drain current | UNCHECKED | not a voltage; owner: module |
| vgs | Gate-source voltage | pins G |  |
| ptot_ta25 | Power dissipation, TA = 25 degC (as printed) | UNCHECKED | not a voltage; owner: module |
| ptot_pcb | Power dissipation, PCB-limited | UNCHECKED | not a voltage; owner: module |
| tj_tstg | Operating and storage temperature Tj, Tstg | UNCHECKED | TJ: needs dissipation x RthJA; owner: module (Tstg part: owner: assembly) |
| iec_climatic | IEC climatic category | UNCHECKED | owner: assembly (climatic classification, not an operating voltage or temperature) |
| eas | Avalanche energy, single pulse | UNCHECKED | not a voltage; owner: module |

## Equations

### `conduction_loss`

```
Not a DS equation: conduction loss P = I^2 x RDS(on). Use the 25 degC max row (rds_on_10v.max at VGS = -10 V) for a
bound at 25 degC; above 25 degC use rds_on_at_tj_typ, a typical estimate. i: drain current, A (sign ignored, squared).
rds_on: ohm. Returns: W.
```

Inputs:

- `rds_on` -> `rds_on_10v.max` (typ 61 max 75 mohm)

### `rds_on_at_tj_typ`

```
Curve-based estimate, not a bound: RDS(on) at Tj = rds_on_25 x factor. factor = RDS(on)/RDS(on)@25 degC read off
DS p.8 Diagram 9 (normalized, ID = -25 A, VGS = -10 V). The curve is unlabelled, read as typical.
rds_on_25: ohm (the 25 degC max row). factor: fraction, 1.0 at 25 degC. Returns: ohm.
```

Inputs:

- `rds_on_25` -> `rds_on_10v.max` (typ 61 max 75 mohm)
- `factor` -> `norm_rds_150c.typ` (typ 2.1 )

### `tj_from_case`

```
Not a DS equation: TJ = TC + P x RthJC, the case-referenced junction temperature (DS p.3 Table 3 RthJC, no
bottom or top qualifier in the DS). tc: case temperature, degC. p: dissipation, W, >= 0. rth_jc: degC/W, use the max
row for a bound. Returns: degC.
```

Inputs:

- `rth_jc` -> `rth_jc.max` (max 0.8 degC/W)

### `tj_from_ambient`

```
Not a DS equation: TJ = TA + P x RthJA (DS p.3 Table 3, device on PCB, 6 cm2 cooling area, footnote 2).
Valid only for that PCB. ta: ambient temperature, degC. p: dissipation, W, >= 0. rth_ja: degC/W, use the max row.
Returns: degC.
```

Inputs:

- `rth_ja` -> `rth_ja.max` (max 50 degC/W)

### `gate_drive_time`

```
Not a DS equation: time to charge the gate, t = |Qg| / Ig, Qg from DS p.4 Table 6 (Qg, VGS = 0 to -10 V, the
printed magnitude 122 nC) and Ig the gate drive current (design choice). abs() is applied to the printed negative
charge. qg: C. ig: A, > 0. Returns: s.
```

Inputs:

- `qg` -> `qg_10v.min` (min -122 typ -92 nC)


## Examples

| Call | Computed | Expected | Rel. tol | Result | Cite |
|---|---|---|---|---|---|
| conduction_loss(i=-25, rds_on=0.075) | 46.875 | 46.875 | 1e-09 | pass | DS p.4 Table 4 and p.1 Table 1, RDS(on) max 75 mohm at VGS = -10 V, ID = -25 A (arithmetic only; sign ignored) |
| rds_on_at_tj_typ(rds_on_25=0.075, factor=1) | 0.075 | 0.075 | 1e-09 | pass | DS p.8 Diagram 9 is normalized to 25 degC: factor 1.0 at 25 degC by definition (arithmetic only) |
| tj_from_ambient(ta=25, p=3, rth_ja=50) | 175 | 175 | 1e-09 | pass | DS p.3 Table 2 Ptot = 3 W at TA = 25 degC with RthJA = 50 degC/W gives Tj = 175 degC, the printed Tj max |
| tj_from_case(tc=25, p=10, rth_jc=0.8) | 33 | 33 | 1e-09 | pass | DS p.3 Table 3 RthJC max 0.8 degC/W (arithmetic only) |
| gate_drive_time(qg=-1.22e-07, ig=1) | 1.22e-07 | 1.22e-07 | 1e-09 | pass | DS p.4 Table 6 Qg VGS = -10 V, printed magnitude 122 nC, Ig = 1 A (arithmetic only; abs applied) |
