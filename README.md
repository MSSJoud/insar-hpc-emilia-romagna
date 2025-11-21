# Operational InSAR at Scale – Emilia–Romagna HPC Benchmark

This repository accompanies the manuscript:

> Mehdi S.S. Joud, "Operational InSAR at Scale: Reproducible HPC Pipeline Benchmarking for Sentinel-1 and SWIN-Based Groundwater Inference over Emilia–Romagna", submitted to IEEE Transactions on Geoscience and Remote Sensing (TGRS).

The goal is to provide a **reproducible, end-to-end MT-InSAR processing chain** for Sentinel-1 IW data over the Emilia–Romagna region and to enable **hardware-to-hardware performance comparisons** between CPU-only and CUDA-enabled backends.

## Contents

- `environments/` – Conda environment definitions for:
  - ISCE3 CPU build (`conda_insar_cpu.yml`)
  - ISCE3 CUDA build (`conda_insar_cuda.yml`)
  - MintPy / SBAS post-processing (`conda_mintpy.yml`)
- `configs/` – AOI geometry, SBAS settings, and example path configuration for the AAU Strato cluster.
- `pipeline/` – Python drivers for:
  - Valid pair selection and baseline graph construction
  - Running the ISCE3 CPU and CUDA chains
  - Running SBAS / MintPy time-series inversion
  - Timing and logging utilities
- `slurm/` – Slurm job scripts for single-node and multi-node (strong/weak scaling) experiments, and SBAS runs.
- `benchmark_slice/` – Metadata and example lists for the fixed benchmark subset used in the paper.
- `docs/` – Instructions to reproduce the main tables and figures.

## Quick start (conceptual)

1. **Create environment** (example for CUDA build):
   ```bash
   conda env create -f environments/conda_insar_cuda.yml
   conda activate insar_cuda
