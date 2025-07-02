import os.path
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64

import google.auth
from google.auth.transport.requests import Request
from google.auth.aio.credentials import Credentials
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import google.oauth2.service_account
import google.oauth2.credentials as c
from pyexpat.errors import messages

# CHANGE THESE WHEN RECREATING PROJECT
credentialsLoc = "/home/jacobmckee/Projects/MeetingSummarizer-master/jsons/credentials.json"
tokenLoc = "/home/jacobmckee/Projects/MeetingSummarizer-master/jsons/token.json"

summary = ""
transcript = ""

sender = "<mckeeartificialintelligence@gmail.com>"
recipient = "thejacobexpress@gmail.com"
subject = "Your meeting summary is ready."

def createEmailStructure():
    # Create a draft of an email in plain text
    summaryPreface = "Here is the summary of your meeting:\n"
    transcriptPreface = "\n\nWant a closer look at your meeting? Here is the transcript: \n"
    return summaryPreface + summary + transcriptPreface + transcript
    
def createHTMLEmailStructure():
    # Create a draft of an email in HTML
    summaryPrefaceHTML = "<p><strong>Here is the summary of your meeting:</strong></p>"
    summaryTextHTML = "<p>" + summary + "<br><br></p>"
    transcriptPrefaceHTML = "<p>Want a closer look at your meeting? <strong>Here is the transcript:</strong></p>"
    transcriptTextHTML = "<p>" + transcript + "</p>"
    return summaryPrefaceHTML + summaryTextHTML + transcriptPrefaceHTML + transcriptTextHTML

def sendEmail():
    creds = None
    try:
        creds = c.Credentials.from_authorized_user_file(tokenLoc, ['https://mail.google.com/'])
    except FileNotFoundError as e:
        flow = InstalledAppFlow.from_client_secrets_file(
            credentialsLoc, ['https://mail.google.com/']
        )
        creds = flow.run_local_server(port=0)
        open(tokenLoc, 'w').write(creds.to_json())

    service = build('gmail', 'v1', credentials = creds)

    message = MIMEMultipart("alternative")

    # Create an HTML version and a plain text version of the email to fallback on.
    plain = MIMEText(createEmailStructure(), 'plain')
    message.attach(plain)
    html = MIMEText(createHTMLEmailStructure(), "html")
    message.attach(html)

    message["To"] = recipient
    message["From"] = "McKeeAI" + sender
    message["Subject"] = subject

    encodedMessage = base64.urlsafe_b64encode(message.as_bytes()).decode()

    createMessage = {"raw": encodedMessage}
    draft = service.users().messages().send(userId="me", body=createMessage).execute() # Send email!
    print("Email sent")
