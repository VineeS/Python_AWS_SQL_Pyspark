import requests
import unittest
from unittest.mock import patch

def get_user_data(employee_id):
    print(employee_id)
    response = requests.get(f'https://www.mockaroo.com/apis/92629/A123')
    print(response.json())
    return response.json()

class TestClass(unittest.TestCase):
    
    @patch('requests.get')
    def test_get_user_data(self, mock_get):
        # Create a mock response object with a sample JSON response
        mock_response = unittest.mock.Mock()
        expected_data = {
            "employee_id": "A0000",
            "name": "Jane dododod",
            "position": "Head Librarian",
            "hire_date": "2010-08-09"
        }
        mock_response.json.return_value = expected_data
        mock_get.return_value = mock_response

        # Call the function with a sample employee_id
        result = get_user_data("A123")
        print(result)

        # Assert the expected response matches the actual response
        self.assertEqual(result, expected_data)
        mock_get.assert_called_once_with('https://www.mockaroo.com/apis/92629/B456')

if __name__ == '__main__':
    unittest.main()
