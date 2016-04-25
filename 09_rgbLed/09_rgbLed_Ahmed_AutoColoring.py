#!/usr/bin/env python
import RPi.GPIO as GPIO
import time



pins = {'pin_R':11, 'pin_G':12, 'pin_B':13}  # pins is a dict

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location

for i in pins:                          # Initilize all pins to output and turn off by outputing HIGH
	GPIO.setup(pins[i], GPIO.OUT)   # Set pins' mode is output
	GPIO.output(pins[i], GPIO.HIGH) # Set pins to high(+3.3V) to off led

p_R = GPIO.PWM(pins['pin_R'], 1000)     # set Frequece to 1KHz
p_G = GPIO.PWM(pins['pin_G'], 1000)     # set Frequece to 1KHz
p_B = GPIO.PWM(pins['pin_B'], 1000)     # set Frequece to 1KHz

p_R.start(0)                     # Start PWM output, Duty Cycle = 0
p_G.start(0)                     # Start PWM output, Duty Cycle = 0
p_B.start(0)                     # Start PWM output, Duty Cycle = 0



try:
	while True:
		for r_value in range(0, 101, 4):   # Increase duty cycle: 0~100 for R Led
                        for g_value in range(0, 101, 4):   # Increase duty cycle: 0~100 for G Led
                                for b_value in range(0, 101, 4):   # Increase duty cycle: 0~100 for B Led
                                        p_R.ChangeDutyCycle(r_value)     # Change duty cycle for R Led
                                        p_G.ChangeDutyCycle(g_value)     # Change duty cycle for G Led
                                        p_B.ChangeDutyCycle(b_value)     # Change duty cycle for B Led
                                        time.sleep(0.05)
                p_R.ChangeDutyCycle(0)     # Turn off R Led 
                p_G.ChangeDutyCycle(0)     # Turn off G Led
                p_B.ChangeDutyCycle(0)     # Turn off B Led
                time.sleep(0.25)
                p_R.ChangeDutyCycle(100)     # Turn on R Led 
                p_G.ChangeDutyCycle(100)     # Turn on G Led
                p_B.ChangeDutyCycle(100)     # Turn on B Led
                time.sleep(0.25)
                p_R.ChangeDutyCycle(0)     # Turn off R Led 
                p_G.ChangeDutyCycle(0)     # Turn off G Led
                p_B.ChangeDutyCycle(0)     # Turn off B Led
                time.sleep(0.25)
                p_R.ChangeDutyCycle(100)     # Turn on R Led 
                p_G.ChangeDutyCycle(100)     # Turn on G Led
                p_B.ChangeDutyCycle(100)     # Turn on B Led
                time.sleep(0.25)
                p_R.ChangeDutyCycle(0)     # Turn off R Led 
                p_G.ChangeDutyCycle(0)     # Turn off G Led
                p_B.ChangeDutyCycle(0)     # Turn off B Led
                time.sleep(0.25)

                for r_value in range(100, -1, -4):   # Increase duty cycle: 0~100 for R Led
                        for g_value in range(100, -1, -4):   # Increase duty cycle: 0~100 for G Led
                                for b_value in range(100, -1, -4):   # Increase duty cycle: 0~100 for B Led
                                        p_R.ChangeDutyCycle(r_value)     # Change duty cycle for R Led
                                        p_G.ChangeDutyCycle(g_value)     # Change duty cycle for G Led
                                        p_B.ChangeDutyCycle(b_value)     # Change duty cycle for B Led
                                        time.sleep(0.10)
                                        
                        
except KeyboardInterrupt:
	for i in pins:                          # All pins off by outputing HIGH
                GPIO.output(pins[i], GPIO.HIGH) # Set pins to high(+3.3V) to off led    # Turn off all leds
	GPIO.cleanup()

