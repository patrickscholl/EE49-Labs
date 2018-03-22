from board import A5, A21, A6, A8
from machine import PWM, Timer, Pin
pin1 = Pin(A5, mode = Pin.OPEN_DRAIN)
pin2 = Pin(A21, mode = Pin.OPEN_DRAIN)

speed = 20
ain1 = PWM(pin1, frequency = 10000, duty = 0, 0)
ain2 = PWM(pin2, frequency = 10000, duty = 0, 0)

if speed < 0:
	ain1.duty(speed)
	ain2.duty(1)
elif speed >= 0:
	ain1.duty(1)
	ain2.duty(speed)