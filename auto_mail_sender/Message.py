from __future__ import print_function
import pickle
import os.path
import base64
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase


from apiclient import errors, discovery
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from htmlJinja import template_loader

class Message():
    def __init__(self, SCOPES):
        '''
            Initailize the G-Mail service

            Args:
                SCOPES: [Array] List of scopes
        '''
        self.scope = SCOPES
        self.user_id = "me"

    
    def login(self):
        """Shows basic usage of the Gmail API.
        Lists the user's Gmail labels.
        """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.scope)
                creds = flow.run_local_server()
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        _service = build('gmail', 'v1', credentials=creds)
        
        self._service = _service
        print("Login successful")
        return


    def create_message(self, sender, to, subject, message_text):
        """Create a message for an email.

        Args:
            sender: Email address of the sender.
            to: Email address of the receiver.(Array)
            subject: The subject of the email message.
            message_text: The text of the email message.

        Returns:
            An object containing a base64url encoded email object.
        """
        message = MIMEText(message_text)
        message['to'] = ", ".join(to)
        message['from'] = sender
        message['subject'] = subject
        self.message1 = {'raw': base64.urlsafe_b64encode(message.as_string().encode('UTF-8')).decode()}


    def create_message_html(self, sender, to, subject, htmlText):
        
        msgRoot = MIMEMultipart()
        msgRoot['to'] = to
        msgRoot['from'] = sender
        msgRoot['subject'] = subject

        msgText = MIMEText(htmlText, 'html')
        msgRoot.attach(msgText)

        self.message1 = {'raw': base64.urlsafe_b64encode(msgRoot.as_string().encode('UTF-8')).decode()}

    def send_message(self):
        """Send an email message.


        Returns:
            Sent Message.
        """
        try:
            message = self._service.users().messages().send(userId=self.user_id, body=self.message1).execute()
            
            print(f"Message Id: {message['id']}")
            return message

        except errors.HttpError as error:
            print(f"An error occurred: {error}")

#example

if __name__ == "__main__":
    msg = Message(SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.send'])
    msg.login()
    msg.create_message_html("in2arkadip13@gmail.com", "janiarka00@gmail.com","AAA","ggg")
    msg.send_message()