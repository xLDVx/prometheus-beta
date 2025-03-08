import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal"""
    assert remove_duplicates([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_empty_list():
    """Test empty list handling"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates"""
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_all_duplicates():
    """Test list with all duplicates"""
    assert remove_duplicates([1, 1, 1, 1]) == [1]

def test_remove_duplicates_mixed_types():
    """Test list with mixed types"""
    assert remove_duplicates([1, '1', 2, '2', 1, '1']) == [1, '1', 2, '2']

def test_remove_duplicates_invalid_input():
    """Test invalid input type"""
    with pytest.raises(TypeError):
        remove_duplicates("not a list")
    with pytest.raises(TypeError):
        remove_duplicates(123)
    with pytest.raises(TypeError):
        remove_duplicates(None)