import pytest
from src.password_validator import validate_password

def test_valid_password():
    """Test a password that meets all complexity requirements."""
    assert validate_password("Strong1Pass!")

def test_password_too_short():
    """Test that passwords less than 8 characters are rejected."""
    assert not validate_password("Short1!")

def test_password_too_long():
    """Test that passwords longer than 64 characters are rejected."""
    long_password = "A" * 65
    assert not validate_password(long_password)

def test_missing_uppercase():
    """Test that a password without uppercase is rejected."""
    assert not validate_password("lowercase1!")

def test_missing_lowercase():
    """Test that a password without lowercase is rejected."""
    assert not validate_password("UPPERCASE1!")

def test_missing_digit():
    """Test that a password without a digit is rejected."""
    assert not validate_password("StrongPass!")

def test_missing_special_character():
    """Test that a password without a special character is rejected."""
    assert not validate_password("StrongPass123")

def test_multiple_complexity_failures():
    """Test a password that fails multiple complexity checks."""
    assert not validate_password("password")

def test_different_special_characters():
    """Test various special characters are accepted."""
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    for char in special_chars:
        assert validate_password(f"StrongPass1{char}")

def test_edge_case_passwords():
    """Test some edge case passwords."""
    assert validate_password("A1b!cdef")  # Minimal valid password
    assert validate_password("Very_Long_Password_With_Complexity_123!")  # Long valid password
    assert not validate_password("")  # Empty string
    assert not validate_password(" ")  # Just a space