import sqlite3

conn = sqlite3.connect(
    "history.db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS history(
id INTEGER PRIMARY KEY AUTOINCREMENT,
language TEXT,
code TEXT,
report TEXT
)
""")

conn.commit()