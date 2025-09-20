from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
DB = "tasks.db"

# Fonction pour récupérer toutes les tâches
def get_tasks():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return tasks

@app.route("/")
def index():
    tasks = get_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    title = request.form["title"]
    if title:
        conn = sqlite3.connect(DB)
        conn.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
        conn.commit()
        conn.close()
    return redirect("/")

@app.route("/done/<int:task_id>")
def done(task_id):
    conn = sqlite3.connect(DB)
    conn.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete(task_id):
    conn = sqlite3.connect(DB)
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
