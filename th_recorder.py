import Adafruit_DHT
import time
import datetime

# Sensor connected to Raspberry Pi 3 pin 4
DHT_PIN = 17

# Type of Adafruit_DHT sensor(DHT11, DHT22, or AM2302)
DHT_TYPE = Adafruit_DHT.DHT22

# How long to wait between measurements.
FREQUENCY_SEC = 3

while True:

	humidity, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
	# Skip to the next reading if a valid measurement couldn't be taken.
	# This might happen if the CPU is under a lot of load and the sensor
	# can't be reliably read (timing is critical to read the sensor).

	if humidity is None or temp is None:
		time.sleep(2)
		continue

	print datetime.datetime.now(), 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temp, humidity)

	time.sleep(FREQUENCY_SEC)
