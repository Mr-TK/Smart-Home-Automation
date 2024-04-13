import os
import time
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import variables as var
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("bit.project")

 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    inMsg = str(msg.payload)[2:-1]
    print(msg.topic+" "+inMsg)
    #print(ID.deiceDetector(var.hostname))

    if inMsg == "on":
        var.setup()
        GPIO.setwarnings(False)
        print("Switch on the light")
        GPIO.output(var.ledDeviceInactPin,GPIO.HIGH)
        time.sleep(2)

    elif inMsg == "off":
        var.setup()
        GPIO.setwarnings(False)
        print("Switch off the light")
        GPIO.output(var.ledDeviceInactPin,GPIO.LOW)
        print("DONE")
    else:
        print("Send a valid instruction")

# Create an MQTT client and attach our routines to it.
if __name__ == "__main__":
    try:
        client = mqtt.Client()
        client.on_connect = on_connect()
        client.on_message = on_message
         
        client.connect("test.mosquitto.org", 1883, 60)
        client.loop_forever()
    except KeyboardInterrupt:
        print("PROGRAM END Successfully!")
    finally:
        GPIO.cleanup()

        