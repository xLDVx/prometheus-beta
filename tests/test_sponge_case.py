import pytest
from src.sponge_case import to_sponge_case

def test_basic_sponge_case():
    """Test basic string conversion to sponge case."""
    assert to_sponge_case("hello") == "HeLlO"
    assert to_sponge_case("world") == "WoRlD"

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_sponge_case("") == ""

def test_single_character():
    """Test conversion of a single character."""
    assert to_sponge_case("a") == "A"
    assert to_sponge_case("B") == "B"

def test_mixed_case_input():
    """Test input with mixed existing case."""
    assert to_sponge_case("HeLLo") == "HeLlO"

def test_non_alphabetic_characters():
    """Test string with non-alphabetic characters."""
    assert to_sponge_case("hello123world") == "HeLlO123WoRlD"
    assert to_sponge_case("!@#$%^") == "!@#$%^"

def test_invalid_input():
    """Test handling of non-string inputs."""
    with pytest.raises(TypeError):
        to_sponge_case(123)
    
    with pytest.raises(TypeError):
        to_sponge_case(None)
    
    with pytest.raises(TypeError):
        to_sponge_case(["hello"])