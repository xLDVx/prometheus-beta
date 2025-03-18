import pytest
import random
from src.smooth_sort import smooth_sort

def test_empty_list():
    """Test sorting an empty list."""
    assert smooth_sort([]) == []

def test_single_element_list():
    """Test sorting a list with a single element."""
    assert smooth_sort([42]) == [42]

def test_already_sorted_list():
    """Test sorting an already sorted list."""
    sorted_list = [1, 2, 3, 4, 5]
    assert smooth_sort(sorted_list) == sorted_list

def test_reverse_sorted_list():
    """Test sorting a reverse sorted list."""
    reverse_sorted = [5, 4, 3, 2, 1]
    assert smooth_sort(reverse_sorted) == [1, 2, 3, 4, 5]

def test_random_integers():
    """Test sorting a list of random integers."""
    # Generate a list of 100 random integers
    random_list = [random.randint(-1000, 1000) for _ in range(100)]
    sorted_list = smooth_sort(random_list)
    
    # Verify the result is sorted
    assert sorted_list == sorted(random_list)
    # Verify the contents are the same
    assert set(sorted_list) == set(random_list)

def test_list_with_duplicates():
    """Test sorting a list with duplicate elements."""
    duplicate_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert smooth_sort(duplicate_list) == sorted(duplicate_list)

def test_negative_numbers():
    """Test sorting a list with negative numbers."""
    negative_list = [-5, -2, -8, -1, -9]
    assert smooth_sort(negative_list) == sorted(negative_list)

def test_mixed_numbers():
    """Test sorting a list with mixed positive and negative numbers."""
    mixed_list = [-5, 3, 0, -2, 8, -1, 4]
    assert smooth_sort(mixed_list) == sorted(mixed_list)

def test_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        smooth_sort("not a list")
    
    with pytest.raises(TypeError):
        smooth_sort(123)
    
    with pytest.raises(TypeError):
        smooth_sort(None)

def test_original_list_unchanged():
    """Verify that the original list remains unchanged."""
    original = [5, 2, 8, 1, 9]
    smooth_sort(original)
    assert original == [5, 2, 8, 1, 9]