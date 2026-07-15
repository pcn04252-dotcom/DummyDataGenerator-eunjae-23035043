import sqlite3
from contextlib import contextmanager
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "app.db"

_SCHEMA = """
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    quantity INTEGER NOT NULL
);
"""


@contextmanager
def get_connection(db_path=DB_PATH):
    if str(db_path) != ":memory:":
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    try:
        conn.execute(_SCHEMA)
        conn.commit()
        yield conn
    finally:
        conn.close()


def insert_items(conn: sqlite3.Connection, items: list[tuple[str, int]]) -> int:
    conn.executemany("INSERT INTO items (name, quantity) VALUES (?, ?)", items)
    conn.commit()
    return len(items)
