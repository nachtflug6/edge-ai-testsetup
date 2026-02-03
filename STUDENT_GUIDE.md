# Student Guide

## Overview
This guide describes the setup flow and the expected milestones for the Edge AI test bench prototype.

## Setup Milestones
1. **Hardware bring-up**
   - Verify Raspberry Pi 5 boots and has network access.
   - Connect a single sensor and confirm readings.
   - Optional: stream sensor data from ESP32 over UART or Wi‑Fi.

2. **Data acquisition MVP**
   - Log timestamped sensor data to CSV on the Pi.
   - Ensure the sampling rate is stable and documented.

3. **Control MVP**
   - Generate a simple motor pattern (step/ramp/sine).
   - Log the control signal alongside sensor readings.

4. **Bench integration**
   - Add a second motor and a known load.
   - Run short test cycles and validate logs.

5. **Analytics baseline**
   - Build baseline detection (z-score, isolation forest).
   - Evaluate with known anomalies.

6. **Edge AI demo**
   - Add embedding model on windowed signals.
   - Store embeddings in SQLite and run similarity search.

## Safety
- Always use an emergency stop for the motor bench.
- Do not run the motors unattended.
- Validate the load coupling before applying high speed.

## Repo Navigation
- Raspberry Pi code: [pi/](pi/)
- Firmware: [firmware/](firmware/)
- Analytics: [analysis/](analysis/)
- DB schema and tools: [db/](db/)

## Logging Conventions
- All timestamps should be in ISO 8601 UTC.
- Log a single sample per row with a `sequence_id`.
- Include `run_id` and `pattern_id` for experiment grouping.

## Deliverables
- Working acquisition + control scripts on the Pi.
- One dataset with a known anomaly scenario.
- A baseline anomaly detection report.
- A similarity search demo using stored embeddings.
