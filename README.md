GPT-based project that summarizes meetings recorded in .wav files and sends them to the user's email from a Raspberry Pi.

How to re-create this project:
1. Ensure all required libraries are installed onto a Python virtual environment on your Pi (see requirements.txt).
2. Create an OpenAI account and deposit a minimum of 5 US dollars into it (see https://platform.openai.com/docs/overview).
3. Create an OpenAI API key (see https://platform.openai.com/settings/organization/api-keys) and make it an environment variable on your Pi. Then change line 4 of Gpt.py to what you named your environment variable.
4. Create a Google Cloud Project, enable the Gmail API, and generate an OAuth 2.0 Credentials json file and put it into the jsons folder (see /jsons/README.md for more details).
5. Wire your button to GPIO17 and your light to GPIO27 on your Py. Or re-wire the button and light to a different GPIO pin and specify your GPIO placements in Button.py and Light.py.
6. Clone this repo, plug in an audio input device into your Py using a usb port, un-comment lines 33 and 34 in Audio.py, and run Main.py through your Python virtual environment.
7. Change the deviceIndex var on line 17 of Audio.py to the device index of your chosen audio input device, viewable in your output log once lines 33 and 34 are un-commented.
8. Run Main.py again (through your Python virtual environment, as always) and sign into the Google account you used to create your Google Cloud Project.
9. Change any variables you don't like! (sender, recipient, subject variables in Gmail.py, etc.)
