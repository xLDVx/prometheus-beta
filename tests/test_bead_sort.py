import pytest
from src.bead_sort import bead_sort

def test_basic_sorting():
    """Test sorting of a basic list of positive integers."""
    input_list = [5, 3, 1, 4, 2]
    expected = [1, 2, 3, 4, 5]
    assert bead_sort(input_list) == expected

def test_already_sorted_list():
    """Test sorting of an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert bead_sort(input_list) == expected

def test_reverse_sorted_list():
    """Test sorting of a reverse sorted list."""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert bead_sort(input_list) == expected

def test_list_with_duplicates():
    """Test sorting of a list with duplicate values."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert bead_sort(input_list) == expected

def test_empty_list():
    """Test sorting of an empty list."""
    input_list = []
    expected = []
    assert bead_sort(input_list) == expected

def test_single_element_list():
    """Test sorting of a list with a single element."""
    input_list = [42]
    expected = [42]
    assert bead_sort(input_list) == expected

def test_invalid_input_non_list():
    """Test that a non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        bead_sort("not a list")

def test_invalid_input_negative_numbers():
    """Test that a list with negative numbers raises a ValueError."""
    with pytest.raises(ValueError, match="All elements must be positive integers"):
        bead_sort([1, 2, -3, 4])

def test_invalid_input_non_integers():
    """Test that a list with non-integer elements raises a ValueError."""
    with pytest.raises(ValueError, match="All elements must be positive integers"):
        bead_sort([1, 2, 3.5, 4])

def test_large_numbers():
    """Test sorting of a list with larger numbers."""
    input_list = [100, 10, 1000, 1, 10000]
    expected = [1, 10, 100, 1000, 10000]
    assert bead_sort(input_list) == expected