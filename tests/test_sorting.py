import pytest
from src.sorting import insertion_sort

def test_insertion_sort_normal_list():
    """Test sorting a normal list of integers."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert insertion_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_insertion_sort_empty_list():
    """Test sorting an empty list."""
    arr = []
    assert insertion_sort(arr) == []

def test_insertion_sort_single_element():
    """Test sorting a list with a single element."""
    arr = [42]
    assert insertion_sort(arr) == [42]

def test_insertion_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    arr = [1, 2, 3, 4, 5]
    assert insertion_sort(arr) == [1, 2, 3, 4, 5]

def test_insertion_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    arr = [5, 4, 3, 2, 1]
    assert insertion_sort(arr) == [1, 2, 3, 4, 5]

def test_insertion_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert insertion_sort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_insertion_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    arr = [-4, 1, -9, 0, 5, -2]
    assert insertion_sort(arr) == [-9, -4, -2, 0, 1, 5]

def test_insertion_sort_invalid_input():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        insertion_sort("not a list")
        insertion_sort(123)
        insertion_sort(None)

def test_insertion_sort_in_place():
    """Test that the list is sorted in-place."""
    arr = [4, 2, 7, 1, 5, 3]
    result = insertion_sort(arr)
    assert result == [1, 2, 3, 4, 5, 7]
    assert result is arr  # Ensure the same list object is returned