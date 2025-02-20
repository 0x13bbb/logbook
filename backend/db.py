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

            # Mood table
            c.execute('''
                CREATE TABLE IF NOT EXISTS mood (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    score INTEGER CHECK (score >= 1 AND score <= 5),
                    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            # Habits table 
            c.execute('''
                CREATE TABLE IF NOT EXISTS habits (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    completed TEXT CHECK (completed IN ('yes', 'no', 'unable')),
                    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            # Milestones table
            c.execute('''
                CREATE TABLE IF NOT EXISTS milestones (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    habit_name TEXT NOT NULL,
                    streak_target INTEGER NOT NULL,
                    reward TEXT NOT NULL
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

    def get_mood(self, name: str) -> Optional[Dict[str, Any]]:
        with self.get_connection() as conn:
            c = conn.cursor()

            try:
                c.execute(
                    'SELECT id, name, score, time FROM mood WHERE name = ?', 
                    (name,)
                )

                moods = c.fetchall()
                
                if not moods:
                    return None
                    
                return [
                    {
                        'id': mood[0],
                        'name': mood[1],
                        'score': mood[2], 
                        'time': mood[3]
                    }
                    for mood in moods
                ]
                    
            except sqlite3.Error:
                conn.rollback()
                return None

    def insert_habit(self, name: str, completed: str) -> Optional[Dict[str, Any]]:
        with self.get_connection() as conn:
            c = conn.cursor()
            
            try:
                c.execute(
                    'INSERT INTO habits (name, completed) VALUES (?, ?)', 
                    (name, completed)
                )
                habit_id = c.lastrowid
                
                c.execute(
                    'SELECT id, name, completed, time FROM habits WHERE id = ?',
                    (habit_id,)
                )
                habit = c.fetchone()
                
                conn.commit()
                
                return {
                    'id': habit[0],
                    'name': habit[1], 
                    'completed': habit[2],
                    'time': habit[3]
                }
                
            except sqlite3.Error:
                conn.rollback()
                return None
    
    def get_habits(self, name: str) -> Optional[Dict[str, Any]]:
        with self.get_connection() as conn:
            c = conn.cursor()

            try:
                c.execute(
                    'SELECT id, name, completed, time FROM habits WHERE name = ?', 
                    (name,)
                )

                moods = c.fetchall()
                
                if not moods:
                    return None
                    
                return [
                    {
                        'id': mood[0],
                        'name': mood[1],
                        'completed': mood[2], 
                        'time': mood[3]
                    }
                    for mood in moods
                ]
                    
            except sqlite3.Error:
                conn.rollback()
                return None

    def insert_milestone(self, habit_name: str, streak_target: int, reward: str) -> Optional[Dict[str, Any]]:
        with self.get_connection() as conn:
            c = conn.cursor()
            
            try:
                habits = self.get_habits(habit_name)
                if not habits:
                    return None
                
                c.execute(
                    'INSERT INTO milestones (habit_name, streak_target, reward) VALUES (?, ?, ?)',
                    (habit_name, streak_target, reward)
                )
                milestone_id = c.lastrowid
                
                c.execute(
                    'SELECT id, habit_name, streak_target, reward FROM milestones WHERE id = ?',
                    (milestone_id,)
                )
                milestone = c.fetchone()
                
                conn.commit()
                
                return {
                    'id': milestone[0],
                    'habit_name': milestone[1],
                    'streak_target': milestone[2],
                    'reward': milestone[3]
                }
                
            except sqlite3.Error:
                conn.rollback()
                return None
            
    def get_milestones(self, habit_name: str) -> Optional[Dict[str, Any]]:
        with self.get_connection() as conn:
            c = conn.cursor()

            try:
                c.execute(
                    'SELECT id, habit_name, streak_target, reward FROM milestones WHERE habit_name = ?',
                    (habit_name,)
                )

                milestones = c.fetchall()
                
                if not milestones:
                    return None
                    
                return [
                    {
                        'id': milestone[0],
                        'habit_name': milestone[1],
                        'streak_target': milestone[2],
                        'reward': milestone[3]
                    }
                    for milestone in milestones
                ]
                    
            except sqlite3.Error:
                conn.rollback()
                return None

db = Database()
db = Database()