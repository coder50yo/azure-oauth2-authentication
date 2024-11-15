import unittest
from src.azure_api import call_azure_api
from src.authentication import get_access_token

class TestAzureAPI(unittest.TestCase):
    def test_call_azure_api(self):
        token = get_access_token() #or "dummy_token"  # Mock token for testing
        response = call_azure_api(token)
        self.assertIn('Consultant', response['value'][0]['displayName'])
        self.assertIn('Tabaco', response['value'][0]['city'])
        self.assertIn('christian.loria@gmail.com', response['value'][0]['technicalNotificationMails'])
        self.assertIn('639693942088', response['value'][0]['businessPhones'])
        self.assertIn('AzureAnalysis', [plan['service'] for plan in response['value'][0]['assignedPlans']])
