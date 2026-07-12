import sqlite3

DB_NAME = "bmi.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bmi_records(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            weight REAL NOT NULL,
            height REAL NOT NULL,
            bmi REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def insert_record(name, weight, height, bmi, category, date):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO bmi_records
        (name, weight, height, bmi, category, date)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, weight, height, bmi, category, date))

    conn.commit()
    conn.close()


def get_records():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, weight, height, bmi, category, date
        FROM bmi_records
        ORDER BY id DESC
    """)

    records = cursor.fetchall()

    conn.close()

    return records


def get_statistics():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
        COUNT(*),
        AVG(bmi),
        MAX(bmi),
        MIN(bmi)
        FROM bmi_records
    """)

    stats = cursor.fetchone()

    conn.close()

    return stats