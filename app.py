from src.authentication import get_access_token
from src.azure_api import call_azure_api

if __name__ == "__main__":
    try:
        token = get_access_token()
        user_data = call_azure_api(token)
        print("Data retrieved successfully:", user_data)
    except Exception as e:
        print(str(e))
