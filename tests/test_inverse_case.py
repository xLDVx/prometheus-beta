import pytest
from src.inverse_case import convert_to_inverse_case

def test_basic_inverse_case():
    """Test basic string conversion to inverse case."""
    assert convert_to_inverse_case("Hello World!") == "hELLO wORLD!"

def test_all_uppercase():
    """Test converting all uppercase string."""
    assert convert_to_inverse_case("PYTHON") == "python"

def test_all_lowercase():
    """Test converting all lowercase string."""
    assert convert_to_inverse_case("python") == "PYTHON"

def test_mixed_with_numbers_and_symbols():
    """Test conversion with numbers and symbols."""
    assert convert_to_inverse_case("Hello123 World!") == "hELLO123 wORLD!"

def test_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_inverse_case("") == ""

def test_unicode_characters():
    """Test conversion with unicode characters."""
    assert convert_to_inverse_case("HéLLó") == "hÉllÓ"

def test_invalid_input_type():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_inverse_case(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_inverse_case(None)