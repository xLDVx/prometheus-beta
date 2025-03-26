import pytest
from src.longest_palindrome import longest_palindromic_substring

def test_basic_palindromes():
    assert longest_palindromic_substring("babad") in ["bab", "aba"]
    assert longest_palindromic_substring("cbbd") == "bb"

def test_edge_cases():
    assert longest_palindromic_substring("") == ""
    assert longest_palindromic_substring("a") == "a"
    assert longest_palindromic_substring("ac") == "a"

def test_full_string_palindromes():
    assert longest_palindromic_substring("racecar") == "racecar"
    assert longest_palindromic_substring("level") == "level"

def test_multiple_palindromes():
    assert longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"

def test_even_length_palindromes():
    assert longest_palindromic_substring("abba") == "abba"
    assert longest_palindromic_substring("abcda") == "a"

def test_no_palindrome_longer_than_single_char():
    assert longest_palindromic_substring("abc") in ["a", "b", "c"]

def test_special_characters():
    assert longest_palindromic_substring("a!!a") == "a!!a"

def test_long_string():
    long_string = "a" * 1000 + "b" + "a" * 1000
    assert longest_palindromic_substring(long_string) == "a" * 1000 + "b" + "a" * 1000