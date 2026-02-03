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

## Development Workflow (Recommended)

### Option 1: VS Code Remote SSH (Recommended)
This is the most efficient workflow for Pi development:

1. **Install VS Code Remote SSH extension** on your laptop/desktop.
2. **Connect to Pi**:
   - Press `F1` → "Remote-SSH: Connect to Host"
   - Enter: `pi@edge-ai-pi.local` (or Pi's IP)
3. **Open project folder** on the Pi directly in VS Code.
4. **Benefits**:
   - Edit code with full IDE features (autocomplete, linting).
   - Run scripts directly on Pi hardware.
   - Debug with breakpoints.
   - Access Pi's file system seamlessly.
5. **Install Python extension** in the remote session for best experience.

### Option 2: Local Development + rsync
If you prefer local editing:
- Edit code on your laptop.
- Use `rsync` or `scp` to sync changes to Pi.
- SSH into Pi to run scripts.
- Less convenient but works without Remote SSH.

### Option 3: Direct Development on Pi
- Connect monitor/keyboard to Pi.
- Use `nano`, `vim`, or desktop IDE on Pi.
- Works but less ergonomic for larger projects.

### Recommended: Remote SSH
For this project, **VS Code Remote SSH is strongly recommended** because:
- You get full IDE support while running on real hardware.
- Sensor/GPIO access requires Pi hardware.
- Debugging is much easier.
- You can quickly iterate on scripts and see results.

## Raspberry Pi Reset + Setup (Recommended)
If the Pi has been used for other projects, start from a clean image to avoid hidden config issues.

### Recommended Credentials (Private Repo)
For consistency across the project:
- **Username**: `pi`
- **Password**: `edgeai2026`
- **Hostname**: `edge-ai-pi`

These credentials should be set during imaging (see below).

### 1) Re-image the Raspberry Pi
- Use **Raspberry Pi Imager** to flash **Raspberry Pi OS (64-bit)**.
- In advanced options (gear icon):
  - Enable SSH
  - Set hostname: `edge-ai-pi`
  - Set username: `pi`
  - Set password: `edgeai2026`
- Add Wi‑Fi credentials if needed.

### 2) First Boot Checks
- Update the system:
  - `sudo apt update && sudo apt upgrade -y`
- Set locale/timezone if needed.
- Reboot after updates.

### 3) Install Core Tools
- Python and essentials:
  - `sudo apt install -y python3 python3-pip python3-venv git sqlite3`
- Optional utilities:
  - `sudo apt install -y i2c-tools python3-smbus` (I2C sensors)
  - `sudo apt install -y libatlas-base-dev` (numeric libs)

### 4) Enable Interfaces (if needed)
- Enable I2C/SPI/UART via `raspi-config`:
  - `sudo raspi-config` → Interface Options

### 5) Create Project Environment
- Clone repo and create virtual environment:
  - `python3 -m venv .venv`
  - `source .venv/bin/activate`
  - `pip install -U pip`

### 6) Verify Logging Script
- Run a short test:
  - `python pi/acquisition/logger.py`
- Confirm output file in `data/raw/`.

### 7) Initialize SQLite DB
- Run:
  - `python db/tools/init_db.py`
- Confirm `db/edge_ai.db` exists.

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
