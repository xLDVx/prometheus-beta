import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindromes():
    """Test basic palindrome strings."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("deified") == True

def test_palindrome_phrases():
    """Test palindrome phrases with spaces and punctuation."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome("No lemon, no melon") == True

def test_non_palindromes():
    """Test strings that are not palindromes."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("OpenAI") == False

def test_edge_cases():
    """Test edge cases and boundary conditions."""
    assert is_palindrome("") == True  # Empty string
    assert is_palindrome(" ") == True  # Whitespace
    assert is_palindrome("a") == True  # Single character
    assert is_palindrome("1") == True  # Single numeric character
    
def test_case_insensitivity():
    """Verify case-insensitive palindrome checking."""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("RaCeCaR") == True

def test_numeric_palindromes():
    """Test palindromes with numeric characters."""
    assert is_palindrome("12321") == True
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("123 321") == True

def test_mixed_characters():
    """Test palindromes with mixed alphanumeric characters."""
    assert is_palindrome("a1b2c33c2b1a") == True
    assert is_palindrome("a1b2c3 3c2b1a") == True