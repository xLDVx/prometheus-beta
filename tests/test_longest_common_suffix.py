import pytest
from src.longest_common_suffix import find_longest_common_suffix

def test_basic_common_suffix():
    """Test finding a basic common suffix."""
    result = find_longest_common_suffix(["flower", "tower", "power"])
    assert result in ["ower", "r"], f"Expected 'ower' or 'r', got {result}"

def test_single_string():
    """Test when only one string is in the list."""
    assert find_longest_common_suffix(["hello"]) == "hello"

def test_no_common_suffix():
    """Test when there is no common suffix."""
    assert find_longest_common_suffix(["abc", "def", "ghi"]) == ""

def test_empty_list():
    """Test with an empty list."""
    assert find_longest_common_suffix([]) == ""

def test_some_common_suffix():
    """Test a list with some strings sharing a suffix."""
    result = find_longest_common_suffix(["cat", "bat", "hat"])
    assert result in ["at", "t"], f"Expected 'at' or 't', got {result}"

def test_full_match():
    """Test when all strings are identical."""
    assert find_longest_common_suffix(["hello", "hello", "hello"]) == "hello"

def test_invalid_input_not_list():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of strings"):
        find_longest_common_suffix("not a list")

def test_invalid_input_non_string_elements():
    """Test raising TypeError for list with non-string elements."""
    with pytest.raises(TypeError, match="All elements must be strings"):
        find_longest_common_suffix(["string", 123, "another"])

def test_different_length_strings():
    """Test finding common suffix with strings of different lengths."""
    assert find_longest_common_suffix(["longer", "short"]) == ""

def test_partial_common_suffix():
    """Test finding a partial common suffix."""
    result = find_longest_common_suffix(["coding", "decoding", "encoding"])
    assert result in ["oding", "ing"], f"Expected 'oding' or 'ing', got {result}"