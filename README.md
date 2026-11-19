# Component library: datasheet numbers + equations + KiCad

[![verify](https://github.com/kb1lqc/zener-library/actions/workflows/verify.yml/badge.svg)](https://github.com/kb1lqc/zener-library/actions/workflows/verify.yml) [![release](https://img.shields.io/github/v/tag/kb1lqc/zener-library?filter=v*&sort=semver&label=release)](https://github.com/kb1lqc/zener-library/tags)

Every part here has three things a person or an AI needs to design with it and check the result:

1. **Data** (`component.toml`): pins and datasheet parameters with min / typ / max, units, test conditions and a
   page cite for every number.
2. **Math** (`calc.py`): the datasheet's application equations as plain Python functions, each citing its page, plus
   the datasheet's own worked examples, which the validator re-runs.
3. **KiCad** (`.kicad_sym`, `.kicad_mod`, embedded STEP): symbol pins match the data exactly; footprint pads follow
   the datasheet land pattern.
4. **Zener wrapper** (`<Value>.zen`): generated from `component.toml` for circuit capture with Diode's `pcb`
   toolchain: typed pins, the KiCad symbol and footprint, and DC checks on the voltages each instance declares.

`lib/` turns those into worst-case and nominal numbers, tables and plots. The format is defined in
[docs/SPEC.md](docs/SPEC.md); KiCad rules in [docs/KICAD.md](docs/KICAD.md).

## Parts

| Part | What | README |
|---|---|---|
| Infineon BSC040N10NS5 | 100 V N-channel OptiMOS 5 MOSFET, 4.0 mΩ max, PG-TDSON-8 (SuperSO8) | [README](components/Infineon/BSC040N10NS5/README.md) |
| Infineon ISC035N10NM5LF2 | 100 V N-channel OptiMOS 5 Linear FET 2 (wide SOA), 3.5 mΩ max, PG-TDSON-8 | [README](components/Infineon/ISC035N10NM5LF2/README.md) |
| Infineon ISC750P10LM | -100 V P-channel MOSFET, 75 mΩ max, PG-TDSON-8 (SuperSO8) | [README](components/Infineon/ISC750P10LM/README.md) |
| TI INA821IDGK | Precision instrumentation amplifier, VSSOP-8 | [README](components/TexasInstruments/INA821IDGK/README.md) |
| ADI LTC4364 MS family (6 variants: C/I/H grade x -1 latch-off / -2 auto-retry) | Surge stopper + ideal diode, MSOP-16 | [README](components/AnalogDevices/LTC4364MS/README.md) |
| TI INA241 DGK family (10 variants: A1-A5 / B1-B5, gain 10/20/50/100/200) | -5 V to 110 V bidirectional current-sense amplifier, VSSOP-8 | [README](components/TexasInstruments/INA241DGK/README.md) |
| TI TPS48000QDGXQ1 | Automotive 3.5-95 V high-side switch controller with short-circuit protection, VSSOP-19 | [README](components/TexasInstruments/TPS48000QDGXQ1/README.md) |
| TI INA229AIDGS | 85 V, 20-bit power/energy/charge monitor, SPI, VSSOP-10 | [README](components/TexasInstruments/INA229AIDGS/README.md) |
| ST STM32H723ZET6 | Cortex-M7 550 MHz MCU, 512 KB flash, LQFP144, -40 to 85 °C; core electrical sections (interface timing not yet extracted) | [README](components/STMicroelectronics/STM32H723ZET6/README.md) |
| ST VNF1248F | 12/24/48 V high-side switch controller with e-fuse, SPI, QFN32L 5x5 | [README](components/STMicroelectronics/VNF1248F/README.md) |
| Panasonic ERJ-2RKF series | Thick film resistor, 0402, ±1 %, 10 Ω to 1 MΩ (E24/E96); value is a design input | [README](components/Panasonic/ERJ-2RKF/README.md) |
| Panasonic ERJ-3EKF series | Thick film resistor, 0603, ±1 %, 10 Ω to 1 MΩ (E24/E96); value is a design input | [README](components/Panasonic/ERJ-3EKF/README.md) |
| Panasonic ERJ-6ENF series | Thick film resistor, 0805, ±1 %, 10 Ω to 2.2 MΩ (E24/E96); value is a design input | [README](components/Panasonic/ERJ-6ENF/README.md) |
| Panasonic ERJ-8ENF series | Thick film resistor, 1206, ±1 %, 10 Ω to 2.2 MΩ (E24/E96); NRFND in the 2026.5 catalog | [README](components/Panasonic/ERJ-8ENF/README.md) |
| Panasonic ERA-2AEB series | Thin film resistor, 0402, ±0.1 %, ±25 ppm/°C, 47 Ω to 100 kΩ (E24; E96 from 100 Ω) | [README](components/Panasonic/ERA-2AEB/README.md) |
| Panasonic ERA-3AEB series | Thin film resistor, 0603, ±0.1 %, ±25 ppm/°C, 47 Ω to 330 kΩ (E24; E96 from 100 Ω) | [README](components/Panasonic/ERA-3AEB/README.md) |
| Panasonic ERA-6AEB series | Thin film resistor, 0805, ±0.1 %, ±25 ppm/°C, 47 Ω to 1 MΩ (E24; E96 from 100 Ω) | [README](components/Panasonic/ERA-6AEB/README.md) |
| Murata GCM155 series (0402) | Automotive X7R and C0G MLCC, 697 catalog values; part picked by capacitance, rated voltage, dielectric | [README](components/Murata/GCM155/README.md) |
| Murata GCM188 series (0603) | Automotive X7R and C0G MLCC, 633 catalog values; part picked by capacitance, rated voltage, dielectric | [README](components/Murata/GCM188/README.md) |
| Murata GCM21A series (0805, 1.0 mm) | Automotive X7R and C0G MLCC, 163 catalog values; part picked by capacitance, rated voltage, dielectric | [README](components/Murata/GCM21A/README.md) |
| Murata GCM21B series (0805, 1.25 mm) | Automotive X7R and C0G MLCC, 137 catalog values; part picked by capacitance, rated voltage, dielectric | [README](components/Murata/GCM21B/README.md) |
| Murata GCM216 series (0805, 0.6 mm) | Automotive X7R and C0G MLCC, 33 catalog values; part picked by capacitance, rated voltage, dielectric | [README](components/Murata/GCM216/README.md) |
| Murata GCM219 series (0805, 0.85 mm) | Automotive X7R and C0G MLCC, 49 catalog values; part picked by capacitance, rated voltage, dielectric | [README](components/Murata/GCM219/README.md) |
| Murata GCM319 series (1206, 0.85 mm) | Automotive C0G MLCC, 44 catalog values; part picked by capacitance, rated voltage, dielectric | [README](components/Murata/GCM319/README.md) |
| Murata GCM31A series (1206, 1.0 mm) | Automotive C0G MLCC, 147 catalog values; part picked by capacitance, rated voltage, dielectric | [README](components/Murata/GCM31A/README.md) |
| Murata GCM31B series (1206, 1.25 mm) | Automotive X7R and C0G MLCC, 22 catalog values; part picked by capacitance, rated voltage, dielectric | [README](components/Murata/GCM31B/README.md) |
| Murata GCM31C series (1206, 1.6 mm) | Automotive X7R and C0G MLCC, 82 catalog values (no 3D model yet); part picked by capacitance, rated voltage, dielectric | [README](components/Murata/GCM31C/README.md) |
| Murata GCM31M series (1206, 1.15 mm) | Automotive X7R and C0G MLCC, 18 catalog values; part picked by capacitance, rated voltage, dielectric | [README](components/Murata/GCM31M/README.md) |
| Murata GCM32D series (1210, 2.0 mm) | Automotive X7R and C0G MLCC, 41 catalog values; part picked by capacitance, rated voltage, dielectric | [README](components/Murata/GCM32D/README.md) |
| Murata GCM32E series (1210, 2.5 mm) | Automotive X7R and C0G MLCC, 43 catalog values; part picked by capacitance, rated voltage, dielectric | [README](components/Murata/GCM32E/README.md) |
| Murata GCM32Q series (1210, 1.5 mm) | Automotive X7R MLCC, 4 catalog values; part picked by capacitance, rated voltage, dielectric | [README](components/Murata/GCM32Q/README.md) |
| Vishay Dale WSK2512 series | 4-terminal current-sense resistor, 2512, 5-200 mΩ, ±0.1/0.5/1 %, Vishay decade values; value and tolerance are design inputs | [README](components/Vishay/WSK2512/README.md) |
| Vishay Dale WSK2512-LOW series | 4-terminal current-sense resistor, 2512, 1-4.9 mΩ, ±0.5/1 % (sub-1 mΩ excluded: no printed code) | [README](components/Vishay/WSK2512-LOW/README.md) |
| Vishay Dale WSK2512R0250D | 25 mohm ±0.5 % 4-terminal current-sense resistor | [README](components/Vishay/WSK2512R0250D/README.md) |

## Use it

Python 3.11+ and matplotlib. No other dependencies.

```python
from lib import load, Param, wca, table

ina = load("TexasInstruments/INA821IDGK")
rg = Param.tol(2.61, 0.001, "kohm")               # design choice: 2.61 kohm, 0.1 %
g = wca(ina.calc.gain, rg=rg)                      # worst case over every min/max corner
vos = wca(ina.calc.vos_rti, unit="V", g=20.0, **ina.inputs("vos_rti"))   # inputs from the INPUTS map
print(table([("Gain", g, ""), ("Offset (RTI)", vos, "full temperature")]))
```

Worked circuit analysis, with tables, rating checks and plots:
[examples/current_sense.py](examples/current_sense.py). Run `python3 -m examples.current_sense` to generate its
report and plots in `examples/out/` (generated, not committed).

How worst case works, so you can check it by hand: the result's typ is the function at every input's typ; its
min/max are the lowest and highest results over all 2^n combinations of input min/max. A missing bound is an error,
never a guess.

## Two layers, one source of truth

| Layer | Files | What it is for | Who edits it |
|---|---|---|---|
| Data + math | `component.toml`, `calc.py` | Every datasheet number (min/typ/max, cite) and equation; worst-case and nominal analysis, tables, plots in Python | People and AI, verified against the datasheet |
| Circuit capture | `<Value>.zen`, `pcb.toml` | Zener wrapper: pins as typed nets, KiCad symbol/footprint, part info, DC voltage/ambient checks | Nobody: generated by `python3 -m lib.zen` |

Which datasheet rows become Zener checks is written in `component.toml` (`check_pins`, `check_ambient`, or an
`unchecked` reason), so the checks are reviewed with the data. Each part's README has a "Zener checks" table.
Using a part in a Zener module:

```zen
INA = Module("github.com/kb1lqc/zener-library/components/TexasInstruments/INA821IDGK/INA821IDGK.zen")
INA(name="U1", VS_P=Power("V15", voltage="15V 5%"), VS_N=Power("VN15", voltage="-15V 5%"),
    IN_P=Net("SNS_P", voltage="0V to 130mV"), IN_N=Net("SNS_N", voltage="0V"), RG1=Net("RG1"), RG2=Net("RG2"),
    REF=Net("REF", voltage="0V"), OUT=Net("VOUT"), ambient=ambient, derate=derate)
```
then `pcb sync`. Every checked net needs a declared voltage range, or the build reports UNVERIFIED. Details:
docs/SPEC.md "Zener wrapper" and the `zener-wrapper` skill in `.claude/skills/`.

## Check it

```sh
python3 -m lib.check                     # data vs symbol vs footprint, units, cites, datasheet examples
python3 -m unittest discover -s tests    # library tests + Zener wrapper builds (skipped without pcb)
python3 -m lib.zen                       # regenerate each Zener wrapper from its data (needs pcb for pcb fmt)
python3 -m lib.readme                    # regenerate each component README from its data
pcb build -Wstyle -Dwarnings components/TexasInstruments/INA821IDGK   # build one wrapper
python3 -m examples.current_sense        # regenerate the worked example
```

Per-parameter human verification is recorded by `verified` plus `verification_type = "human_page_image"` in
`component.toml`; its supporting page images and decisions are kept in the component's `datasheet-review/` archive. See the
[review workflow](docs/spec/datasheet-review.md).

## For AI assistants designing with this library

- Use only parameters from `component.toml` (via `part.param(key)` or `part.inputs(fn)`); never retype a datasheet
  number. If a needed number is not there, say so; do not estimate it.
- Use `scope = "full"` rows for worst case over temperature. `25C` rows hold only at 25 °C; `partial` rows do not
  cover the whole grade. Follow the temperature recipe in docs/SPEC.md.
- `curve = true` values and `_typ` functions are estimates, never pass/fail bounds. `text` rows (for example
  "Continuous") have no number.
- Mark every value you choose as a design choice in code, as `examples/current_sense.py` does. For nominal analysis
  of a bound-only spec, state the assumption with `Param.with_typ(...)`.
- Read each part's README notes and conditions before using a row: footnotes and datasheet ambiguities are recorded
  there.

## Add a part

1. Put the datasheet PDF in `docs/datasheets/` and the vendor KiCad/STEP download in `docs/vendor/<Value>/`
   (both are git-ignored).
2. Fix up the symbol and footprint per docs/KICAD.md into `components/<Manufacturer>/<Value>/`.
3. Write `component.toml` and `calc.py` per docs/SPEC.md, reading table pages as rendered images
   (`pdftoppm -r 150 -png -f N -l N`), not extracted text.
4. Generate the complete review packet and save its human-review record beside the component with one command:
   ```sh
   python3 tools/ds_review_packet.py docs/datasheets/<datasheet>.pdf components/<Manufacturer>/<Value> \
     --out temporary/<Value>-review --archive
   ```
   Open `components/<Manufacturer>/<Value>/datasheet-review/<PDF-SHA-prefix>/datasheet-review.md` and `coverage.md`.
   Compare each row with its cited PDF image, record a decision, then account for every indexed section/table/figure
   and manually check for unindexed material. `AGREE_TEXT_CHECK` is only a text aid, not verification. This one
   command calls `ds_index` and `table_xcheck`; do not run those scripts separately. Commit the archive with the
   component; never copy the PDF into `components/`.
5. For each **Confirmed** parameter only, add both fields inside its `[param.<key>]` table:
   `verified = "abrown 2026-11-19 human page-image review"` and
   `verification_type = "human_page_image"`. Cross-model audits use `cross_model_page_image`; text checks get no
   verification stamp. `lib.check` validates format, not whether the review happened. If a value changes, remove or
   renew its stamp and review it again.
6. After filling reviewer/date, attestation, every parameter decision, and all coverage items, run
   `python3 tools/ds_review_packet.py --finalize components/<Manufacturer>/<Value>/datasheet-review/<PDF-SHA-prefix>`.
   It refuses incomplete checklists, stale values/cites, and Confirmed rows without matching human stamps.
7. Give every abs_max / rec_op row `check_pins`, `check_ambient` or an `unchecked` reason, then
   `python3 -m lib.check` clean, `python3 -m lib.zen`, `python3 -m lib.readme`.
8. Add `tests/zen/<Value>_harness.zen` and its cases in `tests/test_zen.py`; all tests pass.
9. Have a second reviewer check every number against the page images.
A short guide to the workflow and part types is [docs/WORKFLOW.md](docs/WORKFLOW.md). The full procedure, with defaults for every judgement call, is in [CLAUDE.md](CLAUDE.md).
