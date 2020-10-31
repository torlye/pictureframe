#!/usr/local/bin/python

import subprocess
import sys

interval=30

def showPhoto(filepath):
	print('Starting slideshow from directory '+filepath)
	return subprocess.call(['fim', '-q', '--no-history', '--random', '--slideshow', str(interval), '-R', filepath])

search_dir='/mnt'


if len(sys.argv) > 1:
	search_dir=sys.argv[1]

showPhoto(search_dir)
