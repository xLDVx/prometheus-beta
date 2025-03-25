import pytest
from src.url_validator import is_valid_url

def test_valid_urls():
    """Test various valid URL formats"""
    valid_urls = [
        'http://www.example.com',
        'https://example.com',
        'https://example.com/path',
        'http://localhost',
        'https://localhost:8080',
        'ftp://files.example.com',
        'https://subdomain.example.co.uk/path?param=value',
        'http://192.168.1.1',
        'https://example.com:8080/path?query=123',
    ]
    for url in valid_urls:
        assert is_valid_url(url), f"{url} should be valid"

def test_invalid_urls():
    """Test various invalid URL formats"""
    invalid_urls = [
        '',  # Empty string
        '   ',  # Whitespace
        'not a url',
        'htp://invalid.com',  # Typo in scheme
        'http://',  # No domain
        'https://.',  # Invalid domain
        123,  # Non-string input
        None,  # None input
    ]
    for url in invalid_urls:
        assert not is_valid_url(url), f"{url} should be invalid"

def test_edge_cases():
    """Test edge case URL formats"""
    edge_cases = [
        'http://example.com/',  # URL with trailing slash
        'https://example.com/path/to/resource',  # Long path
        'http://example.com?param=value',  # URL with query parameter
        'https://exam-ple.com',  # Domain with hyphen
    ]
    for url in edge_cases:
        assert is_valid_url(url), f"{url} should be valid"