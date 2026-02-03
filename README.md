# Edge AI Test Bench (Dual-Motor) — Student Repo

This repository contains a practical, modular scaffold for prototyping a dual-motor test bench for anomaly detection and edge AI research. It is designed for Raspberry Pi 5 as the main controller, with optional ESP32 and Arduino-based prototypes.

## Goals
- Provide a controlled environment for manipulating rotation patterns and loads.
- Collect synchronized sensor and control data.
- Enable repeatable anomaly-detection experiments.
- Provide a path to edge AI embedding + similarity search demos.

## Quickstart (MVP)
1. **Raspberry Pi bring-up**
   - Log a single sensor at a fixed rate (timestamped).
   - Store CSV locally.
2. **Control pattern**
   - Generate a simple motor control pattern (step/ramp/sine).
   - Log the control signal together with sensor data.
3. **Sanity checks**
   - Plot sensor vs. control for a quick correlation check.

## Repository Layout
- docs/ — diagrams, protocols, decision logs
- hardware/ — wiring, parts list
- firmware/ — microcontroller firmware (ESP32, Arduino)
- pi/ — Raspberry Pi control, acquisition, configs
- data/ — samples; raw/processed are gitignored
- analysis/ — scripts or notebooks for exploration
- models/ — embedding and anomaly models
- db/ — SQLite schema and tools
- tests/ — unit and integration tests
- scripts/ — utility scripts for syncing and flashing

## Recommended First Tests
1. Timestamped logging from a single sensor at fixed rate.
2. Single motor control with simple pattern and logging.
3. Correlate control vs sensor in a plot.
4. Introduce a known anomaly (e.g., load spike) and detect it.

## Edge AI + Similarity Search (Plan)
- Compute windowed embeddings (on Pi or offline).
- Store embeddings in SQLite with metadata.
- Run similarity queries to retrieve nearest neighbors.

## Safety
Do not run the motor bench unattended. Verify emergency stop and power cutoffs before each session.

## Next Steps
See [STUDENT_GUIDE.md](STUDENT_GUIDE.md) for detailed setup and task flow.
