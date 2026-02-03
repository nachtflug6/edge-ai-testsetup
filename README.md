# Edge AI Test Bench (Dual-Motor) — Student Repo

This repository contains a practical, modular scaffold for prototyping a dual-motor test bench for anomaly detection and edge AI research. It is designed for Raspberry Pi 5 as the main controller, with optional ESP32 and Arduino-based prototypes.

## Problem Statement
The goal of this repository is to provide the **physical test platform** counterpart to the cluster-based benchmarking of edge log-to-vector under constraints. We need to validate, in a real environment, whether the algorithms and pipelines developed on the cluster actually work on **real sensor signals**. This test bench captures sensor data from controlled motor patterns and loads, runs edge AI to generate embeddings, and stores those vectors (plus metadata) in a lightweight vector-capable database for similarity search and anomaly analysis. The outcome should demonstrate that the end-to-end pipeline is feasible and reliable on real hardware.

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

## Repository Layout & Code Organization

### Where to Put Your Code

#### `/pi/` — Raspberry Pi Code
This is the **core runtime** for the test bench. All Pi-side logic goes here.

- **`pi/acquisition/`** — Sensor data logging
  - Add new loggers here (e.g., `logger_i2c.py`, `logger_adc.py`)
  - Each logger should write timestamped CSV to `data/raw/`
  - Include `run_id` and `sequence_id` in all logs

- **`pi/control/`** — Motor control patterns
  - Add pattern generators (e.g., `patterns_advanced.py`)
  - Each pattern should accept a config and output control signals
  - Log control signals alongside sensor data

- **`pi/config/`** — Configuration files
  - Add YAML/JSON configs for experiments
  - Keep sensor calibration constants here
  - Document all parameters

#### `/firmware/` — Microcontroller Code
For offloading sensors to ESP32/Arduino.

- **`firmware/esp32/`** — ESP32 sensor streaming
  - Add Arduino/PlatformIO sketches here
  - Stream data to Pi over UART/Wi‑Fi
  - Document pinouts in comments

- **`firmware/arduino/`** — Arduino actuator demos
  - Add simple motor/servo demos
  - Useful for testing before Pi integration

#### `/analysis/` — Offline Analysis
For exploration, visualization, and baseline models.

- **`analysis/scripts/`** — Python scripts
  - Add preprocessing scripts (windowing, resampling, filtering)
  - Add visualization scripts (plot patterns, spectrograms)
  - Add baseline anomaly detection (z-score, isolation forest)
  - Keep scripts modular and reusable

#### `/models/` — AI Models
For embedding and anomaly models.

- **`models/embedding/`** — Embedding models
  - Add trained models (ONNX, TFLite, PyTorch)
  - Include inference scripts
  - Document input/output shapes

- **`models/anomaly/`** — Anomaly detection models
  - Add baseline classifiers (pickled scikit-learn)
  - Add threshold configs
  - Include evaluation scripts

#### `/db/` — Database Layer
For persistent storage and vector search.

- **`db/schema/`** — SQLite schemas
  - Add SQL schema definitions
  - Include migration scripts
  - Document all tables and indexes

- **`db/tools/`** — DB utilities
  - Add import/export scripts
  - Add vector similarity search tools
  - Keep queries in dedicated scripts

#### `/data/` — Data Storage (Mostly Gitignored)
- **`data/raw/`** — Raw sensor logs (gitignored)
- **`data/processed/`** — Cleaned data (gitignored)
- **`data/samples/`** — Small demo datasets (tracked in git)

#### `/tests/` — Testing
- **`tests/unit/`** — Unit tests for parsing, preprocessing
- **`tests/integration/`** — End-to-end pipeline tests

#### `/scripts/` — Utility Scripts
- Add one-off utilities (sync logs, flash firmware, etc.)
- Keep these simple and well-documented

#### `/hardware/` — Hardware Documentation
- **`hardware/wiring/`** — Pinout diagrams, schematics
- **`hardware/bom/`** — Parts list with vendor links

#### `/docs/` — Project Documentation
- Decision logs, meeting notes, experiment protocols

### General Guidelines
- **Keep scripts focused**: One script = one task
- **Use relative imports**: Make code reusable
- **Document I/O**: Every script should document inputs/outputs
- **Config over hardcode**: Use YAML/JSON for parameters
- **Version control data**: Only commit small samples

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
