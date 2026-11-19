<!-- GENERATED - do not edit. Run: python3 -m lib.readme -->

# BSC040N10NS5

## Datasheet review

[![Human page-image review: 0/47 human](https://img.shields.io/badge/human%20review-0%2F47%20human-lightgrey)](../../../docs/spec/datasheet-review.md)

Human page-image review: 0/47; cross-model audits: 0; manufacturer-export stamps: 0; legacy/unclassified: 0. Text checks are not verification. `lib.check` validates stamp format, not that review occurred.

## Part

- **mpn**: BSC040N10NS5
- **manufacturer**: Infineon Technologies
- **description**: 100 V N-channel OptiMOS 5 power MOSFET, 136 A, 4.0 mohm max at VGS=10 V, PG-TDSON-8 (SuperSO8)
- **category**: mosfet
- **package**: PG-TDSON-8 (SuperSO8)
- **datasheet_url**: https://www.infineon.com
- **datasheet_file**: docs/datasheets/infineon/infineon-bsc040n10ns5-datasheet-en.pdf
- **datasheet_rev**: Rev.2.4
- **datasheet_date**: 2020-05-15
- **temp_grade**: -55 to 150 degC
- **kicad_symbol**: BSC040N10NS5.kicad_sym
- **kicad_footprint**: BSC040N10NS5.kicad_mod
- **step**: none

## Pins

| Pin | Name | Type | Function | Cite |
|---|---|---|---|---|
| 1 | S | passive | Source (S1), discrete MOSFET terminal; S1, S2 and S3 are one source node | DS p.1, pin diagram (SuperSO8), S 1 |
| 2 | S | passive | Source (S2), discrete MOSFET terminal; same source node as pin 1 | DS p.1, pin diagram (SuperSO8), S 2 |
| 3 | S | passive | Source (S3), discrete MOSFET terminal; same source node as pin 1 | DS p.1, pin diagram (SuperSO8), S 3 |
| 4 | G | passive | Gate (G4), discrete MOSFET terminal | DS p.1, pin diagram (SuperSO8), G 4 |
| 5 | D | passive | Drain (D5), discrete MOSFET terminal; pins 5 to 8 are one drain node. The drain tab (exposed pad) has no DS number and is not a separate pin: the footprint makes it pad 5 (a real pad on the drain net), overlapping the drain lead pads 5-8. | DS p.1, pin diagram (SuperSO8), 5 D |
| 6 | D | passive | Drain (D6), discrete MOSFET terminal; same drain node as pin 5 | DS p.1, pin diagram (SuperSO8), 6 D |
| 7 | D | passive | Drain (D7), discrete MOSFET terminal; same drain node as pin 5 | DS p.1, pin diagram (SuperSO8), 7 D |
| 8 | D | passive | Drain (D8), discrete MOSFET terminal; same drain node as pin 5 | DS p.1, pin diagram (SuperSO8), 8 D |

## Parameters: abs_max

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Continuous drain current, TC = 25 degC | ID |  |  | 136 | A | VGS = 10 V, TC = 25 degC Note: Footnote 1: rating refers to the product only with absolute maximum values, case temperature held at 25 degC; derate above it (Diagram 2). | DS p.3, Table 2 Maximum ratings, Continuous drain current ID (row 1) |  |
| Continuous drain current, TC = 100 degC | ID |  |  | 86 | A | VGS = 10 V, TC = 100 degC | DS p.3, Table 2 Maximum ratings, Continuous drain current ID (row 2) |  |
| Continuous drain current, PCB-limited | ID |  |  | 18 | A | VGS = 10 V, TC = 25 degC, RthJA = 50 K/W Note: Footnote 2: 40 x 40 x 1.5 mm FR4 PCB with 6 cm2 drain copper, vertical in still air. Printed RthJA 50 K/W is the PCB value. | DS p.3, Table 2 Maximum ratings, Continuous drain current ID (row 3), footnote 2 |  |
| Pulsed drain current | ID,pulse |  |  | 544 | A | TC = 25 degC Note: The SOA (Diagram 3) is not extracted (open item). | DS p.3, Table 2 Maximum ratings, Pulsed drain current ID,pulse (footnote 3: Diagram 3 SOA) |  |
| Gate-source voltage | VGS | -20 (rel. S) |  | 20 (rel. S) | V | Note: No reference pin printed; applied as gate to source (pin-pair row, S is the reference). | DS p.3, Table 2 Maximum ratings, Gate source voltage VGS |  |
| Power dissipation, TC = 25 degC | Ptot |  |  | 139 | W | TC = 25 degC Note: Ptot = f(TC) is Diagram 1 (curve, not extracted). Stored at TC = 25 degC only. | DS p.3, Table 2 Maximum ratings, Power dissipation Ptot (row 1) |  |
| Power dissipation, PCB-limited | Ptot |  |  | 2.5 | W | TA = 25 degC, RthJA = 50 K/W | DS p.3, Table 2 Maximum ratings, Power dissipation Ptot (row 2), footnote 3 |  |
| Operating and storage temperature Tj, Tstg | Tj,Tstg | -55 |  | 150 | degC | Note: Junction range (Tj); the storage part of the row is assembly-owned (see the note below). | DS p.3, Table 2 Maximum ratings, Operating and storage temperature Tj, Tstg |  |
| IEC climatic category |  |  | 55/150/56 |  |  | DIN IEC 68-1 Note: Classification printed as text; no number. | DS p.3, Table 2 Maximum ratings, Operating and storage temperature, IEC climatic category (note column) |  |
| Avalanche energy, single pulse | EAS |  |  | 268 | mJ | ID = 50 A, RGS = 25 ohm | DS p.3, Table 2 Maximum ratings, Avalanche energy, single pulse EAS (footnote 4: Diagram 13) |  |

## Parameters: rec_op

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Drain-source voltage rating | VDS |  |  | 100 (rel. S) | V | Note: Not a row of the Maximum ratings table (DS p.3). The DS gives no temperature for it. The guaranteed minimum breakdown voltage is V(BR)DSS = 100 V at 25 degC (vbr_dss, DS p.4 Table 4). Printed with no MIN/TYP/MAX label: stored as max. Only the upper bound is checked; the body-diode negative drain voltage is not a row in this DS. | DS p.1, Table 1 Key Performance Parameters, VDS |  |

## Parameters: electrical

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Drain-source breakdown voltage | V(BR)DSS | 100 |  |  | V | VGS = 0 V, ID = 1 mA | DS p.4, Table 4 Static characteristics, Drain-source breakdown voltage V(BR)DSS |  |
| Gate threshold voltage | VGS(th) | 2.2 | 3.0 | 3.8 | V | VDS = VGS, ID = 95 uA | DS p.4, Table 4 Static characteristics, Gate threshold voltage VGS(th) |  |
| Zero gate voltage drain current, Tj = 25 degC | IDSS |  | 0.1 | 1 | uA | VDS = 100 V, VGS = 0 V, Tj = 25 degC | DS p.4, Table 4 Static characteristics, Zero gate voltage drain current IDSS (row 1) |  |
| Zero gate voltage drain current, Tj = 125 degC | IDSS |  | 10 | 100 | uA | VDS = 100 V, VGS = 0 V, Tj = 125 degC Note: Single stated temperature (125 degC); not a full-range row. | DS p.4, Table 4 Static characteristics, Zero gate voltage drain current IDSS (row 2) |  |
| Gate-source leakage current | IGSS |  | 10 | 100 | nA | VGS = 20 V, VDS = 0 V | DS p.4, Table 4 Static characteristics, Gate-source leakage current IGSS |  |
| Drain-source on-state resistance, VGS = 10 V | RDS(on) |  | 3.4 | 4.0 | mohm | VGS = 10 V, ID = 50 A Note: Table 1 prints RDS(on),max 4.0 mohm (DS p.1), same value. Tj = 25 degC only: no RDS(on) row over temperature (open item, see calc.py). | DS p.4, Table 4 Static characteristics, Drain-source on-state resistance RDS(on) (row 1) |  |
| Drain-source on-state resistance, VGS = 6 V | RDS(on) |  | 4.0 | 5.6 | mohm | VGS = 6 V, ID = 25 A | DS p.4, Table 4 Static characteristics, Drain-source on-state resistance RDS(on) (row 2) |  |
| Drain-source on-state resistance at Tj = 100 degC, typical line (curve) | RDS(on) |  | 4.9 |  | mohm | ID = 50 A, VGS = 10 V, Tj = 100 degC Note: Read by eye off the figure, +/-0.15 mohm. Typical line (labelled typ on the figure). Not a bound. | DS p.8, Diagram 9 figure Drain-source on-state resistance, RDS(on)=f(Tj), typ line, read at Tj = 100 degC (curve) |  |
| Drain-source on-state resistance at Tj = 100 degC, max line (curve) | RDS(on) |  |  | 5.8 | mohm | ID = 50 A, VGS = 10 V, Tj = 100 degC Note: Read by eye off the figure, +/-0.15 mohm. Printed max line: the bound-like curve value (not a guaranteed row). | DS p.8, Diagram 9 figure Drain-source on-state resistance, RDS(on)=f(Tj), max line, read at Tj = 100 degC (curve) |  |
| Drain-source on-state resistance at Tj = 150 degC, typical line (curve) | RDS(on) |  | 6.2 |  | mohm | ID = 50 A, VGS = 10 V, Tj = 150 degC Note: Read by eye off the figure, +/-0.15 mohm. Typical line (labelled typ). Not a bound. 150 degC is the printed Tj max. | DS p.8, Diagram 9 figure Drain-source on-state resistance, RDS(on)=f(Tj), typ line, read at Tj = 150 degC (curve) |  |
| Drain-source on-state resistance at Tj = 150 degC, max line (curve) | RDS(on) |  |  | 7.4 | mohm | ID = 50 A, VGS = 10 V, Tj = 150 degC Note: Read by eye off the figure, +/-0.15 mohm. Printed max line: the bound-like curve value at the hottest printed Tj (not a guaranteed row). Use this for hot conduction loss. | DS p.8, Diagram 9 figure Drain-source on-state resistance, RDS(on)=f(Tj), max line, read at Tj = 150 degC (curve) |  |
| Gate resistance | RG |  | 1.3 | 2.0 | ohm | Note: Footnote 1 on the row: defined by design, not subject to production test. | DS p.4, Table 4 Static characteristics, Gate resistance RG |  |
| Transconductance | gfs | 60 | 120 |  | A/V | \|VDS\| > 2\|ID\| RDS(on)max, ID = 50 A Note: Printed unit S; S = A/V, stored as A/V (loader has no S unit). | DS p.4, Table 4 Static characteristics, Transconductance gfs |  |
| Input capacitance | Ciss |  | 4100 | 5300 | pF | VGS = 0 V, VDS = 50 V, f = 1 MHz Note: Defined by design. Not subject to production test (footnote 1). | DS p.4, Table 5 Dynamic characteristics, Input capacitance Ciss |  |
| Output capacitance | Coss |  | 630 | 820 | pF | VGS = 0 V, VDS = 50 V, f = 1 MHz Note: Defined by design. Not subject to production test (footnote 1). | DS p.4, Table 5 Dynamic characteristics, Output capacitance Coss |  |
| Reverse transfer capacitance | Crss |  | 28 | 49 | pF | VGS = 0 V, VDS = 50 V, f = 1 MHz Note: Defined by design. Not subject to production test (footnote 1). | DS p.4, Table 5 Dynamic characteristics, Reverse transfer capacitance Crss |  |
| Turn-on delay time | td(on) |  | 13 |  | ns | VDD = 50 V, VGS = 10 V, ID = 50 A, RG,ext = 3.0 ohm Note: Typical only (no min or max printed). | DS p.4, Table 5 Dynamic characteristics, Turn-on delay time td(on) |  |
| Rise time | tr |  | 9 |  | ns | VDD = 50 V, VGS = 10 V, ID = 50 A, RG,ext = 3.0 ohm Note: Typical only. | DS p.4, Table 5 Dynamic characteristics, Rise time tr |  |
| Turn-off delay time | td(off) |  | 32 |  | ns | VDD = 50 V, VGS = 10 V, ID = 50 A, RG,ext = 3.0 ohm Note: Typical only. | DS p.4, Table 5 Dynamic characteristics, Turn-off delay time td(off) |  |
| Fall time | tf |  | 10 |  | ns | VDD = 50 V, VGS = 10 V, ID = 50 A, RG,ext = 3.0 ohm Note: Typical only. | DS p.4, Table 5 Dynamic characteristics, Fall time tf |  |
| Gate plateau voltage | Vplateau |  | 4.6 |  | V | VDD = 50 V, ID = 50 A, VGS = 0 to 10 V Note: Typical only. | DS p.4, Table 6 Gate charge characteristics, Gate plateau voltage Vplateau |  |
| Diode continuous forward current | IS |  |  | 126 | A | TC = 25 degC Note: Single stated temperature (TC = 25 degC). | DS p.5, Table 7 Reverse diode, Diode continuous forward current IS |  |
| Diode pulse current | IS,pulse |  |  | 544 | A | TC = 25 degC Note: Single stated temperature (TC = 25 degC). | DS p.5, Table 7 Reverse diode, Diode pulse current IS,pulse |  |
| Diode forward voltage | VSD |  | 0.86 | 1.1 | V | VGS = 0 V, IF = 50 A, Tj = 25 degC | DS p.5, Table 7 Reverse diode, Diode forward voltage VSD |  |
| Reverse recovery time | trr |  | 54 | 108 | ns | VR = 50 V, IF = 50 A, diF/dt = 100 A/us Note: Defined by design. Not subject to production test (footnote 1). | DS p.5, Table 7 Reverse diode, Reverse recovery time trr |  |
| Gate to source charge | Qgs |  | 19 |  | nC | VDD = 50 V, ID = 50 A, VGS = 0 to 10 V | DS p.4, Table 6 Gate charge characteristics, Gate to source charge Qgs |  |
| Gate charge at threshold | Qg(th) |  | 11 |  | nC | VDD = 50 V, ID = 50 A, VGS = 0 to 10 V | DS p.4, Table 6 Gate charge characteristics, Gate charge at threshold Qg(th) |  |
| Gate to drain charge | Qgd |  | 12 | 18 | nC | VDD = 50 V, ID = 50 A, VGS = 0 to 10 V Note: Defined by design. Not subject to production test (footnote 1). | DS p.4, Table 6 Gate charge characteristics, Gate to drain charge Qgd |  |
| Switching charge | Qsw |  | 19 |  | nC | VDD = 50 V, ID = 50 A, VGS = 0 to 10 V | DS p.4, Table 6 Gate charge characteristics, Switching charge Qsw |  |
| Gate charge total | Qg |  | 58 | 72 | nC | VDD = 50 V, ID = 50 A, VGS = 0 to 10 V Note: Defined by design. Not subject to production test (footnote 1). | DS p.4, Table 6 Gate charge characteristics, Gate charge total Qg |  |
| Gate charge total, sync. FET | Qg(sync) |  | 50 |  | nC | VDS = 0.1 V, VGS = 0 to 10 V | DS p.4, Table 6 Gate charge characteristics, Gate charge total, sync. FET Qg(sync) |  |
| Output charge | Qoss |  | 75 | 100 | nC | VDD = 50 V, VGS = 0 V Note: Defined by design. Not subject to production test (footnote 1). | DS p.4, Table 6 Gate charge characteristics, Output charge Qoss |  |
| Reverse recovery charge | Qrr |  | 90 | 180 | nC | VR = 50 V, IF = 50 A, diF/dt = 100 A/us Note: Defined by design. Not subject to production test (footnote 1). | DS p.5, Table 7 Reverse diode, Reverse recovery charge Qrr |  |

## Parameters: thermal

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Thermal resistance, junction to case, bottom | RthJC |  | 0.5 | 0.9 | degC/W | Note: Printed unit K/W, stored as degC/W (same value for a temperature difference, the loader does not accept K/W). | DS p.3, Table 3 Thermal characteristics, Thermal resistance junction-case, bottom |  |
| Thermal resistance, junction to case, top | RthJC |  |  | 20 | degC/W | Note: Printed unit K/W, stored as degC/W. Top side is not the drain-to-PCB path; calc.tj_from_case uses the bottom row. | DS p.3, Table 3 Thermal characteristics, Thermal resistance junction-case, top |  |
| Thermal resistance, junction to ambient, 6 cm2 PCB | RthJA |  |  | 50 | degC/W | Device on PCB, 6 cm2 cooling area Note: Printed unit K/W, stored as degC/W. Valid only for the DS PCB (footnote 2). | DS p.3, Table 3 Thermal characteristics, Device on PCB 6 cm2 cooling area (RthJA), footnote 2 |  |

## Limits of this data

Rows by scope: 25C 26, na 21 (25C rows hold only at 25 degC). Curve (graph) rows: 4. Text rows: 1. Temperatures are junction (TJ): analyse with TJ = TA + P x RthJA; no ambient range is printed.

## Zener checks

Generated wrapper: `BSC040N10NS5.zen` (`python3 -m lib.zen`). abs_max and rec_op rows are errors (abs_max x derate); 25C and partial rows are waivable warnings; a checked net with no voltage is UNVERIFIED.

| Param | Name | Checked against | Not checked / reason |
|---|---|---|---|
| vds_rating | Drain-source voltage rating | pins D |  |
| id_tc25 | Continuous drain current, TC = 25 degC | UNCHECKED | not a voltage; owner: module |
| id_tc100 | Continuous drain current, TC = 100 degC | UNCHECKED | not a voltage; owner: module |
| id_pcb | Continuous drain current, PCB-limited | UNCHECKED | not a voltage; owner: module |
| id_pulse | Pulsed drain current | UNCHECKED | not a voltage; owner: module |
| vgs | Gate-source voltage | pins G |  |
| ptot_tc25 | Power dissipation, TC = 25 degC | UNCHECKED | not a voltage; owner: module |
| ptot_pcb | Power dissipation, PCB-limited | UNCHECKED | not a voltage; owner: module |
| tj_tstg | Operating and storage temperature Tj, Tstg | UNCHECKED | TJ: needs dissipation x RthJA; owner: module (Tstg part: owner: assembly) |
| iec_climatic | IEC climatic category | UNCHECKED | owner: assembly (climatic classification, not an operating voltage or temperature) |
| eas | Avalanche energy, single pulse | UNCHECKED | not a voltage; owner: module |

## Equations

### `conduction_loss`

```
Not a DS equation: conduction loss P = I^2 x RDS(on). Use rds_on at the temperature of interest: 25 degC from the
table (rds_on_10v.max) or a hot curve value (the BSC curve rows rds_on_*c_max below).
i: drain current, A (either sign; squared). rds_on: ohm. Returns: W.
```

Inputs:

- `rds_on` -> `rds_on_10v.max` (typ 3.4 max 4.0 mohm)

### `tj_from_case`

```
Not a DS equation: TJ = TC + P x RthJC, the case-referenced junction temperature (DS RthJC row, Table 3).
tc: case temperature, degC. p: dissipation, W, >= 0. rth_jc: degC/W, use the max row for a bound. Returns: degC.
```

Inputs:

- `rth_jc` -> `rth_jc_bottom.max` (typ 0.5 max 0.9 degC/W)

### `tj_from_ambient`

```
Not a DS equation: TJ = TA + P x RthJA (DS p.3-4 Table 3, device on the DS PCB, 6 cm2 drain copper, footnote).
Valid only for that PCB. ta: ambient temperature, degC. p: dissipation, W, >= 0. rth_ja: degC/W, use the max row.
Returns: degC.
```

Inputs:

- `rth_ja` -> `rth_ja.max` (max 50 degC/W)

### `gate_drive_time`

```
Not a DS equation: time to charge the gate, t = |Qg| / Ig, with Qg from the DS gate-charge table (Table 6) and Ig
the gate drive current (design choice). abs() is applied because a P-channel Qg is printed negative.
qg: C. ig: A, > 0. Returns: s.
```

Inputs:

- `qg` -> `qg.max` (typ 58 max 72 nC)


## Examples

| Call | Computed | Expected | Rel. tol | Result | Cite |
|---|---|---|---|---|---|
| conduction_loss(i=50, rds_on=0.004) | 10 | 10 | 1e-09 | pass | DS p.4 Table 4, RDS(on) max 4.0 mohm at ID = 50 A (arithmetic only) |
| tj_from_ambient(ta=25, p=2.5, rth_ja=50) | 150 | 150 | 1e-09 | pass | DS p.3 Table 2 Ptot = 2.5 W at TA = 25 degC with RthJA = 50 K/W gives Tj = 150 degC, the printed Tj max |
| tj_from_case(tc=25, p=10, rth_jc=0.9) | 34 | 34 | 1e-09 | pass | DS p.3 Table 3 RthJC max 0.9 K/W (arithmetic only) |
| gate_drive_time(qg=7.2e-08, ig=1) | 7.2e-08 | 7.2e-08 | 1e-09 | pass | DS p.4 Table 6 Qg max 72 nC with Ig = 1 A (arithmetic only) |
