import pytest
from src.list_union import find_list_union

def test_basic_union():
    """Test basic list union functionality"""
    result = find_list_union([1, 2, 3], [3, 4, 5])
    assert result == [1, 2, 3, 4, 5]

def test_preserves_first_occurrence_order():
    """Ensure first occurrence of elements is preserved"""
    result = find_list_union([3, 1, 2], [2, 4, 3])
    assert result == [3, 1, 2, 4]

def test_handles_duplicate_within_lists():
    """Test handling of duplicates within individual lists"""
    result = find_list_union([1, 1, 2, 3], [3, 4, 4, 5])
    assert result == [1, 2, 3, 4, 5]

def test_empty_lists():
    """Test union of empty lists"""
    assert find_list_union([], []) == []
    assert find_list_union([1, 2], []) == [1, 2]
    assert find_list_union([], [3, 4]) == [3, 4]

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        find_list_union("not a list", [1, 2])
    with pytest.raises(TypeError):
        find_list_union([1, 2], "not a list")
    with pytest.raises(TypeError):
        find_list_union(None, [1, 2])

def test_mixed_type_lists():
    """Test union of lists with mixed types"""
    result = find_list_union([1, 'a', 2], ['a', 3, 4])
    assert result == [1, 'a', 2, 3, 4]