import pytest
from src.odd_integer_filter import filter_and_sort_odd_integers

def test_filter_and_sort_odd_integers_normal_case():
    """Test filtering and sorting odd integers from a mixed list."""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected = [1, 3, 5, 7, 9]
    assert filter_and_sort_odd_integers(input_list) == expected

def test_filter_and_sort_odd_integers_empty_list():
    """Test behavior with an empty list."""
    assert filter_and_sort_odd_integers([]) == []

def test_filter_and_sort_odd_integers_no_odd_numbers():
    """Test behavior when no odd numbers are present."""
    assert filter_and_sort_odd_integers([2, 4, 6, 8]) == []

def test_filter_and_sort_odd_integers_negative_numbers():
    """Test handling of negative odd and even numbers."""
    input_list = [-1, -2, -3, -4, -5, 0, 1, 2, 3, 4, 5]
    expected = [-5, -3, -1, 1, 3, 5]
    assert filter_and_sort_odd_integers(input_list) == expected

def test_filter_and_sort_odd_integers_invalid_input_type():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        filter_and_sort_odd_integers("not a list")

def test_filter_and_sort_odd_integers_invalid_element_type():
    """Test raising TypeError for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        filter_and_sort_odd_integers([1, 2, "3", 4, 5])