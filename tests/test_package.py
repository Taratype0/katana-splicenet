"""Unit tests for katana-splicenet v2.3.1."""
from __future__ import annotations

from pathlib import Path
import numpy as np
import pandas as pd
import katana_splicenet as ksn
from katana_splicenet.cli import main as sn_cli_main


def test_splicenet_exports_bicor_tom_and_wgcna(tmp_path: Path) -> None:
    assert ksn.__version__ == "2.3.1"
    for sym in ksn.__all__:
        assert hasattr(ksn, sym), f"Missing export {sym}"
    rng = np.random.default_rng(42)
    f1 = rng.normal(size=(1, 16))
    f2 = rng.normal(size=(1, 16))
    x = np.vstack([0.5 + 0.15 * f1 + 0.03 * rng.normal(size=(25, 16)), 0.5 + 0.15 * f2 + 0.03 * rng.normal(size=(25, 16))])
    df_u = pd.DataFrame(np.clip(x, 0.05, 0.95), index=[f"EV_{i}" for i in range(50)], columns=[f"S_{j}" for j in range(16)])
    mods = ksn.fit_wgcna_v2(df_u, power=0, min_module_size=10)
    assert len(mods) == 50
    assert mods["module"].nunique() >= 2
    assert sn_cli_main(["--emit-versions-yml", str(tmp_path / "versions.yml")]) == 0
