#!/usr/bin/python3
import os
import sys
import time
import RPi.GPIO as GPIO
from config import config

conf = config['shutdown']
BUTTON_GPIO = conf.getint('GPIO_button_pin')
time1 = sys.maxsize

def button_pressed(channel):
	global time1
	if GPIO.input(BUTTON_GPIO):
		# Rising edge
		time1 = time.time()
	else:
		# Falling edge
		if time.time() - time1 > 3:
			# Button was held for 3s
			GPIO.cleanup()
			os.system("sudo shutdown -h now")
			quit()

isRunning = False

def startMonitoring():
	global isRunning
	if not isRunning:
		isRunning = True
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.add_event_detect(BUTTON_GPIO, GPIO.BOTH, callback=button_pressed, bouncetime=200)

if __name__ == '__main__':
	startMonitoring()
	while True:
		time.sleep(100)