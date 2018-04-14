from board import A10
from machine import Pin, PWM
import machine
import time
DUTY = 0
pin = Pin(A10, mode=Pin.OUT)
pwm = PWM(pin, 50, 0, 1)
for i in range(13):
	pwm.duty(i)
	time.sleep_ms(80)
pwm.duty(1)

time.sleep(1)

pwm.duty(10)
time.sleep(1)
pwm.deinit()