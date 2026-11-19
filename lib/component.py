"""Load a component directory: component.toml, calc.py, parameters in SI."""

import dataclasses
import importlib.util
import tomllib
from dataclasses import dataclass, field
from pathlib import Path

from . import capacitor as _cap
from . import series as _series
from .param import Param
from .units import to_si

ROOT = Path(__file__).resolve().parent.parent
# Param fields that are copied from the TOML as-is.
META = ("name", "symbol", "kind", "scope", "conditions", "cite", "note", "min_ref", "max_ref", "typ_ref", "curve", "text",
        "verified", "verification_type")
_USED = {}  # "<Value>:<key>" -> verified (None = unverified), for every row an analysis has read this process


def _record(label, key, verified):
    """Record one row read. Unverified is sticky: a later verified read of the same key never clears it."""
    k = f"{label}:{key}"
    _USED[k] = None if (k in _USED and not _USED[k]) else verified


def unverified_inputs():
    """Sorted "<Value>:<key>" of every row read through Part.param/inputs/series (and the helpers built on them) that
    has no `verified` stamp. A judged PASS that rests on any of them is reported "PASS (UNVERIFIED INPUTS)"."""
    return sorted(k for k, v in _USED.items() if not v)


def used_inputs():
    """Sorted "<Value>:<key>" of every row read so far (verified or not)."""
    return sorted(_USED)


def reset_inputs():
    """Forget the rows read so far (one analysis per process is the normal case; tests reset between cases)."""
    _USED.clear()


