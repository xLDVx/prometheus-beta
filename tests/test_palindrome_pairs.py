import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_basic_palindrome_pairs():
    """Test finding basic palindrome pairs."""
    words = ["bat", "tab", "cat"]
    result = find_palindrome_pairs(words)
    assert (0, 1) in result and (1, 0) in result
    assert len(result) == 2

def test_empty_input():
    """Test handling of empty input."""
    assert find_palindrome_pairs([]) == []
    assert find_palindrome_pairs(None) == []

def test_single_word_input():
    """Test input with single word."""
    words = ["hello"]
    assert find_palindrome_pairs(words) == []

def test_palindrome_with_different_lengths():
    """Test palindrome pairs with words of different lengths."""
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    result = find_palindrome_pairs(words)
    assert (0, 1) in result and (1, 0) in result
    
def test_no_palindrome_pairs():
    """Test case with no palindrome pairs."""
    words = ["hello", "world", "python"]
    assert find_palindrome_pairs(words) == []

def test_self_palindrome():
    """Test case with self-palindrome words."""
    words = ["a", "bb", ""]
    result = find_palindrome_pairs(words)
    assert len(result) > 0  # Should find some pairs

def test_large_input():
    """Test function with larger input to check performance."""
    words = ["a"] * 100
    result = find_palindrome_pairs(words)
    assert len(result) > 0  # Ensure some pairs are found