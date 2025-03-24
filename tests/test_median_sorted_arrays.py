import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from median_sorted_arrays import find_median_sorted_arrays

def test_median_even_total_length():
    """Test median when total length is even"""
    assert find_median_sorted_arrays([1, 3], [2]) == 2.0
    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5

def test_median_odd_total_length():
    """Test median when total length is odd"""
    assert find_median_sorted_arrays([1, 3], [2, 4]) == 2.5
    assert find_median_sorted_arrays([0, 0], [0, 0]) == 0

def test_empty_array():
    """Test cases with empty arrays"""
    assert find_median_sorted_arrays([], [1]) == 1
    assert find_median_sorted_arrays([2], []) == 2
    assert find_median_sorted_arrays([], [1, 2, 3, 4, 5]) == 3

def test_different_array_sizes():
    """Test median with arrays of different sizes"""
    assert find_median_sorted_arrays([1, 3], [2, 4, 5, 6]) == 3.5
    assert find_median_sorted_arrays([1, 2, 3], [4, 5, 6]) == 3.5

def test_negative_numbers():
    """Test median with negative numbers"""
    assert find_median_sorted_arrays([-5, -3, -1], [-2, 0, 2]) == -1

def test_float_numbers():
    """Test median with floating point numbers"""
    assert find_median_sorted_arrays([1.5, 2.5], [3.5, 4.5]) == 3.0

def test_type_error():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        find_median_sorted_arrays("not a list", [1, 2])
    with pytest.raises(TypeError):
        find_median_sorted_arrays([1, 2], "not a list")

def test_value_error():
    """Test error handling for non-numeric elements"""
    with pytest.raises(ValueError):
        find_median_sorted_arrays([1, 'a'], [2, 3])
    with pytest.raises(ValueError):
        find_median_sorted_arrays([1, 2], ['b', 3])

def test_unsorted_arrays():
    """Test error handling for unsorted arrays"""
    with pytest.raises(ValueError):
        find_median_sorted_arrays([3, 1], [2, 4])