@dataclass
class Part:
    """A loaded component."""

    path: Path  # component directory
    info: dict  # the [part] table
    pins: list  # list of [[pin]] dicts
    params: dict  # key -> Param (SI)
    calc: object  # imported calc.py module, or None
    raw: dict  # the whole TOML as printed (printed units); for a variant, merged with its overrides
    variant: str = None  # variant Value for a family part, None for a plain component
    family_path: Path = None  # family directory (same as path) for a variant, None for a plain component
    hidden: dict = field(default_factory=dict)  # capacitor series: key -> restriction text of rows not loaded here
    selection: str = None  # capacitor series: catalog value of a Part.select() result (input record label)
    aliases: dict = field(default_factory=dict)  # key -> the TOML row it stands for (select(): tc -> tc_x7r)

    def param(self, key):
        """Param for one TOML key, in SI. KeyError names the unknown key."""
        if key not in self.params:
            why = f" (the row exists but is restricted to {self.hidden[key]}: use part.select(...).part)" if key in self.hidden else ""
            raise KeyError(f"{self.info.get('value')}: no parameter '{key}'{why}")
        return self._used(key)

    def _used(self, key):
        p = self.params[key]
        _record(self._label(), self.aliases.get(key, key), p.verified)
        return p

    def _label(self):
        base = self.variant or self.info.get("value")
        return f"{base}[{self.selection}]" if self.selection else base

    def inputs(self, function):
        """Datasheet arguments for calc.<function>, from its INPUTS map: {arg: Param or float}.

        "key" gives the whole Param (wca sweeps its min/max); "key.max" gives that one number as a float.
        Usage: wca(part.calc.rsns, ilim=5.0, **part.inputs("rsns")).
        """
        out = {}
        for arg, key in getattr(self.calc, "INPUTS", {}).get(function, {}).items():
            name, _, field = key.partition(".")
            out[arg] = getattr(self.param(name), field) if field else self.param(name)
        return out

    def series(self, prefix):
        """Params for keys '<prefix>_<n>' (n decimal): {n: Param}, sorted by n.

        part.series("vovc_thr") -> {0: Param, 1: Param, ...}.
        """
        found = {}
        for key, param in self.params.items():
            head, _, tail = key.rpartition("_")
            if head == prefix and tail.isdigit():
                found[int(tail)] = self._used(key)
        return dict(sorted(found.items()))

    def _bounds(self, key):
        r = self.param(key)
        return r.min, r.max

    def _need_resistor(self):
        if self.info.get("series") != "resistor":
            raise ValueError(f"{self.info.get('value')} is not a resistor series component")

    def pairs(self):
        """Sorted [(value, tolerance code)] a resistor series allows (code None for a series without tolerance options)."""
        self._need_resistor()
        return _series.pairs(self.info, self._bounds)

    def tolerances(self):
        """Tolerance codes of a resistor series with tolerance options, as listed ([] for a plain series)."""
        self._need_resistor()
        return [code for code, _, _ in _series.options(self.info)]

    def values(self, tol=None):
        """Allowed values (ohm) of a series component, sorted: the series values inside its ranges.

        With tolerance options, tol = a code gives the values that code allows; None gives the values any code allows.
        """
        self._need_resistor()
        if tol is not None and tol not in self.tolerances():
            raise ValueError(f"{self.info['value']}: tolerance code '{tol}' is not an option (options: "
                             f"{', '.join(self.tolerances()) or 'none'})")
        return sorted({v for v, code in self.pairs() if tol is None or code == tol})

    def _resolve(self, value, tol):
        """The tolerance code (None for a plain series) for an allowed value; ValueError for anything else."""
        values = self.values(tol)
        name = self.info["value"]
        if not any(abs(value - v) <= 1e-9 * v for v in values):
            where = f" with tolerance {tol}" if tol else ""
            span = f" from {values[0]:g} to {values[-1]:g} ohm" if values else ""
            raise ValueError(f"{name}: {value:g} ohm{where} is not an allowed value ({', '.join(self.info['e_series'])}{span})")
        if not self.tolerances():
            return None
        if tol is not None:
            return tol
        codes = [c for v, c in self.pairs() if abs(value - v) <= 1e-9 * v]
        if len(codes) > 1:
            raise ValueError(f"{name}: ambiguous: {value:g} ohm is allowed with tolerance codes {', '.join(codes)}; pass tol")
        return codes[0]

    def mpn(self, value, tol=None):
        """Orderable MPN of a series component for one allowed value (ohm), from calc.mpn.

        A series with tolerance options needs the code (calc.mpn(value, code)) unless only one code allows the value.
        """
        code = self._resolve(value, tol)
        return self.calc.mpn(value) if code is None else self.calc.mpn(value, code)

    def tolerance(self, tol):
        """Param of a tolerance option (fraction, min and max): wca(calc.resistance_worst, tol=part.tolerance("D"), ...)."""
        self._need_resistor()
        keys = {code: key for code, key, _ in _series.options(self.info)}
        if tol not in keys:
            raise ValueError(f"{self.info['value']}: tolerance code '{tol}' is not an option (options: {', '.join(keys) or 'none'})")
        return self.param(keys[tol])

    def series_value(self, value, tol=None):
        """Param for a chosen series value (ohm): typ = value, min/max from the tolerance row (a fraction).

        The row is `series_tol`, or with tolerance options the row of code tol (None only if one code allows the value).
        erj.series_value(2.61e3) -> min 2.5839 kohm, typ 2.61 kohm, max 2.6361 kohm for a +/-1 % row.
        """
        code = self._resolve(value, tol)
        row = self.param(self.info["series_tol"]) if code is None else self.tolerance(code)
        return Param(min=value * (1 + row.min), typ=value, max=value * (1 + row.max), unit="ohm")

    def tcr(self, value):
        """Param of the TCR row (1/degC) whose own range holds a value (ohm): [part] series_tcr pairs each row with its range.

        Use it as the tcr input of calc.resistance_worst, which INPUTS cannot map when the TCR depends on the value.
        """
        self._need_resistor()
        found = [self.param(t) for t, r in _series.tcr_rows(self.info)
                 if self.param(r).min * (1 - 1e-9) <= value <= self.param(r).max * (1 + 1e-9)]
        if len(found) != 1:
            raise ValueError(f"{self.info['value']}: {len(found)} TCR rows cover {value:g} ohm (need exactly 1; series_tcr)")
        return found[0]

    def catalog(self):
        """Catalog rows (lib.capacitor.CatalogRow) of a capacitor series: one per orderable value."""
        if self.info.get("series") != "capacitor":
            raise ValueError(f"{self.info.get('value')} is not a capacitor series component")
        return _cap.read_catalog(self.path / self.info["catalog"])

    def dielectrics(self):
        """Sorted dielectric names in the catalog of a capacitor series ('C0G', 'X7R')."""
        return sorted({r.dielectric for r in self.catalog()})

    def select(self, capacitance, rated_voltage, dielectric, tolerance=None):
        """Pick one catalog part: returns a Selection (MPN, Params, and a Part holding the rows that apply to it).

        capacitance in F and rated_voltage in V (or printed text '0.1uF', '50Vdc'); dielectric as printed in the catalog
        ('X7R'); tolerance as printed ('+/-10%', optional: needed only when the catalog has several for that value).
        ValueError for no match or an ambiguous match. sel.part.param("tc") is the dielectric's temperature
        characteristic row; sel.part.inputs("capacitance_worst_pct") feeds calc.capacitance_worst_pct (X7R), the _ppm twin serves C0G.
        """
        row = _cap.choose(self.catalog(), capacitance, rated_voltage, dielectric, tolerance)
        params, _ = _applicable(self.raw.get("param", {}), dielectric, row.value)
        cap, tol, rated = _cap.selection_params(row)
        tc_key = self.info["tc_param"][dielectric]
        params.update(capacitance=cap, tolerance=tol, rated_v=rated, tc=params[tc_key])
        label = f"{self.info.get('value')}[{row.value}]"
        _record(label, "capacitance", cap.verified)  # handed out directly as sel.capacitance / sel.rated_voltage
        _record(label, "rated_v", rated.verified)
        letter, alts = self.info["package_default"], self.info["package_alternates"]
        return Selection(row=row, value=row.value, mpn=row.value + letter, alternates=[row.value + a for a in alts],
                         dielectric=dielectric, tolerance=row.tolerance, thickness=row.thickness, capacitance=cap,
                         rated_voltage=rated, part=dataclasses.replace(self, params=params, hidden={}, selection=row.value,
                                                                        aliases={"tc": tc_key}))

    def resolve(self, key, rails):
        """Param with absolute min/max for a param stated relative to pins (min_ref / max_ref).

        rails = {pin_name: float or Param}. A float is exact. Conservative (narrowest guaranteed
        window): abs_min = offset_min + rail.max, abs_max = offset_max + rail.min.
        typ is dropped when min_ref/max_ref is used, unless typ_ref names a rail: then typ = typ offset + rail.typ
        (None if the rail Param has no typ). Params without refs are returned unchanged.

        Example: INA821 input range is min = 2 (ref -VS), max = -2 (ref +VS).
        With rails {"-VS": -15.0, "+VS": 15.0} resolve gives -13 V to 13 V.
        With rails {"-VS": Param(min=-15.9, max=-14.1), "+VS": Param(min=14.1, max=15.9)} it gives
        -12.1 V to 12.1 V (-14.1 + 2 and 14.1 - 2).
        """
        p = self.param(key)
        if not (p.min_ref or p.max_ref or p.typ_ref):
            return p
        lo, hi, typ = p.min, p.max, p.typ
        if p.min_ref:
            lo = p.min + _rail(key, rails, p.min_ref).max
        if p.max_ref:
            hi = p.max + _rail(key, rails, p.max_ref).min
        if p.typ_ref:  # typ = offset + rail typ; None if the rail has no typ
            rail_typ = _rail(key, rails, p.typ_ref, bounds=False).typ
            typ = None if rail_typ is None or p.typ is None else p.typ + rail_typ
        elif p.min_ref or p.max_ref:
            typ = None
        return dataclasses.replace(p, min=lo, max=hi, typ=typ, min_ref=None, max_ref=None, typ_ref=None)


