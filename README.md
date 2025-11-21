# insar-hpc-emilia-romagna


# Operational InSAR at Scale – Emilia–Romagna HPC Benchmark
All materials for the InSAR + HPC benchmarking pipeline described in the TGRS paper: ISCE3 CPU/CUDA, SBAS/MintPy stage, Slurm scripts, configs, and benchmark slice metadata.

This repository accompanies the manuscript:

**Mehdi S. S. Joud**, *Operational InSAR at Scale: Reproducible HPC Pipeline Benchmarking for Sentinel-1 and SWIN-Based Groundwater Inference over Emilia–Romagna*, submitted to **IEEE Transactions on Geoscience and Remote Sensing (TGRS)**.

It provides a **fully reproducible, end-to-end MT-InSAR processing chain** for Sentinel-1 IW data and enables **hardware-to-hardware performance comparisons** across CPU-only and CUDA-accelerated backends using ISCE3 on the AAU Strato cluster.

---

## Contents
- `environments/` – Conda envs for ISCE3 CPU, ISCE3 CUDA, MintPy  
- `configs/` – AOI, SBAS settings, paths, masks  
- `pipeline/` – Python drivers for CPU/CUDA chains + SBAS  
- `slurm/` – Strong/weak scaling scripts  
- `benchmark_slice/` – Metadata for benchmark subset  
- `docs/` – Reproduction instructions  


---

## Quick Start

### 1. Create environment (example: CUDA build)
```bash
conda env create -f environments/conda_insar_cuda.yml
conda activate insar_cuda

### 2. Edit paths for your system
python pipeline/driver_run_isce3_cuda.py \
    --config configs/config_insar_cuda.yaml

### 3. Run ISCE3 pipeline (CUDA)
python pipeline/driver_run_isce3_cuda.py \
    --config configs/config_insar_cuda.yaml

### 4. Run SBAS / MintPy
python pipeline/driver_sbas_mintpy.py \
    --config configs/sbas_settings.json

### 5. For HPC experiments
Use the Slurm scripts in slurm/:
sbatch slurm/run_insar_cuda_strong_scaling.sbatch

## Citation

If you use this repository, please cite:
Joud, M. S. S. (2025).
Operational InSAR at Scale: Reproducible HPC Pipeline Benchmarking
for Sentinel-1 and SWIN-Based Groundwater Inference over Emilia–Romagna.
IEEE Transactions on Geoscience and Remote Sensing.

## And cite the repository:
https://github.com/MSSJoud/insar-hpc-emilia-romagna

## Acknowledgment

Pipeline design and benchmarking were performed on the AAU Strato (CLAAUDIA) HPC cluster.

