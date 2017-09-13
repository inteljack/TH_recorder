import pigpio
import DHT22
import time
import datetime

# Sensor connected to Raspberry Pi 3 pin 4
DHT_PIN = 4
LED_PIN = 17

# How long to wait between measurements.
FREQUENCY_SEC = 3

pi = pigpio.pi()

s = DHT22.sensor(pi, DHT_PIN, LED_PIN)
s.trigger()

# delay time for pi to retrive data from the sensor
time.sleep(0.1)

# print datetime.datetime.now(), 'Temp={0:3.2f}*C  Humidity={1:0.1f}%'.format(s.temperature()/1., s.humidity()/1.)
print datetime.datetime.now()
print 'Temp=', s.temperature(), '*C'
print 'Humidity=', s.humidity(), '%'

s.cancel()
