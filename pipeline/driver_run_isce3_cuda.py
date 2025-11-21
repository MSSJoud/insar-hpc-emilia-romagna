#!/usr/bin/env python
"""
High-level driver for the CUDA ISCE3 pipeline.

Right now this is a minimal, but functioning, skeleton:
- reads a YAML config
- runs a few named steps
- logs timing to logs/timing_cuda.json

You can later replace the `print(...)` blocks with real ISCE3 commands.
"""

import argparse
from pathlib import Path

import yaml

from utils_io_timing import timed_step


def run_isce3_cuda(config_path: Path) -> None:
    # Load config
    with open(config_path, "r") as f:
        cfg = yaml.safe_load(f)

    backend = cfg.get("backend", "cuda")
    if backend != "cuda":
        raise ValueError(f"Config backend must be 'cuda', got {backend!r}")

    timing_log = Path(cfg.get("timing_log", "logs/timing_cuda.json"))

    # --- STEP 1: pair selection / baselines (placeholder) ---
    with timed_step("step1_pair_selection", timing_log):
        # TODO: call your real pair selection or use a precomputed list.
        print("Running pair selection (placeholder) ...")

    # --- STEP 5: co-registration + resampling + IFG + geocoding (placeholder) ---
    with timed_step("step5_coreg_resample_ifg_geocode", timing_log):
        # TODO: replace with actual ISCE3-CUDA workflow calls.
        print("Running ISCE3 CUDA coreg/IFG/geocode (placeholder) ...")

    # --- STEP 10: SBAS / time-series (placeholder) ---
    with timed_step("step10_sbas_time_series", timing_log):
        # TODO: later you can call a MintPy/Dolphin script here.
        print("Running SBAS time-series (placeholder) ...")

    print(f"Finished CUDA pipeline. Timing log: {timing_log}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run ISCE3 CUDA pipeline.")
    parser.add_argument(
        "--config",
        required=True,
        help="Path to YAML config file (e.g., configs/config_insar_cuda.yaml)",
    )
    args = parser.parse_args()

    run_isce3_cuda(Path(args.config))


if __name__ == "__main__":
    main()
