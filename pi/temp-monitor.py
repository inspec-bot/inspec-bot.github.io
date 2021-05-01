import requests
import time
import board
import busio
import adafruit_ahtx0
from simple_pid import PID

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_ahtx0.AHTx0(i2c)

while True:
    print("Temp: %0.1f C" % sensor.temperature)
    time.sleep(5)
