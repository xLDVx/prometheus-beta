"""
Test suite for extended Fibonacci sequence generator.

Covers:
- Positive integer indices
- Negative integer indices
- Float indices
- Edge cases
- Error handling
"""

import pytest
import math
from src.fibonacci import fibonacci

def test_positive_integers():
    """Test Fibonacci sequence for positive integer indices."""
    test_cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (5, 5),
        (10, 55)
    ]
    for index, expected in test_cases:
        assert fibonacci(index) == expected

def test_negative_integers():
    """Test Fibonacci sequence for negative integer indices."""
    test_cases = [
        (-1, 1),
        (-2, -1),
        (-3, 2),
        (-4, -3),
        (-5, 5)
    ]
    for index, expected in test_cases:
        assert fibonacci(index) == expected

def test_float_indices():
    """Test Fibonacci sequence for float indices."""
    test_cases = [
        (0.5, fibonacci(0) + 0.5 * (fibonacci(1) - fibonacci(0))),
        (1.5, fibonacci(1) + 0.5 * (fibonacci(2) - fibonacci(1))),
        (2.25, fibonacci(2) + 0.25 * (fibonacci(3) - fibonacci(2)))
    ]
    for index, expected in test_cases:
        assert math.isclose(fibonacci(index), expected, rel_tol=1e-9)

def test_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        fibonacci("not a number")
    with pytest.raises(TypeError):
        fibonacci(None)
    with pytest.raises(TypeError):
        fibonacci([1, 2, 3])

def test_large_indices():
    """Test Fibonacci sequence for larger indices."""
    # Verify a few known large Fibonacci numbers
    assert fibonacci(20) == 6765
    assert fibonacci(-20) == 6765 * (-1)**21