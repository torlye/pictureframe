#!/bin/bash

if [ -e /dev/sda1 ]
then
	mount -o ro,noatime /dev/sda1 /mnt/sda1
fi

if [ -e /dev/sdb1 ]
then
	mount -o ro,noatime /dev/sdb1 /mnt/sdb1
fi

if [ -e /dev/sdc1 ]
then
	mount -o ro,noatime /dev/sdc1 /mnt/sdc1
fi

if [ -e /dev/sdd1 ]
then
	mount -o ro,noatime /dev/sdd1 /mnt/sdd1
fi

