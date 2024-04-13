# Smart-Home-Automation

# Introduction-
With the help of this system it doesn’t matter where you are you can easily automate the electronic appliances of your home. It can also make decisions when it senses stormy weather outside it will       automatically switch off your electronic appliances and keep them safe. It works wirelessly. Through MQTT protocol we can send messages to the server. First, we send signals to the server then we fetch Details through the RaspberryPi. As per the signals, we trigger the relay, and then through the relay we can easily turn on or off the electronic appliances.  

# HardWares-
  Raspberry Pi
  Humidity Sensor DHT22
  5v Relay module
  Bread Board
  Connecting wires
  A small fan
  A light bulb
  
# Step By Step Guide-
 ## Setup MQTT Server: 
  Set up an MQTT server where your Raspberry Pi and other devices will connect to communicate. You can use popular MQTT brokers like Mosquitto or set up your own using software like Eclipse Paho.

 # Install Dependencies: 
  Make sure you have the necessary libraries installed on your Raspberry Pi. You'll need paho-mqtt for MQTT communication and RPi.GPIO for controlling GPIO pins.

 # Connect Relay to Raspberry Pi: 
  Connect a relay module to your Raspberry Pi. Typically, you'll connect it to a GPIO pin for control and to a power source for the devices you want to control.

 # Write Python Script: 
 Create a Python script on your Raspberry Pi that listens for MQTT messages and controls the relay accordingly. This script should use the paho-mqtt library to subscribe to a topic on the MQTT server and   the RPi.GPIO library to control the GPIO pin connected to the relay.

 # Set MQTT Parameters:
  Configure the script with the necessary MQTT parameters such as the server address, port, topic, and client ID.

 # Define Callback Functions:
 Define callback functions for MQTT events like connection and message reception. These functions should handle the logic for turning the relay ON or OFF based on the messages received.

 # Connect to MQTT Broker:
 Connect the script to the MQTT broker using the parameters configured earlier.

 # Start MQTT Loop: 
 Start the MQTT loop to listen for incoming messages indefinitely.


 # Send MQTT Messages:
 From your other devices or applications, publish MQTT messages to the topic subscribed by the Raspberry Pi script whenever you want to turn the relay ON or OFF.

 # Run the Script:
 Run the Python script on your Raspberry Pi. You should see it connect to the MQTT server and wait for incoming messages. When messages are received, it should control the relay accordingly.
  
