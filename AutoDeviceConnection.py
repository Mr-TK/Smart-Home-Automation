#!/usr/bin/env python3
########################################################################
# Filename    : NetworkDeviceDetector.py
# Description : This program will detect the avilability of a device in the WiFi network
# Author      : Epsilon Delta
# modification: 2022/06/23
########################################################################
import os
import RPi.GPIO as GPIO
import variables as var
def deiceDetector(host = var.host):
    response = os.system("ping -c 1 " + host)
    if response == 0:
        pingstatus = "Active"
        #GPIO.output(ledDeviceActPin,GPIO.HIGH)
        GPIO.output(var.ledDeviceInactPin,GPIO.HIGH)
                
    else:
        pingstatus = "Inactive"
        #GPIO.output(ledDeviceActPin,GPIO.LOW)
        GPIO.output(var.ledDeviceInactPin,GPIO.LOW)
    print (pingstatus)
    
            
def loop():
    try:
        while True:
            deiceDetector(var.hostname)
            var.time.sleep(1)
    except KeyboardInterrupt:
        print("PROGRAM END Successfully!")
    #finally:
     #   mylcd.lcd_clear()
      #  GPIO.cleanup()

if __name__=='__main__':
    var.setup()
    loop()
