import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from main import main


class TestFlaskApp(unittest.TestCase):

    # Setup Flask test client
    def setUp(self):
        self.app = main.test_client()
        self.app.testing = True

    # Test 1: Route Test
    # Write a unit test for one of your routes (e.g., /home) to verify that the endpoint returns the expected status code when an invalid request is sent
    def test_home_route_invalid_method(self):
        response = self.app.post('/')
        self.assertEqual(response.status_code, 405)
        # Testing for Method Not Allowed

    # Test 2: Database Read Operation
    # Write a unit test to check the correct connection of a MongoDB read operation
    @patch('main.client')
    def test_mongodb_connection(self, mock_client):
        try:
            # Verifying if MongoDB client is able to ping the server
            mock_client.admin.command('ping')
        except Exception:
            self.fail("MongoDB Connection failed")

    # Test 3: Database Write Operation
    # Write a unit test for a MongoDB write operation (e.g., inserting a new document)
    @patch('main.collection')
    def test_insert_document(self, mock_collection):
        # Sample document to insert
        doc = {"name": "Low_fat", "price": "5.99", "expiry": "24/12", "category": "milk",
               "image_path": "/static/images/milk.jpg"}

        # Mocking the insert operation
        mock_collection.insert_one.return_value.inserted_id = 'mocked_id'

        # Performing the insert operation
        insert_result = mock_collection.insert_one(doc)

        # Checking if the insert method was called with the correct document
        mock_collection.insert_one.assert_called_with(doc)
        self.assertIsNotNone(insert_result.inserted_id)


if __name__ == '__main__':
    unittest.main()