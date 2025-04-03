import pytest
from src.list_pair_products import calculate_pair_products

def test_normal_list():
    """Test calculation with a standard list of integers."""
    result = calculate_pair_products([1, 2, 3])
    assert result == [2, 3, 6]

def test_list_with_negative_numbers():
    """Test calculation with negative numbers."""
    result = calculate_pair_products([-1, 2, -3])
    assert result == [-2, 3, -6]

def test_list_with_zeros():
    """Test calculation with zeros in the list."""
    result = calculate_pair_products([0, 1, 2])
    assert result == [0, 0, 2]

def test_list_with_large_numbers():
    """Test calculation with larger numbers."""
    result = calculate_pair_products([10, 20, 30])
    assert result == [200, 300, 600]

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_pair_products(123)

def test_invalid_element_type():
    """Test that TypeError is raised for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        calculate_pair_products([1, 2, '3'])

def test_insufficient_list_length():
    """Test that ValueError is raised for lists with fewer than 2 elements."""
    with pytest.raises(ValueError, match="Input list must have at least 2 elements"):
        calculate_pair_products([1])

def test_empty_list():
    """Test that ValueError is raised for empty list."""
    with pytest.raises(ValueError, match="Input list must have at least 2 elements"):
        calculate_pair_products([])