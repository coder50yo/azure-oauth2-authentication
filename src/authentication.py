import os
import requests
from dotenv import load_dotenv

load_dotenv(override=True)

TENANT_ID = os.getenv('TENANT_ID')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

def get_access_token():
    """
    Retrieves an access token to use when calling the Microsoft Graph API.

    The following environment variables must be set:

    - TENANT_ID: The Tenant ID from your Azure app registration.
    - CLIENT_ID: The Client ID from your Azure app registration.
    - CLIENT_SECRET: The Client Secret generated from Azure.

    Returns:
        str: The access token to use when calling the Microsoft Graph API.

    Raises:
        Exception: If the request to retrieve the access token fails.
    """
    url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'client_id': CLIENT_ID,
        'scope': 'https://graph.microsoft.com/.default',
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }

    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        raise Exception(f"Error {response.status_code}: Failed to retrieve access token.")
