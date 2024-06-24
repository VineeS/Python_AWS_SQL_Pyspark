import unittest
from unittest.mock import patch, MagicMock
from main import len_joke, get_joke

class TestJoke(unittest.TestCase):

    @patch('main.get_joke')
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = 'three'
        self.assertEqual(len_joke(),5)
        # this will cause test case to fail
        self.assertEqual(len_joke(),5)

    @patch('main.requests')  # Patching requests.get from main module
    def test_response(self, mock_get):
        mock_response = MagicMock(status_code = 200)
        mock_response.json.return_value = {'value': {'joke': 'hello world'}}

        mock_get.get.return_value = mock_response

        ## this will cause test case to fail
        # self.assertEqual(get_joke(), 'hell o world')  # Asserting the joke returned by get_joke
        self.assertEqual(get_joke(), 'hello world')

    @patch('main.requests')
    def test_fail_to_get_response(self,mock_requests):
        mock_response = MagicMock(status_code=404)
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), 'No jokes')
        ## this will cause test case to fail
        # self.assertEqual(get_joke(), 'No j okes ') 


if __name__ == "__main__":
    unittest.main()