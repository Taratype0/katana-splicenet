"""Unit tests for katana-splicenet v2.3.0."""
from __future__ import annotations

import numpy as np
import katana_splicenet as ksn


def test_splicenet_bicor_tom_and_soft_threshold() -> None:
    assert ksn.__version__ == "2.3.0"
    rng = np.random.default_rng(42)
    x = rng.normal(size=(40, 15))
    bc = ksn.compute_tukey_bicor_matrix(x)
    pwr = ksn.pick_soft_threshold_v2(bc)
    tom = ksn.compute_signed_tom_from_bicor(bc, power=pwr)
    assert tom.shape == (40, 40)
    assert np.allclose(np.diag(tom), 1.0)
