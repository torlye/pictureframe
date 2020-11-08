#!/usr/bin/python3
import subprocess
import os
import signal
from config import config
import shutdown

weatherConfig = config['weather']
interval = weatherConfig.getint('interval')
location = weatherConfig.get('location')

def showMeteogram():
	try:
		wgetProc = subprocess.run(['wget', '-NqO', '-', 'https://www.yr.no/place/'+location+'/meteogram.png'], stdout=subprocess.PIPE)
		p = subprocess.Popen(['fim', '-c', "scale 1.6; pan 'left'", '-qi', '--no-history'], stdin=subprocess.PIPE, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
		p.communicate(wgetProc.stdout, timeout=interval)
	except subprocess.TimeoutExpired:
		p.send_signal(signal.SIGINT)
		pass

def start():
	print('Showing meteogram for '+location+', refreshing every '+str(interval)+' seconds')
	shutdown.startProcess()

	while True:
		showMeteogram()

if __name__ == '__main__':
	start()