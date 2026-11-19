<!-- GENERATED - do not edit. Run: python3 -m lib.readme -->

# INA229AIDGS

## Datasheet review

[![Human page-image review: 0/75 human](https://img.shields.io/badge/human%20review-0%2F75%20human-lightgrey)](datasheet-review/)

Human page-image review: 0/75; cross-model audits: 35; manufacturer-export stamps: 0; legacy/unclassified: 0. Text checks are not verification. `lib.check` validates stamp format, not that review occurred.

## Part

- **mpn**: INA229AIDGSR
- **alternates**: []
- **manufacturer**: Texas Instruments
- **description**: 85 V, 20-bit power/energy/charge monitor with SPI interface
- **category**: power_monitor
- **package**: VSSOP-10 (DGS0010A)
- **datasheet_url**: https://www.ti.com/lit/ds/symlink/ina229.pdf
- **datasheet_file**: docs/datasheets/ina229.pdf
- **datasheet_rev**: SLYS023A
- **datasheet_date**: 2022-05
- **temp_grade**: -40 to 125 degC
- **kicad_symbol**: INA229AIDGS.kicad_sym
- **kicad_footprint**: INA229AIDGS.kicad_mod
- **step**: INA229AIDGS.step

## Pins

| Pin | Name | Type | Function | Cite |
|---|---|---|---|---|
| 1 | CS | input | SPI chip select (Active Low) | DS p.3, 5 Pin Configuration and Functions, Table 5-1 Pin Functions, CS (pin 1) |
| 2 | MOSI | input | SPI digital data input | DS p.3, 5 Pin Configuration and Functions, Table 5-1 Pin Functions, MOSI (pin 2) |
| 3 | ALERT | open_collector | Open-drain alert output, default state is active low | DS p.3, 5 Pin Configuration and Functions, Table 5-1 Pin Functions, ALERT (pin 3) |
| 4 | MISO | output | SPI digital data output (push-pull) | DS p.3, 5 Pin Configuration and Functions, Table 5-1 Pin Functions, MISO (pin 4) |
| 5 | SCLK | input | SPI clock input | DS p.3, 5 Pin Configuration and Functions, Table 5-1 Pin Functions, SCLK (pin 5) |
| 6 | VS | power_in | Power supply, 2.7 V to 5.5 V | DS p.3, 5 Pin Configuration and Functions, Table 5-1 Pin Functions, VS (pin 6) |
| 7 | GND | power_in | Ground | DS p.3, 5 Pin Configuration and Functions, Table 5-1 Pin Functions, GND (pin 7) |
| 8 | VBUS | input | Bus voltage input | DS p.3, 5 Pin Configuration and Functions, Table 5-1 Pin Functions, VBUS (pin 8) |
| 9 | IN- | input | Negative input to the device. High-side: connect to load side of sense resistor. Low-side: connect to ground side of sense resistor | DS p.3, 5 Pin Configuration and Functions, Table 5-1 Pin Functions, IN- (pin 9) |
| 10 | IN+ | input | Positive input to the device. High-side: connect to power supply side of sense resistor. Low-side: connect to load side of sense resistor | DS p.3, 5 Pin Configuration and Functions, Table 5-1 Pin Functions, IN+ (pin 10) |

## Parameters: abs_max

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Supply voltage | VS |  |  | 6 | V | over operating free-air temperature range (unless otherwise noted) Note: Only a MAX is printed (MIN column blank). No reference pin printed; checked against system 0 V (a floating GND is not modelled). | DS p.3, 6.1 Absolute Maximum Ratings, Supply voltage VS | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Differential input voltage, (VIN+) - (VIN-) | VIN+, VIN- | -40 (rel. IN-) |  | 40 (rel. IN-) | V | over operating free-air temperature range (unless otherwise noted) Note: Pin-pair row: the value is V(IN+), the reference is IN- (second pin as reference). Footnote (2) on the same table: VIN+ and VIN- are the voltages at the IN+ and IN- pins. check_pins IN+ with IN- as reference. | DS p.3, 6.1 Absolute Maximum Ratings, VIN+, VIN- Differential (VIN+) - (VIN-) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Common-mode input voltage, VIN+ and VIN- | VIN+, VIN- | -0.3 |  | 85 | V | over operating free-air temperature range (unless otherwise noted) Note: Same limits as vcm_rec (DS p.4, 6.3). No reference pin printed (DS p.12, 7.3.1 gives -0.3 V to +85 V at the input pins with no reference); checked against system 0 V (a floating GND is not modelled). | DS p.3, 6.1 Absolute Maximum Ratings, VIN+, VIN- Common-mode | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Bus voltage input, VBUS | VBUS | -0.3 |  | 85 | V | over operating free-air temperature range (unless otherwise noted) Note: No reference pin printed; checked against system 0 V (a floating GND is not modelled). | DS p.3, 6.1 Absolute Maximum Ratings, VBUS | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Digital input/output voltage, MOSI, MISO, SCLK, ALERT | VIO | -0.3 (rel. GND) |  | 0.3 (rel. VS) | V | over operating free-air temperature range (unless otherwise noted) Note: Printed GND - 0.3 V (MIN) and VS + 0.3 V (MAX): min_ref = GND, max_ref = VS. CS is not in this row (DS omission, open item): CS is not checked. | DS p.3, 6.1 Absolute Maximum Ratings, VIO, MOSI, MISO, SCLK, ALERT | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Input current into any pin | IIN |  |  | 5 | mA | over operating free-air temperature range (unless otherwise noted) Note: MAX column only (MIN blank), stored as max. | DS p.3, 6.1 Absolute Maximum Ratings, IIN, Input current into any pin | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Digital output current | IOUT |  |  | 10 | mA | over operating free-air temperature range (unless otherwise noted) Note: MAX column only (MIN blank), stored as max. | DS p.3, 6.1 Absolute Maximum Ratings, IOUT, Digital output current | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Junction temperature | TJ |  |  | 150 | degC |  | DS p.3, 6.1 Absolute Maximum Ratings, TJ, Junction temperature | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Storage temperature | Tstg | -65 |  | 150 | degC |  | DS p.3, 6.1 Absolute Maximum Ratings, Tstg, Storage temperature | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Electrostatic discharge, human body model | V(ESD) | -2000 |  | 2000 | V | HBM per ANSI/ESDA/JEDEC JS-001, all pins Note: Printed +/-2000 V. DS footnote (1): JEDEC JEP155 500 V HBM allows safe manufacturing. | DS p.4, 6.2 ESD Ratings, Human body model (HBM), V(ESD) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Electrostatic discharge, charged device model | V(ESD) | -1000 |  | 1000 | V | CDM per JEDEC JESD22-C101, all pins Note: Printed +/-1000 V. DS footnote (2): JEDEC JEP157 250 V CDM allows safe manufacturing. | DS p.4, 6.2 ESD Ratings, Charged device model (CDM), V(ESD) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |

## Parameters: rec_op

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Common-mode input range | VCM | -0.3 |  | 85 | V | over operating free-air temperature range (unless otherwise noted) Note: No reference pin printed; checked against system 0 V (a floating GND is not modelled). | DS p.4, 6.3 Recommended Operating Conditions, VCM, Common-mode input range | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Operating supply range | VS | 2.7 |  | 5.5 | V | over operating free-air temperature range (unless otherwise noted) Note: No reference pin printed; checked against system 0 V (a floating GND is not modelled). | DS p.4, 6.3 Recommended Operating Conditions, VS, Operating supply range | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Ambient temperature | TA | -40 |  | 125 | degC |  | DS p.4, 6.3 Recommended Operating Conditions, TA, Ambient temperature | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |

## Parameters: electrical

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Common-mode input range | VCM | -0.3 |  | 85 | V | TA = -40 degC to +125 degC | DS p.5, 6.5 Electrical Characteristics, INPUT, Common-mode input range VCM |  |
| Bus voltage input range | VVBUS | 0 |  | 85 | V | no row condition; table header: TA = 25 degC, VS = 3.3 V, VSENSE = 0 V, VCM = 48 V Note: No own test condition: header applies (25 degC). Not in the rec-op table (DS p.4 has no VBUS row). | DS p.5, 6.5 Electrical Characteristics, INPUT, Bus voltage input range VBUS |  |
| Common-mode rejection | CMRR | 154 | 170 |  | dB | -0.3 V < VCM < 85 V, TA = -40 degC to +125 degC | DS p.5, 6.5 Electrical Characteristics, INPUT, Common-mode rejection CMRR |  |
| Shunt voltage input range, ADCRANGE = 0 | VDIFF | -163.84 |  | 163.84 | mV | TA = -40 degC to +125 degC, ADCRANGE = 0 Note: MIN -163.84 and MAX 163.84 printed with signs: stored as printed. | DS p.5, 6.5 Electrical Characteristics, INPUT, Shunt voltage input range VDIFF, ADCRANGE = 0 | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Shunt voltage input range, ADCRANGE = 1 | VDIFF | -40.96 |  | 40.96 | mV | TA = -40 degC to +125 degC, ADCRANGE = 1 Note: MIN -40.96 and MAX 40.96 printed with signs: stored as printed. | DS p.5, 6.5 Electrical Characteristics, INPUT, Shunt voltage input range VDIFF, ADCRANGE = 1 |  |
| Shunt offset voltage, VCM = 48 V | Vos | -1 | ±0.3 | 1 | uV | VCM = 48 V, TCT > 280 us; table header TA = 25 degC Note: TYP printed +/-0.3 uV (spread around zero: typ_pm). MAX printed +/-1 uV: min = -1, max = 1. No temperature condition: header 25 degC. The full-temperature offset comes from vos_drift_full (SPEC recipe step 2). | DS p.5, 6.5 Electrical Characteristics, INPUT, Shunt offset voltage Vos, VCM = 48 V | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Shunt offset voltage, VCM = 0 V | Vos | -1 | ±0.3 | 1 | uV | VCM = 0 V, TCT > 280 us; table header TA = 25 degC Note: TYP printed +/-0.3 uV (typ_pm). MAX printed +/-1 uV: min = -1, max = 1. No temperature condition: header 25 degC. | DS p.5, 6.5 Electrical Characteristics, INPUT, Shunt offset voltage Vos, VCM = 0 V | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Shunt offset voltage drift | dVos/dT | -10 | ±2 | 10 | nV/degC | TA = -40 degC to +125 degC Note: TYP printed +/-2 nV/degC (typ_pm); MAX printed +/-10 nV/degC: min = -10, max = 10. | DS p.5, 6.5 Electrical Characteristics, INPUT, Shunt offset voltage drift dVos/dT | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Shunt offset voltage vs power supply | PSRR | -0.5 | ±0.05 | 0.5 | uV/V | VS = 2.7 V to 5.5 V, TA = -40 degC to +125 degC Note: Printed uV/V; stored as printed. TYP +/-0.05 (typ_pm), MAX +/-0.5: min = -0.5, max = 0.5. | DS p.5, 6.5 Electrical Characteristics, INPUT, Shunt offset voltage vs power supply PSRR |  |
| VBUS offset voltage | Vos_bus | -2.5 | ±1 | 2.5 | mV | VBUS = 20 mV; table header TA = 25 degC Note: TYP printed +/-1 mV (typ_pm); MAX printed +/-2.5 mV: min = -2.5, max = 2.5. No temperature condition: header 25 degC. | DS p.5, 6.5 Electrical Characteristics, INPUT, VBUS offset voltage Vos_bus | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| VBUS offset voltage drift | dVos/dT | -20 | ±4 | 20 | uV/degC | TA = -40 degC to +125 degC Note: TYP printed +/-4 uV/degC (typ_pm); MAX printed +/-20 uV/degC: min = -20, max = 20. | DS p.5, 6.5 Electrical Characteristics, INPUT, VBUS offset voltage drift dVos/dT | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| VBUS offset voltage vs power supply | PSRR |  | ±0.25 |  | mV/V | VS = 2.7 V to 5.5 V; table header TA = 25 degC Note: Printed +/-0.25 mV/V in TYP (MAX blank); stored as printed (typ_pm). No temperature condition: header 25 degC. | DS p.5, 6.5 Electrical Characteristics, INPUT, VBUS offset voltage vs power supply PSRR | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Input bias current | IB |  | ±0.1 | ±2.5 | nA | Either input, IN+ or IN-, VCM = 85 V; table header TA = 25 degC Note: DS prints an unsigned magnitude for a quantity that can be either sign: sym = true (min = -max), printed TYP kept as typ_spread. Single value at 25 degC. | DS p.5, 6.5 Electrical Characteristics, INPUT, Input bias current IB | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| VBUS pin input impedance | ZVBUS | 0.8 | 1 | 1.2 | Mohm | Active mode; table header TA = 25 degC | DS p.5, 6.5 Electrical Characteristics, INPUT, VBUS pin input impedance ZVBUS | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| VBUS pin leakage current | IVBUS |  | 10 |  | nA | Shutdown mode, VBUS = 85 V; table header TA = 25 degC Note: TYP only, no MIN or MAX printed. | DS p.5, 6.5 Electrical Characteristics, INPUT, VBUS pin leakage current IVBUS |  |
| Input differential impedance | RDIFF |  | 92 |  | kohm | Active mode, VIN+ - VIN- < 164 mV; table header TA = 25 degC Note: TYP only, no MIN or MAX printed. | DS p.5, 6.5 Electrical Characteristics, INPUT, Input differential impedance RDIFF |  |
| Shunt voltage gain error | GSERR | -0.05 | ±0.01 | 0.05 | % | VCM = 24 V; table header TA = 25 degC Note: TYP printed +/-0.01 % (typ_pm). MAX printed +/-0.05 %: min = -0.05, max = 0.05 (loader gives fractions). No full-temperature row: drift from gs_drift_25c (SPEC recipe step 2). | DS p.5, 6.5 Electrical Characteristics, DC ACCURACY, Shunt voltage gain error GSERR | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Shunt voltage gain error drift | GS_DRFT | -20 |  | 20 | ppm/degC | no row condition; table header TA = 25 degC Note: MAX printed +/-20 ppm/degC (no TYP). Test conditions column blank, so the header (25 degC) applies literally, although a drift is normally specified over temperature. Used as the drift term of the SPEC recipe X(T) = X25 + drift x (T - 25). DS ambiguity, open item. | DS p.5, 6.5 Electrical Characteristics, DC ACCURACY, Shunt voltage gain error drift GS_DRFT | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| VBUS voltage gain error | GBERR | -0.05 | ±0.01 | 0.05 | % | table header TA = 25 degC Note: TYP printed +/-0.01 % (typ_pm). MAX printed +/-0.05 %: min = -0.05, max = 0.05. No own condition: header 25 degC. | DS p.5, 6.5 Electrical Characteristics, DC ACCURACY, VBUS voltage gain error GBERR | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| VBUS voltage gain error drift | GB_DRFT | -20 |  | 20 | ppm/degC | no row condition; table header TA = 25 degC Note: MAX printed +/-20 ppm/degC (no TYP). Blank condition: header applies literally (same ambiguity as gs_drift_25c). | DS p.5, 6.5 Electrical Characteristics, DC ACCURACY, VBUS voltage gain error drift GB_DRFT | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Power total measurement error (TME) | PTME | -0.5 |  | 0.5 | % | TA = -40 degC to +125 degC, at full scale Note: MAX printed +/-0.5 % (no TYP). | DS p.5, 6.5 Electrical Characteristics, DC ACCURACY, Power total measurement error (TME) PTME | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Energy and charge total measurement error (TME) | ETME | -1 |  | 1 | % | at full scale power; table header TA = 25 degC Note: MAX printed +/-1 % (no TYP). No temperature condition: header 25 degC. | DS p.5, 6.5 Electrical Characteristics, DC ACCURACY, Energy and charge TME ETME |  |
| ADC resolution |  |  | 20 |  | bits | table header TA = 25 degC Note: Printed unit 'Bits'. | DS p.5, 6.5 Electrical Characteristics, DC ACCURACY, ADC resolution |  |
| Shunt voltage 1 LSB step size, ADCRANGE = 0 |  |  | 312.5 |  | nV | Shunt voltage, ADCRANGE = 0; table header TA = 25 degC Note: Same value in Table 7-9 (DS p.23) and Section 8.1.1 (DS p.29). | DS p.5, 6.5 Electrical Characteristics, DC ACCURACY, 1 LSB step size, Shunt voltage ADCRANGE = 0 |  |
| Shunt voltage 1 LSB step size, ADCRANGE = 1 |  |  | 78.125 |  | nV | Shunt voltage, ADCRANGE = 1; table header TA = 25 degC Note: Same value in Table 7-9 (DS p.23) and Section 8.1.1 (DS p.29). | DS p.5, 6.5 Electrical Characteristics, DC ACCURACY, 1 LSB step size, Shunt voltage ADCRANGE = 1 |  |
| Bus voltage 1 LSB step size |  |  | 195.3125 |  | uV | Bus voltage; table header TA = 25 degC Note: Same value in Table 7-10 (DS p.23) and Section 8.1.1 (DS p.29). | DS p.5, 6.5 Electrical Characteristics, DC ACCURACY, 1 LSB step size, Bus voltage | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Temperature 1 LSB step size |  |  | 7.8125 |  | mdegC | Temperature; table header TA = 25 degC Note: Printed 7.8125 m degC/LSB (DS p.5, p.24 Table 7-11); stored as printed. | DS p.5, 6.5 Electrical Characteristics, DC ACCURACY, 1 LSB step size, Temperature |  |
| ADC conversion time, field = 0h | TCT |  | 50 |  | us | Conversion time field = 0h; table header TA = 25 degC Note: DS footnote (1) on the TCT row (DS p.6): subject to oscillator accuracy and drift. TYP only. | DS p.5, 6.5 Electrical Characteristics, DC ACCURACY, ADC conversion-time TCT, field = 0h |  |
| ADC conversion time, field = 1h | TCT |  | 84 |  | us | Conversion time field = 1h; table header TA = 25 degC Note: DS footnote (1) (p.6): subject to oscillator accuracy and drift. TYP only. | DS p.5, 6.5 Electrical Characteristics, DC ACCURACY, ADC conversion-time TCT, field = 1h |  |
| ADC conversion time, field = 2h | TCT |  | 150 |  | us | Conversion time field = 2h; table header TA = 25 degC Note: DS footnote (1) (p.6): subject to oscillator accuracy and drift. TYP only. | DS p.5, 6.5 Electrical Characteristics, DC ACCURACY, ADC conversion-time TCT, field = 2h |  |
| ADC conversion time, field = 3h | TCT |  | 280 |  | us | Conversion time field = 3h; table header TA = 25 degC Note: DS footnote (1) (p.6): subject to oscillator accuracy and drift. TYP only. | DS p.5, 6.5 Electrical Characteristics, DC ACCURACY, ADC conversion-time TCT, field = 3h |  |
| ADC conversion time, field = 4h | TCT |  | 540 |  | us | Conversion time field = 4h; table header TA = 25 degC Note: DS footnote (1) (p.6): subject to oscillator accuracy and drift. TYP only. | DS p.5, 6.5 Electrical Characteristics, DC ACCURACY, ADC conversion-time TCT, field = 4h |  |
| ADC conversion time, field = 5h | TCT |  | 1052 |  | us | Conversion time field = 5h; table header TA = 25 degC Note: DS footnote (1) (p.6): subject to oscillator accuracy and drift. TYP only. | DS p.5, 6.5 Electrical Characteristics, DC ACCURACY, ADC conversion-time TCT, field = 5h |  |
| ADC conversion time, field = 6h | TCT |  | 2074 |  | us | Conversion time field = 6h; table header TA = 25 degC Note: DS footnote (1) (p.6): subject to oscillator accuracy and drift. TYP only. | DS p.5, 6.5 Electrical Characteristics, DC ACCURACY, ADC conversion-time TCT, field = 6h |  |
| ADC conversion time, field = 7h | TCT |  | 4120 |  | us | Conversion time field = 7h; table header TA = 25 degC Note: DS footnote (1) (p.6): subject to oscillator accuracy and drift. TYP only. | DS p.5, 6.5 Electrical Characteristics, DC ACCURACY, ADC conversion-time TCT, field = 7h |  |
| Integral non-linearity | INL |  | ±2 |  | m% | table header TA = 25 degC Note: TYP printed +/-2 m% (typ_pm); stored as printed. | DS p.5, 6.5 Electrical Characteristics, DC ACCURACY, Integral Non-Linearity INL |  |
| Differential non-linearity | DNL |  | 0.2 |  | LSB | table header TA = 25 degC Note: Printed unit 'LSB'. TYP only. | DS p.5, 6.5 Electrical Characteristics, DC ACCURACY, Differential Non-Linearity DNL |  |
| Internal oscillator frequency | FOSC |  | 1 |  | MHz | table header TA = 25 degC Note: TYP only. | DS p.5, 6.5 Electrical Characteristics, CLOCK SOURCE, Internal oscillator frequency FOSC |  |
| Internal oscillator frequency tolerance, TA = 25 degC | FOSC_TOL | -0.5 |  | 0.5 | % | TA = 25 degC Note: MAX printed +/-0.5 % (no TYP). | DS p.5, 6.5 Electrical Characteristics, CLOCK SOURCE, Internal oscillator frequency tolerance FOSC_TOL, TA = 25 degC |  |
| Internal oscillator frequency tolerance, full temperature | FOSC_TOL | -1 |  | 1 | % | TA = -40 degC to +125 degC Note: MAX printed +/-1 % (no TYP). | DS p.5, 6.5 Electrical Characteristics, CLOCK SOURCE, Internal oscillator frequency tolerance FOSC_TOL, TA = -40 degC to +125 degC |  |
| Temperature measurement range |  | -40 |  | 125 | degC | no row condition; table header TA = 25 degC Note: Range row with no condition: header applies literally. The range itself is the temperature grade (DS p.4, TA). | DS p.6, 6.5 Electrical Characteristics, TEMPERATURE SENSOR, Measurement range |  |
| Temperature accuracy, TA = 25 degC |  | -1 | ±0.15 | 1 | degC | TA = 25 degC Note: TYP printed +/-0.15 degC (typ_pm). MAX printed +/-1 degC: min = -1, max = 1. | DS p.6, 6.5 Electrical Characteristics, TEMPERATURE SENSOR, Temperature accuracy, TA = 25 degC |  |
| Temperature accuracy, full temperature |  | -2 | ±0.2 | 2 | degC | TA = -40 degC to +125 degC Note: TYP printed +/-0.2 degC (typ_pm). MAX printed +/-2 degC: min = -2, max = 2. | DS p.6, 6.5 Electrical Characteristics, TEMPERATURE SENSOR, Temperature accuracy, TA = -40 degC to +125 degC |  |
| Supply voltage | VS | 2.7 |  | 5.5 | V | no row condition; table header TA = 25 degC, VS = 3.3 V Note: Same numbers as vs_rec (DS p.4, 6.3). No own condition: header applies literally. | DS p.6, 6.5 Electrical Characteristics, POWER SUPPLY, Supply voltage VS |  |
| Quiescent current | IQ |  | 640 | 750 | uA | VSENSE = 0 V; table header TA = 25 degC Note: TYP 640 uA, MAX 750 uA as printed (MIN blank). | DS p.6, 6.5 Electrical Characteristics, POWER SUPPLY, Quiescent current IQ, VSENSE = 0 V | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Quiescent current, full temperature | IQ |  |  | 1.1 | mA | VSENSE = 0 V, TA = -40 degC to +125 degC Note: MAX only (1.1 mA) printed for this row. | DS p.6, 6.5 Electrical Characteristics, POWER SUPPLY, Quiescent current IQ, VSENSE = 0 V, TA = -40 degC to +125 degC | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Quiescent current, shutdown | IQSD |  | 2.8 | 5 | uA | Shutdown mode; table header TA = 25 degC Note: TYP 2.8 uA, MAX 5 uA as printed. | DS p.6, 6.5 Electrical Characteristics, POWER SUPPLY, Quiescent current, shutdown IQSD | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Device start-up time, power-up (NPOR) | TPOR |  | 300 |  | us | Power-up (NPOR); table header TA = 25 degC Note: TYP only. | DS p.6, 6.5 Electrical Characteristics, POWER SUPPLY, Device start-up time TPOR, Power-up (NPOR) |  |
| Device start-up time, from shutdown mode | TPOR |  | 60 |  | us | From shutdown mode; table header TA = 25 degC Note: TYP only. | DS p.6, 6.5 Electrical Characteristics, POWER SUPPLY, Device start-up time TPOR, From shutdown mode |  |
| Logic input level, high | VIH | 1.2 |  | 0 (rel. VS) | V | no row condition; table header TA = 25 degC Note: Printed MIN 1.2 V and MAX VS: MAX stored as the offset 0 from pin VS (max_ref = VS); users call part.resolve(). | DS p.6, 6.5 Electrical Characteristics, DIGITAL INPUT / OUTPUT, Logic input level, high VIH |  |
| Logic input level, low | VIL | 0 (rel. GND) |  | 0.4 | V | no row condition; table header TA = 25 degC Note: Printed MIN GND and MAX 0.4 V: MIN stored as offset 0 from pin GND (min_ref = GND). | DS p.6, 6.5 Electrical Characteristics, DIGITAL INPUT / OUTPUT, Logic input level, low VIL |  |
| Logic output level, low | VOL | 0 (rel. GND) |  | 0.4 | V | IOL = 1 mA; table header TA = 25 degC Note: Printed MIN GND (offset 0 from pin GND) and MAX 0.4 V. | DS p.6, 6.5 Electrical Characteristics, DIGITAL INPUT / OUTPUT, Logic output level, low VOL, IOL = 1 mA | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Logic output level, high | VOH | -0.4 (rel. VS) |  | 0 (rel. VS) | V | IOL = 1 mA; table header TA = 25 degC Note: Printed MIN VS - 0.4 V and MAX VS: stored as offsets from pin VS. The row's condition prints IOL = 1 mA (not IOH); stored as printed. DS ambiguity, open item. | DS p.6, 6.5 Electrical Characteristics, DIGITAL INPUT / OUTPUT, Logic output level, high VOH, IOL = 1 mA | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Digital leakage input current | IIO_LEAK | -1 |  | 1 | uA | 0 <= VIN <= VS; table header TA = 25 degC Note: Printed -1 uA (MIN) and 1 uA (MAX), stored as printed. | DS p.6, 6.5 Electrical Characteristics, DIGITAL INPUT / OUTPUT, Digital leakage input current IIO_LEAK |  |
| Shunt temperature coefficient register resolution | TEMPCO |  | 1 |  | ppm/degC | Note: The register provides a resolution of 1 ppm/degC/LSB (Table 7-8). Register description, not an EC row. | DS p.23, 7.6.1.4 Shunt Temperature Coefficient (SHUNT_TEMPCO) Register, Table 7-8, TEMPCO |  |
| Shunt temperature coefficient register range | TEMPCO | 0 |  | 16383 | ppm/degC | Note: Register range 0h = 0 ppm/degC to 16383 ppm/degC (Table 7-8). Section 7.3.5 (DS p.16) says the full scale is 16384 ppm/degC. The DS contradicts itself (16383 vs 16384); the register table value is stored. DS ambiguity, open item. | DS p.23, 7.6.1.4 Shunt Temperature Coefficient (SHUNT_TEMPCO) Register, Table 7-8, TEMPCO (3FFFh = 16383 ppm/degC) |  |

## Parameters: thermal

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Junction-to-ambient thermal resistance | RthetaJA |  | 177.6 |  | degC/W | DGS (VSSOP), 10 pins Note: Single printed value (no min or max), stored as typ. | DS p.4, 6.4 Thermal Information, RthetaJA, DGS (VSSOP) 10 PINS | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Junction-to-case (top) thermal resistance | RthetaJC(top) |  | 66.4 |  | degC/W | DGS (VSSOP), 10 pins Note: Single printed value (no min or max), stored as typ. | DS p.4, 6.4 Thermal Information, RthetaJC(top), DGS (VSSOP) 10 PINS |  |
| Junction-to-board thermal resistance | RthetaJB |  | 99.5 |  | degC/W | DGS (VSSOP), 10 pins Note: Single printed value (no min or max), stored as typ. | DS p.4, 6.4 Thermal Information, RthetaJB, DGS (VSSOP) 10 PINS |  |
| Junction-to-top characterization parameter | PsiJT |  | 9.7 |  | degC/W | DGS (VSSOP), 10 pins Note: Single printed value (no min or max), stored as typ. | DS p.4, 6.4 Thermal Information, PsiJT, DGS (VSSOP) 10 PINS |  |
| Junction-to-board characterization parameter | YJB |  | 97.6 |  | degC/W | DGS (VSSOP), 10 pins Note: Single printed value (no min or max), stored as typ. The DS prints YJB (not PsiJB) for this row. | DS p.4, 6.4 Thermal Information, YJB, DGS (VSSOP) 10 PINS |  |

## Limits of this data

Rows by scope: 25C 43, full 11, na 21 (25C rows hold only at 25 degC). Curve (graph) rows: 0. Text rows: 0.

## Zener checks

Generated wrapper: `INA229AIDGS.zen` (`python3 -m lib.zen`). abs_max and rec_op rows are errors (abs_max x derate); 25C and partial rows are waivable warnings; a checked net with no voltage is UNVERIFIED.

| Param | Name | Checked against | Not checked / reason |
|---|---|---|---|
| vs_abs | Supply voltage | UNCHECKED | covered by vs_rec (2.7 V to 5.5 V, error), which is stricter |
| vin_diff_abs | Differential input voltage, (VIN+) - (VIN-) | pins IN+ |  |
| vcm_abs | Common-mode input voltage, VIN+ and VIN- | pins IN+, IN- |  |
| vbus_abs | Bus voltage input, VBUS | pins VBUS |  |
| vio_abs | Digital input/output voltage, MOSI, MISO, SCLK, ALERT | pins MOSI, SCLK, ALERT | MISO not checked: push-pull output driven by the part; owner: module. CS: not listed in the DS VIO row (DS omission); no rating stored, open item |
| iin_abs | Input current into any pin | UNCHECKED | current rating, not a voltage (the wrapper checks voltages only); owner: board |
| iout_abs | Digital output current | UNCHECKED | current rating, not a voltage (the wrapper checks voltages only); owner: module |
| tj_abs | Junction temperature | UNCHECKED | needs dissipation x RthetaJA; owner: module |
| tstg_abs | Storage temperature | UNCHECKED | owner: assembly |
| esd_hbm | Electrostatic discharge, human body model | UNCHECKED | owner: assembly |
| esd_cdm | Electrostatic discharge, charged device model | UNCHECKED | owner: assembly |
| vcm_rec | Common-mode input range | pins IN+, IN- |  |
| vs_rec | Operating supply range | pins VS |  |
| ta_rec | Ambient temperature | board ambient |  |

## Equations

### `current_lsb`

```
CURRENT_LSB = maximum expected current / 2^19. DS p.30, 8.1.2 Current, Power, Energy, and Charge Calculations,
Equation 3. i_max: maximum expected current, A. Returns: CURRENT_LSB, A per count.
```

Inputs:


### `shunt_cal`

```
SHUNT_CAL = 13107.2e6 x CURRENT_LSB x RSHUNT. DS p.30, 8.1.2 Current, Power, Energy, and Charge Calculations,
Equation 2. For ADCRANGE = 1 the value is multiplied by 4 (DS p.30, bullet under Equation 2).
i_lsb: CURRENT_LSB, A. rshunt: shunt resistance, ohm. adcrange: 0 or 1 (CONFIG bit 4).
Returns: SHUNT_CAL register value, unitless. The register takes an integer: round before writing.
Checked against the DS design example (p.35, 8.2.2.3): 19.0735 uA and 16.2 mohm give 4050d.
```

Inputs:


### `rshunt_max`

```
RSHUNT < VSENSE_MAX / IMAX. DS p.35, 8.2.2.1 Select the Shunt Resistor, Equation 8 (strict upper bound).
vsense_max: largest differential shunt voltage for the chosen ADC range, V (0.16384 for ADCRANGE = 0).
i_max: maximum current to be sensed, A. Returns: upper bound on RSHUNT, ohm (not inclusive).
```

Inputs:


### `current`

```
Current [A] = CURRENT_LSB x CURRENT. DS p.30, 8.1.2 Current, Power, Energy, and Charge Calculations, Equation 4.
i_lsb: CURRENT_LSB, A. current_reg: CURRENT register, signed integer. Returns: current, A (signed).
```

Inputs:


### `power`

```
Power [W] = 3.2 x CURRENT_LSB x POWER. DS p.30, 8.1.2 Current, Power, Energy, and Charge Calculations, Equation 5.
i_lsb: CURRENT_LSB, A. power_reg: POWER register, unsigned integer. Returns: power, W.
```

Inputs:


### `energy`

```
Energy [J] = 16 x 3.2 x CURRENT_LSB x ENERGY. DS p.30, 8.1.2 Current, Power, Energy, and Charge Calculations,
Equation 6. i_lsb: CURRENT_LSB, A. energy_reg: ENERGY register, unsigned integer. Returns: energy, J.
```

Inputs:


### `charge`

```
Charge [C] = CURRENT_LSB x CHARGE. DS p.31, 8.1.2 Current, Power, Energy, and Charge Calculations, Equation 7.
i_lsb: CURRENT_LSB, A. charge_reg: CHARGE register, signed integer. Returns: charge, C (signed).
```

Inputs:


### `shunt_voltage`

```
V_SHUNT = VSHUNT x LSB. DS p.29, 8.1.1 Device Measurement Range and Resolution ("multiplying the digital value
by its respective resolution size"); LSB from DS p.23, Table 7-9 (312.5 nV/LSB for ADCRANGE = 0, 78.125 nV/LSB
for ADCRANGE = 1). vshunt_reg: VSHUNT register, signed integer. lsb: V per count. Returns: voltage, V (signed).
```

Inputs:

- `lsb` -> `lsb_vshunt_adcr0_25c.typ` (typ 312.5 nV)

### `bus_voltage`

```
V_BUS = VBUS x LSB. DS p.29, 8.1.1 Device Measurement Range and Resolution; LSB from DS p.23, Table 7-10
(195.3125 uV/LSB). vbus_reg: VBUS register, unsigned in practice (always positive, DS p.23).
lsb: V per count. Returns: voltage, V.
```

Inputs:

- `lsb` -> `lsb_vbus_25c.typ` (typ 195.3125 uV)

### `die_temperature`

```
T_DIE = DIETEMP x LSB. DS p.29, 8.1.1 Device Measurement Range and Resolution; LSB from DS p.24, Table 7-11
(7.8125 m degC/LSB). dietemp_reg: DIETEMP register, signed integer. lsb: degC per count.
Returns: die temperature, degC (signed).
```

Inputs:

- `lsb` -> `lsb_temp_25c.typ` (typ 7.8125 mdegC)

### `shunt_tempco_radj`

```
RADJ = RNOM x (1 + TEMPCO x (DIETEMP - 25)). DS p.16, 7.3.5 Shunt Resistor Drift Compensation, Equation 1
(printed as RNOM + RNOM x (DIETEMP - 25) x SHUNT_TEMPCO / 10^6). Algebra on Equation 1: tempco = SHUNT_TEMPCO / 10^6,
in 1/degC (the register value in ppm/degC divided by 1e6).
rnom: shunt resistance at 25 degC, ohm. dietemp: die temperature, degC. tempco: shunt temperature coefficient, 1/degC.
Returns: compensated shunt resistance, ohm. Assumes TEMPCO bit in CONFIG is set (DS p.16).
```

Inputs:


### `current_error`

```
Not a DS equation: measured-current error from shunt offset and shunt gain error, at temperature t_c.
The DS prints the terms (Vos and dVos/dT, GSERR and GS_DRFT, p.5) and the current scaling (Equations 2 and 4, p.30),
but not their combination. Derivation: the CURRENT register reports the shunt voltage divided by RSHUNT (the
calibration of Equation 2 sets that scale). With V_true = i_true x rshunt, the measured shunt voltage is
V_true x (1 + g) + vos, where (SPEC temperature recipe, step 2: X(T) = X25 + drift x (T - 25)):
    g(T)   = gserr + gs_drift x (T - 25)     gserr: GSERR row, gs_drift: GS_DRFT row (DS p.5)
    vos(T) = vos25 + vos_drift x (T - 25)    vos25: Vos row (DS p.5), vos_drift: dVos/dT row (DS p.5)
so the measured current minus the true current is i_true x g(T) + vos(T) / rshunt.
Bilinear in (gs_drift, t_c) and (vos_drift, t_c), so the wca corners are exact. Pass t_c as Param(min=-40, max=125).
i_true: true current, A, signed. rshunt: shunt resistance, ohm (pass with its tolerance). vos25: V, signed.
vos_drift: V/degC, signed. gserr: fraction, signed. gs_drift: 1/degC, signed. t_c: degC.
Partial budget: excludes CMRR, PSRR, INL, 1-LSB quantisation and SHUNT_CAL integer rounding.
Returns: current error, A, signed (positive = reads high).
```

Inputs:

- `vos25` -> `vos_vcm48_25c` (min -1 typ ±0.3 max 1 uV)
- `vos_drift` -> `vos_drift_full` (min -10 typ ±2 max 10 nV/degC)
- `gserr` -> `gserr_25c` (min -0.05 typ ±0.01 max 0.05 %)
- `gs_drift` -> `gs_drift_25c` (min -20 max 20 ppm/degC)


## Examples

| Call | Computed | Expected | Rel. tol | Result | Cite |
|---|---|---|---|---|---|
| current_lsb(i_max=10) | 1.90735e-05 | 1.90735e-05 | 1e-06 | pass | DS p.36, Table 8-4, Current LSB 10 A / 2^19 = 19.073486 uA/LSB |
| rshunt_max(vsense_max=0.16384, i_max=10) | 0.016384 | 0.01638 | 0.001 | pass | DS p.35, 8.2.2.1, Equation 8: RSHUNT max 16.38 mohm. The DS prints 16.38 (rounded); exact 16.384 mohm, 2.4e-4 high |
| shunt_cal(i_lsb=1.90735e-05, rshunt=0.0162) | 4050 | 4050 | 0.001 | pass | DS p.35, 8.2.2.3, SHUNT_CAL = 4050d (FD2h) for 10 A design, 16.2 mohm shunt |
| shunt_cal(i_lsb=1.90735e-05, rshunt=0.0162, adcrange=1) | 16200 | 16200 | 0.001 | pass | DS p.30, Equation 2 bullet: x4 for ADCRANGE = 1 (4 x 4050) |
| current(i_lsb=1.90735e-05, current_reg=314572) | 5.99998 | 6 | 0.001 | pass | DS p.36, Table 8-4, Current 314572d -> 6 A |
| power(i_lsb=1.90735e-05, power_reg=4.7186e+06) | 288.001 | 288 | 0.001 | pass | DS p.36, Table 8-4, Power 4718604d -> 288 W |
| energy(i_lsb=1.90735e-05, energy_reg=1.06168e+09) | 1.0368e+06 | 1.0368e+06 | 0.001 | pass | DS p.36, Table 8-4, Energy 1061683200d -> 1036800 J |
| charge(i_lsb=1.90735e-05, charge_reg=1.13246e+09) | 21600 | 21600 | 0.001 | pass | DS p.36, Table 8-4, Charge 1132462080d -> 21600 C |
| shunt_voltage(vshunt_reg=311040, lsb=3.125e-07) | 0.0972 | 0.0972 | 0.001 | pass | DS p.36, Table 8-4, Shunt voltage 311040d -> 0.0972 V |
| bus_voltage(vbus_reg=245760, lsb=0.000195313) | 48 | 48 | 0.001 | pass | DS p.36, Table 8-4, Bus voltage 245760d -> 48 V |
| die_temperature(dietemp_reg=3200, lsb=0.0078125) | 25 | 25 | 0.001 | pass | DS p.36, Table 8-4, Temperature 3200d -> 25 degC |
| shunt_tempco_radj(rnom=0.0162, dietemp=25, tempco=0.0001) | 0.0162 | 0.0162 | 1e-09 | pass | DS p.16, Equation 1 at DIETEMP = 25 degC (reference temperature): RADJ = RNOM |
| current_error(i_true=10, rshunt=0.0162, vos25=0, vos_drift=0, gserr=0, gs_drift=0, t_c=25) | 0 | 0 | 1e-12 | pass | Not a DS equation: zero offset, gain error and drift give zero error |
| current_error(i_true=10, rshunt=0.0162, vos25=0, vos_drift=0, gserr=0.0005, gs_drift=0, t_c=25) | 0.005 | 0.005 | 0.001 | pass | Not a DS equation: GSERR MAX 0.05 % on 10 A = 5 mA (DS p.5) |
| current_error(i_true=0, rshunt=0.0162, vos25=1e-06, vos_drift=0, gserr=0, gs_drift=0, t_c=25) | 6.17284e-05 | 6.17284e-05 | 0.001 | pass | Not a DS equation: Vos MAX 1 uV over 16.2 mohm = 61.7 uA (DS p.5) |
