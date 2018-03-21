from machine import Pin, PWM
from board import A10, A6

p1 = Pin(A10, mode =Pin.OPEN_DRAIN)
p2 = Pin(A6, mode =Pin.OPEN_DRAIN)


PWM(p1, freq=5000, duty = 20, timer= 0)

PWM(p2, freq=8000, duty = 60, timer= 1)