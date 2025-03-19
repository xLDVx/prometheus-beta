import pytest
from src.factor_counter import count_factors

def test_factor_count_small_numbers():
    """Test factor counting for small numbers."""
    assert count_factors(1) == 1
    assert count_factors(4) == 3  # 1, 2, 4
    assert count_factors(6) == 4  # 1, 2, 3, 6
    assert count_factors(12) == 6  # 1, 2, 3, 4, 6, 12

def test_factor_count_prime_numbers():
    """Test factor counting for prime numbers."""
    assert count_factors(7) == 2  # 1 and 7
    assert count_factors(11) == 2  # 1 and 11
    assert count_factors(17) == 2  # 1 and 17

def test_factor_count_large_number():
    """Test factor counting for a larger number."""
    assert count_factors(100) == 9  # 1, 2, 4, 5, 10, 20, 25, 50, 100

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        count_factors("not an integer")
    
    with pytest.raises(ValueError):
        count_factors(0)
    
    with pytest.raises(ValueError):
        count_factors(-5)

def test_perfect_square():
    """Test factor counting for perfect squares."""
    assert count_factors(9) == 3  # 1, 3, 9
    assert count_factors(16) == 5  # 1, 2, 4, 8, 16