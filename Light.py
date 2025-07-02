from gpiozero import LED
from time import sleep

light = LED(27)

def quickBlink():
	for i in range(0,3):
		light.off()
		sleep(0.3)
		light.on()
		sleep(0.3)
