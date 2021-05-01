import requests
import time
import board
import busio
import adafruit_ahtx0
from simple_pid import PID
pid = PID(Kp=20.0, Ki=2.0, Kd=0.0, setpoint=25, sample_time=5.00, output_limits=(18, 30))
tempC = 25.0
tempCO = 25.0
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_ahtx0.AHTx0(i2c)
while True:
    tempCO = tempC
    tempM = sensor.temperature
    tempCs = pid(tempM)
    tempC = round(tempCs)
    if tempCO != tempC:
        urlMain = "http://192.168.137.100/ac"
        tempText = str(tempC)
        URL = urlMain + tempText
        r = requests.get(url = URL)
    print("Temp-TempCon-Kp-Ki,%0.1f,%d" % (sensor.temperature,tempC))
    time.sleep(10)
