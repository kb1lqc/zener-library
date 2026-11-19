<!-- GENERATED - do not edit. Run: python3 -m lib.readme -->

# LTC4364MS

## Datasheet review

[![Human page-image review: 0/83 human](https://img.shields.io/badge/human%20review-0%2F83%20human-lightgrey)](../../../docs/spec/datasheet-review.md)

Human page-image review: 0/83; cross-model audits: 0; manufacturer-export stamps: 0; legacy/unclassified: 0. Text checks are not verification. `lib.check` validates stamp format, not that review occurred.

## Part

- **manufacturer**: Analog Devices
- **description**: Surge stopper with ideal diode, 4-80 V, MSOP-16 (MS); -1 latch-off or -2 auto-retry, C/I/H grade
- **category**: surge_stopper
- **package**: MSOP-16 (MS), LTC DWG 05-08-1669 Rev A
- **datasheet_url**: https://www.analog.com/media/en/technical-documentation/data-sheets/ltc4364-1-4364-2.pdf
- **datasheet_file**: docs/datasheets/ltc4364.pdf
- **datasheet_rev**: Rev. B
- **datasheet_date**: 2023-01
- **kicad_symbol**: LTC4364MS.kicad_sym
- **kicad_footprint**: LTC4364MS.kicad_mod
- **step**: embedded

## Variants

Shared data below applies to every variant unless a row names its variants.

| Value | mpn | alternates | temp_grade | description |
|---|---|---|---|---|
| LTC4364CMS-1 | LTC4364CMS-1#TRPBF | LTC4364CMS-1#PBF | 0 to 70 degC | Surge stopper with ideal diode, MSOP-16 (MS), C grade 0 to 70 degC, -1 latch-off after fault |
| LTC4364IMS-1 | LTC4364IMS-1#TRPBF | LTC4364IMS-1#PBF | -40 to 85 degC | Surge stopper with ideal diode, MSOP-16 (MS), I grade -40 to 85 degC, -1 latch-off after fault |
| LTC4364HMS-1 | LTC4364HMS-1#TRPBF | LTC4364HMS-1#PBF | -40 to 125 degC | Surge stopper with ideal diode, MSOP-16 (MS), H grade -40 to 125 degC, -1 latch-off after fault |
| LTC4364CMS-2 | LTC4364CMS-2#TRPBF | LTC4364CMS-2#PBF | 0 to 70 degC | Surge stopper with ideal diode, MSOP-16 (MS), C grade 0 to 70 degC, -2 auto-retry after cool-down |
| LTC4364IMS-2 | LTC4364IMS-2#TRPBF | LTC4364IMS-2#PBF | -40 to 85 degC | Surge stopper with ideal diode, MSOP-16 (MS), I grade -40 to 85 degC, -2 auto-retry after cool-down |
| LTC4364HMS-2 | LTC4364HMS-2#TRPBF | LTC4364HMS-2#PBF | -40 to 125 degC | Surge stopper with ideal diode, MSOP-16 (MS), H grade -40 to 125 degC, -2 auto-retry after cool-down |

## Pins

| Pin | Name | Type | Function | Cite |
|---|---|---|---|---|
| 1 | OUT | input | Output voltage sense input; drain of the external pass MOSFET M1 | DS p.8, Pin Functions, OUT (Pin 1 MS) |
| 2 | SENSE | input | Current sense input; sense resistor from SENSE to OUT | DS p.8, Pin Functions, SENSE (Pin 2 MS) |
| 3 | NC3 | no_connect | No connection, not internally connected; may be tied to GND or any voltage, open increases clearance | DS p.9, Pin Functions, NC (Pins 3 and 7, MS and S packages) |
| 4 | DGATE | output | Diode controller gate drive output for the ideal diode MOSFET M2 | DS p.8, Pin Functions, DGATE (Pin 4 MS) |
| 5 | SOURCE | input | Common source input and gate drive return; connect to the sources of M1 and M2 | DS p.8, Pin Functions, SOURCE (Pin 5 MS) |
| 6 | HGATE | output | Surge stopper gate drive output for pass MOSFET M1 | DS p.8, Pin Functions, HGATE (Pin 6 MS) |
| 7 | NC7 | no_connect | No connection, not internally connected; may be tied to GND or any voltage, open increases clearance | DS p.9, Pin Functions, NC (Pins 3 and 7, MS and S packages) |
| 8 | VCC | power_in | Positive supply voltage input, 4 V to 80 V normal, -40 V reverse | DS p.9, Pin Functions, VCC (Pin 8 MS) |
| 9 | SHDN | input | Shutdown control input, active low; open is clamped internally to about 4 V | DS p.9, Pin Functions, SHDN (Pin 9 MS) |
| 10 | UV | input | Undervoltage comparator input, 1.25 V threshold; connect to SHDN if unused | DS p.8, Pin Functions, UV (Pin 10 MS) |
| 11 | OV | input | Overvoltage comparator input, 1.25 V threshold; connect to GND if unused | DS p.8, Pin Functions, OV (Pin 11 MS) |
| 12 | GND | power_in | Device ground | DS p.9, Pin Functions, GND (Pin 12 MS) |
| 13 | FLT | open_collector | Fault output, open drain, low on fault warning or overcurrent; can sink 2 mA, withstands 80 V | DS p.9, Pin Functions, FLT (Pin 13 MS) |
| 14 | ENOUT | open_collector | Enable output, open drain, high impedance when OUT is within 0.7 V of VCC; needs pull-up to OUT | DS p.9, Pin Functions, ENOUT (Pin 14 MS) |
| 15 | TMR | passive | Fault timer input; capacitor to GND sets warning, fault and cool-down times | DS p.9, Pin Functions, TMR (Pin 15 MS) |
| 16 | FB | input | Voltage regulator feedback input; resistive divider from OUT; GND disables the clamp | DS p.9, Pin Functions, FB (Pin 16 MS) |

## Parameters: abs_max

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Supply voltage VCC | VCC | -40 (rel. GND) |  | 100 (rel. GND) | V | Note: Reference: DS p.2 header (Notes 1, 2) and DS p.5, Note 2 ('All voltages are referenced to GND unless otherwise specified'). min_ref/max_ref = GND. | DS p.2, Absolute Maximum Ratings, Supply Voltage VCC |  |
| SOURCE, OV, UV, SHDN voltages |  | -40 (rel. GND) |  | 100 (rel. GND) | V | Note: Reference: DS p.2 header (Notes 1, 2) and DS p.5, Note 2 ('All voltages are referenced to GND unless otherwise specified'). min_ref/max_ref = GND. | DS p.2, Absolute Maximum Ratings, SOURCE, OV, UV, SHDN Voltages |  |
| DGATE, HGATE voltages (relative to SOURCE) |  | -0.3 (rel. SOURCE) |  | 10 (rel. SOURCE) | V | Note: Note 3 (DS p.5): internal clamps limit DGATE and HGATE to a minimum of 10 V above SOURCE; driving beyond the clamp may damage the device. | DS p.2, Absolute Maximum Ratings, DGATE, HGATE Voltages (Note 3) SOURCE - 0.3 V to SOURCE + 10 V |  |
| ENOUT, FLT voltages |  | -0.3 (rel. GND) |  | 100 (rel. GND) | V | Note: Conflict inside the DS: abs max row gives 100 V (p.2); pin text DS p.9 says each pin 'can withstand up to 80V', and ILEAK is tested at 80 V (DS p.4). Both stored as printed; the 80 V statement is not an abs max row. Reference: DS p.2 header (Notes 1, 2) and DS p.5, Note 2 ('All voltages are referenced to GND unless otherwise specified'). min_ref/max_ref = GND. | DS p.2, Absolute Maximum Ratings, ENOUT, FLT Voltages |  |
| OUT, SENSE voltages |  | -20 (rel. GND) |  | 100 (rel. GND) | V | Note: Reference: DS p.2 header (Notes 1, 2) and DS p.5, Note 2 ('All voltages are referenced to GND unless otherwise specified'). min_ref/max_ref = GND. | DS p.2, Absolute Maximum Ratings, OUT, SENSE Voltages |  |
| Voltage difference SENSE to OUT |  | -30 (rel. OUT) |  | 30 (rel. OUT) | V | Note: Difference V(SENSE) - V(OUT): the value is SENSE, the reference pin is OUT (DS p.2 row 'Voltage Difference (SENSE to OUT)'); the row names no reference pin beyond the difference. Cite: DS p.2 header (Notes 1, 2). | DS p.2, Absolute Maximum Ratings, Voltage Difference (SENSE to OUT) |  |
| Voltage difference OUT to VCC |  | -100 (rel. VCC) |  | 100 (rel. VCC) | V | Note: Difference V(OUT) - V(VCC): the value is OUT, the reference pin is VCC (DS p.2 row 'Voltage Difference (OUT to VCC)'). Cite: DS p.2 header (Notes 1, 2). | DS p.2, Absolute Maximum Ratings, Voltage Difference (OUT to VCC) |  |
| Voltage difference SENSE to SOURCE |  | -100 (rel. SOURCE) |  | 100 (rel. SOURCE) | V | Note: Difference V(SENSE) - V(SOURCE): the value is SENSE, the reference pin is SOURCE (DS p.2 row 'Voltage Difference (SENSE to SOURCE)'). Cite: DS p.2 header (Notes 1, 2). SENSE is circuit-set (the sense resistor node), so the row is checked on SENSE with SOURCE as the reference; a module that leaves SOURCE undeclared gets UNVERIFIED (docs/spec/extract.md check-row rules). | DS p.2, Absolute Maximum Ratings, Voltage Difference (SENSE to SOURCE) |  |
| FB, TMR voltages |  | -0.3 (rel. GND) |  | 5.5 (rel. GND) | V | Note: Reference: DS p.2 header (Notes 1, 2) and DS p.5, Note 2 ('All voltages are referenced to GND unless otherwise specified'). min_ref/max_ref = GND. | DS p.2, Absolute Maximum Ratings, FB, TMR Voltages |  |
| Operating ambient temperature range, LTC4364H |  | -40 |  | 125 | degC | LTC4364H grade, -40 degC to 125 degC (variants LTC4364HMS-1, LTC4364HMS-2) Variants: LTC4364HMS-1, LTC4364HMS-2. | DS p.2, Absolute Maximum Ratings, Operating Ambient Temperature Range, LTC4364H |  |
| Operating ambient temperature range, LTC4364C |  | 0 |  | 70 | degC | LTC4364C grade, 0 degC to 70 degC (variants LTC4364CMS-1, LTC4364CMS-2) Variants: LTC4364CMS-1, LTC4364CMS-2. | DS p.2, Absolute Maximum Ratings, Operating Ambient Temperature Range, LTC4364C |  |
| Operating ambient temperature range, LTC4364I |  | -40 |  | 85 | degC | LTC4364I grade, -40 degC to 85 degC (variants LTC4364IMS-1, LTC4364IMS-2) Variants: LTC4364IMS-1, LTC4364IMS-2. | DS p.2, Absolute Maximum Ratings, Operating Ambient Temperature Range, LTC4364I |  |
| Storage temperature range |  | -65 |  | 150 | degC |  | DS p.2, Absolute Maximum Ratings, Storage Temperature Range |  |
| Lead temperature, soldering 10 s, MS and SO packages |  |  |  | 300 | degC | Soldering, 10 sec, MS and SO packages | DS p.2, Absolute Maximum Ratings, Lead Temperature (Soldering, 10 sec), MS, SO Packages |  |

## Parameters: electrical

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Operating supply range | VCC | 4 (rel. GND) |  | 80 (rel. GND) | V | Note: Referenced to GND: DS p.5, Note 2, 'All voltages are referenced to GND unless otherwise specified'. | DS p.3, Electrical Characteristics, VCC Operating Supply Range |  |
| Supply current, no fault | ICC |  | 370 | 750 | uA | VCC = SOURCE = SENSE = OUT = 12V, no fault | DS p.3, Electrical Characteristics, ICC |  |
| Supply current in shutdown | ICC(SHDN) |  | 10 | 50 | uA | Shutdown | DS p.3, Electrical Characteristics, ICC(SHDN) |  |
| Reverse input current | ICC(REV) | -10 | 0 |  | uA | VCC = -30V Note: DS prints this negative quantity in magnitude order (MAX column -10); stored in numeric order: printed MAX -> min, printed MIN -> max. | DS p.3, Electrical Characteristics, ICC(REV) |  |
| HGATE gate drive, VHGATE - VSOURCE, VCC = 4 V | dVHGATE | 5 | 7 | 9 | V | VCC = 4V, DGATE Low, IHGATE = 0uA, -1uA | DS p.3, Electrical Characteristics, dVHGATE (row 1) |  |
| HGATE gate drive, VHGATE - VSOURCE, VCC = 8 V to 80 V | dVHGATE | 10 | 12 | 16 | V | VCC = 8V to 80V, DGATE Low, IHGATE = 0uA, -1uA | DS p.3, Electrical Characteristics, dVHGATE (row 2) |  |
| HGATE pull-up current | IHGATE(UP) | -30 | -20 | -10 | uA | VCC = HGATE = DGATE = SOURCE = 12V Note: DS prints this negative quantity in magnitude order (MIN column -10, MAX column -30); stored in numeric order: printed MAX -> min, printed MIN -> max. | DS p.3, Electrical Characteristics, IHGATE(UP) |  |
| HGATE pull-down current, overvoltage | IHGATE(DN) | 60 | 130 |  | mA | Overvoltage: FB = 1.5V, dVHGATE = 5V | DS p.3, Electrical Characteristics, IHGATE(DN), Overvoltage |  |
| HGATE pull-down current, overcurrent | IHGATE(DN) | 60 | 130 |  | mA | Overcurrent: dVSNS = 100mV, dVHGATE = 5V | DS p.3, Electrical Characteristics, IHGATE(DN), Overcurrent |  |
| HGATE pull-down current, shutdown or fault turn-off | IHGATE(DN) | 0.4 | 1 |  | mA | Shutdown/Fault Turn-Off: dVHGATE = 5V | DS p.3, Electrical Characteristics, IHGATE(DN), Shutdown/Fault Turn-Off |  |
| SOURCE input current, normal | ISRC |  | 18 | 40 | uA | VCC = SOURCE = SENSE = OUT = 12V | DS p.3, Electrical Characteristics, ISRC (row 1) |  |
| SOURCE input current, shutdown | ISRC |  | 32 | 90 | uA | VCC = SOURCE = 12V, Shutdown | DS p.3, Electrical Characteristics, ISRC (row 2) |  |
| SOURCE input current, reverse | ISRC | -3.5 | -2.0 |  | mA | VSOURCE = -30V Note: DS prints this negative quantity in magnitude order (MAX column -3.5); stored in numeric order: printed MAX -> min, printed MIN -> max. | DS p.3, Electrical Characteristics, ISRC (row 3) |  |
| FB servo voltage | VFB | 1.22 | 1.25 | 1.28 | V | VCC = 12V to 80V | DS p.3, Electrical Characteristics, VFB |  |
| FB input current | IFB | -1 | 0 | 1 | uA | FB = 1.25V Note: Printed as 0 TYP and +/-1 in the MAX column; stored as symmetric min -1 / max 1. | DS p.3, Electrical Characteristics, IFB |  |
| Overcurrent fault threshold (VSENSE - VOUT), 0 to 125 degC row | dVSNS | 45 | 50 | 55 | mV | VCC = 4V to 80V, OUT = 2.5V to VCC, 0degC to 125degC (partial range, not -40degC) Note: Partial range for the I and H variants: covers 0 to 125 degC only, not -40 degC; use dvsns_full. The C variants override this row to scope full in variants.toml (0 to 125 degC contains the whole C range, 0 to 70 degC). | DS p.3, Electrical Characteristics, dVSNS (row 1) |  |
| Overcurrent fault threshold (VSENSE - VOUT), -40 to 125 degC | dVSNS | 43 | 50 | 57 | mV | VCC = 4V to 80V, OUT = 2.5V to VCC, -40degC to 125degC | DS p.3, Electrical Characteristics, dVSNS (row 2) |  |
| Overcurrent fault threshold (VSENSE - VOUT), OUT low (foldback) | dVSNS | 18 | 25 | 32 | mV | VCC = 4V to 80V, OUT = 0V to 1.5V Note: The row prints no temperature qualifier; the bullet marks it as full range (DS p.3 legend). OUT 1.5 V to 2.5 V is not specified. | DS p.3, Electrical Characteristics, dVSNS (row 3) |  |
| SENSE input current, normal | ISNS |  | 55 | 110 | uA | SENSE = VCC = SOURCE = OUT = 12V | DS p.4, Electrical Characteristics, ISNS (row 1) |  |
| SENSE input current, SENSE = -15 V | ISNS | -4 | -2 |  | mA | SENSE = -15V Note: DS prints this negative quantity in magnitude order (MAX column -4); stored in numeric order: printed MAX -> min, printed MIN -> max. | DS p.4, Electrical Characteristics, ISNS (row 2) |  |
| TMR pull-up current, overvoltage, VCC - OUT = 0.5 V | ITMR(UP) | -3 | -2.2 | -1.3 | uA | TMR = 1V, FB = 1.5V, VCC - OUT = 0.5V Note: DS prints this negative quantity in magnitude order (MIN column -1.3, MAX column -3); stored in numeric order: printed MAX -> min, printed MIN -> max. | DS p.4, Electrical Characteristics, ITMR(UP) Overvoltage (row 1) |  |
| TMR pull-up current, overvoltage, VCC - OUT = 75 V | ITMR(UP) | -60 | -50 | -40 | uA | TMR = 1V, FB = 1.5V, VCC - OUT = 75V Note: DS prints this negative quantity in magnitude order (MIN column -40, MAX column -60); stored in numeric order: printed MAX -> min, printed MIN -> max. | DS p.4, Electrical Characteristics, ITMR(UP) Overvoltage (row 2) |  |
| TMR pull-up current, overcurrent, VCC - OUT = 0.5 V | ITMR(UP) | -14 | -10 | -6 | uA | TMR = 1V, dVSNS = 60mV, VCC - OUT = 0.5V Note: DS prints this negative quantity in magnitude order (MIN column -6, MAX column -14); stored in numeric order: printed MAX -> min, printed MIN -> max. | DS p.4, Electrical Characteristics, ITMR(UP) Overcurrent (row 1) |  |
| TMR pull-up current, overcurrent, VCC - OUT = 75 V | ITMR(UP) | -310 | -260 | -210 | uA | TMR = 1V, dVSNS = 60mV, VCC - OUT = 75V Note: DS prints this negative quantity in magnitude order (MIN column -210, MAX column -310); stored in numeric order: printed MAX -> min, printed MIN -> max. | DS p.4, Electrical Characteristics, ITMR(UP) Overcurrent (row 2) |  |
| TMR pull-up current, warning | ITMR(UP) | -7 | -5 | -3 | uA | TMR = 1.3V, FB = 1.5V, VCC - OUT = 0.5V Note: DS prints this negative quantity in magnitude order (MIN column -3, MAX column -7); stored in numeric order: printed MAX -> min, printed MIN -> max. | DS p.4, Electrical Characteristics, ITMR(UP) Warning |  |
| TMR pull-up current, retry and cool-down | ITMR(UP) | -3 | -2 | -1.3 | uA | TMR = 1V, FB = 1.5V Note: OPEN ITEM: DS Figure 4 caption says 'LTC4364-2 Only' but the p.15 text says the -1 also generates these cool-down TMR pulses; the text is followed. DS prints this negative quantity in magnitude order (MIN column -1.3, MAX column -3); stored in numeric order: printed MAX -> min, printed MIN -> max. Shared by all six variants: the -1 cool-down pulses (DS p.15, Figure 4) use the same charge current; the -2 restart uses it too. | DS p.4, Electrical Characteristics, ITMR(UP) Retry |  |
| TMR pull-down current, retry and cool-down | ITMR(DN) | 1.1 | 2 | 2.7 | uA | TMR = 1V, FB = 1.5V, Retry Note: OPEN ITEM: DS Figure 4 caption says 'LTC4364-2 Only' but the p.15 text says the -1 also generates these cool-down TMR pulses; the text is followed. Shared by all six variants: DS p.15, the -1 generates the same cool-down TMR pulses (Figure 4) and then latches, so this current is used for -1 as well. Used by calc.t_cool (i_cycle). | DS p.4, Electrical Characteristics, ITMR(DN) Retry |  |
| TMR pull-down current, shutdown | ITMR(DN) | 0.3 | 0.75 | 1.5 | mA | Shutdown | DS p.4, Electrical Characteristics, ITMR(DN) Shutdown |  |
| TMR fault threshold (FLT falls) | VTMR(F) | 1.22 | 1.25 | 1.28 | V | FLT falling, VCC = 4V to 80V | DS p.4, Electrical Characteristics, VTMR(F) |  |
| TMR gate-off threshold (HGATE falls) | VTMR(G) | 1.32 | 1.35 | 1.38 | V | HGATE falling, VCC = 4V to 80V | DS p.4, Electrical Characteristics, VTMR(G) |  |
| TMR retry threshold, 32nd crossing (0.15 V; HGATE rises only for -2) | VTMR(R) | 0.125 | 0.15 | 0.175 | V | HGATE rising (after 32 cycles), VCC = 4V to 80V Note: OPEN ITEM: DS Figure 4 caption says 'LTC4364-2 Only' but the p.15 text says the -1 also generates these cool-down TMR pulses; the text is followed. Shared by all six variants. Restart by HGATE rising at this crossing is the -2 function (DS p.14, p.15). The -1 also runs the 32 cool-down cycles that reach 0.15 V (DS p.15, Figure 4), so the threshold applies to -1 too. Used by calc.t_cool (dv_cycle = VTMR(G) - VTMR(R)). | DS p.4, Electrical Characteristics, VTMR(R) |  |
| Early warning timer window | dVTMR | 75 | 100 | 125 | mV | VTMR(G) - VTMR(F), VCC = 4V to 80V | DS p.4, Electrical Characteristics, Early Warning Timer Window |  |
| UV input threshold (falling) | VUV | 1.22 | 1.25 | 1.28 | V | UV falling, VCC = 4V to 80V | DS p.4, Electrical Characteristics, VUV |  |
| UV input hysteresis | VUV(HYST) | 25 | 50 | 80 | mV |  | DS p.4, Electrical Characteristics, VUV(HYST) |  |
| UV reset threshold (LTC4364-1 only) | VUV(RST) | 0.5 | 0.6 | 0.7 | V | UV falling, VCC = 4V to 80V, LTC4364-1 only Variants: LTC4364CMS-1, LTC4364IMS-1, LTC4364HMS-1. Note: Restricted to the -1 variants (DS p.4, 'LTC4364-1 Only'). Pulling UV below 0.6 V resets the latch (DS p.9, p.11). | DS p.4, Electrical Characteristics, VUV(RST) |  |
| OV input threshold (rising) | VOV | 1.22 | 1.25 | 1.28 | V | OV rising, VCC = 4V to 80V | DS p.4, Electrical Characteristics, VOV |  |
| OV input hysteresis | VOV(HYST) |  | 12 |  | mV | Note: Unmarked row (25 degC). Typical only; no MIN or MAX printed. | DS p.4, Electrical Characteristics, VOV(HYST) |  |
| UV, OV input current at threshold | IIN | -1 | 0 | 1 | uA | UV, OV = 1.25V Note: Printed 0 TYP and +/-1 in the MAX column; stored as symmetric min -1 / max 1. | DS p.4, Electrical Characteristics, IIN (row 1) |  |
| UV, OV input current at -30 V | IIN | -0.6 | -0.3 |  | mA | UV, OV = -30V Note: DS prints this negative quantity in magnitude order (MAX column -0.6); stored in numeric order: printed MAX -> min, printed MIN -> max. | DS p.4, Electrical Characteristics, IIN (row 2) |  |
| ENOUT, FLT output low at 0.25 mA | VOL |  | 0.1 | 0.3 | V | ISINK = 0.25mA | DS p.4, Electrical Characteristics, VOL (row 1) |  |
| ENOUT, FLT output low at 2 mA | VOL |  | 0.5 | 1.3 | V | ISINK = 2mA | DS p.4, Electrical Characteristics, VOL (row 2) |  |
| ENOUT, FLT leakage current | ILEAK | -2.5 | 0 | 2.5 | uA | ENOUT, FLT = 80V Note: Printed 0 TYP and +/-2.5 in the MAX column; stored as symmetric min -2.5 / max 2.5. | DS p.4, Electrical Characteristics, ILEAK |  |
| OUT high threshold, VCC - VOUT (ENOUT goes high impedance) | dVOUT(TH) | 0.4 | 0.7 | 1 | V | ENOUT from Low to High | DS p.4, Electrical Characteristics, dVOUT(TH) |  |
| OUT reset threshold (ENOUT latch resets) | VOUT(RST) | 1.4 | 2.2 | 3 | V | ENOUT from High to Low | DS p.4, Electrical Characteristics, VOUT(RST) |  |
| OUT input current, normal | IOUT |  | 40 | 80 | uA | VCC = OUT = 12V, SHDN open | DS p.4, Electrical Characteristics, IOUT (row 1) |  |
| OUT input current, OUT = -15 V | IOUT | -8 | -4 |  | mA | OUT = -15V Note: DS prints this negative quantity in magnitude order (MAX column -8); stored in numeric order: printed MAX -> min, printed MIN -> max. | DS p.4, Electrical Characteristics, IOUT (row 2) |  |
| Output current in shutdown, ISNS + IOUT |  |  | 12 | 40 | uA | VCC = SOURCE = SENSE = OUT = 12V, Shutdown | DS p.4, Electrical Characteristics, Output Current in Shutdown, ISNS + IOUT |  |
| SHDN input threshold | VSHDN | 0.5 | 1.6 | 2.2 | V | VCC = 4V to 80V | DS p.4, Electrical Characteristics, VSHDN |  |
| SHDN pin float voltage | VSHDN(FLT) | 2.3 | 4 | 6.5 | V | VCC = 12V to 80V | DS p.4, Electrical Characteristics, VSHDN(FLT) |  |
| SHDN input current, SHDN = 0.5 V | ISHDN |  | -3.3 | -1 | uA | SHDN = 0.5V Note: DS prints this negative quantity in magnitude order (MIN column -1); stored in numeric order: printed MAX -> min, printed MIN -> max. | DS p.4, Electrical Characteristics, ISHDN (row 1) |  |
| SHDN maximum allowable leakage, VCC = 4 V | ISHDN |  | -1.5 |  | uA | Maximum Allowable Leakage, VCC = 4V Note: Unmarked row (25 degC). Printed in the TYP column but labelled 'Maximum Allowable Leakage': this is a limit on EXTERNAL leakage on SHDN, not a typical device value. Supporting text: DS p.9, SHDN pin function, leakage current to ground at the pin should be limited to no more than 1 uA if no pull-up device is used. The table value (1.5 uA, DS p.4) and the p.9 text (1 uA) differ: open item. Not used as a device bound. | DS p.4, Electrical Characteristics, ISHDN (row 2) |  |
| SHDN input current, SHDN = -30 V | ISHDN | -300 | -120 |  | uA | SHDN = -30V Note: DS prints this negative quantity in magnitude order (MAX column -300); stored in numeric order: printed MAX -> min, printed MIN -> max. | DS p.4, Electrical Characteristics, ISHDN (row 3) |  |
| Retry duty cycle, overvoltage (LTC4364-2 function) |  |  | 0.125 | 0.2 | % | FB = 1.5V, VCC = 80V, OUT = 16V Variants: LTC4364CMS-2, LTC4364IMS-2, LTC4364HMS-2. Note: Auto-retry duty cycle, overvoltage. Restricted to the -2 variants: the -1 latches and does not retry (DS p.15; feature 0.1 % retry duty cycle, DS p.1, LTC4364-2). | DS p.4, Electrical Characteristics, D, Retry Duty Cycle, Overvoltage |  |
| Retry duty cycle, output short (LTC4364-2 function) |  |  | 0.075 | 0.12 | % | dVSNS = 60mV, VCC - OUT = 12V Variants: LTC4364CMS-2, LTC4364IMS-2, LTC4364HMS-2. Note: Auto-retry duty cycle, output short. Restricted to the -2 variants: the -1 latches and does not retry (DS p.15; DS p.1, LTC4364-2). | DS p.4, Electrical Characteristics, D, Retry Duty Cycle, Output Short |  |
| Undervoltage to HGATE low propagation delay | tOFF,HGATE(UV) |  | 1.3 | 4 | us | UV steps from 1.5V to 1V | DS p.4, Electrical Characteristics, tOFF,HGATE(UV) |  |
| Overvoltage to HGATE low propagation delay | tOFF,HGATE(OV) |  | 0.25 | 1 | us | FB steps from 1V to 1.5V | DS p.4, Electrical Characteristics, tOFF,HGATE(OV) |  |
| Overcurrent to HGATE low propagation delay | tOFF,HGATE(OC) |  | 0.5 | 2 | us | dVSNS steps from 0mV to 150mV, OUT = 0V | DS p.4, Electrical Characteristics, tOFF,HGATE(OC) |  |
| DGATE gate drive, VDGATE - VSOURCE, VCC = 4 V | dVDGATE | 5 | 8.5 | 12 | V | VCC = 4V, IDGATE = 0uA, -1uA, Fully On | DS p.5, Electrical Characteristics, Ideal Diode, dVDGATE (row 1) |  |
| DGATE gate drive, VDGATE - VSOURCE, VCC = 8 V to 80 V | dVDGATE | 10 | 12 | 16 | V | VCC = 8V to 80V, IDGATE = 0uA, -1uA, Fully On | DS p.5, Electrical Characteristics, Ideal Diode, dVDGATE (row 2) |  |
| DGATE pin pull-up current | IDGATE(UP) | -15 | -10 | -5 | uA | DGATE = SOURCE = VCC = 12V, dVSD = 0.1V Note: DS prints this negative quantity in magnitude order (MIN column -5, MAX column -15); stored in numeric order: printed MAX -> min, printed MIN -> max. | DS p.5, Electrical Characteristics, Ideal Diode, IDGATE(UP) |  |
| DGATE pin pull-down current, reverse current | IDGATE(DN) | 60 | 130 |  | mA | dVDGATE = 5V, dVSD = -0.2V | DS p.5, Electrical Characteristics, Ideal Diode, IDGATE(DN) (row 1) |  |
| DGATE pin pull-down current, shutdown or fault turn-off | IDGATE(DN) | 0.4 | 1 |  | mA | dVDGATE = 5V, Shutdown/Fault Turn-Off | DS p.5, Electrical Characteristics, Ideal Diode, IDGATE(DN) (row 2) |  |
| Ideal diode regulation voltage, VCC = SOURCE = 12 V | dVSD | 10 | 30 | 45 | mV | dVDGATE = 2.5V, VCC = SOURCE = 12V | DS p.5, Electrical Characteristics, Ideal Diode, dVSD (row 1) |  |
| Ideal diode regulation voltage, VCC = SOURCE = 4 V | dVSD | 24 | 48 | 72 | mV | dVDGATE = 2.5V, VCC = SOURCE = 4V | DS p.5, Electrical Characteristics, Ideal Diode, dVSD (row 2) |  |
| DGATE turn-off propagation delay | tOFF(DGATE) |  | 0.35 | 1.5 | us | dVSD steps from 0.1V to -1V | DS p.5, Electrical Characteristics, Ideal Diode, tOFF(DGATE) |  |

## Parameters: thermal

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Thermal resistance, junction to ambient, MS package | thetaJA |  | 120 |  | degC/W | Board and test method not stated in the DS Note: Printed as a plain value with no MIN/TYP/MAX label; stored as typ. Not a guaranteed bound. Board condition not stated. Unit degC/W is not in the SPEC units list; loader must add it. | DS p.2, Pin Configuration, MS package, theta JA |  |
| Maximum junction temperature, MS package | TJMAX |  |  | 150 | degC |  | DS p.2, Pin Configuration, MS package, TJMAX |  |

## Variant-specific parameters: LTC4364CMS-1

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Overcurrent fault threshold (VSENSE - VOUT), 0 to 125 degC row | dVSNS | 45 | 50 | 55 | mV | VCC = 4V to 80V, OUT = 2.5V to VCC, 0degC to 125degC Note: C grade: scope full. The 0 to 125 degC row contains the whole C range (0 to 70 degC), so for this variant it is full-range data (SPEC scope full). Not used by calc INPUTS, which use dvsns_full (valid for every grade). | DS p.3, Electrical Characteristics, dVSNS (row 1) |  |

## Variant-specific parameters: LTC4364CMS-2

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Overcurrent fault threshold (VSENSE - VOUT), 0 to 125 degC row | dVSNS | 45 | 50 | 55 | mV | VCC = 4V to 80V, OUT = 2.5V to VCC, 0degC to 125degC Note: C grade: scope full. The 0 to 125 degC row contains the whole C range (0 to 70 degC), so for this variant it is full-range data (SPEC scope full). Not used by calc INPUTS, which use dvsns_full (valid for every grade). | DS p.3, Electrical Characteristics, dVSNS (row 1) |  |

## Limits of this data

Rows by scope: 25C 2, full 64, na 16, partial 1 (25C rows hold only at 25 degC). Curve (graph) rows: 0. Text rows: 0.

## Zener checks

Generated wrapper: `<Variant>.zen` (`python3 -m lib.zen`). abs_max and rec_op rows are errors (abs_max x derate); 25C and partial rows are waivable warnings; a checked net with no voltage is UNVERIFIED.

| Param | Name | Checked against | Not checked / reason |
|---|---|---|---|
| abs_vcc | Supply voltage VCC | pins VCC |  |
| abs_source_ov_uv_shdn | SOURCE, OV, UV, SHDN voltages | pins OV, UV, SHDN, SOURCE |  |
| abs_dgate_hgate | DGATE, HGATE voltages (relative to SOURCE) | UNCHECKED | DGATE and HGATE are driven by the part (internally clamped); owner: module |
| abs_enout_flt | ENOUT, FLT voltages | pins ENOUT, FLT |  |
| abs_out_sense | OUT, SENSE voltages | pins OUT, SENSE |  |
| abs_sense_out | Voltage difference SENSE to OUT | pins SENSE |  |
| abs_out_vcc | Voltage difference OUT to VCC | pins OUT |  |
| abs_sense_source | Voltage difference SENSE to SOURCE | pins SENSE |  |
| abs_fb_tmr | FB, TMR voltages | pins FB | TMR not checked: timer capacitor node driven by the part; owner: module |
| ta_h | Operating ambient temperature range, LTC4364H | board ambient |  |
| ta_c | Operating ambient temperature range, LTC4364C | board ambient |  |
| ta_i | Operating ambient temperature range, LTC4364I | board ambient |  |
| tstg | Storage temperature range | UNCHECKED | owner: assembly |
| t_lead | Lead temperature, soldering 10 s, MS and SO packages | UNCHECKED | owner: assembly |
| vcc_op | Operating supply range | pins VCC |  |

### Zener checks: variant LTC4364CMS-1

No Zener checks declared.

### Zener checks: variant LTC4364CMS-2

No Zener checks declared.

## Equations

### `rsns`

```
RSNS = dVSNS / ILIM. DS p.12, Overcurrent Fault, equation; DS p.19, Design Example.
INPUTS uses dvsns_full (min 43 mV, -40 to 125 degC): its range contains the C (0 to 70 degC), I (-40 to 85 degC)
and H (-40 to 125 degC) grade ranges, so it is valid for all six variants. The DS design example (p.19) uses the
0-125 degC 45 mV row (dvsns_0c125c), which is full-range data for the C variants only.
dvsns: overcurrent sense threshold, V. ilim: desired current limit, A. Returns: ohm.
```

Inputs:

- `dvsns` -> `dvsns_full` (min 43 typ 50 max 57 mV)

### `vreg`

```
VREG = VFB * (R7 + R8) / R8 + iin * R7. Output clamp regulated by the FB divider OUT-R7-FB-R8-GND.
DS p.19, Design Example (VREG = 1.25 V (R7 + R8)/R8); FB divider Figure 1 (DS p.12); VFB DS p.3.
With iin != 0 this is Not a DS equation: adds the IFB (DS p.3) error through the divider's Thevenin resistance.
Derivation: KCL at FB (f): (VOUT - f)/R7 = f/R8 + iin, with iin the current drawn out of the FB pin. Solve for VOUT
with f = VFB: VOUT = VFB (R7+R8)/R8 + iin R7. The node Thevenin resistance is R7||R8; the node error iin*R7||R8
referred to VOUT is multiplied by (R7+R8)/R8, giving iin*R7.
r7: OUT to FB, ohm. r8: FB to GND, ohm. vfb: FB servo voltage, V. iin: FB pin current, A, positive into the pin.
Returns: VREG, V.
INPUTS: vfb -> vfb, iin -> ifb (FB = 1.25 V, min -1 uA, max 1 uA).
```

Inputs:

- `vfb` -> `vfb` (min 1.22 typ 1.25 max 1.28 V)
- `iin` -> `ifb` (min -1 typ 0 max 1 uA)

### `r7_for_vreg`

```
R7 = (VREG - VFB) * R8 / VFB, the solved form of vreg() without iin. DS p.19, Design Example
(R7 = (27V - 1.25V) * R8 / 1.25V = 102.8k). vreg_target: V. r8: ohm. vfb: V. Returns: ohm.
```

Inputs:

- `vfb` -> `vfb` (min 1.22 typ 1.25 max 1.28 V)

### `vin_uv`

```
VIN falling UV trip = VTH * (R1+R2+R3)/(R2+R3) + iin * R1 + iin_ov * R1 * R3/(R2+R3).
Divider VIN-R1-UV-R2-OV-R3-GND. DS p.19, Design Example (6V / (R1+R2+R3) = 1.25V / (R2+R3)); Figure 1, UV = 6 V
(DS p.12). With iin != 0 or iin_ov != 0 this is Not a DS equation: adds the IIN (DS p.4) error through the
divider's Thevenin resistance.
Derivation: pin currents are positive into the pin, so they leave the divider node. KCL at UV (u) and OV (o):
  (VIN - u)/R1 = (u - o)/R2 + iin
  (u - o)/R2   = o/R3 + iin_ov
Eliminating o gives u = [VIN - R1*iin - R1*iin_ov*R3/(R2+R3)] * (R2+R3)/(R1+R2+R3). Setting u = VTH and solving
for VIN gives the formula. The UV-node Thevenin resistance is Rth = R1*(R2+R3)/(R1+R2+R3), so the UV-node error is
iin*Rth; referred to VIN (multiply by (R1+R2+R3)/(R2+R3)) it is iin*R1.
Rising trip (the turn-on point): pass vth = VUV + VUV(HYST), i.e. keys vuv + vuv_hyst (DS p.13: UV must rise above
the UV threshold plus the hysteresis). Keys: vuv (falling, DS p.4) and vuv_hyst (DS p.4).
r1, r2, r3: ohm. vth: V. iin: UV pin current, A. iin_ov: OV pin current, A. Returns: V.
INPUTS: vth -> vuv (falling trip), iin -> iin_uvov_pos (UV at 1.25 V), iin_ov -> iin_uvov_pos (OV at 1.25 V).
```

Inputs:

- `vth` -> `vuv` (min 1.22 typ 1.25 max 1.28 V)
- `iin` -> `iin_uvov_pos` (min -1 typ 0 max 1 uA)
- `iin_ov` -> `iin_uvov_pos` (min -1 typ 0 max 1 uA)

### `vin_ov`

```
VIN rising OV trip = VTH * (R1+R2+R3)/R3 + iin * (R1+R2) + iin_uv * R1.
DS p.19, Design Example (60V / (R1+R2+R3) = 1.25V / R3); Figure 1, OV = 60 V (DS p.12).
With iin != 0 or iin_uv != 0 this is Not a DS equation: adds the IIN (DS p.4) error through the divider's Thevenin
resistance.
Derivation (same KCL as vin_uv, with the OV node o = VTH): from the OV node, u = o (R2+R3)/R3 + iin * R2, where
iin is the OV pin current. Then VIN = u (R1+R2+R3)/(R2+R3) + iin * R1 R3/(R2+R3) + iin_uv * R1, with iin_uv the UV
pin current. Substituting u: the iin coefficient is R2 (R1+R2+R3)/(R2+R3) + R1 R3/(R2+R3) = R1 + R2.
r1, r2, r3: ohm. vth: OV threshold, V. iin: OV pin current, A. iin_uv: UV pin current, A. Returns: V.
INPUTS: vth -> vov, iin -> iin_uvov_pos (OV at 1.25 V), iin_uv -> iin_uvov_pos (UV at 1.25 V).
```

Inputs:

- `vth` -> `vov` (min 1.22 typ 1.25 max 1.28 V)
- `iin` -> `iin_uvov_pos` (min -1 typ 0 max 1 uA)
- `iin_uv` -> `iin_uvov_pos` (min -1 typ 0 max 1 uA)

### `uv_ov_r2`

```
R2 = (VOV / VUV - 1) * R3. DS p.19, Design Example (R2 = (60V/6V - 1) * R3 = 90k). vuv, vov: target trip
points, V (design choices). r3: ohm. Returns: ohm. INPUTS: none (design choices).
```

Inputs:


### `uv_r1`

```
R1 = (VUV / VTH - 1) * (R2 + R3). DS p.19, Design Example (R1 = (6V/1.25V - 1) * (R2+R3) = 380k).
vuv: target falling trip, V. vth: UV threshold, V. r2, r3: ohm. Returns: ohm.
INPUTS: vth -> vuv (falling UV threshold, typ 1.25 V).
```

Inputs:

- `vth` -> `vuv` (min 1.22 typ 1.25 max 1.28 V)

### `c_tmr_for_warning`

```
CTMR = tWARNING * |ITMR(UP,warn)| / dVTMR. DS p.19, Design Example (1 ms * 5 uA / 100 mV = 50 nF), solved from
the DS p.14 equation tWARNING = CTMR * 100 mV / 5 uA. i_warn is the stored signed current: abs() is applied, so a
negative param gives a positive capacitance. t_warn: s (design choice). dv_warn: V. Returns: F.
INPUTS: i_warn -> itmr_up_warn (DS p.4, typ -5 uA), dv_warn -> dvtmr (DS p.4, typ 100 mV).
```

Inputs:

- `i_warn` -> `itmr_up_warn` (min -7 typ -5 max -3 uA)
- `dv_warn` -> `dvtmr` (min 75 typ 100 max 125 mV)

### `t_warning`

```
tWARNING = CTMR * dVTMR / |ITMR(UP,warn)|. DS p.14, Fault Timer equation (100 mV / 5 uA): the interval between
FLT asserting and HGATE turn-off. abs() is applied to i_warn, so a negative stored param works.
ctmr: F (design choice). i_warn: A, signed. dv_warn: V. Returns: s.
INPUTS: i_warn -> itmr_up_warn, dv_warn -> dvtmr.
```

Inputs:

- `i_warn` -> `itmr_up_warn` (min -7 typ -5 max -3 uA)
- `dv_warn` -> `dvtmr` (min 75 typ 100 max 125 mV)

### `itmr_up_ov_typ`

```
ITMR(UP)OV = 2 uA + 0.644 uA/V * (VCC - VOUT - 0.5 V). DS p.14, Fault Timer, overvoltage fault timer current
(fit to Figure 3a). TYPICAL curve fit: never a worst-case bound. The guaranteed points are the DS p.4 rows
itmr_up_ov_lo (VCC-OUT = 0.5 V, min -1.3 max -3 uA as printed, stored as min -3 max -1.3 uA) and itmr_up_ov_hi
(VCC-OUT = 75 V, stored min -60 max -40 uA). dv = VCC - VOUT, V. Returns: A (positive). INPUTS: none (dv is an
operating condition).
```

Inputs:


### `itmr_up_oc_typ`

```
ITMR(UP)OC = 10 uA + 3.36 uA/V * (VCC - VOUT - 0.5 V). DS p.14, overcurrent fault timer current (fit to
Figure 3b). TYPICAL curve fit: never a worst-case bound. The guaranteed points are the DS p.4 rows itmr_up_oc_lo
(VCC-OUT = 0.5 V) and itmr_up_oc_hi (VCC-OUT = 75 V). dv = VCC - VOUT, V. Returns: A (positive).
INPUTS: none (dv is an operating condition).
```

Inputs:


### `t_flt`

```
Time to FLT asserting = CTMR * VTMR(F) / |ITMR(UP)|. DS p.14 (first term of tOV); Figure 3 labels tFLT.
abs() is applied to i_up. ctmr: F (design choice). i_up: A, signed. vtmr_f: FLT threshold, V. Returns: s.
INPUTS: i_up -> itmr_up_ov_hi (overvoltage, VCC-OUT = 75 V row). For overcurrent use itmr_up_oc_hi, or
itmr_up_ov_lo/itmr_up_oc_lo for VCC-OUT = 0.5 V; the caller picks the row for the operating point.
vtmr_f -> vtmr_f.
```

Inputs:

- `i_up` -> `itmr_up_ov_hi` (min -60 typ -50 max -40 uA)
- `vtmr_f` -> `vtmr_f` (min 1.22 typ 1.25 max 1.28 V)

### `t_ov`

```
tOV = CTMR * VTMR(F) / |ITMR(UP)OV| + CTMR * dVTMR / |ITMR(UP)warn|. DS p.14, overvoltage fault: time from the
start of the fault to HGATE turn-off (time to FLT plus the warning window). abs() is applied to both currents.
ctmr: F (design choice). i_up_ov: A, signed. i_warn: A, signed. vtmr_f: V. dv_warn: V. Returns: s.
INPUTS: i_up_ov -> itmr_up_ov_hi (75 V row; see t_flt for other rows), i_warn -> itmr_up_warn, vtmr_f -> vtmr_f,
dv_warn -> dvtmr.
```

Inputs:

- `i_up_ov` -> `itmr_up_ov_hi` (min -60 typ -50 max -40 uA)
- `i_warn` -> `itmr_up_warn` (min -7 typ -5 max -3 uA)
- `vtmr_f` -> `vtmr_f` (min 1.22 typ 1.25 max 1.28 V)
- `dv_warn` -> `dvtmr` (min 75 typ 100 max 125 mV)

### `t_oc`

```
tOC = CTMR * VTMR(G) / |ITMR(UP)OC|. DS p.14, overcurrent fault time to HGATE turn-off (the timer current is not
reduced to 5 uA after FLT in overcurrent). abs() is applied to i_up_oc. ctmr: F (design choice). i_up_oc: A, signed.
vtmr_g: TMR gate-off threshold, V. Returns: s.
INPUTS: i_up_oc -> itmr_up_oc_hi (75 V row), vtmr_g -> vtmr_g.
```

Inputs:

- `i_up_oc` -> `itmr_up_oc_hi` (min -310 typ -260 max -210 uA)
- `vtmr_g` -> `vtmr_g` (min 1.32 typ 1.35 max 1.38 V)

### `t_cool`

```
tCOOL = 63 * CTMR * 1.2 V / 2 uA. DS p.15, Cool Down Period and Restart. The TMR pin cycles 32 times between
0.15 V and 1.35 V (DS p.14); the 63 is as printed. The -1 option also runs these cool-down cycles and then latches
(DS p.15), so this applies to -1. abs() is applied to i_cycle. ctmr: F (design choice). i_cycle: A, 2 uA printed as
typical (DS p.14, p.15); the guaranteed retry-function rows are itmr_dn_retry (1.1 to 2.7 uA) and itmr_up_retry
(-1.3 to -3 uA). dv_cycle: V, 1.2 V printed (= VTMR(G) - VTMR(R) nominal: keys vtmr_g and vtmr_r). Returns: s.
INPUTS: i_cycle -> itmr_dn_retry (discharge leg), i_up -> itmr_up_retry (charge leg).
With i_up given this is Not a DS equation: the 63 legs are split evenly between the discharge current i_cycle
and the charge current i_up, tCOOL = 63/2 * CTMR * dv_cycle * (1/|i_cycle| + 1/|i_up|), so worst case uses both
guaranteed currents. The DS does not state the split; with i_up == i_cycle it equals the DS equation.
```

Inputs:

- `i_cycle` -> `itmr_dn_retry` (min 1.1 typ 2 max 2.7 uA)
- `i_up` -> `itmr_up_retry` (min -3 typ -2 max -1.3 uA)

### `c_hgate_for_inrush`

```
CHG = |IHGATE(UP)| * CL / IINRUSH. HGATE-to-GND capacitor for a target inrush current. DS p.17, Limiting Inrush
Current. abs() is applied to i_hgate_up (stored negative). i_inrush: A (design choice). c_load: F (design choice).
Returns: F. The DS minimum of 6.8 nF (DS p.8, HGATE pin) is a separate requirement and is not applied here.
INPUTS: i_hgate_up -> ihgate_up (DS p.3, typ -20 uA).
```

Inputs:

- `i_hgate_up` -> `ihgate_up` (min -30 typ -20 max -10 uA)

### `r4_max`

```
R4 <= (VIN(min) - VCC(min)) / ICC(max). Series resistor so VCC stays at or above 4 V. DS p.19, Design Example
(R4 = (6V - 4V) / 0.75 mA = 2.7k). vin_min: V (design choice). vcc_min: V. icc_max: A. Returns: ohm (maximum).
INPUTS: vcc_min -> vcc_op (min 4 V), icc_max -> icc (max 750 uA).
```

Inputs:

- `vcc_min` -> `vcc_op.min` (min 4 (rel. GND) max 80 (rel. GND) V)
- `icc_max` -> `icc.max` (typ 370 max 750 uA)

### `i_d1_peak`

```
I(D1,PK) = (VIN(max) - VZ(min)) / R4. Transient current in the VCC clamp Zener. DS p.19, Design Example
((200V - 64V) / 2.2k = 62 mA). vin_max: V (design choice). vz_min: Zener minimum voltage, V (external part, not in
this component). r4: ohm. Returns: A. INPUTS: none.
```

Inputs:


### `p_m1_oc`

```
P = dVDS(M1) * dVSNS(MAX) / RSNS. Power in M1 during an overcurrent limit. DS p.20, Design Example
(14 V * 32 mV / 10 mohm = 45 W; 12 V * 55 mV / 10 mohm = 66 W). vds: VCC - OUT, V (operating point). dvsns: V.
rsns_ohm: ohm. Returns: W. INPUTS: dvsns -> dvsns_full (max 57 mV at H grade).
```

Inputs:

- `dvsns` -> `dvsns_full` (min 43 typ 50 max 57 mV)

### `rdson_m2_max`

```
RDS(ON) <= VFW / ILOAD(MAX). Ideal diode MOSFET M2 on-resistance for a forward drop VFW. DS p.20, MOSFET
Selection (0.25 V / 5.5 A = 45.5 mohm). vfw, i_load_max: design choices. Returns: ohm. INPUTS: none.
```

Inputs:


### `p2t_simple`

```
P^2t = 1/2 * ILOAD^2 * (VPK - VREG)^2 * tau. Simplified transient stress for VREG ~ VIN and tau >> tr.
DS p.17, Calculating Transient Stress (18.4 W^2 s for 3 A, 80 V, 16 V, 1 ms). All arguments are design or
transient-waveform choices. i_load: A. vpk, vreg_v: V. tau: s. Returns: W^2 s. INPUTS: none.
```

Inputs:


### `p2t_transient`

```
P^2t = ILOAD^2 * [ (1/3) * tr * (b-a)^3 / b + (1/2) * tau * (2 a^2 ln(b/a) + 3 a^2 + b^2 - 4 a b) ] with
a = VREG - VIN, b = VPK - VIN, for the linear-rise, exponential-decay transient of DS Figure 5. DS p.16,
Calculating Transient Stress. All arguments are waveform or design choices. i_load: A. tr: rise time, s.
tau: decay time constant, s. vpk, vin, vreg_v: V. Returns: W^2 s. Needs VIN < VREG < VPK. INPUTS: none.
```

Inputs:


### `p2t_short`

```
P^2t = (VIN * dVSNS / RSNS)^2 * tOC. Short-circuit stress on M1. DS p.17, Short-Circuit Stress
(15 V, 25 mV, 12 mohm, 100 nF gives 2.2 W^2 s). vin: V (operating point). dvsns: V. rsns_ohm: ohm. t_oc_s: s, the
output of t_oc(). Returns: W^2 s. INPUTS: dvsns -> dvsns_full.
```

Inputs:

- `dvsns` -> `dvsns_full` (min 43 typ 50 max 57 mV)

### `tau_parallel_rc`

```
tau = (R_a || R_b) * C, the UV/OV start-up RC used for the tau_UV / tau_OV skew. DS p.13, Figure 2
(tau_UV = (383k || 100k) * 10 nF, tau_OV = (475k || 10k) * 1 nF; DS requires tau_UV / tau_OV > 50).
r_a, r_b: ohm. c: F. Returns: s. INPUTS: none.
```

Inputs:



## Examples

| Call | Computed | Expected | Rel. tol | Result | Cite |
|---|---|---|---|---|---|
| rsns(dvsns=0.045, ilim=4) | 0.01125 | 0.011 | 0.03 | pass | DS p.19, Design Example, RSNS = 45 mV / 4 A = 11 mohm |
| vreg(r7=102800, r8=4990, vfb=1.25) | 27.0015 | 27 | 0.002 | pass | DS p.19, Design Example, VREG = 27 V (R7 = 102.8k, R8 = 4.99k) |
| r7_for_vreg(vreg_target=27, r8=4990, vfb=1.25) | 102794 | 102800 | 0.002 | pass | DS p.19, Design Example, R7 = 102.8k |
| vin_uv(r1=380000, r2=90000, r3=10000, vth=1.25) | 6 | 6 | 0.001 | pass | DS p.19, Design Example, UV = 6 V (R1 380k, R2 90k, R3 10k) |
| vin_ov(r1=380000, r2=90000, r3=10000, vth=1.25) | 60 | 60 | 0.001 | pass | DS p.19, Design Example, OV = 60 V (same divider) |
| vin_uv(r1=383000, r2=90900, r3=10000, vth=1.25) | 5.9948 | 6 | 0.01 | pass | DS p.12, Figure 1, UV = 6 V (383k, 90.9k, 10k) |
| vin_ov(r1=383000, r2=90900, r3=10000, vth=1.25) | 60.4875 | 60 | 0.02 | pass | DS p.12, Figure 1, OV = 60 V (383k, 90.9k, 10k) |
| uv_ov_r2(vuv=6, vov=60, r3=10000) | 90000 | 90000 | 0.001 | pass | DS p.19, Design Example, R2 = 90k |
| uv_r1(vuv=6, vth=1.25, r2=90000, r3=10000) | 380000 | 380000 | 0.001 | pass | DS p.19, Design Example, R1 = 380k |
| c_tmr_for_warning(t_warn=0.001, i_warn=5e-06, dv_warn=0.1) | 5e-08 | 5e-08 | 0.001 | pass | DS p.19, Design Example, CTMR = 50 nF |
| c_tmr_for_warning(t_warn=0.001, i_warn=-5e-06, dv_warn=0.1) | 5e-08 | 5e-08 | 0.001 | pass | DS p.19 with the signed stored param (itmr_up_warn is negative): abs() gives 50 nF |
| t_warning(ctmr=1e-06, i_warn=5e-06, dv_warn=0.1) | 0.02 | 0.02 | 0.001 | pass | DS p.14, Figure 3a label tWARNING = 20 ms/uF |
| t_warning(ctmr=1e-06, i_warn=-5e-06, dv_warn=0.1) | 0.02 | 0.02 | 0.001 | pass | DS p.4 stored sign: itmr_up_warn negative, abs() gives 20 ms/uF |
| itmr_up_ov_typ(dv=75) | 4.9978e-05 | 5e-05 | 0.01 | pass | DS p.14, Figure 3a label ITMR = 50 uA at VCC-VOUT = 75 V |
| itmr_up_ov_typ(dv=10) | 8.118e-06 | 8e-06 | 0.02 | pass | DS p.14, Figure 3a label ITMR = 8 uA at VCC-VOUT = 10 V |
| itmr_up_oc_typ(dv=75) | 0.00026032 | 0.00026 | 0.01 | pass | DS p.14, Figure 3b label ITMR = 260 uA at VCC-VOUT = 75 V |
| itmr_up_oc_typ(dv=10) | 4.192e-05 | 4.2e-05 | 0.01 | pass | DS p.14, Figure 3b label ITMR = 42 uA at VCC-VOUT = 10 V |
| t_flt(ctmr=1e-06, i_up=-5e-05, vtmr_f=1.25) | 0.025 | 0.025 | 0.001 | pass | DS p.14, Figure 3a label tFLT = 25 ms/uF, stored negative current |
| t_flt(ctmr=1e-06, i_up=0.00026, vtmr_f=1.25) | 0.00480769 | 0.0048 | 0.002 | pass | DS p.14, Figure 3b label tFLT = 4.8 ms/uF |
| t_ov(ctmr=1e-06, i_up_ov=-5e-05, i_warn=-5e-06, vtmr_f=1.25, dv_warn=0.1) | 0.045 | 0.045 | 0.001 | pass | DS p.14, Figure 3a labels tFLT 25 + tWARNING 20 = 45 ms/uF, stored negative currents |
| t_oc(ctmr=1e-06, i_up_oc=0.00026, vtmr_g=1.35) | 0.00519231 | 0.00518 | 0.005 | pass | DS p.14, Figure 3b labels tFLT 4.8 + tWARNING 0.38 = 5.18 ms/uF |
| t_oc(ctmr=4.7e-08, i_up_oc=5.5e-05, vtmr_g=1.35) | 0.00115364 | 0.00115 | 0.005 | pass | DS p.19, Design Example, tOC = 1.15 ms |
| t_oc(ctmr=4.7e-08, i_up_oc=4.9e-05, vtmr_g=1.35) | 0.0012949 | 0.0013 | 0.01 | pass | DS p.20, tOC = 1.3 ms at VOUT = 2 V (49 uA) |
| r4_max(vin_min=6, vcc_min=4, icc_max=0.00075) | 2666.67 | 2700 | 0.02 | pass | DS p.19, Design Example, R4 = 2.7k |
| i_d1_peak(vin_max=200, vz_min=64, r4=2200) | 0.0618182 | 0.062 | 0.01 | pass | DS p.19, Design Example, ID1(PK) = 62 mA |
| p_m1_oc(vds=14, dvsns=0.032, rsns_ohm=0.01) | 44.8 | 45 | 0.01 | pass | DS p.20, Design Example, P = 45 W |
| p_m1_oc(vds=12, dvsns=0.055, rsns_ohm=0.01) | 66 | 66 | 0.001 | pass | DS p.20, Design Example, P = 66 W |
| rdson_m2_max(vfw=0.25, i_load_max=5.5) | 0.0454545 | 0.0455 | 0.002 | pass | DS p.20, MOSFET Selection, RDS(ON) = 45.5 mohm |
| p2t_simple(i_load=3, vpk=80, vreg_v=16, tau=0.001) | 18.432 | 18.4 | 0.005 | pass | DS p.17, Calculating Transient Stress, P2t = 18.4 W^2 s |
| p2t_short(vin=15, dvsns=0.025, rsns_ohm=0.012, t_oc_s=0.00229905) | 2.24516 | 2.2 | 0.025 | pass | DS p.17, Short-Circuit Stress, P2t = 2.2 W^2 s |
