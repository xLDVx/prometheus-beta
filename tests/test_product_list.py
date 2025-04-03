import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from product_list import product_of_others

def test_basic_product_list():
    """Test basic functionality with a list of integers."""
    assert product_of_others([1, 2, 3, 4]) == [24, 12, 8, 6]

def test_empty_list():
    """Test empty list input."""
    assert product_of_others([]) == []

def test_single_element_list():
    """Test list with a single element."""
    assert product_of_others([5]) == [1]

def test_float_inputs():
    """Test list with float inputs."""
    assert product_of_others([1.0, 2.0, 3.0]) == [6.0, 3.0, 2.0]

def test_mixed_int_float():
    """Test list with mixed integer and float inputs."""
    assert product_of_others([1, 2.5, 3]) == [7.5, 3.0, 2.5]

def test_zero_in_list():
    """Test list containing zero."""
    assert product_of_others([1, 2, 0, 4]) == [0, 0, 8, 0]

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        product_of_others("not a list")

def test_non_numeric_elements():
    """Test that ValueError is raised for non-numeric elements."""
    with pytest.raises(ValueError, match="All list elements must be numeric"):
        product_of_others([1, 2, "three"])

def test_large_numbers():
    """Test functionality with larger numbers."""
    assert product_of_others([10, 20, 30]) == [6000, 3000, 2000]

def test_negative_numbers():
    """Test functionality with negative numbers."""
    assert product_of_others([-1, 2, -3]) == [-6, 3, 2]