import pytest
from src.palindrome_finder import find_palindromic_substrings

def test_empty_string():
    """Test that an empty string returns an empty list."""
    assert find_palindromic_substrings("") == []

def test_single_character():
    """Test that a single character returns a list with that character."""
    assert find_palindromic_substrings("a") == ["a"]

def test_repeated_character():
    """Test a string with repeated characters."""
    result = find_palindromic_substrings("aaa")
    assert set(result) == {"a", "aa", "aaa"}

def test_mixed_palindromes():
    """Test a string with mixed palindromic substrings."""
    result = find_palindromic_substrings("hello")
    assert set(result) == {"h", "e", "l", "l", "o"}

def test_multiple_palindromes():
    """Test a string with multiple palindromic substrings."""
    result = find_palindromic_substrings("abba")
    assert set(result) == {"a", "b", "bb", "abba"}

def test_complex_palindrome():
    """Test a string with complex palindromic substrings."""
    result = find_palindromic_substrings("racecar")
    assert set(result) == {"r", "a", "c", "e", "racecar", "aceca", "cec"}

def test_no_palindromes():
    """Test a string with no palindromes except single characters."""
    result = find_palindromic_substrings("abcde")
    assert set(result) == {"a", "b", "c", "d", "e"}

def test_unicode_palindromes():
    """Test palindromic substrings with unicode characters."""
    result = find_palindromic_substrings("こんにちは")
    assert set(result) == {"こ", "ん", "に", "ち", "は"}