@dataclass
class Selection:
    """One catalog part of a capacitor series (Part.select)."""

    row: object  # lib.capacitor.CatalogRow
    value: str  # MPN without the package letter
    mpn: str  # value + the default package letter
    alternates: list  # value + each alternate package letter (same part, other packaging)
    dielectric: str
    tolerance: str  # as printed
    thickness: str  # as printed
    capacitance: Param  # F, min/typ/max from the printed tolerance
    rated_voltage: Param  # V, min = -rating, max = rating (non-polarized)
    part: Part  # rows that apply to this part, plus capacitance, tolerance, rated_v and tc (the dielectric's row)


def _rail(key, rails, pin, bounds=True):
    """Rail for `pin` as a Param (floats become exact). ValueError if missing."""
    if pin not in rails:
        raise ValueError(f"resolve {key}: rails has no value for '{pin}'")
    rail = rails[pin]
    if not isinstance(rail, Param):
        rail = Param(min=rail, typ=rail, max=rail)
    if bounds and (rail.min is None or rail.max is None):
        raise ValueError(f"resolve {key}: rail '{pin}' needs both min and max")
    return rail


def restriction(table):
    """Text of a capacitor-series row's restriction ('dielectric X7R', 'parts A, B'), or None if it applies to all."""
    if "dielectric" in table:
        return f"dielectric {table['dielectric']}"
    if "parts" in table:
        return "parts " + ", ".join(table["parts"])
    return None


def _applicable(tables, dielectric=None, value=None):
    """({key: Param}, {key: restriction text of the rows left out}) for a capacitor series.

    A row with `dielectric` applies to parts of that dielectric, a row with `parts` to those catalog values; a row with
    neither applies to all. With dielectric=None and value=None only the unrestricted rows are returned.
    """
    params, hidden = {}, {}
    for key, table in tables.items():
        if "dielectric" in table:
            applies = table["dielectric"] == dielectric
        elif "parts" in table:
            applies = value in table["parts"]
        else:
            applies = True
        if applies:
            params[key] = to_param(table)
        else:
            hidden[key] = restriction(table)
    return params, hidden


