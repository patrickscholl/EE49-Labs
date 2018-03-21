from machine import Pin, ADC
import time
from board import A5, ADC6, ADC3

p = Pin(A5, mode=Pin.IN, pull=Pin.PULL_UP)
COUNTER = 0
lasttime = time.time()
def h(pin):
	global lasttime
	global COUNTER
	currenttime = time.time()
	if pin.value() == 0:
		if currenttime - lasttime > 0.15:
			COUNTER +=1
			lasttime = currenttime
			print("{}".format(COUNTER))
		else:
			pass
	else: 
		pass

p.irq(handler=h, trigger=Pin.IRQ_FALLING)

