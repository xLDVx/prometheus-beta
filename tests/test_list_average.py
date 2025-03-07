import pytest
from src.list_average import calculate_average

def test_calculate_average_basic():
    """Test basic average calculation."""
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0

def test_calculate_average_floats():
    """Test average calculation with floating point numbers."""
    assert calculate_average([1.5, 2.5, 3.5]) == 2.5

def test_calculate_average_single_element():
    """Test average calculation with a single element."""
    assert calculate_average([42]) == 42.0

def test_calculate_average_empty_list():
    """Test that ValueError is raised for empty list."""
    with pytest.raises(ValueError, match="Cannot calculate average of an empty list"):
        calculate_average([])

def test_calculate_average_non_list_input():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_average("not a list")

def test_calculate_average_non_numeric_list():
    """Test that TypeError is raised for list with non-numeric elements."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_average([1, 2, "three", 4])

def test_calculate_average_mixed_numeric_types():
    """Test average calculation with mixed integer and float types."""
    assert calculate_average([1, 2.5, 3, 4.5]) == 2.75