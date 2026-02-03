"""Simple CSV logger for sensor data (placeholder).

Replace `read_sensor()` with actual sensor reads.
"""

from __future__ import annotations

import csv
import time
from datetime import datetime, timezone
from pathlib import Path

OUTPUT_DIR = Path("data/raw")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def read_sensor() -> float:
    # TODO: replace with actual sensor read
    return 0.0


def main(sample_hz: float = 50.0, duration_s: float = 10.0) -> None:
    run_id = datetime.now(timezone.utc).strftime("run_%Y%m%dT%H%M%SZ")
    out_file = OUTPUT_DIR / f"{run_id}.csv"

    interval = 1.0 / sample_hz
    end_time = time.time() + duration_s
    sequence_id = 0

    with out_file.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "sequence_id", "sensor_value"])

        while time.time() < end_time:
            timestamp = datetime.now(timezone.utc).isoformat()
            value = read_sensor()
            writer.writerow([timestamp, sequence_id, value])
            sequence_id += 1
            time.sleep(interval)


if __name__ == "__main__":
    main()
