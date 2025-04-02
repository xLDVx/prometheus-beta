import pytest
import math
from src.bitonic_sort import bitonic_sort

def test_bitonic_sort_ascending():
    """Test bitonic sort in ascending order"""
    test_list = [3, 7, 1, 5, 2, 8, 4, 6]
    result = bitonic_sort(test_list)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8]

def test_bitonic_sort_descending():
    """Test bitonic sort in descending order"""
    test_list = [3, 7, 1, 5, 2, 8, 4, 6]
    result = bitonic_sort(test_list, ascending=False)
    assert result == [8, 7, 6, 5, 4, 3, 2, 1]

def test_bitonic_sort_empty_list():
    """Test bitonic sort with an empty list of size 2^0"""
    test_list = []
    with pytest.raises(ValueError, match="List length must be a power of 2"):
        bitonic_sort(test_list)

def test_bitonic_sort_non_power_of_two():
    """Test bitonic sort with a list not of power of 2 length"""
    test_list = [3, 7, 1, 5, 2]
    with pytest.raises(ValueError, match="List length must be a power of 2"):
        bitonic_sort(test_list)

def test_bitonic_sort_invalid_input():
    """Test bitonic sort with non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        bitonic_sort("not a list")

def test_bitonic_sort_preserves_original():
    """Test that original list is not modified"""
    test_list = [3, 7, 1, 5, 2, 8, 4, 6]
    original = test_list.copy()
    bitonic_sort(test_list)
    assert test_list == original

def test_bitonic_sort_large_power_of_two():
    """Test bitonic sort with a larger power of 2 list"""
    # Generate a list of powers of 2 in random order
    import random
    size = 16
    test_list = list(range(1, size + 1))
    random.shuffle(test_list)
    
    result = bitonic_sort(test_list)
    assert result == list(range(1, size + 1))

def test_bitonic_sort_repeated_elements():
    """Test bitonic sort with repeated elements"""
    test_list = [3, 3, 1, 5, 1, 8, 3, 6]
    result = bitonic_sort(test_list)
    assert result == [1, 1, 3, 3, 3, 5, 6, 8]