from machine import Pin, ADC, DAC
from board import ADC3, ADC6
from time import sleep

adc = ADC(Pin(ADC6))
adc2 = ADC(Pin(ADC3))
adc2.atten(ADC.ATTN_11DB)
adc.atten(ADC.ATTN_11DB)
for i in range(1000):
	sleep(.1)
	val = adc.read()
	val1 = adc2.read()
	print(val, val1)