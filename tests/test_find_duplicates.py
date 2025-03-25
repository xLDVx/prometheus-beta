import pytest
from src.find_duplicates import find_duplicates

def test_basic_duplicates():
    """Test finding basic duplicates in a list."""
    assert find_duplicates([1, 2, 3, 4, 2, 5, 6, 3]) == [2, 3]

def test_multiple_duplicates():
    """Test a list with multiple duplicates of the same number."""
    assert find_duplicates([1, 1, 1, 1]) == [1]

def test_no_duplicates():
    """Test a list with no duplicates."""
    assert find_duplicates([1, 2, 3, 4, 5]) == []

def test_empty_list():
    """Test an empty list."""
    assert find_duplicates([]) == []

def test_preserves_first_appearance_order():
    """Test that duplicates are returned in order of their first appearance."""
    assert find_duplicates([3, 1, 2, 3, 4, 2, 1, 5]) == [3, 1, 2]

def test_large_list():
    """Test with a larger list of numbers."""
    numbers = list(range(1000)) + list(range(500))
    assert find_duplicates(numbers) == list(range(500))

def test_negative_numbers():
    """Test with negative numbers."""
    assert find_duplicates([-1, -2, -1, -3, -2]) == [-1, -2]