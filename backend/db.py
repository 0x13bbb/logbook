import sqlite3
from datetime import datetime
from contextlib import contextmanager
from typing import Optional, Dict, Any

class Database:
    def __init__(self, db_name: str = 'tracker.db'):
        self.db_name = db_name

    @contextmanager
    def get_connection(self):
        conn = sqlite3.connect(self.db_name)
        try:
            yield conn
        finally:
            conn.close()

    def init_db(self):
        with self.get_connection() as conn:
            c = conn.cursor()

            # Create mood table
            c.execute('''
                CREATE TABLE IF NOT EXISTS mood (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    score INTEGER CHECK (score >= 1 AND score <= 5),
                    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            # Create habits table 
            c.execute('''
                CREATE TABLE IF NOT EXISTS habits (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    completed TEXT CHECK (completed IN ('yes', 'no', 'unable')),
                    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            conn.commit()

    def insert_mood(self, name: str, score: int) -> Optional[Dict[str, Any]]:
        with self.get_connection() as conn:
            c = conn.cursor()
            
            try:
                c.execute(
                    'INSERT INTO mood (name, score) VALUES (?, ?)', 
                    (name, score)
                )
                mood_id = c.lastrowid
                
                c.execute(
                    'SELECT id, name, score, time FROM mood WHERE id = ?',
                    (mood_id,)
                )
                mood = c.fetchone()
                
                conn.commit()
                
                return {
                    'id': mood[0],
                    'name': mood[1], 
                    'score': mood[2],
                    'time': mood[3]
                }
                
            except sqlite3.Error:
                conn.rollback()
                return None

# Create a singleton instance
db = Database()