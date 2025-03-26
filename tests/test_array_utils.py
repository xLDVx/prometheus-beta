import pytest
from src.array_utils import remove_duplicates_and_sort

def test_remove_duplicates_and_sort_basic():
    """Test basic functionality of removing duplicates and sorting"""
    assert remove_duplicates_and_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 2, 3, 4, 5, 6, 9]

def test_remove_duplicates_and_sort_already_sorted():
    """Test when input is already sorted"""
    assert remove_duplicates_and_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_and_sort_reverse_sorted():
    """Test when input is reverse sorted"""
    assert remove_duplicates_and_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_and_sort_all_duplicates():
    """Test when all elements are duplicates"""
    assert remove_duplicates_and_sort([1, 1, 1, 1, 1]) == [1]

def test_remove_duplicates_and_sort_empty_list():
    """Test with an empty list"""
    assert remove_duplicates_and_sort([]) == []

def test_remove_duplicates_and_sort_single_element():
    """Test with a single element"""
    assert remove_duplicates_and_sort([42]) == [42]

def test_remove_duplicates_and_sort_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates_and_sort("not a list")

def test_remove_duplicates_and_sort_invalid_element_type():
    """Test raising TypeError for non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        remove_duplicates_and_sort([1, 2, "3", 4])

def test_remove_duplicates_and_sort_negative_numbers():
    """Test with negative numbers"""
    assert remove_duplicates_and_sort([-3, -1, -4, -1, -5, 0, 2]) == [-5, -4, -3, -1, 0, 2]