import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        dbname="dbname",
        user="username",
        password="password",
        host="db"
    )
    conn.autocommit = True
    return conn

def init_db():
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute('''
        CREATE TABLE IF NOT EXISTS app_user (
            id SERIAL PRIMARY KEY,
            username VARCHAR(150) NOT NULL,
            password VARCHAR(150) NOT NULL
        )''')
        cur.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            content TEXT NOT NULL
        )''')
    conn.close()

if __name__ == '__main__':
    init_db()
