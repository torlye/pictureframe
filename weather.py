#!/usr/bin/python3
import subprocess

interval = 10*60
location = 'Norway/Oslo/Oslo/Oslo'

def showMeteogram():
	try:
		wgetProc = subprocess.run(['wget', '-NqO', '-', 'https://www.yr.no/place/'+location+'/meteogram.png'], stdout=subprocess.PIPE)
		subprocess.run(['fim', '-aqi', '--no-history'], input=wgetProc.stdout, timeout=interval)
	except subprocess.TimeoutExpired:
		pass

print('Showing meteogram for '+location+', refreshing every '+str(interval)+' seconds')

while True:
	showMeteogram()
