import pytest
from src.gcd import recursive_gcd

def test_basic_gcd():
    """Test basic GCD calculations"""
    assert recursive_gcd(48, 18) == 6
    assert recursive_gcd(54, 24) == 6
    assert recursive_gcd(100, 75) == 25

def test_zero_cases():
    """Test cases involving zero"""
    assert recursive_gcd(0, 5) == 5
    assert recursive_gcd(5, 0) == 5
    assert recursive_gcd(0, 0) == 0

def test_same_number():
    """Test GCD of same number"""
    assert recursive_gcd(7, 7) == 7
    assert recursive_gcd(13, 13) == 13

def test_coprime():
    """Test coprime numbers"""
    assert recursive_gcd(17, 23) == 1
    assert recursive_gcd(8, 9) == 1

def test_negative_input_error():
    """Test that negative inputs raise ValueError"""
    with pytest.raises(ValueError):
        recursive_gcd(-10, 5)
    with pytest.raises(ValueError):
        recursive_gcd(10, -5)
    with pytest.raises(ValueError):
        recursive_gcd(-10, -5)

def test_type_error():
    """Test that non-integer inputs raise TypeError"""
    with pytest.raises(TypeError):
        recursive_gcd(10.5, 5)
    with pytest.raises(TypeError):
        recursive_gcd(10, '5')
    with pytest.raises(TypeError):
        recursive_gcd([10], 5)