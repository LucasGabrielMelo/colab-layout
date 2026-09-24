"""Executa ActiveCircuit.ipynb e grava o GDS nesta pasta."""

from __future__ import annotations

import json
import os
from pathlib import Path

os.environ.setdefault("MPLBACKEND", "Agg")

HERE = Path(__file__).resolve().parent
os.chdir(HERE)

nb = json.loads((HERE / "ActiveCircuit.ipynb").read_text(encoding="utf-8"))
ns: dict = {"__name__": "__main__"}

for i, cell in enumerate(nb["cells"]):
    if cell["cell_type"] != "code":
        continue
    src = "".join(cell["source"])
    if not src.strip():
        continue
    src = src.replace("c.show()", "pass")
    exec(compile(src, f"ActiveCircuit.ipynb:cell{i}", "exec"), ns)

print(f"GDS salvo em {HERE / 'CircuitoLucivaldoV2.gds'}")
