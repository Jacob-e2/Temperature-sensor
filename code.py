import time
import board
import adafruit_ahtx0
import busio
from adafruit_datetime import datetime

i2c = busio.I2C(scl=board.GP1, sda=board.GP0) #Configures which ports on the microcontroller are being used.
sensor = adafruit_ahtx0.AHTx0(i2c)

settings = open("/Settings.txt", "r")
interval = settings.readline() #Variable used to store the recording interval in seconds, loaded from text file.
print(interval)

while True:   #Main while loop ensures that the temeprature recordings are repeated.
    temperature = sensor.temperature
    log = open("/Temperature.txt", "a") #Writes he temperature data to the log.
    log.write(str(temperature) + "\n")
    log.close()
    time.sleep(int(interval))
