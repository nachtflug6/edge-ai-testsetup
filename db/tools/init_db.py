"""Initialize SQLite database with schema."""

from __future__ import annotations

import sqlite3
from pathlib import Path

SCHEMA_PATH = Path(__file__).resolve().parents[1] / "schema" / "schema.sql"
DB_PATH = Path("db") / "edge_ai.db"


def main() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.executescript(SCHEMA_PATH.read_text())
    print(f"Initialized: {DB_PATH}")


if __name__ == "__main__":
    main()
