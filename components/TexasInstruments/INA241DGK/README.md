<!-- GENERATED - do not edit. Run: python3 -m lib.readme -->

# INA241DGK

## Datasheet review

[![Human page-image review: 0/86 human](https://img.shields.io/badge/human%20review-0%2F86%20human-lightgrey)](../../../docs/spec/datasheet-review.md)

Human page-image review: 0/86; cross-model audits: 0; manufacturer-export stamps: 0; legacy/unclassified: 0. Text checks are not verification. `lib.check` validates stamp format, not that review occurred.

## Part

- **manufacturer**: Texas Instruments
- **description**: Bidirectional current-sense amplifier, -5 V to 110 V common mode, 2.7 V to 20 V supply, VSSOP-8 (DGK)
- **category**: current_sense_amplifier
- **package**: VSSOP-8 (DGK0008A)
- **datasheet_url**: https://www.ti.com/lit/ds/symlink/ina241a.pdf
- **datasheet_file**: docs/datasheets/ina241a.pdf
- **datasheet_rev**: SBOSA30D
- **datasheet_date**: 2024-12
- **kicad_symbol**: INA241DGK.kicad_sym
- **kicad_footprint**: INA241DGK.kicad_mod
- **step**: INA241DGK.step

## Variants

Shared data below applies to every variant unless a row names its variants.

| Value | mpn | alternates | temp_grade | description |
|---|---|---|---|---|
| INA241A1IDGK | INA241A1IDGKR |  | -40 to 125 degC | INA241A1 gain 10 V/V, VSSOP-8 (DGK), -40 to 125 degC |
| INA241A2IDGK | INA241A2IDGKR |  | -40 to 125 degC | INA241A2 gain 20 V/V, VSSOP-8 (DGK), -40 to 125 degC |
| INA241A3IDGK | INA241A3IDGKR |  | -40 to 125 degC | INA241A3 gain 50 V/V, VSSOP-8 (DGK), -40 to 125 degC |
| INA241A4IDGK | INA241A4IDGKR |  | -40 to 125 degC | INA241A4 gain 100 V/V, VSSOP-8 (DGK), -40 to 125 degC |
| INA241A5IDGK | INA241A5IDGKR |  | -40 to 125 degC | INA241A5 gain 200 V/V, VSSOP-8 (DGK), -40 to 125 degC |
| INA241B1IDGK | INA241B1IDGKR |  | -40 to 125 degC | INA241B1 gain 10 V/V, VSSOP-8 (DGK), -40 to 125 degC |
| INA241B2IDGK | INA241B2IDGKR |  | -40 to 125 degC | INA241B2 gain 20 V/V, VSSOP-8 (DGK), -40 to 125 degC |
| INA241B3IDGK | INA241B3IDGKR |  | -40 to 125 degC | INA241B3 gain 50 V/V, VSSOP-8 (DGK), -40 to 125 degC |
| INA241B4IDGK | INA241B4IDGKR |  | -40 to 125 degC | INA241B4 gain 100 V/V, VSSOP-8 (DGK), -40 to 125 degC |
| INA241B5IDGK | INA241B5IDGKR |  | -40 to 125 degC | INA241B5 gain 200 V/V, VSSOP-8 (DGK), -40 to 125 degC |

## Pins

| Pin | Name | Type | Function | Cite |
|---|---|---|---|---|
| 1 | IN- | input | Current-sense amplifier negative input. High-side: connect to load side of sense resistor. Low-side: connect to ground side of sense resistor | DS p.2, Table 5-1 Pin Functions: D, DDF and DGK Packages, IN- (pin 1) |
| 2 | GND | power_in | Ground | DS p.2, Table 5-1 Pin Functions: D, DDF and DGK Packages, GND (pin 2) |
| 3 | REF2 | input | Reference 2 voltage. Connect to voltage potential from 0 V to VS; see Adjusting the Output With the Reference Pins | DS p.3, Table 5-1 Pin Functions: D, DDF and DGK Packages (continued), REF2 (pin 3) |
| 4 | GND | power_in | DS name NC: 'Reserved. Connect to ground.' (DS TYPE column: Ground). Named GND here so the wrapper ties it to ground: pcb lint symbol.pin.nc_type rejects a pin named NC that is not no_connect, and a no_connect pin cannot follow the DS instruction. Same rule as an exposed pad that must connect to a net (CLAUDE.md Defaults). | DS p.2, Table 5-1 Pin Functions: D, DDF and DGK Packages, NC (pin 4) |
| 5 | OUT | output | Output voltage | DS p.2, Table 5-1 Pin Functions: D, DDF and DGK Packages, OUT (pin 5) |
| 6 | VS | power_in | Power supply, 2.7 V to 20 V | DS p.3, Table 5-1 Pin Functions: D, DDF and DGK Packages (continued), VS (pin 6) |
| 7 | REF1 | input | Reference 1 voltage. Connect to voltage potential from 0 V to VS; see Adjusting the Output With the Reference Pins | DS p.3, Table 5-1 Pin Functions: D, DDF and DGK Packages (continued), REF1 (pin 7) |
| 8 | IN+ | input | Current-sense amplifier positive input. High-side: connect to bus-voltage side of sense resistor. Low-side: connect to load side of sense resistor | DS p.2, Table 5-1 Pin Functions: D, DDF and DGK Packages, IN+ (pin 8) |

## Parameters: abs_max

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Supply voltage | VS |  |  | 22 | V | over operating free-air temperature range (unless otherwise noted) Note: Only a MAX is printed (MIN column blank). No reference pin is printed for this row; applied as VS vs GND. | DS p.4, 6.1 Absolute Maximum Ratings, Supply voltage (VS) |  |
| Analog inputs, differential voltage | V(IN+) - V(IN-) | -30 (rel. IN-) |  | 30 (rel. IN-) | V | over operating free-air temperature range (unless otherwise noted) Note: Pin-pair row: IN+ relative to IN- (footnote 2: VIN+ and VIN- are the voltages at the IN+ and IN- pins). The second pin is the reference (SPEC pin-pair rule). | DS p.4, 6.1 Absolute Maximum Ratings, Analog inputs VIN+, VIN-, Differential (VIN+) - (VIN-) |  |
| Analog inputs, common-mode voltage | VIN+, VIN- | -20 |  | 120 | V | over operating free-air temperature range (unless otherwise noted) Note: Each input pin voltage. No reference pin is printed; applied as each pin vs GND (system 0 V). | DS p.4, 6.1 Absolute Maximum Ratings, Analog inputs VIN+, VIN-, Common-mode |  |
| REF1, REF2, NC inputs | VREF1, VREF2, VNC | -0.3 (rel. GND) |  | 0.3 (rel. VS) | V | over operating free-air temperature range (unless otherwise noted) Note: Printed GND - 0.3 V to VS + 0.3 V: the DS states the reference is GND, so min_ref = GND and max_ref = VS (SPEC rule). The NC pin (symbol name GND, pin 4) is not checked separately: it is tied to GND, the reference of this row. | DS p.4, 6.1 Absolute Maximum Ratings, REF1, REF2, NC inputs |  |
| Output pin | VOUT | -0.3 (rel. GND) |  | 0.3 (rel. VS) | V | over operating free-air temperature range (unless otherwise noted) Note: Printed GND - 0.3 V to VS + 0.3 V; reference GND as printed in the row. | DS p.4, 6.1 Absolute Maximum Ratings, Output |  |
| Operating temperature | TA | -55 |  | 150 | degC | operating temperature | DS p.4, 6.1 Absolute Maximum Ratings, Operating temperature, TA |  |
| Junction temperature | TJ |  |  | 150 | degC |  | DS p.4, 6.1 Absolute Maximum Ratings, Junction temperature, TJ |  |
| Storage temperature | Tstg | -65 |  | 150 | degC |  | DS p.4, 6.1 Absolute Maximum Ratings, Storage temperature, Tstg |  |
| Electrostatic discharge, human body model | V(ESD) | -2000 |  | 2000 | V | HBM per ANSI/ESDA/JEDEC JS-001, all pins Note: Printed +/-2000 V (footnote 1: JEP155, 500 V HBM is safe in standard ESD control). | DS p.4, 6.2 ESD Ratings, Human body model (HBM) |  |
| Electrostatic discharge, charged device model | V(ESD) | -1000 |  | 1000 | V | CDM per ANSI/ESDA/JEDEC JS-002, all pins Note: Printed +/-1000 V (footnote 2: JEP157, 250 V CDM). | DS p.4, 6.2 ESD Ratings, Charged device model (CDM) |  |

## Parameters: rec_op

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Common-mode input range | VCM | -5 | 48 | 110 | V | over operating free-air temperature range (unless otherwise noted) Note: NOM 48 V stored as typ. Common-mode voltage at both VIN+ and VIN- (DS p.7, footnote 1). | DS p.4, 6.3 Recommended Operating Conditions, Common-mode input range, VCM |  |
| Operating supply range | VS | 2.7 | 5 | 20 | V | over operating free-air temperature range (unless otherwise noted) Note: NOM 5 V stored as typ. No reference pin printed; applied as VS vs GND. | DS p.4, 6.3 Recommended Operating Conditions, Operating supply range, VS |  |
| Ambient temperature | TA | -40 |  | 125 | degC | over operating free-air temperature range | DS p.4, 6.3 Recommended Operating Conditions, Ambient temperature, TA |  |

## Parameters: electrical

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Common-mode input range | VCM | -5 |  | 110 | V | VIN+, VIN- = -5 V to 110 V, VSENSE = 0 mV, TA = -40 degC to 125 degC Note: Same range as vcm_rec. Footnote 1: common-mode voltage at both VIN+ and VIN- must not exceed the range. | DS p.5, 6.5 Electrical Characteristics, INPUT, Common-mode input range (footnote 1) |  |
| Common-mode rejection ratio, input-referred | CMRR | 150 | 166 |  | dB | VIN+, VIN- = -5 V to 110 V, VSENSE = 0 mV, TA = -40 degC to 125 degC Variants: INA241A1IDGK, INA241A2IDGK, INA241A3IDGK, INA241A4IDGK, INA241A5IDGK. Note: Printed for INA241A (all A devices). No MAX printed. | DS p.5, 6.5 Electrical Characteristics, INPUT, Common-mode rejection ratio, input-referred, INA241A |  |
| Common-mode rejection ratio, input-referred | CMRR | 120 | 130 |  | dB | VIN+, VIN- = -5 V to 110 V, VSENSE = 0 mV, TA = -40 degC to 125 degC Variants: INA241B1IDGK, INA241B2IDGK, INA241B3IDGK, INA241B4IDGK, INA241B5IDGK. Note: Printed for INA241B (all B devices). No MAX printed. | DS p.5, 6.5 Electrical Characteristics, INPUT, Common-mode rejection ratio, input-referred, INA241B |  |
| Common-mode rejection ratio, input-referred, f = 50 kHz | CMRR |  | 105 |  | dB | f = 50 kHz (TA = 25 degC) Note: The row has no version label, so it is read as all 10 devices. Ambiguity: the DS does not say; open item. | DS p.5, 6.5 Electrical Characteristics, INPUT, Common-mode rejection ratio, input-referred, f = 50kHz |  |
| Input bias current | IB | 25 | 35 | 45 | uA | IB+, IB-, VSENSE = 0 mV Note: Printed as positive magnitudes per input pin; stored as printed (not a +/- row). | DS p.5, 6.5 Electrical Characteristics, INPUT, Input bias current, IB |  |
| Reference input range |  | 0 (rel. GND) |  | 0 (rel. VS) | V | Note: Printed 0 V to VS: rail-relative, min = 0 vs GND and max = 0 vs VS (users call part.resolve()). | DS p.5, 6.5 Electrical Characteristics, INPUT, Reference input range |  |
| Power-supply rejection ratio, input-referred | PSRR | -1 | ±0.2 | 1 | uV/V | VS = 2.7 V to 20 V, VSENSE = 0 mV, VREF1 = VREF2 = 1 V, TA = -40 degC to 125 degC Variants: INA241A1IDGK. Note: TYP printed +/-0.2, MAX +/-1: stored as typ_pm with min = -max, max = max (SPEC +/- rule). | DS p.5, 6.5 Electrical Characteristics, INPUT, Power-supply rejection ratio, input-referred, INA241A1 |  |
| Power-supply rejection ratio, input-referred | PSRR | -0.75 | ±0.1 | 0.75 | uV/V | VS = 2.7 V to 20 V, VSENSE = 0 mV, VREF1 = VREF2 = 1 V, TA = -40 degC to 125 degC Variants: INA241A2IDGK. Note: TYP printed +/-0.1, MAX +/-0.75: typ_pm, min = -max. | DS p.5, 6.5 Electrical Characteristics, INPUT, Power-supply rejection ratio, input-referred, INA241A2 |  |
| Power-supply rejection ratio, input-referred | PSRR | -0.5 | ±0.06 | 0.5 | uV/V | VS = 2.7 V to 20 V, VSENSE = 0 mV, VREF1 = VREF2 = 1 V, TA = -40 degC to 125 degC Variants: INA241A3IDGK, INA241A4IDGK, INA241A5IDGK. Note: TYP printed +/-0.06, MAX +/-0.5: typ_pm, min = -max. | DS p.5, 6.5 Electrical Characteristics, INPUT, Power-supply rejection ratio, input-referred, INA241A3, INA241A4, INA241A5 |  |
| Power-supply rejection ratio, input-referred | PSRR | -10 | ±1 | 10 | uV/V | VS = 2.7 V to 20 V, VSENSE = 0 mV, VREF1 = VREF2 = 1 V, TA = -40 degC to 125 degC Variants: INA241B1IDGK, INA241B2IDGK, INA241B3IDGK, INA241B4IDGK, INA241B5IDGK. Note: TYP printed +/-1, MAX +/-10: typ_pm, min = -max. | DS p.5, 6.5 Electrical Characteristics, INPUT, Power-supply rejection ratio, input-referred, INA241B |  |
| Reference voltage rejection ratio, input-referred | RVRR | -2.5 | ±1 | 2.5 | uV/V | VREF1 = VREF2 = 0.5 V to 4.5 V, TA = -40 degC to 125 degC Variants: INA241A1IDGK. Note: TYP printed +/-1, MAX +/-2.5: typ_pm, min = -max. | DS p.6, 6.5 Electrical Characteristics, REFERENCE INPUT, Reference voltage rejection ratio, input-referred, INA241A1 |  |
| Reference voltage rejection ratio, input-referred | RVRR | -1.5 | ±0.5 | 1.5 | uV/V | VREF1 = VREF2 = 0.5 V to 4.5 V, TA = -40 degC to 125 degC Variants: INA241A2IDGK, INA241A3IDGK, INA241A4IDGK, INA241A5IDGK. Note: TYP printed +/-0.5, MAX +/-1.5: typ_pm, min = -max. | DS p.6, 6.5 Electrical Characteristics, REFERENCE INPUT, Reference voltage rejection ratio, input-referred, INA241A2 to INA241A5 |  |
| Reference voltage rejection ratio, input-referred | RVRR | -20 | ±10 | 20 | uV/V | VREF1 = VREF2 = 0.5 V to 4.5 V, TA = -40 degC to 125 degC Variants: INA241B1IDGK, INA241B2IDGK, INA241B3IDGK, INA241B4IDGK, INA241B5IDGK. Note: TYP printed +/-10, MAX +/-20: typ_pm, min = -max. | DS p.6, 6.5 Electrical Characteristics, REFERENCE INPUT, Reference voltage rejection ratio, input-referred, INA241B |  |
| Reference divider accuracy | VOUT | -0.005 | ±0.002 | 0.005 | % | VOUT = \|(VREF1 + VREF2)\| / 2 at VSENSE = 0 mV, VREF1 = VS / VREF2 = GND and VREF1 = GND / VREF2 = VS, TA = -40 degC to 125 degC Variants: INA241A1IDGK, INA241A2IDGK. Note: TYP printed +/-0.002 %, MAX +/-0.005 %: typ_pm, min = -max. Percent, loader converts to a fraction. | DS p.6, 6.5 Electrical Characteristics, REFERENCE INPUT, Reference divider accuracy, INA241A1, INA241A2 |  |
| Reference divider accuracy | VOUT | -0.01 | ±0.002 | 0.01 | % | VOUT = \|(VREF1 + VREF2)\| / 2 at VSENSE = 0 mV, VREF1 = VS / VREF2 = GND and VREF1 = GND / VREF2 = VS, TA = -40 degC to 125 degC Variants: INA241A3IDGK, INA241A4IDGK, INA241A5IDGK. Note: TYP printed +/-0.002 %, MAX +/-0.01 %: typ_pm, min = -max. | DS p.6, 6.5 Electrical Characteristics, REFERENCE INPUT, Reference divider accuracy, INA241A3, INA241A4, INA241A5 |  |
| Reference divider accuracy | VOUT | -0.15 | ±0.02 | 0.15 | % | VOUT = \|(VREF1 + VREF2)\| / 2 at VSENSE = 0 mV, VREF1 = VS / VREF2 = GND and VREF1 = GND / VREF2 = VS, TA = -40 degC to 125 degC Variants: INA241B1IDGK, INA241B2IDGK, INA241B3IDGK, INA241B4IDGK, INA241B5IDGK. Note: TYP printed +/-0.02 %, MAX +/-0.15 %: typ_pm, min = -max. | DS p.6, 6.5 Electrical Characteristics, REFERENCE INPUT, Reference divider accuracy, INA241B |  |
| Non-linearity error |  |  | ±0.001 |  | % | Note: Printed +/-0.001 % in the TYP column, no MAX: typ_pm, typ = 0 with spread 0.001 (loader). | DS p.6, 6.5 Electrical Characteristics, GERR, Non-linearity error |  |
| Maximum capacitive load |  |  | 1 |  | nF | no sustained oscillations, no isolation resistor Note: Printed in the TYP column (1 nF); stored as typ. | DS p.6, 6.5 Electrical Characteristics, GERR, Maximum capacitive load |  |
| Offset voltage, input-referred | VOS | -150 | ±25 | 150 | uV | VSENSE = 0 mV, INA241B (TA = 25 degC) Variants: INA241B1IDGK, INA241B2IDGK, INA241B3IDGK, INA241B4IDGK, INA241B5IDGK. Note: TYP printed +/-25, MAX +/-150: typ_pm, min = -max. A devices: per-variant rows in variants.toml. Used by calc.current_error (INPUTS 'vos'). | DS p.5, 6.5 Electrical Characteristics, INPUT, Offset voltage, input-referred, INA241B |  |
| Offset voltage drift, input-referred | dVOS/dT | -500 | ±100 | 500 | nV/degC | TA = -40 degC to 125 degC, INA241B Variants: INA241B1IDGK, INA241B2IDGK, INA241B3IDGK, INA241B4IDGK, INA241B5IDGK. Note: TYP printed +/-100, MAX +/-500: typ_pm, min = -max. A devices: per-variant rows in variants.toml. Used by calc.current_error (INPUTS 'vos_drift'). | DS p.5, 6.5 Electrical Characteristics, INPUT, Offset voltage drift, input-referred, INA241B |  |
| Gain error | GERR | -0.1 | ±0.02 | 0.1 | % | (GND + 50 mV) < VOUT < (VS - 200 mV), INA241B (TA = 25 degC) Variants: INA241B1IDGK, INA241B2IDGK, INA241B3IDGK, INA241B4IDGK, INA241B5IDGK. Note: TYP printed +/-0.02 %, MAX +/-0.1 %: typ_pm, min = -max. A devices: per-variant rows in variants.toml. Used by calc.current_error (INPUTS 'gain_err'). | DS p.6, 6.5 Electrical Characteristics, OUTPUT, GERR, Gain error, INA241B |  |
| Gain error drift | GERR drift | -5 | ±0.2 | 5 | ppm/degC | TA = -40 degC to 125 degC, INA241B Variants: INA241B1IDGK, INA241B2IDGK, INA241B3IDGK, INA241B4IDGK, INA241B5IDGK. Note: TYP printed +/-0.2, MAX +/-5 ppm/degC: typ_pm, min = -max. A devices: per-variant rows in variants.toml. Used by calc.current_error (INPUTS 'gain_drift'). | DS p.6, 6.5 Electrical Characteristics, OUTPUT, GERR, Gain error drift, INA241B |  |
| Swing to VS power supply rail |  | -0.2 (rel. VS) | -0.07 (rel. VS) |  | V | RL = 10 kohm to GND, TA = -40 degC to 125 degC Note: Printed TYP VS - 0.07 V, MAX VS - 0.2 V (magnitude order: the MAX swing from the rail is the lowest output high level). Stored numerically: printed MAX -> min = -0.2 V, min_ref = VS; output high reaches at least VS - 0.2 V. | DS p.6, 6.5 Electrical Characteristics, VOLTAGE OUTPUT, Swing to VS power supply rail |  |
| Swing to ground |  |  | 8 | 20 | mV | RL = 10 kohm to GND, VSENSE = 0 mV, VREF1 = VREF2 = 0 V, TA = -40 degC to 125 degC | DS p.6, 6.5 Electrical Characteristics, VOLTAGE OUTPUT, Swing to ground |  |
| Bandwidth |  |  | 1.1 |  | MHz | all gains, -3 dB bandwidth | DS p.6, 6.5 Electrical Characteristics, FREQUENCY RESPONSE, Bandwidth, BW |  |
| Settling time to 0.5 % |  |  | 1.5 |  | us | VIN+, VIN- = 48 V, VOUT = 0.5 V to 4.5 V, output settles to 0.5 % | DS p.6, 6.5 Electrical Characteristics, FREQUENCY RESPONSE, Settling time, settles to 0.5 % |  |
| Settling time to 1 % |  |  | 1 |  | us | VIN+, VIN- = 48 V, VOUT = 0.5 V to 4.5 V, output settles to 1 % | DS p.6, 6.5 Electrical Characteristics, FREQUENCY RESPONSE, Settling time, settles to 1 % |  |
| Settling time to 5 % |  |  | 0.5 |  | us | VIN+, VIN- = 48 V, VOUT = 0.5 V to 4.5 V, output settles to 5 % | DS p.6, 6.5 Electrical Characteristics, FREQUENCY RESPONSE, Settling time, settles to 5 % |  |
| Slew rate, rising | SR |  | 8 |  | V/us | rising | DS p.6, 6.5 Electrical Characteristics, FREQUENCY RESPONSE, Slew rate, SR |  |
| Voltage noise density, input-referred, gain 10 V/V | eN |  | 62 |  | nV/rtHz | input referred, TA = 25 degC Variants: INA241A1IDGK, INA241B1IDGK. Note: Typical only (no MIN/MAX printed). Not a bound. | DS p.7, 6.5 Electrical Characteristics, NOISE (Input referred), Voltage noise density, A1, B1 devices |  |
| Voltage noise density, input-referred, gain 20 V/V | eN |  | 49 |  | nV/rtHz | input referred, TA = 25 degC Variants: INA241A2IDGK, INA241B2IDGK. Note: Typical only. Not a bound. | DS p.7, 6.5 Electrical Characteristics, NOISE (Input referred), Voltage noise density, A2, B2 devices |  |
| Voltage noise density, input-referred, gain 50 V/V | eN |  | 39 |  | nV/rtHz | input referred, TA = 25 degC Variants: INA241A3IDGK, INA241B3IDGK. Note: Typical only. Not a bound. | DS p.7, 6.5 Electrical Characteristics, NOISE (Input referred), Voltage noise density, A3, B3 devices |  |
| Voltage noise density, input-referred, gain 100 V/V | eN |  | 36 |  | nV/rtHz | input referred, TA = 25 degC Variants: INA241A4IDGK, INA241B4IDGK. Note: Typical only. Not a bound. | DS p.7, 6.5 Electrical Characteristics, NOISE (Input referred), Voltage noise density, A4, B4 devices |  |
| Voltage noise density, input-referred, gain 200 V/V | eN |  | 28 |  | nV/rtHz | input referred, TA = 25 degC Variants: INA241A5IDGK, INA241B5IDGK. Note: Typical only. Not a bound. | DS p.7, 6.5 Electrical Characteristics, NOISE (Input referred), Voltage noise density, A5, B5 devices |  |
| Supply voltage | VS | 2.7 |  | 20 | V |  | DS p.7, 6.5 Electrical Characteristics, POWER SUPPLY, Supply voltage, VS |  |
| Quiescent current | IQ |  | 2.5 | 3 | mA | VSENSE = 0 mV | DS p.7, 6.5 Electrical Characteristics, POWER SUPPLY, Quiescent current, VSENSE = 0 mV |  |
| Quiescent current | IQ |  |  | 3.2 | mA | VSENSE = 0 mV, TA = -40 degC to +125 degC Note: Only MAX printed for the full range. | DS p.7, 6.5 Electrical Characteristics, POWER SUPPLY, Quiescent current, TA = -40 degC to +125 degC |  |
| Specified range | TA | -40 |  | 125 | degC | specified range | DS p.7, 6.5 Electrical Characteristics, TEMPERATURE, Specified range, TA |  |

## Parameters: thermal

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Junction-to-ambient thermal resistance | RthetaJA |  | 167.2 |  | degC/W | DGK (VSSOP), 8 pins Note: Single printed value, stored as typ. | DS p.4, 6.4 Thermal Information, Junction-to-ambient thermal resistance, DGK column |  |
| Junction-to-case (top) thermal resistance | RthetaJC(top) |  | 58.9 |  | degC/W | DGK (VSSOP), 8 pins Note: Single printed value, stored as typ. | DS p.4, 6.4 Thermal Information, Junction-to-case (top) thermal resistance, DGK column |  |
| Junction-to-board thermal resistance | RthetaJB |  | 88.9 |  | degC/W | DGK (VSSOP), 8 pins Note: Single printed value, stored as typ. | DS p.4, 6.4 Thermal Information, Junction-to-board thermal resistance, DGK column |  |
| Junction-to-top characterization parameter | PsiJT |  | 8.1 |  | degC/W | DGK (VSSOP), 8 pins Note: Single printed value, stored as typ. | DS p.4, 6.4 Thermal Information, Junction-to-top characterization parameter, DGK column |  |
| Junction-to-board characterization parameter | PsiJB |  | 87.4 |  | degC/W | DGK (VSSOP), 8 pins Note: Single printed value, stored as typ. | DS p.4, 6.4 Thermal Information, Junction-to-board characterization parameter, DGK column |  |

## Variant-specific parameters: INA241A1IDGK

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Gain | G |  | 10 |  |  | VS = 5 V, VSENSE = VIN+ - VIN-, VCM = VIN- = 48 V, VREF1 = VREF2 = VS / 2 (TA = 25 degC) Note: Typical only (no MIN or MAX printed for gain). Per-variant row: the gain is set by the device version. | DS p.5, 6.5 Electrical Characteristics, OUTPUT, Gain, A1, B1 Devices row |  |
| Gain error | GERR | -0.01 | ±0.002 | 0.01 | % | (GND + 50 mV) < VOUT < (VS - 200 mV), TA = 25 degC Note: TYP printed +/-, MAX printed +/-: typ_pm, min = -max. Per-variant row (A devices). | DS p.6, 6.5 Electrical Characteristics, OUTPUT, GERR, Gain error, INA241A1, INA241A2, INA241A3 |  |
| Gain error drift | GERR drift | -1 | ±0.05 | 1 | ppm/degC | TA = -40 degC to 125 degC Note: TYP printed +/-, MAX printed +/-: typ_pm, min = -max. Per-variant row (A devices). | DS p.6, 6.5 Electrical Characteristics, OUTPUT, GERR, Gain error drift, INA241A1, INA241A2, INA241A3 |  |
| Offset voltage, input-referred | VOS | -20 | ±5 | 20 | uV | VSENSE = 0 mV (TA = 25 degC) Note: TYP printed +/-, MAX printed +/-: typ_pm, min = -max. Per-variant row (A devices). | DS p.5, 6.5 Electrical Characteristics, INPUT, Offset voltage, input-referred, INA241A1 |  |
| Offset voltage drift, input-referred | dVOS/dT | -250 | ±50 | 250 | nV/degC | TA = -40 degC to 125 degC Note: TYP printed +/-, MAX printed +/-: typ_pm, min = -max. Per-variant row (A devices). | DS p.5, 6.5 Electrical Characteristics, INPUT, Offset voltage drift, input-referred, INA241A1 |  |

## Variant-specific parameters: INA241A2IDGK

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Gain | G |  | 20 |  |  | VS = 5 V, VSENSE = VIN+ - VIN-, VCM = VIN- = 48 V, VREF1 = VREF2 = VS / 2 (TA = 25 degC) Note: Typical only (no MIN or MAX printed for gain). Per-variant row: the gain is set by the device version. | DS p.5, 6.5 Electrical Characteristics, OUTPUT, Gain, A2, B2 Devices row |  |
| Gain error | GERR | -0.01 | ±0.002 | 0.01 | % | (GND + 50 mV) < VOUT < (VS - 200 mV), TA = 25 degC Note: TYP printed +/-, MAX printed +/-: typ_pm, min = -max. Per-variant row (A devices). | DS p.6, 6.5 Electrical Characteristics, OUTPUT, GERR, Gain error, INA241A1, INA241A2, INA241A3 |  |
| Gain error drift | GERR drift | -1 | ±0.05 | 1 | ppm/degC | TA = -40 degC to 125 degC Note: TYP printed +/-, MAX printed +/-: typ_pm, min = -max. Per-variant row (A devices). | DS p.6, 6.5 Electrical Characteristics, OUTPUT, GERR, Gain error drift, INA241A1, INA241A2, INA241A3 |  |
| Offset voltage, input-referred | VOS | -15 | ±3 | 15 | uV | VSENSE = 0 mV (TA = 25 degC) Note: TYP printed +/-, MAX printed +/-: typ_pm, min = -max. Per-variant row (A devices). | DS p.5, 6.5 Electrical Characteristics, INPUT, Offset voltage, input-referred, INA241A2 |  |
| Offset voltage drift, input-referred | dVOS/dT | -150 | ±30 | 150 | nV/degC | TA = -40 degC to 125 degC Note: TYP printed +/-, MAX printed +/-: typ_pm, min = -max. Per-variant row (A devices). | DS p.5, 6.5 Electrical Characteristics, INPUT, Offset voltage drift, input-referred, INA241A2 |  |

## Variant-specific parameters: INA241A3IDGK

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Gain | G |  | 50 |  |  | VS = 5 V, VSENSE = VIN+ - VIN-, VCM = VIN- = 48 V, VREF1 = VREF2 = VS / 2 (TA = 25 degC) Note: Typical only (no MIN or MAX printed for gain). Per-variant row: the gain is set by the device version. | DS p.5, 6.5 Electrical Characteristics, OUTPUT, Gain, A3, B3 Devices row |  |
| Gain error | GERR | -0.01 | ±0.002 | 0.01 | % | (GND + 50 mV) < VOUT < (VS - 200 mV), TA = 25 degC Note: TYP printed +/-, MAX printed +/-: typ_pm, min = -max. Per-variant row (A devices). | DS p.6, 6.5 Electrical Characteristics, OUTPUT, GERR, Gain error, INA241A1, INA241A2, INA241A3 |  |
| Gain error drift | GERR drift | -1 | ±0.05 | 1 | ppm/degC | TA = -40 degC to 125 degC Note: TYP printed +/-, MAX printed +/-: typ_pm, min = -max. Per-variant row (A devices). | DS p.6, 6.5 Electrical Characteristics, OUTPUT, GERR, Gain error drift, INA241A1, INA241A2, INA241A3 |  |
| Offset voltage, input-referred | VOS | -10 | ±3 | 10 | uV | VSENSE = 0 mV (TA = 25 degC) Note: TYP printed +/-, MAX printed +/-: typ_pm, min = -max. Per-variant row (A devices). | DS p.5, 6.5 Electrical Characteristics, INPUT, Offset voltage, input-referred, INA241A3, INA241A4 |  |
| Offset voltage drift, input-referred | dVOS/dT | -100 | ±20 | 100 | nV/degC | TA = -40 degC to 125 degC Note: TYP printed +/-, MAX printed +/-: typ_pm, min = -max. Per-variant row (A devices). | DS p.5, 6.5 Electrical Characteristics, INPUT, Offset voltage drift, input-referred, INA241A3, INA241A4, INA241A5 |  |

## Variant-specific parameters: INA241A4IDGK

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Gain | G |  | 100 |  |  | VS = 5 V, VSENSE = VIN+ - VIN-, VCM = VIN- = 48 V, VREF1 = VREF2 = VS / 2 (TA = 25 degC) Note: Typical only (no MIN or MAX printed for gain). Per-variant row: the gain is set by the device version. | DS p.5, 6.5 Electrical Characteristics, OUTPUT, Gain, A4, B4 Devices row |  |
| Gain error | GERR | -0.015 | ±0.003 | 0.015 | % | (GND + 50 mV) < VOUT < (VS - 200 mV), TA = 25 degC Note: TYP printed +/-, MAX printed +/-: typ_pm, min = -max. Per-variant row (A devices). | DS p.6, 6.5 Electrical Characteristics, OUTPUT, GERR, Gain error, INA241A4, INA241A5 |  |
| Gain error drift | GERR drift | -2 | ±0.1 | 2 | ppm/degC | TA = -40 degC to 125 degC Note: TYP printed +/-, MAX printed +/-: typ_pm, min = -max. Per-variant row (A devices). | DS p.6, 6.5 Electrical Characteristics, OUTPUT, GERR, Gain error drift, INA241A4, INA241A5 |  |
| Offset voltage, input-referred | VOS | -10 | ±3 | 10 | uV | VSENSE = 0 mV (TA = 25 degC) Note: TYP printed +/-, MAX printed +/-: typ_pm, min = -max. Per-variant row (A devices). | DS p.5, 6.5 Electrical Characteristics, INPUT, Offset voltage, input-referred, INA241A3, INA241A4 |  |
| Offset voltage drift, input-referred | dVOS/dT | -100 | ±20 | 100 | nV/degC | TA = -40 degC to 125 degC Note: TYP printed +/-, MAX printed +/-: typ_pm, min = -max. Per-variant row (A devices). | DS p.5, 6.5 Electrical Characteristics, INPUT, Offset voltage drift, input-referred, INA241A3, INA241A4, INA241A5 |  |

## Variant-specific parameters: INA241A5IDGK

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Gain | G |  | 200 |  |  | VS = 5 V, VSENSE = VIN+ - VIN-, VCM = VIN- = 48 V, VREF1 = VREF2 = VS / 2 (TA = 25 degC) Note: Typical only (no MIN or MAX printed for gain). Per-variant row: the gain is set by the device version. | DS p.5, 6.5 Electrical Characteristics, OUTPUT, Gain, A5, B5 Devices row |  |
| Gain error | GERR | -0.015 | ±0.003 | 0.015 | % | (GND + 50 mV) < VOUT < (VS - 200 mV), TA = 25 degC Note: TYP printed +/-, MAX printed +/-: typ_pm, min = -max. Per-variant row (A devices). | DS p.6, 6.5 Electrical Characteristics, OUTPUT, GERR, Gain error, INA241A4, INA241A5 |  |
| Gain error drift | GERR drift | -2 | ±0.1 | 2 | ppm/degC | TA = -40 degC to 125 degC Note: TYP printed +/-, MAX printed +/-: typ_pm, min = -max. Per-variant row (A devices). | DS p.6, 6.5 Electrical Characteristics, OUTPUT, GERR, Gain error drift, INA241A4, INA241A5 |  |
| Offset voltage, input-referred | VOS | -8 | ±2 | 8 | uV | VSENSE = 0 mV (TA = 25 degC) Note: TYP printed +/-, MAX printed +/-: typ_pm, min = -max. Per-variant row (A devices). | DS p.5, 6.5 Electrical Characteristics, INPUT, Offset voltage, input-referred, INA241A5 |  |
| Offset voltage drift, input-referred | dVOS/dT | -100 | ±20 | 100 | nV/degC | TA = -40 degC to 125 degC Note: TYP printed +/-, MAX printed +/-: typ_pm, min = -max. Per-variant row (A devices). | DS p.5, 6.5 Electrical Characteristics, INPUT, Offset voltage drift, input-referred, INA241A3, INA241A4, INA241A5 |  |

## Variant-specific parameters: INA241B1IDGK

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Gain | G |  | 10 |  |  | VS = 5 V, VSENSE = VIN+ - VIN-, VCM = VIN- = 48 V, VREF1 = VREF2 = VS / 2 (TA = 25 degC) Note: Typical only (no MIN or MAX printed for gain). Per-variant row: the gain is set by the device version. | DS p.5, 6.5 Electrical Characteristics, OUTPUT, Gain, A1, B1 Devices row |  |

## Variant-specific parameters: INA241B2IDGK

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Gain | G |  | 20 |  |  | VS = 5 V, VSENSE = VIN+ - VIN-, VCM = VIN- = 48 V, VREF1 = VREF2 = VS / 2 (TA = 25 degC) Note: Typical only (no MIN or MAX printed for gain). Per-variant row: the gain is set by the device version. | DS p.5, 6.5 Electrical Characteristics, OUTPUT, Gain, A2, B2 Devices row |  |

## Variant-specific parameters: INA241B3IDGK

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Gain | G |  | 50 |  |  | VS = 5 V, VSENSE = VIN+ - VIN-, VCM = VIN- = 48 V, VREF1 = VREF2 = VS / 2 (TA = 25 degC) Note: Typical only (no MIN or MAX printed for gain). Per-variant row: the gain is set by the device version. | DS p.5, 6.5 Electrical Characteristics, OUTPUT, Gain, A3, B3 Devices row |  |

## Variant-specific parameters: INA241B4IDGK

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Gain | G |  | 100 |  |  | VS = 5 V, VSENSE = VIN+ - VIN-, VCM = VIN- = 48 V, VREF1 = VREF2 = VS / 2 (TA = 25 degC) Note: Typical only (no MIN or MAX printed for gain). Per-variant row: the gain is set by the device version. | DS p.5, 6.5 Electrical Characteristics, OUTPUT, Gain, A4, B4 Devices row |  |

## Variant-specific parameters: INA241B5IDGK

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Gain | G |  | 200 |  |  | VS = 5 V, VSENSE = VIN+ - VIN-, VCM = VIN- = 48 V, VREF1 = VREF2 = VS / 2 (TA = 25 degC) Note: Typical only (no MIN or MAX printed for gain). Per-variant row: the gain is set by the device version. | DS p.5, 6.5 Electrical Characteristics, OUTPUT, Gain, A5, B5 Devices row |  |

## Limits of this data

Rows by scope: 25C 39, full 28, na 19 (25C rows hold only at 25 degC). Curve (graph) rows: 0. Text rows: 0.

## Zener checks

Generated wrapper: `<Variant>.zen` (`python3 -m lib.zen`). abs_max and rec_op rows are errors (abs_max x derate); 25C and partial rows are waivable warnings; a checked net with no voltage is UNVERIFIED.

| Param | Name | Checked against | Not checked / reason |
|---|---|---|---|
| vs_abs | Supply voltage | UNCHECKED | covered by vs_rec (2.7 V to 20 V, checked, error), which is stricter |
| vdiff_abs | Analog inputs, differential voltage | pins IN+ |  |
| vcm_abs | Analog inputs, common-mode voltage | UNCHECKED | covered by vcm_rec (-5 V to 110 V, checked, error), which is stricter |
| vref_abs | REF1, REF2, NC inputs | pins REF1, REF2 |  |
| vout_abs | Output pin | UNCHECKED | OUT is driven by the part; owner: module |
| ta_abs | Operating temperature | UNCHECKED | covered by ta_rec (-40 degC to 125 degC, check_ambient, error), which is stricter |
| tj_abs | Junction temperature | UNCHECKED | needs dissipation x RthetaJA; owner: module |
| tstg_abs | Storage temperature | UNCHECKED | owner: assembly |
| esd_hbm | Electrostatic discharge, human body model | UNCHECKED | owner: assembly |
| esd_cdm | Electrostatic discharge, charged device model | UNCHECKED | owner: assembly |
| vcm_rec | Common-mode input range | pins IN+, IN- |  |
| vs_rec | Operating supply range | pins VS |  |
| ta_rec | Ambient temperature | board ambient |  |
| vref_range_25c | Reference input range | pins REF1, REF2 |  |

### Zener checks: variant INA241A1IDGK

No Zener checks declared.

### Zener checks: variant INA241A2IDGK

No Zener checks declared.

### Zener checks: variant INA241A3IDGK

No Zener checks declared.

### Zener checks: variant INA241A4IDGK

No Zener checks declared.

### Zener checks: variant INA241A5IDGK

No Zener checks declared.

### Zener checks: variant INA241B1IDGK

No Zener checks declared.

### Zener checks: variant INA241B2IDGK

No Zener checks declared.

### Zener checks: variant INA241B3IDGK

No Zener checks declared.

### Zener checks: variant INA241B4IDGK

No Zener checks declared.

### Zener checks: variant INA241B5IDGK

No Zener checks declared.

## Equations

### `vout`

```
VOUT = G x (VIN+ - VIN-) + (VREF1 + VREF2) / 2. DS p.17, 7.4.1 Adjusting the Output With the Reference Pins, Equation 1.
g: gain, V/V. vin_p, vin_n: IN+ and IN- pin voltages, V. vref1, vref2: REF1 and REF2 voltages, V.
Returns: VOUT, V. Assumes the ideal reference network (the reference-divider error is a separate DS row).
```

Inputs:

- `g` -> `gain.typ` (typ 200 )

### `vsense_ideal`

```
VSENSE = VOUT / G. DS p.22, 8.1.1 RSENSE and Device Gain Selection, Table 8-1, row VSENSE.
vout_fs: output voltage at full scale, V. g: gain, V/V. Returns: differential input voltage VSENSE, V.
```

Inputs:

- `g` -> `gain.typ` (typ 200 )

### `rsense_ideal`

```
RSENSE = VSENSE / IMAX. DS p.22, 8.1.1 RSENSE and Device Gain Selection, Table 8-1, row RSENSE.
vsense: differential input at full scale, V. imax: full-scale current, A. Returns: RSENSE, ohm.
```

Inputs:


### `psense`

```
PSENSE = RSENSE x IMAX^2. DS p.22, 8.1.1 RSENSE and Device Gain Selection, Table 8-1, row PSENSE.
rsense: ohm. imax: A. Returns: power dissipated in RSENSE, W.
```

Inputs:


### `rsense_max_power`

```
RSENSE < PDMAX / IMAX^2 (strict). DS p.21, 8.1.1 RSENSE and Device Gain Selection, Equation 2.
Returns the limit (the largest RSENSE allowed by the power budget), ohm. pdmax: W. imax: A.
```

Inputs:


### `vout_at_imax`

```
VOUT_MAX = IMAX x RSENSE x G. DS p.21, 7.4.4 High Signal Throughput, Table 7-1 (VOUT_MAX row).
Also the left side of DS p.21 Equation 3 (IMAX x RSENSE x GAIN < VSP) and DS p.22 Equation 4 (IMIN x RSENSE x GAIN > VSN):
compare the result with the positive swing VSP (DS p.6, swing to VS) or the negative swing VSN.
imax: A. rsense: ohm. g: V/V. Returns: output voltage, V.
```

Inputs:

- `g` -> `gain.typ` (typ 200 )

### `tresponse`

```
Tresponse = VOUT_THR / SR. DS p.21, 7.4.4 High Signal Throughput, Table 7-1 (Tresponse row).
vout_thr: output voltage at the threshold current, V. sr: slew rate, V/s (the DS SR row is V/us; the loader gives V/s).
Returns: response time, s. Uses the typical slew rate (INPUTS sr = slew_rate_25c.typ).
```

Inputs:

- `sr` -> `slew_rate_25c.typ` (typ 8 V/us)

### `current_error`

```
Not a DS equation: input-referred current-measurement error for one device, in A, combining the printed
gain error, its drift, the input offset and its drift (DS p.6 GERR, DS p.5 Vos and dVos/dT, DS p.17 Equation 1).
gf = (1 + gain_err) x (1 + gain_drift x (T - 25)) is the actual gain relative to the nominal G (SPEC recipe:
25 degC row plus drift x (T - 25)); vos_t = vos + vos_drift x (T - 25).
The output is VOUT = G x gf x (VSENSE + vos_t) + VREF, so the sensed VSENSE is gf x (VSENSE + vos_t) and the error
is vsense x (gf - 1) + gf x vos_t, divided by RSENSE to give current.
rsense: ohm. vsense: true differential input at this current (= I x RSENSE), V. gain_err: fraction, signed.
gain_drift: 1/degC, signed. t_c: degC. vos: V, signed. vos_drift: V/degC, signed. Returns: current error, A.
Corners are not monotone in t_c (t_c enters with a product of drift terms), so use wca samples for T.
Gain (G) cancels, so the nominal gain is not an input. Gain error is a 25 degC row (curve-free).
Limits: valid only at the EC table conditions (DS p.5 header: VCM = 48 V, VS = 5 V, VREF1 = VREF2 = VS/2).
Not included: CMRR x (VCM - 48 V), PSRR x (VS - 5 V) and RVRR x (VREF - VS/2) offset terms (DS p.5 CMRR and
PSRR rows, DS p.6 RVRR row). Away from those conditions add them to vos yourself; for A devices they can be
as large as the offset.
```

Inputs:

- `gain_err` -> `gain_err_25c` (min -0.1 typ ±0.02 max 0.1 %)
- `gain_drift` -> `gain_drift_full` (min -5 typ ±0.2 max 5 ppm/degC)
- `vos` -> `vos_25c` (min -150 typ ±25 max 150 uV)
- `vos_drift` -> `vos_drift_full` (min -500 typ ±100 max 500 nV/degC)


## Examples

| Call | Computed | Expected | Rel. tol | Result | Cite |
|---|---|---|---|---|---|
| vout(g=10, vin_p=0.5, vin_n=0, vref1=0, vref2=0) | 5 | 5 | 0.001 | pass | DS p.22, Table 8-1 (VSENSE = 500 mV at G = 10, output 5 V), with Equation 1 and VREF = 0 V |
| vout(g=10, vin_p=0, vin_n=0, vref1=5, vref2=0) | 2.5 | 2.5 | 0.001 | pass | DS p.17, 7.4.1, Equation 1 and text: mid-point of REF1 and REF2 at VSENSE = 0 |
| vsense_ideal(vout_fs=5, g=10) | 0.5 | 0.5 | 0.001 | pass | DS p.22, Table 8-1, G 10 V/V, VSENSE 500 mV |
| vsense_ideal(vout_fs=5, g=20) | 0.25 | 0.25 | 0.001 | pass | DS p.22, Table 8-1, G 20 V/V, VSENSE 250 mV |
| vsense_ideal(vout_fs=5, g=50) | 0.1 | 0.1 | 0.001 | pass | DS p.22, Table 8-1, G 50 V/V, VSENSE 100 mV |
| vsense_ideal(vout_fs=5, g=100) | 0.05 | 0.05 | 0.001 | pass | DS p.22, Table 8-1, G 100 V/V, VSENSE 50 mV |
| vsense_ideal(vout_fs=5, g=200) | 0.025 | 0.025 | 0.001 | pass | DS p.22, Table 8-1, G 200 V/V, VSENSE 25 mV |
| rsense_ideal(vsense=0.5, imax=10) | 0.05 | 0.05 | 0.001 | pass | DS p.22, Table 8-1, G 10 V/V, RSENSE 50 mohm |
| rsense_ideal(vsense=0.25, imax=10) | 0.025 | 0.025 | 0.001 | pass | DS p.22, Table 8-1, G 20 V/V, RSENSE 25 mohm |
| rsense_ideal(vsense=0.1, imax=10) | 0.01 | 0.01 | 0.001 | pass | DS p.22, Table 8-1, G 50 V/V, RSENSE 10 mohm |
| rsense_ideal(vsense=0.05, imax=10) | 0.005 | 0.005 | 0.001 | pass | DS p.22, Table 8-1, G 100 V/V, RSENSE 5 mohm |
| rsense_ideal(vsense=0.025, imax=10) | 0.0025 | 0.0025 | 0.001 | pass | DS p.22, Table 8-1, G 200 V/V, RSENSE 2.5 mohm |
| psense(rsense=0.05, imax=10) | 5 | 5 | 0.001 | pass | DS p.22, Table 8-1, G 10 V/V, PSENSE 5 W |
| psense(rsense=0.025, imax=10) | 2.5 | 2.5 | 0.001 | pass | DS p.22, Table 8-1, G 20 V/V, PSENSE 2.5 W |
| psense(rsense=0.01, imax=10) | 1 | 1 | 0.001 | pass | DS p.22, Table 8-1, G 50 V/V, PSENSE 1 W |
| psense(rsense=0.005, imax=10) | 0.5 | 0.5 | 0.001 | pass | DS p.22, Table 8-1, G 100 V/V, PSENSE 0.5 W |
| psense(rsense=0.0025, imax=10) | 0.25 | 0.25 | 0.001 | pass | DS p.22, Table 8-1, G 200 V/V, PSENSE 0.25 W |
| rsense_max_power(pdmax=5, imax=10) | 0.05 | 0.05 | 0.001 | pass | DS p.21, Equation 2 with DS p.22, Table 8-1 (5 W, 10 A) |
| vout_at_imax(imax=100, rsense=0.002, g=20) | 4 | 4 | 0.001 | pass | DS p.21, Table 7-1, VOUT_MAX 4 V |
| vout_at_imax(imax=75, rsense=0.002, g=20) | 3 | 3 | 0.001 | pass | DS p.21, Table 7-1, VOUT_THR 3 V |
| current_error(rsense=0.1, vsense=0, gain_err=0, gain_drift=0, t_c=25, vos=0, vos_drift=0) | 0 | 0 | 0.001 | pass | Sanity: no error terms give zero (not a DS value) |
| tresponse(vout_thr=3, sr=8e+06) | 3.75e-07 | 3.75e-07 | 0.001 | pass | DS p.21, Table 7-1: Tresponse = VOUT_THR / SR = 3 V / 8 V/us (DS prints < 1 us) |
