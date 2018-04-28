from network import WLAN, STA_IF
from network import mDNS
import time
#### TO DO: Add switching action based on user input
wlan = WLAN(STA_IF)
wlan.active(True)
if not wlan.isconnected():
	wlan.connect('EECS-PSK', 'Thequickbrown', 5000)

for i in range(30):
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


#### TO DO: Modify mqtt broker, get this publisher set up as a callback to a timer
#start telnet server for remote login
#from network import telnet

#print("start telnet server")
#telnet.start(user='User', password='telnet password ...')
#Set up pulissher node
from mqttclient import MQTTClient 
from time import sleep
from machine import deepsleep
#set up broker
BROKER = 'iot.eclipse.org'
USER = ''
PWD = ''
mqtt = MQTTClient(BROKER)
topic = 'BOSERBOIS/Project'
sleep(0.3)
print('Connecting to broker')

### TO DO: Set up the callback to record and actuate the servos at the same time, 
#also possibly figure out phased arrays

### TO DO: Include this in the other callback

from machine import Timer
from board import A10, A5, A8, A6
from machine import Pin, PWM
import machine
from math import sin, cos, pi
import time
DUTY = 3
pin1 = Pin(A8, mode=Pin.OUT)
pwm1 = PWM(pin1, 50, DUTY, 1)
pin2 = Pin(A5, mode=Pin.OUT)
pwm2 = PWM(pin2, 50, DUTY, 2)
##Used code from https://github.com/mithru/MicroPython-Examples/blob/master/08.Sensors/HC-SR04/ultrasonic.py to initialize pins

start = 0
end = 0
dist_cm = 0
trigpin = A10
Echopin = A6
trigger = Pin(trigpin, mode = Pin.OUT, pull = None)
trigger.value(0)
Echo = Pin(Echopin, mode = Pin.IN, pull = None)
phi = 0
theta = 0
pwm1.duty(6)
pwm2.duty(3)
philist = [90, 75, 60, 45, 30, 15, 0]
thetalist = [0, 7.5, 15, 22.5, 30, 37.5, 45, 52.5, 60, 67.5, 75]
i = 2
j = 4
def ping(timer):
	global i
	global j
	global trigger
	i_max = 13
	j_max = 15
	i_min = 7
	j_min = 5
	trigger.value(0) # Stabilize the sensor
	time.sleep_us(5)
	trigger.value(1)
	# Send a 10us pulse.
	time.sleep_us(10)
	trigger.value(0)
	try:
	    pulse_time = machine.time_pulse_us(Echo, 1, 30000)
	    distance_cm = pulse_time/58
	except OSError as ex:
	    if ex.args[0] == 110: # 110 = ETIMEDOUT
	        raise OSError('Out of range')
 	    raise ex
	r = distance_cm

	i += 1
	if i > i_max:
		i = i_min
		j+=1
	if j > j_max:
	 	j= j_min

	pwm1.duty(i)
	pwm2.duty(j)
	phi = philist[i-i_min]
	theta = thetalist[j-j_min]
	x = r*cos(theta*pi/180.0)*cos(phi*pi/180.0)
	y = r*cos(theta*pi/180.0)*sin(phi*pi/180.0)
	z = r*sin(theta*pi/180.0)
	message = "{:7.3f}, {:7.3f}, {:7.3f}".format(x, y, z)
	mqtt.publish(topic, message)

tim = Timer(3)
tim.init(period = 500, mode = tim.PERIODIC, callback = ping)

