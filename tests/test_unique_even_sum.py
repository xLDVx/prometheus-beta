import pytest
from src.unique_even_sum import sum_unique_even_integers

def test_sum_unique_even_integers_basic():
    """Test basic functionality with unique even numbers."""
    assert sum_unique_even_integers([2, 4, 6, 8]) == 0
    assert sum_unique_even_integers([2, 3, 4, 5, 6]) == 2

def test_sum_unique_even_integers_with_duplicates():
    """Test scenarios with duplicate even numbers."""
    assert sum_unique_even_integers([2, 2, 4, 4, 6, 8]) == 8
    assert sum_unique_even_integers([2, 2, 3, 4, 4, 5, 6]) == 6

def test_sum_unique_even_integers_empty_list():
    """Test with an empty list."""
    assert sum_unique_even_integers([]) == 0

def test_sum_unique_even_integers_no_evens():
    """Test with no even numbers."""
    assert sum_unique_even_integers([1, 3, 5, 7]) == 0

def test_sum_unique_even_integers_negative_numbers():
    """Test with negative numbers."""
    assert sum_unique_even_integers([-2, -4, 2, 4]) == 0
    assert sum_unique_even_integers([-2, 2, -4, 4]) == 0

def test_invalid_input_type():
    """Test invalid input types."""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_unique_even_integers(123)
    
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_unique_even_integers([1, 2, '3', 4])
    
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_unique_even_integers([1, 2, 3.5, 4])