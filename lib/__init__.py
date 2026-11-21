"""Component library: load parts, run worst-case math, make tables and plots.

component, param and wca are stdlib only and imported eagerly; only lib.report (matplotlib) resolves lazily (PEP 562),
so `import lib.component` (as tools/check_stamps.py and tools/stamp.py use) needs no matplotlib. The eager
`from .wca import wca` must stay: it rebinds lib.wca from the submodule to the function, which a lazy lookup cannot do
(Python sets lib.wca to the submodule when it is first imported, e.g. by lib.report).
"""

import importlib

from .component import human_review_needed, load, reset_inputs, unverified_inputs, used_inputs
from .param import Param
from .wca import sweep, wca

_LAZY = {"inputs_section": "report", "plot_band": "report", "table": "report", "verdict": "report"}

__all__ = ["load", "Param", "wca", "sweep", "table", "plot_band", "unverified_inputs", "used_inputs", "reset_inputs", "verdict",
           "inputs_section", "human_review_needed"]


def __getattr__(name):
    mod = _LAZY.get(name)
    if mod is None:
        raise AttributeError(f"module 'lib' has no attribute {name!r}")
    value = getattr(importlib.import_module(f".{mod}", __name__), name)
    globals()[name] = value
    return value


def __dir__():
    return sorted(set(globals()) | set(__all__))
