from ina219 import INA219
from machine import I2C, Pin
from board import SDA, SCL
import time
#setup I2C comms
i2c = I2C(id = 0, scl=Pin(SCL), sda = Pin(SDA), freq = 100000)
#connect to ina
print("Scanning I2C bus...")
print("I2C:", i2c.scan())
#configure ina
SHUNT_RESISTOR_OHMS = 0.1
ina = INA219(SHUNT_RESISTOR_OHMS, i2c)
ina.configure()
#define function to read desired data
def VoltageRead():
	v = ina.voltage()
	i = ina.current()
	p = ina.power()
	if i > 0:
		r = (v/i)*1000
	else:
		r = 0
	return [v, i, p, r]
# Set up MQTT and plotclient for use on ESP32
from mqttclient import MQTTClient 
from time import sleep
from plotclient import PlotClient
#set up broker
TS_CHANNEL_ID = '436309'
TS_WRITE_KEY = 'HRHIBUDP4FBOK88A'
BROKER = 'mqtt.thingspeak.com'
topic = "channels/" + TS_CHANNEL_ID + "/publish/" + TS_WRITE_KEY


# connect (from lecture slides)
print("Connecting to broker", BROKER, "...")
mqtt = MQTTClient(BROKER)

lastvalues = [1, 1, 1, 1]
while True:	
	values = VoltageRead()
	if abs(values[2]-lastvalues[2]) > 0.1*values[2]: # Just checking that the change is greater than 10%
		print("Publishing message = {}".format(values))
		v = values[0]
		i = values[1]
		message = "field1={}&field2={}".format(v, i)
		mqtt.publish(topic, message)
		lastvalues = values
		sleep(0.3)
	if values[3] > 8000: #Checks that the resistance is greater than 8000 and breaks the loop
		break


mqtt.disconnect()