<!-- GENERATED - do not edit. Run: python3 -m lib.readme -->

# GCM32Q

## Datasheet review

[![Human page-image review: 0/5 human](https://img.shields.io/badge/human%20review-0%2F5%20human-lightgrey)](../../../docs/spec/datasheet-review.md)

Human page-image review: 0/5; cross-model audits: 0; manufacturer-export stamps: 0; legacy/unclassified: 0. Text checks are not verification. `lib.check` validates stamp format, not that review occurred.

## Part

- **manufacturer**: Murata
- **description**: Chip multilayer ceramic capacitors, X7R (R7), 3225M (1210), thickness 1.5 mm (code Q), AEC-Q200 (GCM series)
- **category**: capacitor_mlcc
- **package**: 3225M (1210)
- **datasheet_url**: 
- **datasheet_file**: docs/datasheets/GCM32Q7U2J682JX01-00B-EN.pdf
- **datasheet_rev**: 00B
- **datasheet_date**: 2026-04
- **kicad_symbol**: GCM32Q.kicad_sym
- **kicad_footprint**: GCM32Q.kicad_mod
- **step**: GCM32Q.step

## Series

- **Catalog**: `catalog.csv`, 4 orderable values, one row per value with its cite (a manufacturer export, not a datasheet table)
- **MPN rule**: catalog value + package letter; default `L`, alternates `K` (same part, other packaging); example: `GCM32QR72J103KWB1` -> `GCM32QR72J103KWB1L`
- **Selection**: `sel = part.select(capacitance, rated_voltage, dielectric, tolerance=None)` returns the MPN, `capacitance` / `rated_voltage` Params and `sel.part`, a Part holding the rows that apply (dielectric and part restrictions applied, plus `capacitance`, `tolerance`, `rated_v` and `tc`); an unlisted or ambiguous request raises ValueError
- **Zener wrapper**: configs `value`, `rated_v`, `dielectric`, optional `tolerance`; checks `part_orderable`, `rated_voltage` (|V(P1) - V(P2)| <= derate x rated voltage) and `ambient_range` (per dielectric)
- **Worst-case capacitance**: X7R (percent change): `wca(sel.part.calc.capacitance_worst_pct, **sel.part.inputs('capacitance_worst_pct'))`; C0G (ppm/degC): `wca(sel.part.calc.capacitance_worst_ppm, dt=Param(min=0, max=100), **sel.part.inputs('capacitance_worst_ppm'))` (dt required, 0 to 100 degC; below 25 degC use the printed drift rows). Both EXCLUDE DC-bias and aging loss

| Dielectric | Parts | Capacitance | Rated voltages | Tolerances | TC row |
|---|---|---|---|---|---|
| X7R | 4 | 6.8 nF to 150 nF | 250 V, 630 V | ±10% | `tc_x7r` |

## Pins

| Pin | Name | Type | Function | Cite |
|---|---|---|---|---|
| 1 | 1 | passive | Capacitor terminal (non-polarized) | DS p.2, Type & Dimension, image:Dimension |
| 2 | 2 | passive | Capacitor terminal (non-polarized) | DS p.2, Type & Dimension, image:Dimension |

## Parameters: rec_op

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Operating temperature range |  | -55 |  | 125 | degC | Applies to: dielectric X7R. Note: Read from the 1210 X7R sheet GCM32ER71C226ME19-01A. lib.catalog refuses an export row whose Operating Temperature is not -55 to 125 degC, so every X7R catalog row uses it. | DS p.2 (GCM32ER71C226ME19-01A-EN.pdf), Rated Value, Operating Temp. Range (-55 to 125 degC) |  |

## Parameters: electrical

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Temperature characteristic, R7 (X7R) | TC | -15 |  | 15 | % | Ref. temp 25 degC; temp range -55 to 125 degC; capacitance change over temperature Applies to: dielectric X7R. Note: Public STD code X7R (EIA). Capacitance change over temperature, not a DC-bias or aging limit. Read from the 1210 X7R sheet of thickness code E, used for every X7R catalog row of thickness code Q (open item: no X7R sheet for thickness code Q). | DS p.2 (GCM32ER71C226ME19-01A-EN.pdf), Rated Value, Temp. coeff. or Cap. Change (-15 to 15 %) |  |

## Parameters: mechanical

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions | Cite | Verified |
|---|---|---|---|---|---|---|---|---|
| Land pattern dimension a (reflow) | a | 2.0 |  | 2.4 | mm | Reflow soldering, chip 3.2x2.5, code 32 Note: Letter label only in the DS figure; neutral name. Inferred meaning: gap between lands (not printed). | DS p.28 (GCM32ER71C226ME19-01A-EN.pdf), 2. Land Dimensions, Table 2 Reflow Soldering Method, 3.2x2.5, a |  |
| Land pattern dimension b (reflow) | b | 1.0 |  | 1.2 | mm | Reflow soldering, chip 3.2x2.5, code 32 Note: Letter label only in the DS figure; neutral name. Inferred meaning: land length, outer side (not printed). | DS p.28 (GCM32ER71C226ME19-01A-EN.pdf), 2. Land Dimensions, Table 2 Reflow Soldering Method, 3.2x2.5, b |  |
| Land pattern dimension c (reflow) | c | 1.8 |  | 2.3 | mm | Reflow soldering, chip 3.2x2.5, code 32 Note: Letter label only in the DS figure; neutral name. Inferred meaning: land width across the chip (not printed). | DS p.28 (GCM32ER71C226ME19-01A-EN.pdf), 2. Land Dimensions, Table 2 Reflow Soldering Method, 3.2x2.5, c |  |

## Limits of this data

Rows by scope: full 1, na 4 (25C rows hold only at 25 degC). Curve (graph) rows: 0. Text rows: 0.

## Zener checks

Generated wrapper: `GCM32Q.zen` (`python3 -m lib.zen`). abs_max and rec_op rows are errors (abs_max x derate); 25C and partial rows are waivable warnings; a checked net with no voltage is UNVERIFIED.

| Param | Name | Checked against | Not checked / reason |
|---|---|---|---|
| op_temp_x7r | Operating temperature range | board ambient |  |

## Equations

### `capacitance_worst_pct`

```
Not a DS equation: C = C0 * (1 + tol) * (1 + tc).  For percent-change dielectrics (X7R): tc is the capacitance
change over the whole range as a FRACTION (the 1210 X7R sheet, DS p.2, Rated Value, Temp. coeff. or Cap. Change,
-15 to 15 % over -55 to 125 degC, ref 25 degC), so with the row's min/max the corners give the full-range worst case.
|tc| below 1e-3 (other than 0) raises ValueError, because that is a ppm/degC coefficient, not a fraction.
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


## Examples

| Call | Computed | Expected | Rel. tol | Result | Cite |
|---|---|---|---|---|---|
| capacitance_worst_pct(c0=6.8e-09, tol=-0.1, tc=-0.15) | 5.202e-09 | 5.202e-09 | 1e-12 | pass | DS p.2, Rated Value (X7R 1210 sheet) |
