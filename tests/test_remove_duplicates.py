import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal."""
    assert remove_duplicates([1, 2, 3, 2, 1]) == [1, 2, 3]

def test_remove_duplicates_empty_list():
    """Test with an empty list."""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates."""
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_preserve_order():
    """Test that original order is preserved."""
    assert remove_duplicates([3, 1, 2, 3, 1, 4, 2]) == [3, 1, 2, 4]

def test_remove_duplicates_mixed_types():
    """Test duplicate removal with mixed types."""
    assert remove_duplicates([1, 'a', 2, 'a', 1, 3]) == [1, 'a', 2, 3]

def test_remove_duplicates_invalid_input():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates(None)