#!/usr/bin/python3
import sys
import subprocess
import signal
from config import config
import shutdown

photoConfig = config['photo']
interval = photoConfig.getint('interval')
search_dir = photoConfig.get('searchDir')

def showPhoto(filepath):
	try:
		p = subprocess.Popen(['fim', '-q', '--no-history', '--random', '-R', '--autozoom', filepath])
		p.wait(timeout=interval)
	except subprocess.TimeoutExpired:
		p.send_signal(signal.SIGINT)
		pass

if len(sys.argv) > 1:
	search_dir=sys.argv[1]

print('Starting slideshow from directory '+search_dir)

while True:
	showPhoto(search_dir)
