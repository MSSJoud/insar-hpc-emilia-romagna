#!/usr/bin/env python
import argparse
import yaml
from pathlib import Path
from utils_io_timing import timed_step

def run_isce3_cuda(config):
    # This is a high-level orchestrator; you plug in your actual ISCE3 calls here.
    timing_log = Path(config.get("timing_log", "logs/timing_cuda.json"))

    with timed_step("step1_pair_selection", timing_log):
        # In your real code you may read a precomputed pair list
        pass

    with timed_step("step5_coreg_resample_ifg_geocode", timing_log):
        # Example: call your ISCE3 wrapper / workflow scripts here
        # os.system("isce3_tops_app.py ...")  # replace with real commands
        pass

    with timed_step("step10_sbas_inversion", timing_log):
        # Later you can move SBAS here or call MintPy driver
        pass

def main():
    parser = argparse.ArgumentParser(description="Run ISCE3 CUDA pipeline.")
    parser.add_argument("--config", required=True, help="Path to YAML config")
    args = parser.parse_args()

    with open(args.config, "r") as f:
        config = yaml.safe_load(f)

    assert config.get("backend") == "cuda", "Config backend must be 'cuda'."
    run_isce3_cuda(config)

if __name__ == "__main__":
    main()
