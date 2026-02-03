"""Motor control pattern generator (placeholder).

Replace `send_control()` with actual motor control interface.
"""

from __future__ import annotations

import math
import time
from dataclasses import dataclass


@dataclass
class PatternConfig:
    duration_s: float = 10.0
    sample_hz: float = 50.0
    amplitude: float = 1.0


def send_control(value: float) -> None:
    # TODO: replace with actual motor control command
    _ = value


def sine_pattern(cfg: PatternConfig) -> None:
    interval = 1.0 / cfg.sample_hz
    start = time.time()
    while time.time() - start < cfg.duration_s:
        t = time.time() - start
        value = cfg.amplitude * math.sin(2.0 * math.pi * t / cfg.duration_s)
        send_control(value)
        time.sleep(interval)


if __name__ == "__main__":
    sine_pattern(PatternConfig())
