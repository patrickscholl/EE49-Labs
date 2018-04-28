from board import A5
from machine import Pin, PWM
import machine
import time
DUTY = 4
pin = Pin(A5, mode=Pin.OUT)
pwm = PWM(pin, 50, DUTY, 1)
for i in range(6):
	pwm.duty(i+DUTY)
	time.sleep_ms(1000)
	print(i)
pwm.duty(1)

time.sleep(1)

pwm.duty(0)
time.sleep(1)
pwm.deinit()