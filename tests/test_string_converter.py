import pytest
from src.string_converter import to_alternating_path_case

def test_to_alternating_path_case_normal():
    """Test basic string conversion."""
    assert to_alternating_path_case("hello world") == "Hello/world"
    assert to_alternating_path_case("python is awesome") == "Python/is/Awesome"

def test_to_alternating_path_case_single_word():
    """Test single word input."""
    assert to_alternating_path_case("hello") == "Hello"

def test_to_alternating_path_case_empty_string():
    """Test empty string input."""
    assert to_alternating_path_case("") == ""

def test_to_alternating_path_case_multiple_spaces():
    """Test input with multiple spaces."""
    assert to_alternating_path_case("  hello   world  ") == "Hello/world"

def test_to_alternating_path_case_invalid_input():
    """Test invalid input types."""
    with pytest.raises(TypeError):
        to_alternating_path_case(123)
    
    with pytest.raises(TypeError):
        to_alternating_path_case(None)

def test_to_alternating_path_case_mixed_case():
    """Test input with mixed case."""
    assert to_alternating_path_case("HeLLo WoRLd") == "Hello/world"