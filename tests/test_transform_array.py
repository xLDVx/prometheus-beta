import pytest
from src.transform_array import transform_array

def test_transform_array_basic():
    """Test basic functionality of transform_array"""
    assert transform_array([0, 1, 2, 3]) == [0, 2, 5, 10]

def test_transform_array_empty():
    """Test transformation of an empty list"""
    assert transform_array([]) == []

def test_transform_array_zero_only():
    """Test list with only zeros"""
    assert transform_array([0, 0, 0]) == [0, 0, 0]

def test_transform_array_large_numbers():
    """Test with larger numbers"""
    assert transform_array([10, 20]) == [101, 401]

def test_transform_array_invalid_input_negative():
    """Test that negative numbers raise a ValueError"""
    with pytest.raises(ValueError, match="All elements must be non-negative integers"):
        transform_array([-1, 2, 3])

def test_transform_array_invalid_input_non_integer():
    """Test that non-integer inputs raise a ValueError"""
    with pytest.raises(ValueError, match="All elements must be non-negative integers"):
        transform_array([1, 2.5, 3])

def test_transform_array_invalid_input_type():
    """Test that non-list inputs raise a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        transform_array("not a list")
        transform_array(123)
        transform_array(None)