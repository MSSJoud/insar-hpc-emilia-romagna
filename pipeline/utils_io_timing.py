#!/usr/bin/env python
import time
import json
from pathlib import Path
from contextlib import contextmanager


@contextmanager
def timed_step(step_name: str, log_file: str | Path | None = None):
    """Context manager to time a pipeline step and optionally log to JSON."""
    t0 = time.time()
    yield
    dt = time.time() - t0

    hours = dt / 3600.0
    print(f"[TIMING] {step_name}: {hours:.3f} h")

    if log_file is not None:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)

        if log_path.exists():
            data = json.loads(log_path.read_text())
        else:
            data = {}

        data.setdefault(step_name, []).append(dt)
        log_path.write_text(json.dumps(data, indent=2))
