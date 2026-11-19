<!-- GENERATED - do not edit. Run: python3 -m lib.readme -->

# INA821IDGK

## Datasheet review

[![Human page-image review: 0/81 human](https://img.shields.io/badge/human%20review-0%2F81%20human-lightgrey)](../../../docs/spec/datasheet-review.md)

Human page-image review: 0/81; cross-model audits: 0; manufacturer-export stamps: 0; legacy/unclassified: 0. Text checks are not verification. `lib.check` validates stamp format, not that review occurred.

## Part

- **mpn**: INA821IDGKR
- **alternates**: ['INA821IDGKT']
- **manufacturer**: Texas Instruments
- **description**: Precision instrumentation amplifier, 4.5-36 V
- **category**: instrumentation_amplifier
- **package**: VSSOP-8 (DGK0008A)
- **datasheet_url**: https://www.ti.com/lit/ds/symlink/ina821.pdf
- **datasheet_file**: docs/datasheets/ina821.pdf
- **datasheet_rev**: SBOS893D
- **datasheet_date**: 2020-06
- **temp_grade**: -40 to 125 degC
- **kicad_symbol**: INA821IDGK.kicad_sym
- **kicad_footprint**: INA821IDGK.kicad_mod
- **step**: embedded

## Pins

| Pin | Name | Type | Function | Cite |
|---|---|---|---|---|
| 1 | -IN | input | Negative (inverting) input | DS p.4, 6 Pin Functions, -IN (pin 1) |
| 2 | RG1 | passive | Gain setting pin; gain resistor RG connects between pin 2 and pin 3. Symbol name RG1 (separate node from pin 3) | DS p.4, 6 Pin Functions, RG (pins 2, 3) |
| 3 | RG2 | passive | Gain setting pin; gain resistor RG connects between pin 2 and pin 3. Symbol name RG2 (separate node from pin 2) | DS p.4, 6 Pin Functions, RG (pins 2, 3) |
| 4 | +IN | input | Positive (noninverting) input | DS p.4, 6 Pin Functions, +IN (pin 4) |
| 5 | -VS | power_in | Negative supply | DS p.4, 6 Pin Functions, -VS (pin 5) |
| 6 | REF | input | Reference input; must be driven by a low impedance source | DS p.4, 6 Pin Functions, REF (pin 6) |
| 7 | OUT | output | Output | DS p.4, 6 Pin Functions, OUT (pin 7) |
| 8 | +VS | power_in | Positive supply | DS p.4, 6 Pin Functions, +VS (pin 8) |

## Parameters: abs_max

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Supply voltage |  | -20 |  | 20 | V | over operating free-air temperature range (unless otherwise noted) Note: Printed -20 V to 20 V with no reference pin. Read as a 40 V maximum span between +VS and -VS: DS p.24, 8.3.5, 'Supply voltages higher than 40 V (+/-20 V) can permanently damage the device'. A per-rail reading would reject the 36 V single supply that rec-op allows (DS p.5, 7.3). | DS p.5, 7.1 Absolute Maximum Ratings, Supply voltage |  |
| Signal input pins, voltage |  | -40 |  | 40 | V | over operating free-air temperature range (unless otherwise noted) Note: Each input is rated alone (DS p.23, 8.3.4: -40 V on one input and +40 V on the other does not cause damage). No reference pin is printed; checked against system 0 V. DS p.23 shows input current only with +/-15 V supplies applied: driving an input while unpowered is not rated (owner: module). | DS p.5, 7.1 Absolute Maximum Ratings, Signal input pins, Voltage |  |
| Signal input pins, REF pin |  | -20 |  | 20 | V | over operating free-air temperature range (unless otherwise noted) Note: Applied as: the REF pin within -20 V to 20 V of the system common, since no reference pin is printed (DS p.5, 7.1). | DS p.5, 7.1 Absolute Maximum Ratings, Signal input pins, REF pin |  |
| Signal output pins |  | -0.5 (rel. -VS) |  | 0.5 (rel. +VS) | V | over operating free-air temperature range (unless otherwise noted) Note: Printed as (-Vs) - 0.5 V to (+Vs) + 0.5 V. | DS p.5, 7.1 Absolute Maximum Ratings, Signal output pins |  |
| Operating temperature | TA | -50 |  | 150 | degC |  | DS p.5, 7.1 Absolute Maximum Ratings, Operating Temperature, TA |  |
| Junction temperature | TJ |  |  | 175 | degC |  | DS p.5, 7.1 Absolute Maximum Ratings, Junction Temperature, TJ |  |
| Output short-circuit |  |  | Continuous |  |  | short-circuit to VS / 2 Note: Footnote (2) text: Short-circuit to VS / 2. Footnote (1) text: exposure to absolute-maximum-rated conditions for extended periods may affect device reliability. Not numeric: stored as text. | DS p.5, 7.1 Absolute Maximum Ratings, Output short-circuit (2) |  |
| Storage temperature | Tstg | -65 |  | 150 | degC |  | DS p.5, 7.1 Absolute Maximum Ratings, Storage Temperature, Tstg |  |
| Electrostatic discharge, human-body model | V(ESD) | -1500 |  | 1500 | V | HBM per ANSI/ESDA/JEDEC JS-001 Note: Printed +/-1500 V. ESD table stored with kind abs_max (no ESD kind in SPEC). | DS p.5, 7.2 ESD Ratings, Human-body model (HBM) |  |
| Electrostatic discharge, charged-device model | V(ESD) | -750 |  | 750 | V | CDM per JEDEC JESD22-C101 Note: Printed +/-750 V. ESD table stored with kind abs_max (no ESD kind in SPEC). | DS p.5, 7.2 ESD Ratings, Charged-device model (CDM) |  |

## Parameters: rec_op

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Supply voltage, single-supply | VS | 4.5 (rel. -VS) |  | 36 (rel. -VS) | V | single-supply; over operating free-air temperature range | DS p.5, 7.3 Recommended Operating Conditions, Supply voltage VS, Single-supply |  |
| Supply voltage, dual-supply | VS | 2.25 |  | 18 | V | dual-supply; over operating free-air temperature range Note: Printed +/-2.25 V (MIN column) and +/-18 V (MAX column). Stored as magnitudes of each supply, without sign. | DS p.5, 7.3 Recommended Operating Conditions, Supply voltage VS, Dual-supply |  |
| Specified temperature | TA | -40 |  | 125 | degC | specified temperature | DS p.5, 7.3 Recommended Operating Conditions, Specified temperature, TA |  |

## Parameters: electrical

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Input stage offset voltage | VOSI |  | ±10 | ±40 | uV | TA = 25 degC, VS = +/-15 V, RL = 10 kohm, VREF = 0 V, G = 1; INA821IDGK column Note: Footnotes (1)(2): VOS(RTI) = VOSI + VOSO/G (see calc.py vos_rti). DGK value is 40 uV; ID/DRG value is 35 uV. DS prints an unsigned magnitude; sym = true (loader uses min = -max). | DS p.6, 7.5 Electrical Characteristics, Input stage offset voltage VOSI, INA821IDGK, 25 degC row |  |
| Input stage offset voltage, full temperature | VOSI |  |  | ±80 | uV | TA = -40 degC to +125 degC; INA821IDGK row Note: Specified by characterization, not production tested (DS note 3). ID/DRG value is 75 uV. DS prints an unsigned magnitude; sym = true (loader uses min = -max). | DS p.6, 7.5 Electrical Characteristics, Input stage offset voltage VOSI, TA = -40 degC to +125 degC, INA821IDGK |  |
| Input stage offset voltage drift | VOSI |  | ±0.1 | ±0.4 | uV/degC | vs temperature, TA = -40 degC to +125 degC Note: Row printed for all packages (no package split). DS prints an unsigned magnitude; sym = true (loader uses min = -max). | DS p.6, 7.5 Electrical Characteristics, Input stage offset voltage VOSI, vs temperature |  |
| Output stage offset voltage | VOSO |  | ±50 | ±350 | uV | TA = 25 degC, VS = +/-15 V, RL = 10 kohm, VREF = 0 V, G = 1; INA821ID, INA821DGK row Note: Footnotes (1)(2): VOS(RTI) = VOSI + VOSO/G. INA821DRG value is 400 uV (not this part). DS prints an unsigned magnitude; sym = true (loader uses min = -max). | DS p.6, 7.5 Electrical Characteristics, Output stage offset voltage VOSO, INA821ID and INA821DGK |  |
| Output stage offset voltage, full temperature | VOSO |  |  | ±850 | uV | TA = -40 degC to +125 degC Note: Specified by characterization, not production tested (DS note 3). Row printed for all packages. DS prints an unsigned magnitude; sym = true (loader uses min = -max). | DS p.6, 7.5 Electrical Characteristics, Output stage offset voltage VOSO, TA = -40 degC to +125 degC |  |
| Output stage offset voltage drift | VOSO |  |  | ±5 | uV/degC | vs temperature, TA = -40 degC to +125 degC Note: Only a MAX is printed. DS prints an unsigned magnitude; sym = true (loader uses min = -max). | DS p.6, 7.5 Electrical Characteristics, Output stage offset voltage VOSO, vs temperature |  |
| Power-supply rejection ratio, G = 1 |  | 110 | 120 |  | dB | G = 1, RTI; TA = 25 degC (table header) | DS p.6, 7.5 Electrical Characteristics, Power-supply rejection ratio, G = 1, RTI |  |
| Power-supply rejection ratio, G = 10 |  | 114 | 130 |  | dB | G = 10, RTI; TA = 25 degC (table header) | DS p.6, 7.5 Electrical Characteristics, Power-supply rejection ratio, G = 10, RTI |  |
| Power-supply rejection ratio, G = 100 |  | 130 | 135 |  | dB | G = 100, RTI; TA = 25 degC (table header) | DS p.6, 7.5 Electrical Characteristics, Power-supply rejection ratio, G = 100, RTI |  |
| Power-supply rejection ratio, G = 1000 |  | 136 | 140 |  | dB | G = 1000, RTI; TA = 25 degC (table header) | DS p.6, 7.5 Electrical Characteristics, Power-supply rejection ratio, G = 1000, RTI |  |
| Differential input impedance, resistive part | zid |  | 100 |  | Gohm | TA = 25 degC (table header) Note: Printed as R \|\| C: 100 GOhm \|\| 1 pF. | DS p.6, 7.5 Electrical Characteristics, Differential impedance zid, TYP column |  |
| Differential input impedance, capacitive part | zid |  | 1 |  | pF | TA = 25 degC (table header) Note: Printed as R \|\| C: 100 GOhm \|\| 1 pF. | DS p.6, 7.5 Electrical Characteristics, Differential impedance zid, TYP column |  |
| Common-mode input impedance, resistive part | zic |  | 100 |  | Gohm | TA = 25 degC (table header) Note: Printed as R \|\| C: 100 GOhm \|\| 7 pF. | DS p.6, 7.5 Electrical Characteristics, Common-mode impedance zic, TYP column |  |
| Common-mode input impedance, capacitive part | zic |  | 7 |  | pF | TA = 25 degC (table header) Note: Printed as R \|\| C: 100 GOhm \|\| 7 pF. | DS p.6, 7.5 Electrical Characteristics, Common-mode impedance zic, TYP column |  |
| RFI filter, -3 dB frequency |  |  | 45 |  | MHz | TA = 25 degC (table header) | DS p.6, 7.5 Electrical Characteristics, RFI filter, -3-dB frequency |  |
| Operating input range (common-mode) | VCM | 2 (rel. -VS) |  | -2 (rel. +VS) | V | TA = 25 degC, VS = +/-15 V, RL = 10 kohm, VREF = 0 V, G = 1 (table header) Note: Printed (V-) + 2 V to (V+) - 2 V. Footnote (4): input range depends on common-mode voltage, differential voltage, gain and VREF; see Figures 51-54 (curves). The VS = +/-2.25 V to +/-18 V, TA = -40 degC to +125 degC row prints no numeric limit. | DS p.6, 7.5 Electrical Characteristics, Operating input range (4), first row |  |
| Input overvoltage range |  | -40 |  | 40 | V | TA = -40 degC to +125 degC Note: Printed +/-40 V. Specified by characterization, not production tested (DS note 3). | DS p.6, 7.5 Electrical Characteristics, Input overvoltage range, TA = -40 degC to +125 degC |  |
| Common-mode rejection ratio, G = 1 |  | 92 | 105 |  | dB | DC to 60 Hz, RTI, VCM = (V-) + 2 V to (V+) - 2 V, G = 1 | DS p.6, 7.5 Electrical Characteristics, Common-mode rejection ratio, G = 1 |  |
| Common-mode rejection ratio, G = 10 |  | 112 | 125 |  | dB | DC to 60 Hz, RTI, VCM = (V-) + 2 V to (V+) - 2 V, G = 10 | DS p.6, 7.5 Electrical Characteristics, Common-mode rejection ratio, G = 10 |  |
| Common-mode rejection ratio, G = 100 |  | 132 | 145 |  | dB | DC to 60 Hz, RTI, VCM = (V-) + 2 V to (V+) - 2 V, G = 100 | DS p.6, 7.5 Electrical Characteristics, Common-mode rejection ratio, G = 100 |  |
| Common-mode rejection ratio, G = 1000 |  | 140 | 150 |  | dB | DC to 60 Hz, RTI, VCM = (V-) + 2 V to (V+) - 2 V, G = 1000 | DS p.6, 7.5 Electrical Characteristics, Common-mode rejection ratio, G = 1000 |  |
| Input bias current | IB |  | ±0.15 | ±0.5 | nA | VCM = VS / 2; TA = 25 degC (table header) Note: DS prints an unsigned magnitude; sym = true (loader uses min = -max). | DS p.6, 7.5 Electrical Characteristics, Input bias current IB, VCM = VS / 2 |  |
| Input bias current, full temperature | IB |  |  | ±2 | nA | TA = -40 degC to +125 degC Note: VCM not stated on this row. Not footnoted in the DS (no note 3). DS prints an unsigned magnitude; sym = true (loader uses min = -max). | DS p.6, 7.5 Electrical Characteristics, Input bias current IB, TA = -40 degC to +125 degC |  |
| Input offset current | IOS |  | ±0.15 | ±0.5 | nA | VCM = VS / 2; TA = 25 degC (table header) Note: DS prints an unsigned magnitude; sym = true (loader uses min = -max). | DS p.6, 7.5 Electrical Characteristics, Input offset current IOS, VCM = VS / 2 |  |
| Input offset current, full temperature | IOS |  |  | ±2 | nA | TA = -40 degC to +125 degC Note: VCM not stated on this row. DS prints an unsigned magnitude; sym = true (loader uses min = -max). | DS p.6, 7.5 Electrical Characteristics, Input offset current IOS, TA = -40 degC to +125 degC |  |
| Input stage voltage noise, f = 1 kHz | eNI |  | 7 |  | nV/rtHz | f = 1 kHz, G = 100, RS = 0 ohm Note: Footnote (5): total RTI noise eN(RTI) = sqrt(eNI^2 + (eNO/G)^2). | DS p.6, 7.5 Electrical Characteristics, Input stage voltage noise eNI, f = 1 kHz |  |
| Input stage voltage noise, 0.1 Hz to 10 Hz | eNI |  | 0.14 |  | uVpp | fB = 0.1 Hz to 10 Hz, G = 100, RS = 0 ohm Note: Peak-to-peak unit; footnote (5) formula is printed for this row. Unit uVpp is not in the SPEC unit list (open item). | DS p.6, 7.5 Electrical Characteristics, Input stage voltage noise eNI, fB = 0.1 Hz to 10 Hz |  |
| Output stage voltage noise, f = 1 kHz | eNO |  | 65 |  | nV/rtHz | f = 1 kHz, RS = 0 ohm Note: Footnote (5) applies: eN(RTI) = sqrt(eNI^2 + (eNO/G)^2). | DS p.6, 7.5 Electrical Characteristics, Output stage voltage noise eNO, f = 1 kHz |  |
| Output stage voltage noise, 0.1 Hz to 10 Hz | eNO |  | 2.5 |  | uVpp | fB = 0.1 Hz to 10 Hz, RS = 0 ohm Note: Peak-to-peak unit; footnote (5) formula is printed for this row. Unit uVpp is not in the SPEC unit list (open item). | DS p.6, 7.5 Electrical Characteristics, Output stage voltage noise eNO, fB = 0.1 Hz to 10 Hz |  |
| Input noise current, f = 1 kHz | In |  | 130 |  | fA/rtHz | f = 1 kHz Note: Unit fA/rtHz is not in the SPEC unit list (open item). | DS p.6, 7.5 Electrical Characteristics, Noise current In, f = 1 kHz |  |
| Input noise current, 0.1 Hz to 10 Hz | In |  | 4.7 |  | pApp | fB = 0.1 Hz to 10 Hz, G = 100 Note: Peak-to-peak unit pApp is not in the SPEC unit list (open item). | DS p.6, 7.5 Electrical Characteristics, Noise current In, fB = 0.1 Hz to 10 Hz, G = 100 |  |
| Range of gain | G | 1 |  | 10000 |  | no conditions printed; table header (TA = 25 degC, VS = +/-15 V) applies Note: Unitless V/V, stored as unit "" per SPEC. Gain equation G = 1 + 49.4 kohm / RG (DS p.6 and p.20, Equation 1) is in calc.py. | DS p.6, 7.5 Electrical Characteristics, GAIN, Range of gain |  |
| Gain error, G = 1 | GE | -0.025 | ±0.005 | 0.025 | % | G = 1, VO = +/-10 V; TA = 25 degC (table header) Note: Printed TYP +/-0.005 % and MAX +/-0.025 %. Typ printed +/- is a spread around zero: stored as X with typ_pm = true (loader keeps X as typ_spread). Printed +/- limit in MAX stored as min = -max, max = +max. | DS p.7, 7.5 Electrical Characteristics, Gain error, G = 1, VO = +/-10 V |  |
| Gain error, G = 10 | GE | -0.15 | ±0.025 | 0.15 | % | G = 10, VO = +/-10 V; TA = 25 degC (table header) Note: Printed TYP +/-0.025 % and MAX +/-0.15 %. Typ printed +/- is a spread around zero: stored as X with typ_pm = true (loader keeps X as typ_spread). Printed +/- limit in MAX stored as min = -max, max = +max. | DS p.7, 7.5 Electrical Characteristics, Gain error, G = 10, VO = +/-10 V |  |
| Gain error, G = 100 | GE | -0.15 | ±0.025 | 0.15 | % | G = 100, VO = +/-10 V; TA = 25 degC (table header) Note: Printed TYP +/-0.025 % and MAX +/-0.15 %. Typ printed +/- is a spread around zero: stored as X with typ_pm = true (loader keeps X as typ_spread). Printed +/- limit in MAX stored as min = -max, max = +max. | DS p.7, 7.5 Electrical Characteristics, Gain error, G = 100, VO = +/-10 V |  |
| Gain error, G = 1000 | GE |  | ±0.05 |  | % | G = 1000, VO = +/-10 V; TA = 25 degC (table header) Note: Printed TYP +/-0.05 %, no MAX printed. Spread around zero: stored as X with typ_pm = true (loader keeps X as typ_spread). No min or max stored. | DS p.7, 7.5 Electrical Characteristics, Gain error, G = 1000, VO = +/-10 V |  |
| Gain vs temperature, G = 1 |  | -5 |  | 5 | ppm/degC | G = 1, TA = -40 degC to +125 degC Note: Printed +/-5 ppm/degC as MAX; stored as min = -max, max = +max. | DS p.7, 7.5 Electrical Characteristics, Gain vs temperature (6), G = 1 |  |
| Gain vs temperature, G > 1 |  | -35 |  | 35 | ppm/degC | G > 1, TA = -40 degC to +125 degC Note: Printed +/-35 ppm/degC as MAX; stored as min = -max, max = +max. Footnote (6): values for G > 1 exclude the effect of the external RG. | DS p.7, 7.5 Electrical Characteristics, Gain vs temperature (6), G > 1 |  |
| Gain nonlinearity, G = 1 to 10 |  |  | ±1 | ±10 | ppm | G = 1 to 10, VO = -10 V to 10 V, RL = 10 kohm; TA = 25 degC (table header) Note: DS prints an unsigned magnitude; sym = true (loader uses min = -max). | DS p.7, 7.5 Electrical Characteristics, Gain nonlinearity, G = 1 to 10 |  |
| Gain nonlinearity, G = 100 |  |  |  | ±15 | ppm | G = 100, VO = -10 V to 10 V, RL = 10 kohm; TA = 25 degC (table header) Note: Only a MAX is printed. DS prints an unsigned magnitude; sym = true (loader uses min = -max). | DS p.7, 7.5 Electrical Characteristics, Gain nonlinearity, G = 100 |  |
| Gain nonlinearity, G = 1000 |  |  | 10 |  | ppm | G = 1000, VO = -10 V to 10 V, RL = 10 kohm; TA = 25 degC (table header) | DS p.7, 7.5 Electrical Characteristics, Gain nonlinearity, G = 1000 |  |
| Gain nonlinearity, G = 1 to 100, RL = 2 kohm |  |  | 30 |  | ppm | G = 1 to 100, VO = -10 V to 10 V, RL = 2 kohm; TA = 25 degC (table header) | DS p.7, 7.5 Electrical Characteristics, Gain nonlinearity, G = 1 to 100, RL = 2 kohm |  |
| Output voltage swing |  | 0.15 (rel. -VS) |  | -0.15 (rel. +VS) | V | RL = 10 kohm; TA = 25 degC, VS = +/-15 V (table header) Note: Printed (V-) + 0.15 V to (V+) - 0.15 V. | DS p.7, 7.5 Electrical Characteristics, OUTPUT, Voltage swing |  |
| Load capacitance stability |  |  | 1000 |  | pF | TA = 25 degC (table header) | DS p.7, 7.5 Electrical Characteristics, OUTPUT, Load capacitance stability |  |
| Closed-loop output impedance | ZO |  | 1.3 |  | ohm | f = 10 kHz; TA = 25 degC (table header) | DS p.7, 7.5 Electrical Characteristics, OUTPUT, Closed-loop output impedance, f = 10 kHz |  |
| Short-circuit current | ISC |  | 20 |  | mA | continuous to VS / 2; TA = 25 degC (table header) Note: Printed +/-20 mA in the TYP column. Typical only: stored as magnitude typ, not a bound (SPEC: typical values are never a check bound). | DS p.7, 7.5 Electrical Characteristics, OUTPUT, Short-circuit current |  |
| Bandwidth, -3 dB, G = 1 |  |  | 4.7 |  | MHz | G = 1; TA = 25 degC (table header) | DS p.7, 7.5 Electrical Characteristics, FREQUENCY RESPONSE, Bandwidth -3 dB, G = 1 |  |
| Bandwidth, -3 dB, G = 10 |  |  | 970 |  | kHz | G = 10; TA = 25 degC (table header) | DS p.7, 7.5 Electrical Characteristics, FREQUENCY RESPONSE, Bandwidth -3 dB, G = 10 |  |
| Bandwidth, -3 dB, G = 100 |  |  | 290 |  | kHz | G = 100; TA = 25 degC (table header) | DS p.7, 7.5 Electrical Characteristics, FREQUENCY RESPONSE, Bandwidth -3 dB, G = 100 |  |
| Bandwidth, -3 dB, G = 1000 |  |  | 30 |  | kHz | G = 1000; TA = 25 degC (table header) | DS p.7, 7.5 Electrical Characteristics, FREQUENCY RESPONSE, Bandwidth -3 dB, G = 1000 |  |
| Slew rate | SR |  | 2.0 |  | V/us | G = 1, VO = +/-10 V; TA = 25 degC (table header) | DS p.7, 7.5 Electrical Characteristics, FREQUENCY RESPONSE, Slew rate |  |
| Settling time to 0.01%, G = 1 to 100 | tS |  | 6 |  | us | 0.01%, G = 1 to 100, VSTEP = 10 V; TA = 25 degC (table header) | DS p.7, 7.5 Electrical Characteristics, FREQUENCY RESPONSE, Settling time, 0.01%, G = 1 to 100 |  |
| Settling time to 0.01%, G = 1000 | tS |  | 40 |  | us | 0.01%, G = 1000, VSTEP = 10 V; TA = 25 degC (table header) | DS p.7, 7.5 Electrical Characteristics, FREQUENCY RESPONSE, Settling time, 0.01%, G = 1000 |  |
| Settling time to 0.001%, G = 1 to 100 | tS |  | 10 |  | us | 0.001%, G = 1 to 100, VSTEP = 10 V; TA = 25 degC (table header) | DS p.7, 7.5 Electrical Characteristics, FREQUENCY RESPONSE, Settling time, 0.001%, G = 1 to 100 |  |
| Settling time to 0.001%, G = 1000 | tS |  | 50 |  | us | 0.001%, G = 1000, VSTEP = 10 V; TA = 25 degC (table header) | DS p.7, 7.5 Electrical Characteristics, FREQUENCY RESPONSE, Settling time, 0.001%, G = 1000 |  |
| Reference input impedance | RIN |  | 10 |  | kohm | TA = 25 degC (table header) | DS p.7, 7.5 Electrical Characteristics, REFERENCE INPUT, Input impedance |  |
| Reference input voltage range |  | 0 (rel. -VS) |  | 0 (rel. +VS) | V | TA = 25 degC, VS = +/-15 V (table header) Note: Printed (V-) and (V+), stored as offset 0 V from each rail. | DS p.7, 7.5 Electrical Characteristics, REFERENCE INPUT, Voltage range |  |
| Reference gain to output |  |  | 1 |  |  | TA = 25 degC (table header) Note: Unitless V/V, stored as unit "" per SPEC. | DS p.7, 7.5 Electrical Characteristics, REFERENCE INPUT, Gain to output |  |
| Reference gain error |  |  | 0.01 |  | % | TA = 25 degC (table header) | DS p.7, 7.5 Electrical Characteristics, REFERENCE INPUT, Reference gain error |  |
| Power-supply voltage, single-supply (electrical table) | VS | 4.5 |  | 36 | V | single-supply; TA = 25 degC (table header) Note: Same values as the 7.3 rec-op row (DS p.5). | DS p.7, 7.5 Electrical Characteristics, POWER SUPPLY, Power-supply voltage, Single-supply |  |
| Power-supply voltage, dual-supply (electrical table) | VS | 2.25 |  | 18 | V | dual-supply; TA = 25 degC (table header) Note: Printed +/-2.25 V (MIN) and +/-18 V (MAX). Stored as magnitudes, without sign. Same values as the 7.3 rec-op row (DS p.5). | DS p.7, 7.5 Electrical Characteristics, POWER SUPPLY, Power-supply voltage, Dual-supply |  |
| Quiescent current | IQ |  | 600 | 650 | uA | VIN = 0 V; TA = 25 degC (table header) | DS p.7, 7.5 Electrical Characteristics, POWER SUPPLY, Quiescent current, VIN = 0 V |  |
| Quiescent current, full temperature | IQ |  |  | 870 | uA | vs temperature, TA = -40 degC to +125 degC Note: Only a MAX is printed. | DS p.7, 7.5 Electrical Characteristics, POWER SUPPLY, Quiescent current, vs temperature |  |

## Parameters: thermal

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Junction-to-ambient thermal resistance | RthetaJA |  | 215.4 |  | degC/W | DGK (VSSOP), 8 pins Note: Single printed value (no min or max), stored as typ. | DS p.5, 7.4 Thermal Information, Junction-to-ambient thermal resistance, DGK column |  |
| Junction-to-case (top) thermal resistance | RthetaJC(top) |  | 66.3 |  | degC/W | DGK (VSSOP), 8 pins Note: Single printed value (no min or max), stored as typ. | DS p.5, 7.4 Thermal Information, Junction-to-case (top) thermal resistance, DGK column |  |
| Junction-to-board thermal resistance | RthetaJB |  | 97.8 |  | degC/W | DGK (VSSOP), 8 pins Note: Single printed value (no min or max), stored as typ. | DS p.5, 7.4 Thermal Information, Junction-to-board thermal resistance, DGK column |  |
| Junction-to-top characterization parameter | PsiJT |  | 10.5 |  | degC/W | DGK (VSSOP), 8 pins Note: Single printed value (no min or max), stored as typ. | DS p.5, 7.4 Thermal Information, Junction-to-top characterization parameter, DGK column |  |
| Junction-to-board characterization parameter | PsiJB |  | 96.1 |  | degC/W | DGK (VSSOP), 8 pins Note: Single printed value (no min or max), stored as typ. | DS p.5, 7.4 Thermal Information, Junction-to-board characterization parameter, DGK column |  |

## Limits of this data

Rows by scope: 25C 53, full 10, na 18 (25C rows hold only at 25 degC). Curve (graph) rows: 0. Text rows: 1.

## Zener checks

Generated wrapper: `INA821IDGK.zen` (`python3 -m lib.zen`). abs_max and rec_op rows are errors (abs_max x derate); 25C and partial rows are waivable warnings; a checked net with no voltage is UNVERIFIED.

| Param | Name | Checked against | Not checked / reason |
|---|---|---|---|
| vs_abs | Supply voltage | UNCHECKED | printed +/-20 V is a 40 V span (DS p.24, 8.3.5); covered by vs_rec_single (4.5 V to 36 V span, error), which is stricter |
| vin_abs | Signal input pins, voltage | pins +IN, -IN |  |
| vref_abs | Signal input pins, REF pin | pins REF |  |
| vout_abs | Signal output pins | UNCHECKED | OUT is driven by the part; owner: module |
| ta_abs | Operating temperature | UNCHECKED | covered by ta_rec (-40 degC to 125 degC, error), which is stricter |
| tj_abs | Junction temperature | UNCHECKED | needs dissipation x rtheta_ja; owner: module |
| isc_abs | Output short-circuit | UNCHECKED | text rating (Continuous, to VS/2); owner: board |
| tstg_abs | Storage temperature | UNCHECKED | owner: assembly |
| esd_hbm | Electrostatic discharge, human-body model | UNCHECKED | owner: assembly |
| esd_cdm | Electrostatic discharge, charged-device model | UNCHECKED | owner: assembly |
| vs_rec_single | Supply voltage, single-supply | pins +VS |  |
| vs_rec_dual | Supply voltage, dual-supply | UNCHECKED | same 4.5 V to 36 V span as vs_rec_single, which is checked |
| ta_rec | Specified temperature | board ambient |  |
| vcm_range_25c | Operating input range (common-mode) | pins +IN, -IN |  |
| vref_range_25c | Reference input voltage range | pins REF |  |

## Equations

### `gain`

```
G = 1 + 49.4 kohm / RG. DS p.20, 8.3.1 Setting the Gain, Equation 1.
rg: gain resistor between the RG pins (pins 2 and 3), ohm. Returns: gain G, V/V (unitless).
```

Inputs:


### `rg_for_gain`

```
RG = 49.4 kohm / (G - 1). Algebra on DS p.20, Equation 1 (the DS prints Equation 1 only, not this form).
g: target gain, V/V, must be > 1 (G = 1 is RG open, DS p.20 Table 2 NC). Returns: RG, ohm.
Ideal value; the nearest standard resistor changes the gain (DS p.20 Table 2 gives both).
```

Inputs:


### `vos_rti`

```
VOS(RTI) = VOSI + VOSO / G. DS p.6, 7.5 Electrical Characteristics, footnote (1).
vosi: input stage offset voltage, V, signed (sym param: magnitude bound). voso: output stage offset voltage, V,
signed (sym param). g: gain, V/V. Returns: total offset referred to input, V, signed.
```

Inputs:

- `vosi` -> `vosi_full` (max ±80 uV)
- `voso` -> `vos_o_full` (max ±850 uV)

### `dvos_rti`

```
dVOS(RTI) = sqrt(dVOSI^2 + (dVOSO / G)^2). DS p.6, 7.5 Electrical Characteristics, footnote (2)
(offset drifts are uncorrelated). dvosi, dvoso: offset drifts, V/degC (magnitudes; the square makes sign irrelevant).
g: gain, V/V. Returns: V/degC.
```

Inputs:

- `dvosi` -> `vosi_drift_full` (typ ±0.1 max ±0.4 uV/degC)
- `dvoso` -> `vos_o_drift_full` (max ±5 uV/degC)

### `en_rti`

```
eN(RTI) = sqrt(eNI^2 + (eNO / G)^2). DS p.6, 7.5 Electrical Characteristics, footnote (5).
eni: input stage voltage noise, V/rtHz (or Vpp, as printed for the row). eno: output stage voltage noise, same unit.
g: gain, V/V. Returns: total RTI voltage noise in the same unit as eni and eno.
```

Inputs:

- `eni` -> `eni_g100_1khz.typ` (typ 7 nV/rtHz)
- `eno` -> `eno_1khz.typ` (typ 65 nV/rtHz)

### `vout`

```
VO = G * (VIN+ - VIN-) + VREF. DS p.20, 8.3.1 Setting the Gain, Figure 55 output equation.
g: gain, V/V. vin_p: +IN voltage, V. vin_n: -IN voltage, V. vref: REF voltage, V. Returns: VO, V.
```

Inputs:


### `gain_actual`

```
Not a DS equation: gain at temperature t_c with gain error and gain drift applied to Equation 1.
G(T) = gain(rg) * (1 + gain_err) * (1 + gain_drift * (T - 25)). Combines three sources:
- gain(rg): DS p.20, 8.3.1 Setting the Gain, Equation 1 (RG tolerance and RG tempco are the caller's rg input,
  so pass rg as a wca input with its own tolerance and TCR);
- gain_err: 25 degC gain error row, DS p.7, 7.5 Electrical Characteristics, Gain error (no full-temperature
  gain-error row exists, so SPEC recipe step 2 applies: 25 degC row plus drift);
- gain_drift: DS p.7, 7.5 Electrical Characteristics, Gain vs temperature (6). Footnote (6): the G > 1 value
  excludes the effect of the external RG.
rg: ohm. gain_err: fraction, signed (+/- spread as in the DS). gain_drift: 1/degC, signed.
t_c: temperature, degC. Returns: gain, V/V.
```

Inputs:

- `gain_err` -> `gain_err_g10_25c` (min -0.15 typ ±0.025 max 0.15 %)
- `gain_drift` -> `gain_drift_gt1_full` (min -35 max 35 ppm/degC)


## Examples

| Call | Computed | Expected | Rel. tol | Result | Cite |
|---|---|---|---|---|---|
| gain(rg=49400) | 2 | 2 | 0.001 | pass | DS p.20, Table 2, DESIRED GAIN 2, RG 49.4 k |
| gain(rg=12350) | 5 | 5 | 0.001 | pass | DS p.20, Table 2, DESIRED GAIN 5, RG 12.35 k |
| gain(rg=5489) | 9.99982 | 10 | 0.001 | pass | DS p.20, Table 2, DESIRED GAIN 10, RG 5.489 k |
| gain(rg=2600) | 20 | 20 | 0.001 | pass | DS p.20, Table 2, DESIRED GAIN 20, RG 2.600 k |
| gain(rg=1008) | 50.0079 | 50 | 0.001 | pass | DS p.20, Table 2, DESIRED GAIN 50, RG 1.008 k |
| gain(rg=499) | 99.998 | 100 | 0.001 | pass | DS p.20, Table 2, DESIRED GAIN 100, RG 499 |
| gain(rg=248) | 200.194 | 200 | 0.001 | pass | DS p.20, Table 2, DESIRED GAIN 200, RG 248 |
| gain(rg=99) | 499.99 | 500 | 0.001 | pass | DS p.20, Table 2, DESIRED GAIN 500, RG 99 |
| gain(rg=49.4) | 1001 | 1000 | 0.002 | pass | DS p.20, Table 2, DESIRED GAIN 1000, RG 49.4 (printed rounded; exact 49.45) |
| gain_actual(rg=5489, gain_err=0, gain_drift=0, t_c=25) | 9.99982 | 10 | 0.001 | pass | DS p.20, Table 2, DESIRED GAIN 10, RG 5.489 k (with zero error and drift) |
