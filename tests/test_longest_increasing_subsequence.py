import pytest
from src.longest_increasing_subsequence import find_longest_increasing_subsequence

def test_normal_case():
    """Test a standard case of finding LIS"""
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    assert find_longest_increasing_subsequence(arr) == [10, 22, 33, 50, 60]

def test_already_sorted():
    """Test an already sorted array"""
    arr = [1, 2, 3, 4, 5]
    assert find_longest_increasing_subsequence(arr) == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    """Test a reverse sorted array"""
    arr = [5, 4, 3, 2, 1]
    assert find_longest_increasing_subsequence(arr) == [5]

def test_empty_list():
    """Test an empty list"""
    arr = []
    assert find_longest_increasing_subsequence(arr) == []

def test_single_element():
    """Test a list with a single element"""
    arr = [42]
    assert find_longest_increasing_subsequence(arr) == [42]

def test_duplicate_elements():
    """Test a list with duplicate elements"""
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    result = find_longest_increasing_subsequence(arr)
    assert len(result) == 6  # Longest increasing subsequence length
    assert all(result[i] < result[i+1] for i in range(len(result)-1))  # Strictly increasing
    assert set(result).issubset(set(arr))  # All elements in original array

def test_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_longest_increasing_subsequence("not a list")

def test_non_comparable_elements():
    """Test raising ValueError for non-comparable elements"""
    class NonComparable:
        def __init__(self, value):
            self.value = value
    
    with pytest.raises(ValueError, match="List contains non-comparable elements"):
        find_longest_increasing_subsequence([NonComparable(1), NonComparable(2)])

def test_mixed_types():
    """Test LIS with mixed comparable types"""
    arr = [1, 2.5, 3, 4.5, 5]
    assert find_longest_increasing_subsequence(arr) == [1, 2.5, 3, 4.5, 5]