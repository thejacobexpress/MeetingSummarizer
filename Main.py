import openai
import os

from Audio import recordAndWriteWavFile, convertWavToText
from Gmail import sendEmail
from Gpt import summarizeText
from email.mime.text import MIMEText

if __name__ == "__main__":
    # Write audio from mic into a file called "recording.wav" and store in project dir
    wavPath = recordAndWriteWavFile()

    # Convert the audio file to text using the audio file's path and Whisper-1 model
    transcript = convertWavToText(wavPath)

    # Summarize the transcript using GPT-3.5-Turbo model
    summary = summarizeText(transcript)

    # Create a draft of an email using Google's API
    summaryPrefaceHTML = "<p><strong>Here is the summary of your meeting:</strong></p>"
    summaryTextHTML = "<p>" + summary + "<br><br></p>"
    transcriptPrefaceHTML = "<p>Want a closer look at your meeting? <strong>Here is the transcript:</strong></p>"
    transcriptTextHTML = "<p>" + transcript + "</p>"
    emailText = summaryPrefaceHTML + summaryTextHTML + transcriptPrefaceHTML + transcriptTextHTML
    draft = sendEmail(MIMEText(emailText, "html"))