#!/usr/bin/python3

import subprocess
import sys

interval=10

def showPhoto(filepath):
	try:
		return subprocess.call(['fim', '-q', '--no-history', '--random', '-R', '--autozoom', filepath], timeout=interval)
	except subprocess.TimeoutExpired:
		pass

search_dir='/media'


if len(sys.argv) > 1:
	search_dir=sys.argv[1]

print('Starting slideshow from directory '+search_dir)

while True:
	exit = showPhoto(search_dir)
	#print(exit)
