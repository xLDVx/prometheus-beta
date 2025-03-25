import pytest
from src.frequency_sort import sort_by_frequency

def test_basic_frequency_sort():
    """Test basic functionality of frequency sorting"""
    input_list = [1, 1, 2, 2, 2, 3]
    expected = [3, 1, 1, 2, 2, 2]
    assert sort_by_frequency(input_list) == expected

def test_empty_list():
    """Test sorting an empty list"""
    assert sort_by_frequency([]) == []

def test_single_element_list():
    """Test a list with a single element"""
    assert sort_by_frequency([5]) == [5]

def test_all_same_frequency():
    """Test list where all elements have same frequency"""
    input_list = [1, 2, 3, 4]
    # Should sort by value when frequencies are the same
    expected = [1, 2, 3, 4]
    assert sort_by_frequency(input_list) == expected

def test_complex_frequency_sorting():
    """Test more complex frequency sorting scenario"""
    input_list = [5, 5, 4, 4, 4, 3, 3, 3, 3]
    expected = [5, 5, 4, 4, 4, 3, 3, 3, 3]
    assert sort_by_frequency(input_list) == expected

def test_negative_numbers():
    """Test sorting with negative numbers"""
    input_list = [-1, -1, 2, 2, 2, 3, 3]
    expected = [-1, -1, 3, 3, 2, 2, 2]
    assert sort_by_frequency(input_list) == expected