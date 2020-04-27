import sqlite3 as lite
import sys

table = "moisture_data"

con = lite.connect('sensorsData.db')
with con:
    cur = con.cursor()
    command = f'DROP TABLE IF EXISTS {table};'
    cur.execute(command)
    command = f'CREATE TABLE {table}(timestamp DATETIME, temp NUMERIC, hum NUMERIC);'
    print(command)
    print(cur.execute(command))
