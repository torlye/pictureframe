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
	if GPIO.input(BUTTON_GPIO): # rising edge
		time1 = time.time()
	else # falling edge
		if time.time() - time1 > 5: # button was held for 5s
			GPIO.cleanup()
			os.system("sudo shutdown -h now")
			quit()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(BUTTON_GPIO, GPIO.BOTH, callback=button_pressed, bouncetime=200)
