#!/usr/bin/env python
import time
import json
from pathlib import Path
from contextlib import contextmanager

@contextmanager
def timed_step(step_name: str, log_file: Path | None = None):
    t0 = time.time()
    yield
    t1 = time.time()
    dt = t1 - t0
    print(f"[TIMING] {step_name}: {dt/3600:.3f} h")

    if log_file is not None:
        log_file = Path(log_file)
        log_file.parent.mkdir(parents=True, exist_ok=True)
        if log_file.exists():
            data = json.loads(log_file.read_text())
        else:
            data = {}
        data.setdefault(step_name, []).append(dt)
        log_file.write_text(json.dumps(data, indent=2))
