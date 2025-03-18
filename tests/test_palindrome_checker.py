import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindrome():
    """Test basic palindrome detection."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True

def test_case_insensitive():
    """Test that function is case-insensitive."""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("A man a plan a canal Panama") == True

def test_non_palindrome():
    """Test non-palindrome strings."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_numbers_and_spaces():
    """Test palindromes with numbers and spaces."""
    assert is_palindrome("12321") == True
    assert is_palindrome("A1 b22b 1a") == True

def test_empty_and_single_char():
    """Test edge cases with empty and single character strings."""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_special_characters():
    """Test handling of special characters."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False