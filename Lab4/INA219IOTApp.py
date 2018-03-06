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
BROKER = 'iot.eclipse.org'
USER = ''
PWD = ''
# connect (from lecture slides)
print("Connecting to broker", BROKER, "...")
mqtt = MQTTClient(BROKER, user = USER, password= PWD, ssl = True, )
mp = PlotClient(mqtt, session="BOSERBOIS_Plotter_2")

#name series
SERIES = 'power'
#publish series
mp.new_series(SERIES, 'R', 'P')
lastmessage = [1, 1, 1, 1]
while True:	
	message = VoltageRead()
	if abs(message[2]-lastmessage[2]) > 0.1*message[2]: # Just checking that the change is greater than 10%
		mp.data(SERIES, message[3], message[2])
		print("Publishing message = {}".format(message))
		lastmessage = message
		sleep(0.3)
	if message[3] > 8000: #Checks that the resistance is greater than 8000 and breaks the loop
		break


mp.save_series(SERIES)

mp.plot_series(SERIES, 
		filename="Power_Output.pdf", 
		xlabel="Resistance", 
		ylabel="Power", 
		title="Power vs Resistance")

mqtt.disconnect()