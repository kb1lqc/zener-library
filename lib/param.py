"""Param: a value with optional min / typ / max, stored in SI base units."""

from dataclasses import dataclass, replace

from .units import eng, to_si


@dataclass(repr=False)
class Param:
    """A datasheet number. Any of min/typ/max may be None (the datasheet did not give it).

    Values are SI floats (ohm, V, A, ...); `unit` is the SI base unit. The other fields are
    optional metadata copied from component.toml.
    """

    min: float = None
    typ: float = None
    max: float = None
    unit: str = ""
    name: str = None
    symbol: str = None
    kind: str = None
    scope: str = None
    conditions: str = None
    cite: str = None
    note: str = None
    min_ref: str = None
    max_ref: str = None
    typ_ref: str = None
    curve: bool = None
    text: str = None  # a rating stated in words, no number
    typ_spread: float = None  # set when the DS prints "+/-X" as typ: typ is then 0 and X is the typical spread
    verified: str = None  # "<who> <YYYY-MM-DD> <method>": an independent check of this row against the DS (None = not yet)
    verification_type: str = None  # human_page_image | cross_model_page_image | manufacturer_export

    @classmethod
    def tol(cls, nominal, fraction, unit):
        """Nominal value +/- a fraction. Param.tol(5.49, 0.01, 'kohm') is 5.49 kohm +/-1 %."""
        x, base = to_si(nominal, unit)
        low, high = sorted([x * (1 - fraction), x * (1 + fraction)])
        return cls(min=low, typ=x, max=high, unit=base)

    @classmethod
    def exact(cls, x, unit):
        """A value with no tolerance: min = typ = max = x."""
        value, base = to_si(x, unit)
        return cls(min=value, typ=value, max=value, unit=base)

    def with_typ(self, typ_si):
        """Copy with typ set by the CALLER (SI units), for nominal analysis of a bound-only param.

        Example: tolerance printed only as +/-0.5 % -> tol.with_typ(0.0) says "nominal resistor = R_nom".
        The library never does this on its own; the caller states the assumption in code.
        """
        return replace(self, typ=typ_si)

    def fmt(self, field):
        """Format one of 'min', 'typ', 'max' with an engineering prefix ('-' if missing)."""
        return eng(getattr(self, field), self.unit)

    def __repr__(self):
        if self.text is not None:
            return f"Param(text={self.text!r})"
        parts = [f"{f}={self.fmt(f)}" for f in ("min", "typ", "max") if getattr(self, f) is not None]
        return "Param(" + ", ".join(parts) + ")"
