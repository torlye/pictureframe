#!/usr/bin/python3
import time
import os
import subprocess
import sys
import select
import signal
import RPi.GPIO as GPIO
from config import config
import photo, video, weather

menuConfig = config['menu']
countdown = menuConfig.getint('timeout')
BUTTON_GPIO = menuConfig.getint('GPIO_button_pin')

selection = 0
menuitems = ['Photos', 'Videos', 'Weather']

def printMenu():
	os.system('clear')
	for x in range(3):
		print(('\u25BA' if x == selection else ' ') + ' ' + menuitems[x])
	print('')
	print('Selected option will start in: '+str(countdown))

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

if selection == 0:
	photo.start()
elif selection == 1:
	video.start()
else:
	weather.start()
