import sqlite3 as lite
import sys

table = "moisture_data"

con = lite.connect('sensorsData.db')
with con:
    cur = con.cursor()
    cur.execute(f"INSERT INTO {table} VALUES(datetime('now'), 20.5, 30)")
    cur.execute(f"INSERT INTO {table} VALUES(datetime('now'), 25.8, 40)")
    cur.execute(f"INSERT INTO {table} VALUES(datetime('now'), 30.3, 50)")
