# katana-splicenet (`v2.3.0`) — KatanaAS Suite

[![CI](https://github.com/Taratype0/katana-splicenet/actions/workflows/ci.yml/badge.svg)](https://github.com/Taratype0/katana-splicenet/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

KatanaAS pure-Python count-debiased ExcessBioVar + Tukey bicor + Signed TOM bulk alternative co-splicing network and module discovery.

## CLI Quickstart
```bash
pip install git+https://github.com/Taratype0/katana-splicenet.git

katana-splicenet --usage psi_matrix.tsv --samples samples.tsv --support counts.tsv --annotation event2gene.tsv --gmt pathways.gmt --output-dir ./splicenet_out
```

---

## KatanaAS Standalone Alternative Splicing Suite
| Package | Scope | Repository |
| :--- | :--- | :--- |
| **`katana-splicetrace`** | Bulk RBP regulator discovery, mature-mRNA motif & ORF/NMD/domain consequence tracing | [Taratype0/katana-splicetrace](https://github.com/Taratype0/katana-splicetrace) |
| **`katana-splicenet`** | Bulk count-debiased `ExcessBioVar` + Signed TOM co-splicing module networks | [Taratype0/katana-splicenet](https://github.com/Taratype0/katana-splicenet) |
| **`katana-sc-splicetrace`** | Smart-seq3 single-cell RBP discovery, motif & ORF/NMD tracing, and PSI modeling | [Taratype0/katana-sc-splicetrace](https://github.com/Taratype0/katana-sc-splicetrace) |
| **`katana-sc-splicenet`** | Smart-seq3 single-cell Hybrid-Manifold co-splicing module discovery | [Taratype0/katana-sc-splicenet](https://github.com/Taratype0/katana-sc-splicenet) |
