"""Standalone unit test for katana-cosplice."""
from __future__ import annotations

import numpy as np
import katana_cosplice as kcs


def test_pure_python_bicor_and_tom() -> None:
    assert kcs.__version__ == "2.2.0"
    rng = np.random.default_rng(42)
    x = rng.normal(size=(24, 16))
    bc = kcs.compute_tukey_bicor_matrix(x)
    tom = kcs.compute_signed_tom_from_bicor(bc, power=6)
    assert bc.shape == (24, 24)
    assert tom.shape == (24, 24)
    assert np.allclose(np.diag(tom), 1.0)
