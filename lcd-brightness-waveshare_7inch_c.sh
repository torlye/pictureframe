#!/bin/bash

if [[ $# -eq 0 ]];then
   echo "Please specify brightness (440-500)"
   exit 1
fi

echo "PWM brightness control for Waveshare 7 inch HDMI LCD (C)"
echo "Setting brightness $1"

gpio -g pwm 18 1024
gpio -g mode 18 pwm
gpio pwmc 1000
gpio -g pwm 18 $1
