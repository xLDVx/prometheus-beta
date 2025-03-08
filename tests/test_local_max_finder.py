import pytest
from src.local_max_finder import find_local_max_values


def test_find_local_max_values_basic():
    """Test basic scenarios of finding local maximums"""
    assert find_local_max_values([1, 3, 2, 4, 1, 5]) == [3, 4, 5]
    assert find_local_max_values([5, 3, 7, 1, 2]) == [5, 7]


def test_find_local_max_values_single_element():
    """Test single element list returns the element"""
    assert find_local_max_values([42]) == [42]


def test_find_local_max_values_ascending():
    """Test ascending list returns last element"""
    assert find_local_max_values([1, 2, 3, 4, 5]) == [5]


def test_find_local_max_values_descending():
    """Test descending list returns first element"""
    assert find_local_max_values([5, 4, 3, 2, 1]) == [5]


def test_find_local_max_values_all_equal():
    """Test list with all equal elements returns that element"""
    assert find_local_max_values([2, 2, 2, 2]) == [2]


def test_find_local_max_values_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        find_local_max_values("not a list")
    
    with pytest.raises(ValueError):
        find_local_max_values([])


def test_find_local_max_values_with_negatives():
    """Test local max finding with negative numbers"""
    assert find_local_max_values([-1, -3, -2, -4, -1, -5]) == [-1, -2]