def to_param(table):
    """Build a Param (SI) from one [param.x] TOML table."""
    unit = table.get("unit", "")
    values = {}
    for field in ("min", "typ", "max"):
        if field in table:
            values[field], base = to_si(table[field], unit)
    base = to_si(0, unit)[1]
    if "tol_pct" in table:  # DS prints "typ, -10 % / +10 %": min and max follow from typ
        if "typ" not in values or "min" in values or "max" in values:
            raise ValueError("tol_pct needs typ and no min/max")
        lo, hi = table["tol_pct"]
        values["min"], values["max"] = sorted([values["typ"] * (1 + lo / 100), values["typ"] * (1 + hi / 100)])
    meta = {k: table[k] for k in META if k in table}
    if table.get("sym"):  # DS printed an unsigned bound for a +/- quantity
        if "max" not in values or "min" in values:
            raise ValueError("sym = true needs max and no min")
        values["min"] = -values["max"]
    if table.get("typ_pm") or (table.get("sym") and "typ" in values):
        # DS printed "+/-X" in the TYP column: centred on 0 with a typical spread of X.
        values["typ_spread"], values["typ"] = abs(values["typ"]), 0.0
    return Param(unit=base, **values, **meta)


def load_calc(path):
    """Import calc.py from a file path (no package needed). Returns the module."""
    spec = importlib.util.spec_from_file_location("calc_" + path.parent.name.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def variants_of(folder):
    """The [variant.<Value>] tables of a family directory's variants.toml ({} for a plain component)."""
    file = Path(folder) / "variants.toml"
    if not file.exists():
        return {}
    with open(file, "rb") as f:
        return tomllib.load(f).get("variant", {})


def merge_variant(raw, variants, name):
    """component.toml data for one variant: shared data, filtered and overridden by variants.toml.

    [part]: shared keys, overridden by the variant's own keys; value = the variant name.
    Params: shared rows that apply to this variant (no `variants` list, or the list names it), then each
    [variant.<name>.param.<key>] table replaces the row of that key (same position) or is added at the end.
    """
    if name not in variants:
        raise ValueError(f"unknown variant '{name}'; variants: {', '.join(sorted(variants))}")
    own = variants[name]
    part = {**raw.get("part", {}), **{k: v for k, v in own.items() if k != "param"}, "value": name}
    params = {}
    for key, table in raw.get("param", {}).items():
        if name in table.get("variants", [name]):
            params[key] = {k: v for k, v in table.items() if k != "variants"}
    params.update(own.get("param", {}))
    return {**raw, "part": part, "param": params}


def find_variant(path):
    """(family directory, variant) for a path whose last part is a variant Value, found by scanning
    <path.parent>/*/variants.toml. FileNotFoundError if no family lists it."""
    for file in sorted(path.parent.glob("*/variants.toml")):
        if path.name in variants_of(file.parent):
            return file.parent, path.name
    raise FileNotFoundError(f"no component or variant '{path.name}' under {path.parent}")


def load(name, root=None, variant=None):
    """Load 'Mfr/Value' (under components/) or a directory path.

    A family directory (has variants.toml) needs variant=<Value>; a variant Value that is not a directory
    ('Mfr/LTC4364HMS-1') is found by scanning the manufacturer's families.
    """
    path = Path(name)
    if not path.is_dir():
        path = (root or ROOT) / "components" / name
    if not path.is_dir() and variant is None:
        path, variant = find_variant(path)
    with open(path / "component.toml", "rb") as f:
        raw = tomllib.load(f)
    variants = variants_of(path)
    if variants and variant is None:
        raise ValueError(f"{path.name} is a family; load it with variant= one of: {', '.join(sorted(variants))}")
    if variants:
        raw = merge_variant(raw, variants, variant)
    elif variant is not None:
        raise ValueError(f"{path.name} has no variants.toml, so variant='{variant}' is unknown")
    if raw.get("part", {}).get("series") == "capacitor":
        params, hidden = _applicable(raw.get("param", {}))
    else:
        params, hidden = {k: to_param(t) for k, t in raw.get("param", {}).items()}, {}
    calc_file = path / "calc.py"
    calc = load_calc(calc_file) if calc_file.exists() else None
    return Part(path, raw.get("part", {}), raw.get("pin", []), params, calc, raw,
                variant=variant, family_path=path if variants else None, hidden=hidden)


def run_example(calc, row):
    """Run one calc.EXAMPLES row (function, kwargs, expected, rel tol, cite). Returns (got, ok)."""
    fname, kwargs, expected, tol, _cite = row
    got = getattr(calc, fname)(**kwargs)
    # Tolerance is relative, except when expected is 0 (then it is absolute).
    allowed = tol if expected == 0 else tol * abs(expected)
    return got, abs(got - expected) <= allowed
