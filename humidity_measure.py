import Adafruit_DHT
import variables as var
import RPi.GPIO as GPIO

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
ledDeviceInactPin =35

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        if(humidity >= 92.0):
            var.setup()
            GPIO.setwarnings(False)
            print("Switch on the light")
            GPIO.output(var.ledDeviceInactPin,GPIO.HIGH)
        elif humidity < 92.0:
            var.setup()
            GPIO.output(var.ledDeviceInactPin,GPIO.LOW)
            
        
    else:
        print("Failed to retrieve data from humidity sensor")