import sqlite3


def init_db():
    conn = sqlite3.connect('user.db')
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    age INTEGER)''')
    return conn


def add_user(conn, name, age):
    cur = conn.cursor()
    cur.execute('''INSERT INTO users (name, age) VALUES (?, ?)''', (name, age))
    conn.commit()


def get_user(conn, name):
    cur = conn.cursor()
    cur.execute('''
    SELECT * FROM users WHERE name = ?''', (name,))
    output = cur.fetchone()
    return output[1], output[2]
