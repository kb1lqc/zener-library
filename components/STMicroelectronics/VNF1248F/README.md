<!-- GENERATED - do not edit. Run: python3 -m lib.readme -->

# VNF1248F

## Datasheet review

[![Human page-image review: 0/297 human](https://img.shields.io/badge/human%20review-0%2F297%20human-lightgrey)](../../../docs/spec/datasheet-review.md)

Human page-image review: 0/297; cross-model audits: 0; manufacturer-export stamps: 0; legacy/unclassified: 0. Text checks are not verification. `lib.check` validates stamp format, not that review occurred.

## Part

- **mpn**: VNF1248FTR
- **alternates**: []
- **manufacturer**: STMicroelectronics
- **description**: High-side switch controller with intelligent fuse protection, 6-60 V (70 V transient), AEC-Q100, QFN32L 5x5 mm
- **category**: high_side_controller
- **package**: QFN32L 5x5 mm Epad, wettable flanks (DS p.69 Figure 22, DS p.70 Table 65)
- **datasheet_url**: https://www.st.com/resource/en/datasheet/vnf1248f.pdf
- **datasheet_file**: docs/datasheets/DS_vnf1248f.pdf
- **datasheet_rev**: Rev 8
- **datasheet_date**: 2026-07
- **temp_grade**: TJ -40 to 150 degC
- **kicad_symbol**: VNF1248F.kicad_sym
- **kicad_footprint**: VNF1248F.kicad_mod
- **step**: VNF1248F.step

## Pins

| Pin | Name | Type | Function | Cite |
|---|---|---|---|---|
| 1 | VSPI | power_in | DS: DC supply input for the SPI interface. 3.3 V and 5 V are compatible. | DS p.4, Table 1. Pin functions, VSPI |
| 2 | CSN | input | Chip select (active low) for SPI communication. CMOS compatible input. | DS p.4, Table 1. Pin functions, CSN |
| 3 | SDI | input | Serial data input for SPI communication, sampled on SCK rising edge (connected to MOSI). | DS p.4, Table 1. Pin functions, SDI |
| 4 | SDO | tri_state | Serial data output for SPI communication, shifted out on SCK falling edge (connected to MISO). DS Table 7: SDO tristate after CSN rising edge. | DS p.4, Table 1. Pin functions, SDO; DS p.8, Table 7, tCSNQT |
| 5 | SCK | input | DS: Serial clock for SPI communication. CMOS compatible input. | DS p.4, Table 1. Pin functions, SCK |
| 6 | DIAG | open_collector | DS: Diagnostic feedback pin: open drain logic output (active low). | DS p.4, Table 1. Pin functions, DIAG; DS p.10, Table 11 |
| 7 | TEST1 | passive | DS: Test mode pin 1. It must be connected to the ground through 1 kohm resistor. | DS p.4, Table 1. Pin functions, TEST1 |
| 8 | TEST2 | passive | DS: Test mode pin 2. It must be connected to the ground through 1 kohm resistor. | DS p.4, Table 1. Pin functions, TEST2 |
| 9 | DIN | input | DS: Direct input to wake-up device from Standby and to control directly gate turn-on/turn-off. If not used, must be connected to the ground through 1 kohm resistor. | DS p.4, Table 1. Pin functions, DIN |
| 10 | HWLO | input | DS: Active high input compatible with 3.3 V and 5 V CMOS. If not used, must be connected to the ground through 1 kohm resistor. | DS p.4, Table 1. Pin functions, HWLO |
| 11 | N.C | no_connect | DS: N.C, "Not connected." (name in DS Table 1 is N.C) | DS p.4, Table 1. Pin functions, N.C |
| 12 | V3V3 | power_out | DS: Output of the 3.3 V internal LDO voltage regulator (logic and I/O supply). Connect a low ESR capacitor (1 uF) close to this pin. | DS p.4, Table 1. Pin functions, V3V3 |
| 13 | GND | power_in | DS: Ground connection. | DS p.4, Table 1. Pin functions, GND |
| 14 | EXT_LDO | power_in | DS: External V3V3 supply. If not used, must be connected to the ground through 1 kohm resistor. | DS p.4, Table 1. Pin functions, EXT_LDO |
| 15 | OUTST | open_collector | Gate status monitor. Reports HS_GATE status (OUTST = H when HS_GATE is high). Connect to ground by a 8.2 kohm resistor. Open drain, active high (DS Table 10 note 1). | DS p.4, Table 1. Pin functions, OUTST; DS p.10, Table 10 |
| 16 | N.C | no_connect | DS: N.C, "Not connected." (name in DS Table 1 is N.C) | DS p.4, Table 1. Pin functions, N.C |
| 17 | N.C | no_connect | DS: N.C, "Not connected." (name in DS Table 1 is N.C) | DS p.4, Table 1. Pin functions, N.C |
| 18 | NTC_M | passive | Negative input pin for external NTC resistor. | DS p.4, Table 1. Pin functions, NTC_M |
| 19 | NTC | passive | DS: Positive input pin for external NTC resistor. | DS p.4, Table 1. Pin functions, NTC |
| 20 | ISNS_N | input | DS: Current sense amplifier negative input. | DS p.4, Table 1. Pin functions, ISNS_N |
| 21 | ISNS_P | input | DS: Current sense amplifier positive input. | DS p.4, Table 1. Pin functions, ISNS_P |
| 22 | N.C | no_connect | DS: N.C, "Not connected." (name in DS Table 1 is N.C) | DS p.4, Table 1. Pin functions, N.C |
| 23 | OUT | passive | DS: External MOSFET source connection. | DS p.4, Table 1. Pin functions, OUT |
| 24 | HS_GATE | output | DS: External MOSFET gate connection (gate drive output). | DS p.4, Table 1. Pin functions, HS_GATE |
| 25 | VS | power_in | DS: Supply pin. Connect to the 12 V, 24 V, 48 V battery voltage by a Schottky diode. | DS p.4, Table 1. Pin functions, VS |
| 26 | N.C | no_connect | DS: N.C, "Not connected." (name in DS Table 1 is N.C) | DS p.4, Table 1. Pin functions, N.C |
| 27 | CP | power_out | DS: Charge pump output. | DS p.4, Table 1. Pin functions, CP |
| 28 | CP2P | passive | DS: Charge pump, positive terminal of the flying capacitor CP2. | DS p.4, Table 1. Pin functions, CP2P |
| 29 | CP2M | passive | DS: Charge pump, negative terminal of the flying capacitor CP2. | DS p.4, Table 1. Pin functions, CP2M |
| 30 | CP1P | passive | DS: Charge pump, positive terminal of the flying capacitor CP1. | DS p.4, Table 1. Pin functions, CP1P |
| 31 | CP1M | passive | DS: Charge pump, negative terminal of the flying capacitor CP1. | DS p.4, Table 1. Pin functions, CP1M |
| 32 | N.C | no_connect | DS: N.C, "Not connected." (name in DS Table 1 is N.C) | DS p.4, Table 1. Pin functions, N.C |
| 33 | GND | power_in | DS: TAB (footprint pad 33), the exposed pad (corner leads electrically connected to TAB, DS p.3). DS note: "TAB connection must be to the ground. TAB is not intended as the device reference ground (a dedicated pin shall be used)." | DS p.4, Table 1. Pin functions, TAB (GND); DS p.3, Figure 2 note |

## Parameters: abs_max

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| VS pin DC voltage | VS | -0.3 |  | 70 | V | Note: DS states no reference pin. Read as voltage to the part's GND pin (DS p.3 note: TAB is not the reference ground, a dedicated pin shall be used). Covered by vs_op (60 V) on the same pin. | DS p.5, Table 2. Absolute maximum ratings, VS |  |
| GND pin reverse DC current | -IGND |  |  | 200 | mA | Note: Single printed value 200 mA (reverse current magnitude), stored as max. | DS p.5, Table 2. Absolute maximum ratings, -IGND |  |
| VSPI pin DC voltage | VSPI | -0.3 |  | 6.5 | V | Note: No reference pin stated (see abs_vs note). The 6.5 V limit is looser than the checked rec_op row vspi_op (3.0 to 6.0 V). | DS p.5, Table 2. Absolute maximum ratings, VSPI |  |
| V3V3 pin DC voltage | V3V3 | -0.3 |  | 4.6 | V |  | DS p.5, Table 2. Absolute maximum ratings, V3V3 |  |
| EXT_LDO pin DC voltage | VEXT_LDO | -0.3 |  | 4.6 | V | Note: No reference pin stated (see abs_vs note). Circuit sets it: ground through 1 kohm when unused, or external 3.3 V supply (Table 1, pin 14). | DS p.5, Table 2. Absolute maximum ratings, VEXT_LDO |  |
| SPI input pins DC voltage (CSN, SDI, SCK) | VCSN, VSDI, VSCK | -0.3 |  | 6.5 | V | Note: No reference pin stated (see abs_vs note). | DS p.5, Table 2. Absolute maximum ratings, VCSN, VSDI, VSCK |  |
| SDO pin DC voltage | VSDO | -0.3 |  | 6.5 | V | Note: Printed -0.3 to VSPI + 0.3, < 6.5 V (DS p.5 Table 2). Absolute limit kept here; the VSPI + 0.3 limit is abs_sdo_vspi. SDO is driven by the part. | DS p.5, Table 2. Absolute maximum ratings, VSDO |  |
| SDO pin DC voltage relative to VSPI | VSDO |  |  | 0.3 (rel. VSPI) | V | Note: Printed -0.3 to VSPI + 0.3, < 6.5 V (DS p.5 Table 2). min -0.3 absolute (see abs_sdo); max relative to VSPI (max_ref = VSPI). | DS p.5, Table 2. Absolute maximum ratings, VSDO (VSPI + 0.3 V) |  |
| HWLO pin DC voltage | VHWLO | -0.3 |  | 70 | V | Note: No reference pin stated (see abs_vs note). | DS p.5, Table 2. Absolute maximum ratings, VHWLO |  |
| DIAG pin DC voltage | VDIAG | -0.3 |  | 4.6 | V | Note: Printed -0.3 to V3V3 + 0.3, < 4.6 V (DS p.5 Table 2). Absolute limit kept here; the V3V3 + 0.3 limit is abs_diag_v3v3. Open-drain pin: the high level comes from the external pull-up, so the circuit sets it. | DS p.5, Table 2. Absolute maximum ratings, VDIAG |  |
| VDIAG pin DC voltage relative to V3V3 | VDIAG |  |  | 0.3 (rel. V3V3) | V | Note: Printed -0.3 to V3V3 + 0.3, < 4.6 V (DS p.5 Table 2). min -0.3 absolute (see abs_diag); max relative to V3V3 (max_ref = V3V3). | DS p.5, Table 2. Absolute maximum ratings, VDIAG (V3V3 + 0.3 V) |  |
| DIAG pin DC current | IDIAG |  | Internally limited |  | mA |  | DS p.5, Table 2. Absolute maximum ratings, IDIAG |  |
| ISNS_P and ISNS_N pins voltage | VISNS_P, VISNS_N | -15 |  | 70 | V | Note: No reference pin stated (see abs_vs note). Circuit sets them through the shunt. | DS p.5, Table 2. Absolute maximum ratings, VISNS_P, VISNS_N |  |
| Differential DC input voltage (VSENSE = VISNS_P - VISNS_N) | dVISNS |  |  | 3.3 (rel. ISNS_N) | V | Note: Printed '< 3.3' (DS p.5 Table 2, Differential DC input voltage VSENSE = VISNS_P - VISNS_N). No minimum is printed on p.5. Stored as max 3.3 V relative to ISNS_N (max_ref = ISNS_N), checked on ISNS_P. | DS p.5, Table 2. Absolute maximum ratings, Differential DC input voltage (VSENSE = VISNS_P - VISNS_N) |  |
| HS_GATE pin DC voltage | VHS_GATE | -15 |  | 20 (rel. OUT) | V | Note: Printed -15 to Vout + 20 V. max is relative to OUT (max_ref = OUT, the printed reference). min -15 V is absolute. | DS p.5, Table 2. Absolute maximum ratings, VHS_GATE |  |
| OUT pin DC voltage | VOUT | -15 |  | 3 (rel. VS) | V | Note: Printed -15 to VS + 3 V. max is relative to VS (max_ref = VS, the printed reference). min -15 V is absolute. Circuit sets OUT through the load and external MOSFET. | DS p.5, Table 2. Absolute maximum ratings, VOUT |  |
| NTC, NTC_M pins DC voltage | VNTC, VNTC_M | -15 |  | 0.3 (rel. ISNS_P) | V | Note: Printed -15 to VISNS_P + 0.3 V. max is relative to ISNS_P (max_ref = ISNS_P, the printed reference). | DS p.5, Table 2. Absolute maximum ratings, VNTC, VNTC_M |  |
| CP pin DC voltage | VCP | -0.3 (rel. VS) |  | 20 (rel. VS) | V | Note: Printed VS - 0.3 to VS + 20 V (both relative to VS, the printed reference). | DS p.5, Table 2. Absolute maximum ratings, VCP |  |
| CP1P, CP2P pins DC voltage | VCP1P, VCP2P | -0.3 (rel. VS) |  | 20 (rel. VS) | V | Note: Printed VS - 0.3 to VS + 20 V (relative to VS). | DS p.5, Table 2. Absolute maximum ratings, VCP1P, VCP2P |  |
| CP1M, CP2M pins DC voltage | VCP1M, VCP2M | -0.3 |  | 0.3 (rel. VS) | V | Note: Printed -0.3 to VS + 0.3 V: min absolute, max relative to VS. | DS p.5, Table 2. Absolute maximum ratings, VCP1M, VCP2M |  |
| DIN pin DC voltage | VDIN | -0.3 |  | 70 | V | Note: No reference pin stated (see abs_vs note). | DS p.5, Table 2. Absolute maximum ratings, VDIN |  |
| OUTST pin DC voltage | VOUTST | -0.3 |  | 4.6 | V | Note: Printed -0.3 to V3V3 + 0.3, < 4.6 V (DS p.5 Table 2). Absolute limit kept here; the V3V3 + 0.3 limit is abs_outst_v3v3. Open-drain pin: the high level comes from the external pull-up, so the circuit sets it. | DS p.5, Table 2. Absolute maximum ratings, VOUTST |  |
| VOUTST pin DC voltage relative to V3V3 | VOUTST |  |  | 0.3 (rel. V3V3) | V | Note: Printed -0.3 to V3V3 + 0.3, < 4.6 V (DS p.5 Table 2). min -0.3 absolute (see abs_outst); max relative to V3V3 (max_ref = V3V3). | DS p.5, Table 2. Absolute maximum ratings, VOUTST (V3V3 + 0.3 V) |  |
| ESD, JEDEC 22A-114F (HBM), general pins | VESD |  |  | 2000 | V | JEDEC 22A-114F Note: Printed as a single value with no sign: stored as max. No footnote on this row, so it applies to all pins. | DS p.5, Table 2. Absolute maximum ratings, Electrostatic discharge (JEDEC 22A-114F), 2000 |  |
| ESD, JEDEC 22A-114F (HBM), VS, OUT, DIN only | VESD |  |  | 4000 | V | JEDEC 22A-114F Note: DS footnote 1: only for pins VS, OUT, DIN. | DS p.5, Table 2. Absolute maximum ratings, Electrostatic discharge (JEDEC 22A-114F), 4000 (1) |  |
| ESD, CDM-AEC-Q100-011, all pins except corners | VESD | -500 |  | 500 | V | CDM-AEC-Q100-011 Note: Printed +/-500 V: min = -500, max = 500 (symmetric). DS footnote 2: all pins except corners. | DS p.5, Table 2. Absolute maximum ratings, Charge device model (CDM-AEC-Q100-011), +/-500 (2) |  |
| ESD, CDM-AEC-Q100-011, corner pins | VESD | -750 |  | 750 | V | CDM-AEC-Q100-011 Note: Printed +/-750 V: min = -750, max = 750. DS footnote 3: corner pins. | DS p.5, Table 2. Absolute maximum ratings, Charge device model (CDM-AEC-Q100-011), +/-750 (3) |  |
| Junction operating temperature | TJ | -40 |  | 150 | degC | Note: Junction temperature only; no ambient rating is printed, so no check_ambient. | DS p.5, Table 2. Absolute maximum ratings, Junction operating temperature (TJ) |  |
| Storage temperature | Tstg | -55 |  | 150 | degC |  | DS p.5, Table 2. Absolute maximum ratings, Storage temperature |  |
| Maximum number of FTP NVM programming cycles | NFTP |  |  | 1000 |  |  | DS p.6, Table 2. Absolute maximum ratings (continued), NFTP |  |

## Parameters: rec_op

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Operating supply voltage | VS | 6 | 48 | 60 | V | 6 V < VS < 60 V; -40 degC < TJ < 150 degC (general condition, DS p.6 2.3); typ at VS = 48 V, TJ = 25 degC | DS p.6, Table 4. Supply specification, VS |  |
| Extended operating supply voltage | VS_EXT | 6 |  | 70 | V | 100 ms max. duration Note: The 70 V limit is abs_vs (not checked, covered by vs_op). A 100 ms duration cannot be modelled by a DC check. | DS p.6, Table 4. Supply specification, VS_EXT |  |
| SPI pin operating range | VSPI | 3.0 |  | 6.0 | V |  | DS p.7, Table 4. Supply specification, VSPI |  |

## Parameters: electrical

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Low level voltage EXT_LDO | VEXT_LDO_L | 2.6 | 2.8 | 3 | V |  | DS p.6, Table 4. Supply specification, VEXT_LDO_L |  |
| High level voltage EXT_LDO | VEXT_LDO_H | 2.8 | 3 | 3.2 | V |  | DS p.6, Table 4. Supply specification, VEXT_LDO_H |  |
| Current consumption from EXT_LDO when externally supplied | IEXT_LDO_H | 3.5 | 5 | 6 | mA | VEXT_LDO > VEXT_LDO_H | DS p.6, Table 4. Supply specification, IEXT_LDO_H |  |
| Current consumption from EXT_LDO | IEXT_LDO_L | 6 | 10 | 16 | uA | VEXT_LDO < VEXT_LDO_L | DS p.6, Table 4. Supply specification, IEXT_LDO_L |  |
| Undervoltage shutdown (VS) | VS_USD1 | 3.8 | 4 | 4.2 | V | Field UV_THR = 00b or 01b in CR#3 | DS p.6, Table 4. Supply specification, VS_USD1 |  |
| Undervoltage shutdown (VS) | VS_USD2 | 12 | 13 | 14 | V | Field UV_THR = 10b in CR#3 | DS p.6, Table 4. Supply specification, VS_USD2 |  |
| Undervoltage shutdown (VS) | VS_USD3 | 22 | 24 | 25 | V | Field UV_THR = 11b in CR#3 | DS p.6, Table 4. Supply specification, VS_USD3 |  |
| Undervoltage shutdown reset (VS) | VS_USD_RES1 | 4.3 | 4.5 | 4.8 | V | Field UV_THR = 00b or 01b in CR#3 | DS p.6, Table 4. Supply specification, VS_USD_RES1 |  |
| Undervoltage shutdown reset (VS) | VS_USD_RES2 | 13 | 14 | 15 | V | Field UV_THR = 10b in CR#3 | DS p.6, Table 4. Supply specification, VS_USD_RES2 |  |
| Undervoltage shutdown reset (VS) | VS_USD_RES3 | 24 | 27 | 29 | V | Field UV_THR = 11b in CR#3 | DS p.6, Table 4. Supply specification, VS_USD_RES3 |  |
| Undervoltage shutdown hysteresis (VS) | VS_USD_HYS1 |  | 0.5 |  | V | Field UV_THR = 00b or 01b in CR#3 | DS p.6, Table 4. Supply specification, VS_USD_HYS1 |  |
| Undervoltage shutdown hysteresis (VS) | VS_USD_HYS2 |  | 1 |  | V | Field UV_THR = 10b in CR#3 | DS p.6, Table 4. Supply specification, VS_USD_HYS2 |  |
| Undervoltage shutdown hysteresis (VS) | VS_USD_HYS3 |  | 3 |  | V | Field UV_THR = 11b in CR#3 | DS p.6, Table 4. Supply specification, VS_USD_HYS3 |  |
| Undervoltage shutdown filtering time | tVS_USD |  | 33 |  | us |  | DS p.6, Table 4. Supply specification, tVS_USD |  |
| Undervoltage shutdown on VSPI | VSPI_UV | 1.5 | 1.6 | 1.8 | V |  | DS p.7, Table 4. Supply specification, VSPI_UV |  |
| Undervoltage shutdown reset on VSPI | VSPI_UV_RESET | 2 | 2.1 | 2.2 | V |  | DS p.7, Table 4. Supply specification, VSPI_UV_RESET |  |
| SPI supply current during frame communication | ISPI |  |  | 3 | mA |  | DS p.7, Table 4. Supply specification, ISPI |  |
| SPI supply current in Standby state | ISPI_STBY |  |  | 5 | uA |  | DS p.7, Table 4. Supply specification, ISPI_STBY |  |
| Supply current on VS pin (includes logic), VS = 13 V | IS(ON) |  | 8.6 |  | mA | VEXT_LDO < VEXT_LDO_L (internal LDO active); OUT = VS; HS_GATE on, RGB = 47 kohm; VS = 13 V | DS p.7, Table 4. Supply specification, IS(ON) row 1 |  |
| Supply current on VS pin (includes logic), VS = 48 V | IS(ON) |  | 7.9 |  | mA | VEXT_LDO < VEXT_LDO_L (internal LDO active); OUT = VS; HS_GATE on, RGB = 47 kohm; VS = 48 V | DS p.7, Table 4. Supply specification, IS(ON) row 2 |  |
| Supply current on VS pin (includes logic), VS = 48 V, charge pump off | IS(ON) | 4.5 | 7.2 | 8.5 | mA | VEXT_LDO < VEXT_LDO_L (internal LDO active); OUT = VS; VS = 48 V; measured in test mode with the charge pump off (DS note 2) | DS p.7, Table 4. Supply specification, IS(ON) row 3 |  |
| Supply current on VS pin (includes logic), external LDO, VS = 13 V | IS(ON) |  | 4 |  | mA | VEXT_LDO > VEXT_LDO_H (external LDO, internal LDO disabled); OUT = VS; HS_GATE on, RGB = 47 kohm; VS = 13 V | DS p.7, Table 4. Supply specification, IS(ON) row 4 |  |
| Supply current on VS pin (includes logic), external LDO, VS = 48 V | IS(ON) |  | 3.1 |  | mA | VEXT_LDO > VEXT_LDO_H (external LDO, internal LDO disabled); OUT = VS; HS_GATE on, RGB = 47 kohm; VS = 48 V | DS p.7, Table 4. Supply specification, IS(ON) row 5 |  |
| Output current Standby mode, VS = 13 V | IOUT_STDBY | 1.5 | 3 | 5 | uA | VS = 13 V, Standby mode, OUT = GND | DS p.7, Table 4. Supply specification, IOUT_STDBY row 1 |  |
| Output current Standby mode, VS = 48 V | IOUT_STDBY | 1 | 3 | 5 | uA | VS = 48 V, Standby mode, OUT = GND | DS p.7, Table 4. Supply specification, IOUT_STDBY row 2 |  |
| Output current Unlocked mode, VS = 13 V | IOUT_ON | 140 | 185 | 230 | uA | VS = 13 V, Unlocked mode, OUT = GND | DS p.7, Table 4. Supply specification, IOUT_ON row 1 |  |
| Output current Unlocked mode, VS = 48 V | IOUT_ON | 210 | 250 | 320 | uA | VS = 48 V, Unlocked mode, OUT = GND | DS p.7, Table 4. Supply specification, IOUT_ON row 2 |  |
| VS pin quiescent current (includes logic), independent of P-channel bypass | IS_Q | 45 | 60 | 70 | uA | VS = 48 V, TJ = 25 degC, OUT = VS Note: Unmarked TJ = 25 degC row in the test conditions: scope 25C. | DS p.7, Table 4. Supply specification, IS_Q row 1 |  |
| VS pin quiescent current (includes logic), independent of P-channel bypass | IS_Q | 50 | 60 | 75 | uA | VS = 48 V, TJ = 25 degC, OUT = GND Note: TJ = 25 degC: scope 25C. | DS p.7, Table 4. Supply specification, IS_Q row 2 |  |
| VS pin quiescent current (includes logic), independent of P-channel bypass | IS_Q | 30 | 48 | 57 | uA | VS = 13 V, TJ = 25 degC, OUT = VS Note: TJ = 25 degC: scope 25C. | DS p.7, Table 4. Supply specification, IS_Q row 3 |  |
| Power-on reset threshold (device leaves reset mode) | VS_POR_ON | 2.4 | 2.5 | 2.65 | V |  | DS p.7, Table 4. Supply specification, VS_POR_ON |  |
| Power-on shutdown threshold (device enters reset mode) | VS_POR_OFF | 2.2 | 2.3 | 2.45 | V |  | DS p.7, Table 4. Supply specification, VS_POR_OFF |  |
| Power-on reset hysteresis | VS_POR_HYST |  | 0.2 |  | V |  | DS p.7, Table 4. Supply specification, VS_POR_HYST |  |
| Time from power-on to Standby | tPWON |  |  | 500 | us | VS > VS_POR_ON, V3V3 external capacitor 1 uF | DS p.7, Table 4. Supply specification, tPWON |  |
| Low level input current (SCK and SDI) | IIL | 1.7 |  | 4 | uA | VIL = 1.5 V | DS p.8, Table 5. SPI logic inputs (CSN, SCK, and SDI) specification, IIL (SCK and SDI) |  |
| Low level input current (CSN) | IIL | -2.9 |  | -2 | uA | VIL = 1.5 V | DS p.8, Table 5. SPI logic inputs (CSN, SCK, and SDI) specification, IIL (CSN) |  |
| High level input current (SCK and SDI) | IIH | -13 |  | -3 | uA | VIH = 2.1 V | DS p.8, Table 5. SPI logic inputs (CSN, SCK, and SDI) specification, IIH (SCK and SDI) |  |
| High level input current (CSN) | IIH | -18 |  | -10 | uA | VIH = 2.1 V | DS p.8, Table 5. SPI logic inputs (CSN, SCK, and SDI) specification, IIH (CSN) |  |
| Low level input voltage (CSN, SCK, SDI) | VIL |  |  | 1.5 | V |  | DS p.8, Table 5. SPI logic inputs (CSN, SCK, and SDI) specification, VIL |  |
| High level input voltage (CSN, SCK, SDI) | VIH | 2.1 |  |  | V |  | DS p.8, Table 5. SPI logic inputs (CSN, SCK, and SDI) specification, VIH |  |
| Input hysteresis voltage (CSN, SCK, SDI) | VI_HYST |  | 0.4 |  | V |  | DS p.8, Table 5. SPI logic inputs (CSN, SCK, and SDI) specification, VI_HYST |  |
| Low level output voltage (SDO) | VOL |  | 0.3 * VSPI |  | V | Note: Printed max 0.3 * VSPI: a formula, stored as text. | DS p.8, Table 6. SPI logic output (SDO) specification, VOL |  |
| High level output voltage (SDO) | VOH |  | 0.7 * VSPI |  | V | Note: Printed min 0.7 * VSPI: a formula, stored as text. | DS p.8, Table 6. SPI logic output (SDO) specification, VOH |  |
| Low level output current (SDO) | ISDO_Ilow | 45 |  | 96 | mA | VSDO = 1 V, VSPI = 5 V | DS p.8, Table 6. SPI logic output (SDO) specification, ISDO_Ilow |  |
| High level output current (SDO) | ISDO_Ihigh | 15 |  | 32 | mA | VSDO = 4 V, VSPI = 5 V | DS p.8, Table 6. SPI logic output (SDO) specification, ISDO_Ihigh |  |
| Output leakage current (SDO) | ILO | -1 |  | 1 | uA | Note: Printed as a limit without TYP: stored min -1, max 1 (symmetric). | DS p.8, Table 6. SPI logic output (SDO) specification, ILO |  |
| SPI clock frequency | fSCK |  |  | 8 | MHz |  | DS p.8, Table 7. SPI timing specification, fSCK |  |
| SCK high time | tHSCK | 55 |  |  | ns |  | DS p.8, Table 7. SPI timing specification, tHSCK |  |
| SCK low time | tLSCK | 55 |  |  | ns |  | DS p.8, Table 7. SPI timing specification, tLSCK |  |
| CSN high time | tHCSN | 1 |  |  | us |  | DS p.8, Table 7. SPI timing specification, tHCSN |  |
| CSN setup time: CSN low before SCK rising edge | tSCSN | 100 |  |  | ns |  | DS p.8, Table 7. SPI timing specification, tSCSN |  |
| SCK setup time: SCK low before CSN rising edge | tSSCK | 100 |  |  | ns |  | DS p.8, Table 7. SPI timing specification, tSSCK |  |
| SDI setup time before SCK rising edge | tSSDI | 25 |  |  | ns |  | DS p.8, Table 7. SPI timing specification, tSSDI |  |
| SDI hold time | tHSDI | 20 |  |  | ns |  | DS p.8, Table 7. SPI timing specification, tHSDI |  |
| CSN falling edge until SDO valid | tCSNQV |  |  | 70 | ns |  | DS p.8, Table 7. SPI timing specification, tCSNQV |  |
| CSN rising edge until SDO tristate | tCSNQT |  | 220 |  | ns |  | DS p.8, Table 7. SPI timing specification, tCSNQT |  |
| SCK falling edge until SDO valid | tSCKQV |  |  | 50 | ns |  | DS p.8, Table 7. SPI timing specification, tSCKQV |  |
| SDO rise time | tRSDO |  |  | 25 | ns |  | DS p.8, Table 7. SPI timing specification, tRSDO |  |
| SDO fall time | tFSDO |  |  | 25 | ns |  | DS p.8, Table 7. SPI timing specification, tFSDO |  |
| CSN low timeout (MCU maximum time to send an SPI frame) | tWHCH | -10 % | 50 | +10 % | ms | Note: Min -10 % and Max +10 % printed as offsets from typ: stored as tol_pct. DS note 1: if violated, DIAG error. | DS p.8, Table 7. SPI timing specification, tWHCH |  |
| Watchdog toggle bit timeout | tWDTB | -10 % | 50 | +10 % | ms | WD_TIME = 00b (see CR#3) Note: Typ column lists the four WD_TIME settings; the Min/Max -10 % / +10 % columns are offsets: stored as tol_pct. | DS p.8, Table 7. SPI timing specification, tWDTB, WD_TIME setting 00b |  |
| Watchdog toggle bit timeout | tWDTB | -10 % | 100 | +10 % | ms | WD_TIME = 01b (see CR#3) Note: Typ column lists the four WD_TIME settings; the Min/Max -10 % / +10 % columns are offsets: stored as tol_pct. | DS p.8, Table 7. SPI timing specification, tWDTB, WD_TIME setting 01b |  |
| Watchdog toggle bit timeout | tWDTB | -10 % | 150 | +10 % | ms | WD_TIME = 10b (see CR#3) Note: Typ column lists the four WD_TIME settings; the Min/Max -10 % / +10 % columns are offsets: stored as tol_pct. | DS p.8, Table 7. SPI timing specification, tWDTB, WD_TIME setting 10b |  |
| Watchdog toggle bit timeout | tWDTB | -10 % | 200 | +10 % | ms | WD_TIME = 11b (see CR#3) Note: Typ column lists the four WD_TIME settings; the Min/Max -10 % / +10 % columns are offsets: stored as tol_pct. | DS p.8, Table 7. SPI timing specification, tWDTB, WD_TIME setting 11b |  |
| Minimum CSN low time to wake the device from Standby | tSTBY_OUT | 2 | 4 | 6 | us | Device in Standby state | DS p.8, Table 7. SPI timing specification, tSTBY_OUT |  |
| Low level input current (HWLO) | IIL | 0.5 |  | 2.5 | uA | VIL = 1.5 V | DS p.9, Table 8. HWLO logic input pin specification, IIL |  |
| High level input current (HWLO) | IIH | 1.6 |  | 3.5 | uA | VIH = 2.1 V | DS p.9, Table 8. HWLO logic input pin specification, IIH |  |
| Low level input voltage (HWLO) | VIL |  |  | 1.5 | V |  | DS p.9, Table 8. HWLO logic input pin specification, VIL |  |
| High level input voltage (HWLO) | VIH | 2.1 |  |  | V |  | DS p.9, Table 8. HWLO logic input pin specification, VIH |  |
| Input hysteresis voltage (HWLO) | VI_HYST |  | 0.4 |  | V |  | DS p.9, Table 8. HWLO logic input pin specification, VI_HYST |  |
| HWLO filtering time | tHWLO | -10 % | 33 | +10 % | us | Note: Min -10 % and Max +10 % printed as offsets: stored as tol_pct. | DS p.9, Table 8. HWLO logic input pin specification, tHWLO |  |
| Low level input current (DIN) | IIL | 1.5 |  | 5 | uA | VIL = 1.5 (unit not printed; V) | DS p.9, Table 9. DIN logic input pin specification, IIL |  |
| High level input current (DIN) | IIH | -12 |  | -2 | uA | VIH = 2.1 (unit not printed; V) | DS p.9, Table 9. DIN logic input pin specification, IIH |  |
| Low level input voltage (DIN) | VIL | 1.48 | 1.59 | 1.73 | V |  | DS p.9, Table 9. DIN logic input pin specification, VIL |  |
| High level input voltage (DIN) | VIH | 2.01 | 2.05 | 2.1 | V |  | DS p.10, Table 9. DIN logic input pin specification, VIH |  |
| Input hysteresis voltage (DIN) | VI_HYST |  | 0.4 |  | V |  | DS p.10, Table 9. DIN logic input pin specification, VI_HYST |  |
| Filtering time on DIN rise edge for device wakeup | tDIN_WAKEUP |  | 4 |  | us |  | DS p.10, Table 9. DIN logic input pin specification, tDIN_WAKEUP |  |
| De-glitch filtering time on DIN rise and fall edges | tDIN_DEGLITCH | -10 % | 1.2 | +10 % | us | Note: Min -10 % / Max +10 % printed as offsets: stored as tol_pct. | DS p.10, Table 9. DIN logic input pin specification, tDIN_DEGLITCH |  |
| Filtering time on DIN rise edge for direct control of external MOSFET in Fail-safe state | tDIN_RISE_FILTER | -15 % | 10 | +10 % | us | Note: Min -15 % / Max +10 % printed as offsets: stored as tol_pct. | DS p.10, Table 9. DIN logic input pin specification, tDIN_RISE_FILTER |  |
| DIN toggling timeout | tDIN_TOGGLE_TOUT | -10 % | 20 | +10 % | us | Note: Min -10 % / Max +10 % printed as offsets: stored as tol_pct. | DS p.10, Table 9. DIN logic input pin specification, tDIN_TOGGLE_TOUT |  |
| OUTST pin open-drain high level (pull-up) voltage | VOUTST_PU | 3.15 |  |  | V | HS_GATE = on; IOUTST_PU = 1 mA Note: DS note 1: OUTST is an active high open drain pin. | DS p.10, Table 10. OUTST logic output pin specification, VOUTST_PU |  |
| OUTST pin open-drain output current | IOUTST_PU |  |  | 1 | mA |  | DS p.10, Table 10. OUTST logic output pin specification, IOUTST_PU |  |
| OUTST pin leakage current | IOUTST_LKG | 0 |  | 16 | uA | HS_GATE = on Note: The Parameter cell of this row is blank in the DS; the name is taken from the symbol. | DS p.10, Table 10. OUTST logic output pin specification, IOUTST_LKG |  |
| DIAG pin open-drain pull-down voltage | VDIAG_PD |  |  | 0.2 | V | IDIAG_PD = 1 mA Note: DS note 1: DIAG is an active low open drain pin. | DS p.10, Table 11. DIAG logic output pin specification, VDIAG_PD |  |
| DIAG pin open-drain input current | IDIAG_PD |  |  | 1 | mA | VDIAG = VDIAG_PD | DS p.10, Table 11. DIAG logic output pin specification, IDIAG_PD |  |
| DIAG pin open-drain leakage current | IDIAG_LKG | 0 |  | 1 | uA | VDIAG = V3V3 = 4.6 V | DS p.10, Table 11. DIAG logic output pin specification, IDIAG_LKG |  |
| Charge pump output voltage, VS = 6 V | VCP_6V | 7 (rel. VS) | 11 (rel. VS) |  | V | VS = 6 V Note: DS p.10 Table 12 prints typ VS + 11 V (typ_ref = VS); min and max are also relative to VS (min_ref / max_ref = VS). | DS p.10, Table 12. Charge pump specification, VCP_6V |  |
| Charge pump output voltage, VS > 10 V | VCP_10V | 13.5 (rel. VS) | 14.5 (rel. VS) | 15.5 (rel. VS) | V | VS > 10 V Note: DS p.10 Table 12 prints typ VS + 14.5 V (typ_ref = VS); min and max are also relative to VS (min_ref / max_ref = VS). | DS p.10, Table 12. Charge pump specification, VCP_10V |  |
| Charge pump output undervoltage high threshold (ramp up on VCP) | VCP_LOW_H | 5.5 (rel. VS) | 6 (rel. VS) | 6.5 (rel. VS) | V | Ramp up on VCP Note: DS p.10 Table 12 prints typ VS + 6 V (typ_ref = VS); min and max are also relative to VS (min_ref / max_ref = VS). | DS p.10, Table 12. Charge pump specification, VCP_LOW_H |  |
| Charge pump output undervoltage low threshold (ramp down on VCP) | VCP_LOW_L | 5.1 (rel. VS) | 5.6 (rel. VS) | 6.2 (rel. VS) | V | Ramp down on VCP Note: DS p.10 Table 12 prints typ VS + 5.6 V (typ_ref = VS); min and max are also relative to VS (min_ref / max_ref = VS). | DS p.10, Table 12. Charge pump specification, VCP_LOW_L |  |
| Charge pump output undervoltage hysteresis | VCP_LOW_hyst |  | 0.4 |  | V |  | DS p.10, Table 12. Charge pump specification, VCP_LOW_hyst |  |
| Charge pump frequency | fCP | -5 % | 400 | +5 % | kHz | Note: Min -5 % / Max +5 % printed as offsets: stored as tol_pct. | DS p.10, Table 12. Charge pump specification, fCP |  |
| Charge pump low (CP_LOW diagnostic) rising edge filtering time | tCP_RISE | -5 % | 60 | +5 % | us | Note: Min -5 % / Max +5 % printed as offsets: stored as tol_pct. Refers to SR#1. | DS p.10, Table 12. Charge pump specification, tCP_RISE |  |
| Charge pump low (CP_LOW diagnostic) falling edge filtering time | tCP_FALL | -10 % | 2.3 | +10 % | us | Note: Min -10 % / Max +10 % printed as offsets: stored as tol_pct. Refers to SR#1. | DS p.10, Table 12. Charge pump specification, tCP_FALL |  |
| HS_GATE pin on voltage, VS = 6 V | VGSON_6V | 6 |  |  | V | VS = 6 V, IG = 50 uA | DS p.11, Table 13. Gate driver specification, VGSON_6V |  |
| HS_GATE pin on voltage, VS > 10 V | VGSON_10V | 11.5 |  | 15 | V | VS > 10 V, IG = 50 uA | DS p.11, Table 13. Gate driver specification, VGSON_10V |  |
| HS_GATE pin off voltage | VGSOFF |  |  | 0.5 | V |  | DS p.11, Table 13. Gate driver specification, VGSOFF |  |
| Maximum HS_GATE pin voltage (internally limited) | VGSMAX |  |  | 20 | V |  | DS p.11, Table 13. Gate driver specification, VGSMAX |  |
| HS_GATE pin turn-on time | tON |  |  | 3 | us | VGS = 0.5 V to VGS = 10 V, CGATE = 80 nF | DS p.11, Table 13. Gate driver specification, tON |  |
| HS_GATE pin turn-off time | tOFF |  |  | 10 | us | Full VGS to VGS < 0.5 V, CGATE = 80 nF | DS p.11, Table 13. Gate driver specification, tOFF |  |
| HS_GATE pin undervoltage lockout, VS = 6 V | VGS_UVLO_6V | 3.5 |  |  | V | VS = 6 V | DS p.11, Table 13. Gate driver specification, VGS_UVLO_6V |  |
| HS_GATE pin undervoltage lockout, VS > 10 V | VGS_UVLO_10V | 7 |  |  | V | VS > 10 V, CGATE_max = 30 nF | DS p.11, Table 13. Gate driver specification, VGS_UVLO_10V |  |
| HS_GATE pin undervoltage lockout blanking time | VG_UVLO_BLK | -5 % | 100 | +5 % | us | Enable at charge pump startup if external MOSFET turn-on is required, and applied after CP_LOW expiration (falling edge) Note: Min -5 % / Max +5 % printed as offsets: stored as tol_pct. | DS p.11, Table 13. Gate driver specification, VG_UVLO_BLK |  |
| HS_GATE pin undervoltage lockout de-glitch filtering time | VG_UVLO_DEGLITCH | -15 % | 8 | +15 % | us | Note: Min -15 % / Max +15 % printed as offsets: stored as tol_pct. | DS p.11, Table 13. Gate driver specification, VG_UVLO_DEGLITCH |  |
| Junction temperature thermal shutdown threshold | TTSD | 160 | 175 | 190 | degC |  | DS p.11, Table 14. Device thermal protection with integrated 10-bits ADC, TTSD |  |
| Junction temperature thermal shutdown hysteresis | TTSD_HYS |  | 15 |  | degC |  | DS p.11, Table 14. Device thermal protection with integrated 10-bits ADC, TTSD_HYS |  |
| Junction temperature ADC full-scale range resolution (code) | TJ_ADC_CONV | 0 |  | 1023 |  | Note: Code 0 to 1023 (10 bits). DS note 1: TJ[degC] = TJ_ADC[22:13]/3 - 72 (calc.tj_from_adc_code). | DS p.11, Table 14. Device thermal protection with integrated 10-bits ADC, TJ_ADC_CONV (1) |  |
| Junction temperature ADC sample rate | TJ_ADC_RATE |  | 10 |  | kHz | Note: Printed kSample/s; 1 sample/s = 1 Hz, so stored as kHz. | DS p.11, Table 14. Device thermal protection with integrated 10-bits ADC, TJ_ADC_RATE |  |
| Common-mode input voltage range (VSENSE = VISNS_P - VISNS_N) | VSENSE_CM |  |  | 0 (rel. VS) | V | Note: Printed min CS_UV (the Table 33 entering threshold, DS p.41, 2.78 to 3 V; a parameter reference, not a number here) and max VS. max = 0 relative to VS (max_ref = VS). | DS p.11, Table 15. Integrated current sense amplifier (CSA) for ILOAD measure based on VSENSE, VSENSE_CM |  |
| Differential input voltage full-scale range | VSENSE_FSR | 0 |  | 160 | mV |  | DS p.11, Table 15. Integrated current sense amplifier (CSA) for ILOAD measure based on VSENSE, VSENSE_FSR |  |
| CSA positive input current | IISNS_P | 1.1 | 1.3 | 1.5 | mA | VS = 12 V | DS p.11, Table 15. Integrated current sense amplifier (CSA) for ILOAD measure based on VSENSE, IISNS_P |  |
| CSA negative input current | IISNS_N | 100 | 200 | 300 | uA | VISNS_P = 12 V, VISNS_N = 11.9 V, HS_GATE = on | DS p.11, Table 15. Integrated current sense amplifier (CSA) for ILOAD measure based on VSENSE, IISNS_N |  |
| External MOSFET VDS monitor threshold range (31 steps, VDS_THR field in CR#2) | VDS_THR_RANGE | 300 |  | 1800 | mV | Note: Settings VDS_THR_0 to VDS_THR_30 (decimal; 0x00 to 0x1E) are keyed vds_thr_0 to vds_thr_30. The 0x1F setting has no value printed (blank in DS p.12). DS p.52: 0x1F is reserved. | DS p.11, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_RANGE |  |
| VDS monitor threshold step | VDS_THR_STEP |  | 50 |  | mV |  | DS p.11, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_STEP |  |
| VDS monitor threshold | VDS_THR_0 |  | 300 |  | mV | VDS_THR = 0x00 | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_0 |  |
| VDS monitor threshold | VDS_THR_1 |  | 350 |  | mV | VDS_THR = 0x01 | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_1 |  |
| VDS monitor threshold | VDS_THR_2 |  | 400 |  | mV | VDS_THR = 0x02 | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_2 |  |
| VDS monitor threshold | VDS_THR_3 |  | 450 |  | mV | VDS_THR = 0x03 | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_3 |  |
| VDS monitor threshold | VDS_THR_4 |  | 500 |  | mV | VDS_THR = 0x04 | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_4 |  |
| VDS monitor threshold | VDS_THR_5 |  | 550 |  | mV | VDS_THR = 0x05 | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_5 |  |
| VDS monitor threshold | VDS_THR_6 |  | 600 |  | mV | VDS_THR = 0x06 | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_6 |  |
| VDS monitor threshold | VDS_THR_7 |  | 650 |  | mV | VDS_THR = 0x07 | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_7 |  |
| VDS monitor threshold | VDS_THR_8 |  | 700 |  | mV | VDS_THR = 0x08 | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_8 |  |
| VDS monitor threshold | VDS_THR_9 |  | 750 |  | mV | VDS_THR = 0x09 | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_9 |  |
| VDS monitor threshold | VDS_THR_10 |  | 800 |  | mV | VDS_THR = 0x0A | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_10 |  |
| VDS monitor threshold | VDS_THR_11 |  | 850 |  | mV | VDS_THR = 0x0B | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_11 |  |
| VDS monitor threshold | VDS_THR_12 |  | 900 |  | mV | VDS_THR = 0x0C | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_12 |  |
| VDS monitor threshold | VDS_THR_13 |  | 950 |  | mV | VDS_THR = 0x0D | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_13 |  |
| VDS monitor threshold | VDS_THR_14 |  | 1000 |  | mV | VDS_THR = 0x0E | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_14 |  |
| VDS monitor threshold | VDS_THR_15 |  | 1050 |  | mV | VDS_THR = 0x0F | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_15 |  |
| VDS monitor threshold | VDS_THR_16 |  | 1100 |  | mV | VDS_THR = 0x10 | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_16 |  |
| VDS monitor threshold | VDS_THR_17 |  | 1150 |  | mV | VDS_THR = 0x11 | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_17 |  |
| VDS monitor threshold | VDS_THR_18 |  | 1200 |  | mV | VDS_THR = 0x12 | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_18 |  |
| VDS monitor threshold | VDS_THR_19 |  | 1250 |  | mV | VDS_THR = 0x13 | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_19 |  |
| VDS monitor threshold | VDS_THR_20 |  | 1300 |  | mV | VDS_THR = 0x14 | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_20 |  |
| VDS monitor threshold | VDS_THR_21 |  | 1350 |  | mV | VDS_THR = 0x15 | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_21 |  |
| VDS monitor threshold | VDS_THR_22 |  | 1400 |  | mV | VDS_THR = 0x16 | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_22 |  |
| VDS monitor threshold | VDS_THR_23 |  | 1450 |  | mV | VDS_THR = 0x17 | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_23 |  |
| VDS monitor threshold | VDS_THR_24 |  | 1500 |  | mV | VDS_THR = 0x18 | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_24 |  |
| VDS monitor threshold | VDS_THR_25 |  | 1550 |  | mV | VDS_THR = 0x19 | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_25 |  |
| VDS monitor threshold | VDS_THR_26 |  | 1600 |  | mV | VDS_THR = 0x1A | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_26 |  |
| VDS monitor threshold | VDS_THR_27 |  | 1650 |  | mV | VDS_THR = 0x1B | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_27 |  |
| VDS monitor threshold | VDS_THR_28 |  | 1700 |  | mV | VDS_THR = 0x1C | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_28 |  |
| VDS monitor threshold | VDS_THR_29 |  | 1750 |  | mV | VDS_THR = 0x1D | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_29 |  |
| VDS monitor threshold | VDS_THR_30 |  | 1800 |  | mV | VDS_THR = 0x1E | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_30 |  |
| VDS monitor threshold accuracy | VDS_THR_ACC | -5 |  | 5 | % |  | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_THR_ACC |  |
| VDS monitor shut-off deglitch time | VDS_DEGLITCH | -20 % | 5 | +20 % | us | Note: Min -20 % / Max +20 % printed as offsets: stored as tol_pct. | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_DEGLITCH |  |
| VDS monitor shut-off delay time | VDS_DELAY |  |  | 5 | us | CGATE = 30 nF, T = 105 degC (single stated temperature) | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_DELAY |  |
| VDS monitor shut-off blanking time | VDS_BLK | -10 % | 960 | +10 % | us | At external MOSFET startup Note: DS note 1 (DS p.13): the internal counter stops if HS_GATE is forced low. Min -10 % / Max +10 % printed as offsets: stored as tol_pct. | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_BLK (1) |  |
| VDS monitor ADC full-scale range resolution (code) | VDS_ADC_CONV_RES | 0 |  | 1023 |  | Note: DS note 2 (DS p.13): VDS[V] = VDS_ADC[22:13] * 2.4 / 1280 - 0.05 (calc.vds_from_adc_code). | DS p.12, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_ADC_CONV_RES (2) |  |
| VDS monitor ADC full-scale voltage range | VDS_ADC_CONV | -0.05 |  | 1.87 | V |  | DS p.13, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_ADC_CONV |  |
| VDS monitor ADC sample rate | VDS_ADC_RATE |  | 900 |  | kHz | Note: Printed kSample/s; stored as kHz. | DS p.13, Table 16. External MOSFET VDS protection with integrated fast 10-bits ADC, VDS_ADC_RATE |  |
| Current sense ADC full-scale range resolution (code) | VSENSE_ADC_CONV | 0 |  | 8191 |  | VSENSE_ADC[14:2] = min((VSENSE/160 * 8192), 8191) Note: DS conflict: footnote 1 prints code * 160 / 1024 mV, a misprint (13-bit field [14:2], 8191 clamp and VSENSE_FSR 160 mV all require / 8192). calc.vsense_from_csa_code uses this test condition: VSENSE = code * 160 / 8192 mV. | DS p.13, Table 17. Integrated 13-bit ADC for ILOAD measure based on VSENSE (= VISNS_P - VISNS_N), VSENSE_ADC_CONV (1)(2) |  |
| Current sense ADC sample rate | VSENSE_REFRESH |  | 2.4 |  | kHz | Note: Printed kSample/s; stored as kHz. | DS p.13, Table 17. Integrated 13-bit ADC for ILOAD measure based on VSENSE (= VISNS_P - VISNS_N), VSENSE_REFRESH |  |
| Digital current sense accuracy | VSENSE_ACC_6mV | -10 |  | 10 | % | 6 mV < VSENSE < 10 mV | DS p.13, Table 17. Integrated 13-bit ADC for ILOAD measure based on VSENSE (= VISNS_P - VISNS_N), VSENSE_ACC_6mV |  |
| Digital current sense accuracy | VSENSE_ACC_10mV | -5 |  | 5 | % | 10 mV < VSENSE < 20 mV | DS p.13, Table 17. Integrated 13-bit ADC for ILOAD measure based on VSENSE (= VISNS_P - VISNS_N), VSENSE_ACC_10mV |  |
| Digital current sense accuracy | VSENSE_ACC_20mV | -3 |  | 3 | % | VSENSE > 20 mV | DS p.13, Table 17. Integrated 13-bit ADC for ILOAD measure based on VSENSE (= VISNS_P - VISNS_N), VSENSE_ACC_20mV |  |
| Digital current sense accuracy | VSENSE_ACC_3mV | -17 |  | 17 | % | 3 mV < VSENSE < 6 mV | DS p.13, Table 17. Integrated 13-bit ADC for ILOAD measure based on VSENSE (= VISNS_P - VISNS_N), VSENSE_ACC_3mV |  |
| Digital current sense accuracy | VSENSE_ACC_1.8mV | -0.5 |  | 0.5 | mV | 1.8 mV < VSENSE < 3 mV | DS p.13, Table 17. Integrated 13-bit ADC for ILOAD measure based on VSENSE (= VISNS_P - VISNS_N), VSENSE_ACC_1.8mV |  |
| Hard short circuit protection threshold range (16 steps, HSC_THR field in CR#2) | VHSC_THR_RANGE | 20 |  | 160 | mV |  | DS p.13, Table 18. Load hard short circuit (HSC) protection with integrated 10-bit ADC, VHSC_THR_RANGE |  |
| Hard short circuit protection threshold | VHSC_THR_0 |  | 20 |  | mV | HSC_THR = 0x0 | DS p.13, Table 18. Load hard short circuit (HSC) protection with integrated 10-bit ADC, VHSC_THR_0 |  |
| Hard short circuit protection threshold | VHSC_THR_1 |  | 23 |  | mV | HSC_THR = 0x1 | DS p.13, Table 18. Load hard short circuit (HSC) protection with integrated 10-bit ADC, VHSC_THR_1 |  |
| Hard short circuit protection threshold | VHSC_THR_2 |  | 26.4 |  | mV | HSC_THR = 0x2 | DS p.13, Table 18. Load hard short circuit (HSC) protection with integrated 10-bit ADC, VHSC_THR_2 |  |
| Hard short circuit protection threshold | VHSC_THR_3 |  | 30.3 |  | mV | HSC_THR = 0x3 | DS p.13, Table 18. Load hard short circuit (HSC) protection with integrated 10-bit ADC, VHSC_THR_3 |  |
| Hard short circuit protection threshold | VHSC_THR_4 |  | 34.8 |  | mV | HSC_THR = 0x4 | DS p.13, Table 18. Load hard short circuit (HSC) protection with integrated 10-bit ADC, VHSC_THR_4 |  |
| Hard short circuit protection threshold | VHSC_THR_5 |  | 40 |  | mV | HSC_THR = 0x5 | DS p.13, Table 18. Load hard short circuit (HSC) protection with integrated 10-bit ADC, VHSC_THR_5 |  |
| Hard short circuit protection threshold | VHSC_THR_6 |  | 45.9 |  | mV | HSC_THR = 0x6 | DS p.13, Table 18. Load hard short circuit (HSC) protection with integrated 10-bit ADC, VHSC_THR_6 |  |
| Hard short circuit protection threshold | VHSC_THR_7 |  | 52.8 |  | mV | HSC_THR = 0x7 | DS p.13, Table 18. Load hard short circuit (HSC) protection with integrated 10-bit ADC, VHSC_THR_7 |  |
| Hard short circuit protection threshold | VHSC_THR_8 |  | 60.6 |  | mV | HSC_THR = 0x8 | DS p.13, Table 18. Load hard short circuit (HSC) protection with integrated 10-bit ADC, VHSC_THR_8 |  |
| Hard short circuit protection threshold | VHSC_THR_9 |  | 69.6 |  | mV | HSC_THR = 0x9 | DS p.13, Table 18. Load hard short circuit (HSC) protection with integrated 10-bit ADC, VHSC_THR_9 |  |
| Hard short circuit protection threshold | VHSC_THR_10 |  | 80 |  | mV | HSC_THR = 0xA | DS p.13, Table 18. Load hard short circuit (HSC) protection with integrated 10-bit ADC, VHSC_THR_10 |  |
| Hard short circuit protection threshold | VHSC_THR_11 |  | 91.9 |  | mV | HSC_THR = 0xB | DS p.13, Table 18. Load hard short circuit (HSC) protection with integrated 10-bit ADC, VHSC_THR_11 |  |
| Hard short circuit protection threshold | VHSC_THR_12 |  | 105.6 |  | mV | HSC_THR = 0xC | DS p.13, Table 18. Load hard short circuit (HSC) protection with integrated 10-bit ADC, VHSC_THR_12 |  |
| Hard short circuit protection threshold | VHSC_THR_13 |  | 121.3 |  | mV | HSC_THR = 0xD | DS p.13, Table 18. Load hard short circuit (HSC) protection with integrated 10-bit ADC, VHSC_THR_13 |  |
| Hard short circuit protection threshold | VHSC_THR_14 |  | 139.3 |  | mV | HSC_THR = 0xE | DS p.14, Table 18. Load hard short circuit (HSC) protection with integrated 10-bit ADC, VHSC_THR_14 |  |
| Hard short circuit protection threshold | VHSC_THR_15 |  | 160 |  | mV | HSC_THR = 0xF | DS p.14, Table 18. Load hard short circuit (HSC) protection with integrated 10-bit ADC, VHSC_THR_15 |  |
| Hard short circuit protection threshold accuracy | VHSC_THR_ACC | -5 |  | 5 | % |  | DS p.14, Table 18. Load hard short circuit (HSC) protection with integrated 10-bit ADC, VHSC_THR_ACC |  |
| Hard short circuit protection delay time | VHSC_DELAY |  |  | 5 | us | CGATE = 30 nF, T = 105 degC (single stated temperature) | DS p.14, Table 18. Load hard short circuit (HSC) protection with integrated 10-bit ADC, VHSC_DELAY |  |
| Hard short circuit protection ADC full range resolution (code) | VHSC_ADC_CONV | 0 |  | 1023 |  | Note: DS note 1: VSENSE[mV] = VHSC_ADC[9:0] * 160 / 1024 (calc.vsense_from_hsc_code). DS note 2: IOUT[A] = VSENSE[mV] / RSENSE[mohm]. | DS p.14, Table 18. Load hard short circuit (HSC) protection with integrated 10-bit ADC, VHSC_ADC_CONV (1)(2) |  |
| Hard short circuit ADC sample rate | VHSC_ADC_RATE |  | 900 |  | kHz | Note: Printed kSample/s; stored as kHz. | DS p.14, Table 18. Load hard short circuit (HSC) protection with integrated 10-bit ADC, VHSC_ADC_RATE |  |
| Overcurrent protection threshold range (32 steps, OVC_THR field in CR#2) | VOVC_THR_RANGE | 6 |  | 90 | mV |  | DS p.14, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_RANGE |  |
| Overcurrent protection threshold | VOVC_THR_0 |  | 6 |  | mV | OVC_THR = 0x00 | DS p.14, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_0 |  |
| Overcurrent protection threshold | VOVC_THR_1 |  | 7.2 |  | mV | OVC_THR = 0x01 | DS p.14, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_1 |  |
| Overcurrent protection threshold | VOVC_THR_2 |  | 8.7 |  | mV | OVC_THR = 0x02 | DS p.14, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_2 |  |
| Overcurrent protection threshold | VOVC_THR_3 |  | 10.4 |  | mV | OVC_THR = 0x03 | DS p.14, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_3 |  |
| Overcurrent protection threshold | VOVC_THR_4 |  | 11.8 |  | mV | OVC_THR = 0x04 | DS p.14, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_4 |  |
| Overcurrent protection threshold | VOVC_THR_5 |  | 13 |  | mV | OVC_THR = 0x05 | DS p.14, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_5 |  |
| Overcurrent protection threshold | VOVC_THR_6 |  | 13.8 |  | mV | OVC_THR = 0x06 | DS p.14, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_6 |  |
| Overcurrent protection threshold | VOVC_THR_7 |  | 14.8 |  | mV | OVC_THR = 0x07 | DS p.14, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_7 |  |
| Overcurrent protection threshold | VOVC_THR_8 |  | 15.8 |  | mV | OVC_THR = 0x08 | DS p.14, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_8 |  |
| Overcurrent protection threshold | VOVC_THR_9 |  | 16.8 |  | mV | OVC_THR = 0x09 | DS p.14, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_9 |  |
| Overcurrent protection threshold | VOVC_THR_10 |  | 17.9 |  | mV | OVC_THR = 0x0A | DS p.14, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_10 |  |
| Overcurrent protection threshold | VOVC_THR_11 |  | 19.1 |  | mV | OVC_THR = 0x0B | DS p.14, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_11 |  |
| Overcurrent protection threshold | VOVC_THR_12 |  | 20.4 |  | mV | OVC_THR = 0x0C | DS p.14, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_12 |  |
| Overcurrent protection threshold | VOVC_THR_13 |  | 21.8 |  | mV | OVC_THR = 0x0D | DS p.14, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_13 |  |
| Overcurrent protection threshold | VOVC_THR_14 |  | 23.3 |  | mV | OVC_THR = 0x0E | DS p.14, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_14 |  |
| Overcurrent protection threshold | VOVC_THR_15 |  | 24.8 |  | mV | OVC_THR = 0x0F | DS p.14, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_15 |  |
| Overcurrent protection threshold | VOVC_THR_16 |  | 26.5 |  | mV | OVC_THR = 0x10 | DS p.14, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_16 |  |
| Overcurrent protection threshold | VOVC_THR_17 |  | 28.2 |  | mV | OVC_THR = 0x11 | DS p.14, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_17 |  |
| Overcurrent protection threshold | VOVC_THR_18 |  | 30.1 |  | mV | OVC_THR = 0x12 | DS p.14, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_18 |  |
| Overcurrent protection threshold | VOVC_THR_19 |  | 32.2 |  | mV | OVC_THR = 0x13 | DS p.14, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_19 |  |
| Overcurrent protection threshold | VOVC_THR_20 |  | 34.3 |  | mV | OVC_THR = 0x14 | DS p.14, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_20 |  |
| Overcurrent protection threshold | VOVC_THR_21 |  | 36.6 |  | mV | OVC_THR = 0x15 | DS p.14, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_21 |  |
| Overcurrent protection threshold | VOVC_THR_22 |  | 39.1 |  | mV | OVC_THR = 0x16 | DS p.14, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_22 |  |
| Overcurrent protection threshold | VOVC_THR_23 |  | 41.7 |  | mV | OVC_THR = 0x17 | DS p.14, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_23 |  |
| Overcurrent protection threshold | VOVC_THR_24 |  | 44.5 |  | mV | OVC_THR = 0x18 | DS p.15, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_24 |  |
| Overcurrent protection threshold | VOVC_THR_25 |  | 47.5 |  | mV | OVC_THR = 0x19 | DS p.15, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_25 |  |
| Overcurrent protection threshold | VOVC_THR_26 |  | 50.6 |  | mV | OVC_THR = 0x1A | DS p.15, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_26 |  |
| Overcurrent protection threshold | VOVC_THR_27 |  | 54 |  | mV | OVC_THR = 0x1B | DS p.15, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_27 |  |
| Overcurrent protection threshold | VOVC_THR_28 |  | 61.3 |  | mV | OVC_THR = 0x1C | DS p.15, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_28 |  |
| Overcurrent protection threshold | VOVC_THR_29 |  | 69.5 |  | mV | OVC_THR = 0x1D | DS p.15, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_29 |  |
| Overcurrent protection threshold | VOVC_THR_30 |  | 78.8 |  | mV | OVC_THR = 0x1E | DS p.15, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_30 |  |
| Overcurrent protection threshold | VOVC_THR_31 |  | 89.3 |  | mV | OVC_THR = 0x1F | DS p.15, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, VOVC_THR_31 |  |
| Overcurrent protection threshold accuracy, settings 0x00 to 0x02 | VOVC_THR_ACC | -12 |  | 12 | % | OVC_THR = 0x00 to 0x02 (merged cell) | DS p.14, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, accuracy (merged rows 0x00 to 0x02) |  |
| Overcurrent protection threshold accuracy, settings 0x03 to 0x0C | VOVC_THR_ACC | -7 |  | 7 | % | OVC_THR = 0x03 to 0x0C (merged cell) | DS p.14, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, accuracy (merged rows 0x03 to 0x0C) |  |
| Overcurrent protection threshold accuracy, settings 0x0D to 0x1F | VOVC_THR_ACC | -5 |  | 5 | % | OVC_THR = 0x0D to 0x1F (merged cells) | DS p.14, Table 19 (rows 0x0D to 0x17) and DS p.15, Table 19 (rows 0x18 to 0x1F). Load overcurrent (OVC) protection with integrated 10-bits ADC, accuracy |  |
| I-t tolerance on time step (y axis) | i-time_tol_t |  | (t-10%) - 32 (min) ; (t+10%) + 32 (max), t in us |  | us | Note: Printed as formulas in words (the tolerance depends on the time step t): stored as text. | DS p.15, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, i-time_tol_t |  |
| I2t algorithm sampling time | tI_SAMPLING | -10 % | 61 | +10 % | us | Note: Min -10 % / Max +10 % printed as offsets: stored as tol_pct. | DS p.15, Table 19. Load overcurrent (OVC) protection with integrated 10-bits ADC, tI_SAMPLING |  |
| VOUT ADC full range resolution (code) | VOUT_ADC_CONV | 0 |  | 1023 |  | Note: DS note 1: VOUT[mV] = VOUT_ADC[11:2] * 1.2 * 51 / 1024 (printed mV; the numbers give volts, see calc.vout_from_adc_code). | DS p.15, Table 20. Output voltage (VOUT) sensing with integrated 10-bits ADC, VOUT_ADC_CONV (1) |  |
| VOUT ADC sample rate | VOUT_ADC_RATE |  | 4.9 |  | kHz | Note: Printed kSample/s; stored as kHz. | DS p.15, Table 20. Output voltage (VOUT) sensing with integrated 10-bits ADC, VOUT_ADC_RATE |  |
| Output voltage accuracy | VOUT_ACC_1V | -18 |  | 18 | % | 1 V < VOUT <= 2 V | DS p.15, Table 20. Output voltage (VOUT) sensing with integrated 10-bits ADC, VOUT_ACC_1V |  |
| Output voltage accuracy | VOUT_ACC_2V | -9 |  | 9 | % | 2 V < VOUT <= 3 V | DS p.15, Table 20. Output voltage (VOUT) sensing with integrated 10-bits ADC, VOUT_ACC_2V |  |
| Output voltage accuracy | VOUT_ACC_3V | -6 |  | 6 | % | 3 V < VOUT <= 12 V | DS p.15, Table 20. Output voltage (VOUT) sensing with integrated 10-bits ADC, VOUT_ACC_3V |  |
| Output voltage accuracy | VOUT_ACC_12V | -3 |  | 3 | % | 12 V < VOUT <= 60 V | DS p.15, Table 20. Output voltage (VOUT) sensing with integrated 10-bits ADC, VOUT_ACC_12V |  |
| NTC input voltage full-scale range | VNTC_FSR | -1.2 (rel. ISNS_N) |  | 0 (rel. ISNS_N) | V | Note: Printed min VISNS_N - 1.2 V and max VISNS_N: both relative to ISNS_N (min_ref / max_ref = ISNS_N). | DS p.16, Table 21. External MOSFET thermal shutdown via NTC input, VNTC_FSR |  |
| NTC_M output voltage | VNTC_M |  | VISNS_N - 1.2 |  | V | Note: Printed typ VISNS_N - 1.2 V: a formula, stored as text. | DS p.16, Table 21. External MOSFET thermal shutdown via NTC input, VNTC_M |  |
| NTC input voltage threshold accuracy | VNTC_ACC | -5 |  | 5 | mV |  | DS p.16, Table 21. External MOSFET thermal shutdown via NTC input, VNTC_ACC |  |
| NTC input voltage threshold (external MOSFET thermal shutdown) | VNTC_THR_0 |  | 110.92 |  | mV | NTC_THR = 0x0 | DS p.16, Table 21. External MOSFET thermal shutdown via NTC input, VNTC_THR_0 |  |
| NTC input voltage threshold (external MOSFET thermal shutdown) | VNTC_THR_1 |  | 98.76 |  | mV | NTC_THR = 0x1 | DS p.16, Table 21. External MOSFET thermal shutdown via NTC input, VNTC_THR_1 |  |
| NTC input voltage threshold (external MOSFET thermal shutdown) | VNTC_THR_2 |  | 88.07 |  | mV | NTC_THR = 0x2 | DS p.16, Table 21. External MOSFET thermal shutdown via NTC input, VNTC_THR_2 |  |
| NTC input voltage threshold (external MOSFET thermal shutdown) | VNTC_THR_3 |  | 78.66 |  | mV | NTC_THR = 0x3 | DS p.16, Table 21. External MOSFET thermal shutdown via NTC input, VNTC_THR_3 |  |
| NTC input voltage threshold (external MOSFET thermal shutdown) | VNTC_THR_4 |  | 70.38 |  | mV | NTC_THR = 0x4 | DS p.16, Table 21. External MOSFET thermal shutdown via NTC input, VNTC_THR_4 |  |
| NTC input voltage threshold (external MOSFET thermal shutdown) | VNTC_THR_5 |  | 63.08 |  | mV | NTC_THR = 0x5 | DS p.16, Table 21. External MOSFET thermal shutdown via NTC input, VNTC_THR_5 |  |
| NTC input voltage threshold (external MOSFET thermal shutdown) | VNTC_THR_6 |  | 56.64 |  | mV | NTC_THR = 0x6 | DS p.16, Table 21. External MOSFET thermal shutdown via NTC input, VNTC_THR_6 |  |
| NTC input voltage threshold (external MOSFET thermal shutdown) | VNTC_THR_7 |  | 50.95 |  | mV | NTC_THR = 0x7 | DS p.16, Table 21. External MOSFET thermal shutdown via NTC input, VNTC_THR_7 |  |
| NTC input voltage threshold (external MOSFET thermal shutdown) | VNTC_THR_8 |  | 45.92 |  | mV | NTC_THR = 0x8 | DS p.16, Table 21. External MOSFET thermal shutdown via NTC input, VNTC_THR_8 |  |
| NTC input voltage threshold (external MOSFET thermal shutdown) | VNTC_THR_9 |  | 41.46 |  | mV | NTC_THR = 0x9 | DS p.16, Table 21. External MOSFET thermal shutdown via NTC input, VNTC_THR_9 |  |
| NTC input voltage threshold (external MOSFET thermal shutdown) | VNTC_THR_10 |  | 37.5 |  | mV | NTC_THR = 0xA | DS p.16, Table 21. External MOSFET thermal shutdown via NTC input, VNTC_THR_10 |  |
| NTC input voltage threshold (external MOSFET thermal shutdown) | VNTC_THR_11 |  | 37.5 |  | mV | NTC_THR = 0xB | DS p.16, Table 21. External MOSFET thermal shutdown via NTC input, VNTC_THR_11 |  |
| NTC input voltage threshold (external MOSFET thermal shutdown) | VNTC_THR_12 |  | 37.5 |  | mV | NTC_THR = 0xC | DS p.16, Table 21. External MOSFET thermal shutdown via NTC input, VNTC_THR_12 |  |
| NTC input voltage threshold (external MOSFET thermal shutdown) | VNTC_THR_13 |  | 37.5 |  | mV | NTC_THR = 0xD | DS p.16, Table 21. External MOSFET thermal shutdown via NTC input, VNTC_THR_13 |  |
| NTC input voltage threshold (external MOSFET thermal shutdown) | VNTC_THR_14 |  | 37.5 |  | mV | NTC_THR = 0xE | DS p.16, Table 21. External MOSFET thermal shutdown via NTC input, VNTC_THR_14 |  |
| NTC input voltage threshold (external MOSFET thermal shutdown) | VNTC_THR_15 |  | 37.5 |  | mV | NTC_THR = 0xF | DS p.16, Table 21. External MOSFET thermal shutdown via NTC input, VNTC_THR_15 |  |
| External MOSFET thermal shutdown deglitch time | VNTC_DEGLITCH | 10 |  | 500 | us |  | DS p.16, Table 21. External MOSFET thermal shutdown via NTC input, VNTC_DEGLITCH |  |
| External MOSFET thermal shutdown ADC full range resolution (code) | VNTC_ADC_CONV | 0 |  | 1023 |  | Note: DS note 1: VNTC[V] = VNTC_ADC[11:2] * 1.2 / 1024 (calc.vntc_from_adc_code). RNTC[ohm] = VNTC * RT_REF / (VBG - VNTC) (calc.r_ntc). | DS p.16, Table 21. External MOSFET thermal shutdown via NTC input, VNTC_ADC_CONV (1) |  |
| External MOSFET thermal shutdown ADC sample rate | VNTC_ADC_RATE |  | 4.9 |  | kHz | Note: Printed kSample/s; stored as kHz. | DS p.16, Table 21. External MOSFET thermal shutdown via NTC input, VNTC_ADC_RATE |  |
| NTC bridge reference voltage VBG | VBG |  | 1.2 |  | V | Note: Typical only (no MIN or MAX printed). Used by calc.r_ntc via INPUTS vbg.typ. | DS p.17, Figure 4. NTC bridge, note VBG = 1.2 V (also DS p.39: VBG = VISNS_N - VNTC_M, typ. 1.2 V) |  |
| NTC bridge reference resistor RT_REF (recommended) | RT_REF | -1 % | 12 | +1 % | kohm | recommended value, Figure 4 note and Table 64 Note: Recommended external value, not a device parameter. Its +/-1 % is stored as tol_pct. | DS p.17, Figure 4. NTC bridge, note RT_REF = 12 kohm +/-1 %; DS p.68, Table 64. Components value, RT_REF |  |
| Bypass switch VDS saturation protection threshold | VDS_BYPASS_SAT | 1 |  | 2 | V |  | DS p.17, Table 22. P-channel bypass, VDS_BYPASS_SAT |  |
| Bypass switch saturation current | IBYPASS_SAT | 297 | 572 | 900 | mA | VS - VOUT = VDS_BYPASS_SAT | DS p.17, Table 22. P-channel bypass, IBYPASS_SAT |  |
| Bypass switch on state resistance | RDS(ON)_BYPASS | 1 | 2 | 4.5 | ohm |  | DS p.17, Table 22. P-channel bypass, RDS(ON)_BYPASS |  |
| HS_GATE turn-on time on bypass-shutting off | tON_BYPOFF |  |  | 100 | us |  | DS p.17, Table 22. P-channel bypass, tON_BYPOFF |  |
| Bypass switch saturation diagnostic de-glitch filtering time | tBYPASS_SAT_DEGLITCH | -20 % | 5 | +20 % | us | Standby state Note: Min -20 % / Max +20 % printed as offsets: stored as tol_pct. | DS p.17, Table 22. P-channel bypass, tBYPASS_SAT_DEGLITCH |  |
| Self-test execution time | tS_T_ACTIVE | -10 % | 5 | +10 % | us | Note: Min -10 % / Max +10 % printed as offsets: stored as tol_pct. | DS p.17, Table 23. Self-test timing, tS_T_ACTIVE |  |
| Self-test wait time | tS_T_WAIT | -10 % | 5 | +10 % | us | Note: Min -10 % / Max +10 % printed as offsets: stored as tol_pct. | DS p.17, Table 23. Self-test timing, tS_T_WAIT |  |
| Entering threshold of current sense undervoltage (CS_UV = 0b to 1b in SR#1) | CS_UV | 2.78 | 2.87 | 3 | V | VISNS_P decreasing | DS p.41, Table 33. Current sense undervoltage thresholds, CS_UV (entering) |  |
| Exiting threshold of current sense undervoltage (CS_UV = 1b to 0b in SR#1) | CS_UV | 2.98 | 3.08 | 3.18 | V | VISNS_P increasing | DS p.41, Table 33. Current sense undervoltage thresholds, CS_UV (exiting) |  |
| Current sense fault deglitch filtering | tCS_UV_DEGLITCH | -10 % | 10 | +10 % | us | HS_GATE = on Note: Min -10 % / Max +10 % printed as offsets: stored as tol_pct. | DS p.41, Table 33. Current sense undervoltage thresholds, tCS_UV_DEGLITCH |  |
| Current sense fault clear autoretry time | tCS_UV_RETRY_TIME | -5 % | 100 | +5 % | us | CS_UV_RETRY_T = 00b Note: Min -5 % / Max +5 % printed as offsets: stored as tol_pct. | DS p.41, Table 33. Current sense undervoltage thresholds, tCS_UV_RETRY_TIME, CS_UV_RETRY_T = 00b |  |
| Current sense fault clear autoretry time | tCS_UV_RETRY_TIME | -5 % | 250 | +5 % | us | CS_UV_RETRY_T = 01b Note: Min -5 % / Max +5 % printed as offsets: stored as tol_pct. | DS p.41, Table 33. Current sense undervoltage thresholds, tCS_UV_RETRY_TIME, CS_UV_RETRY_T = 01b |  |
| Current sense fault clear autoretry time | tCS_UV_RETRY_TIME | -5 % | 500 | +5 % | us | CS_UV_RETRY_T = 10b Note: Min -5 % / Max +5 % printed as offsets: stored as tol_pct. | DS p.41, Table 33. Current sense undervoltage thresholds, tCS_UV_RETRY_TIME, CS_UV_RETRY_T = 10b |  |
| Current sense fault clear autoretry time | tCS_UV_RETRY_TIME | -5 % | 1000 | +5 % | us | CS_UV_RETRY_T = 11b Note: Min -5 % / Max +5 % printed as offsets: stored as tol_pct. | DS p.41, Table 33. Current sense undervoltage thresholds, tCS_UV_RETRY_TIME, CS_UV_RETRY_T = 11b |  |

## Parameters: thermal

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Thermal resistance, junction-to-ambient, JEDEC JESD 51-2 (-7), two-layer PCB | RthJA |  | 56 |  | degC/W | JEDEC JESD 51-2 (-7); device on two-layer 2s0p PCB with 2 cm2 heatsink copper trace (DS note 1) Note: Printed as Typ. value only; stored as typ, not a bound. Board: FR4, 1.6 mm, 129x60 mm, footprint 3.5x3.5 mm (DS p.6 note). | DS p.6, Table 3. Thermal data, RthJA (JESD 51-2, -7) |  |
| Thermal resistance, junction-to-ambient, JEDEC JESD 51-2 (-5), four-layer PCB | RthJA |  | 26 |  | degC/W | JEDEC JESD 51-2 (-5); device on four-layer 2s2p PCB (DS note 2) Note: Printed as Typ. value only; stored as typ, not a bound. | DS p.6, Table 3. Thermal data, RthJA (JESD 51-2, -5) |  |

## Limits of this data

Rows by scope: 25C 3, full 258, na 36 (25C rows hold only at 25 degC). Curve (graph) rows: 0. Text rows: 5. Temperatures are junction (TJ): analyse with TJ = TA + P x RthJA; no ambient range is printed.

## Zener checks

Generated wrapper: `VNF1248F.zen` (`python3 -m lib.zen`). abs_max and rec_op rows are errors (abs_max x derate); 25C and partial rows are waivable warnings; a checked net with no voltage is UNVERIFIED.

| Param | Name | Checked against | Not checked / reason |
|---|---|---|---|
| abs_vs | VS pin DC voltage | UNCHECKED | covered by vs_op |
| abs_ignd | GND pin reverse DC current | UNCHECKED | current rating, not a voltage; owner: module |
| abs_vspi | VSPI pin DC voltage | UNCHECKED | covered by vspi_op |
| abs_v3v3 | V3V3 pin DC voltage | UNCHECKED | part-driven: output of the internal 3.3 V LDO (Table 1, pin 12); owner: module |
| abs_ext_ldo | EXT_LDO pin DC voltage | pins EXT_LDO |  |
| abs_spi_in | SPI input pins DC voltage (CSN, SDI, SCK) | pins CSN, SDI, SCK |  |
| abs_sdo | SDO pin DC voltage | UNCHECKED | SDO is driven by the part; owner: module |
| abs_sdo_vspi | SDO pin DC voltage relative to VSPI | UNCHECKED | SDO is driven by the part; owner: module |
| abs_hwlo | HWLO pin DC voltage | pins HWLO |  |
| abs_diag | DIAG pin DC voltage | pins DIAG |  |
| abs_diag_v3v3 | VDIAG pin DC voltage relative to V3V3 | pins DIAG |  |
| abs_idiag | DIAG pin DC current | UNCHECKED | current rating, internally limited; part-driven pin; owner: module |
| abs_isns | ISNS_P and ISNS_N pins voltage | pins ISNS_P, ISNS_N |  |
| abs_dvisns | Differential DC input voltage (VSENSE = VISNS_P - VISNS_N) | pins ISNS_P |  |
| abs_hs_gate | HS_GATE pin DC voltage | UNCHECKED | part-driven: gate drive output; owner: module |
| abs_out | OUT pin DC voltage | UNCHECKED | OUT is the external MOSFET source, set by external parts; owner: module |
| abs_ntc | NTC, NTC_M pins DC voltage | UNCHECKED | NTC bridge nodes: voltage set by the external NTC network and the internal bridge (DS p.17 Figure 4); owner: module |
| abs_vcp | CP pin DC voltage | UNCHECKED | part-driven: charge pump output; owner: module |
| abs_vcp1p_cp2p | CP1P, CP2P pins DC voltage | UNCHECKED | part-driven: charge pump flying-capacitor nodes; owner: module |
| abs_vcp1m_cp2m | CP1M, CP2M pins DC voltage | UNCHECKED | part-driven: charge pump flying-capacitor nodes; owner: module |
| abs_vdin | DIN pin DC voltage | pins DIN |  |
| abs_outst | OUTST pin DC voltage | pins OUTST |  |
| abs_outst_v3v3 | VOUTST pin DC voltage relative to V3V3 | pins OUTST |  |
| esd_hbm_2000 | ESD, JEDEC 22A-114F (HBM), general pins | UNCHECKED | owner: assembly |
| esd_hbm_4000 | ESD, JEDEC 22A-114F (HBM), VS, OUT, DIN only | UNCHECKED | owner: assembly |
| esd_cdm_500 | ESD, CDM-AEC-Q100-011, all pins except corners | UNCHECKED | owner: assembly |
| esd_cdm_750 | ESD, CDM-AEC-Q100-011, corner pins | UNCHECKED | owner: assembly |
| tj_abs | Junction operating temperature | UNCHECKED | TJ rating; needs dissipation; owner: module |
| tstg | Storage temperature | UNCHECKED | owner: assembly |
| nftp | Maximum number of FTP NVM programming cycles | UNCHECKED | NVM programming endurance count, not a voltage or temperature; owner: module |
| vs_op | Operating supply voltage | pins VS |  |
| vs_ext | Extended operating supply voltage | UNCHECKED | 100 ms transient limit; a DC check cannot model duration; owner: module |
| vspi_op | SPI pin operating range | pins VSPI |  |

## Equations

### `vsense_from_csa_code`

```
VSENSE [mV] = VSENSE_ADC[14:2] * 160 / 8192. DS p.13, Table 17, test condition of VSENSE_ADC_CONV:
VSENSE_ADC[14:2] = min(VSENSE / 160 * 8192, 8191), solved for VSENSE.
DS CONFLICT, resolved: Table 17 footnote 1 prints "* 160 / 1024", a misprint copied from the 10-bit HSC ADC
(DS p.14, Table 18 footnote 1, field [9:0]). The field [14:2] is 13 bits (0 to 8191), and only /8192 gives the
160 mV full scale of VSENSE_FSR (DS p.11, Table 15); /1024 would give 1.28 V. Table > footnote (CLAUDE.md).
code: VSENSE_ADC[14:2] field value, 0 to 8191. Returns: VSENSE, V. INPUTS: none.
```

Inputs:


### `i_load_from_vsense`

```
IOUT [A] = VSENSE [mV] / RSENSE [ohm]. DS p.13, Table 17 footnote 2 (current sense ADC) and DS p.14, Table 18
footnote 2 (HSC ADC, IOUT [A] = VSENSE [mV] / RSENSE [mohm], same ratio). vsense: V. rsense: ohm. Returns: A.
The DS prints mV / ohm = mA; in SI, V / ohm = A. INPUTS: none (vsense is an ADC result, rsense a design choice).
```

Inputs:


### `vsense_from_hsc_code`

```
VSENSE [mV] = VHSC_ADC[9:0] * 160 / 1024. DS p.14, Table 18, footnote 1 (10-bit HSC ADC; 1023 gives 160 mV full scale).
code: VHSC_ADC[9:0] field value, 0 to 1023. Returns: VSENSE, V. INPUTS: none.
```

Inputs:


### `vds_from_adc_code`

```
VDS [V] = VDS_ADC[22:13] * 2.4 / 1280 - 0.05. DS p.13, Table 16, footnote 2 (external MOSFET VDS fast ADC).
code: VDS_ADC[22:13] field value, 0 to 1023. Returns: VDS, V. INPUTS: none.
Check: code 0 gives -0.05 V (DS p.13 min); code 1023 gives 1.868 V (DS prints 1.87 V, rounded).
```

Inputs:


### `vout_from_adc_code`

```
VOUT = VOUT_ADC[11:2] * 1.2 * 51 / 1024. DS p.15, Table 20, footnote 1. The DS prints the result as [mV], but
the numbers give volts (full scale 61.1 V for code 1023; Table 20 accuracy is specified up to 60 V), so the result is
in V. OPEN ITEM: unit label in the DS. code: VOUT_ADC[11:2] field value, 0 to 1023. Returns: VOUT, V. INPUTS: none.
```

Inputs:


### `tj_from_adc_code`

```
TJ [degC] = TJ_ADC[22:13] / 3 - 72. DS p.11, Table 14, footnote 1 (junction temperature ADC, 1/3 degC per code).
code: TJ_ADC[22:13] field value, 0 to 1023 (TJ -72 to 269 degC over the code range). Returns: degC. INPUTS: none.
```

Inputs:


### `vntc_from_adc_code`

```
VNTC [V] = VNTC_ADC[11:2] * 1.2 / 1024. DS p.16, Table 21, footnote 1 (external MOSFET NTC ADC).
code: VNTC_ADC[11:2] field value, 0 to 1023. Returns: VNTC, V. INPUTS: none.
```

Inputs:


### `r_ntc`

```
RNTC [ohm] = VNTC * RT_REF / (VBG - VNTC). DS p.16, Table 21, footnote 1 (second line); inverse of DS p.39 Eq. (1).
RT_REF = 12 kohm +/-1 % (DS p.17, Figure 4 note; DS p.68, Table 64). VBG = 1.2 V typ (DS p.17 Figure 4 note; DS p.39).
vntc: V (from vntc_from_adc_code or vntc_from_rntc). rt_ref: ohm (design choice). vbg: V.
Returns: ohm. INPUTS: vbg -> vbg.typ (typical only).
```

Inputs:

- `vbg` -> `vbg.typ` (typ 1.2 V)

### `i_threshold`

```
I = VTHR / RSENSE. DS p.18, eFuse function text: load hard short circuit threshold IHSC = VHSC_THR_x / RSENSE and
eFuse nominal current INOM = VOVC_THR_x / RSENSE (the same ratio). v_thr: threshold, V (one stored setting, e.g.
vhsc_thr_12 typ 105.6 mV or vovc_thr_16 typ 26.5 mV; pass the typical or a bound of that setting). rsense: ohm.
Returns: A. INPUTS: none (the setting is chosen by the caller).
```

Inputs:


### `i_trip`

```
Not a DS equation: I_TRIP = VTHR * (1 + acc) / RSENSE. Combines the DS p.18 threshold ratio (i_threshold) with the
printed threshold accuracy of the chosen setting. acc is a fraction (-0.05 = -5 %), chosen by the setting's range:
- HSC (VHSC_THR_x, DS p.13-14 Table 18): acc -> vhsc_thr_acc, -5 % to +5 % for all 16 codes.
- OVC (VOVC_THR_x, DS p.14-15 Table 19), by decimal code n: n = 0 to 2 -> vovc_acc_0_2 (-12 % to +12 %);
  n = 3 to 12 -> vovc_acc_3_12 (-7 % to +7 %); n = 13 to 31 -> vovc_acc_13_31 (-5 % to +5 %).
  The group boundaries are the merged cells of Table 19 (0x00-0x02, 0x03-0x0C, 0x0D-0x17 on p.14; 0x18-0x1F on p.15).
v_thr: setting value, V (design choice from the Table 18 or 19 typ). rsense: ohm (design choice). Returns: A.
Worst case: wca min at acc = lo, max at acc = hi. INPUTS: default acc -> vhsc_thr_acc (HSC). For OVC, the caller
passes the group key (e.g. vovc_acc_13_31) as the acc argument's Param.
```

Inputs:

- `acc` -> `vhsc_thr_acc` (min -5 max 5 %)

### `vntc_from_rntc`

```
VNTC [V] = VBG * RNTC / (RT_REF + RNTC). DS p.39, 11.3 External MOSFET overtemperature shutdown, Equation (1).
Forward form of the Table 21 footnote 1 (r_ntc is its inverse). VBG = (VISNS_N - VNTC_M), typ 1.2 V (DS p.39).
rntc: ohm (NTC resistance; DS p.17 Figure 4 note: B57232V5103F360, 10 kohm at 25 degC). rt_ref: ohm (12 kohm +/-1 %,
DS p.17 Figure 4 note). vbg: V. Returns: V. INPUTS: vbg -> vbg.typ (typical only).
```

Inputs:

- `vbg` -> `vbg.typ` (typ 1.2 V)

### `i_time_tol_min`

```
Minimum of the I-t time step tolerance: (t - 10 %) - 32 = 0.9 * t - 32 us. DS p.15, Table 19, row i-time_tol_t
(Min column, printed '(t-10%) - 32', unit us). The 32 is read in us from the printed unit column.
t: time step, s. Returns: s. INPUTS: none (t is the step being evaluated).
```

Inputs:


### `i_time_tol_max`

```
Maximum of the I-t time step tolerance: (t + 10 %) + 32 = 1.1 * t + 32 us. DS p.15, Table 19, row i-time_tol_t
(Max column, printed '(t+10%) + 32', unit us). Same unit reading as i_time_tol_min. t: s. Returns: s. INPUTS: none.
```

Inputs:



## Examples

| Call | Computed | Expected | Rel. tol | Result | Cite |
|---|---|---|---|---|---|
| vsense_from_csa_code(code=8191) | 0.15998 | 0.16 | 0.0002 | pass | DS p.11, Table 15, VSENSE_FSR; DS p.13, Table 17 test condition |
| vsense_from_hsc_code(code=1023) | 0.159844 | 0.16 | 0.002 | pass | DS p.13, Table 18, VHSC_THR_RANGE max 160 mV at the top code |
| vds_from_adc_code(code=0) | -0.05 | -0.05 | 0.001 | pass | DS p.13, Table 16, VDS_ADC_CONV min -0.05 V |
| vds_from_adc_code(code=1023) | 1.86812 | 1.87 | 0.002 | pass | DS p.13, Table 16, VDS_ADC_CONV max 1.87 V (rounded in the DS) |
| i_threshold(v_thr=0.0265, rsense=0.001) | 26.5 | 26.5 | 0.001 | pass | DS p.18, eFuse text: VOVC_THR_16 = 26.5 mV with RSENSE = 1 mohm (DS p.68, Table 64 value) gives 26.5 A |
| i_threshold(v_thr=0.1056, rsense=0.001) | 105.6 | 105.6 | 0.001 | pass | DS p.18, eFuse text: VHSC_THR_12 = 105.60 mV with RSENSE = 1 mohm gives 105.6 A |
| i_trip(v_thr=0.1056, acc=0, rsense=0.001) | 105.6 | 105.6 | 0.001 | pass | DS p.18 example VHSC_THR_12 = 105.60 mV with 0 % accuracy, RSENSE = 1 mohm |
| i_trip(v_thr=0.16, acc=-0.05, rsense=0.001) | 152 | 152 | 0.001 | pass | DS p.13-14, Table 18, VHSC_THR_15 = 160 mV at the -5 % accuracy corner (160 * 0.95 = 152 A at 1 mohm) |
| i_trip(v_thr=0.0265, acc=-0.05, rsense=0.001) | 25.175 | 25.175 | 0.001 | pass | DS p.15, Table 19, VOVC_THR_16 = 26.5 mV in the 13-31 group (-5 %), 1 mohm: 26.5 * 0.95 = 25.175 A |
| vntc_from_rntc(rntc=10000, rt_ref=12000, vbg=1.2) | 0.545455 | 0.545455 | 1e-09 | pass | DS p.39, Equation (1) with RNTC 10 kohm, RT_REF 12 kohm, VBG 1.2 V (DS p.17 Figure 4 notes) |
| r_ntc(vntc=0.545455, rt_ref=12000, vbg=1.2) | 10000 | 10000 | 1e-09 | pass | Inverse of DS p.39 Eq. (1) (Table 21 footnote 1): round trip back to RNTC = 10 kohm |
