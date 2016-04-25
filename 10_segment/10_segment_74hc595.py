#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

RCLK  = 12
SRCLK = 13
SDI   = 11

code_Row = [0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0a,0x0b,0x0c,0x0d,0x0e,0x0f]


def print_msg():
	print 'Program is running...'
	print 'Please press Ctrl+C to end the program...'

def setup():
	GPIO.setmode(GPIO.BOARD)    # Number GPIOs by its physical location
	GPIO.setup(SDI, GPIO.OUT)
	GPIO.setup(RCLK, GPIO.OUT)
	GPIO.setup(SRCLK, GPIO.OUT)
	GPIO.output(SDI, GPIO.LOW)
	GPIO.output(RCLK, GPIO.LOW)
	GPIO.output(SRCLK, GPIO.LOW)

def hc595_in(dat):
		GPIO.output(SDI, dat)
		GPIO.output(SRCLK, GPIO.HIGH)
		time.sleep(0.00001)
		GPIO.output(SRCLK, GPIO.LOW)

def hc595_out():
	GPIO.output(RCLK, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(RCLK, GPIO.LOW)


def loop():
	while True:
		for i in range(0, len(code_Row)):
			hc595_in(code_Row[i])
			hc595_out()
			print "code: ", code_Row[i]
			time.sleep(1)

		for i in range(len(code_Row)-1, -1, -1):
			hc595_in(code_Row[i])
			hc595_out()
			print "code: ", code_Row[i]
			time.sleep(1)

def destroy():   # When program ending, the function is executed. 
	GPIO.cleanup()

if __name__ == '__main__':   # Program starting from here 
	print_msg()
	setup() 
	try:
		loop()  
	except KeyboardInterrupt:  
		destroy()  
