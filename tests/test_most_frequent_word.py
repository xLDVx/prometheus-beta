import pytest
from src.most_frequent_word import most_frequent_word

def test_most_frequent_word_basic():
    """Test basic functionality with a simple input string."""
    assert most_frequent_word("the cat sat on the mat") == "the"

def test_most_frequent_word_tie_breaker():
    """Test when multiple words have the same frequency."""
    result = most_frequent_word("cat dog cat dog")
    assert result in ["cat", "dog"]

def test_most_frequent_word_single_word():
    """Test with a single word input."""
    assert most_frequent_word("hello") == "hello"

def test_most_frequent_word_multiple_spaces():
    """Test input with multiple spaces between words."""
    assert most_frequent_word("the  cat  sat  on  the  mat") == "the"

def test_most_frequent_word_empty_input():
    """Test that an empty input raises a ValueError."""
    with pytest.raises(ValueError, match="Input text cannot be empty"):
        most_frequent_word("")

def test_most_frequent_word_only_spaces():
    """Test input with only spaces raises a ValueError."""
    with pytest.raises(ValueError, match="Input text must contain at least one word"):
        most_frequent_word("   ")

def test_most_frequent_word_invalid_characters():
    """Test input with non-lowercase letters raises a ValueError."""
    with pytest.raises(ValueError, match="Input must contain only lowercase letters and spaces"):
        most_frequent_word("The Cat Sat")
    
    with pytest.raises(ValueError, match="Input must contain only lowercase letters and spaces"):
        most_frequent_word("cat123 dog")
    
    with pytest.raises(ValueError, match="Input must contain only lowercase letters and spaces"):
        most_frequent_word("cat! dog")