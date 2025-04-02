import pytest
from src.odd_number_filter import filter_odd_numbers

def test_filter_odd_numbers_basic():
    """Test filtering odd numbers from a mixed list of integers."""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert filter_odd_numbers(input_list) == [1, 3, 5, 7, 9]

def test_filter_odd_numbers_empty_list():
    """Test filtering an empty list."""
    assert filter_odd_numbers([]) == []

def test_filter_odd_numbers_no_odds():
    """Test a list with no odd numbers."""
    input_list = [2, 4, 6, 8, 10]
    assert filter_odd_numbers(input_list) == []

def test_filter_odd_numbers_only_odds():
    """Test a list with only odd numbers."""
    input_list = [1, 3, 5, 7, 9]
    assert filter_odd_numbers(input_list) == [1, 3, 5, 7, 9]

def test_filter_odd_numbers_negative_numbers():
    """Test filtering odd numbers including negative numbers."""
    input_list = [-1, -2, 0, 1, 2]
    assert filter_odd_numbers(input_list) == [-1, 1]

def test_filter_odd_numbers_invalid_input_non_list():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        filter_odd_numbers("not a list")

def test_filter_odd_numbers_invalid_input_non_integers():
    """Test that a TypeError is raised for lists with non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        filter_odd_numbers([1, 2, "3", 4.5])