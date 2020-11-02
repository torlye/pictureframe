#!/usr/bin/python3
import subprocess
import os
import signal

interval = 10*60
location = 'Norway/Oslo/Oslo/Oslo'

def showMeteogram():
	try:
		wgetProc = subprocess.run(['wget', '-NqO', '-', 'https://www.yr.no/place/'+location+'/meteogram.png'], stdout=subprocess.PIPE)
		p = subprocess.Popen(['fim', '-aqi', '--no-history'], stdin=subprocess.PIPE, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
		p.communicate(wgetProc.stdout, timeout=interval)
	except subprocess.TimeoutExpired:
		p.send_signal(signal.SIGINT)
		pass

print('Showing meteogram for '+location+', refreshing every '+str(interval)+' seconds')

while True:
	showMeteogram()
