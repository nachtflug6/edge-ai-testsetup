# Preprocessing Guide

## Goals
Prepare raw logs for anomaly detection and embedding pipelines.

## Steps
1. **Validate**
   - Remove corrupted rows.
   - Ensure monotonic timestamps.

2. **Resample / Synchronize**
   - Align sensors to a common sampling rate.

3. **Windowing**
   - Window size: 1–5 seconds
   - Overlap: 50% (default)

4. **Normalization**
   - Per-sensor z-score or min-max scaling.

5. **Labeling (optional)**
   - Annotate known anomalies (load spikes, stalls).

## Output
- Save as CSV or Parquet in data/processed/.
- Keep a small sample in data/samples/ for demos.
