from mqttclient import MQTTClient 
from time import sleep

BROKER = 'iot.eclipse.org'
USER = None
PWD = None

mqtt = MQTTClient(BROKER, user = USER, password=PWD, ssl = TRUE)

i = 1
while True:
	i += 1
	topic = '/patrick/esp32/hi'
	mqtt.publish(topic, 'Hello {}'.format(i))
