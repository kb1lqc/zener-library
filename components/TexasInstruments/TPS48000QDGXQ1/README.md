<!-- GENERATED - do not edit. Run: python3 -m lib.readme -->

# TPS48000QDGXQ1

## Datasheet review

[![Human page-image review: 0/93 human](https://img.shields.io/badge/human%20review-0%2F93%20human-lightgrey)](../../../docs/spec/datasheet-review.md)

Human page-image review: 0/93; cross-model audits: 47; manufacturer-export stamps: 0; legacy/unclassified: 0. Text checks are not verification. `lib.check` validates stamp format, not that review occurred.

## Part

- **mpn**: TPS48000QDGXRQ1
- **alternates**: []
- **manufacturer**: Texas Instruments
- **description**: 100 V automotive low-IQ high-side driver with reverse polarity, short-circuit protection and diagnostics, VSSOP-19 (DGX), TPS4800-Q1 data sheet
- **category**: high_side_driver
- **package**: VSSOP-19 (DGX), 5.1 x 3.0 mm nominal (DS p.1 Package Information)
- **datasheet_url**: https://www.ti.com/lit/ds/symlink/tps4800-q1.pdf
- **datasheet_file**: docs/datasheets/tps4800-q1.pdf
- **datasheet_rev**: SLUSEZ1B Rev. B
- **datasheet_date**: 2026-03
- **temp_grade**: TJ -40 to 150 degC; ambient -40 to 125 degC (grade 1)
- **kicad_symbol**: TPS48000QDGXQ1.kicad_sym
- **kicad_footprint**: TPS48000QDGXQ1.kicad_mod
- **step**: TPS48000QDGXQ1.step

## Pins

| Pin | Name | Type | Function | Cite |
|---|---|---|---|---|
| 1 | EN/UVLO | input | Condensed from DS Table 4-1: EN/UVLO input. A voltage higher than 1 V enables normal operation. Below 0.3 V shuts down the device; optionally connect to the input supply through a resistive divider to set the UVLO. Floating: internal pull-down keeps the device in shutdown. | DS p.3, Table 4-1 Pin Functions, EN/UVLO |
| 2 | OV | input | Condensed from DS Table 4-1: Adjustable overvoltage threshold input. Resistor ladder from input supply, OV to GND. Must be connected to GND when not used (internal pull-down holds PU to BST when floating). | DS p.3, Table 4-1 Pin Functions, OV |
| 3 | INP | input | Condensed from DS Table 4-1: Input signal for external discharge FET control. CMOS compatible input referenced to GND that sets the state of PD and PU. Internal weak pull-down to GND. | DS p.3, Table 4-1 Pin Functions, INP |
| 4 | FLT_GD | open_collector | Condensed from DS Table 4-1: Open drain fault output for gate drive UVLO. Asserts low when gate drive across PD to SRC is above 7 V (typ.). | DS p.3, Table 4-1 Pin Functions, FLT_GD |
| 5 | FLT | open_collector | Condensed from DS Table 4-1: Open drain fault output. Asserts low during short circuit fault, input UVLO, overvoltage and during SCP comparator diagnosis. Connect to GND if FLT feature not desired. | DS p.3, Table 4-1 Pin Functions, FLT |
| 6 | GND | power_in | Condensed from DS Table 4-1: Connect GND to system ground. (DS type G, ground) | DS p.3, Table 4-1 Pin Functions, GND |
| 7 | CS_SEL | input | Condensed from DS Table 4-1: Current sense select input. Connect to ground for high side current sense. Drive above 1.58 V for low side current sensing. Internal weak pull-down to GND. | DS p.3, Table 4-1 Pin Functions, CS_SEL |
| 8 | ISCP | passive | Condensed from DS Table 4-1: Short circuit detection setting. A resistor across ISCP to GND sets the short circuit current comparator threshold (external bias on ISCP is the alternative, DS p.17). Connect ISCP and TMR to GND if short-circuit protection is not desired. DS type I; passive because an external resistor or bias sets the node. | DS p.3, Table 4-1 Pin Functions, ISCP |
| 9 | TMR | passive | Condensed from DS Table 4-1: Fault timer input. A capacitor across TMR to GND sets the times for fault turn-off. Leave open for fastest setting. DS type I; passive because the external capacitor sets the node. | DS p.3, Table 4-1 Pin Functions, TMR |
| 10 | SCP_TEST | input | Condensed from DS Table 4-1: Internal short circuit comparator (SCP) diagnosis input. Driven low to high with INP high checks the SCP comparator; FLT goes low and PD is pulled to SRC if the comparator is functional. Connect to GND if not used. Internal weak pull-down to GND. | DS p.3, Table 4-1 Pin Functions, SCP_TEST |
| 11 | N.C | no_connect | Condensed from DS Table 4-1: No connect. | DS p.4, Table 4-1 Pin Functions, N.C (pin 11) |
| 12 | BST | passive | Condensed from DS Table 4-1: High side bootstrapped supply. External capacitor (minimum > Qg(tot) of the external FET) between BST and SRC. DS type O; a charge-pump capacitor node, so passive for schematic capture. | DS p.4, Table 4-1 Pin Functions, BST |
| 13 | SRC | passive | Condensed from DS Table 4-1: Source connection of the external FET. DS type O; the external FET source node, so passive for schematic capture. | DS p.4, Table 4-1 Pin Functions, SRC |
| 14 | PD | passive | Condensed from DS Table 4-1: High current gate driver pull-down. Pulls down to SRC. Tie directly to the gate of the external high side MOSFET for fastest turn-off. DS type O; passive because PU and PD are normally tied together (an output-output pair fails KiCad ERC). | DS p.4, Table 4-1 Pin Functions, PD |
| 15 | PU | passive | Condensed from DS Table 4-1: High current gate driver pull-up. Pulls up to BST. Connect to PD for maximum transition speed. A resistor from PU to the gate controls turn-on inrush. DS type O; passive because PU and PD are normally tied together (an output-output pair fails KiCad ERC). | DS p.4, Table 4-1 Pin Functions, PU |
| 17 | CS- | input | Condensed from DS Table 4-1: Current sense negative input. | DS p.4, Table 4-1 Pin Functions, CS- |
| 18 | CS+ | input | Condensed from DS Table 4-1: Current sense positive input. | DS p.4, Table 4-1 Pin Functions, CS+ |
| 19 | N.C | no_connect | Condensed from DS Table 4-1: No connect. | DS p.4, Table 4-1 Pin Functions, N.C (pin 19) |
| 20 | VS | power_in | Condensed from DS Table 4-1: Supply pin of the controller (DS type P, power). | DS p.4, Table 4-1 Pin Functions, VS |

## Parameters: abs_max

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| VS, CS+, CS- voltage to GND | VS, CS+, CS- | -65 (rel. GND) |  | 100 (rel. GND) | V | Absolute maximum, referenced to GND Note: Reference GND from the row title ('to GND'). Pin-pair rows (CS+ to CS-) are a separate row below. | DS p.5, 5.1 Absolute Maximum Ratings, Input Pins, VS, CS+, CS- to GND | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| SRC voltage to GND | SRC | -65 (rel. GND) |  | 100 (rel. GND) | V | Absolute maximum, referenced to GND Note: Reference GND from the row title ('to GND'). | DS p.5, 5.1 Absolute Maximum Ratings, Input Pins, SRC to GND | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| PU, PD, BST voltage to SRC | PU, PD, BST | -0.3 (rel. SRC) |  | 19 (rel. SRC) | V | Absolute maximum, referenced to SRC Note: Reference SRC from the row title ('to SRC'). The DS prints the same -0.3 V to 19 V for each of the three pins. | DS p.5, 5.1 Absolute Maximum Ratings, Input Pins, PU, PD, BST to SRC | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| ISCP, TMR, SCP_TEST voltage to GND | ISCP, TMR, SCP_TEST | -0.3 (rel. GND) |  | 5.5 (rel. GND) | V | Absolute maximum, referenced to GND Note: Reference GND from the row title ('to GND'). SCP_TEST is checked; ISCP and TMR are not (below). | DS p.5, 5.1 Absolute Maximum Ratings, Input Pins, ISCP, TMR, SCP_TEST to GND | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| EN/UVLO, OV, INP, CS_SEL voltage (V(VS) > 0 V) | EN/UVLO, OV, INP, CS_SEL | -1 (rel. GND) |  | 70 (rel. GND) | V | V(VS) > 0 V Note: Reference GND from the row title (the DS prints the range to GND only for VS > 0). The second row below is the VS <= 0 V case. The DS has no rec-op row for OV (EN/UVLO, INP, CS_SEL have 0-65 V, rec_en_inp_cs_sel); OV usually shares their divider, so 65 V is the practical module bound. | DS p.5, 5.1 Absolute Maximum Ratings, Input Pins, EN/UVLO, OV, INP, CS_SEL, V(VS) > 0 V | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| EN/UVLO, OV, INP, CS_SEL voltage (V(VS) <= 0 V) | EN/UVLO, OV, INP, CS_SEL | 0 (rel. VS) |  | 70 (rel. VS) | V | V(VS) <= 0 V Note: Printed as V(VS) (MIN) and (70 + V(VS)) (MAX): min = 0 V and max = 70 V, both relative to VS (min_ref/max_ref = VS). Rail-relative row (Defaults table). | DS p.5, 5.1 Absolute Maximum Ratings, Input Pins, EN/UVLO, OV, INP, CS_SEL, V(VS) <= 0 V (V(VS) to (70 + V(VS))) |  |
| CS+ to CS- voltage | CS+ - CS- | -1 (rel. CS-) |  | 100 (rel. CS-) | V | Absolute maximum, pin pair Note: Pin-pair row: the second pin (CS-) is the reference (Defaults table). Checked on the CS+ net. Zener checks each net range independently: declare CS+ and CS- with a correlated (tight) tolerance, or the real mV drop shows as a large worst-case difference (open item). | DS p.5, 5.1 Absolute Maximum Ratings, Input Pins, CS+ to CS- | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| FLT, FLT_GD voltage to GND | FLT, FLT_GD | -1 (rel. GND) |  | 20 (rel. GND) | V | Absolute maximum, referenced to GND Note: Reference GND from the row title. Open drain: the high level is set by the circuit's pull-up rail, so both pins are checked. | DS p.5, 5.1 Absolute Maximum Ratings, Input Pins, FLT, FLT_GD to GND | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| FLT sink current | I(FLT) |  |  | 10 | mA | Note: Printed MAX only (no MIN column value). A sink-current rating, not a voltage. | DS p.5, 5.1 Absolute Maximum Ratings, Sink current, I(FLT) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| CS+, CS- current, 1 ms | I(CS+), I(CS-) | -100 |  | 100 | mA | 1 ms Note: Printed MIN -100 and MAX 100 mA. Stored numerically (min <= max). Current rating, not a voltage. | DS p.5, 5.1 Absolute Maximum Ratings, Sink current, I(CS+), I(CS-), 1 msec |  |
| PU, PD, G2, BST voltage to GND | PU, PD, G2, BST | -65 (rel. GND) |  | 112 (rel. GND) | V | Absolute maximum, referenced to GND Note: The DS prints G2 in this row; G2 is not in the DGX pin table (Table 4-1). Stored as printed; G2 is not a pin of this package. | DS p.5, 5.1 Absolute Maximum Ratings, Output Pins, PU, PD, G2, BST to GND | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Operating junction temperature, Tj (absolute maximum) | Tj | -40 |  | 150 | degC | Note: Junction temperature, not ambient. TJ = TA + P x RthJA (RthJA DS p.6, 92.3 degC/W). The module must check the dissipation. | DS p.5, 5.1 Absolute Maximum Ratings, Operating junction temperature, Tj | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Storage temperature, Tstg | Tstg | -55 |  | 150 | degC |  | DS p.5, 5.1 Absolute Maximum Ratings, Storage temperature, Tstg | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| ESD, human body model | V(ESD) HBM | -2000 |  | 2000 | V | HBM per AEC Q100-002 Note: Printed +/-2000 V; min = -2000, max = 2000 (Defaults table, +/- limit). | DS p.5, 5.2 ESD Ratings, Human body model (HBM), per AEC Q100-002 | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| ESD, charged device model, corner pins | V(ESD) CDM | -750 |  | 750 | V | CDM per AEC Q100-011, corner pins EN/UVLO, VS, SCP_TEST Note: Printed +/-750 V; min = -750, max = 750. | DS p.5, 5.2 ESD Ratings, Charged device model (CDM), Corner pins (EN/UVLO, VS, SCP_TEST) |  |
| ESD, charged device model, other pins | V(ESD) CDM | -500 |  | 500 | V | CDM per AEC Q100-011, other pins Note: Printed +/-500 V; min = -500, max = 500. | DS p.5, 5.2 ESD Ratings, Charged device model (CDM), Other pins |  |

## Parameters: rec_op

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| VS voltage to GND, operating | VS | 3.5 (rel. GND) |  | 95 (rel. GND) | V | Recommended operating, to GND Note: Same span as the electrical row vs_op (DS p.6, 5.5 Supply voltage, VS 3.5 to 95 V). Checked here once. | DS p.5, 5.3 Recommended Operating Conditions, Input Pins, VS to GND | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| VS minimum for short-circuit protection | VS | 4 (rel. GND) |  |  | V | Minimum voltage on the VS pin for short circuit protection Note: Printed MIN only (no MAX). Reference GND assumed as for the VS row above; the DS gives no reference in this row. Checked against the VS net (minimum only). scope = partial (waivable warning): the row applies only when short-circuit protection is used; below 4 V the part still operates per rec_vs (3.5 V). A module that disables SCP (CS+, CS-, VS tied, ISCP and TMR to GND, DS p.4 Table 4-1) waives it with waive_rec_vs_scp_min. | DS p.5, 5.3 Recommended Operating Conditions, Input Pins, Minimum voltage on VS pin for Short Circuit Protection | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| External bias voltage on ISCP, maximum |  |  |  | 3 (rel. GND) | V | Only when ISCP is externally biased instead of using RISCP Note: Design-text limit, not in the 5.3 table; stricter than the 5.5 V abs max (abs_iscp_tmr_scp_test). | DS p.17, 7.3.3 Short-Circuit Protection, text under the V(SCP_BIAS) equation: 'External bias voltage on ISCP pin should not exceed 3V.' |  |
| EN/UVLO, INP, CS_SEL voltage to GND, operating | EN/UVLO, INP, CS_SEL | 0 (rel. GND) |  | 65 (rel. GND) | V | Recommended operating, to GND Note: Reference GND from the row title. | DS p.5, 5.3 Recommended Operating Conditions, Input Pins, EN/UVLO, INP, CS_SEL to GND | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| FLT voltage to GND, operating | FLT | 0 (rel. GND) |  | 15 (rel. GND) | V | Recommended operating, to GND Note: Open-drain output of the part; the pull-up rail is set by the module. | DS p.5, 5.3 Recommended Operating Conditions, Output Pins, FLT to GND | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| External capacitor, VS and SRC to GND | C | 22 |  |  | nF | External capacitor, VS, SRC to GND Note: Printed MIN 22 nF only. | DS p.5, 5.3 Recommended Operating Conditions, External Capacitor, VS, SRC to GND |  |
| External capacitor, BST to SRC | C | 0.1 |  |  | uF | External capacitor, BST to SRC Note: Printed MIN 0.1 uF only. Charge-pump capacitor (see also DS p.17-18 for the sizing equations). | DS p.5, 5.3 Recommended Operating Conditions, External Capacitor, BST to SRC | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Operating junction temperature, Tj (recommended) | Tj | -40 |  | 150 | degC | Recommended operating Note: Junction temperature. TJ = TA + P x RthJA; the module must check the dissipation. | DS p.5, 5.3 Recommended Operating Conditions, Tj Operating Junction temperature |  |
| Operating ambient temperature range, grade 1 |  | -40 |  | 125 | degC | Device temperature grade 1, ambient operating temperature range Note: From a Features bullet, not a table row. The only ambient range printed; the grade is AEC-Q100 grade 1. Checked through the ambient config. | DS p.1, Features, AEC-Q100 bullet 'Device temperature grade 1: -40 degC to +125 degC ambient operating temperature range' | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |

## Parameters: electrical

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Operating input voltage, VS | VS | 3.5 |  | 95 | V | TJ = -40 to +150 degC Note: Same span as rec_vs (DS p.5). Listed for completeness; the Zener check is on rec_vs. | DS p.6, 5.5 Electrical Characteristics, Supply Voltage, VS |  |
| Input supply POR threshold, rising | V(S_PORR) | 1.7 | 2.5 | 3.34 | V |  | DS p.6, 5.5 Electrical Characteristics, Supply Voltage, V(S_PORR) |  |
| Input supply POR threshold, falling | V(S_PORF) | 1.7 | 2.4 | 3.16 | V |  | DS p.6, 5.5 Electrical Characteristics, Supply Voltage, V(S_PORF) |  |
| Total system quiescent current, operating | I(GND) |  | 46 | 56 | uA | V(EN/UVLO) = 2 V, TJ = -40 to +150 degC Note: Printed TYP 46, MAX 56 uA; no MIN. Quiescent current cannot be negative: the printed max is the worst case. | DS p.6, 5.5 Electrical Characteristics, Supply Voltage, I(GND), V(EN/UVLO) = 2 V | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Total system quiescent current, operating, TJ -40 to +85 degC | I(GND) |  |  | 53 | uA | V(EN/UVLO) = 2 V, -40 degC <= TJ <= +85 degC. Partial range; use i_gnd_full over the full range. Note: Printed MAX only. Partial scope (Defaults table: row covers part of the grade range). | DS p.6, 5.5 Electrical Characteristics, Supply Voltage, I(GND), V(EN/UVLO) = 2 V, -40 degC <= TJ <= +85 degC |  |
| Shutdown supply current, I(GND) | I(SHDN) |  | 1 | 4.3 | uA | V(EN/UVLO) = 0 V, V(SRC) = 0 V Note: Printed TYP 1, MAX 4.3 uA; no MIN. | DS p.6, 5.5 Electrical Characteristics, Supply Voltage, I(SHDN), V(EN/UVLO) = 0 V, V(SRC) = 0 V | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| VS leakage current during reverse polarity | I(REV) | 15 | 22.1 | 38 | uA | 0 V <= V(VS) <= -65 V | DS p.6, 5.5 Electrical Characteristics, Supply Voltage, I(REV), I(VS) leakage current during reverse polarity |  |
| UVLO threshold voltage, rising (EN/UVLO) | V(UVLOR) | 1.17 | 1.23 | 1.29 | V |  | DS p.6, 5.5 Electrical Characteristics, Enable, UVLO, V(UVLOR) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| UVLO threshold voltage, falling (EN/UVLO) | V(UVLOF) | 1.09 | 1.14 | 1.19 | V |  | DS p.6, 5.5 Electrical Characteristics, Enable, UVLO, V(UVLOF) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Enable threshold voltage, rising | V(ENR) |  |  | 1 | V | Note: Printed MAX only. | DS p.6, 5.5 Electrical Characteristics, Enable, V(ENR) |  |
| Enable threshold voltage, falling | V(ENF) | 0.3 |  |  | V | Note: Printed MIN only. | DS p.6, 5.5 Electrical Characteristics, Enable, V(ENF) |  |
| Enable input leakage current, EN/UVLO | I(EN/UVLO) |  | 174 | 490 | nA | V(EN/UVLO) = 70 V Note: Printed TYP 174, MAX 490 nA; no MIN. | DS p.6, 5.5 Electrical Characteristics, Enable, I(EN/UVLO), V(EN/UVLO) = 70 V | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| SCP test mode rising threshold | V(SCP_TEST_H) |  |  | 2 | V | Note: Printed MAX only. | DS p.6, 5.5 Electrical Characteristics, Enable, V(SCP_TEST_H) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| SCP test mode falling threshold | V(SCP_TEST_L) | 0.8 |  |  | V | Note: Printed MIN only. | DS p.6, 5.5 Electrical Characteristics, Enable, V(SCP_TEST_L) |  |
| SCP_TEST input leakage current | I(SCP_TEST) |  | 90 | 730 | nA | Note: Printed TYP 90, MAX 730 nA; no MIN. | DS p.6, 5.5 Electrical Characteristics, Enable, I(SCP_TEST) |  |
| Overvoltage threshold input, rising (OV) | V(OVR) | 1.17 | 1.23 | 1.28 | V | Note: The design example text (DS p.24) uses V(OVR) = 1.225 V; that value is not in this row (see the decision log). | DS p.6, 5.5 Electrical Characteristics, Overvoltage Protection, V(OVR) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Overvoltage threshold input, falling (OV) | V(OVF) | 1.08 | 1.14 | 1.19 | V |  | DS p.6, 5.5 Electrical Characteristics, Overvoltage Protection, V(OVF) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| OV input leakage current | I(OV) |  | 86 | 205 | nA | Note: Printed TYP 86, MAX 205 nA; no MIN. | DS p.6, 5.5 Electrical Characteristics, Overvoltage Protection, I(OV) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Charge pump supply current | I(BST) | 100 | 345 | 555 | uA | V(BST-SRC) = 10 V, V(EN/UVLO) = 2 V Note: Used by the bootstrap delay equation (DS p.14 eq. 1; DS p.14 text quotes 345 uA). | DS p.6, 5.5 Electrical Characteristics, Charge Pump, I(BST) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| V(BST-SRC) UVLO threshold voltage, rising | V(BST_UVLOR) | 7.19 | 9 | 10.81 | V | V(EN/UVLO) = 2 V Note: DS p.14 text: 'V(BST_UVLOR) = 10.81 V (max)' is used in eq. 1. | DS p.6, 5.5 Electrical Characteristics, Charge Pump, V(BST_UVLOR) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| V(BST-SRC) UVLO threshold voltage, falling | V(BST_UVLOF) | 6.54 | 8.2 | 9.64 | V | V(EN/UVLO) = 2 V | DS p.6, 5.5 Electrical Characteristics, Charge Pump, V(BST_UVLOF) |  |
| Charge pump turn ON voltage | V(BST-SRC_ON) | 8.24 | 10.3 | 12.46 | V | V(EN/UVLO) = 2 V | DS p.6, 5.5 Electrical Characteristics, Charge Pump, V(BST-SRC_ON) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Charge pump turn OFF voltage | V(BST-SRC_OFF) | 9.34 | 11.6 | 13.86 | V | V(EN/UVLO) = 2 V | DS p.6, 5.5 Electrical Characteristics, Charge Pump, V(BST-SRC_OFF) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Charge pump voltage at VS = 3.5 V | V(BST-SRC) | 8.9 | 10.5 | 11.82 | V | V(VS) = 3.5 V, V(EN/UVLO) = 2 V Note: Test condition V(VS) = 3.5 V stated in the row; the other charge pump rows are at the table header VS = 48 V. | DS p.6, 5.5 Electrical Characteristics, Charge Pump, V(BST-SRC) Charge Pump Voltage at V(VS) = 3.5 V |  |
| Peak source current, PU | I(PU) |  | 1.69 |  | A | Note: Printed TYP 1.69 A only (no MIN or MAX). Features bullet (DS p.1) says '1.69A source'. Used with the 2 A sink. | DS p.7, 5.5 Electrical Characteristics, Gate Driver Outputs (G1PU, G1PD), I(PU) |  |
| Peak sink current, PD | I(PD) |  | 2 |  | A | Note: Printed TYP 2 A only. Features bullet (DS p.1) says '2A sink'. | DS p.7, 5.5 Electrical Characteristics, Gate Driver Outputs (G1PU, G1PD), I(PD) |  |
| VGS good threshold | V(G_GOOD) | 5.32 | 7 | 8.48 | V |  | DS p.7, 5.5 Electrical Characteristics, Gate Driver Outputs, V(G_GOOD) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| SCP input bias current | I(ISCP) | 8.22 | 10 | 12.51 | uA | Note: The ISCP bias current row. The equations use the printed 2 uA constant (DS p.17 eq. 5); see the decision log. | DS p.7, 5.5 Electrical Characteristics, Short Circuit Protection, I(ISCP) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| SCP threshold, R(ISCP) = 140.5 kohm | V(SCP) | 283 | 300 | 318 | mV | R(ISCP) = 140.5 kohm | DS p.7, 5.5 Electrical Characteristics, Short Circuit Protection, V(SCP), R(ISCP) = 140.5 kohm | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| SCP threshold, R(ISCP) = 28 kohm | V(SCP) | 58.4 | 75 | 91.6 | mV | R(ISCP) = 28 kohm | DS p.7, 5.5 Electrical Characteristics, Short Circuit Protection, V(SCP), R(ISCP) = 28 kohm | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| SCP threshold, R(ISCP) = 10.5 kohm | V(SCP) | 31.1 | 40 | 48.9 | mV | R(ISCP) = 10.5 kohm | DS p.7, 5.5 Electrical Characteristics, Short Circuit Protection, V(SCP), R(ISCP) = 10.5 kohm | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| SCP threshold, R(ISCP) = 500 ohm | V(SCP) | 14.9 | 20 | 25.2 | mV | R(ISCP) = 500 ohm | DS p.7, 5.5 Electrical Characteristics, Short Circuit Protection, V(SCP), R(ISCP) = 500 ohm | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| SCP threshold, R(ISCP) open | V(SCP) | 468 | 560 | 651 | mV | R(ISCP) = open | DS p.7, 5.5 Electrical Characteristics, Short Circuit Protection, V(SCP), R(ISCP) = Open |  |
| SCP threshold with external bias, V(ISCP) = 3 V | V(SCP) | 470 | 563 | 642 | mV | External bias on ISCP pin, V(ISCP) = 3 V | DS p.7, 5.5 Electrical Characteristics, Short Circuit Protection, V(SCP) with external bias on ISCP, V(ISCP) = 3 V |  |
| SCP threshold with external bias, V(ISCP) = 1.405 V | V(SCP) | 279 | 300 | 319 | mV | External bias on ISCP pin, V(ISCP) = 1.405 V | DS p.7, 5.5 Electrical Characteristics, Short Circuit Protection, V(SCP) with external bias on ISCP, V(ISCP) = 1.405 V |  |
| SCP threshold with external bias, V(ISCP) = 280 mV | V(SCP) | 67 | 75 | 83 | mV | External bias on ISCP pin, V(ISCP) = 280 mV | DS p.7, 5.5 Electrical Characteristics, Short Circuit Protection, V(SCP) with external bias on ISCP, V(ISCP) = 280 mV |  |
| SCP threshold with external bias, V(ISCP) = 105 mV | V(SCP) | 33 | 40 | 47 | mV | External bias on ISCP pin, V(ISCP) = 105 mV | DS p.7, 5.5 Electrical Characteristics, Short Circuit Protection, V(SCP) with external bias on ISCP, V(ISCP) = 105 mV |  |
| TMR source current, circuit breaker (charge) pull-up | I(TMR_SRC_CB) | 65 | 87 | 106 | uA | Note: DS p.19 eq. 8 and DS p.25 design eq. 11 use I(TMR_SRC_CB). Typ 87 uA is the value eq. 11 prints (see the decision log). | DS p.7, 5.5 Electrical Characteristics, Delay Timer (TMR), I(TMR_SRC_CB) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| TMR source current, fault retry pull-up | I(TMR_SRC_FLT) | 1.33 | 2.73 | 3.87 | uA |  | DS p.7, 5.5 Electrical Characteristics, Delay Timer (TMR), I(TMR_SRC_FLT) |  |
| TMR sink current | I(TMR_SNK) | 2.14 | 2.8 | 3.43 | uA |  | DS p.7, 5.5 Electrical Characteristics, Delay Timer (TMR), I(TMR_SNK) |  |
| TMR input clamp level | V(TMR_SC) | 0.87 | 1.1 | 1.26 | V |  | DS p.7, 5.5 Electrical Characteristics, Delay Timer (TMR), V(TMR_SC) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| TMR input low level | V(TMR_LOW) | 0.14 | 0.21 | 0.26 | V |  | DS p.7, 5.5 Electrical Characteristics, Delay Timer (TMR), V(TMR_LOW) |  |
| Number of TMR charge-discharge cycles (auto-retry) | N(A-R Count) |  | 32 |  |  | Note: Printed TYP 32 only (a count, unitless). | DS p.7, 5.5 Electrical Characteristics, Delay Timer (TMR), N(A-R Count) |  |
| FLT, FLT_GD pull-down resistance | R(FLT), R(FLT_GD) | 52 | 85 | 107 | ohm |  | DS p.7, 5.5 Electrical Characteristics, Input Control, FLT, FLT_GD Pull-down resistance, R(FLT), R(FLT_GD) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| FLT, FLT_GD input leakage current | I(FLT), I(FLT_GD) |  |  | 410 | nA | 0 V <= V(FLT) <= 20 V Note: Printed MAX only (410 nA). | DS p.7, 5.5 Electrical Characteristics, Input Control, I(FLT), I(FLT_GD), 0 V <= V(FLT) <= 20 V |  |
| INP input logic high level | V(INP_H) |  |  | 2 | V | Note: Printed MAX only. | DS p.7, 5.5 Electrical Characteristics, Input Control, V(INP_H) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| INP input logic low level | V(INP_L) | 0.8 |  |  | V | Note: Printed MIN only. | DS p.7, 5.5 Electrical Characteristics, Input Control, V(INP_L) | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| INP input leakage current | I(INP) |  | 89 | 210 | nA | Note: Printed TYP 89, MAX 210 nA; no MIN. | DS p.7, 5.5 Electrical Characteristics, Input Control, I(INP) |  |
| CS_SEL threshold for low side sensing | V(CS_SEL_H) | 1.25 |  | 1.58 | V | Note: Printed row label is 'CS_SEL threshold for low side sensing' (the H row). Table 4-1 uses the same 1.58 V level. | DS p.7, 5.5 Electrical Characteristics, Input Control, V(CS_SEL_H), CS_SEL threshold for low side sensing |  |
| CS_SEL threshold for high side sensing | V(CS_SEL_L) | 0.66 |  | 1.14 | V |  | DS p.7, 5.5 Electrical Characteristics, Input Control, V(CS_SEL_L), CS_SEL threshold for high side sensing |  |
| CS_SEL input leakage current | I(CS_SEL) | 10 | 88.8 | 210 | nA |  | DS p.7, 5.5 Electrical Characteristics, Input Control, I(CS_SEL) |  |
| INP turn-ON propagation delay (to PU) | tPU(INP_H) | 0.32 |  | 1.68 | us | INP rising to PU rising, CL = 47 nF Note: Printed MIN 0.32, MAX 1.68 us; no TYP. | DS p.7, 5.6 Switching Characteristics, tPU(INP_H), CL = 47 nF | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| INP turn-OFF propagation delay (to PD) | tPD(INP_L) |  | 0.36 | 1.05 | us | INP falling to PD falling, CL = 47 nF Note: Printed TYP 0.36, MAX 1.05 us; no MIN. | DS p.7, 5.6 Switching Characteristics, tPD(INP_L), CL = 47 nF |  |
| EN turn-OFF propagation delay (to PD) | tPD(EN_OFF) | 1.68 | 4.6 | 6.52 | us | EN falling to PD falling, CL = 47 nF | DS p.7, 5.6 Switching Characteristics, tPD(EN_OFF), CL = 47 nF | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| UVLO turn-OFF propagation delay (to PD and FLT) | tPD(UVLO_OFF) | 2.22 | 4.8 | 6.58 | us | UVLO falling to PD falling and FLT falling, CL = 47 nF | DS p.7, 5.6 Switching Characteristics, tPD(UVLO_OFF), CL = 47 nF |  |
| OV turn-OFF propagation delay (to PD and FLT) | tPD(OV_OFF) |  | 4.5 | 5.55 | us | OV rising to PD falling and FLT falling, CL = 47 nF Note: Printed TYP 4.5, MAX 5.55 us; no MIN. | DS p.7, 5.6 Switching Characteristics, tPD(OV_OFF), CL = 47 nF |  |
| Hard short-circuit protection propagation delay | tSC |  |  | 4 | us | V(CS+ - CS-) rising to V(SCP) to PD falling, CL = 47 nF, C(TMR) = open Note: Printed MAX only. | DS p.7, 5.6 Switching Characteristics, tSC, C(TMR) = Open | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Short-circuit protection propagation delay, power-up with output short | tSC_PUS |  |  | 10 | us | C(TMR) = open Note: Printed MAX only. | DS p.8, 5.6 Switching Characteristics (continued), tSC_PUS, CTMR = Open |  |
| FLT assertion delay during short circuit | tPD(FLT_SC) |  | 10.5 | 15 | us | V(CS+ - CS-) rising to V(SCP) to FLT falling, C(TMR) = open Note: Printed TYP 10.5, MAX 15 us; no MIN. | DS p.8, 5.6 Switching Characteristics (continued), tPD(FLT_SC), C(TMR) = Open |  |
| ISCP pulse current frequency | FISCP |  | 1.18 |  | kHz | Note: Printed TYP 1.18 kHz only. | DS p.8, 5.6 Switching Characteristics (continued), FISCP |  |
| FLT_GD assertion delay during gate drive UVLO | tPD(FLT_GD) |  | 120 |  | us | V(PD-SRC) rising, V(BST_UVLOR), to FLT_GD falling Note: Printed TYP 120 us only. Assertion row. | DS p.8, 5.6 Switching Characteristics (continued), tPD(FLT_GD) assertion, V(PD-SRC) rising | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| FLT_GD de-assertion delay during gate drive UVLO | tPD(FLT_GD) |  | 127 |  | us | V(PD-SRC) falling, V(BST_UVLOR), to FLT_GD rising Note: Printed TYP 127 us only. De-assertion row. | DS p.8, 5.6 Switching Characteristics (continued), tPD(FLT_GD) de-assertion, V(PD-SRC) falling |  |
| TMR internal pull-up current (equation text) | ITMR |  | 80 |  | uA | Stated in the text of the CTMR equation section Note: Typ-only value from the text, not an Electrical Characteristics row; the table gives I(TMR_SRC_CB) 87 uA typ (DS p.7). Eq. 6 uses 80 uA as printed; design eq. 11 uses 87 uA. Conflict is recorded in the decision log. Stored as typ (never a bound). The DS states no temperature for it (scope na). Not used by INPUTS. | DS p.18, 7.3.3.1 Short-Circuit Protection With Auto-Retry, 'ITMR is internal pull-up current of 80 uA' (text under eq. 6) |  |

## Parameters: thermal

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Junction-to-ambient thermal resistance, RthJA | RthJA |  | 92.3 |  | degC/W | DGX, 19 pins Note: Single printed value; typ only (not a bound). JEDEC board condition not printed in this table. | DS p.6, 5.4 Thermal Information, RthJA, DGX 19 PINS | cross-model page-image audit: sonnet-audit 2026-11-18 blind page-image reading, cross-model (diet-work/audit/AUDIT.md) |
| Junction-to-case (top) thermal resistance | RthJC(top) |  | 28.6 |  | degC/W | DGX, 19 pins Note: Single printed value; typ only. | DS p.6, 5.4 Thermal Information, RthJC(top), DGX 19 PINS |  |
| Junction-to-board thermal resistance | RthJB |  | 47.5 |  | degC/W | DGX, 19 pins Note: Single printed value; typ only. | DS p.6, 5.4 Thermal Information, RthJB, DGX 19 PINS |  |
| Junction-to-top characterization parameter | PsiJT |  | 0.6 |  | degC/W | DGX, 19 pins Note: Single printed value; typ only. | DS p.6, 5.4 Thermal Information, PsiJT, DGX 19 PINS |  |
| Junction-to-board characterization parameter | PsiJB |  | 47.2 |  | degC/W | DGX, 19 pins Note: Single printed value; typ only. | DS p.6, 5.4 Thermal Information, PsiJB, DGX 19 PINS |  |

## Limits of this data

Rows by scope: full 61, na 30, partial 2 (25C rows hold only at 25 degC). Curve (graph) rows: 0. Text rows: 0.

## Zener checks

Generated wrapper: `TPS48000QDGXQ1.zen` (`python3 -m lib.zen`). abs_max and rec_op rows are errors (abs_max x derate); 25C and partial rows are waivable warnings; a checked net with no voltage is UNVERIFIED.

| Param | Name | Checked against | Not checked / reason |
|---|---|---|---|
| abs_vs_cs_gnd | VS, CS+, CS- voltage to GND | pins VS, CS+, CS- |  |
| abs_src_gnd | SRC voltage to GND | UNCHECKED | SRC is the external FET source node; its voltage is set by the external MOSFET and load; owner: module |
| abs_gate_bst_src | PU, PD, BST voltage to SRC | UNCHECKED | PU, PD and BST are driven by the part (gate driver and charge pump); owner: module |
| abs_iscp_tmr_scp_test | ISCP, TMR, SCP_TEST voltage to GND | pins SCP_TEST | ISCP and TMR voltages are set by the internal sources and the external RISCP / CTMR components (an external ISCP bias, if used, must stay <= 3 V: rec_iscp_bias); owner: module |
| abs_input_vs_pos | EN/UVLO, OV, INP, CS_SEL voltage (V(VS) > 0 V) | pins EN/UVLO, OV, INP, CS_SEL |  |
| abs_input_vs_neg | EN/UVLO, OV, INP, CS_SEL voltage (V(VS) <= 0 V) | UNCHECKED | Reverse-polarity condition (V(VS) <= 0 V) is not the normal operating point; the module must keep the input pins within V(VS)..V(VS)+70 V; owner: module |
| abs_cs_pair | CS+ to CS- voltage | pins CS+ |  |
| abs_flt_gnd | FLT, FLT_GD voltage to GND | pins FLT, FLT_GD |  |
| abs_i_flt_sink | FLT sink current | UNCHECKED | Current rating, not a voltage check; module must keep V(pull-up) / R(pull-up) < 10 mA; owner: module |
| abs_i_cs_1ms | CS+, CS- current, 1 ms | UNCHECKED | Current rating over 1 ms, not a voltage check; owner: module |
| abs_gate_out_gnd | PU, PD, G2, BST voltage to GND | UNCHECKED | PU, PD and BST are driven by the part (see abs_gate_bst_src); owner: module |
| tj_abs | Operating junction temperature, Tj (absolute maximum) | UNCHECKED | TJ rating; needs dissipation; owner: module |
| tstg_abs | Storage temperature, Tstg | UNCHECKED | Storage temperature; owner: assembly |
| esd_hbm | ESD, human body model | UNCHECKED | ESD rating; owner: assembly |
| esd_cdm_corner | ESD, charged device model, corner pins | UNCHECKED | ESD rating; owner: assembly |
| esd_cdm_other | ESD, charged device model, other pins | UNCHECKED | ESD rating; owner: assembly |
| rec_vs | VS voltage to GND, operating | pins VS |  |
| rec_vs_scp_min | VS minimum for short-circuit protection | pins VS |  |
| rec_iscp_bias | External bias voltage on ISCP, maximum | UNCHECKED | applies only to an externally biased ISCP; with RISCP the part sets the pin voltage; owner: module |
| rec_en_inp_cs_sel | EN/UVLO, INP, CS_SEL voltage to GND, operating | pins EN/UVLO, INP, CS_SEL |  |
| rec_flt | FLT voltage to GND, operating | pins FLT |  |
| rec_cap_vs_src | External capacitor, VS and SRC to GND | UNCHECKED | Capacitance requirement, not a voltage check; owner: module |
| rec_cap_bst_src | External capacitor, BST to SRC | UNCHECKED | Capacitance requirement, not a voltage check; owner: module |
| rec_tj | Operating junction temperature, Tj (recommended) | UNCHECKED | TJ rating; needs dissipation; owner: module |
| ta_grade_1 | Operating ambient temperature range, grade 1 | board ambient |  |

## Equations

### `t_drv_en`

```
TDRV_EN = CBST x V(BST_UVLOR) / 345 uA. Initial gate driver enable delay, eq. (1).
DS p.14, 7.3.2 Charge pump, Equation 1 (the DS quotes 345 uA as the charge-pump current; the table value is
I(BST) typ 345 uA, DS p.6). The text under eq. 1 gives V(BST_UVLOR) = 10.81 V (max).
cbst: F (design choice, BST to SRC). vbst_uvlor: V, rising UVLO threshold (DS p.6). i_bst: A, charge-pump
current (DS p.6, I(BST); min 100 uA gives the longest delay). Returns: s.
INPUTS: vbst_uvlor -> v_bst_uvlor (max 10.81 V is the worst case), i_bst -> i_bst (min 100 uA is the worst case).
```

Inputs:

- `vbst_uvlor` -> `v_bst_uvlor` (min 7.19 typ 9 max 10.81 V)
- `i_bst` -> `i_bst` (min 100 typ 345 max 555 uA)

### `i_inrush`

```
IINRUSH = CLOAD x VBATT / Tcharge. Inrush current during turn-on, eq. (2). DS p.15, 7.3.1 Inrush Current
Limiting, Equation 2. c_load: F (design choice). vbatt: V (design choice). t_charge: s (design choice).
Returns: A. INPUTS: none (all design choices).
```

Inputs:


### `c1_for_inrush`

```
C1 = 0.63 x V(BST-SRC) x CLOAD / (R1 x IINRUSH). Gate-ramp capacitor for a target inrush, eq. (3). DS p.16,
7.3.1 Inrush Current Limiting, Equation 3. The 0.63 is printed in the equation. vbst_src: charge-pump voltage, V
(the DS text under eq. 3 gives 11 V; design choice). c_load: F. r1: ohm (the DS suggests 100 kohm as a start).
i_inrush_target: A (design choice). Returns: F. INPUTS: none.
```

Inputs:


### `cbst_min`

```
CBST = Qg(total) / dVBST + 10 x C1. Minimum bootstrap capacitor, eq. (4). DS p.16, 7.3.1 Inrush Current
Limiting, Equation 4. The 10 x C1 term is printed in the equation; with C1 = 0 this is the DS design eq. (9)
(DS p.23, CBST = Qg(total) / 1 V). qg_total: C (gate charge, design choice, e.g. 85 nC for the DS design FET).
dv_bst: V, the BST ripple (DS p.16 text: dVBST 1 V typical; design choice). c1: F (from c1_for_inrush).
Returns: F. INPUTS: none.
```

Inputs:


### `vscp_from_riscp`

```
V(SCP) = 2 uA x RISCP + 19 mV. Short-circuit threshold set by the ISCP resistor, the inverse of eq. (5).
DS p.17, 7.3.3 Short-Circuit Protection, Equation 5: RISCP = (ISC x RSNS - 19 mV) / 2 uA, where ISC x RSNS is
V(SCP). The 19 mV and 2 uA are printed in eq. 5; they reproduce the DS table rows (R(ISCP) = 140.5 kohm gives
300 mV, 28 kohm gives 75 mV, DS p.7). riscp: ohm. Returns: V (threshold across CS+ and CS-).
INPUTS: none (riscp is a design choice; the table row bounds are in the v_scp_* params).
```

Inputs:


### `riscp_for_isc`

```
RISCP = (ISC x RSNS - 19 mV) / 2 uA. Short-circuit ISCP resistor for a desired short-circuit current, eq. (5).
DS p.17, 7.3.3 Short-Circuit Protection, Equation 5. isc: A (design choice). rsns: ohm, the high or low side sense
resistor or the FET RDS(ON) (design choice). Returns: ohm. INPUTS: none.
Note: the DS design example (DS p.23, eq. 10) prints 50.5 kohm for ISC = 60 A with RDS(ON) = 2.3 mohm; eq. 5 with
those numbers gives 59.5 kohm. The printed result implies RSNS = 2.0 mohm. See the open items.
```

Inputs:


### `i_sc_from_vscp`

```
ISC = V(SCP) / RSNS. Short-circuit current trip level from a V(SCP) threshold row and the sense resistor
(eq. 5 solved for ISC: ISC x RSNS = V(SCP)). The V(SCP) row must be the one for the chosen ISCP resistor
(v_scp_r140k5 for 140.5 kohm, v_scp_r28k for 28 kohm, and so on, DS p.7). Using the row min and max gives a
worst-case trip range; the RSNS tolerance is a separate input. vscp: V. rsns: ohm. Returns: A.
INPUTS: vscp -> v_scp_r140k5 (example row; use the row for the chosen R(ISCP)).
```

Inputs:

- `vscp` -> `v_scp_r140k5` (min 283 typ 300 max 318 mV)

### `v_iscp_bias_for_vscp`

```
V(SCP_BIAS) = 5 x ISC x RSNS - 95 mV, with ISC x RSNS = V(SCP). External bias voltage on the ISCP pin that sets
the threshold without RISCP. DS p.17, 7.3.3 Short-Circuit Protection, text equation ('V(SCP_BIAS) in mV = ISC x
RSNS x 5 - 95 mV'). The DS limits the bias to 3 V. vscp: V (threshold, ISC x RSNS). Returns: V.
INPUTS: none (vscp is a design choice; the table rows V(ISCP) = 3 V, 1.405 V, 280 mV, 105 mV are the DS checks).
```

Inputs:


### `ctmr_for_tsc`

```
CTMR = ITMR x tSC / 1.1. Fault-timer capacitor for a desired short-circuit response time, eq. (6). DS p.18,
7.3.3.1 Short-Circuit Protection With Auto-Retry, Equation 6. The DS text under eq. 6 gives ITMR = 80 uA internal
pull-up current; eq. 11 (DS p.24, design example) uses I(TMR_SRC_CB) = 87 uA. The 1.1 is printed; it is the
TMR clamp (V(TMR_SC) typ 1.1 V, DS p.7).
tsc: s (design choice). i_tmr: A, default 80 uA as printed in the eq. 6 text. v_tmr: V, default 1.1 as printed.
Returns: F. INPUTS: i_tmr -> i_tmr_src_cb (table row 65/87/106 uA, DS p.7; eq. 11 uses its typ) and
v_tmr -> v_tmr_sc (0.87/1.1/1.26 V, DS p.7), so wca gives bounds. The 80 uA text value is a DS inconsistency
(open item), kept only as the default and as i_tmr_pullup_text.
```

Inputs:

- `i_tmr` -> `i_tmr_src_cb` (min 65 typ 87 max 106 uA)
- `v_tmr` -> `v_tmr_sc` (min 0.87 typ 1.1 max 1.26 V)

### `t_retry`

```
tRETRY = 22.7 x 10^6 x CTMR. Auto-retry time after the first cycle, eq. (7). DS p.18, 7.3.3.1, Equation 7.
The 22.7e6 s/F is printed in the equation. ctmr: F. Returns: s. INPUTS: none.
```

Inputs:


### `ctmr_latch`

```
CTMR = tSC / (RTMR x ln(1 / (1 - 1.1 / (RTMR x I(TMR_SRC_CB))))). Fault-timer capacitor for latch-off with a
parallel RTMR, eq. (8). DS p.19, 7.3.3.2 Short-Circuit Protection With Latch-Off, Equation 8. The 1.1 is printed
(the TMR clamp). tsc: s (design choice). rtmr: ohm (the DS uses 100 kohm). i_tmr_src_cb: A, positive
charge current, abs() applied. Returns: F. INPUTS: i_tmr_src_cb -> i_tmr_src_cb. C increases with I: max 106 uA
gives the largest C for a target tSC; for a fixed C, min 65 uA gives the longest tSC. The printed 1.1 V is kept
as printed (eq. 8); it is V(TMR_SC) typ (0.87-1.26 V, DS p.7), not swept here.
```

Inputs:

- `i_tmr_src_cb` -> `i_tmr_src_cb` (min 65 typ 87 max 106 uA)

### `vin_ovp_from_divider`

```
VINOVP = V(OVR) x (R1 + R2 + R3) / R3. Overvoltage trip from the resistor divider VIN-R1-EN/UVLO-R2-OV-R3-GND (DS Fig 7-5, p.16; EN/UVLO is the upper tap, OV the lower).
Inverse of eq. (12), DS p.24, 8.2.2 Detailed Design Procedure, Equation 12: V(OVR) = R3/(R1+R2+R3) x VINOVP.
r1, r2, r3: ohm (design choices). vovr: V, OV rising threshold (DS p.6 typ 1.23 V; DS text p.24 uses 1.225 V).
Returns: V. INPUTS: vovr -> v_ovr (rising OV threshold; min 1.17, max 1.28 V gives the trip range).
```

Inputs:

- `vovr` -> `v_ovr` (min 1.17 typ 1.23 max 1.28 V)

### `vin_uvlo_from_divider`

```
VINUVLO = V(UVLOR) x (R1 + R2 + R3) / (R2 + R3). Undervoltage (UVLO) rising trip from the same divider.
Inverse of eq. (13), DS p.24, 8.2.2 Detailed Design Procedure, Equation 13: V(UVLOR) = (R2+R3)/(R1+R2+R3) x
VINUVLO. r1, r2, r3: ohm (design choices). vuvlo: V, UVLO rising threshold (DS p.6). Returns: V.
INPUTS: vuvlo -> v_uvlor (rising UVLO threshold; min 1.17, max 1.29 V gives the trip range).
For the falling (shutdown) trip pass v_uvlof (DS p.6) instead.
```

Inputs:

- `vuvlo` -> `v_uvlor` (min 1.17 typ 1.23 max 1.29 V)


## Examples

| Call | Computed | Expected | Rel. tol | Result | Cite |
|---|---|---|---|---|---|
| cbst_min(qg_total=8.5e-08, dv_bst=1, c1=0) | 8.5e-08 | 8.5e-08 | 0.001 | pass | DS p.23, 8.2.2 Selection of Bootstrap Capacitor, eq. 9, CBST = 85 nF |
| vscp_from_riscp(riscp=140500) | 0.3 | 0.3 | 0.001 | pass | DS p.7, 5.5 V(SCP) R(ISCP) = 140.5 kohm typ 300 mV; eq. 5 inverse |
| vscp_from_riscp(riscp=28000) | 0.075 | 0.075 | 0.001 | pass | DS p.7, 5.5 V(SCP) R(ISCP) = 28 kohm typ 75 mV; eq. 5 inverse |
| vscp_from_riscp(riscp=10500) | 0.04 | 0.04 | 0.001 | pass | DS p.7, 5.5 V(SCP) R(ISCP) = 10.5 kohm typ 40 mV; eq. 5 inverse |
| vscp_from_riscp(riscp=500) | 0.02 | 0.02 | 0.001 | pass | DS p.7, 5.5 V(SCP) R(ISCP) = 500 ohm typ 20 mV; eq. 5 inverse |
| v_iscp_bias_for_vscp(vscp=0.3) | 1.405 | 1.405 | 0.001 | pass | DS p.17 text and DS p.7, V(ISCP) = 1.405 V for V(SCP) 300 mV |
| v_iscp_bias_for_vscp(vscp=0.075) | 0.28 | 0.28 | 0.001 | pass | DS p.17 text and DS p.7, V(ISCP) = 280 mV for V(SCP) 75 mV |
| v_iscp_bias_for_vscp(vscp=0.04) | 0.105 | 0.105 | 0.001 | pass | DS p.17 text and DS p.7, V(ISCP) = 105 mV for V(SCP) 40 mV |
| ctmr_for_tsc(tsc=5e-05, i_tmr=8.7e-05, v_tmr=1.1) | 3.95455e-09 | 3.955e-09 | 0.001 | pass | DS p.24, 8.2.2 Selection of CTMR, eq. 11, 3.95 nF before the standard-value choice |
| vin_ovp_from_divider(r1=470000, r2=28700, r3=10400, vovr=1.225) | 59.9661 | 60 | 0.001 | pass | DS p.24, 8.2.2 Setting the UVLO and OV, eq. 12 with V(OVR) 1.225 V, VINOVP 60 V |
| vin_uvlo_from_divider(r1=470000, r2=28700, r3=10400, vuvlo=1.23) | 16.0152 | 16 | 0.002 | pass | DS p.24, 8.2.2 Setting the UVLO, eq. 13 with V(UVLOR) 1.23 V, VINUVLO 16 V; tolerance 0.2 % for the DS rounding of R2 |
