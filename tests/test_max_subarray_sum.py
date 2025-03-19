import pytest
from src.max_subarray_sum import max_subarray_sum

def test_positive_numbers():
    """Test max subarray sum with all positive numbers."""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_mixed_numbers():
    """Test max subarray sum with mixed positive and negative numbers."""
    assert max_subarray_sum([1, -2, 3, 4, -1, 5]) == 11

def test_all_negative_numbers():
    """Test max subarray sum with all negative numbers."""
    assert max_subarray_sum([-1, -2, -3, -4]) == -1

def test_single_element_list():
    """Test max subarray sum with a single element list."""
    assert max_subarray_sum([42]) == 42

def test_zero_in_list():
    """Test max subarray sum with zero in the list."""
    assert max_subarray_sum([-2, 0, 3, -1, 2]) == 4

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        max_subarray_sum("not a list")

def test_empty_list():
    """Test that ValueError is raised for an empty list."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        max_subarray_sum([])