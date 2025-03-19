import pytest
from src.fibonacci_sum_constraint import fibonacci_sum_constraint

def test_basic_sequence():
    # Basic case where k is small
    result = fibonacci_sum_constraint(5, 3)
    assert len(result) <= 5
    assert all(result[i] + result[i+1] >= 3 for i in range(len(result)-1))

def test_minimum_length():
    # Test with a small n and k
    result = fibonacci_sum_constraint(3, 5)
    assert len(result) <= 3
    assert all(result[i] + result[i+1] >= 5 for i in range(len(result)-1))

def test_large_sequence():
    # Test with a larger sequence
    result = fibonacci_sum_constraint(10, 10)
    assert len(result) <= 10
    assert all(result[i] + result[i+1] >= 10 for i in range(len(result)-1))

def test_single_element():
    # Test when n is 1
    result = fibonacci_sum_constraint(1, 5)
    assert len(result) == 1
    assert result[0] >= 5

def test_invalid_n():
    # Test invalid n values
    with pytest.raises(ValueError):
        fibonacci_sum_constraint(0, 5)
    with pytest.raises(ValueError):
        fibonacci_sum_constraint(-1, 5)
    with pytest.raises(ValueError):
        fibonacci_sum_constraint('invalid', 5)

def test_invalid_k():
    # Test invalid k values
    with pytest.raises(ValueError):
        fibonacci_sum_constraint(5, -1)
    with pytest.raises(ValueError):
        fibonacci_sum_constraint(5, 'invalid')

def test_impossible_sequence():
    # Test a case where no sequence can be generated
    with pytest.raises(ValueError, match="Unable to generate"):
        fibonacci_sum_constraint(5, 10**9)

def test_consecutive_sum_constraint():
    # Ensure consecutive elements satisfy the sum constraint
    for k in [2, 5, 10, 20]:
        result = fibonacci_sum_constraint(6, k)
        for i in range(len(result)-1):
            assert result[i] + result[i+1] >= k, f"Failed for k={k}"