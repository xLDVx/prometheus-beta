import pytest
from src.number_difference import find_min_max_difference

def test_basic_difference():
    """Test basic functionality with positive integers."""
    assert find_min_max_difference("1,5,3,9") == 8

def test_negative_numbers():
    """Test with negative numbers."""
    assert find_min_max_difference("-5,3,-1,7") == 12

def test_mixed_numbers():
    """Test with mixed positive and negative numbers."""
    assert find_min_max_difference("-10,5,0,15") == 25

def test_single_number():
    """Test with a single number."""
    assert find_min_max_difference("42") == 0

def test_empty_string_raises_error():
    """Test that empty string raises a ValueError."""
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        find_min_max_difference("")

def test_whitespace_numbers():
    """Test with whitespace around numbers."""
    assert find_min_max_difference(" 1 , 5 , 3 , 9 ") == 8

def test_invalid_input_raises_error():
    """Test that non-integer input raises a ValueError."""
    with pytest.raises(ValueError):
        find_min_max_difference("1,2,three,4")

def test_only_comma_raises_error():
    """Test that a string with only commas raises a ValueError."""
    with pytest.raises(ValueError, match="No valid numbers found"):
        find_min_max_difference(",")