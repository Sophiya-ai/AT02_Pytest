import sqlite3


# memory - Прописывая вместо названия файла базы данных значение memory, данные будут сохраняться не на диске,
# а только в оперативной памяти и только во время работы программы
def init_db():
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    age INTEGER)''')

    return conn


def add_user(conn, name, age):
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO users (name, age) VALUES (?, ?)''', (name, age))
    conn.commit()


def get_user(conn, name):
    cur = conn.cursor()
    cur.execute('''
    SELECT * FROM users WHERE name = ?''', (name,))
    return cur.fetchone()
