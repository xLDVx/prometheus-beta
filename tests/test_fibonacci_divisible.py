import pytest
from src.fibonacci_divisible import generate_modified_fibonacci

def test_generate_modified_fibonacci_basic():
    """Test basic functionality of the modified Fibonacci generator."""
    result = generate_modified_fibonacci(10)
    assert result == [1, 1, 2, 4]
    
    # Verify divisibility constraint
    for i in range(2, len(result)):
        assert (result[i-1] + result[i-2]) % 3 == 0

def test_generate_modified_fibonacci_zero():
    """Test with zero input."""
    assert generate_modified_fibonacci(0) == []

def test_generate_modified_fibonacci_one():
    """Test with input of 1."""
    assert generate_modified_fibonacci(1) == [1]

def test_generate_modified_fibonacci_two():
    """Test with input of 2."""
    assert generate_modified_fibonacci(2) == [1, 1]

def test_generate_modified_fibonacci_larger_number():
    """Test with a larger number to ensure divisibility constraint."""
    result = generate_modified_fibonacci(100)
    
    # Verify divisibility constraint
    for i in range(2, len(result)):
        assert (result[i-1] + result[i-2]) % 3 == 0

def test_generate_modified_fibonacci_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError):
        generate_modified_fibonacci(-1)
    
    with pytest.raises(ValueError):
        generate_modified_fibonacci("not a number")

def test_generate_modified_fibonacci_divisibility():
    """Comprehensive test of divisibility constraint."""
    test_cases = [
        10,   # Small number
        50,   # Medium number
        100,  # Larger number
    ]
    
    for n in test_cases:
        result = generate_modified_fibonacci(n)
        
        # Ensure first two numbers are always 1, 1
        assert result[:2] == [1, 1]
        
        # Check divisibility constraint for each window of 3 numbers
        for i in range(2, len(result)):
            assert (result[i-1] + result[i-2]) % 3 == 0, \
                f"Failed divisibility at index {i} for n={n}"