#!/usr/bin/python3

import os
from fnmatch import fnmatch
import subprocess
import random
import re
import sys


interval = 5
location = 'Norway/Oslo/Oslo/Oslo'


def showPhoto(filepath):
	try:
		return subprocess.run(['fim', '-q', '--no-history', '--autozoom', filepath], timeout=30)
	except subprocess.TimeoutExpired:
		pass

def getMeteogram():
	subprocess.call(['wget', '-N', 'https://www.yr.no/place/'+location+'/meteogram.png'])

print('Showing meteogram for '+location+', refreshing every '+str(interval)+' seconds')


while True:
	getMeteogram()
	showPhoto('meteogram.png')
