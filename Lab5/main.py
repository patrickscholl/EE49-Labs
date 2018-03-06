from machine import Pin
from board import LED
from time import sleep

led = Pin(LED, mode=Pin.OUT)
led(1)
from network import WLAN, STA_IF
from network import mDNS
import time

wlan = WLAN(STA_IF)
wlan.active(True)
if not wlan.isconnected():
	wlan.connect('thwireless', 'blue&gold', 5000)

for i in range(10):
	if not wlan.isconnected():
		print("Waiting for network connection...")
		time.sleep(1)
	else:
		break

print("WiFi Connected at", wlan.ifconfig()[0])

try:
    hostname = 'BOSERBOIS'
    mdns = mDNS(wlan)
    mdns.start(hostname, "MicroPython REPL")
    mdns.addService('_repl', '_tcp', 23, hostname)
    print("Advertised locally as {}.local".format(hostname))
except OSError:
    print("Failed starting mDNS server - already started?")

#start telnet server for remote login
from network import telnet

print("start telnet server")
telnet.start(user='User', password='telnet password ...')

# fetch NTP time

from ina219 import INA219
from machine import I2C
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

from mqttclient import MQTTClient 
from time import sleep
from plotclient import PlotClient
from machine import deepsleep
#set up broker
TS_CHANNEL_ID = '436309'
TS_WRITE_KEY = 'HRHIBUDP4FBOK88A'
BROKER = 'mqtt.thingspeak.com'
USER = ''
PWD = ''
mqtt = MQTTClient(BROKER)
topic = "channels/" + TS_CHANNEL_ID + "/publish/" + TS_WRITE_KEY
values = VoltageRead()
v = values[0]
i = values[1]
sleep(0.3)
message = "field1={}&field2={}".format(v, i)
print("Publishing message {}, {}".format(v, i))
mqtt.publish(topic, message)
mqtt.disconnect()
led(0)
deepsleep(10000)