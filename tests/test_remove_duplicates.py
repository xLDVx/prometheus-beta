import pytest
from src.remove_duplicates import remove_duplicate_words

def test_remove_duplicate_words_basic():
    """Test basic duplicate word removal."""
    assert remove_duplicate_words("hello hello world") == "hello world"

def test_remove_duplicate_words_multiple_duplicates():
    """Test removing multiple duplicate words."""
    assert remove_duplicate_words("the quick brown fox jumps the quick brown fox") == "the quick brown fox jumps"

def test_remove_duplicate_words_empty_string():
    """Test handling of empty string."""
    assert remove_duplicate_words("") == ""

def test_remove_duplicate_words_no_duplicates():
    """Test string with no duplicates."""
    assert remove_duplicate_words("python is awesome") == "python is awesome"

def test_remove_duplicate_words_consecutive_duplicates():
    """Test consecutive duplicate words."""
    assert remove_duplicate_words("a a b b c c") == "a b c"

def test_remove_duplicate_words_case_sensitive():
    """Test that the function is case-sensitive."""
    assert remove_duplicate_words("Hello hello HELLO") == "Hello hello HELLO"

def test_remove_duplicate_words_invalid_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicate_words(123)
        remove_duplicate_words(None)