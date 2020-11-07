#!/usr/bin/python3
import os, subprocess
from config import config

conf = config['shutdown']
enabled = conf.getboolean('enabled')

def startProcess():
	if enabled:
		subprocess.Popen(['python3', os.path.join(os.path.split(os.path.realpath(__file__))[0], 'shutdownGpioMonitor.py')])