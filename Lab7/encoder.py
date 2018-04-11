from board import A6, A7, A5, A21
from machine import Pin, ENC, PWM, Timer
from time import sleep

pin1 = Pin(A5, mode = Pin.OPEN_DRAIN)
pin2 = Pin(A21, mode = Pin.OPEN_DRAIN)
speed = -100
ain1 = PWM(pin1, freq = 10000, duty = 0, timer= 0)
ain2 = PWM(pin2, freq = 10000, duty = 0, timer=0)

encA_pin = Pin(A6)
#encB_pin = Pin(A7)
encA = ENC(0, encA_pin)
#encB = ENC(1, encB_pin )
encA.filter(1023)
#encB.filter(1023)
cpsarray = []
for i in range(200):
	speed +=1
	if speed < 0:
		ain1.duty(-1*speed)
		ain2.duty(100)
	elif speed >= 0:
		ain1.duty(100)
		ain2.duty(speed)
	cpsarray.append([speed, encA.count()])
	encA.clear()
	print('Waiting')
	sleep(1)
print(cpsarray)

