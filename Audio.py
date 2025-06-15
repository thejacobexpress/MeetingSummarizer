import pyaudio
import wave

channels = 1
rate = 44100

def recordAndWriteWavFile():
    pyaud = pyaudio.PyAudio()

    format = pyaudio.paInt16
    sampleWidth = pyaudio.get_sample_size(format)

    # print out devices
    for i in range(pyaud.get_device_count()):
        print(pyaud.get_device_info_by_index(i))

    stream = pyaud.open(format=format, channels=channels, rate=rate, input_device_index=1, input = True, output = True)

    # Write audio into frames array from stream.
    frames = []
    for i in range(0, 100):
        print(i)
        data = stream.read(1024)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    pyaud.terminate()

    # Create a WAV file and write frames array into file.
    waveFile = wave.open("C:/Users/jacob/PyCharmProjects/LLMProject/recording.wav", 'wb')
    waveFile.setnchannels(channels)
    waveFile.setsampwidth(sampleWidth)
    waveFile.setframerate(rate)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

def convertWavToText(waveFile):
    pass