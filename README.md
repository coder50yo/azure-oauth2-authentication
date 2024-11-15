# Microsoft Azure OAuth2 Authentication

This project demonstrates how to authenticate with Microsoft Azure and use Microsoft Graph API in a Python environment. The project uses OAuth2 to acquire an access token from Azure, which is then used to interact with the API to retrieve user profile data.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Setup](#setup)
- [Testing](#testing)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Environment Variables](#environment-variables)
- [License](#license)

## Requirements

To run this project, ensure you have the following:

- Python 3.8 or higher
- Azure account for app registration
- Internet connection

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/coder50yo/azure-oauth2-authentication.git
   cd copilot-python-api
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: .\venv\Scripts\Activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   This will install all necessary libraries specified in the `requirements.txt` file, such as `requests` and `python-dotenv`.

## Setup

### 1. Azure App Registration:

- Go to the Azure Portal and register an application.
- Retrieve the Tenant ID, Client ID, and Client Secret.
- Set permissions under API Permissions for Microsoft Graph (e.g., `User.Read`).

### 2. Environment Variables:

- Create a `.env` file in the root directory to store sensitive information (e.g., Tenant ID, Client ID, Client Secret).

   ```bash
   touch .env
   ```

- In the `.env` file, add the following:

   ```env
   TENANT_ID=your_tenant_id
   CLIENT_ID=your_client_id
   CLIENT_SECRET=your_client_secret
   ```

## Testing

Run unit tests with:
```bash
python -m unittest discover tests
```

## Running the Application

1. To start the project, run:

   ```bash
   python app.py
   ```

2. The script will authenticate with Azure and make a request to Microsoft Graph API to retrieve profile data.

## Project Structure

```bash
copilot-python-api/
│
├── src/                         # Source code directory
│   ├── __init__.py              # Marks this directory as a Python package
│   ├── authentication.py        # Handles authentication with Azure
│   └── azure_api.py           # API logic (Microsoft Graph or Copilot)
│
├── tests/                       # Unit tests directory
│   └── test_authentication.py   # Tests for authentication logic
│   └── test_azure_api.py      # Tests for API logic
│
├── .env                         # Environment variables (excluded from version control)
├── .gitignore                   # Ignoring sensitive or unnecessary files
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
└── app.py                       # Main entry point for the app

```

## Environment Variables

The following environment variables are required:

- **TENANT_ID**: The Tenant ID from your Azure app registration.
- **CLIENT_ID**: The Client ID from your Azure app registration.
- **CLIENT_SECRET**: The Client Secret generated from Azure.

Make sure to set these in your `.env` file before running the application.

## Final Steps
- **requirements.txt**: Ensure dependencies are listed:
  ```bash
  pip freeze > requirements.txt
  ```
- **Testing & Deployment**: Run all tests locally before deploying to ensure everything works smoothly. For deployment to Azure or other cloud services, follow appropriate deployment steps (e.g., Azure App Service).

## License

This project is licensed under the MIT License