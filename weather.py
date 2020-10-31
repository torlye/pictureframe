#!/usr/local/bin/python

import os
from fnmatch import fnmatch
import subprocess
import random
import re
import sys


interval = 10*60
location = 'Norway/Oslo/Oslo/Oslo'


def showPhoto(filepath):
	return subprocess.call(['fim', '-q', '--no-history', '--autozoom', '-c', 'sleep \"'+ str(interval) + '\";quit;', filepath])

def getMeteogram():
	subprocess.call(['wget', '-N', 'https://www.yr.no/place/'+location+'/meteogram.png'])

print('Showing meteogram for '+location+', refreshing every '+str(interval)+' seconds')

while True:
	getMeteogram()
	showPhoto('meteogram.png')
