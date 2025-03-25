import pytest
from src.string_permutations import generate_unique_permutations

def test_unique_permutations_basic():
    """Test basic string permutations."""
    result = generate_unique_permutations("abc")
    assert set(result) == set(["abc", "acb", "bac", "bca", "cab", "cba"])
    assert len(result) == 6

def test_unique_permutations_with_duplicates():
    """Test permutations with duplicate characters."""
    result = generate_unique_permutations("abb")
    assert set(result) == set(["abb", "bab", "bba"])
    assert len(result) == 3

def test_unique_permutations_single_char():
    """Test permutations with a single character."""
    result = generate_unique_permutations("a")
    assert result == ["a"]

def test_unique_permutations_empty_string():
    """Test permutations with an empty string."""
    result = generate_unique_permutations("")
    assert result == []

def test_unique_permutations_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Input must be a string"):
        generate_unique_permutations(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        generate_unique_permutations(None)

def test_unique_permutations_sorted_output():
    """Test that output is sorted."""
    result = generate_unique_permutations("cab")
    assert result == ["abc", "acb", "bac", "bca", "cab", "cba"]

def test_unique_permutations_long_string():
    """Test permutations with a longer string."""
    result = generate_unique_permutations("abcd")
    assert len(result) == 24  # 4! = 24 unique permutations