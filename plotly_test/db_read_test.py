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
    cur.execute(f"SELECT timestamp, temp, hum FROM {table} ORDER BY timestamp DESC LIMIT {num}")

    rows = cur.fetchall()

    timestamp = []
    temp = []
    hum = []
    
    for row in rows:
        timestamp.insert(-1, row[0])
        temp.insert(-1, row[1])
        hum.insert(-1, row[2])
        print(row)

    return timestamp, temp, hum


def main():
    table = "moisture_data"
    db = "/home/pi/Projects/MoistureSensor/sensorsData.db"

    conn = create_connection(db)
    with conn:
        timestamp, temp, hum = get_last_num_readings(conn, table, 10)

    print(f'hums: {hum}')


if __name__ == '__main__':
    main()
