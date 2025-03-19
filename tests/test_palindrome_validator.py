import pytest
from src.palindrome_validator import is_palindrome

def test_valid_palindromes():
    """Test various valid palindromes with different formatting."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("Madam, I'm Adam") == True

def test_case_insensitivity():
    """Ensure case is ignored in palindrome check."""
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("RACECAR") == True
    assert is_palindrome("RaCeCaR") == True

def test_punctuation_and_spaces():
    """Check that spaces and punctuation are ignored."""
    assert is_palindrome("A Santa at NASA") == True
    assert is_palindrome("No 'x' in Nixon") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_edge_cases():
    """Test edge cases like single character and special characters."""
    assert is_palindrome("a") == True
    assert is_palindrome("!@#$") == True
    assert is_palindrome(" ") == True
    assert is_palindrome("ab") == False

def test_non_string_input():
    """Verify behavior with non-string inputs."""
    with pytest.raises(AttributeError):
        is_palindrome(12321)
    with pytest.raises(AttributeError):
        is_palindrome(None)