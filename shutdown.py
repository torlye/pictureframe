import os
import sys
import time
import RPi.GPIO as GPIO
from config import config

conf = config['shutdown']
BUTTON_GPIO = conf.getint('GPIO_button_pin')
time1 = sys.maxsize

def button_pressed_in(channel):
	global time1
	time1 = time.time()

def button_pressed_out(channel):
	if time.time() - time1 > 5:
		GPIO.cleanup()
		os.system("sudo shutdown -h now")
		quit()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(BUTTON_GPIO, GPIO.RISING, callback=button_pressed_in, bouncetime=200)
GPIO.add_event_detect(BUTTON_GPIO, GPIO.FALLING, callback=button_pressed_out, bouncetime=200)
