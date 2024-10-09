import sqlite3
import os

def setup_database():
    if not os.path.exists('voice-assistant/db'):
        os.makedirs('voice-assiatant/db')

    db_file = os.path.join('voice-assistant/db', 'data.db')

    conn = sqlite3.connect(db_file)
    conn.execute('''
            CREATE TABLE IF NOT EXISTS names (
                id INTEGER PRIMARY KEY,
                user_name TEXT NOT NULL,
                bot_name TEXT NOT NULL
            )
        ''')
    conn.commit()
    return conn

def add_names(conn, user_name, bot_name):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO names (user_name, bot_name) VALUES (?, ?)', (user_name, bot_name))
    conn.commit()

def get_user_name(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT user_name FROM names LIMIT 1')
    return cursor.fetchone()
    
def get_assistant_name(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT bot_name FROM names LIMIT 1')
    return cursor.fetchone()
