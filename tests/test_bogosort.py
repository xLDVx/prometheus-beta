import pytest
import random
from src.bogosort import bogosort

def test_bogosort_empty_list():
    """Test sorting an empty list"""
    assert bogosort([]) == []

def test_bogosort_single_element():
    """Test sorting a single-element list"""
    assert bogosort([5]) == [5]

def test_bogosort_already_sorted():
    """Test sorting a list that is already sorted"""
    sorted_list = [1, 2, 3, 4, 5]
    assert bogosort(sorted_list) == sorted_list

def test_bogosort_unsorted_list():
    """Test sorting an unsorted list of integers"""
    # Set a fixed seed for reproducibility
    random.seed(42)
    unsorted_list = [5, 2, 8, 1, 9]
    assert bogosort(unsorted_list) == [1, 2, 5, 8, 9]

def test_bogosort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    unsorted_list = [3, 1, 4, 1, 5, 9, 2, 6]
    assert bogosort(unsorted_list) == [1, 1, 2, 3, 4, 5, 6, 9]

def test_bogosort_with_floats():
    """Test sorting a list of floating-point numbers"""
    unsorted_list = [3.14, 2.71, 1.41, 0.58]
    assert bogosort(unsorted_list) == [0.58, 1.41, 2.71, 3.14]

def test_bogosort_invalid_input():
    """Test that TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError):
        bogosort("not a list")
    with pytest.raises(TypeError):
        bogosort(123)

def test_bogosort_preserves_original_list():
    """Test that the original list is not modified"""
    original_list = [5, 2, 8, 1, 9]
    bogosort(original_list)
    assert original_list == [5, 2, 8, 1, 9]