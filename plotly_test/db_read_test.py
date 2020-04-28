import sqlite3
import sys


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
        :param db_file: database file
        :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def get_last_num_readings(conn, table, num):
    """
    Query the last 'num' readings
    """

    cur = conn.cursor()
    cur.execute(f"SELECT temp hum FROM {table} LIMIT {num}")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    table = "moisture_data"
    db = "/home/pi/Projects/MoistureSensor/sensorsData.db"

    conn = create_connection(db)
    with conn:
        get_last_num_readings(conn, table, 100)
