import pytest
from src.fibonacci import fibonacci_sequence

def test_fibonacci_sequence_zero():
    """Test generating 0 Fibonacci numbers."""
    assert fibonacci_sequence(0) == []

def test_fibonacci_sequence_one():
    """Test generating first Fibonacci number."""
    assert fibonacci_sequence(1) == [0]

def test_fibonacci_sequence_two():
    """Test generating first two Fibonacci numbers."""
    assert fibonacci_sequence(2) == [0, 1]

def test_fibonacci_sequence_five():
    """Test generating first five Fibonacci numbers."""
    assert fibonacci_sequence(5) == [0, 1, 1, 2, 3]

def test_fibonacci_sequence_ten():
    """Test generating first ten Fibonacci numbers."""
    assert fibonacci_sequence(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_fibonacci_sequence_negative_input():
    """Test that negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_sequence(-1)

def test_fibonacci_sequence_invalid_type():
    """Test that non-integer input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_sequence("not an int")
        fibonacci_sequence(3.14)
        fibonacci_sequence(None)