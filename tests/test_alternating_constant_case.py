import pytest
from src.alternating_constant_case import convert_to_alternating_constant_case

def test_basic_string_conversion():
    """Test basic string conversion to alternating constant case."""
    assert convert_to_alternating_constant_case("hello") == "HeLlO"
    assert convert_to_alternating_constant_case("world") == "WoRlD"

def test_string_with_spaces():
    """Test conversion of strings with spaces."""
    assert convert_to_alternating_constant_case("hello world") == "HeLlO WoRlD"

def test_string_with_punctuation():
    """Test conversion of strings with punctuation."""
    assert convert_to_alternating_constant_case("hello, world!") == "HeLlO, WoRlD!"

def test_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_alternating_constant_case("") == ""

def test_single_character():
    """Test conversion of a single character."""
    assert convert_to_alternating_constant_case("a") == "A"
    assert convert_to_alternating_constant_case("B") == "B"

def test_non_string_input():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_constant_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_constant_case(None)

def test_mixed_case_input():
    """Test conversion of strings with mixed existing case."""
    assert convert_to_alternating_constant_case("HeLLo") == "HeLlO"
    assert convert_to_alternating_constant_case("wORld") == "WoRlD"

def test_special_characters():
    """Test conversion of strings with special characters."""
    assert convert_to_alternating_constant_case("a1b2c3") == "A1b2C3"
    assert convert_to_alternating_constant_case("!@#$%^") == "!@#$%^"