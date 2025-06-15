import openai
import os

from Audio import recordAndWriteWavFile, convertWavToText
from Gpt import summarizeText

if __name__ == "__main__":
    wavPath = recordAndWriteWavFile()
    text = convertWavToText(wavPath)
    print(text)
    print(summarizeText(text))