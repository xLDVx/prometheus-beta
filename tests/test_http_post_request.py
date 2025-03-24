import pytest
import requests
from unittest.mock import patch
from src.http_post_request import send_http_post_request

class MockResponse:
    def __init__(self, json_data, status_code, headers=None):
        self.json_data = json_data
        self.status_code = status_code
        self.headers = headers or {}
        self.content = json_data is not None

    def json(self):
        return self.json_data

    def raise_for_status(self):
        if 400 <= self.status_code < 600:
            raise requests.exceptions.HTTPError(f"HTTP Error: {self.status_code}")

def test_successful_post_request():
    with patch('requests.post') as mock_post:
        # Mock a successful response
        mock_response = MockResponse(
            json_data={'result': 'success'}, 
            status_code=200,
            headers={'Content-Type': 'application/json'}
        )
        mock_post.return_value = mock_response

        # Call the function
        result = send_http_post_request(
            'https://example.com/api', 
            data={'key': 'value'}
        )

        # Assertions
        assert result['status_code'] == 200
        assert result['json'] == {'result': 'success'}
        assert result['headers'] == {'Content-Type': 'application/json'}
        mock_post.assert_called_once_with(
            'https://example.com/api', 
            json={'key': 'value'}, 
            headers={}, 
            timeout=10
        )

def test_empty_url_raises_error():
    with pytest.raises(ValueError, match="Invalid or empty URL"):
        send_http_post_request('')

def test_invalid_url_raises_error():
    with pytest.raises(ValueError, match="Invalid or empty URL"):
        send_http_post_request('invalid_url')

def test_request_exception_handling():
    with patch('requests.post') as mock_post:
        # Simulate a request exception
        mock_post.side_effect = requests.exceptions.ConnectionError("Connection failed")

        with pytest.raises(RuntimeError, match="HTTP POST request failed"):
            send_http_post_request('https://example.com/api')

def test_http_error_handling():
    with patch('requests.post') as mock_post:
        # Mock a 404 error response
        mock_response = MockResponse(
            json_data=None, 
            status_code=404
        )
        mock_post.return_value = mock_response

        with pytest.raises(requests.exceptions.HTTPError):
            send_http_post_request('https://example.com/api')

def test_optional_parameters():
    with patch('requests.post') as mock_post:
        # Mock a successful response
        mock_response = MockResponse(
            json_data={}, 
            status_code=200
        )
        mock_post.return_value = mock_response

        # Call with all optional parameters
        result = send_http_post_request(
            'https://example.com/api', 
            data={'key': 'value'},
            headers={'Authorization': 'Bearer token'},
            timeout=30
        )

        # Verify the call
        mock_post.assert_called_once_with(
            'https://example.com/api', 
            json={'key': 'value'}, 
            headers={'Authorization': 'Bearer token'}, 
            timeout=30
        )

def test_empty_response():
    with patch('requests.post') as mock_post:
        # Mock an empty response
        mock_response = MockResponse(
            json_data=None, 
            status_code=204,
            headers={'Content-Length': '0'}
        )
        mock_post.return_value = mock_response

        # Call the function
        result = send_http_post_request('https://example.com/api')

        # Assertions
        assert result['status_code'] == 204
        assert result['json'] == {}
        assert result['headers'] == {'Content-Length': '0'}