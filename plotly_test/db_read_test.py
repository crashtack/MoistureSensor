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


def get_last_num_rows(conn, table, num):
    """
    Query the last 'num' readings
    """

    cur = conn.cursor()
    cur.execute(f"SELECT timestamp, temp, hum FROM {table} ORDER BY timestamp DESC LIMIT {num}")

    rows = cur.fetchall()
    return rows

def create_plot_data(rows):
    timestamp = []
    temp = []
    hum = []

    for row in rows:
        timestamp.append(row[0])
        temp.append(row[1])
        hum.append(row[2])
        print(row)

    return timestamp, temp, hum

def test():
    print("test")


def main():
    table = "moisture_data"
    db = "/home/pi/Projects/MoistureSensor/sensorsData.db"

    conn = create_connection(db)
    with conn:
        rows = get_last_num_rows(conn, table, 10)

    create_plot_data(rows)


if __name__ == '__main__':
    main()
