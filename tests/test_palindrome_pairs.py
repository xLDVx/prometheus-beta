import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_basic_palindrome_pairs():
    """Test basic palindrome pairs scenario."""
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    expected = [[0, 1], [1, 0], [3, 4], [4, 3]]
    assert sorted(find_palindrome_pairs(words)) == sorted(expected)

def test_empty_input():
    """Test handling of empty input."""
    assert find_palindrome_pairs([]) == []
    assert find_palindrome_pairs(None) == []

def test_single_word_input():
    """Test input with a single word."""
    words = ["abc"]
    assert find_palindrome_pairs(words) == []

def test_no_palindrome_pairs():
    """Test scenario with no palindrome pairs."""
    words = ["cat", "dog", "bird"]
    assert find_palindrome_pairs(words) == []

def test_multiple_palindrome_pairs():
    """Test scenario with multiple palindrome pairs."""
    words = ["bat", "tab", "cat"]
    expected = [[0, 1], [1, 0]]
    assert sorted(find_palindrome_pairs(words)) == sorted(expected)

def test_short_and_long_words():
    """Test combining short and long words."""
    words = ["a", "abc", "aba"]
    expected = [[1, 2], [2, 1]]
    assert sorted(find_palindrome_pairs(words)) == sorted(expected)

def test_self_palindrome():
    """Test words that are self-palindromes."""
    words = ["racecar", "level", "python"]
    expected = []
    assert find_palindrome_pairs(words) == expected