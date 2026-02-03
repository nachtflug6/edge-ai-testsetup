"""Quick look plot for a single run (placeholder)."""

from __future__ import annotations

import csv
from pathlib import Path

try:
    import matplotlib.pyplot as plt
except Exception:  # pragma: no cover
    plt = None


def load_csv(path: Path):
    timestamps = []
    values = []
    with path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            timestamps.append(row["timestamp"])
            values.append(float(row["sensor_value"]))
    return timestamps, values


def main():
    if plt is None:
        raise SystemExit("matplotlib not installed")

    sample_files = list(Path("data/samples").glob("*.csv"))
    if not sample_files:
        raise SystemExit("No sample data in data/samples")

    ts, values = load_csv(sample_files[0])
    plt.plot(values)
    plt.title(f"Quicklook: {sample_files[0].name}")
    plt.xlabel("Sample")
    plt.ylabel("Sensor Value")
    plt.show()


if __name__ == "__main__":
    main()
