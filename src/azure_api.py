import requests

def call_azure_api(access_token):
    """
    Retrieves organization data from Microsoft Graph API.

    Parameters:
    access_token (str): A valid access token for Azure authentication.

    Returns:
    dict: A JSON object representing the organization data, or an Exception if the request fails.
    """
    api_url = "https://graph.microsoft.com/v1.0/organization"
    headers = {'Authorization': f'Bearer {access_token}'}

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error {response.status_code}: Failed to retrieve data.")
