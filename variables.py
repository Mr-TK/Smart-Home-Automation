import os
import time
import RPi.GPIO as GPIO
ledDeviceInactPin = 40
ledDeviceInactPin1 = 16
pin1 = 11
pin2 = 8
hostname = "192.168.29.38"
host="127.0.0.1"
def setup():
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setwarnings(False)
    GPIO.setup(ledDeviceInactPin, GPIO.OUT)
    GPIO.setup(ledDeviceInactPin1, GPIO.OUT)
    GPIO.setup(Pin1, GPIO.OUT)
    GPIO.setup(pin2, GPIO.OUT)