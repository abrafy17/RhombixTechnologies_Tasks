import sqlite3
import os

class Database:
    def __init__(self):
        pass
    
    def setup_database(self):
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

    def add_names(self, conn, user_name, bot_name):
        cursor = conn.cursor()
        cursor.execute('DELETE FROM names')
        cursor.execute('INSERT INTO names (user_name, bot_name) VALUES (?, ?)', (user_name, bot_name))
        conn.commit()

    def get_user_name(self, conn):
        cursor = conn.cursor()
        cursor.execute('SELECT user_name FROM names LIMIT 1')
        return cursor.fetchone()
        
    def get_assistant_name(self, conn):
        cursor = conn.cursor()
        cursor.execute('SELECT bot_name FROM names LIMIT 1')
        return cursor.fetchone()
