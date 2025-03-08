import pytest
from src.case_switcher import switch_cases

def test_basic_case_switching():
    """Test basic case switching for two strings of equal length."""
    assert switch_cases("Hello", "World") == "hELLOWORLD"

def test_different_length_strings():
    """Test case switching for strings of different lengths."""
    assert switch_cases("hi", "Python") == "HIPython"
    assert switch_cases("Python", "hi") == "pYTHONHI"

def test_empty_strings():
    """Test case switching with empty strings."""
    assert switch_cases("", "") == ""
    assert switch_cases("Hello", "") == "hELLO"
    assert switch_cases("", "World") == "wORLD"

def test_mixed_case_strings():
    """Test case switching with mixed case strings."""
    assert switch_cases("HeLLo", "WoRlD") == "hEllOwORLD"

def test_non_alphabetic_characters():
    """Test case switching with non-alphabetic characters."""
    assert switch_cases("123", "ABC") == "123ABC"
    assert switch_cases("!@#", "xyz") == "!@#XYZ"

def test_invalid_input_types():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError):
        switch_cases(123, "Hello")
    
    with pytest.raises(TypeError):
        switch_cases("Hello", [1, 2, 3])
    
    with pytest.raises(TypeError):
        switch_cases(None, "World")