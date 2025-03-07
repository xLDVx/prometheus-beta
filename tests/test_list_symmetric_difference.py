import pytest
from src.list_symmetric_difference import symmetric_difference

def test_basic_symmetric_difference():
    """Test symmetric difference with basic lists"""
    result = symmetric_difference([1, 2, 3], [3, 4, 5])
    assert sorted(result) == [1, 2, 4, 5]

def test_empty_lists():
    """Test symmetric difference with empty lists"""
    result = symmetric_difference([], [])
    assert result == []

def test_one_empty_list():
    """Test symmetric difference with one empty list"""
    result = symmetric_difference([1, 2, 3], [])
    assert sorted(result) == [1, 2, 3]

def test_identical_lists():
    """Test symmetric difference with identical lists"""
    result = symmetric_difference([1, 2, 3], [1, 2, 3])
    assert result == []

def test_partially_overlapping_lists():
    """Test symmetric difference with partially overlapping lists"""
    result = symmetric_difference([1, 2, 3, 4], [3, 4, 5, 6])
    assert sorted(result) == [1, 2, 5, 6]

def test_lists_with_duplicates():
    """Test symmetric difference with lists containing duplicates"""
    result = symmetric_difference([1, 1, 2, 3], [3, 3, 4, 5])
    assert sorted(result) == [1, 2, 4, 5]

def test_input_types():
    """Test that function works with different input list types"""
    result = symmetric_difference(
        [1, 'a', True], 
        ['a', 2, False]
    )
    assert set(result) == {1, 2, True, False}