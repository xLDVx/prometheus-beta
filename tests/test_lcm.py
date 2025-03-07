import pytest
from src.lcm import lcm, gcd

def test_gcd_basic():
    """Test basic GCD calculations"""
    assert gcd(48, 18) == 6
    assert gcd(54, 24) == 6
    assert gcd(17, 5) == 1

def test_gcd_zero():
    """Test GCD with zero"""
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(0, 0) == 0

def test_gcd_negative_input():
    """Test GCD with negative inputs"""
    with pytest.raises(ValueError):
        gcd(-5, 10)
    with pytest.raises(ValueError):
        gcd(5, -10)

def test_lcm_basic():
    """Test basic LCM calculations"""
    assert lcm(4, 6) == 12
    assert lcm(21, 6) == 42
    assert lcm(17, 5) == 85

def test_lcm_zero():
    """Test LCM with zero"""
    assert lcm(0, 5) == 0
    assert lcm(5, 0) == 0

def test_lcm_zero_both_inputs():
    """Test LCM when both inputs are zero"""
    with pytest.raises(ZeroDivisionError):
        lcm(0, 0)

def test_lcm_one_input():
    """Test LCM with one input being 1"""
    assert lcm(1, 5) == 5
    assert lcm(5, 1) == 5

def test_lcm_same_number():
    """Test LCM when both inputs are the same"""
    assert lcm(7, 7) == 7

def test_lcm_coprime():
    """Test LCM of coprime numbers"""
    assert lcm(17, 23) == 17 * 23