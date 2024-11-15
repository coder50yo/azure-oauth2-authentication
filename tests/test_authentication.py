import unittest
from src.authentication import get_access_token

class TestAuthentication(unittest.TestCase):
    def test_get_access_token(self):
        token = get_access_token()
        self.assertIsNotNone(token)
