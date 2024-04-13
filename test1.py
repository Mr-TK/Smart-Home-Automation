import os
import time
import RPi.GPIO as GPIO
pin = 37
GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT) 
GPIO.output(pin,GPIO.HIGH)
time.sleep(20)
GPIO.output(pin,GPIO.LOW)