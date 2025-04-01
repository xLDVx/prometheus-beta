import pytest
from src.array_sum import calculate_array_sum

def test_sum_of_integers():
    """Test summing a list of integers."""
    assert calculate_array_sum([1, 2, 3, 4, 5]) == 15

def test_sum_of_floats():
    """Test summing a list of floats."""
    assert calculate_array_sum([1.5, 2.5, 3.0]) == 7.0

def test_sum_of_mixed_numbers():
    """Test summing a list of mixed integers and floats."""
    assert calculate_array_sum([1, 2.5, 3, 4.5]) == 11.0

def test_empty_list():
    """Test summing an empty list."""
    assert calculate_array_sum([]) == 0

def test_single_element_list():
    """Test summing a list with a single element."""
    assert calculate_array_sum([42]) == 42

def test_negative_numbers():
    """Test summing a list with negative numbers."""
    assert calculate_array_sum([-1, -2, -3]) == -6

def test_invalid_input_type():
    """Test that a non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_array_sum("not a list")

def test_non_numeric_elements():
    """Test that a list with non-numeric elements raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_array_sum([1, 2, "three", 4])