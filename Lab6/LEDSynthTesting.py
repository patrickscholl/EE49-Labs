from machine import Pin, PWM, Timer, ADC
from board import LED, A5, A8, ADC6, ADC3
import time
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
off = 10
FREQUENCY = 10
#song

State = False
fight = [F4, F4, F4, AS4, F4, AS4, D5, AS4, D5, F5, F5, F5, F5, F5, F5, F5, F5, F4, D5, D5, C5, AS4, off,
 AS4, AS4, AS4, AS4, AS4, AS4, AS4, AS4, AS4, A4, A4, A4, GS4, GS4, GS4, G4, 
 G4, G4, G4, G4, G4, G4, G4, G4, AS4, AS4, AS4, DS5, DS5, DS5, DS5, DS5, DS5, D5, D5, D5, C5, C5, C5,
 AS4, AS4, AS4, AS4, AS4, AS4, AS4, AS4, AS4]
bach = [
C4 , E4 , G4 , C5 , E5 , G4 , C5 , E5 , C4 , E4 , G4 , C5 , E5 , G4 , C5 , E5 ,
C4 , D4 , G4 , D5 , F5 , G4 , D5 , F5 , C4 , D4 , G4 , D5 , F5 , G4 , D5 , F5 ,
B3 , D4 , G4 , D5 , F5 , G4 , D5 , F5 , B3 , D4 , G4 , D5 , F5 , G4 , D5 , F5 ,
C4 , E4 , G4 , C5 , E5 , G4 , C5 , E5 , C4 , E4 , G4 , C5 , E5 , G4 , C5 , E5 ,
C4 , E4 , A4 , E5 , A5_ , A4 , E5 , A4 , C4 , E4 , A4 , E5 , A5_ , A4 , E5 , A4 ,
C4 , D4 , FS4 , A4 , D5 , FS4 , A4 , D5 , C4 , D4 , FS4 , A4 , D5 , FS4 , A4 , D5 ,
B3 , D4 , G4 , D5 , G5 , G4 , D5 , G5 , B3 , D4 , G4 , D5 , G5 , G4 , D5 , G5 ,
B3 , C4 , E4 , G4 , C5 , E4 , G4 , C5 , B3 , C4 , E4 , G4 , C5 , E4 , G4 , C5 ,
B3 , C4 , E4 , G4 , C5 , E4 , G4 , C5 , B3 , C4 , E4 , G4 , C5 , E4 , G4 , C5 ,
A3 , C4 , E4 , G4 , C5 , E4 , G4 , C5 , A3 , C4 , E4 , G4 , C5 , E4 , G4 , C5 ,
D3 , A3 , D4 , FS4 , C5 , D4 , FS4 , C5 , D3 , A3 , D4 , FS4 , C5 , D4 , FS4 , C5 ,
G3 , B3 , D4 , G4 , B4 , D4 , G4 , B4 , G3 , B3 , D4 , G4 , B4 , D4 , G4 , B4
]

pwm = PWM(pin, freq=FREQUENCY, duty = 10, timer = 1)
i = 0
xadc = ADC(Pin(ADC6))
yadc = ADC(Pin(ADC3))
xadc.atten(ADC.ATTN_11DB)
yadc.atten(ADC.ATTN_11DB)
def tune_cb(timer):
	global State
	global FREQUENCY
	global fight
	global i
	if State == False:
		FREQUENCY = fight[i]
		i+=1
	else: 
		FREQUENCY = int(4000*(yadc.read()/5000))
		duty = int(100*(xadc.read()/5000))
		pwm.duty(duty)
	pwm.freq(FREQUENCY)
tim = Timer(1)
tim.init(period=167, mode=tim.PERIODIC, callback = tune_cb)


brightness=50
led = Pin(LED, Pin.OPEN_DRAIN)
pwm2 = PWM(LED, freq=500, duty = brightness, timer = 0)

def led_cb(timer):
	global brightness
	if brightness < 100:
		brightness += 1
	else:
		brightness = 0
	pwm2.duty(brightness)
tim2 = Timer(0)
tim2.init(period=50, mode=tim.PERIODIC, callback=led_cb)


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
