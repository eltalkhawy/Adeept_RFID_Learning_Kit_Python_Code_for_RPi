#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

pins = (11, 12, 13)  # pins is a dict

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location

GPIO.setup(pins, GPIO.OUT)   # Set pins' mode is output
GPIO.output(pins, GPIO.HIGH) # Set pins to high(+3.3V) to off led


try:
	while True:
                request = raw_input("Enter RGB in decimal (Ex: 001)-->>"):                
                if(len(request) == 3):
                        GPIO.output(11, int(request[0]))
                        GPIO.output(12, int(request[1]))
                        GPIO.output(13, int(request[2]))
                        
except KeyboardInterrupt:
	GPIO.output(pins, GPIO.HIGH)    # Turn off all leds
	GPIO.cleanup()

