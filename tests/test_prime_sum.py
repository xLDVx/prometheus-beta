import pytest
from src.prime_sum import sum_primes_under_n

def test_sum_primes_under_small_n():
    """Test sum of primes for small input"""
    assert sum_primes_under_n(10) == 17  # 2 + 3 + 5 + 7

def test_sum_primes_under_larger_n():
    """Test sum of primes for a larger input"""
    assert sum_primes_under_n(20) == 77  # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19

def test_sum_primes_under_zero():
    """Test that function returns 0 for inputs less than 2"""
    assert sum_primes_under_n(0) == 0
    assert sum_primes_under_n(1) == 0
    assert sum_primes_under_n(2) == 0

def test_invalid_input_type():
    """Test that invalid input types raise ValueError"""
    with pytest.raises(ValueError, match="Input must be an integer"):
        sum_primes_under_n("10")
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        sum_primes_under_n(3.14)
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        sum_primes_under_n(None)

def test_sum_primes_large_n():
    """Test sum of primes for a larger number"""
    assert sum_primes_under_n(100) == 1060  # Sum of primes less than 100