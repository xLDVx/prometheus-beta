import pytest
from src.vowel_counter import count_vowels_and_consonants

def test_basic_string():
    """Test a basic string with mixed vowels and consonants."""
    result = count_vowels_and_consonants("hello")
    assert result == {'vowels': 2, 'consonants': 3}

def test_empty_string():
    """Test an empty string."""
    result = count_vowels_and_consonants("")
    assert result == {'vowels': 0, 'consonants': 0}

def test_all_vowels():
    """Test a string with only vowels."""
    result = count_vowels_and_consonants("aeiou")
    assert result == {'vowels': 5, 'consonants': 0}

def test_all_consonants():
    """Test a string with only consonants."""
    result = count_vowels_and_consonants("rhythm")
    assert result == {'vowels': 0, 'consonants': 6}

def test_mixed_case():
    """Test a string with mixed case."""
    result = count_vowels_and_consonants("HeLLo WoRLd")
    assert result == {'vowels': 3, 'consonants': 7}

def test_with_numbers_and_symbols():
    """Test a string with numbers and symbols."""
    result = count_vowels_and_consonants("hello123! world")
    assert result == {'vowels': 3, 'consonants': 7}

def test_non_english_characters():
    """Test handling of non-English characters."""
    result = count_vowels_and_consonants("héllo世界")
    assert result == {'vowels': 2, 'consonants': 3}

def test_invalid_input_type():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        count_vowels_and_consonants(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        count_vowels_and_consonants(None)