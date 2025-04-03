import pytest
from src.fibonacci_reverse import fibonacci_reverse

def test_fibonacci_reverse_basic():
    """Test basic functionality with various input values."""
    assert fibonacci_reverse(0) == []
    assert fibonacci_reverse(1) == [0]
    assert fibonacci_reverse(2) == [1, 0]
    assert fibonacci_reverse(5) == [5, 3, 2, 1, 0]
    assert fibonacci_reverse(7) == [13, 8, 5, 3, 2, 1, 0]

def test_fibonacci_reverse_large_input():
    """Test function with larger input values."""
    result = fibonacci_reverse(10)
    assert len(result) == 10
    assert result[0] == 55  # Verify first element
    assert result[-1] == 0  # Verify last element is 0

def test_fibonacci_reverse_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_reverse("5")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_reverse(5.5)
    
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_reverse(-1)