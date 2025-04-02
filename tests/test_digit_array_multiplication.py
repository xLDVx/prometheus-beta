import pytest
from src.digit_array_multiplication import multiply_digit_arrays

def test_basic_multiplication():
    """Test basic multiplication of digit arrays"""
    assert multiply_digit_arrays([1, 2], [3, 4]) == [4, 0, 8]

def test_zero_multiplication():
    """Test multiplication involving zero"""
    assert multiply_digit_arrays([0, 0], [1, 2]) == [0]

def test_single_digit_multiplication():
    """Test multiplication of single-digit arrays"""
    assert multiply_digit_arrays([5], [6]) == [3, 0]

def test_larger_numbers_multiplication():
    """Test multiplication of larger number arrays"""
    assert multiply_digit_arrays([9, 9], [9, 9]) == [9, 8, 0, 1]

def test_unequal_length_arrays():
    """Test that unequal length arrays raise a ValueError"""
    with pytest.raises(ValueError, match="Input arrays must be of equal length"):
        multiply_digit_arrays([1, 2], [3, 4, 5])

def test_invalid_digit_input():
    """Test that arrays with digits outside 0-9 raise a ValueError"""
    with pytest.raises(ValueError, match="All array elements must be single digits"):
        multiply_digit_arrays([1, 10], [3, 4])

def test_edge_case_zeros():
    """Test multiplication with all zeros"""
    assert multiply_digit_arrays([0, 0], [0, 0]) == [0]