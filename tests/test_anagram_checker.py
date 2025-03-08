import pytest
from src.anagram_checker import anagram_checker

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert anagram_checker("listen", "silent") == True
    assert anagram_checker("hello", "olleh") == True

def test_case_insensitive():
    """Test that the function is case-insensitive"""
    assert anagram_checker("Debit Card", "Bad Credit") == True
    assert anagram_checker("RACE", "care") == True

def test_non_anagrams():
    """Test words that are not anagrams"""
    assert anagram_checker("python", "java") == False
    assert anagram_checker("hello", "world") == False

def test_different_lengths():
    """Test words of different lengths"""
    assert anagram_checker("short", "shorter") == False
    assert anagram_checker("a", "ab") == False

def test_empty_string_error():
    """Test error handling for empty strings"""
    with pytest.raises(ValueError):
        anagram_checker("", "test")
    with pytest.raises(ValueError):
        anagram_checker("test", "")
    with pytest.raises(ValueError):
        anagram_checker("", "")

def test_non_string_input():
    """Test error handling for non-string inputs"""
    with pytest.raises(TypeError):
        anagram_checker(123, "test")
    with pytest.raises(TypeError):
        anagram_checker("test", [1, 2, 3])
    with pytest.raises(TypeError):
        anagram_checker(None, None)

def test_spaces_and_special_characters():
    """Test handling of spaces and special characters"""
    assert anagram_checker("a gentleman", "elegant man") == True
    assert anagram_checker("rail safety", "fairy tales") == True