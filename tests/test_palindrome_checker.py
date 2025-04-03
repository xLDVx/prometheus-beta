import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    """Test basic palindrome scenarios"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("radar") == True
    assert is_palindrome("level") == True

def test_non_palindromes():
    """Test non-palindrome scenarios"""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("world") == False

def test_case_sensitivity():
    """Test case-sensitive palindrome checking"""
    assert is_palindrome("Racecar") == False
    assert is_palindrome("RaceCar") == False

def test_numbers_and_special_chars():
    """Test palindromes with numbers and special characters"""
    assert is_palindrome("12321") == True
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("A1b22b2a") == False

def test_edge_cases():
    """Test edge case scenarios"""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_error_handling():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        is_palindrome(12345)
    with pytest.raises(TypeError):
        is_palindrome(None)
    with pytest.raises(TypeError):
        is_palindrome(["not", "a", "string"])