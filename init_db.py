import sqlite3

DB_NAME = "tasks.db"

conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    due_date TEXT,
    done INTEGER NOT NULL DEFAULT 0
)
""")

conn.commit()
conn.close()
print("Base de données initialisée :", DB_NAME)

