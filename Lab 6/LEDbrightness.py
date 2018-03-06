from machine import Pin
from board import LED
from machine import PWM, Timer
from time import sleep

brightness=50
led = Pin(LED, Pin.OPEN_DRAIN)
pwm = PWM(LED, freq=500)

def led_cb(timer):
	global brightness
	if brightness < 100:
		brightness += 1
	else:
		brightness = 0
	pwm.duty(brightness)
tim = Timer(0)
tim.init(period=50, mode=tim.PERIODIC, callback=led_cb)