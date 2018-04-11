from board import A5, A21, A6, A8
from machine import PWM, Timer, Pin
pin1 = Pin(A5, mode = Pin.OPEN_DRAIN)
pin2 = Pin(A21, mode = Pin.OPEN_DRAIN)

speed = 10
ain1 = PWM(pin1, freq = 10000, duty = 0, timer= 0)
ain2 = PWM(pin2, freq = 10000, duty = 0, timer=0)
def speedcallback(timer):
	if speed < 0:
		ain1.duty(speed)
		ain2.duty(100)
	elif speed >= 0:
		ain1.duty(100)
		ain2.duty(speed)

tim = Timer(0)
tim.init(period = 100, mode = tim.PERIODIC, callback = speedcallback)

