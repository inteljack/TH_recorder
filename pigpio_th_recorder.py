import pigpio
import DHT22
import time
import datetime

# Sensor connected to Raspberry Pi 3 pin 4
DHT_PIN = 17
LED_PIN = 4

# How long to wait between measurements.
FREQUENCY_SEC = 3

pi = pigpio.pi()

# filename = 'data.csv'
# try:
# 	file = open(filename, 'a')
# except IOError:
# 	file = open(filename, 'w')

while True:
	s = DHT22.sensor(pi, DHT_PIN)
	s.trigger()
	# delay time for pi to retrive data from the sensor, running trigger()
	time.sleep(0.2)

	h = s.humidity()
	t = s.temperature()

	# verify if reading is valid
	if h is None or t is None:
		print 'invalid reading, retrying...'
		time.sleep(2)
		continue

	timestamp = datetime.datetime.now()
	print timestamp, 'Temp={0:0.1f}*C, Humidity={1:0.1f}%'.format(t/ 1., h/1.)


	# capture sensor data every FREQUENCY_SEC
	time.sleep(FREQUENCY_SEC)
	s.cancel()
