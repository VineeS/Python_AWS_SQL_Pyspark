import pytest
from mockito import when, mock, unstub
from main import get_data
import requests

def test_get_data_with_mockito():
    # Mock the requests module and its get function
    mock_response = mock(dict)
    when(requests).get("https://api.example.com/data").thenReturn(mock_response)

    # Set up the mock response
    mock_response.status_code = 200
    mock_response.json = lambda: {'key': 'value'}  # Mocking the JSON response

    # Call the function under test
    result = get_data()

    # Assert the result
    assert result == {'key': 'value'}

    # Clean up the mock
    unstub()

if __name__ == "__main__":
    pytest.main()
