#!/usr/bin/python3
import time
import os
import subprocess
import sys
import select
import signal
import RPi.GPIO as GPIO

BUTTON_GPIO = 10
countdown = 20
selection = 0
menuitems = ['Photos', 'Videos', 'Weather']
scripts = ['photo.py', 'video.py', 'weather.py']

def printMenu():
	os.system('clear')
	for x in range(3):
		print(('\u25BA' if x == selection else ' ') + ' ' + menuitems[x])
	print('')
	print('Selection option will start in: '+str(countdown))

def button_pressed_callback(channel):
	global selection
	selection = (selection + 1) % len(menuitems)
	printMenu()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(BUTTON_GPIO, GPIO.RISING, callback=button_pressed_callback, bouncetime=200)

while countdown > 0:
	printMenu()
	time.sleep(1)
	countdown -= 1

GPIO.cleanup()
subprocess.run(['python3', scripts[selection]])