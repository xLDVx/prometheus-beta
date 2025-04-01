import pytest
from src.gcd import find_gcd

def test_gcd_basic_cases():
    """Test basic GCD calculations."""
    assert find_gcd(48, 18) == 6
    assert find_gcd(54, 24) == 6
    assert find_gcd(17, 23) == 1

def test_gcd_one_zero():
    """Test cases where one number is zero."""
    assert find_gcd(0, 5) == 5
    assert find_gcd(5, 0) == 5

def test_gcd_both_zero():
    """Test case where both numbers are zero."""
    assert find_gcd(0, 0) == 0

def test_gcd_same_number():
    """Test case where both numbers are the same."""
    assert find_gcd(7, 7) == 7

def test_gcd_type_errors():
    """Test type error handling."""
    with pytest.raises(TypeError):
        find_gcd(10.5, 20)
    with pytest.raises(TypeError):
        find_gcd("10", 20)
    with pytest.raises(TypeError):
        find_gcd([10], 20)

def test_gcd_negative_inputs():
    """Test negative input handling."""
    with pytest.raises(ValueError):
        find_gcd(-10, 20)
    with pytest.raises(ValueError):
        find_gcd(10, -20)
    with pytest.raises(ValueError):
        find_gcd(-10, -20)