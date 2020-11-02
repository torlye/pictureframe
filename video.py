#!/usr/bin/python3
import os
from fnmatch import fnmatch
import subprocess
import random
import re
import sys

search_dir='/media'
extensions = ['mkv', 'mp4', 'm4v', 'mov', 'mpg', 'mpeg', 'avi', 'vob']

def printTemp():
	subprocess.call(['cat', '/sys/class/thermal/thermal_zone0/temp'])
	subprocess.call(['vcgencmd', 'measure_temp'])

def playVideo(filepath):
	print('Video: ' + filepath)
	filename=os.path.basename(filepath)
	omxparams=['omxplayer', '--blank', '--nodeinterlace', '-n', '-1']
	omxparams.append('--stats')
	if ('_LB' in filename or '_LBPB' in filename):
		omxparams.extend(['--aspect-mode', 'fill'])
	#print omxparams
	omxparams.append(filepath)
	return subprocess.call(omxparams)

filelist=[]
if len(sys.argv) > 1:
	print('Searching directory ' + sys.argv[1])
	search_dir=sys.argv[1]

for path, subdirs, files in os.walk(search_dir):
	for name in files:
		for ext in extensions:
			if fnmatch(name.lower(), '*.'+ext):
				filepath = os.path.join(path, name)
				print(filepath)
				filelist.append(filepath)
				break

print('Found ' + str(len(filelist)) + ' files')

if len(filelist) == 0:
	sys.exit(0)

while True:
	filepath=random.choice(filelist)
	playVideo(filepath)
