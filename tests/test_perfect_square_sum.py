import pytest
import math
from src.perfect_square_sum import sum_perfect_squares_from_set

def test_basic_perfect_squares():
    """Test basic set of positive integers with perfect squares."""
    result = sum_perfect_squares_from_set({1, 2, 3, 4})
    assert result == 30  # 1^2 + 2^2 + 3^2 + 4^2

def test_empty_set():
    """Test empty set returns zero."""
    assert sum_perfect_squares_from_set(set()) == 0

def test_no_perfect_squares():
    """Test set with no perfect squares."""
    assert sum_perfect_squares_from_set({5, 7, 11}) == 0

def test_unique_perfect_squares():
    """Test function handles unique perfect squares correctly."""
    # Some squares can be formed in multiple ways, should be counted only once
    result = sum_perfect_squares_from_set({2, 4, 8, 16})
    assert result == 30  # 2^2 + 4^2 + 16^2

def test_invalid_input_type():
    """Test that non-set input raises TypeError."""
    with pytest.raises(TypeError):
        sum_perfect_squares_from_set([1, 2, 3])  # list instead of set

def test_invalid_set_elements():
    """Test that set with non-integer or negative elements raises TypeError."""
    with pytest.raises(TypeError):
        sum_perfect_squares_from_set({1, 2, 'a'})
    
    with pytest.raises(TypeError):
        sum_perfect_squares_from_set({1, 2, -3})

def test_large_set_of_squares():
    """Test with a larger set of potential squares."""
    large_set = set(range(1, 20))
    expected_squares = {x*x for x in large_set if x*x in large_set}
    result = sum_perfect_squares_from_set(large_set)
    assert result == sum(expected_squares)

def test_repeated_perfect_squares():
    """Test that repeated perfect squares are only counted once."""
    result = sum_perfect_squares_from_set({1, 1, 4, 4, 9, 16})
    assert result == 30  # Unique squares: 1, 4, 9, 16