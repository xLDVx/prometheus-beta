import pytest
from src.max_subarray_sum import kadanes_max_subarray_sum

def test_positive_numbers():
    """Test with an array of positive numbers."""
    assert kadanes_max_subarray_sum([1, 2, 3, 4]) == 10

def test_mixed_numbers():
    """Test with mixed positive and negative numbers."""
    assert kadanes_max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_negative_numbers():
    """Test with all negative numbers."""
    assert kadanes_max_subarray_sum([-1, -2, -3, -4]) == -1

def test_single_element():
    """Test with a single element array."""
    assert kadanes_max_subarray_sum([5]) == 5

def test_zero_sum():
    """Test with an array that has zero as the maximum sum."""
    assert kadanes_max_subarray_sum([0, -1, 0]) == 0

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        kadanes_max_subarray_sum([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        kadanes_max_subarray_sum("not a list")

def test_large_numbers():
    """Test with large numbers to ensure no integer overflow issues."""
    assert kadanes_max_subarray_sum([10**6, -10**6, 10**6]) == 10**6

def test_alternating_signs():
    """Test with alternating positive and negative numbers."""
    assert kadanes_max_subarray_sum([1, -1, 1, -1, 1]) == 1