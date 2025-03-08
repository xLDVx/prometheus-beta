import pytest
from src.prime_checker import is_prime

def test_prime_numbers():
    """Test known prime numbers"""
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 997, 991]
    for num in prime_numbers:
        assert is_prime(num) is True, f"{num} should be prime"

def test_non_prime_numbers():
    """Test known non-prime numbers"""
    non_prime_numbers = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 999]
    for num in non_prime_numbers:
        assert is_prime(num) is False, f"{num} should not be prime"

def test_input_validation():
    """Test input validation"""
    # Test below range
    with pytest.raises(ValueError, match="Input must be between 2 and 1000"):
        is_prime(1)
    
    # Test above range
    with pytest.raises(ValueError, match="Input must be between 2 and 1000"):
        is_prime(1001)
    
    # Test non-integer input
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_prime(3.14)
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_prime("10")

def test_edge_cases():
    """Test edge cases at the boundaries"""
    assert is_prime(2) is True, "2 is a prime number"
    assert is_prime(1000) is False, "1000 is not a prime number"