import pytest
from src.array_search import find_first_index

def test_find_first_index_basic():
    """Test basic functionality of finding first index"""
    assert find_first_index([1, 2, 3, 4, 2], 2) == 1

def test_find_first_index_not_found():
    """Test when target is not in the array"""
    assert find_first_index([1, 2, 3, 4], 5) == -1

def test_find_first_index_empty_array():
    """Test behavior with an empty array"""
    assert find_first_index([], 1) == -1

def test_find_first_index_first_element():
    """Test finding index of first element"""
    assert find_first_index([1, 2, 3, 4], 1) == 0

def test_find_first_index_last_element():
    """Test finding index of last element"""
    assert find_first_index([1, 2, 3, 4], 4) == 3

def test_find_first_index_multiple_occurrences():
    """Test returning the first occurrence index"""
    assert find_first_index([1, 2, 2, 3, 2], 2) == 1

def test_find_first_index_different_types():
    """Test finding index with different data types"""
    assert find_first_index([1, 'a', True, 2.5], 'a') == 1

def test_find_first_index_none_value():
    """Test finding None value"""
    assert find_first_index([None, 1, 2], None) == 0