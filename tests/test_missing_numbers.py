import pytest
from src.missing_numbers import find_missing_numbers

def test_missing_numbers_ascending():
    """Test finding missing numbers in an ascending sorted array."""
    assert find_missing_numbers([1, 3, 5, 7]) == [2, 4, 6]

def test_missing_numbers_descending():
    """Test finding missing numbers in a descending sorted array."""
    assert find_missing_numbers([7, 5, 3, 1]) == [6, 4, 2]

def test_no_missing_numbers_ascending():
    """Test an array with no missing numbers in ascending order."""
    assert find_missing_numbers([1, 2, 3, 4, 5]) == []

def test_no_missing_numbers_descending():
    """Test an array with no missing numbers in descending order."""
    assert find_missing_numbers([5, 4, 3, 2, 1]) == []

def test_single_element_array():
    """Test an array with a single element."""
    assert find_missing_numbers([5]) == [1, 2, 3, 4]

def test_large_range():
    """Test an array with a larger range of missing numbers."""
    assert find_missing_numbers([1, 5, 10]) == [2, 3, 4, 6, 7, 8, 9]

def test_invalid_input_empty():
    """Test handling of an empty input."""
    with pytest.raises(ValueError):
        find_missing_numbers([])

def test_invalid_input_non_positive():
    """Test handling of non-positive integers."""
    with pytest.raises(ValueError):
        find_missing_numbers([1, 2, -3, 4])

def test_invalid_input_non_integer():
    """Test handling of non-integer inputs."""
    with pytest.raises(ValueError):
        find_missing_numbers([1, 2, 3.5, 4])