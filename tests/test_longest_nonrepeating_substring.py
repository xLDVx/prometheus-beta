import pytest
from src.longest_nonrepeating_substring import longest_nonrepeating_substring

def test_standard_cases():
    """Test typical scenarios with various input strings."""
    assert longest_nonrepeating_substring("abcabcbb") == 3  # "abc"
    assert longest_nonrepeating_substring("bbbbb") == 1     # "b"
    assert longest_nonrepeating_substring("pwwkew") == 3    # "wke"

def test_edge_cases():
    """Test edge cases like empty string and strings with unique characters."""
    assert longest_nonrepeating_substring("") == 0          # Empty string
    assert longest_nonrepeating_substring("a") == 1         # Single character
    assert longest_nonrepeating_substring("abcdef") == 6    # All unique characters

def test_complex_cases():
    """Test more complex scenarios with repeated characters in different positions."""
    assert longest_nonrepeating_substring("dvdf") == 3      # Tricky case with repeated character
    assert longest_nonrepeating_substring("tmmzuxt") == 5   # Multiple repeated characters

def test_unicode_and_special_characters():
    """Test with Unicode and special characters."""
    assert longest_nonrepeating_substring("안녕하세요") == 6  # Korean characters
    assert longest_nonrepeating_substring("!@#$%^&*()") == 10  # Special characters

def test_whitespace_cases():
    """Test cases involving whitespace characters."""
    assert longest_nonrepeating_substring("a b c d") == 7   # Spaces between unique characters
    assert longest_nonrepeating_substring(" ") == 1         # Single space