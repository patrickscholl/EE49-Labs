from machine import Pin, PWM, Timer
from board import LED, A5, A8, ADC6, ADC3
pin = Pin(A8, Pin.OPEN_DRAIN)
#Note Frequencies
C3 = 131
CS3 = 139
D3 = 147
DS3 = 156
E3 = 165
F3 = 175
FS3 = 185
G3 = 196
GS3 = 208
A3 = 220
AS3 = 233
B3 = 247
C4 = 262
CS4 = 277
D4 = 294
DS4 = 311
E4 = 330
F4 = 349
FS4 = 370
G4 = 392
GS4 = 415
A4 = 440
AS4 = 466
B4 = 494
C5 = 523
CS5 = 554
D5 = 587
DS5 = 622
E5 = 659
F5 = 698
FS5 = 740
G5 = 784
GS5 = 831
A5_ = 880
AS5 = 932
B5 = 988
C6 = 1047
CS6 = 1109
D6 = 1175
DS6 = 1245
E6 = 1319
F6 = 1397
FS6 = 1480
G6 = 1568
GS6 = 1661
A6 = 1760
AS6 = 1865
B6 = 1976
C7 = 2093
CS7 = 2217
D7 = 2349
DS7 = 2489
E7 = 2637
F7 = 2794
FS7 = 2960
G7 = 3136
GS7 = 3322
A7 = 3520
AS7 = 3729
B7 = 3951
C8 = 4186
CS8 = 4435
D8 = 4699
DS8 = 4978
off = 0
FREQUENCY = 0
#song

State = False
fight = [F3, B4, F3, D4, B4, D4, F4, F4, F4, F4, F4, F4, F4, F4, F3, D4, D4, C4, B4, off, B4, B4, B4, B4, B4, B4, B4, B4, B4, A4, A4, A4, GS3, GS3, GS3, G3, G3, G3, G3, G3, G3, G3, G3, G3, B4, E4, E4, E4, E4, E4, E4, D4, D4, D4, C4, C4, C4, B4, B4, B4, B4, B4, B4, B4, B4, B4]
pwm = PWM(pin, freq=FREQUENCY, duty = 50, 1)
i = 0
xadc = ADC(Pin(ADC6))
yadc = ADC(Pin(ADC3))
def tune_cb(timer):
	global State
	global FREQUENCY
	if State == False:
		FREQUENCY = fight[i]
		i+=1
	else: 
		FREQUENCY = .5*(xadc.read()**2 + yadc.read()**2)**(0.5)
	pwm.freq(FREQUENCY)
tim = Timer(1)
tim.init(period=167, mode=tim.PERIODIC, callback = tune_cb)


brightness=50
led = Pin(LED, Pin.OPEN_DRAIN)
pwm = PWM(LED, freq=500, duty = brightness, 0)

def led_cb(timer):
	global brightness
	if brightness < 100:
		brightness += 1
	else:
		brightness = 0
	pwm.duty(brightness)
tim = Timer(0)
tim.init(period=50, mode=tim.PERIODIC, callback=led_cb)


p = Pin(A5, mode=Pin.IN, pull=Pin.PULL_UP)
COUNTER = 0
lasttime = time.time()
def h(pin):
	global lasttime
	global State
	currenttime = time.time()
	if pin.value() == 0:
		if currenttime - lasttime > 0.1:
			State = not State
			lasttime = currenttime
		else:
			pass
	else: 
		pass

p.irq(handler=h, trigger=Pin.IRQ_FALLING)
