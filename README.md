GPT-based project that summarizes meetings recorded in .wav files and sends them to the user's email from a Raspberry Pi.

How to re-create this project:
1. Ensure all required libraries are installed onto Python virtual environment on your Pi (see requirements.txt).
2. Create an OpenAI account and deposit a minimum of 5 US dollars into it (see https://platform.openai.com/docs/overview).
3. Create an OpenAI API key (see https://platform.openai.com/settings/organization/api-keys) and make it an environment variable on your Pi.
4. Create a Google Cloud Project, enable the Gmail API, and generate an OAuth 2.0 Credentials json file and put it into the jsons folder (see /jsons/README.md for more details).
5. Clone this repo and run it through your Python virtual environment!
