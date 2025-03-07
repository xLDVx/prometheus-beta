import pytest
from src.string_converter import convert_to_uppercase_with_spaces

def test_basic_conversion():
    """Test basic string conversion to uppercase with spaces."""
    assert convert_to_uppercase_with_spaces("helloWorld") == "HELLO WORLD"

def test_already_uppercase_with_spaces():
    """Test string that is already uppercase with spaces."""
    assert convert_to_uppercase_with_spaces("HELLO WORLD") == "HELLO WORLD"

def test_mixed_case_with_existing_spaces():
    """Test mixed case string with existing spaces."""
    assert convert_to_uppercase_with_spaces("hello World Test") == "HELLO WORLD TEST"

def test_single_word():
    """Test single word conversion."""
    assert convert_to_uppercase_with_spaces("hello") == "HELLO"

def test_empty_string():
    """Test empty string input."""
    assert convert_to_uppercase_with_spaces("") == ""

def test_invalid_input_type():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_uppercase_with_spaces(123)

def test_camel_case_conversion():
    """Test conversion of camelCase to uppercase with spaces."""
    assert convert_to_uppercase_with_spaces("camelCaseString") == "CAMEL CASE STRING"

def test_multiple_uppercase_letters():
    """Test conversion with multiple consecutive uppercase letters."""
    assert convert_to_uppercase_with_spaces("HTTPRequest") == "HTTP REQUEST"