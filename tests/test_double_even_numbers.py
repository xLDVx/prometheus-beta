import pytest
from src.double_even_numbers import double_even_numbers

def test_basic_functionality():
    """Test basic doubling of even numbers"""
    assert double_even_numbers([1, 2, 3, 4, 5]) == [1, 4, 3, 8, 5]

def test_empty_list():
    """Test with an empty list"""
    assert double_even_numbers([]) == []

def test_only_odd_numbers():
    """Test with only odd numbers"""
    assert double_even_numbers([1, 3, 5, 7]) == [1, 3, 5, 7]

def test_only_even_numbers():
    """Test with only even numbers"""
    assert double_even_numbers([2, 4, 6, 8]) == [4, 8, 12, 16]

def test_negative_numbers():
    """Test with negative numbers"""
    assert double_even_numbers([-1, -2, -3, -4]) == [-1, -4, -3, -8]

def test_zero():
    """Test zero behavior"""
    assert double_even_numbers([0, 1, 2]) == [0, 1, 4]

def test_float_numbers():
    """Test with float numbers"""
    assert double_even_numbers([1.5, 2.0, 3, 4.0]) == [1.5, 4.0, 3, 8.0]

def test_invalid_input_type():
    """Test with invalid input type"""
    with pytest.raises(TypeError, match="Input must be a list"):
        double_even_numbers("not a list")

def test_invalid_element_type():
    """Test with list containing non-numeric elements"""
    with pytest.raises(TypeError, match="All elements must be numbers"):
        double_even_numbers([1, 2, "three", 4])