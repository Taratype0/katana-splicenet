# katana-splicenet (`v2.3.2`) — KatanaAS Suite

[![CI](https://github.com/Taratype0/katana-splicenet/actions/workflows/ci.yml/badge.svg)](https://github.com/Taratype0/katana-splicenet/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Part of the **KatanaAS** 4-package Bulk & Single-Cell (Smart-seq3) alternative splicing suite. Supports **two first-class invocation modes**:
1. **Standalone Python Package & CLI** (`pip install` -> Python API / `katana-splicenet` / `splicenet` / `python -m katana_splicenet`)
2. **Nextflow `nf-core` DSL2 Module & Subworkflow** (`process KATANA_SPLICENET` with native `--emit-versions-yml`)

---

## Mode 1: Standalone Package Installation & Invocation

### Installation
```bash
# Direct one-line wheel install from GitHub Release
pip install https://github.com/Taratype0/katana-splicenet/releases/download/v2.3.2/katana_splicenet-2.3.2-py3-none-any.whl

# Or install from source with server Numba acceleration & Matplotlib visualization extras
pip install "git+https://github.com/Taratype0/katana-splicenet.git#egg=katana-splicenet"
```

### CLI Usage (`katana-splicenet`, `splicenet`, or `python -m katana_splicenet`)
```bash
katana-splicenet \
  --usage psi_matrix.tsv \
  --samples sample_metadata.tsv \
  --support total_junction_counts.tsv \
  --annotation event_to_gene.tsv \
  --gmt m5.go.bp.gmt \
  --power 0 \
  --output-dir ./splicenet_out
```

### Python API Usage
```python
import pandas as pd
import katana_splicenet as ksn

masked, audit = ksn.unit_robust_audit_v2(usage_df, samples_df, support_df)
selected, _ = ksn.select_events_v2(masked, audit, feature_cap=5000)
modules = ksn.fit_wgcna_v2(selected, power=0, min_module_size=20)
```

---

## Mode 2: Nextflow `nf-core` DSL2 Integration

Every KatanaAS CLI natively implements `--emit-versions-yml versions.yml --process-name "${task.process}"` and SLURM multi-core `--threads ${task.cpus}`.

```groovy
include { KATANA_SPLICENET } from './modules/local/katana_splicenet/main'
```

---

## KatanaAS 4-Package Suite Architecture

| Package | Version | Modality | Responsibility |
| :--- | :---: | :---: | :--- |
| **[katana-splicetrace](https://github.com/Taratype0/katana-splicetrace)** | `v2.4.3` | Bulk RNA-seq | RBP discovery (`169` RBPs / `621` PWMs), mature-mRNA motifs, `SpliceNet` bridge & `GTF/UniProt` ORF/NMD + 5 plots |
| **[katana-splicenet](https://github.com/Taratype0/katana-splicenet)** | `v2.3.2` | Bulk RNA-seq | Pure-Python `ExcessBioVar` + Adaptive Scale-Free Signed TOM co-splicing network & GO enrichment |
| **[katana-sc-splicetrace](https://github.com/Taratype0/katana-sc-splicetrace)** | `v2.4.1` | Smart-seq3 SC | Single-cell RBP discovery, mature-mRNA motifs, `SC-SpliceNet` bridge & `GTF/UniProt` ORF/NMD + 5 plots |
| **[katana-sc-splicenet](https://github.com/Taratype0/katana-sc-splicenet)** | `v2.2.2` | Smart-seq3 SC | Hybrid-Manifold `ExcessBioVar` + Empirical-Bayes Fisher-z shrunk Signed TOM single-cell modules |
