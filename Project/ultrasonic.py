from board import A8, A6
from machine import Timer, Pin
import machine
import time
##Used code from https://github.com/mithru/MicroPython-Examples/blob/master/08.Sensors/HC-SR04/ultrasonic.py to initialize pins
start = 0
end = 0
dist_cm = 0
trigpin = A8
Echopin = A6
trigger = Pin(trigpin, mode = Pin.OUT, pull = None)
trigger.value(0)
Echo = Pin(Echopin, mode = Pin.IN, pull = None)
def ping(timer):
	trigger.value(0) # Stabilize the sensor
        time.sleep_us(5)
        trigger.value(1)
        # Send a 10us pulse.
        time.sleep_us(10)
        trigger.value(0)
        try:
            pulse_time = machine.time_pulse_us(Echo, 1, 30000)
            print(pulse_time/58)
        except OSError as ex:
            if ex.args[0] == 110: # 110 = ETIMEDOUT
                raise OSError('Out of range')
            raise ex

tim = Timer(1)
tim.init(period = 100, mode = tim.PERIODIC, callback = ping)