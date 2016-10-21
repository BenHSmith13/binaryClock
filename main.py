import RPi.GPIO as GPIO
import time
import sched
import datetime

s = sched.scheduler(time.time, time.sleep)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# hours
GPIO.setup(12, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
# minutes
GPIO.setup(8, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
# Seconds
GPIO.setup(23, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

def tick(sc):
	current_time = datetime.datetime.now().time()
	secs = format(current_time.second, '#06b')
	mins = format(current_time.minute, '#06b')
	hours = format(current_time.hour, '#04b')
	second_pins = [4, 17, 18, 27, 22, 23]
	minute_pins = [24, 10, 9, 25, 11, 8]
	hour_pins = [7, 5, 6, 12]
	print current_time.hour, " : ", current_time.minute, " : ", current_time.second
	for index, pin in enumerate(second_pins):
		if secs[-index - 1] == '1':
			GPIO.output(pin, GPIO.HIGH)
		else:
			GPIO.output(pin, GPIO.LOW)
	for index, pin in enumerate(minute_pins):
		if mins[-index - 1] == '1':
			GPIO.output(pin, GPIO.HIGH)
		else:
			GPIO.output(pin, GPIO.LOW)
	for index, pin in enumerate(hour_pins):
		if hours[-index - 1] == '1':
			GPIO.output(pin, GPIO.HIGH)
		else:
			GPIO.output(pin, GPIO.LOW)
	s.enter(1, 1, tick, (s,))


s.enter(1, 1, tick, (s,))
s.run()


