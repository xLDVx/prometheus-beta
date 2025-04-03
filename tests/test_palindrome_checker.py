import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    # Simple palindromes
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("A") == True
    assert is_palindrome("") == True

def test_case_insensitive_palindromes():
    # Case-insensitive palindromes
    assert is_palindrome("Racecar") == True
    assert is_palindrome("RaceCar") == True
    assert is_palindrome("A Man A Plan A Canal Panama") == True

def test_non_palindromes():
    # Non-palindrome strings
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("world") == False

def test_palindromes_with_punctuation():
    # Palindromes with non-alphanumeric characters
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False  # This is actually not a palindrome
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_error_handling():
    # Error handling for non-string inputs
    with pytest.raises(TypeError):
        is_palindrome(12345)
    with pytest.raises(TypeError):
        is_palindrome(None)
    with pytest.raises(TypeError):
        is_palindrome(["not", "a", "string"])

def test_edge_cases():
    # Edge cases
    assert is_palindrome(" ") == True  # Whitespace
    assert is_palindrome("!!") == True  # Non-alphanumeric characters
    assert is_palindrome("12321") == True  # Numeric palindrome
    assert is_palindrome("A1b22b1a") == True  # Mixed alphanumeric