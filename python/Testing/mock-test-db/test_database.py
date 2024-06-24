# test_database.py
import unittest
from unittest.mock import Mock, patch
from database import DatabaseHandler

class TestDatabaseHandler(unittest.TestCase):
    @patch('database.DatabaseHandler.execute_query')
    def test_get_user_by_id(self, mock_execute_query):
        # Mocking the response from the database
        mock_response = {
            'id': 1,
            'name': 'John Doe',
            'email': 'john.doe@example.com'
        }
        mock_execute_query.return_value = mock_response

        # Creating an instance of DatabaseHandler
        db_handler = DatabaseHandler("fake_connection_string")

        # Calling the method to database
        result = db_handler.get_user_by_id(1)

        # Asserting the result
        self.assertEqual(result, mock_response)
        mock_execute_query.assert_called_once_with("SELECT * FROM users WHERE id = 1")

if __name__ == '__main__':
    unittest.main()
