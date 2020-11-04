#!/usr/bin/python3
import time
import os
import subprocess
import sys
import select
import signal
import RPi.GPIO as GPIO

BUTTON_GPIO = 16
countdown = 20
selection = 0
menuitems = ['Photos', 'Videos', 'Weather']
scripts = ['photo.py', 'video.py', 'weather.py']

def printMenu():
    os.system('clear')
    for x in range(3):
        print(('\u25BA' if x == selection else ' ') + ' ' + menuitems[x])
    print('')
    print('Selection option will start in: '+str(countdown))

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def button_pressed_callback(channel):
    selection = (selection + 1) % len(menuitems)

def timeout_input(prompt, timeout=1, default=""):
    inputs, outputs, errors = select.select([sys.stdin], [], [], timeout)
    return (0, sys.stdin.readline().strip()) if inputs else (-1, default)

GPIO.setmode(GPIO.BCM)    
GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(BUTTON_GPIO, GPIO.FALLING, callback=button_pressed_callback, bouncetime=200)

while countdown > 0:
    printMenu()
    time.sleep()
    #inp, text = timeout_input("")
    #if (inp == 0):
    #    button_pressed_callback()
    countdown -= 1

subprocess.run(['python3', script[selection]])