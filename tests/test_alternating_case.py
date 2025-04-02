import pytest
from src.alternating_case import to_alternating_case

def test_basic_alternating_case():
    """Test basic string conversion to alternating case."""
    assert to_alternating_case("hello") == "HeLlO"
    assert to_alternating_case("world") == "WoRlD"

def test_empty_string():
    """Test empty string handling."""
    assert to_alternating_case("") == ""

def test_single_character():
    """Test single character conversion."""
    assert to_alternating_case("a") == "A"
    assert to_alternating_case("B") == "b"

def test_mixed_case_input():
    """Test conversion of already mixed case strings."""
    assert to_alternating_case("HeLLo") == "HeLlO"

def test_non_alphabetic_characters():
    """Test handling of non-alphabetic characters."""
    assert to_alternating_case("hello 123!") == "HeLlO 123!"

def test_error_handling():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError):
        to_alternating_case(123)
    
    with pytest.raises(TypeError):
        to_alternating_case(None)

def test_unicode_characters():
    """Test handling of unicode characters."""
    assert to_alternating_case("héllö") == "HéLlÖ"