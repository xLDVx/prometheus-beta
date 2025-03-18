import pytest
from src.fibonacci_utils import fibonacci, fibonacci_sum

def test_fibonacci_basic_sequence():
    """Test basic Fibonacci sequence generation"""
    assert fibonacci(10) == [1, 1, 2, 3, 5, 8]
    assert fibonacci(1) == [1]
    assert fibonacci(0) == []

def test_fibonacci_edge_cases():
    """Test edge cases for Fibonacci sequence generation"""
    with pytest.raises(ValueError):
        fibonacci(-1)
    with pytest.raises(ValueError):
        fibonacci("invalid")

def test_fibonacci_sum_basic():
    """Test basic Fibonacci sum functionality"""
    assert fibonacci_sum([5]) == 11  # 1 + 1 + 2 + 3 + 5
    assert fibonacci_sum([10]) == 19  # 1 + 1 + 2 + 3 + 5 + 8
    assert fibonacci_sum([2, 5]) == 11
    assert fibonacci_sum([1]) == 1

def test_fibonacci_sum_edge_cases():
    """Test edge cases for Fibonacci sum"""
    assert fibonacci_sum([]) == 0
    
    with pytest.raises(ValueError):
        fibonacci_sum([-1, 5])
    
    with pytest.raises(ValueError):
        fibonacci_sum([1, "invalid"])

def test_fibonacci_sum_multiple_inputs():
    """Test Fibonacci sum with multiple inputs"""
    assert fibonacci_sum([3, 7, 10]) == 19  # Fibonacci up to 10
    assert fibonacci_sum([100]) == 231  # Fibonacci up to 100