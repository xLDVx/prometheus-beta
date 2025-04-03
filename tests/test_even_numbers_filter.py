import pytest
from src.even_numbers_filter import filter_even_numbers

def test_filter_even_numbers_basic():
    """Test filtering even numbers from a mixed list."""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8]
    assert filter_even_numbers(input_list) == [2, 4, 6, 8]

def test_filter_even_numbers_only_odd():
    """Test input list with only odd numbers."""
    input_list = [1, 3, 5, 7, 9]
    assert filter_even_numbers(input_list) == []

def test_filter_even_numbers_only_even():
    """Test input list with only even numbers."""
    input_list = [2, 4, 6, 8, 10]
    assert filter_even_numbers(input_list) == [2, 4, 6, 8, 10]

def test_filter_even_numbers_empty_list():
    """Test with an empty list."""
    input_list = []
    assert filter_even_numbers(input_list) == []

def test_filter_even_numbers_negative_even():
    """Test with negative even numbers."""
    input_list = [-1, -2, -3, -4, 0, 1, 2]
    assert filter_even_numbers(input_list) == [-2, -4, 0, 2]

def test_invalid_input_non_list():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        filter_even_numbers("not a list")

def test_invalid_input_non_integer():
    """Test that a TypeError is raised for non-integer list elements."""
    with pytest.raises(TypeError, match="All list elements must be integers"):
        filter_even_numbers([1, 2, "3", 4])

def test_time_complexity():
    """Ensure the function can handle large lists efficiently."""
    large_list = list(range(10000))
    result = filter_even_numbers(large_list)
    assert len(result) == 5000  # Half of the numbers should be even
    assert result[0] == 0
    assert result[-1] == 9998