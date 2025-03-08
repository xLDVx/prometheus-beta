import pytest
from src.unique_even_filter import filter_unique_even_numbers

def test_filter_unique_even_numbers_basic():
    """Test basic functionality of filtering unique even numbers."""
    input_list = [1, 2, 3, 4, 2, 5, 6, 4, 7, 8]
    expected = [2, 4, 6, 8]
    assert filter_unique_even_numbers(input_list) == expected

def test_filter_unique_even_numbers_empty_list():
    """Test filtering an empty list."""
    assert filter_unique_even_numbers([]) == []

def test_filter_unique_even_numbers_no_even_numbers():
    """Test a list with no even numbers."""
    input_list = [1, 3, 5, 7]
    assert filter_unique_even_numbers(input_list) == []

def test_filter_unique_even_numbers_only_even_numbers():
    """Test a list with only even numbers, some repeated."""
    input_list = [2, 4, 2, 6, 4, 8]
    expected = [2, 4, 6, 8]
    assert filter_unique_even_numbers(input_list) == expected

def test_filter_unique_even_numbers_negative_numbers():
    """Test handling of negative even numbers."""
    input_list = [-1, -2, 3, -2, 4, -4, 5]
    expected = [-2, 4, -4]
    assert filter_unique_even_numbers(input_list) == expected

def test_filter_unique_even_numbers_zero():
    """Test handling of zero."""
    input_list = [0, 1, 0, 2, 3]
    expected = [0, 2]
    assert filter_unique_even_numbers(input_list) == expected