import sqlite3

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done BOOLEAN DEFAULT 0
)
""")

conn.commit()
conn.close()
print(" Base de données créée avec succès.")
