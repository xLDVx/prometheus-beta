import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindrome():
    """Test basic palindrome strings."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True

def test_palindrome_with_spaces():
    """Test palindromes with spaces."""
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("race a car") == False

def test_palindrome_case_insensitive():
    """Test case-insensitive palindrome checking."""
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("RaceCar") == True

def test_palindrome_with_punctuation():
    """Test palindromes with punctuation."""
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("hello, world!") == False

def test_empty_and_single_char_strings():
    """Test empty and single character strings."""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_non_palindrome():
    """Test non-palindrome strings."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_error_handling():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError):
        is_palindrome(12345)
    
    with pytest.raises(TypeError):
        is_palindrome(None)
    
    with pytest.raises(TypeError):
        is_palindrome(["not", "a", "string"])