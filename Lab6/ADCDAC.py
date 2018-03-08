from machine import Pin, ADC, DAC
from board import DAC1, ADC6
from time import sleep


dac1 = DAC(Pin(DAC1))
adc = ADC(Pin(ADC6))
adc.atten(ADC.ATTN_11DB)
for i in range(255):
	dac1.write(i)
	print(i)
	sleep(.1)
	val2 = adc.read()
	print(val2)