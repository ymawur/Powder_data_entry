import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DATABASE = 'ingredients.db'


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS ingredients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
            -- Add new columns here
        )
        """
    )
    conn.commit()
    conn.close()


@app.route('/')
def index():
    return render_template('ingredient_form.html')


@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    description = request.form.get('description')
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO ingredients (name, description) VALUES (?, ?)',
        (name, description)
    )
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    init_db()
    host = '0.0.0.0'
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)
