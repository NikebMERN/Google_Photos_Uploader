import os
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# Scopes required to access Google Photos
SCOPES = ['https://www.googleapis.com/auth/photoslibrary.appendonly']

def authenticate():
    """Authenticate and return a Google Photos API service."""
    creds = None
    token_path = 'config/token.json'
    creds_path = 'config/credentials.json'

    # Load existing tokens if available
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    # If no valid credentials available, initiate login flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for future use
        with open(token_path, 'w') as token_file:
            token_file.write(creds.to_json())

    return creds
