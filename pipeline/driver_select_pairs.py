#!/usr/bin/env python
import argparse
import json
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(
        description="Select valid Sentinel-1 pairs and build SBAS settings."
    )
    parser.add_argument("--config", required=True, help="YAML config with paths/AOI")
    parser.add_argument("--output", required=True, help="Output SBAS settings JSON")
    args = parser.parse_args()

    # TODO: read AOI and acquisition list; here we just create a placeholder
    sbas_settings = {
        "description": "SBAS settings placeholder – fill with your real graph.",
        "max_baseline": 200,       # m
        "max_temporal": 200,       # days
        "pairs_file": "benchmark_slice/example_ifg_list.txt",
    }

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(sbas_settings, indent=2))
    print(f"SBAS settings written to {out_path}")

if __name__ == "__main__":
    main()
