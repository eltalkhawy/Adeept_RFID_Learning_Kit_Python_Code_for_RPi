#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

RCLK  = 12
SRCLK = 13
SDI   = 11

bcd_data = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
hex_data = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,0x77,0x7f,0x39,0x3f,0xf9,0x71]


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
	for bit in range(0, 8):	
		GPIO.output(SDI, 0x80 & (dat << bit))
		GPIO.output(SRCLK, GPIO.HIGH)
		time.sleep(0.00001)
		GPIO.output(SRCLK, GPIO.LOW)

def hc595_out():
	GPIO.output(RCLK, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(RCLK, GPIO.LOW)


def loop():
	while True:
		for i in range(0, len(hex_data)):
			hc595_in(hex_data[i])
			hc595_out()
			print "Print: ", bcd_data[i]
			time.sleep(0.5)

		for i in range(len(hex_data)-1, -1, -1):
			hc595_in(hex_data[i])
			hc595_out()
			time.sleep(0.5)

def destroy():   # When program ending, the function is executed. 
	GPIO.cleanup()

if __name__ == '__main__':   # Program starting from here 
	print_msg()
	setup() 
	try:
		loop()  
	except KeyboardInterrupt:  
		destroy()  
