# Meeting Summarizer Project

A Raspberry Pi-based project that summarizes meetings recorded in .WAV files using an LLM and sends them to the user's email.

## Overview

When the user presses the button on top of the Pi's case, the microphone connected to the Pi begins recording the conversation of the occuring meeting and writes that data into a .WAV file. Once the meeting is over and the user presses the button again, OpenAI's Whisper-1 and GPT-3.5-Turbo models are used to convert that .WAV file into text, and then transform that text into a summary of the recorded meeting. If needed, the summary is automatically translated into English by Whisper-1. Then, the summary is immediately sent to any stakeholders of the meeting through the Gmail API.

## Why this project?

This project was taken on to learn how to utilize LLMs (Large Language Models) with code, and to learn a little about the hardware side of engineering by utilizing a Raspberry Pi and physical input and output. As an incoming college freshman majoring in computer engineering, I wanted to get a head-start on what I am going to be learning at my university--on both the software and the hardware aspects of my studies.

## What was learned?

- How to utilize LLMs through an API
- How to send emails through the Gmail API
- How to wire external inputs and outputs onto a Raspberry Pi header
- How to listen to input from physical buttons and display output through LEDs
- How to record audio through a microphone attached by USB

## How to re-create this project

### Ingredients
1. Raspberry Pi
2. Button
3. LED
4. Microphone (attached to Pi through USB)
5. At least 4 jumper wires to connect a button and light to your Pi

### Recipe
1. Ensure all required libraries are installed onto a Python virtual environment on your Pi (see requirements.txt).
2. Create an OpenAI account and deposit a minimum of 5 US dollars into it (see https://platform.openai.com/docs/overview).
3. Create an OpenAI API key (see https://platform.openai.com/settings/organization/api-keys) and make it an environment variable on your Pi. Then change line 4 of Gpt.py to the name of that environment variable.
4. Create a Google Cloud Project, enable the Gmail API, and generate an OAuth 2.0 Credentials json file. Then, put it into the jsons folder in the repo (see /jsons/README.md for more details).
5. Wire your button to GPIO17 and your light to GPIO27 on your Py. Or re-wire the button and light to different GPIO pins and specify your GPIO placements in Button.py and Light.py.
6. Clone this repo, plug in an audio input device into your Py using a usb port, un-comment lines 33 and 34 in Audio.py, and run Main.py through your Python virtual environment.
7. Change the deviceIndex var on line 17 of Audio.py to the device index of your chosen audio input device, viewable in your output log once lines 33 and 34 are un-commented.
8. Run Main.py again (through your Python virtual environment, as always) and sign into the Google account you used to create your Google Cloud Project.
9. Change any variables you don't like! (sender, recipient, subject variables in Gmail.py, etc.)
