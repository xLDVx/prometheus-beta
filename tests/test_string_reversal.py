import pytest
from src.string_reversal import recursive_reverse_string

def test_basic_string_reversal():
    """Test basic string reversal"""
    assert recursive_reverse_string("hello") == "olleh"
    assert recursive_reverse_string("world") == "dlrow"

def test_mixed_case_reversal():
    """Test reversal of mixed case strings"""
    assert recursive_reverse_string("Hello World") == "dlroW olleH"
    assert recursive_reverse_string("PyThOn") == "nOhTyP"

def test_single_character():
    """Test single character reversal"""
    assert recursive_reverse_string("a") == "a"
    assert recursive_reverse_string("Z") == "Z"

def test_empty_string():
    """Test empty string reversal"""
    assert recursive_reverse_string("") == ""

def test_string_with_spaces():
    """Test string with multiple spaces"""
    assert recursive_reverse_string("  ab cd  ") == "  dc ba  "

def test_invalid_input_type():
    """Test error handling for non-string input"""
    with pytest.raises(TypeError, match="Input must be a string"):
        recursive_reverse_string(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        recursive_reverse_string(None)

def test_invalid_characters():
    """Test error handling for invalid characters"""
    with pytest.raises(ValueError, match="Input can only contain letters and spaces"):
        recursive_reverse_string("hello123")
    with pytest.raises(ValueError, match="Input can only contain letters and spaces"):
        recursive_reverse_string("hello!")
    with pytest.raises(ValueError, match="Input can only contain letters and spaces"):
        recursive_reverse_string("hello@world")