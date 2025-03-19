import pytest
from src.ip_validator import validate_ip_address

def test_valid_ip_addresses():
    """Test valid IP addresses"""
    assert validate_ip_address('1.2.3.4') is True
    assert validate_ip_address('0.0.0.0') is True
    assert validate_ip_address('9.9.9.9') is True

def test_invalid_ip_addresses():
    """Test invalid IP addresses"""
    # Multi-digit octets
    assert validate_ip_address('10.2.3.4') is False
    assert validate_ip_address('1.20.3.4') is False
    
    # Non-digit characters
    assert validate_ip_address('a.2.3.4') is False
    assert validate_ip_address('1.b.3.4') is False
    
    # Out of range digits
    assert validate_ip_address('1.2.3.10') is False
    
    # Incorrect format
    assert validate_ip_address('1.2.3') is False
    assert validate_ip_address('1.2.3.4.5') is False

def test_edge_cases():
    """Test edge cases"""
    # Non-string inputs
    assert validate_ip_address(None) is False
    assert validate_ip_address(123) is False
    assert validate_ip_address([]) is False
    
    # Empty string
    assert validate_ip_address('') is False
    
    # Whitespace
    assert validate_ip_address(' 1.2.3.4 ') is False
    assert validate_ip_address('1. 2.3.4') is False