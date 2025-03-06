import pytest
from src.number_extractor import extract_numbers

def test_extract_positive_integers():
    """Test extraction of positive integers"""
    assert extract_numbers("I have 42 apples") == [42]

def test_extract_multiple_integers():
    """Test extraction of multiple integers"""
    assert extract_numbers("I have 42 apples and 7 oranges") == [42, 7]

def test_extract_floats():
    """Test extraction of floating point numbers"""
    assert extract_numbers("Pi is approximately 3.14159") == [3.14159]

def test_extract_mixed_numbers():
    """Test extraction of mixed integer and float numbers"""
    assert extract_numbers("I have 42 apples and 3.14 pies") == [42, 3.14]

def test_negative_numbers():
    """Test extraction of negative numbers"""
    assert extract_numbers("Temperature is -5 and wind speed is -3.5") == [-5, -3.5]

def test_no_numbers():
    """Test case with no numbers in the string"""
    assert extract_numbers("No numbers here") == []

def test_numbers_with_text():
    """Test numbers embedded in text"""
    assert extract_numbers("abc123def456.78ghi") == [123, 456.78]

def test_empty_string():
    """Test empty string input"""
    assert extract_numbers("") == []

def test_input_types():
    """Ensure function raises TypeError for non-string input"""
    with pytest.raises(TypeError):
        extract_numbers(123)  # type: ignore