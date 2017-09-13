import Adafruit_DHT as dht
import time
import datatime

# Sensor connected to Raspberry Pi 3 pin 4
DHT_PIN = 4

# Type of Adafruit_DHT sensor(DHT11, DHT22, or AM2302)
DHT_TYPE = Adafruit_DHT.DHT22

# How long to wait between measurements.
FREQUENCY_SEC = 30

def th_recorder():
	humidity, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
	print datetime.datetime.now() + 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temp, humidity)

while True:
	th_recorder()
	time.sleep(FREQUENCY_SEC)
