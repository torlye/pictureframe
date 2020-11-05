#!/usr/bin/python3
import configparser
from pathlib import Path
import os

filePath = os.path.join(Path.home(), 'pictureframe-config')

try:
	with open(filePath) as f:
		print('Config file exists')
except FileNotFoundError:
	config = configparser.ConfigParser()
	config['DEFAULT'] = { 
		'searchDir': '/media',
		'GPIO_button_pin': str(10)
	}
	config['menu'] = {}
	config['menu']['timeout'] = str(15)
	config['photo'] = {}
	config['photo']['interval'] = str(60*60)
	config['shutdown'] = {}
	config['video'] = {}
	config['weather'] = {}
	config['weather']['interval'] = str(15*60)
	config['weather']['location'] = 'Norway/Oslo/Oslo/Oslo'
	
	with open(filePath, 'w') as configfile:
		config.write(configfile)
	pass

config = configparser.ConfigParser()
config.read(filePath)