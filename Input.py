import gpiozero as gp
import Audio
from Audio import recordAndWriteWavFile
from signal import pause
import threading
import Button
import Light
from time import sleep

def buttonPressed():
	if Audio.collectingAudio and Audio.canStopRecording:
		Audio.collectingAudio = False
	else:
		Audio.collectingAudio = True
		recordAndWriteWavFile()

def listenAndPause():
	Button.button.when_pressed = buttonPressed
	Light.light.on() # Alerts the user that they can press the button again.
	print("Listening...")
	pause()
