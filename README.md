# katana-cosplice (`v2.2.0`)

[![CI](https://github.com/Taratype0/katana-cosplice/actions/workflows/ci.yml/badge.svg)](https://github.com/Taratype0/katana-cosplice/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

100% Pure-Python (zero R dependency required) **Count-Debiased Excess Biological Variance (`ExcessBioVar`) + Exact Tukey Biweight Midcorrelation (`bicor`) + Single-Block Signed TOM** co-splicing network, module eigengene (`ME`), hub-splicing (`kME`), and gene-level pathway enrichment engine.

---

## Key Capabilities
- **Count-Debiased `ExcessBioVar` Selection**: Subtracts exact binomial read-depth sampling noise `$\psi(1-\psi)/n$` before ranking variable splicing events, eliminating low-coverage variance inflation.
- **Exact Pure-Python `bicor` + Signed TOM**: Reproduces Langfelder & Horvath Tukey biweight midcorrelation (`maxPOutliers = 0.10`), soft-threshold scale-free topology selection, single-block Signed TOM, `dynamicTreeCut` hybrid module detection, and eigengene merging (`ARI = 1.000` parity without requiring R or `WGCNA`).
- **Gene-Deduplicated Module Pathway Enrichment**: Maps splicing modules to unique host genes against `.gmt` gene sets (GO/Reactome/Hallmark) with hypergeometric BH-FDR control, preventing multi-exon genes from inflating pathway significance.

---

## Installation

```bash
# Install directly from GitHub
pip install git+https://github.com/Taratype0/katana-cosplice.git

# Or install pre-built wheel from GitHub Releases
pip install https://github.com/Taratype0/katana-cosplice/releases/download/v2.2.0/katana_cosplice-2.2.0-py3-none-any.whl
```

---

## Standalone CLI Usage

```bash
katana-cosplice \
  --usage psi_matrix.tsv \
  --samples sample_metadata.tsv \
  --support junction_counts.tsv \
  --annotation event_to_gene.tsv \
  --gmt pathways.gmt \
  --output-dir ./cosplice_out
```

---

## Python API Usage

```python
import numpy as np
import katana_cosplice as kcs

bc = kcs.compute_tukey_bicor_matrix(psi_matrix)
tom = kcs.compute_signed_tom_from_bicor(bc, power=6)
```

---

## Katana Standalone Package Suite
| Package | Scope | Repository |
| :--- | :--- | :--- |
| **`katana-motiftrace`** | Bulk RBP regulator discovery & mature-mRNA motif tracing | [Taratype0/katana-motiftrace](https://github.com/Taratype0/katana-motiftrace) |
| **`katana-cosplice`** | Bulk count-debiased ExcessBioVar + Signed TOM co-splicing networks | [Taratype0/katana-cosplice](https://github.com/Taratype0/katana-cosplice) |
| **`katana-sc-motiftrace`** | Smart-seq3 single-cell RBP discovery, motif tracing & PSI modeling | [Taratype0/katana-sc-motiftrace](https://github.com/Taratype0/katana-sc-motiftrace) |
| **`katana-sc-cosplice`** | Smart-seq3 single-cell Hybrid-Manifold co-splicing module discovery | [Taratype0/katana-sc-cosplice](https://github.com/Taratype0/katana-sc-cosplice) |
