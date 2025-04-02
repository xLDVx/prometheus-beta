import pytest
from src.selection_sort import selection_sort

def test_selection_sort_basic():
    """Test sorting a list of integers"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert selection_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_selection_sort_empty_list():
    """Test sorting an empty list"""
    arr = []
    assert selection_sort(arr) == []

def test_selection_sort_single_element():
    """Test sorting a list with a single element"""
    arr = [42]
    assert selection_sort(arr) == [42]

def test_selection_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    arr = [-4, 1, -9, 0, 5]
    assert selection_sort(arr) == [-9, -4, 0, 1, 5]

def test_selection_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    arr = [1, 2, 3, 4, 5]
    assert selection_sort(arr) == [1, 2, 3, 4, 5]

def test_selection_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    arr = [5, 4, 3, 2, 1]
    assert selection_sort(arr) == [1, 2, 3, 4, 5]

def test_selection_sort_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert selection_sort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_selection_sort_floats():
    """Test sorting a list of floating-point numbers"""
    arr = [3.14, 2.71, 1.41, 0.58]
    assert selection_sort(arr) == [0.58, 1.41, 2.71, 3.14]

def test_selection_sort_invalid_input_type():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        selection_sort("not a list")

def test_selection_sort_uncomparable_elements():
    """Test that a TypeError is raised for uncomparable elements"""
    with pytest.raises(TypeError, match="List contains elements that cannot be compared"):
        selection_sort([1, "a", 3])

def test_selection_sort_in_place():
    """Test that the original list is modified in-place"""
    arr = [5, 2, 9, 1, 7]
    original_id = id(arr)
    selection_sort(arr)
    assert id(arr) == original_id
    assert arr == [1, 2, 5, 7, 9]