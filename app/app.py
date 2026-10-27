import os
import psycopg2
from flask import Flask

app = Flask(__name__)


def get_conn():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        dbname="testdb",
        user="postgres",
        password=os.getenv("DB_PASSWORD", "pass12345"),
    )


@app.route("/")
def index():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM students")
    rows = cur.fetchall()
    conn.close()
    items = "<br>".join(f"{r[0]}: {r[1]}" for r in rows)
    return f"<h1>App + DB</h1>{items}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)