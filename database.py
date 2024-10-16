import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    with conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS tasks (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          content TEXT NOT NULL
                      )''')
    conn.close()

if __name__ == '__main__':
    init_db()
