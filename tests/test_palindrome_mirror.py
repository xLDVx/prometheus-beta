import pytest
from src.palindrome_mirror import create_palindrome_mirror

def test_basic_string():
    """Test basic string palindrome mirror creation."""
    assert create_palindrome_mirror("hello") == "helloolleh"

def test_empty_string():
    """Test empty string input."""
    assert create_palindrome_mirror("") == ""

def test_single_character():
    """Test single character input."""
    assert create_palindrome_mirror("a") == "aa"

def test_with_numbers():
    """Test string with numbers."""
    assert create_palindrome_mirror("123") == "123321"

def test_with_special_characters():
    """Test string with special characters."""
    assert create_palindrome_mirror("A1!") == "A1!1!A"

def test_with_spaces():
    """Test string with spaces."""
    assert create_palindrome_mirror("hello world") == "hello worlddlrow olleh"

def test_invalid_input_type():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        create_palindrome_mirror(123)
        create_palindrome_mirror(None)
        create_palindrome_mirror(["list"])