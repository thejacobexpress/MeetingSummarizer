import os.path
from email.message import EmailMessage
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

sender = "<mckeeartificialintelligence@gmail.com>"
recipient = "thejacobexpress@gmail.com"
subject = "Your meeting summary is ready."

def sendEmail(content):
    creds = None
    try:
        creds = c.Credentials.from_authorized_user_file("jsons/token.json", ['https://mail.google.com/'])
    except FileNotFoundError as e:
        flow = InstalledAppFlow.from_client_secrets_file(
            "jsons/credentials.json", ['https://mail.google.com/']
        )
        creds = flow.run_local_server(port=0)
        open("jsons/token.json", 'w').write(creds.to_json())

    service = build('gmail', 'v1', credentials = creds)

    message = EmailMessage()

    message.set_content(content)
    message["To"] = recipient
    message["From"] = "McKeeAI" + sender
    message["Subject"] = subject

    encodedMessage = base64.urlsafe_b64encode(message.as_bytes()).decode()

    createMessage = {"raw": encodedMessage}
    draft = service.users().messages().send(userId="me", body=createMessage).execute()