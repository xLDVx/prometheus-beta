import pytest
from src.array_multiplier import multiply_array_elements

def test_multiply_numbers():
    """Test multiplication of numeric arrays"""
    assert multiply_array_elements([1, 2, 3], [4, 5, 6]) == [4, 10, 18]

def test_multiply_strings():
    """Test multiplication of strings (repetition)"""
    assert multiply_array_elements(['a', 'b'], [3, 2]) == ['aaa', 'bb']

def test_mixed_types():
    """Test multiplication with mixed numeric and string types"""
    assert multiply_array_elements([2, 'a'], [3, 2]) == [6, 'aa']

def test_empty_arrays():
    """Test multiplication of empty arrays"""
    assert multiply_array_elements([], []) == []

def test_different_length_arrays():
    """Test that arrays of different lengths raise a ValueError"""
    with pytest.raises(ValueError, match="Input arrays must have the same length"):
        multiply_array_elements([1, 2], [1, 2, 3])

def test_float_multiplication():
    """Test multiplication of floating-point numbers"""
    assert multiply_array_elements([1.5, 2.0], [2, 3]) == [3.0, 6.0]

def test_complex_multiplication():
    """Test multiplication of complex numbers"""
    assert multiply_array_elements([1+2j, 3+4j], [2, 3]) == [2+4j, 9+12j]