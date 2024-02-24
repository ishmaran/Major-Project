
import sqlite3
from datetime import datetime

def initialize_database():
    # Create a SQLite database connection and cursor
    conn = sqlite3.connect('plant_data.db')
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS plant_log (
            timestamp TEXT,
            plant_id INTEGER,
            disease_class INTEGER,
            pump_run_time TEXT
        )
    ''')
    conn.commit()

    return conn, cursor

def close_database_connection(conn):
    # Close the database connection
    conn.close()

def insert_record(cursor, plant_id, disease_class):
    # Record data in the database
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    pump_run_time = timestamp  # You may modify this based on your pump control logic

    cursor.execute('''
        INSERT INTO plant_log (timestamp, plant_id, disease_class, pump_run_time)
        VALUES (?, ?, ?, ?)
    ''', (timestamp, plant_id, disease_class, pump_run_time))
