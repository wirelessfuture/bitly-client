import sqlite3

DATABASE = 'history.db'

def get_conn():
    return sqlite3.connect(DATABASE)

def close_conn(conn):
    if conn:
        conn.close()

def insert(data):
    conn = get_conn()
    values = (data['unix_timestamp'], data['url_before'], data['url_after'])
    conn.execute("INSERT INTO history VALUES (?, ?, ?)", values)
    conn.commit()
    close_conn(conn)

# Builds the initial in memory db and inserts the table
# This re-builds the table each time the server is started for demo purposes
def build_db():
    conn = get_conn()
    try:
        conn.execute("CREATE TABLE history (unix_timestamp text, url_before text, url_after text)")
    except sqlite3.OperationalError:
        conn.execute("DROP TABLE history")
        conn.execute("CREATE TABLE history (unix_timestamp text, url_before text, url_after text)")
    close_conn(conn)