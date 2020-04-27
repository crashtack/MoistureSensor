from datetime import datetime
import sqlite3 as lite
import sys
from time import sleep
from board import SCL, SDA
from adafruit_seesaw.seesaw import Seesaw
import busio


def log_data(con, table, data):
    with con:
        cur = con.cursor()
        cur.execute(f"INSERT INTO {table} VALUES(datetime('now'), {data['temp']}, {data['moisture']})")

def celsius_to_fahrenheit(deg_celsius):
    return 9.0/5.0 * deg_celsius + 32

def get_sensor_data(ss):
    moisture = ss.moisture_read()
    temp = celsius_to_fahrenheit(ss.get_temp())

    return {"moisture": moisture, "temp": temp}

if __name__ == '__main__':
    i2c_bus = busio.I2C(SCL, SDA)
    ss = Seesaw(i2c_bus, addr=0x36)
    db = "sensorsData.db"
    table = "moisture_data"
    con = lite.connect('sensorsData.db')

    while True:
        total_moisture = 0
        for i in range(50):
            data = get_sensor_data(ss)
            total_moisture += data['moisture']
            sleep(.1)
        data['moisture'] = total_moisture / 50
        print(f"Logging: {datetime.now()} : {data['moisture']} : {data['temp']:4.2f}")
        log_data(con, table, data)
        sleep(60)
