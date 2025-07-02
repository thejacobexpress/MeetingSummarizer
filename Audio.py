import pyaudio
import wave
import openai
from Gpt import summarizeText
from Gmail import sendEmail, createEmailStructure, createHTMLEmailStructure
import Gmail
import Button
import Light
import time
import threading

collectingAudio = False
canStopRecording = False

channels = 1
rate = 44100
deviceIndex = 2

stream = None

filePath = "/home/jacobmckee/Projects/MeetingSummarizer-master/recording.wav"

def recordAndWriteWavFile():
    Light.quickBlink() # 3-time blink to alert the user that the py has started to record audio.
    Light.light.blink() # Alerts the user that the py is loading.
    
    pyaud = pyaudio.PyAudio()

    format = pyaudio.paInt16
    sampleWidth = pyaudio.get_sample_size(format)

    # print out devices
    #for i in range(pyaud.get_device_count()):
    #    print(pyaud.get_device_info_by_index(i))

    stream = pyaud.open(format=format, channels=channels, rate=rate, input_device_index=deviceIndex, input = True, output = True)

    # Write audio into frames array from stream.
    frames = []
    Light.light.on() # Alerts the user that they can press the button again.
    print("Recording!")
    canStopRecording = True
    while collectingAudio:
        data = stream.read(1024)
        frames.append(data)
        if Button.button.is_pressed:
            Light.light.blink()
            break
    stream.stop_stream()
    stream.close()
    pyaud.terminate()
    print("Stopped Recording!")

    # Create a WAV file and write frames array into file.
    waveFile = wave.open(filePath, 'wb')
    waveFile.setnchannels(channels)
    waveFile.setsampwidth(sampleWidth)
    waveFile.setframerate(rate)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    Gmail.transcript = convertWavToText(filePath) # Convert .WAV file to text using OpenAI's Whisper-1 model.
    Gmail.summary = summarizeText(Gmail.transcript) # Summarize the generated transcript using GPT.
    print(createEmailStructure())
    sendEmail() # Finally, send the transcript and the generated summary using Gmail's API.
    time.sleep(2) # pyaud.open called too often results in "Invalid number of channels" error.
    # Default back to listening for a button press:
    Light.quickBlink() # 3-time blink to alert the user that an email as been sent.
    Light.light.on() # Alerts the user that they can press the button again.
    print("Listening...")
    while True:
        if Button.button.is_pressed:
            recordAndWriteWavFile()

def convertWavToText(path):
    try:
        transcription = openai.audio.translations.create(
            model = "whisper-1",
            file = open(path, "rb")
        )
        return transcription.text
    except openai.BadRequestError as e:
         print("audio is too short!")
         time.sleep(2) # pyaud.open within recordAndWriteWavFile() function called too often results in "Invalid number of channels" error.
         # Default back to listening for a button press:
         Light.light.on() # Alerts the user that they can press the button again.
         print("Listening...")
         while True:
            if Button.button.is_pressed:
                recordAndWriteWavFile()
         
