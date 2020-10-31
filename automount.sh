#!/bin/bash

if [ -e /dev/mmcblk0p3 ]
then
	mount -o ro,noatime /dev/mmcblk0p3 /media/mmcblk0p3
fi

if [ -e /dev/sda1 ]
then
	mount -o ro,noatime /dev/sda1 /media/sda1
fi

if [ -e /dev/sdb1 ]
then
	mount -o ro,noatime /dev/sdb1 /media/sdb1
fi

if [ -e /dev/sdc1 ]
then
	mount -o ro,noatime /dev/sdc1 /media/sdc1
fi

if [ -e /dev/sdd1 ]
then
	mount -o ro,noatime /dev/sdd1 /media/sdd1
fi

