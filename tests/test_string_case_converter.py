import pytest
from src.string_case_converter import convert_to_alternating_dot_case

def test_basic_conversion():
    """Test basic string conversion to alternating dot case."""
    assert convert_to_alternating_dot_case("hello") == 'h.E.l.L.o'
    assert convert_to_alternating_dot_case("world") == 'w.O.r.L.d'

def test_uppercase_input():
    """Test conversion with uppercase input."""
    assert convert_to_alternating_dot_case("PYTHON") == 'p.Y.t.H.o.N'

def test_mixed_case_input():
    """Test conversion with mixed case input."""
    assert convert_to_alternating_dot_case("PyThOn") == 'p.Y.t.H.o.N'

def test_empty_string():
    """Test conversion of empty string."""
    assert convert_to_alternating_dot_case("") == ''

def test_single_character():
    """Test conversion of single character."""
    assert convert_to_alternating_dot_case("a") == 'a'

def test_invalid_input_type():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_dot_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_dot_case(None)

def test_special_characters():
    """Test conversion with special characters and spaces."""
    assert convert_to_alternating_dot_case("hello world!") == 'h.E.l.L.o. .W.o.R.l.D.!'