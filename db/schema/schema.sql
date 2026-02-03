-- SQLite schema for sensor logs and embeddings

CREATE TABLE IF NOT EXISTS runs (
  run_id TEXT PRIMARY KEY,
  started_at TEXT NOT NULL,
  notes TEXT
);

CREATE TABLE IF NOT EXISTS samples (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  run_id TEXT NOT NULL,
  timestamp TEXT NOT NULL,
  sequence_id INTEGER NOT NULL,
  sensor_value REAL NOT NULL,
  control_value REAL,
  FOREIGN KEY (run_id) REFERENCES runs(run_id)
);

CREATE TABLE IF NOT EXISTS embeddings (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  run_id TEXT NOT NULL,
  window_start TEXT NOT NULL,
  window_end TEXT NOT NULL,
  vector BLOB NOT NULL,
  meta TEXT,
  FOREIGN KEY (run_id) REFERENCES runs(run_id)
);
