import pytest
from src.prime_finder import find_primes_in_range

def test_basic_prime_range():
    """Test finding primes in a basic range"""
    assert find_primes_in_range(10, 20) == [11, 13, 17, 19]

def test_small_prime_range():
    """Test finding primes in a small range"""
    assert find_primes_in_range(2, 10) == [2, 3, 5, 7]

def test_single_prime():
    """Test finding a single prime number"""
    assert find_primes_in_range(17, 17) == [17]

def test_no_primes_range():
    """Test range with no primes"""
    assert find_primes_in_range(24, 26) == []

def test_lower_bound_larger_than_upper_bound():
    """Test that ValueError is raised when lower bound is larger"""
    with pytest.raises(ValueError, match="Lower bound must be less than or equal to upper bound"):
        find_primes_in_range(20, 10)

def test_negative_range():
    """Test range with negative numbers"""
    assert find_primes_in_range(-10, 10) == [2, 3, 5, 7]

def test_zero_and_one_range():
    """Test range including zero and one"""
    assert find_primes_in_range(0, 5) == [2, 3, 5]

def test_invalid_input_types():
    """Test that TypeError is raised for non-integer inputs"""
    with pytest.raises(TypeError, match="Inputs must be integers"):
        find_primes_in_range("10", 20)
    
    with pytest.raises(TypeError, match="Inputs must be integers"):
        find_primes_in_range(10, "20")
    
    with pytest.raises(TypeError, match="Inputs must be integers"):
        find_primes_in_range(10.5, 20.5)